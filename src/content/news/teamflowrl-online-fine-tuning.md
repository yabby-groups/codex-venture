---
category: "models"
summaryEn: "The TeamFlowRL authors report that online fine-tuning improved all 51 offline flow-policy baselines they tested, with an average gain of 47.3% in normalized simulation scores."
summaryZh: "TeamFlowRL 作者报告，在线微调提升了全部 51 个受测离线流策略的表现，仿真归一化得分平均提高 47.3%。"
tags: ["reinforcement-learning", "multi-agent", "flow-policies", "robotics"]
titleEn: "TeamFlowRL improves offline coordination policies in 51 simulation comparisons"
titleZh: "TeamFlowRL 在 51 个仿真对照中提高离线协作策略得分"
published: "2026-11-25T19:50:11+08:00"
sources: [{"title": "TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination", "url": "https://arxiv.org/abs/2611.32645"}]
---
<p lang="zh-CN">Guowei Zou、Beiwen Zhang、Haitao Wang、Hong Hong、Zhiquan Chen 和 Hejun Wu 于 11 月 24 日向 arXiv 提交 TeamFlowRL 预印本。该方法先用离线数据预训练各智能体的流策略，再通过环境交互继续训练。在线阶段在完整的去噪轨迹上定义优化目标，绕开难以直接计算的动作似然，并用共享的团队优势估计指导各智能体的策略更新。</p>

<p lang="en">Guowei Zou, Beiwen Zhang, Haitao Wang, Hong Hong, Zhiquan Chen, and Hejun Wu submitted the TeamFlowRL preprint to arXiv on November 24. The method first pretrains each agent’s flow policy on offline data, then continues training through interaction with the environment. The online objective operates on full denoising trajectories, sidestepping hard-to-compute action likelihoods and using a shared team advantage estimate to guide each agent’s policy updates.</p>

<p lang="zh-CN">作者报告，七组仿真的 51 个配对配置中，在线微调后的归一化得分均高于各自的离线起点。在六项双臂协作任务中，有探索噪声时，该方法的平均成功率比高斯策略微调高 33.1%。这为研究人员提供了一种从现有离线策略出发、通过仿真交互继续改善协作的训练方案。</p>

<p lang="en">The authors report that online fine-tuning raised the normalized score over the corresponding offline baseline in all 51 paired configurations across seven simulation groups. In six bimanual tasks with exploration noise, the average success rate was 33.1% higher than with Gaussian-policy fine-tuning. The method gives researchers a way to start with existing offline policies and improve coordination through further interaction in simulation.</p>
