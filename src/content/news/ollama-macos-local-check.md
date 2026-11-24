---
titleZh: "在 macOS 上确认 Ollama 本地服务"
titleEn: "Verify an Ollama service on macOS"
summaryZh: "把应用启动、模型是否下载和本地 API 是否通分别检查。"
summaryEn: "Check app startup, model availability, and local API connectivity separately."
type: "tutorials"
category: "models"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Current macOS documentation"
status: "current"
tested: false
tags: ["local-inference","ollama"]
sources: [{"title":"Verify an Ollama service on macOS – primary reference","url":"https://docs.ollama.com/macos"}]
---
<p lang="zh-CN">从 Ollama 官方 macOS 页面下载应用，移入 Applications 并打开。确保下载目录有足够空间，并先查看模型的尺寸、许可证和内存需求。在终端运行 <code>ollama list</code> 查看已下载模型。刚安装时列表可能为空。</p>

<p lang="en">Download Ollama from its official macOS page, move it to Applications, and open it. Check disk space and review model size, license, and memory needs. Run <code>ollama list</code> to see downloaded models. A fresh install may return an empty list.</p>

<p lang="zh-CN">可从同一台机器访问 <code>http://localhost:11434/api/tags</code>，预期得到可解析的 JSON 模型列表。连接被拒绝时先确认应用已启动。仅在本机测试默认地址，避免把服务端口直接暴露到公网。命令依据文档整理，本站未安装实测。</p>

<p lang="en">From the same machine, request <code>http://localhost:11434/api/tags</code> and expect a parseable JSON model list. If the connection is refused, check that the app is running first. Test the default address locally and avoid exposing the service directly to the public internet. These steps are documentation-based and were not run by this site.</p>
