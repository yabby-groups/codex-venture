---
category: "agents"
summaryEn: "Tillerly groups decisions from multiple coding agents into one queue while keeping plan approval, acceptance testing, and merging in human hands. Its account describes the workflow but gives no measured impact on delivery time."
summaryZh: "Tillerly 将多个编码代理需要人工处理的决定集中到一张清单，团队仍负责批准计划、验收和合并。原文交代了流程，交付是否因此加快仍待验证。"
tags: ["coding-agents", "human-review", "tillerly"]
titleEn: "How Tillerly queues decisions from multiple coding agents"
titleZh: "Tillerly 如何集中处理多个编码代理的待审决定"
type: "insights"
version: "Tillerly workflow described on 2026-11-23"
verified: "2026-11-25"
status: "current"
tested: false
published: "2026-11-25T21:04:05+08:00"
sources: [{"title": "Why supervision does not scale with the AI coding agents", "url": "https://tillerly.dev/blog/managing-multiple-ai-coding-agents-from-one-list"}]
---
<p lang="zh-CN">当多个编码代理同时推进工单，计划审批、实现疑问和验收都可能打断同一个人。Tillerly 在 2026 年 11 月 23 日的文章中介绍了自己的做法：事先规定哪些决定必须由人作出，将待处理事项集中到一张清单里，让负责人自己选择处理时机。<a href="https://tillerly.dev/blog/managing-multiple-ai-coding-agents-from-one-list">Tillerly 原文</a></p>

<p lang="en">When several coding agents work on tickets at once, plan approvals, implementation questions, and acceptance checks can all interrupt the same person. In a November 23, 2026 post, Tillerly described its approach. It decides up front which calls need a person and collects pending decisions in one list that reviewers can check on their own schedule. <a href="https://tillerly.dev/blog/managing-multiple-ai-coding-agents-from-one-list">Tillerly’s post</a></p>

<p lang="zh-CN">按 Tillerly 的描述，每张工单都依次经过七个阶段，前一阶段完成后才进入下一阶段。一个代理制定计划，另一个负责实现。团队先批准计划，再由代理实施。实现遇到需要判断的问题时，代理在工单里提问并等待答复。团队负责打开和合并拉取请求，构建通过后还要人工验收。<a href="https://tillerly.dev/blog/managing-multiple-ai-coding-agents-from-one-list">流程说明</a></p>

<p lang="en">Tillerly says each ticket moves through seven stages in order, with each stage blocking the next. One agent drafts the plan and another implements it after the team approves it. If implementation calls for a decision, the agent asks in the ticket and waits. The team opens and merges the pull request, and a passing build is followed by human acceptance testing. <a href="https://tillerly.dev/blog/managing-multiple-ai-coding-agents-from-one-list">Workflow description</a></p>

<p lang="zh-CN">这套流程把部分即时打断变成了可以集中处理的待办，但工单仍要等到负责人作出决定才能继续。Tillerly 的文章描述了这种等待机制。它对实际中断次数、审查耗时和交付速度的影响仍待验证。</p>

<p lang="en">The workflow turns some interruptions into decisions that can be handled together. A blocked ticket still waits for its reviewer. Tillerly’s account describes how that waiting works, while the effects on interruption frequency, review time, and delivery speed remain unmeasured in the supplied account.</p>
