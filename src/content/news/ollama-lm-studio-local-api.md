---
titleZh: "Ollama 与 LM Studio 的本地 API 怎么选"
titleEn: "Choosing between Ollama and LM Studio for a local API"
summaryZh: "按现有客户端接口和模型管理方式选择本地运行工具。"
summaryEn: "Choose a local runner based on your client protocol and model management needs."
type: "comparisons"
category: "models"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Current API documentation"
status: "current"
tested: false
tags: ["local-inference","apple-silicon"]
sources: [{"title":"Choosing between Ollama and LM Studio for a local API","url":"https://lmstudio.ai/docs/developer/openai-compat"},{"title":"Ollama macOS documentation","url":"https://docs.ollama.com/macos"}]
updated: "2026-11-24"
blocks: [{"kind": "comparison", "title": {"zh": "按现有客户端选入口", "en": "Choose by your existing client"}, "columns": [{"zh": "比较项", "en": "Criterion"}, {"zh": "Ollama 侧", "en": "Ollama"}, {"zh": "LM Studio 侧", "en": "LM Studio"}], "rows": [[{"zh": "操作入口", "en": "Starting point"}, {"zh": "终端命令与本地 API", "en": "Terminal commands and local API"}, {"zh": "桌面界面与兼容端点", "en": "Desktop interface and compatible endpoint"}], [{"zh": "已有客户端", "en": "Existing client"}, {"zh": "从客户端实际需要的方法开始，核对原生接口。", "en": "Start with the operations your client needs and check the native API."}, {"zh": "用已有 OpenAI 客户端验证所用的方法。", "en": "Check the methods you use with your existing OpenAI client."}], [{"zh": "第一项验证", "en": "First check"}, {"zh": "列出本机模型，确认目标模型已下载。", "en": "List local models and confirm the target model is present."}, {"zh": "向本地服务发送一个脱敏请求。", "en": "Send a request with nonsensitive data to the local server."}]]}]
---

<p lang="zh-CN">如果你已有一个 OpenAI 客户端，迁移前先列出它实际使用的方法。LM Studio 文档给出本地兼容服务地址 <code>http://localhost:1234/v1</code>。如果主要靠终端脚本启动和管理模型，Ollama 的 macOS 文档提供了对应的起点。</p>

<p lang="en">If you already have an OpenAI client, list the methods it actually uses before migrating. LM Studio documents its local compatible server at <code>http://localhost:1234/v1</code>. If shell scripts drive model startup and management, the Ollama macOS documentation provides a starting point.</p>

<p lang="zh-CN">模型权重的许可证需要单独核对。下面的选择表基于公开文档，未测吞吐、延迟或内存占用。</p>

<p lang="en">Check the license of the model weights separately. The table is based on public documentation. Throughput, latency, and memory use were not measured.</p>
