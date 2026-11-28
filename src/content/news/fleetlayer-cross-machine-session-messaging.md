---
category: "agents"
summaryEn: "Fleetlayer shows how to list Claude Code and Codex sessions by machine and address a message to a specific session. Its early examples give developers a concrete way to evaluate handoffs between a laptop and a home server."
summaryZh: "Fleetlayer 官网展示了如何按机器查看 Claude Code 和 Codex 会话，并将消息发给指定会话。这个早期项目可用来评估笔记本和家用服务器之间的会话交接。"
tags: ["fleetlayer", "claude-code", "codex", "session-management"]
titleEn: "How Fleetlayer addresses coding sessions across machines"
titleZh: "Fleetlayer 如何给不同机器上的编码会话发消息"
type: "insights"
version: "Early source-available project, official site as of 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 66, "tier": "standard", "audience": "core"}
published: "2026-11-28T18:01:27+08:00"
sources: [{"title": "Show HN: Fleetlayer – Framework for running many AI agents on multiple machines", "url": "https://fleetlayer.ai/"}]
---
<p lang="zh-CN">笔记本上的会话修完上传测试后，家用服务器上的会话怎样接到进度？Fleetlayer 官网展示的做法是给运行中的 Claude Code 和 Codex 会话分配包含机器名的地址。它的命令行示例把消息送到 <code>api@laptop</code>，对应笔记本上的 API 会话。<a href="https://fleetlayer.ai/">Fleetlayer 官网</a></p>

<p lang="en">When a session on your laptop finishes fixing an upload test, how does the session on your home server get the update? Fleetlayer’s site shows Claude Code and Codex sessions with addresses that include their machine names. In its command-line example, a message goes to <code>api@laptop</code>, the API session on the laptop. <a href="https://fleetlayer.ai/">Fleetlayer website</a></p>

<p lang="zh-CN">官网还展示了按机器列出的会话状态，以及集中查看待审批请求的面板。如果你在评估跨机器交接，可以把验收条件定为：两台机器的会话都出现在列表里，一条无敏感内容的进度消息只送达指定会话。官网把项目描述为早期、源码可查看。本篇依据官网示例，未运行双机部署，节点部署条件和会话管理器兼容范围仍待核实。<a href="https://fleetlayer.ai/">Fleetlayer 官网</a></p>

<p lang="en">The site also shows session status grouped by machine and a dashboard for pending approvals. If you’re evaluating cross-machine handoffs, check that both sessions appear in the list and that a harmless status message reaches only the intended session. Fleetlayer describes itself as early and source-available. This article draws on the site’s examples. We did not run a two-machine setup, and node deployment requirements and session-manager compatibility remain unverified. <a href="https://fleetlayer.ai/">Fleetlayer website</a></p>
