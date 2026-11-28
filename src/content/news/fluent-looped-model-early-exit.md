---
category: "models"
summaryEn: "FLUENT uses a looped model’s final predictions to train its earlier iterations. In one real-robot experiment, the authors report higher success and shorter average duration among successful runs."
summaryZh: "FLUENT 用循环模型的末轮预测训练较早轮次。在作者报告的一项真实机器人实验中，任务成功率提高，成功回合的平均耗时缩短。"
tags: ["early-exit", "looped-models", "robotics"]
titleEn: "FLUENT trains looped models to exit earlier"
titleZh: "FLUENT 让循环模型学会提前退出"
editorial: {"score": 72, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T17:45:22+08:00"
sources: [{"title": "Practice Makes Fluent: Learning to Use Earlier Predictions in Looped Models", "url": "https://arxiv.org/abs/2611.33722"}]
---
<p lang="zh-CN">循环模型可以在每轮给出中间预测。11 月 26 日公布的 FLUENT 预印本用初始模型冻结的末轮预测训练较早轮次，同时约束训练后模型的末轮输出。退出门控在预测差异和计算成本之间做取舍，决定是否继续迭代。按作者描述，这套训练无需额外任务标签或奖励。</p>

<p lang="en">Looped models can produce an intermediate prediction on each iteration. The FLUENT preprint announced on November 26 uses the initial model’s frozen final-iteration prediction to train earlier iterations and to anchor the trained model’s final prediction. An exit gate balances prediction disagreement against compute cost to decide whether to keep iterating. The authors describe a training process that requires no additional task labels or rewards.</p>

<p lang="zh-CN">在作者报告的一项真实机器人实验中，成功率从 62.3% 升至 74.6%，成功回合的平均耗时从 69 秒降至 31 秒。这个耗时口径只计成功回合。复用这一评估思路时，可以一并记录实际迭代次数、全体回合成功率和成功回合耗时，并复查训练后的末轮预测质量。<a href="https://arxiv.org/abs/2611.33722">论文摘要</a></p>

<p lang="en">In one real-robot experiment reported by the authors, the success rate rose from 62.3% to 74.6%, and average duration fell from 69 to 31 seconds among successful runs. That timing metric covers successful runs only. A similar evaluation can track actual iteration counts, success across all runs, and duration among successful runs, alongside a check of final-iteration prediction quality after training. <a href="https://arxiv.org/abs/2611.33722">Paper abstract</a></p>
