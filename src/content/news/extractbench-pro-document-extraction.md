---
category: "coding"
summaryEn: "The authors tested coding agents and specialized APIs on 100 synthetic documents. The best system was error-free on just 61% of documents, making whole-document accuracy a useful measure when budgeting for manual review."
summaryZh: "ExtractBench Pro 用 100 份合成文档比较编程 Agent 和专用 API。最佳系统的整文档零错率只有 61%，这个指标可用于估算直接入库前的人工复核量。"
tags: ["document-extraction", "benchmarks", "coding-agents"]
titleEn: "ExtractBench Pro finds even the best extractor gets only 61% of documents entirely right"
titleZh: "ExtractBench Pro 测复杂文档抽取，最佳系统也只完整抽对 61%"
blocks: [{"kind": "notice", "text": {"en": "When a document must be correct before it can be imported, use the error-free document rate to estimate how many documents will need review. Track Value F1, whether values are grounded in the source, and cost per page on the same test set.", "zh": "如果整份文档必须正确才能入库，可用整文档零错率估算复核量。在同一批验收样本上同时记录 Value F1、抽取值能否定位到原文，以及单页成本。"}, "title": {"en": "A PDF extraction acceptance check", "zh": "复杂 PDF 抽取验收"}}]
editorial: {"score": 83, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:16:12+08:00"
sources: [{"title": "ExtractBench Pro: The Long Tail of Document Extraction", "url": "https://arxiv.org/abs/2611.33791"}]
---
<p lang="zh-CN">如果复杂 PDF 要直接入库，少抽一个字段也可能让整份记录退回人工。11 月 26 日公布的 ExtractBench Pro v1 预印本用 100 份合成文档测试了 10 个编程 Agent 和 8 种专用抽取 API 配置。按作者报告，表现最好的系统也只在 61% 的文档上做到整份抽取零错。<a href="https://arxiv.org/abs/2611.33791">预印本</a></p>

<p lang="en">When data from a complex PDF goes straight into a database, a single missing field can send the whole record back for manual review. The ExtractBench Pro v1 preprint, announced on November 26, tested 10 coding agents and eight specialized extraction API configurations on 100 synthetic documents. The authors report that the best system extracted just 61% of documents without an error. <a href="https://arxiv.org/abs/2611.33791">Preprint</a></p>

<p lang="zh-CN">在这批样本中，作者报告 Claude Code 和 Codex 的最佳配置在整文档零错率和 Value F1 上领先专用 API，单页成本也更高。执行记录显示，Agent 有时误用文档内的定义，或漏掉图示中的关系。团队做采购试验时，可以把这两类页面加入同一批验收样本，再用整文档结果估算各配置的复核量。</p>

<p lang="en">On this test set, the authors report that the strongest Claude Code and Codex configurations beat the specialized APIs on error-free document rate and Value F1, at a higher cost per page. Agent traces showed mistakes such as misapplying definitions within a document and missing relationships in diagrams. A procurement trial can include both kinds of pages in a shared test set and use whole-document results to estimate the review burden for each configuration.</p>
