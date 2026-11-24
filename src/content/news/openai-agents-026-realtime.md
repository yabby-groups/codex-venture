---
titleZh: "OpenAI Agents SDK 0.26 修正实时链路的防护检查时机"
titleEn: "OpenAI Agents SDK 0.26 adjusts Realtime guardrail timing"
summaryZh: "SDK 在轮次结束时检查 Realtime 输出防护规则，并让单次调用的 MCP 元数据优先于发现阶段的默认值。"
summaryEn: "The SDK checks Realtime output guardrails at turn completion and prioritizes per-call MCP metadata over discovery defaults."
published: "2026-11-24T15:01:03+08:00"
category: "agents"
tags: ["agents-sdk", "realtime", "mcp"]
sources:
  - title: "openai-agents-python v0.26.0 release notes"
    url: https://github.com/openai/openai-agents-python/releases/tag/v0.26.0
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 24 日（北京时间），openai-agents-python 发布 v0.26.0。SDK 在轮次结束时检查 Realtime 输出防护规则，并让单次调用的 MCP 元数据优先于发现阶段的默认值。</p>

<p lang="en">openai-agents-python published v0.26.0 on November 24 (China Standard Time). The SDK checks Realtime output guardrails at turn completion and prioritizes per-call MCP metadata over discovery defaults.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">实时助手的开发者可检查最后一段输出如何进入应用的防护流程。多个调用共享同一工具时，也可验证每次传入的元数据能否覆盖发现阶段的值。</p>

<p lang="en">Realtime assistant developers can check how the end of an output turn enters their guardrail flow. When calls share a tool, they can also verify that call-specific metadata overrides values from discovery.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">从发布页获取 Python SDK 0.26.0。流式界面需要按自己的显示和播放时序验证，最终检查与中途的用户可见行为需要分别观察。</p>

<p lang="en">Get Python SDK 0.26.0 from the release page. Validate your own display and playback timing, and observe both the final check and what users see during streaming.</p>
