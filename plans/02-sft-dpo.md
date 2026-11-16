# 阶段 2–3：SFT、评估与 DPO（第 6–7 周）

状态：计划，尚未执行。模型实现和数值对齐用于理解；这里用 Transformers、PEFT、TRL 等成熟实现训练，固定实际使用的版本与默认设置。

## 第 6 周：先把 SFT 数据和监督搞对

**入门问题**：InstructGPT 中 SFT 更新了什么？一条多轮对话如何变成训练样本？prompt token、assistant token、padding 分别如何参与 loss？

**阅读**：[LoRA](https://arxiv.org/abs/2106.09685) 的更新公式、初始化和实验；[PEFT LoRA 指南](https://huggingface.co/docs/peft/developer_guides/lora)；[TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)。只读当前版本实际用到的参数与数据格式。

**实践**：

1. 使用阶段 1 跑通的小型 dense 模型，先确认现成基座对任务有基本能力。模板和 thinking 设置与推理基线保持一致。
2. 建立数据说明：来源、许可/生成方法、字段、条数、长度、去重方法、train/dev/test 划分。建议项目先取数百条训练样本，几十条开发样本，单独留最终测试；具体规模随可得性调整。
3. 打印 5 条完整样本的模板文本、token IDs、labels 和实际参与 loss 的文本。可先选单轮、只监督 assistant 回复；检查 EOS 与截断是否把答案切掉。
4. 手写一层 LoRA 计算，检查初始增量、可训练参数与梯度；冻结主干后确认主干没有梯度。理解缩放与初始化随实现配置可能不同。
5. 用 20–50 条样本过拟合。训练前后比较相同输入；若 loss 降而输出没变，检查 adapter 是否启用、监督位置、截断、学习率和解码。
6. 记录一轮训练的显存、吞吐和耗时，确认预算后再扩大。

先关闭 packing，先验证单样本边界；需要时再引入 packing 并检查位置和 attention 处理。默认从 LoRA、小 batch、短序列开始；量化与梯度检查点按实测需要增加，不同时引入多个变量。

建议本周：阅读 6 小时、实现与训练 14 小时、分析 5 小时。

## 第 7 周前半：做一个可信的 SFT 对照（约 10 小时）

1. 冻结开发集、评分器和解码设置，记录原模型结果；最终测试集保留到方案确定后评估。
2. 小规模 SFT，记录配置、训练 token 数、学习率、rank、目标模块、损失和验证曲线。只在开发集选 checkpoint。
3. 对比原模型与 SFT：目标任务、格式、长度、拒答/无依据内容、无关任务、耗时与显存。
4. 做一项消融，例如 rank 或数据质量，固定其他因素；记录参数量和训练预算差异。
5. 人工看至少 20 个成功/失败样本，区分原本就会、格式改善、事实错误和泛化失败。接近的差异做重复实验或报告不确定性。
6. 从保存的 adapter 和原基座重建推理，检查加载后的结果。

通过标准：能解释每个监督 token 和实验变量；有可重载的 adapter、原模型/SFT 对照及失败分析。训练 loss 降低不单独构成任务能力提升证据。

## 第 7 周后半：从偏好到 DPO loss，再做短训练

**阅读顺序**：[DPO 论文](https://arxiv.org/abs/2305.18290) 的偏好模型 → KL 约束最优策略 → DPO 目标；[TRL DPOTrainer](https://huggingface.co/docs/trl/dpo_trainer) 对应实现。InstructGPT 的奖励模型只作联系，不额外安排完整 PPO 复现。

**先手算与手写（约 5 小时）**：

- 对同一个 prompt，写 chosen/rejected 在 policy 与冻结 reference 下的回复 log probability。
- 令 delta 为 policy 的 chosen/rejected log-prob 差减去 reference 的对应差；loss 为 -log sigmoid(beta × delta)。
- 从人工 log-prob tensor 验证：policy 等于 reference 时 loss 为 log(2)；提高 chosen 相对概率时 loss 应下降。检查梯度方向与 reference 不参与更新。
- 只累计回复 token，忽略 prompt/padding。原始 DPO 使用序列 log-prob 之和；若采用长度归一化等变体，单独命名和记录。
- 对同一小 batch，与所固定框架版本在相同 beta、mask、reduction 和 loss 类型下对齐。

**再训练（约 7 小时）**：

- 从同一个 SFT checkpoint 建立 policy 和冻结 reference。
- 先构造或筛选 100–500 对量级的偏好数据，记录来源并抽检 chosen 是否确实优于 rejected；数量只是起步建议。
- 将相同 prompt 及其改写归入同一划分；偏好构造不使用最终测试集。
- 先测一个 batch 的显存与更新，再做短训练；比较 SFT 与 DPO 的质量、长度、格式和无关任务。
- preference accuracy、训练 loss 作为训练诊断；独立生成评估用来判断目标任务是否改善。

**复盘（约 3 小时）**：分析偏好噪声、长度偏好、beta 和分布偏移，保留正负结果。无法形成可靠偏好时先用来源清楚的公开偏好数据验证流程，不强行给合成 chosen/rejected 贴高质量标签。

## 本阶段建议产物

- notes/03-lora.md、notes/04-dpo.md。
- experiments/02-sft.md、experiments/03-dpo.md。
- 后续代码放 src/data/、src/train/、src/eval/；配置放 configs/。
- 数据 manifest、模型/数据 revision、样本级预测和评分、adapter 路径、复现命令。

这些是待完成路径与任务，不代表已有实现。第 8 周进入 [RL 指南](03-rl.md)。
