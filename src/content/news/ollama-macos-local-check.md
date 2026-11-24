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
updated: "2026-11-24"
blocks: [{"kind": "steps", "title": {"zh": "按顺序排查", "en": "Work through the checks"}, "items": [{"zh": "打开 Ollama 应用并在终端查看模型清单。", "en": "Open the Ollama app and inspect the model list in a terminal."}, {"zh": "调用本机 HTTP 接口并检查响应。", "en": "Call the local HTTP endpoint and inspect the response."}]}, {"kind": "code", "title": {"zh": "本机检查命令", "en": "Local verification commands"}, "language": "bash", "file": "", "code": "ollama list\ncurl --fail --show-error http://localhost:11434/api/tags"}]
---

<p lang="zh-CN">本地客户端连不上时，先分别确认 Ollama 应用、模型列表和 HTTP 接口。先从官方页面下载 macOS 应用，移到 Applications 文件夹并打开。下载模型前查看磁盘空间、内存需求和模型许可证。</p>

<p lang="en">When a local client cannot connect, check the Ollama app, model inventory, and HTTP API individually. Download the macOS app from the official page, move it to Applications, and open it. Before downloading a model, check disk space, memory requirements, and the model license.</p>

<h2><span lang="zh-CN">怎样读检查结果</span><span lang="en">How to read the results</span></h2>

<p lang="zh-CN">新安装的模型列表可能为空。访问本地标签接口时，预期得到可解析的 JSON。连接被拒绝时，先检查应用是否已经启动，然后核对客户端地址和端口。默认检查在同一台机器完成。</p>

<p lang="en">A fresh installation may have an empty model list. The local tags endpoint should return JSON. If the connection is refused, check that the app is running, then verify the client address and port. Run the default check on the same machine.</p>
