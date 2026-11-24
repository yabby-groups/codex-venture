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
updated: "2026-11-24"
blocks: [{"kind": "code", "title": {"zh": "只读 stdio 配置示例", "en": "Example read-only stdio configuration"}, "language": "json", "code": "{\n  \"mcpServers\": {\n    \"sample-files\": {\n      \"command\": \"npx\",\n      \"args\": [\n        \"-y\",\n        \"@modelcontextprotocol/server-filesystem\",\n        \"--read-only\",\n        \"--confine-roots\",\n        \"/absolute/path/to/public-samples\"\n      ]\n    }\n  }\n}"}, {"kind": "steps", "title": {"zh": "确认宿主实际开放了哪些目录", "en": "Check which directories the host exposes"}, "items": [{"zh": "把示例路径换成实际存在的公开样本目录。只读标志会去掉写入工具。", "en": "Replace the example path with an existing public sample directory. The read-only flag removes write tools."}, {"zh": "如果宿主提供 Roots，限制标志会将可用目录限定在 Roots 与命令行目录的交集。连接后用 list_allowed_directories 查看实际范围。", "en": "If the host supplies Roots, the confinement flag limits access to their overlap with the command-line directories. After connecting, inspect the effective scope with list_allowed_directories."}]}]
---
<p lang="zh-CN">MCP 官方服务器示例仓库提供 Filesystem Server。文档区分带写入能力的目录与只读目录。用几份公开样本搭建文档检索时，可只开放样本目录，并使用文档列出的 list_allowed_directories 确认生效范围。</p>

<p lang="en">The official MCP reference server repository includes Filesystem Server. Its documentation distinguishes writable directories from read-only ones. For a document lookup exercise, expose only a sample directory and confirm the effective scope with the documented list_allowed_directories tool.</p>

<p lang="zh-CN">README 的本地 npx 用法要求 Node.js 24 或更新版本，服务器为 MIT 许可证。支持 stdio 的宿主可按文档配置本地进程。文件读取本身仍会向宿主暴露内容，应同时核对宿主是否把结果发送给远程模型。本文未安装或运行该服务器。</p>

<p lang="en">The README’s local npx path requires Node.js 24 or newer, and the server is MIT-licensed. A host that supports stdio can configure a local process as documented. Reading still exposes file contents to the host, so check whether it sends tool results to a remote model. We did not install or run the server.</p>
