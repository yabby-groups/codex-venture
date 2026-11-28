---
category: "models"
summaryEn: "Azure Content Understanding added three GPT model families. Microsoft recommends starting with GPT-6.1 Sol for standard document extraction and reports a 0.21 percentage point lead for the higher-token-cost GPT-6 Astra in one GA evaluation."
summaryZh: "Azure Content Understanding 新增三个 GPT 模型系列。微软建议标准文档抽取从 GPT-6.1 Sol 起测。在一项正式版评估中，token 开销更高的 GPT-6 Astra 领先 0.21 个百分点。"
tags: ["azure-content-understanding", "document-extraction", "model-selection"]
titleEn: "Azure Content Understanding Adds New GPT Models, With GPT-6.1 Sol as the Starting Point for Extraction"
titleZh: "Azure Content Understanding 扩充 GPT 模型选项，文档抽取建议先试 GPT-6.1 Sol"
editorial: {"score": 68, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T12:45:54+08:00"
sources: [{"title": "Content Understanding adds GPT-6.1, 6, and 5.6: Choose the right model for your workload", "url": "https://devblogs.microsoft.com/foundry/content-understanding-adds-gpt-5-6-gpt-6-and-gpt-6-1-choose-the-right-model-for-your-workload"}]
---
<p lang="zh-CN">微软在 11 月 11 日宣布，Azure Content Understanding 已加入 GPT-5.6、GPT-6 和 GPT-6.1 系列，为文档、文本、语音和视频工作流增加了模型选项。微软 Foundry 博客署名作者、首席产品经理 Joe Filcik 建议，标准文档抽取可以从 GPT-6.1 Sol 起测。<a href="https://devblogs.microsoft.com/foundry/content-understanding-adds-gpt-5-6-gpt-6-and-gpt-6-1-choose-the-right-model-for-your-workload">微软 Foundry 博客</a></p>

<p lang="en">Microsoft announced on November 11 that Azure Content Understanding had added the GPT-5.6, GPT-6, and GPT-6.1 families, expanding model choice for document, text, speech, and video workflows. Writing on the Microsoft Foundry Blog, principal product manager Joe Filcik recommends starting with GPT-6.1 Sol for standard document extraction. <a href="https://devblogs.microsoft.com/foundry/content-understanding-adds-gpt-5-6-gpt-6-and-gpt-6-1-choose-the-right-model-for-your-workload">Microsoft Foundry Blog</a></p>

<p lang="zh-CN">在微软公布的一项正式版（GA）文档抽取评估中，GPT-6 Astra 得分 95.95%，GPT-6.1 Sol 得分 95.74%，相差 0.21 个百分点，Astra 的 token 开销则明显更高。Sol 在另一项预览版抽取评估中领先。对于表单、合同或票据抽取，可以用同一批代表性文档测出 Sol 的基线，在填错代价高的字段上试 Astra，再用 GPT-6 Luna 测 token 预算紧的批次。分别记录关键字段错误和 token 用量，才能判断微软评估中的取舍是否适用于自己的文档。</p>

<p lang="en">In one Microsoft evaluation of generally available document extraction, GPT-6 Astra scored 95.95% and GPT-6.1 Sol scored 95.74%, a gap of 0.21 percentage points, with substantially higher token cost for Astra. Sol led a separate preview extraction evaluation. For forms, contracts, or receipts, teams can use the same representative documents to establish a Sol baseline, try Astra on fields where mistakes are costly, and test GPT-6 Luna for batches with tight token budgets. Track errors on critical fields and token use to see whether the trade-off in Microsoft’s evaluation holds for your documents.</p>
