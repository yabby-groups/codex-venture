---
category: "agents"
summaryEn: "ARGUS checks that fallback paths preserve the protections required for sensitive operations. The authors observed no protection loss with enforcement enabled in a separate 864-run evaluation."
summaryZh: "ARGUS 检查备用路径是否保留敏感操作所需的保护。作者在另行开展的 864 次运行评估中发现，启用强制检查后未观察到保护丢失。"
tags: ["mcp", "agent-safety", "workflow-recovery"]
titleEn: "ARGUS checks security requirements when agents switch to a fallback"
titleZh: "ARGUS 在 Agent 切换备用路径时核验安全要求"
blocks: [{"kind": "notice", "text": {"en": "What protection does the sensitive operation require? Does the evidence apply to the exact resource the fallback will touch? Which component enforces the requirement before the operation proceeds?", "zh": "这项敏感操作需要哪些保护？现有证据是否对应备用路径将要操作的同一资源？哪个组件负责在操作放行前强制检查？"}, "title": {"en": "Three questions for reviewing a fallback", "zh": "评审备用路径时的三个问题"}}]
editorial: {"score": 84, "tier": "standard", "audience": "core"}
published: "2026-11-28T21:46:05+08:00"
sources: [{"title": "The Detour Is the Danger: Preserving Security During LLM Agent Recovery", "url": "https://arxiv.org/abs/2611.33605"}]
---
<p lang="zh-CN">当带审批的 MCP 工具调用失败，Agent 可能改用另一条路径完成任务。维护者需要确认，原先的审批是否仍适用于新路径实际操作的资源。Boyang Ma 等人在 2026 年 11 月 25 日提交的预印本中提出 ARGUS，将这项检查纳入自动恢复过程。<a href="https://arxiv.org/abs/2611.33605">arXiv 预印本</a></p>

<p lang="en">When an MCP tool call fails in a workflow that requires approval, an agent may take another route to finish the job. Maintainers need to check whether the original approval still covers the resource the new route will touch. In a preprint submitted on November 25, 2026, Boyang Ma and colleagues propose ARGUS to make that check part of automated recovery. <a href="https://arxiv.org/abs/2611.33605">arXiv preprint</a></p>

<p lang="zh-CN">ARGUS 将安全证据绑定到具体资源，独立验证恢复计划，并在敏感操作执行时强制落实保护要求。作者对 7 个模型、12 个任务模板和 3 类安全敏感场景进行了研究。在另行开展的 864 次运行评估中，启用强制检查后未观察到保护丢失。与只拦截不满足要求的操作相比，协助 Agent 找到符合要求的恢复路径，对任务完成率的改善因模型而异。</p>

<p lang="en">ARGUS ties security evidence to specific resources, validates recovery plans in isolation, and enforces protection requirements when sensitive operations run. The authors studied seven models across 12 task templates and three security-sensitive domains. In a separate 864-run evaluation, they observed no loss of protection with enforcement enabled. Compared with blocking alone, helping agents find a recovery path that met the requirements improved task completion to varying degrees across models.</p>
