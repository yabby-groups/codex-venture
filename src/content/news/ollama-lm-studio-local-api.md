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
---
<p lang="zh-CN">在 macOS 上，Ollama 的文档从应用和终端命令入手，原生接口提供模型列表等能力。LM Studio 的文档提供兼容 OpenAI 客户端的本地接口，示例地址是 http://localhost:1234/v1。已有客户端时，先列出实际调用的方法，再逐个核对支持情况。</p>

<p lang="en">On macOS, Ollama’s documentation starts with the app and terminal commands, and its native API includes operations such as listing models. LM Studio documents a local OpenAI-compatible endpoint at http://localhost:1234/v1. For an existing client, list the methods you actually call and check support for each one.</p>

<p lang="zh-CN">这是一份文档对比。依赖本地桌面界面和已有 OpenAI 客户端的团队，可以先用 LM Studio 的兼容端点验证一个请求。依赖终端脚本的团队，可以先评估 Ollama 的启动和模型管理流程。本文未测吞吐、延迟与内存消耗，使用的模型权重仍适用各自的许可证。</p>

<p lang="en">This comparison uses documentation. Teams with an existing OpenAI client and a preference for a desktop UI can try one request against LM Studio’s compatible endpoint. Teams with shell scripts can start by evaluating Ollama’s startup and model management workflow. Throughput, latency, and memory were not tested. Model weights carry their own licenses.</p>
