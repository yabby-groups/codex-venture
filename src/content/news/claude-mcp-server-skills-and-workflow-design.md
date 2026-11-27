---
category: "agents"
summaryEn: "Claude can load workflow guidance from an MCP server on demand. Anthropic’s November 24 announcement also made Tasks and Elicitation generally available."
summaryZh: "Claude 可按需加载 MCP 服务器提供的操作指南。Anthropic 同时宣布，面向长任务和请求用户输入的 Tasks 与 Elicitation 已正式可用。"
tags: ["claude", "mcp", "skills"]
titleEn: "Claude lets MCP servers ship workflow guidance alongside tools"
titleZh: "Claude 允许 MCP 服务器随工具发布工作流指南"
type: "insights"
version: "Claude apps and Claude Platform, November 24, 2026 announcement"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T18:03:28+08:00"
sources: [{"title": "MCP servers can now ship skills, run tasks, and more with Claude", "url": "https://claude.com/resources/articles/skills-over-mcp-tasks-and-more"}]
---
<p lang="zh-CN">工具定义告诉 Claude 有哪些操作可用，但一个跨步骤的任务还需要说明何时调用哪些工具、按什么顺序做。Anthropic 在 2026 年 11 月 24 日宣布，MCP 服务器现在可以把这类操作指南作为技能随工具一起发布。Claude 在需要时加载技能，技能随服务器更新，用户无需另行安装。<a href="https://claude.com/resources/articles/skills-over-mcp-tasks-and-more">Anthropic 发布说明</a></p>

<p lang="en">Tool definitions tell Claude which actions are available. A multistep job can also require guidance on when to call each tool and in what order. On November 24, 2026, Anthropic announced that MCP servers can publish that guidance as skills alongside their tools. Claude loads a skill when it needs it, and the skill updates with the server without a separate installation for users. <a href="https://claude.com/resources/articles/skills-over-mcp-tasks-and-more">Anthropic’s announcement</a></p>

<p lang="zh-CN">这给连接器开发者提供了三个不同的设计入口。技能负责传递操作指南，Tasks 面向运行时间较长的工作，Elicitation 让服务器在处理过程中向用户索取输入。按 Anthropic 当天公布的状态，Skills over MCP 处于公开测试，Tasks 和 Elicitation 已正式可用，File Uploads 尚待推出。</p>

<p lang="en">That gives connector developers three ways to support a workflow. Skills convey operating guidance, Tasks support longer-running work, and Elicitation lets a server request user input along the way. In Anthropic’s announcement, Skills over MCP was in public beta, Tasks and Elicitation were generally available, and File Uploads was still forthcoming.</p>
