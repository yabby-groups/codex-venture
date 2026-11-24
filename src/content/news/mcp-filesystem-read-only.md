---
titleZh: "用 MCP Filesystem 限定文档访问范围"
titleEn: "Limit document access with MCP Filesystem"
summaryZh: "检查目录白名单和只读访问，给文件工具一个清晰边界。"
summaryEn: "Use allowed directories and read-only access to scope a file tool."
type: "mcp"
category: "agents"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Node.js 24+ / main"
status: "current"
tested: false
project: "mcp-filesystem"
tags: ["mcp","mcp"]
sources: [{"title":"Limit document access with MCP Filesystem – primary reference","url":"https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem"}]
---
<p lang="zh-CN">MCP 官方服务器示例仓库提供 Filesystem Server。文档区分带写入能力的目录与只读目录。用几份公开样本搭建文档检索时，可只开放样本目录，并使用文档列出的 list_allowed_directories 确认生效范围。</p>

<p lang="en">The official MCP reference server repository includes Filesystem Server. Its documentation distinguishes writable directories from read-only ones. For a document lookup exercise, expose only a sample directory and confirm the effective scope with the documented list_allowed_directories tool.</p>

<p lang="zh-CN">README 的本地 npx 用法要求 Node.js 24 或更新版本，服务器为 MIT 许可证。支持 stdio 的宿主可按文档配置本地进程。文件读取本身仍会向宿主暴露内容，应同时核对宿主是否把结果发送给远程模型。本文未安装或运行该服务器。</p>

<p lang="en">The README’s local npx path requires Node.js 24 or newer, and the server is MIT-licensed. A host that supports stdio can configure a local process as documented. Reading still exposes file contents to the host, so check whether it sends tool results to a remote model. We did not install or run the server.</p>
