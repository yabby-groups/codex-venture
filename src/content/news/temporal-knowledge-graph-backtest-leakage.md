---
category: "models"
summaryEn: "Five of six models beat a historical baseline when given the newest knowledge graph. The authors traced the apparent improvement to retrieval paths that usually contained the later trial itself."
summaryZh: "使用最新版知识图谱时，六个模型中有五个明显超过历史基线。作者检查检索路径后发现，其中通常已经包含预测日期之后才发生的试验。"
tags: ["rag", "backtesting", "data-leakage"]
titleEn: "A clinical-trial forecasting study finds future answers in the retrieval graph"
titleZh: "临床试验预测回测发现，最新版图谱泄漏了未来结果"
editorial: {"score": 87, "tier": "featured", "audience": "core"}
published: "2026-11-28T22:16:12+08:00"
sources: [{"title": "Did the Model Forecast It, or Already Know It? Evaluating Large Language Models for Novel Drug-Target Prioritisation with a Temporal Knowledge-Graph Oracle", "url": "https://arxiv.org/abs/2611.34247"}]
---
<p lang="zh-CN">用今天的知识库重跑去年的预测，检索结果可能直接带回后来发生的事件。11 月 26 日公布的一篇预印本用药物靶点与疾病配对的首次临床试验来检查这个问题。作者重建逐年冻结的知识图谱，让六个开放语言模型预测哪些配对会在下一年首次进入临床试验。<a href="https://arxiv.org/abs/2611.34247">预印本</a></p>

<p lang="en">Replay last year’s forecast against today’s knowledge base and retrieval may bring back the very event the model is supposed to predict. A preprint announced on November 26 examines this problem using the first clinical trial for a drug target–disease pair. The authors reconstructed annual knowledge graph snapshots and asked six open language models which pairs would enter a first trial the following year. <a href="https://arxiv.org/abs/2611.34247">Preprint</a></p>

<p lang="zh-CN">以同一治疗领域内该靶点的历史试验次数为基线，使用决策前证据至多带来小幅提升。换成最新版图谱后，六个模型中有五个明显超过基线，但作者发现，检索路径通常包含决策日期之后才发生的那场试验。维护 RAG 回测时，可以按预测日期冻结可检索快照，记录证据首次可用的日期和结果日期，并抽查高分预测实际引用了什么。</p>

<p lang="en">The baseline counted each target’s past trials in the same therapeutic area. Evidence available before the decision date added at most a small gain. With the newest graph, five of the six models clearly beat the baseline, but the authors found that retrieval paths usually included the trial itself, dated after the decision. For a RAG backtest, freeze the searchable snapshot at the forecast date, record when evidence first became available and when the outcome occurred, and inspect the evidence behind a sample of high-scoring forecasts.</p>
