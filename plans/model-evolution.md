# 从 GPT-2 / Qwen2.5 接着读：开源 LLM 演进与配套练习

更新：2026-11-16。先覆盖代表性机制，再追当前模型差异。下面是学习依赖与对照路线，不是模型排名，也不表示所有家族具有直接继承关系。

## 三种阅读深度

- **A：精读代码与公式**。dense 主线选一套代码深读到底；MoE、MLA、混合注意力分别深读关键模块，不逐个家族全文重写。
- **B：差异阅读**。每个模型约 2–4 小时，只读相对已掌握模型的变化、证据与限制，形成一页比较。
- **C：前沿扫描**。每家族约 30–60 分钟核查官方模型卡、开放范围、报告与部署要求；本轮选一个变化深入，其余入后续清单。

每次比较分开看：架构、tokenizer/数据、预训练预算、后训练目标、推理系统、评估设置。benchmark 更高不能单独证明某一模块更好。

## 代表路线与练习

| 顺序/时间 | 代表模型与官方材料 | 核心变化/阅读问题 | 实践与验收 | 深度 |
| --- | --- | --- | --- | --- |
| 第 1 周起点 | 已读 GPT-2 与 Qwen2.5 代码 | 能否闭卷解释 forward、mask、shifted CE、生成？ | 标出自己已懂/不懂的函数；复现一条 loss | 回顾 |
| 第 1 周 | [LLaMA](https://arxiv.org/abs/2302.13971)、[Llama 2](https://arxiv.org/abs/2307.09288) | 相对 GPT-2：RMSNorm、RoPE、SwiGLU；哪些规格使用 GQA？ | 做 norm/RoPE/MLP 小 tensor 对照；按具体 config 比 head 数 | A：dense 主线 |
| 第 1–2 周 | [Qwen2](https://arxiv.org/abs/2407.10671)、[Qwen2.5](https://arxiv.org/abs/2412.15115)、[Llama 3](https://arxiv.org/abs/2407.21783) | 已读结构之外，词表、数据配比、长上下文、后训练改变了什么？ | 对照 config/模板；估算参数/cache；不同 tokenizer 的长度只作诊断 | B |
| 第 2 周 | [Qwen3](https://github.com/QwenLM/Qwen3)、[报告](https://arxiv.org/abs/2505.09388) | dense/MoE、QK-Norm、thinking/non-thinking、训练阶段 | dense block → 权重/前向/cache 对齐 → tiny overfit | A |
| 第 3 周 | [Mistral 7B](https://arxiv.org/abs/2310.06825)、[Mixtral](https://arxiv.org/abs/2401.04088) | 局部注意力与稀疏专家；总参数/激活参数/驻留权重区别 | 4 专家 top-2 toy MoE，与逐 token 朴素组合对齐；统计专家负载 | B + MoE 模块 A |
| 第 3 周 | [DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2)、[V3](https://github.com/deepseek-ai/DeepSeek-V3) | MLA、细粒度/共享专家、负载均衡、MTP；V2 到 V3 哪些变化？ | MLA 小矩阵压缩/解压 shape 验证；计算缓存量；解释位置分支，列出 toy 简化 | A：MLA；其余 B |
| 第 4 周 | [Mamba](https://arxiv.org/abs/2312.00752)、[Qwen3.5 实现文档](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/qwen3_5.md)、[小规格模型](https://huggingface.co/Qwen/Qwen3.5-0.8B) | 状态空间、线性注意力、full attention 有何不同？混合层如何配置？ | 先实现简单线性注意力 recurrence，与它自己的显式矩阵形式对齐；再定位实际 Gated DeltaNet 更新 | B + 一个状态更新模块 A |
| 第 4 周 | [Kimi Linear](https://github.com/MoonshotAI/Kimi-Linear) | KDA 与混合注意力；与上一种线性方法的区别 | 对照官方 state 更新的输入/输出/缓存；测小规格 state/cache 随长度变化 | B |
| 第 5 周 | [当前官方材料快照](../papers/current-models.md) | Qwen3.8、DeepSeek-V4.1、Kimi K3.1 等相对前代新增什么？哪些仅改变数据/后训练？ | 一页差异卡；追一个具体模块/config；大规格不要求本地加载 | C，选一个升 B |
| 第 6–7 周 | [LoRA](https://arxiv.org/abs/2106.09685)、已读 [InstructGPT](https://arxiv.org/abs/2203.02155)、[DPO](https://arxiv.org/abs/2305.18290) | 参数适配、监督数据、偏好优化分别如何改变行为？ | LoRA/SFT、监督 mask、DPO 数值和短训练 | A：loss 与训练路径 |
| 第 8–10 周 | [DeepSeekMath](https://arxiv.org/abs/2402.03300)、[R1](https://arxiv.org/abs/2501.12948) | GRPO、数据筛选、蒸馏、推理预算；哪些收益需要独立验证？ | toy GRPO → 真实小训练 → 正确率与成本对照 | A：核心计算 |
| 每周选读 | [Gemma](https://ai.google.dev/gemma)、[Mistral 官方](https://mistral.ai/news)、[OLMo](https://allenai.org/olmo) 等家族 | 是否带来不同结构、数据开放/训练可复现性或后训练方法？ | 用同一差异卡归类；重复机制不追加完整实现 | C |

LLaMA 1/2/3、Qwen2/2.5/3 的整条线不都做完整复现：以一个 Qwen dense 实现为载体，把其他模型的重要变化放进可控模块实验。已读 Qwen2.5 的内容可以快速通过，省下的时间用于后续变化。

## 五个必做机制练习

1. **dense 与 cache**：GPT-2/LLaMA/Qwen 差异表、模块/前向误差、cache 与重算对齐、tiny overfit。
2. **MoE**：router、top-k、专家输出加权、负载分布、梯度检查；吞吐取决于实现，不把 toy 结果直接外推生产系统。
3. **MLA**：按原公式列出维度、压缩缓存与位置分支。小矩阵验证只证明代数/shape，不宣称复现生产 kernel 和报告吞吐。
4. **长上下文与混合注意力**：局部/full mask、简单 recurrence 的显式/递推对齐，再追实际 Delta/KDA 公式。简单线性注意力练习不标记为完整 KDA 复现。
5. **同任务模型比较**：固定任务、提示语义、解码预算和指标，比较两个能运行的小模型；记录 tokenizer/模板、训练来源和模式差异，不能把能力差全归因于结构。

建议记录到 experiments/architecture/，编号分别为 dense-cache、moe、mla、hybrid-attention、model-comparison。这里只规定后续产物，未执行实验。

## 预训练与后训练知识怎样穿插

第 2 周读 [Chinchilla](https://arxiv.org/abs/2203.15556) 的计算预算结论及适用假设，再从 Llama/Qwen 报告中比较数据过滤、去重、配比和长上下文训练。可用自己准备的小文本集练去重、长度统计和 token 计数，但不由此声称掌握大规模预训练。

InstructGPT 已完成阅读，保留流程图查漏；SFT、DPO、GRPO 随训练阶段逐步落实。最新 agentic 模型还需区分模型能力与工具/harness 贡献，个人项目先加确定性的优惠计算工具作为对照。

## 每个模型的一页差异卡

复制 [笔记模板](../notes/paper-template.md)，至少记录：

- 模型/版本、官方来源、报告版本、开放权重/代码/数据范围及许可证。
- 比较对象；哪些是架构变化，哪些是数据、训练、推理变化。
- 关键公式与源码函数/config 字段，输入输出 shape。
- 作者证据及实验设置；自己实际验证了什么。
- 总参数/激活参数、cache/state、成本与适用任务；未公开的信息写未知。
- 一个可复现实验，或明确为何本轮只阅读。

## “补到最新”的维护方式

先完成 [当前快照](../papers/current-models.md)，再每周用 1 小时看官方公告和模型卡。只在出现新的结构、训练或评估问题时深入；同配方的小版本用一行补充。允许学习时前沿继续变化，不以“所有模型读完”作为开始项目的条件。
