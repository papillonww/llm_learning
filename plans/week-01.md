# 首周任务

## 任务 1：InstructGPT

- [ ] 阅读方法、数据与能力退化分析。
- [ ] 画出 SFT → reward model → policy optimization 的数据/模型流向。
- [ ] 标明每阶段样本格式、可训练参数与目标函数。
- [ ] 回答为什么需要 reference policy，以及混合预训练目标解决什么问题。

## 任务 2：DeepSeekMath

- [ ] 浏览数据构造与训练阶段，精读 GRPO。
- [ ] 区分 old policy 与 reference policy。
- [ ] 用手工奖励 [0, 0, 1, 1]、[0, 0, 0, 0] 计算组内优势。
- [ ] 明确标准差为零的处理，以及实现中的 epsilon。
- [ ] 核对 ratio、clipping、KL 各项的梯度与适用位置。
- [ ] 对齐论文公式与所用实现版本，记录差异。

## 任务 3：建立记录

- [ ] 复制 notes/paper-template.md 记录上述两篇。
- [ ] 记录 Python/PyTorch/CUDA/驱动与库版本；先确认本机兼容性。
- [ ] 记录未解决问题；不以“看过”替代“能解释或验证”。

完成标准：能够不看原文解释训练流程与 GRPO 主要变量，并展示一份最小数值验证记录。第一周不要求完整模型训练。