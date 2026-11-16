# 当前公开模型材料：2026-11-16 核验快照

本页用于让历史阅读接到当前公开进展，是本次能核验到的代表样本，不是全量发布目录或性能排名。以下官方页面于 2026-11-16 检查；“核验日期”不是模型发布日期。只核对材料和公开状态，未下载权重、运行推理或独立复现分数。

## 本次核验到的后续模型

| 官方入口 | 本次确认与阅读用途 | 本轮练习 |
| --- | --- | --- |
| [Qwen3.8-27B 模型卡](https://huggingface.co/Qwen/Qwen3.8-27B)、[config](https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/config.json) | 官方提供后训练模型权重与配置；对照 Qwen3.5/3.6 读新增训练、工具与推理设置 | 阅读/config 对照，大规格不列为 16GB 训练目标 |
| [Qwen3.5-0.8B 模型卡](https://huggingface.co/Qwen/Qwen3.5-0.8B)、[Transformers 说明](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/qwen3_5.md) | 有小规格公开材料；混合注意力适合连接 dense 与状态更新学习 | 环境支持时跑文本路径；与 Qwen3-0.6B 作任务比较，避免结构因果归因 |
| [DeepSeek-V4.1-Flash 模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | 官方说明 CED、CSA2、KV 压缩与后训练流程；接在 V2/V3 的 MLA 阅读之后 | 选一项画数据流/缓存图，大模型只做缩小机制实验 |
| [Kimi-K3.1-Pro 模型卡](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/README.md) | 官方给出 MoE、KDA 与 Gated DSA 等结构和公开权重信息 | 先读 Kimi Linear，再理解混合模块组合；不安排完整加载 |
| [GLM-5.3 官方公告](https://z.ai/blog/glm-5.3) | 官方有公开权重发布说明；具体权重文件、许可证、实现要从公告链接逐项核对 | 本轮只做一页家族对照，下载与代码级复核待做 |

Qwen 新版本不能统一沿用早期 Qwen3 的 AutoModel 类、模板或 thinking 开关；按具体 checkpoint 的模型卡和固定版本核查。多模态模型这里只学语言路径与共用训练方法，视觉编码与视频生成不纳入本轮必做。

## 如何读本页

1. 前 2 周使用 Qwen3-0.6B 建立可理解的 dense 载体，不把它标记为当前最新模型。
2. 第 3–4 周理解 MoE、MLA 与混合注意力，再读上表中相关的新模型。
3. 第 5 周选择两个家族详细比较，再选一个变化追 config/源码。源码未公开、原理未披露时如实写未知。
4. 大模型公开卡可供阅读；硬件不够时跑缩小模块，不能把 API 调用、量化运行和完整训练混写成一种经验。

## 快照更新字段

每次更新记录：检查日期、官方来源、模型版本/发布日期（若明确给出）、权重 revision、代码 commit、许可证、开放数据范围、新增机制、需要的实践、核验状态。发布日期不明确时留空，不用页面抓取时间替代。

本次新增在线材料未进入 [历史 PDF manifest](manifest.json)，也不修改已有 9 篇 PDF 的下载时间和哈希。
