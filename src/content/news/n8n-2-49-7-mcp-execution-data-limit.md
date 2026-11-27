---
category: "agents"
summaryEn: "n8n’s stable update enforces the execution-data size limit on an MCP lookup tool, which affects how much data clients can retrieve from large workflow runs."
summaryZh: "n8n 稳定版更新让 MCP 查询工具遵守执行数据大小上限，客户端从大型工作流执行记录中可获取的数据量因此受到限制。"
tags: ["n8n", "mcp"]
titleEn: "n8n 2.49.7 enforces a size limit on workflow execution data returned through MCP"
titleZh: "n8n 2.49.7 对 MCP 返回的工作流执行数据实施大小限制"
published: "2026-11-27T22:45:30+08:00"
sources: [{"title": "stable", "url": "https://github.com/n8n-io/n8n/releases/tag/stable"}]
---
<p lang="zh-CN">n8n 于 2026 年 11 月 26 日发布稳定版 2.49.7，将执行数据大小上限应用到 MCP 工具 <code>get_workflow_execution</code>。通过 MCP 排查工作流的用户，在读取大型执行记录时可能拿不到全部数据。<a href="https://github.com/n8n-io/n8n/releases/tag/stable">n8n 稳定版发布记录</a></p>

<p lang="en">n8n released stable version 2.49.7 on November 26, 2026, applying the execution-data size limit to the MCP tool <code>get_workflow_execution</code>. Users debugging workflows through MCP may receive less data when inspecting large execution records. <a href="https://github.com/n8n-io/n8n/releases/tag/stable">n8n stable release notes</a></p>

<p lang="zh-CN">同一版本还降低了隔离表达式引擎对工作流数据数组执行 <code>concat</code> 时的内存占用，并让该引擎的 <code>extractUrlPath</code> 返回结果与旧版引擎一致。</p>

<p lang="en">The same release reduces memory use when the isolated expression engine runs <code>concat</code> on workflow data arrays. It also brings the engine’s <code>extractUrlPath</code> results in line with the legacy engine.</p>
