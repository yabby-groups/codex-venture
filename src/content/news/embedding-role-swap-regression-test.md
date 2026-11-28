---
category: "coding"
summaryEn: "Turn directional facts from your own corpus into ranking checks. A faithful paraphrase should rank above a sentence that swaps the two parties’ roles."
summaryZh: "从自己的语料抽取有方向的事实做排序检查。正确改写应排在互换双方角色的错句之前。"
tags: ["embeddings", "retrieval", "rag"]
titleEn: "Test whether embedding search preserves who did what to whom"
titleZh: "给向量检索加一道角色互换回归题"
blocks: [{"kind": "notice", "text": {"en": "The reported result comes from Beskorovainyi’s laptop test. The excerpt does not identify the model versions or provide the complete dataset. The workflow applies to whichever model and similarity measure your application actually uses.", "zh": "报道中的结果来自 Beskorovainyi 的笔记本测试。摘录未给出模型版本或完整数据。本文的测试流程适用于实际应用所用的模型和相似度度量。"}, "title": {"en": "Evidence and scope", "zh": "证据与适用范围"}}]
type: "workflows"
version: "Pairwise ranking workflow based on the author’s 2026-11-28 report"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 86, "tier": "featured", "audience": "core"}
published: "2026-11-28T20:01:09+08:00"
sources: [{"title": "What Is an Embedding? Two Models Rated “Boris Paid Anna” Closer Than the Right Answer", "url": "https://dev.to/vladimir_beskorovainyi/what-is-an-embedding-two-models-rated-boris-paid-anna-closer-than-the-right-answer-4o61"}]
---
<p lang="zh-CN">「安娜付给鲍里斯 100 美元」和「鲍里斯付给安娜 100 美元」共享姓名、金额和动作，却描述了方向相反的转账。Vladimir Beskorovainyi 报告，他在笔记本上用两个开放嵌入模型测了 55 个句对。在他尝试的 10 个角色互换案例中，两个模型都把互换后的句子排在正确改写前面，案例涉及英语和俄语。<a href="https://dev.to/vladimir_beskorovainyi/what-is-an-embedding-two-models-rated-boris-paid-anna-closer-than-the-right-answer-4o61">Besk orovainyi 的原始测试记录</a></p>

<p lang="en">“Anna paid Boris 100 dollars” and “Boris paid Anna 100 dollars” share the same names, amount, and action, but describe transfers in opposite directions. Vladimir Beskorovainyi reports testing two open embedding models on 55 sentence pairs on his laptop. In the 10 role-swap cases he tried, both models ranked the swapped sentence above a correct paraphrase. The cases covered English and Russian. <a href="https://dev.to/vladimir_beskorovainyi/what-is-an-embedding-two-models-rated-boris-paid-anna-closer-than-the-right-answer-4o61">Beskorovainyi’s test account</a></p>

<h2><span lang="zh-CN">把关系方向做成成对排序题</span><span lang="en">Turn relationship direction into a pairwise ranking test</span></h2>

<p lang="zh-CN">从自家搜索或 RAG 语料挑几条方向明确的事实。以每条事实为查询，准备一个保留原意的改写和一个只互换双方角色的难负例。以付款为例，正确改写可以是「鲍里斯从安娜那里收到 100 美元」，难负例则是「鲍里斯付给安娜 100 美元」。逐题核对姓名和金额，让关系方向成为判断答案的关键。</p>

<p lang="en">Pick a few facts with a clear direction from your search or RAG corpus. Use each fact as a query and write two candidates, a faithful paraphrase and a hard negative that swaps the parties’ roles. For the payment example, the paraphrase could be “Boris received 100 dollars from Anna” and the hard negative “Boris paid Anna 100 dollars.” Check the names and amount in each case so that the direction of the relationship determines the correct answer.</p>

<p lang="zh-CN">使用应用实际采用的嵌入模型和相似度度量，给同一查询的两个候选打分。通过条件是正确改写排在互换句之前。把反排和平分记在结果表里，同时保留模型版本、查询、两个候选和分数，方便更换模型后用原题复跑。这个成对检查衡量的是给定候选的排序，生产语料中的召回表现需要另行测量。</p>

<p lang="en">Use your application’s embedding model and similarity measure to score both candidates against the same query. The case passes when the faithful paraphrase ranks above the swap. Record reversals and ties alongside the model version, query, candidates, and scores so you can rerun the same cases after changing models. This pairwise check measures the ordering of supplied candidates. Recall across the production corpus needs its own measurement.</p>
