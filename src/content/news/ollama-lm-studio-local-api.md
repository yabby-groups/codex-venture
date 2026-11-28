---
titleZh: "Ollama 和 LM Studio 都能接 OpenAI 客户端，先试你用的那个端点"
titleEn: "Ollama and LM Studio both take OpenAI clients. Start with the endpoint you use"
summaryZh: "换本地模型服务前，用同一个小请求验证接口，再决定要不要改客户端。"
summaryEn: "Before switching local model servers, try the same small request on both and see whether your client needs changes."
type: "comparisons"
category: "models"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Current API documentation"
status: "current"
tested: false
tags: ["local-inference","apple-silicon"]
sources: [{"title":"Ollama OpenAI compatibility","url":"https://docs.ollama.com/api/openai-compatibility"},{"title":"Choosing between Ollama and LM Studio for a local API","url":"https://lmstudio.ai/docs/developer/openai-compat"},{"title":"Ollama native API","url":"https://docs.ollama.com/api/introduction"},{"title":"Ollama macOS documentation","url":"https://docs.ollama.com/macos"}]
updated: "2026-11-28"
---
<p lang="zh-CN">把已有 OpenAI 客户端接到本地时，两个入口都值得先试。Ollama 的兼容地址是 <code>http://localhost:11434/v1</code>，LM Studio 的文档示例用 <code>http://localhost:1234/v1</code>。切换时还要换成各自服务里可用的模型标识。</p>

<p lang="en">You can start with either server if you already have an OpenAI client. Ollama’s compatible base URL is <code>http://localhost:11434/v1</code>. LM Studio’s documentation uses <code>http://localhost:1234/v1</code>. When you switch, also set the model ID to one available on that server.</p>

<p lang="zh-CN">如果脚本实际用的是 <code>POST /v1/chat/completions</code>，先在两个本地服务上用同一条无敏感内容的短消息试一次。看客户端能否解析回答。只有业务用流式时，再核对分段和结束条件。用其他端点时，逐项查两份兼容文档。<a href="https://docs.ollama.com/api/openai-compatibility">Ollama 兼容接口</a> · <a href="https://lmstudio.ai/docs/developer/openai-compat">LM Studio 兼容接口</a></p>

<p lang="en">If your script calls <code>POST /v1/chat/completions</code>, send the same short, non-sensitive prompt to both local servers. Check that the client can parse the reply. If your workflow streams, check the chunk format and termination as well. For other endpoints, check the compatibility docs for each server. <a href="https://docs.ollama.com/api/openai-compatibility">Ollama compatibility</a> · <a href="https://lmstudio.ai/docs/developer/openai-compat">LM Studio compatibility</a></p>

<p lang="zh-CN">客户端要是两边都能跑，再根据模型管理方式选。偏好桌面界面可从 LM Studio 开始，已有 Ollama 原生 API 脚本则可继续沿用。先把基地址和模型标识放在配置里，回退时只需改配置。</p>

<p lang="en">If the client works with both, choose by how you want to manage models. LM Studio is a starting point if you prefer a desktop interface. If you already have scripts built around Ollama’s native API, you can keep using them. Put the base URL and model ID in configuration so you can switch back easily.</p>
