# 论文阅读顺序

第一轮只安排前三篇。后续按主线推进，基座论文穿插选读，专题论文等首次适配实验后阅读。

| 顺序 | 论文与官方来源 | 阅读方式 | 核心问题 | 本地全文 |
| --- | --- | --- | --- | --- |
| 1 | [InstructGPT](https://arxiv.org/abs/2203.02155) | 精读 | SFT、奖励模型、RL、数据与能力保持 | [PDF](pdf/01-instructgpt.pdf) |
| 2 | [DeepSeekMath](https://arxiv.org/abs/2402.03300) | 精读 | 数据、继续预训练与 GRPO | [PDF](pdf/02-deepseekmath.pdf) |
| 3 | [LoRA](https://arxiv.org/abs/2106.09685) | 方法与实验 | 低秩更新、初始化、适配与干扰 | [PDF](pdf/03-lora.pdf) |
| 4 | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | 精读推导 | KL 约束目标到偏好 loss | [PDF](pdf/04-dpo.pdf) |
| 5 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | 训练流程 | cold start、RL、筛选与蒸馏 | [PDF](pdf/05-deepseek-r1.pdf) |
| 6 | [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 选读 | 参数、token 与计算预算 | [PDF](pdf/06-chinchilla.pdf) |
| 7 | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | 回读 | MLA、MoE、MTP、数据与消融 | [PDF](pdf/07-deepseek-v3.pdf) |
| 8 | [Doc-to-LoRA](https://arxiv.org/abs/2602.15902) | 专题选读 | 知识内化及 C.4 知识干扰 | [PDF](pdf/08-doc-to-lora.pdf) |
| 9 | [AlphaEdit](https://arxiv.org/abs/2410.02355) | 专题选读 | 零空间约束、保护范围与局限 | [PDF](pdf/09-alphaedit.pdf) |

PDF 来自官方 arXiv，下载脚本记录实际来源、时间、文件大小与 SHA256。未带版本号的链接指向下载时版本，SHA256 固定本次文件内容。权利归原作者/权利人。论文观点不等于已完成的个人实验。

每篇记录：问题、数据、目标函数、实验证据、局限，并安排一个最小验证。
