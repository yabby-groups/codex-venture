---
category: "coding"
summaryEn: "SessionGraph documents a local index for searching past conversations from Codex, Claude Code, and other coding tools. A conversation you already know is a good first check for both desktop search and MCP access."
summaryZh: "SessionGraph 官网介绍了如何用一个本地索引搜索 Codex、Claude Code 等工具留下的对话。首次使用时，可以用一条已知会话检查桌面搜索和 MCP 查询是否都能找到它。"
tags: ["sessiongraph", "coding-agents", "session-search", "mcp"]
titleEn: "Find old debugging conversations across coding agents with SessionGraph"
titleZh: "用 SessionGraph 跨编码代理找回旧排障对话"
type: "insights"
version: "SessionGraph official website documentation"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 66, "tier": "standard", "audience": "core"}
published: "2026-11-28T14:03:44+08:00"
sources: [{"title": "SessionGraph: Visualize all your coding agent sessions in one interactive graph", "url": "https://sessiongraph.ai/"}]
---
<p lang="zh-CN">上次排查发票重复重试用的是 Claude Code，这次打开的是 Codex。要找回当时的排查对话，可以在 SessionGraph 里用故障关键词跨工具搜索。项目官网介绍，SessionGraph 读取各编码工具保存的会话，建立一个本地索引。Codex、Claude Code 和 OpenCode 都在官网的支持名单里。<a href="https://sessiongraph.ai/">SessionGraph 官网</a></p>

<p lang="en">You investigated duplicate invoice retries in Claude Code last time, and now you’re working in Codex. To recover that conversation, you can search across tools in SessionGraph using a phrase from the incident. The project’s website says SessionGraph reads saved conversations from coding tools and builds a single local index. Codex, Claude Code, and OpenCode are on its support list. <a href="https://sessiongraph.ai/">SessionGraph website</a></p>

<p lang="zh-CN">同一个索引也能通过 MCP 查询。官网以发票重试为例，演示如何让当前代理按关键词查找旧会话，返回来自不同工具的匹配项。准备在下一次排障中使用前，可以先在桌面应用里搜索一条记得原文的会话，确认索引里有这条记录，再用同一关键词检查代理能否通过 MCP 找到它。本文依据项目文档，未运行验证会话识别或 MCP 查询。<a href="https://sessiongraph.ai/">官网查询示例</a></p>

<p lang="en">The same index is searchable through MCP. The website uses invoice retries to illustrate how a coding agent can search past conversations by keyword and get matches from different tools. Before relying on it for your next debugging session, try a phrase you remember from an old conversation in the desktop app. Once you find it there, use the same phrase to check whether your agent can retrieve it through MCP. This article is based on project documentation. Session discovery and MCP queries were not tested. <a href="https://sessiongraph.ai/">Search example on the project website</a></p>
