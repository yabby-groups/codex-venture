---
category: "open-source"
summaryEn: "LiteLLM 1.108.17 LTS fixes empty arguments in streamed OpenAI tool calls and restores budget enforcement for Agents API session calls routed through the gateway."
summaryZh: "LiteLLM 1.108.17 LTS 修复了 OpenAI 流式工具调用参数为空的问题，并恢复了网关对 OpenAI Agents API 会话调用的预算约束。"
tags: ["litellm", "openai", "tool-calling"]
titleEn: "LiteLLM 1.108.17 LTS fixes streamed tool calls and Agents API budgets"
titleZh: "LiteLLM 1.108.17 LTS 修复流式工具调用和 Agents API 预算问题"
published: "2026-11-25T19:28:24+08:00"
sources: [{"title": "1.108.17 (LTS)", "url": "https://github.com/BerriAI/litellm/releases/tag/v1.108.17"}]
---
<p lang="zh-CN">LiteLLM 于 2026 年 11 月 24 日发布 1.108.17 LTS。此前，通过 LiteLLM 接入 OpenAI 的智能体可能收到参数为空的工具调用，问题发生在 OpenAI 直到流式响应末尾才发送参数时。此次更新修复了这一路径。</p>

<p lang="en">LiteLLM released 1.108.17 LTS on November 24, 2026. Agents using OpenAI through LiteLLM could receive tool calls with empty arguments when OpenAI sent those arguments only at the end of the stream. The release fixes that behavior.</p>

<p lang="zh-CN">这次更新还影响网关的预算管理。此前，经由 <code>/openai</code> 转发的 OpenAI Agents API 会话调用会被记录为 0 美元。修复后，LiteLLM 的密钥和团队预算可以覆盖这些调用。发布说明也列出一项兼容性修复，解决 <code>chat-latest</code> 和 <code>gpt-chat-latest</code> 在 OpenAI、Azure 和 Azure AI 上首条提示返回 HTTP 400 的问题。</p>

<p lang="en">The update also affects gateway budget enforcement. OpenAI Agents API session calls routed through <code>/openai</code> previously logged zero cost. With the fix, LiteLLM’s key and team budgets apply to those calls. The release also fixes an HTTP 400 on the first prompt when using <code>chat-latest</code> or <code>gpt-chat-latest</code> with OpenAI, Azure, or Azure AI.</p>
