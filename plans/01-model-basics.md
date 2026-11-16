# 阶段 1：从已读 GPT-2 / Qwen2.5 到 Qwen3 实现（第 1–2 周）

状态：计划，尚未执行。建议预算约 50 小时，含环境、数值对齐、复盘和项目准备。首周按 [7 天任务](week-01.md)，第二周补齐以下验收。

## 先知道自己要解释什么

1. 给定 token 序列，为什么每个位置都能预测下一个 token？训练和生成如何不同？
2. 输入 IDs、attention mask、position IDs、labels 的职责分别是什么？
3. 为什么 GQA 可以降低 KV cache 开销？Qwen3 的 QK-Norm 在哪里？
4. 为什么模型能前向运行，不代表权重映射、loss 和 cache 都正确？

不会时才补对应基础：张量变形与广播、softmax、交叉熵、autograd、causal attention。优先用 2 个 token、2 个 head 的手工例子，不重开完整入门课程。

## 阅读和源码入口

- [Qwen3 官方仓库](https://github.com/QwenLM/Qwen3)：阅读 dense 结构、推理和 thinking/non-thinking 使用说明。
- [Qwen3 技术报告](https://arxiv.org/abs/2505.09388)：先读模型结构和训练流程；MoE 与大规模训练细节留作选读。
- [Qwen3-0.6B 模型卡](https://huggingface.co/Qwen/Qwen3-0.6B)：核查安装要求、权重、配置、模板和推理示例。
- [Transformers Qwen3 文档](https://huggingface.co/docs/transformers/model_doc/qwen3)；[参考源码](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen3/modeling_qwen3.py)。

网页链接是材料入口，实际对齐时记录本地安装版本及其对应 commit；不把 main 分支当作固定参考。先看目标 checkpoint 的 config 与 state_dict，再写结构。hidden_size、head_dim、head 数、bias、norm epsilon、权重共享和 RoPE 配置均从实际配置获取。

## 最小实践顺序

| 顺序 | 亲手做什么 | 怎样检查 |
| --- | --- | --- |
| 1 | 官方模型加载、模板渲染、短文本生成 | 固定 revision、5 条 prompts 和生成配置 |
| 2 | shifted cross-entropy、padding 和 labels mask | 与参考 loss 对齐；更换 padding 后有效 token 结果一致 |
| 3 | RMSNorm、RoPE、GQA、QK-Norm、SwiGLU | 固定小 tensor，逐模块比较输出与 shape |
| 4 | 单个 decoder block 与权重映射 | 比较 norm、Q/K/V、attention、MLP 和 block 输出 |
| 5 | 完整 dense 前向与 greedy generation | 同输入比较最终 norm、logits；输出差异追到最早偏差层 |
| 6 | KV cache prefill/decode | 与逐步完整重算的有效位置 logits 对齐 |
| 7 | 小随机模型训练 | 20–50 条短样本过拟合，确认 loss 与生成行为一起变化 |

建议后续代码路径：src/model/、tests/model/、configs/model/。这里只约定产物位置，不预先把关键模块实现好。

第一轮用显式 attention 便于检查，确认正确后再比较 SDPA 等实现。FP32、eval、固定输入先对齐；检查 dropout、norm epsilon、mask、RoPE 旋转约定、transpose、权重绑定以及目标版本的行为。先预设容差，再记录 max absolute / relative error；近零元素的相对误差不能单独作为失败依据。低精度和不同 kernel 另做容差实验。

tiny overfit 使用随机初始化、少层小维度且配置合法的模型，目的是检查反向与训练链路。预训练 0.6B 用于权重/推理对齐和后续 LoRA；不要求从头训练出同等能力。训练 loss 降低后检查样本生成，并保存 loss、种子、配置和 checkpoint。

## 第二周建议节奏（25 小时）

- 全模型权重与前向对齐：8 小时。
- cache、padding、batch 一致性和失败定位：4 小时。
- tiny overfit 与重载 checkpoint：4 小时。
- 读 LoRA、准备项目数据、测原模型基线：5 小时。
- 复盘与岗位要求整理：4 小时。

## 第 3–5 周怎样接着读

dense 基础通过后按 [演进地图](model-evolution.md) 进入 MoE、MLA、稀疏/线性/混合注意力和当前模型对比。每个分支至少一个机制练习；不要求在 16GB 上加载所有大规格模型。项目基线和数据准备与阅读并行。

## 通过标准

- [ ] 解释 token → embedding → block → logits → loss → sampling 的完整路径。
- [ ] 对照 GPT-2 / LLaMA / Qwen2.5 / Qwen3 说明结构、数据与训练变化。
- [ ] 关键模块、单 block、完整前向和 cache 有数值记录，失败项明确。
- [ ] 完成 tiny overfit，并能保存、重载、复现输出。
- [ ] 有冻结的模型/参考版本、环境说明和运行命令。
- [ ] 第 2 周完成项目数据候选，第 5 周前完成基线。

SFT 阶段使用已验证的成熟模型实现训练，自己的架构练习独立保留。
