# 从已读 GPT-2 / Qwen2.5 接着学：接下来 7 天

状态：待执行。第 1 天是实际开始日，不推定过去一周已完成。总计约 25 小时；可以五天各 4 小时、一天 5 小时、一天休息。

## 第 1 天：把 InstructGPT 接到真实模型（4 小时）

**先理解，1 小时**：前 30 分钟闭卷复述 InstructGPT，再局部核查三阶段数据与模型角色。后 30 分钟打开已读 GPT-2 / Qwen2.5 代码和 LLaMA 结构图，列出 norm、位置编码、MLP、Q/K/V heads 的差异。不会的点进入本周问题清单。

**实践，2 小时**：在实际训练设备记录 Python/PyTorch/CUDA/驱动和库版本。使用 [Qwen3-0.6B 模型卡](https://huggingface.co/Qwen/Qwen3-0.6B) 的兼容加载方法，先跑单条短文本，再跑 5 个固定 prompts。记录权重 revision、chat template、thinking 模式、生成参数、耗时和显存。首轮使用非 thinking 模式（若模板支持），检查渲染后的实际文本。

**记录，1 小时**：保存 notes/01-instructgpt.md、experiments/00-environment.md、experiments/01-inference.md。这些是建议产物路径，目前尚未创建或执行。

通过标准：不看论文解释三阶段；能展示输入文本、token IDs 和生成输出。遇到环境问题先记录完整报错与版本，单次排查设 1 小时检查点，避免整周都在安装。

## 第 2 天：token 到 next-token loss（4 小时）

**阅读，1 小时**：按 [演进地图](model-evolution.md) 读 LLaMA 的结构部分，对照已读 GPT-2 / Qwen2.5；定位参考 Qwen dense 的 embedding、decoder layer、LM head。只补 causal LM loss 和 attention mask 的具体缺口。

**实践，2 小时**：打印一条样本的 tokens 和 labels，手写 logits 去掉最后一位、labels 去掉第一位后的交叉熵，忽略 -100，与参考模型 loss 对齐。加一条不同长度样本，核查 padding、attention mask、position IDs；比较单独运行和组成 batch 的有效 token logits。

**记录，1 小时**：列出 [B,L] → [B,L,D] → [B,L,V] 的 shape；解释哪些 token 被预测、最后一个位置如何处理。

通过标准：同输入、同 mask、同归一化的 loss 数值一致；若有差异，能定位 shift、padding、分母或位置编号。

## 第 3 天：RMSNorm、RoPE、GQA 与 QK-Norm（4 小时）

**阅读，1 小时**：核查 LLaMA 1/2 和 Qwen2.5/Qwen3 对应配置；按 [模型指南](01-model-basics.md) 理解 RoPE 维度、GQA head 数、QK-Norm 位置。把本来就会的部分快速通过，专注新增差异。

**实践，2 小时**：手写 RMSNorm 和 RoPE，构造固定随机 tensor 与参考输出比较。画出 Q/K/V reshape、transpose、KV head 展开的 shape。验证 position offset，避免 cache 阶段位置从零重置。

**记录，1 小时**：保存模块误差表，注明 dtype、输入范围、绝对与相对误差。

通过标准：解释维度和广播；对齐同一实现约定后通过数值比较。

## 第 4 天：实现并对齐一个 decoder block（4 小时）

**阅读，1 小时**：沿参考实现检查 norm、attention、残差、MLP 顺序，以及 SwiGLU 三个线性层的作用。

**实践，2 小时**：实现单个 dense block，按 checkpoint 配置加载对应权重。FP32、eval、固定输入，对比 norm、Q/K/V、attention 输出、MLP 和 block 输出，找到第一个发生偏差的位置。

**记录，1 小时**：写出误差来源和修复过程，保留一条失败案例。

通过标准：逐层误差可解释并达到预先约定容差；不以最终生成文本相似代替数值检查。

## 第 5 天：拼接模型与生成；建立项目候选（4 小时）

**实践，3 小时**：按配置拼接 embedding、blocks、final norm、LM head，核查 tied embeddings 等配置；短文本比较 logits 和 greedy 输出。未完成全模型时，保留单 block 结果与阻塞，第二周继续。

**项目准备，1 小时**：读 [专题方案](project.md)，列出一个问题、公开/合成数据、自动指标和质量评估办法；选 20 条开发 prompts，另留最终测试集，不在本周反复查看测试输出。

通过标准：有模型对齐记录和一页项目候选说明，未完成部分明确保留。

## 第 6 天：KV cache 验证与复盘（5 小时）

**实践，3 小时**：实现或跟踪 KV cache。用相同前缀比较完整重算与 prefill + 单 token decode 的 logits，检查 causal mask、位置偏移、缓存 shape。全模型未对齐时，先在参考模型验证 cache 行为，再对齐自己的局部实现。

**复盘，1 小时**：不看源码讲一遍 token → logits → loss → generation；记录实际完成、误差和下一步。

**下周准备，1 小时**：读 Qwen3 与 Qwen2.5 报告的数据/训练差异；确定营销规则项目的数据格式。第二周完成模型剩余验证、tiny overfit 和项目数据准备。

通过标准：缓存和非缓存的有效位置 logits 一致，或明确尚未通过的原因；没有证据的任务不勾选完成。

## 第 7 天：休息或弹性调整

默认休息。若前面超时，最多挪一个最小阻塞来解决，不追加新论文或框架。

## 本周结束应留下什么

- [ ] InstructGPT 流程图与自己的疑问；GPT-2 / LLaMA / Qwen 系列第一版差异卡。
- [ ] 环境和 5 条固定推理记录。
- [ ] shifted loss、padding、关键模块与单 block 数值记录。
- [ ] 全模型/cache 的实测状态，包含尚未通过的检查。
- [ ] 一个专题候选与下周数据基线任务。

不要求首周训练完整 Qwen3；小数据过拟合安排在第二周。详细要求见 [模型指南](01-model-basics.md)。
