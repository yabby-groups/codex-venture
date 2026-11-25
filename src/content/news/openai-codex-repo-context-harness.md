---
titleZh: "Codex 团队为什么把上下文从讨论搬进仓库"
titleEn: "Why an OpenAI team moved Codex context into the repository"
summaryZh: "Ryan Lopopolo 的工程复盘解释了团队怎样把架构决定、可检查约束和清理任务交给版本控制。"
summaryEn: "Ryan Lopopolo describes how his team put architectural decisions, enforceable rules, and cleanup tasks under version control."
type: "stories"
category: "agents"
published: "2026-11-25T20:55:05+08:00"
verified: "2026-11-25"
version: "OpenAI engineering account, 2026-02-11"
status: "current"
tested: false
tags: ["ai-stories"]
sources: [{"title": "Ryan Lopopolo / OpenAI engineering account", "url": "https://openai.com/index/harness-engineering/"}]
---

<p lang="zh-CN">OpenAI 的 Ryan Lopopolo 回顾了一个用 Codex 开发内部产品的工程项目。团队发现，聊天里达成共识的架构决定，如果没有进入仓库，后续的 Agent 会话就很难找到。最初试图把全部说明集中在一份 AGENTS.md 里，文档越长，越难维护，也越难判断哪些条目已经过时。</p>

<p lang="en">OpenAI’s Ryan Lopopolo described an internal product built with Codex. Architectural decisions made in chat were hard for later agent sessions to retrieve if they never reached the repository. An early attempt to put everything in AGENTS.md produced a growing document that was difficult to maintain and audit for stale guidance.</p>

<p lang="zh-CN">团队后来把根级说明当作入口，把设计、架构和实施计划放进有结构的文档目录，辅以自动检查。他还记录了人手每周清理生成代码难以持续，团队随之把部分偏好写成可以检测的规则，再安排定期任务提交有针对性的改动。</p>

<p lang="en">The team turned the root instructions into an entry point, moved designs, architecture, and implementation plans into structured documents, and backed them with automated checks. Lopopolo also recounts how weekly manual cleanup became hard to sustain. The team encoded some preferences as checkable rules and scheduled jobs to propose focused changes.</p>

<p lang="zh-CN">这是该团队的工程复盘。原作者把多年尺度的架构一致性列为仍待观察的问题。小团队可以先从一条常被漏掉、后果可检查的约束入手，为它补上仓库里的说明和自动检查，让下一次改动能直接看到反馈。</p>

<p lang="en">This is the team’s engineering retrospective. Lopopolo leaves architectural coherence over a period of years as an open question. A small team can start with one repeatedly missed rule whose consequences are observable, then add repository guidance and an automated check that gives feedback on the next change.</p>
