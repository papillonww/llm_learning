# LLM 学习与实践

面向有约 1.5 年营销算法经验、读过 GPT-2 与 Qwen2.5 系列代码的工程师，沿模型演进补齐 LLM 知识，并积累训练、评估和项目经验。

更新：2026-11-16。InstructGPT 论文已读完（用户确认）。主线采用约 14 周、每周 25 小时；视频生成按独立计划安排。阅读、实现和训练分别记录，不把模型清单当作已掌握知识。

## 从这里开始

1. 读 [总路线](plans/roadmap.md)，了解模型演进、练习与项目如何衔接。
2. 对照 [模型演进地图](plans/model-evolution.md)，从 GPT-2 / Qwen2.5 已读代码出发，按“历史关键变化 + 当前模型对比”学习。
3. 今天执行 [接下来 7 天](plans/week-01.md) 的第 1 天；InstructGPT 只做复述与查漏，随后进入 LLaMA / Qwen 的结构差异。
4. 按 [dense 模型实现](plans/01-model-basics.md)、[SFT / DPO](plans/02-sft-dpo.md)、[LLM RL](plans/03-rl.md) 推进，每阶段都有小规模验证。
5. 从第一周准备 [营销规则理解与优惠计算项目](plans/project.md)，最后完成 [部署与交付](plans/04-delivery.md)。
6. 新模型看 [本次核验快照](papers/current-models.md)，具体阅读见 [材料顺序](papers/README.md)，实际进度记在 [PROGRESS.md](PROGRESS.md)。

阅读一代模型时固定回答：相对前代改了什么 → 解决什么瓶颈 → 公式与代码在哪里 → 如何做最小验证 → 对训练和推理有什么影响。

## 学习范围

- 广度：覆盖 dense、MoE、MLA、稀疏/线性/混合注意力、预训练数据、SFT、偏好优化、推理 RL、工具使用与部署的代表路线。
- 深度：精读少量核心代码，做模块级实验，选一个小模型完成训练闭环；其他家族用差异表比较。
- 前沿：截至 2026-11-16 核验官方来源，包括 Qwen3.8、DeepSeek-V4.1-Flash、Kimi-K3.1-Pro 等已公开材料；不把 Qwen3 当作最新终点，也不声称穷尽所有模型。
- 实践：一个架构实验合集 + 一个营销相关后训练项目；RL 用可验证短答案起步。
- 硬件：原计划记录 RTX 5080 16GB；在实际训练设备核对环境和显存，大模型用于阅读与缩小模块实验。
- 目标：优先建立可迁移的 LLM 算法能力，探索后训练、数据评估、营销/推荐与 LLM 交叉岗位；岗位选择随实际实验与面试反馈调整。

## 仓库内容

| 路径 | 用途 |
| --- | --- |
| plans/roadmap.md | 14 周主线、每周预算及 12 周压缩方法 |
| plans/model-evolution.md | 代表模型、关键变化、源码阅读和配套练习 |
| plans/week-01.md | 从已读代码与 InstructGPT 接续的 7 天任务 |
| plans/01-model-basics.md 至 04-delivery.md | 分阶段实践与验收 |
| plans/project.md | 复用 SFT/RL 学习的营销项目 |
| papers/ | 材料来源、当前核验快照及历史 PDF |
| notes/、experiments/ | 笔记和实验模板 |
| PROGRESS.md | 实际状态和下一步 |

论文、模型与代码的权利和许可由各自官方来源说明。本仓库中的安排是个人学习材料。
