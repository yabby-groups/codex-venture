---
category: "coding"
summaryEn: "Claude Code now warns about tool rules that look incomplete, explains why MCP servers stop loading after a mid-session managed configuration change, and shows when a provider or environment variable disables a feature."
summaryZh: "Claude Code 新增疑似不完整工具规则的启动警告，在托管配置于会话中加入时说明 MCP 服务器为何停止加载，并在 /status 显示由服务提供商或环境变量停用的功能。"
tags: ["claude-code", "mcp", "diagnostics"]
titleEn: "Claude Code v2.1.326 adds diagnostics for tool rules and managed MCP"
titleZh: "Claude Code v2.1.326 新增工具规则警告和托管 MCP 提示"
editorial: {"score": 66, "tier": "standard", "audience": "core"}
published: "2026-11-28T07:01:26+08:00"
sources: [{"title": "v2.1.326", "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.326"}]
---
<p lang="zh-CN">如果 Claude Code 没有按预期提供某个工具，可以先看启动提示。11 月 16 日发布的 v2.1.326 会在 --allowedTools、--disallowedTools 或 --tools 中发现疑似不完整的规则条目时给出启动警告。按 Ctrl+O 可以查看隐藏的启动提示。</p>

<p lang="en">If a tool you expect is missing in Claude Code, start with the startup notices. Version 2.1.326, released on November 16, warns at startup when an entry in --allowedTools, --disallowedTools, or --tools looks incomplete. Press Ctrl+O to reveal hidden startup notices.</p>

<p lang="zh-CN">如果 MCP 服务器在会话中停止加载，可查看会话内的提示。管理员在会话期间加入 managed-mcp.json 时，新版会说明服务器为何停止加载。若缺失的是某项功能，则可以打开 /status，查看它是否被服务提供商或 DISABLE_TELEMETRY 等环境变量停用。<a href="https://github.com/anthropics/claude-code/releases/tag/v2.1.326">官方发布说明</a></p>

<p lang="en">If MCP servers stop loading mid-session, check the session messages. The update explains why loading stops when an administrator adds managed-mcp.json during a session. For an unavailable feature, open /status to see whether your provider or an environment variable such as DISABLE_TELEMETRY disabled it. <a href="https://github.com/anthropics/claude-code/releases/tag/v2.1.326">Official release notes</a></p>
