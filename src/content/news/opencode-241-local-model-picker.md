---
titleZh: "OpenCode 2.4.1 补齐本地模型列表"
titleEn: "OpenCode 2.4.1 restores local models to the picker"
summaryZh: "只通过配置添加的模型提供商现可显示在模型选择器，macOS 12 的会话保存问题也得到修复。"
summaryEn: "Providers added through configuration now appear in the model picker, and session saving on macOS 12 is fixed."
published: "2026-11-24T15:01:03+08:00"
category: "coding"
tags: ["opencode", "ollama"]
sources:
  - title: "opencode v2.4.1 release notes"
    url: https://github.com/anomalyco/opencode/releases/tag/v2.4.1
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 23 日（北京时间），opencode 发布 v2.4.1。只通过配置添加的模型提供商现可显示在模型选择器，macOS 12 的会话保存问题也得到修复。</p>

<p lang="en">opencode published v2.4.1 on November 23 (China Standard Time). Providers added through configuration now appear in the model picker, and session saving on macOS 12 is fixed.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">已经配置 Ollama 的用户可以直接从 /models 选用模型。版本说明把旧 macOS 的保存问题归因于系统 SQLite 不支持上一版所用的 JSON 运算符。</p>

<p lang="en">Users with Ollama configured can select models directly from /models. The release notes attribute the macOS 12 save failure to the system SQLite lacking a JSON operator used by the preceding version.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">依据版本页更新 OpenCode。配置仍需指向可访问的模型服务，可分别验证模型列表、实际连接和重启后的会话读取。</p>

<p lang="en">Update OpenCode from the release page. The configured model service must be reachable. Check the picker, the connection and session loading after restart separately.</p>
