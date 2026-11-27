---
category: "open-source"
summaryEn: "LiteLLM’s LTS gateway adds Volcengine Ark Seedream support for image generation and editing, with pricing support. Gemini requests that produce no image now return an error."
summaryZh: "LiteLLM 长期支持版网关接入火山方舟 Seedream 的图像生成、编辑和价格支持。Gemini 生图请求未产出图像时，现在会返回错误。"
tags: ["litellm", "ai-gateway", "seedream", "gemini", "azure"]
titleEn: "LiteLLM 1.108.19 LTS adds Seedream and fixes empty Gemini image responses"
titleZh: "LiteLLM 1.108.19 LTS 接入 Seedream，修复 Gemini 生图空响应"
published: "2026-11-27T15:03:50+08:00"
sources: [{"title": "1.108.19 (LTS)", "url": "https://github.com/BerriAI/litellm/releases/tag/v1.108.19"}]
---
<p lang="zh-CN">LiteLLM 于 2026 年 11 月 26 日发布 1.108.19 LTS。根据官方发布记录，此前经网关发出的 Gemini 生图请求在未生成图像时，可能仍返回计费的 HTTP 200 响应，且 <code>data</code> 为空。新版会在这种情况下返回错误，让调用方能通过错误处理流程识别失败。</p>

<p lang="en">LiteLLM released 1.108.19 LTS on November 26, 2026. According to the release notes, Gemini image requests routed through the gateway could return a billed HTTP 200 response with an empty <code>data</code> field when no image was generated. The release returns an error in that case, so clients can detect the failure through their usual error handling.</p>

<p lang="zh-CN">Azure 集成也有两项修复。音频转录现在会采用部署配置的 API 版本，修复了 <code>api_version="v1"</code> 被忽略后请求返回 HTTP 500 的问题。Document Intelligence OCR 现在会读取 <code>pages</code> 和 <code>outputContentFormat</code> 等请求选项，让调用方可以指定识别页码和输出格式。</p>

<p lang="en">The release also fixes two Azure integrations. Audio transcription now honors the deployment’s API version, addressing an HTTP 500 failure when <code>api_version="v1"</code> was ignored. Document Intelligence OCR now honors request options such as <code>pages</code> and <code>outputContentFormat</code>, so callers can select which pages to process and specify the output format.</p>
