---
category: "coding"
summaryEn: "PromptShield’s documented workflow reuses placeholders for repeated sensitive values and uses a local mapping to restore them in a model reply."
summaryZh: "PromptShield 的页面流程为重复的敏感值复用占位符，并通过本地映射还原模型回复中保留下来的占位符。"
tags: ["promptshield", "redaction", "privacy"]
titleEn: "How PromptShield keeps repeated email references intact during redaction"
titleZh: "PromptShield 用同一个占位符替换重复邮箱，再在本地还原"
type: "insights"
version: "官方页面，2026-11-28 核对 / Product page reviewed 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 79, "tier": "standard", "audience": "core"}
published: "2026-11-28T10:04:10+08:00"
sources: [{"title": "Show HN: PromptShield – Local reversible secret/PII redactor for LLM prompts", "url": "https://hxu129.github.io/scholarcraft-tools/promptshield/index.html"}]
---
<p lang="zh-CN">一段客服记录可能在抬头、转发正文和签名里反复出现同一个邮箱。PromptShield 官方页面说明，重复出现的敏感值会复用同一个占位符，例如 [EMAIL_1]。这样，发给模型的文本仍能表示这些位置指的是同一个地址。<a href="https://hxu129.github.io/scholarcraft-tools/promptshield/index.html">PromptShield 官方页面</a></p>

<p lang="en">A support transcript can repeat the same email address in a header, a forwarded message, and a signature. The official PromptShield page says repeated sensitive values reuse a placeholder such as [EMAIL_1]. The text sent to the model can still show that those references point to the same address. <a href="https://hxu129.github.io/scholarcraft-tools/promptshield/index.html">PromptShield product page</a></p>

<p lang="zh-CN">按页面显示的流程，可以先加载演示样本，核对高亮结果和映射表，再复制脱敏文本。页面也提供演示回复，可用来查看占位符怎样还原。处理真实回复时，把模型的回复粘回页面，让恢复功能按映射表替换保留下来的占位符。项目方把映射表标为本地使用，并提醒不要将恢复映射上传给外部 AI。</p>

<p lang="en">The page’s documented flow starts with a demo sample. Review the highlighted redactions and their mappings before copying the redacted text. The page also supplies a demo reply for inspecting how restoration works. With a real reply, paste it back into the page so the restoration feature can replace intact placeholders using the mapping. The project identifies that mapping as local and warns against uploading it to an external AI service.</p>

<p lang="zh-CN">官方页面将多文件 ZIP 导出和完整批量恢复映射下载列为 Pro 功能。本文依据页面说明，未验证检测覆盖、联网行为或模型保留占位符的表现。发送真实资料前，仍需逐段核对复制出去的文本。</p>

<p lang="en">The page lists multi-file ZIP export and download of the full batch restoration map as Pro features. This article draws on the page and did not test detection coverage, network behavior, or how consistently a model preserves placeholders. Review the text you intend to send before using it with real records.</p>
