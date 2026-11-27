---
category: "coding"
summaryEn: "Use Scrubly’s documented placeholder workflow to redact IBANs and email addresses before sending a prompt, then restore values in the application when needed."
summaryZh: "用 Scrubly 的占位符流程，在发送提示词前替换 IBAN 和邮箱地址，再按需在应用侧还原。"
tags: ["llm", "redaction", "typescript"]
titleEn: "Redact IBANs and email addresses before sending an LLM prompt"
titleZh: "在发送 LLM 提示词前替换 IBAN 和邮箱地址"
blocks: [{"kind": "notice", "text": {"en": "Before connecting a model, use a synthetic fixture that repeats the same email address. Check that the outgoing text uses the same placeholder both times and that restoration yields the expected result. The author's example leaves the behavior for altered placeholders unspecified.", "zh": "接入模型前，用重复出现同一邮箱地址的合成样例检查两件事：待发送文本是否两次使用同一占位符，还原结果是否符合预期。作者的示例未说明占位符被改写后的行为。"}, "title": {"en": "Check placeholder handling with synthetic data", "zh": "用合成数据检查占位符"}}]
type: "workflows"
version: "Scrubly redact/restore example published 2026-11-27"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T22:01:31+08:00"
sources: [{"title": "I kept finding credit card numbers in LLM prompts, so I wrote a redactor", "url": "https://dev.to/shilpi_daswani/i-kept-finding-credit-card-numbers-in-llm-prompts-so-i-wrote-a-redactor-5d0l"}]
---
<p lang="zh-CN">如果摘要功能直接把整段对话拼进提示词，脱敏就应放在组装请求之前。Scrubly 作者 Shilpi Daswani 在原文中用一条同时含有 IBAN 和邮箱地址的消息演示了这个接入点。同一次调用中，重复出现的同一 IBAN 会使用相同的占位符，因此模型仍能看出这些位置指的是同一个值。<a href="https://dev.to/shilpi_daswani/i-kept-finding-credit-card-numbers-in-llm-prompts-so-i-wrote-a-redactor-5d0l">作者示例</a></p>

<p lang="en">If a summarizer inserts an entire conversation into a prompt, redact the conversation before assembling the request. Scrubly author Shilpi Daswani demonstrates this integration point with a message containing both an IBAN and an email address. Repeated occurrences of the same IBAN get the same placeholder within a call, so the model can still tell that those references point to one value. <a href="https://dev.to/shilpi_daswani/i-kept-finding-credit-card-numbers-in-llm-prompts-so-i-wrote-a-redactor-5d0l">Author’s example</a></p>

<p lang="zh-CN">按作者的接口示例，先用 <code>redact</code> 处理输入，只把返回的 <code>text</code> 拼入发给模型的提示词。回复到达应用后，再根据展示场景决定是否调用同次返回的 <code>restore</code>。如果下游只需要脱敏摘要，可以直接保留含占位符的回复。本文依据作者公开示例整理，适用范围是该示例展示的接口和数据类型。</p>

<p lang="en">In the author’s API example, call <code>redact</code> on the input and use only the returned <code>text</code> when building the model prompt. When the reply reaches the application, decide whether to call the accompanying <code>restore</code> based on what the recipient needs to see. If the downstream consumer only needs a redacted summary, keep the reply with its placeholders. This documentation-based workflow covers the interface and data types shown in the author’s example.</p>
