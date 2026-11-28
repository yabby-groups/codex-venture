---
category: "agents"
summaryEn: "RadOncGym uses fast surrogate feedback to decide when to run a full radiotherapy planning solve. In a retrospective head-and-neck study capped at three full solves, the agent beat the evaluated non-agent tuning methods at the same solve budget."
summaryZh: "RadOncGym 用快速代理反馈决定何时调用完整放疗计划求解。在头颈病例回顾性评估中，Agent 在最多三次完整求解的条件下优于同等预算内纳入评估的非 Agent 调参方法。"
tags: ["radoncgym", "radiotherapy", "optimization", "agents"]
titleEn: "RadOncGym Tunes Radiotherapy Plan Weights With Three Full Solves"
titleZh: "RadOncGym 在三次完整求解预算内调整放疗计划权重"
editorial: {"score": 64, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T17:31:21+08:00"
sources: [{"title": "RadOncGym: An Agent-Based Framework for Radiotherapy Dose-Mimicking Optimization", "url": "https://arxiv.org/abs/2611.33821"}]
---
<p lang="zh-CN">预测出的三维放疗剂量分布还要经过优化，才能形成满足物理约束的治疗计划。11 月 26 日列入 arXiv 公告的 RadOncGym 预印本研究了这一环节的 12 个计划目标权重如何调整。框架用快速代理验证器为候选权重提供反馈，由 Agent 决定何时花掉一次完整计划求解的配额。</p>

<p lang="en">A predicted 3D radiotherapy dose distribution still has to go through optimization to produce a physically constrained treatment plan. The RadOncGym preprint listed in arXiv’s November 26 announcements studies how to tune the 12 planning-objective weights used at that stage. A fast surrogate verifier gives feedback on candidate weights, and the agent decides when to spend one of its full planning solves.</p>

<p lang="zh-CN">作者使用了 OpenKBP 的 60 个头颈病例，每例配十份 OpenKBP-Opt 剂量预测。预印本报告，在 16 轮、最多三次完整求解的设置下，GPT-5.6 Sol Agent 相对 12 个权重均固定为 1 的基线，将平均临床准则违背量降低了 0.6131 Gy。在同等求解预算下，它也优于作者纳入评估的非 Agent 调参方法。</p>

<p lang="en">The authors used 60 head-and-neck cases from OpenKBP, each paired with ten OpenKBP-Opt dose predictions. Under a 16-turn setting with up to three full solves, the preprint reports that a GPT-5.6 Sol agent reduced mean clinical-criterion violation by 0.6131 Gy compared with fixing all 12 weights at 1. It also outperformed the non-agent tuning methods the authors evaluated under the same solve budget.</p>

<p lang="zh-CN">如果要在另一套昂贵的优化任务中检验这类方法，可以给各方法相同的完整求解上限，记录哪些候选经过了完整求解，再用完整求解的指标比较结果。RadOncGym 报告的数值来自这组回顾性病例上的计划优化评估。<a href="https://arxiv.org/abs/2611.33821">arXiv 预印本</a></p>

<p lang="en">To test this approach on another expensive optimization problem, give each method the same cap on full solves, record which candidates receive one, and compare the metrics from those solves. RadOncGym’s reported figures come from a retrospective evaluation of plan optimization on this case set. <a href="https://arxiv.org/abs/2611.33821">arXiv preprint</a></p>
