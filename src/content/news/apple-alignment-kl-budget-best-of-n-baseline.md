---
category: "models"
summaryEn: "Apple researchers derive a reward ceiling for a fixed KL divergence budget. Best-of-N approached it on two tasks, giving training teams a baseline for measuring the gains from reinforcement learning."
summaryZh: "Apple 研究团队推导了固定 KL 散度预算下的奖励上限。Best-of-N 在两项任务上接近该上限，可作为衡量强化学习收益的基线。"
tags: ["llm-alignment", "best-of-n", "reinforcement-learning"]
titleEn: "Apple Study Finds Best-of-N Nears the Alignment Reward Ceiling on Two Tasks"
titleZh: "Apple 研究发现 Best-of-N 在两项任务上接近对齐奖励上限"
editorial: {"score": 73, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T12:45:54+08:00"
sources: [{"title": "Theoretical Limits of Language Model Alignment", "url": "https://machinelearning.apple.com/research/theoretical-limits-alignment"}]
---
<p lang="zh-CN">团队准备投入偏好强化学习时，可以先测从基础模型采样多次、按奖励选出一条的 best-of-N。Apple 在 2026 年 11 月发布的 NeurIPS 论文中，Lucas Monteiro Paes、Natalie Mackraz、Barry-John Theobald 和 Federico Danieli 推导了固定 KL 散度预算下的最大期望奖励增益。这个预算衡量对齐后的输出分布可以偏离基础模型多远。作者还把增益表达式写成协方差形式，让研究者可以用基础模型的样本估计增益上限。<a href="https://machinelearning.apple.com/research/theoretical-limits-alignment">Apple 研究页面</a></p>

<p lang="en">Before investing in reinforcement learning from preferences, a team can benchmark best-of-N, which draws several outputs from the base model and picks the one with the highest reward. In a NeurIPS paper Apple published in November 2026, Lucas Monteiro Paes, Natalie Mackraz, Barry-John Theobald, and Federico Danieli derive the maximum expected reward gain for a fixed KL divergence budget. That budget measures how far the aligned output distribution can move from the base model’s distribution. The authors also express the gain in terms of covariance, making it possible to estimate the ceiling from base-model samples. <a href="https://machinelearning.apple.com/research/theoretical-limits-alignment">Apple research page</a></p>

<p lang="zh-CN">作者在安全和摘要两项任务上比较了奖励与 KL 偏移的关系。实测 best-of-N 接近理论上限，所测 PPO 和 GRPO 还差得较远。对正在制定训练方案的团队，这给出了一个可测的基线。在自己的任务上比较同等 KL 偏移下的奖励，再分别记录 best-of-N 的重复采样开销和强化学习方案的训练与推理开销。论文的实证比较覆盖上述两项任务。</p>

<p lang="en">The authors compared reward against KL divergence on safety and summarization tasks. Best-of-N came close to the theoretical ceiling, while the PPO and GRPO runs they tested fell further short. Teams planning a training run can use best-of-N as a measurable baseline on their own tasks. Compare rewards at a matched KL divergence, then track the cost of repeated sampling alongside the reinforcement learning approach’s training and inference costs. The paper’s empirical comparison covers the two tasks above.</p>
