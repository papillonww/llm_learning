"""Download official arXiv PDFs; resume valid local files and record hashes."""
import hashlib
import json
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = ROOT / "papers" / "manifest.json"
items = json.loads(manifest.read_text(encoding="utf-8"))
failed = []
for item in items:
    target = ROOT / "papers" / item["file"]
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        if not target.exists():
            req = urllib.request.Request(item["pdf_url"], headers={"User-Agent": "LLM-Learning-PaperArchive/1.0"})
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read()
                final_url = response.url
            if not data.startswith(b"%PDF-") or len(data) < 1000:
                raise ValueError("Response is not a valid PDF download")
            target.write_bytes(data)
            item["downloaded_at_utc"] = datetime.now(timezone.utc).isoformat()
            item["resolved_url"] = final_url
            time.sleep(1)
        data = target.read_bytes()
        if not data.startswith(b"%PDF-"):
            raise ValueError("Local file is not a PDF")
        item.update(download_status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        item.pop("error", None)
        print(item["slug"], len(data), "bytes", flush=True)
    except Exception as exc:
        item.update(download_status="failed", error=str(exc))
        failed.append(item["slug"])
        print(item["slug"], "FAILED", str(exc), flush=True)
    manifest.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if failed:
    raise SystemExit("Failed downloads: " + ", ".join(failed))
