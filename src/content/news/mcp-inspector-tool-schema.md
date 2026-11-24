---
titleZh: "用 MCP Inspector 检查工具的输入结构"
titleEn: "Inspect tool inputs with MCP Inspector"
summaryZh: "在连接日常客户端之前，先查看工具清单与参数。"
summaryEn: "Review the tool list and arguments before connecting a day-to-day client."
type: "tools"
category: "agents"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Inspector v2 documentation"
status: "current"
tested: false
project: "mcp-inspector"
tags: ["mcp","developer-tools"]
sources: [{"title":"Inspect tool inputs with MCP Inspector","url":"https://github.com/modelcontextprotocol/inspector"}]
---
<p lang="zh-CN">MCP Inspector 为调试服务器提供网页界面与 CLI。调试自建服务时，先连接隔离环境中的测试实例，列出工具与参数，再用一条公开样本检查响应结构。这样能把协议问题和宿主的调用行为分别定位。</p>

<p lang="en">MCP Inspector provides a web interface and CLI for debugging servers. For your own server, first connect to an isolated test instance, list tools and arguments, and use a public sample to inspect the response shape. This helps identify protocol issues separately from host behavior.</p>

<p lang="zh-CN">README 将 npm 包 @modelcontextprotocol/inspector 列作启动入口。连接本地进程前核对其启动命令、环境变量与文件访问范围。只列工具与实际调用工具是不同操作，调用可能触发真实写入。本文未运行 Inspector。</p>

<p lang="en">The README lists the npm package @modelcontextprotocol/inspector as the launcher. Before connecting a local process, check its command, environment variables, and file scope. Listing tools and invoking them are different operations, and invocation may make real writes. We did not run Inspector.</p>
