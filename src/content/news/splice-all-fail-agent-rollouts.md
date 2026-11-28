---
category: "agents"
summaryEn: "SPLICE uses short branches from failed rollouts to recover a training signal. Its authors report gains of 2.8 to 9.8 percentage points over GRPO across four benchmark settings."
summaryZh: "SPLICE 从失败轨迹中间尝试短续接，为整组零分的任务找回学习信号。作者在四组基准设置中报告比 GRPO 高 2.8 至 9.8 个百分点。"
tags: ["reinforcement-learning", "grpo", "agent-training"]
titleEn: "When every agent rollout fails, SPLICE tries a different next step"
titleZh: "Agent 训练轨迹全失败时，SPLICE 从中途换一步再试"
editorial: {"score": 73, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T15:46:02+08:00"
sources: [{"title": "When Every Rollout Fails: Splicing Learner-Conditioned Options into Long-Horizon Agent RL", "url": "https://arxiv.org/abs/2611.34777"}]
---
<p lang="zh-CN">用可验证奖励训练长任务 Agent 时，如果同一题采样出的轨迹全得零分，组相对方法就缺少基于奖励的更新信号。SPLICE 从当前策略已经生成的失败轨迹中选一个切入点，由提议模型给出几段短续接，再让当前策略从各个选项多次续跑，用得到的回报估计哪些局部选择值得学习。</p>

<p lang="en">In long-horizon agent training with verifiable rewards, group-relative methods lose their reward-based update signal when every rollout for a task scores zero. SPLICE starts partway through a failed rollout from the current policy. A proposal model offers several short continuations, and the current policy rolls out repeatedly from each option to estimate which local choices are worth learning.</p>

<p lang="zh-CN">作者用两类策略模型测试了 SWE-bench Verified 和 BrowseComp-Plus，在四组设置中报告相对 GRPO 提高 2.8 至 9.8 个百分点。对频繁遇到整组零分的训练团队，可以把局部续跑和完整教师轨迹纳入同预算对照，同时衡量任务成功率和提议模型的计算开销。<a href="https://arxiv.org/abs/2611.34777">arXiv 预印本</a></p>

<p lang="en">The authors tested two policy families on SWE-bench Verified and BrowseComp-Plus and reported gains of 2.8 to 9.8 percentage points over GRPO across four settings. Teams that see frequent all-zero groups can compare local continuations with full teacher trajectories under the same budget, measuring both task success and proposal-model compute. <a href="https://arxiv.org/abs/2611.34777">arXiv preprint</a></p>
