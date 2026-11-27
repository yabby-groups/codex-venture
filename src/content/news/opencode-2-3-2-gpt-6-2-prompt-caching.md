---
category: "coding"
summaryEn: "OpenCode v2.3.2 moves the system prompt from the Responses instructions field to a leading developer message, letting GPT-6.2 reuse the cached prefix from the second step."
summaryZh: "OpenCode v2.3.2 把系统提示从 Responses 的 instructions 字段移到首条 developer 消息，让 GPT-6.2 从第二步起复用缓存前缀。"
tags: ["opencode", "gpt-6-2", "prompt-caching", "responses-api"]
titleEn: "OpenCode 2.3.2 fixes GPT-6.2 prompt caching across agent steps"
titleZh: "OpenCode 2.3.2 修复 GPT-6.2 多步会话的提示词缓存"
editorial: {"score": 86, "tier": "featured", "audience": "core"}
published: "2026-11-28T06:32:25+08:00"
sources: [{"title": "v2.3.2", "url": "https://github.com/anomalyco/opencode/releases/tag/v2.3.2"}]
---
<p lang="zh-CN">OpenCode 在 2026 年 11 月 18 日发布的 v2.3.2 中修复了 GPT-6.2 多步会话的提示词缓存。此前，OpenCode 把系统提示放在 Responses 请求的 instructions 字段中，GPT-6.2 会在每一步把这段固定提示计为未缓存输入。新版把它放进请求开头的 developer 消息，让后续步骤从第二步起复用缓存前缀。</p>

<p lang="en">OpenCode v2.3.2, released November 18, 2026, fixes prompt caching in multi-step GPT-6.2 sessions. OpenCode previously put its system prompt in the Responses instructions field, so GPT-6.2 counted the same prompt as uncached input on every step. The new version sends it as the leading developer message, so requests can reuse the cached prefix starting with the second step.</p>

<p lang="zh-CN">改动覆盖 OpenCode 的 Responses 路由，包括 OpenAI（API 密钥和 ChatGPT 登录）、GitHub Copilot、Zen、Azure 和 OpenRouter。发布说明还指出，经由 /responses/compact 进行上下文压缩时，也会读取同一缓存前缀。</p>

<p lang="en">The change applies to OpenCode’s Responses routes, including OpenAI via API key or ChatGPT sign-in, GitHub Copilot, Zen, Azure, and OpenRouter. The release notes also say that context compaction through /responses/compact reads the same cached prefix.</p>

<p lang="zh-CN">OpenCode 发布说明记录了一个 GitHub Copilot 的 gpt-6.2-sol 个案，每步未缓存输入从约 14,000 个 token 降至 3 个。排查类似用量时，可以先对照同一模型和路由的首步与后续步骤，分别查看缓存和未缓存输入，再核对固定提示词在请求中的位置。实际费用取决于所用服务的计费规则。</p>

<p lang="en">OpenCode’s release notes report that uncached input fell from about 14,000 tokens per step to 3 in one GitHub Copilot case using gpt-6.2-sol. To investigate a similar usage pattern, compare cached and uncached input on the first and later steps of a session using the same model and route, then check where the client places the fixed prompt. The effect on the bill depends on the provider’s pricing.</p>
