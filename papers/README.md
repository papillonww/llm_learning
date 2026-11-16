# 模型演进驱动的阅读顺序

更新：2026-11-16。已读 GPT-2 / Qwen2.5 系列代码及 InstructGPT。先看 [演进地图](../plans/model-evolution.md)，按关键变化补齐知识，每段配小练习；训练与完整项目按 [总路线](../plans/roadmap.md) 推进。

## 先读什么，再练什么

| 阶段 | 材料 | 阅读目标 | 对应实践 |
| --- | --- | --- | --- |
| 已读/查漏 | [InstructGPT](https://arxiv.org/abs/2203.02155) | 三阶段数据、模型角色、目标与能力保持 | 流程图、token 到 SFT loss；不用整篇重读 |
| 第 1 周 | [LLaMA](https://arxiv.org/abs/2302.13971)、[Llama 2](https://arxiv.org/abs/2307.09288) | 连接已读 GPT-2 / Qwen2.5，读 norm、RoPE、MLP 与 head/cache 差异 | 小 tensor 验证与一页结构表 |
| 第 2 周 | [Qwen3](https://arxiv.org/abs/2505.09388)、[官方仓库](https://github.com/QwenLM/Qwen3) | dense 实现主载体；QK-Norm、配置、模板与训练流程 | block、权重、前向/cache 对齐和 tiny overfit |
| 第 2 周差异阅读 | [Qwen2.5](https://arxiv.org/abs/2412.15115)、[Llama 3](https://arxiv.org/abs/2407.21783)、[Chinchilla](https://arxiv.org/abs/2203.15556) | 数据、tokenizer、训练量、后训练与计算预算 | 小文本去重/token 统计、配置与数据差异卡 |
| 第 3 周 | [Mistral 7B](https://arxiv.org/abs/2310.06825)、[Mixtral](https://arxiv.org/abs/2401.04088)、[DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2)、[V3](https://github.com/deepseek-ai/DeepSeek-V3) | 局部注意力、MoE、MLA、负载均衡、MTP | toy MoE、MLA 维度/cache 验证 |
| 第 4 周 | [Qwen3.5 实现文档](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/qwen3_5.md)、[Kimi Linear](https://github.com/MoonshotAI/Kimi-Linear) | 线性/混合注意力、状态更新、长上下文 | recurrence 与显式计算对齐、缓存测量 |
| 第 5 周 | [本次官方材料快照](current-models.md) | 将历史机制接到当前公开模型，区分开放范围 | 两份当前模型差异卡、一个新模块/config 跟踪 |
| 第 6 周 | [LoRA](https://arxiv.org/abs/2106.09685) | 低秩更新、初始化、参数与显存 | 单层 LoRA、监督 mask、SFT |
| 第 7 周 | [DPO](https://arxiv.org/abs/2305.18290) | 偏好模型、KL 约束推导、回复 log-prob | 人工 tensor/梯度、框架对齐、短训练 |
| 第 8–10 周 | [DeepSeekMath](https://arxiv.org/abs/2402.03300)、[DeepSeek-R1](https://arxiv.org/abs/2501.12948) | GRPO、数据/训练阶段、蒸馏与推理预算 | toy 更新、真实小训练、独立评估 |
| 专题选读 | [Doc-to-LoRA](https://arxiv.org/abs/2602.15902)、[AlphaEdit](https://arxiv.org/abs/2410.02355) | 只有选知识内化/知识编辑项目时深入 | 小范围适配与能力保持，不要求超网络 |

## 源码与工具

| 用途 | 官方入口 | 核查重点 |
| --- | --- | --- |
| 起步模型 | [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | 配置、模板、thinking 模式、兼容版本 |
| 参考结构 | [Transformers Qwen3](https://huggingface.co/docs/transformers/model_doc/qwen3) | 实际安装版本的 forward/cache/loss |
| 后续小规格 | [Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | 文本路径、混合层、不同加载类与依赖 |
| 参数适配 | [PEFT LoRA](https://huggingface.co/docs/peft/developer_guides/lora) | target modules、初始化、缩放、保存加载 |
| SFT | [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) | 模板、assistant/completion 监督、截断、packing |
| DPO | [TRL DPOTrainer](https://huggingface.co/docs/trl/dpo_trainer) | reference、loss 类型、beta、回复 log-prob |
| GRPO | [TRL GRPOTrainer](https://huggingface.co/docs/trl/grpo_trainer) | rollout、reward、归一化、KL、mask、更新 |
| RL 补课 | [Spinning Up PPO](https://spinningup.openai.com/en/latest/algorithms/ppo.html) | policy gradient、ratio、clipping |
| 部署 | [vLLM](https://docs.vllm.ai/) | 模型/设备支持、服务、采样与性能 |

在线文档会变化；实验记录实际包版本、模型 revision、对应源码和关键默认值。一个家族的后续版本不一定采用相同结构、模板或模型类。

## 已下载 PDF

以下编号用于历史下载追溯，不代表当前阅读顺序。

| 材料 | 本地文件 |
| --- | --- |
| InstructGPT | [PDF](pdf/01-instructgpt.pdf) |
| DeepSeekMath | [PDF](pdf/02-deepseekmath.pdf) |
| LoRA | [PDF](pdf/03-lora.pdf) |
| DPO | [PDF](pdf/04-dpo.pdf) |
| DeepSeek-R1 | [PDF](pdf/05-deepseek-r1.pdf) |
| Chinchilla | [PDF](pdf/06-chinchilla.pdf) |
| DeepSeek-V3 | [PDF](pdf/07-deepseek-v3.pdf) |
| Doc-to-LoRA | [PDF](pdf/08-doc-to-lora.pdf) |
| AlphaEdit | [PDF](pdf/09-alphaedit.pdf) |

这 9 篇的来源、下载时间、大小、SHA256 保存在 [manifest](manifest.json)，本次不改写历史元数据。新增在线材料未下载，不标记为已有 PDF。精读时记录实际论文版本；权利归原作者/权利人。

笔记用 [论文模板](../notes/paper-template.md)，跨模型比较用 [模型差异卡](../notes/model-comparison-template.md)，实验用 [实验模板](../experiments/template.md)。进度在 [PROGRESS.md](../PROGRESS.md) 中分别记录。
