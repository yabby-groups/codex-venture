---
titleZh: "Context7 如何给 Agent 提供库文档"
titleEn: "How Context7 supplies library documentation to agents"
summaryZh: "用库名和版本缩小检索范围，并检查远程请求的数据。"
summaryEn: "Narrow documentation lookup by library name and version, and check what remote requests contain."
type: "mcp"
category: "coding"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "README / main"
status: "current"
tested: false
project: "context7"
tags: ["mcp","context7"]
sources: [{"title":"How Context7 supplies library documentation to agents – primary reference","url":"https://github.com/upstash/context7"}]
resource: {"id": "context7", "type": "mcp", "name": "Context7", "summary": ["按库名与版本向 Agent 提供文档和用法。", "Give agents library documentation and examples by name and version."], "categories": [["软件开发", "Software development"]], "site": "https://github.com/upstash/context7", "repository": "https://github.com/upstash/context7", "deployment": "Remote", "notes": ["按文档配置 API 密钥。避免查询携带私有代码。", "Configure an API key as documented. Keep private code out of queries."], "featured": true}
---
<p lang="zh-CN">Upstash 的 Context7 是社区维护的文档检索服务。遇到依赖库改版时，可以给 Agent 明确的库名和版本，要求它核对当前接口，再把结果与本地锁文件和项目文档对照。</p>

<p lang="en">Upstash’s Context7 is a community-maintained documentation lookup service. When a dependency changes, give the agent the library name and version and ask it to check the current interface, then compare the result with the local lockfile and upstream documentation.</p>

<p lang="zh-CN">README 给出的远程 MCP 端点是 mcp.context7.com/mcp，并说明如何用 Authorization 请求头携带 API 密钥。启用前确认宿主发送的检索词和上下文，避免在查询中附带私有代码。限额和收费以服务商当前条款为准。本文依据文档整理。</p>

<p lang="en">The README lists mcp.context7.com/mcp as the remote MCP endpoint and documents passing an API key in the Authorization header. Check which queries and context your host sends, and keep private code out of lookups. Consult current provider terms for limits and charges. This profile is documentation-based.</p>
