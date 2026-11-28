---
category: "models"
summaryEn: "Some two-stage RAG pipelines beat the final reranker alone but lose to the first-stage ranker alone. A preprint shows why both standalone configurations belong in the same evaluation."
summaryZh: "部分 RAG 两级重排优于单独精排，却不及单独粗排。固定候选集和预算分别跑三组，才能判断第二级值不值得保留。"
tags: ["rag", "reranking", "evaluation"]
titleEn: "Before adding a second RAG reranker, test the first stage on its own"
titleZh: "RAG 加第二级重排前，先测只用粗排的表现"
editorial: {"score": 87, "tier": "featured", "audience": "core"}
published: "2026-11-28T15:46:02+08:00"
sources: [{"title": "When Rerankers Work Together: Better and Faster Reranking without Joint Training", "url": "https://arxiv.org/abs/2611.33844"}]
---
<p lang="zh-CN">只用轻量粗排、只用精排，还是把两级串起来？一篇 arXiv 预印本在固定输入候选和预算的条件下比较了这三种配置。作者发现，有些级联比单独精排答得更准，却输给只用粗排的配置。只拿精排做基线，可能会误判第二级的价值。</p>

<p lang="en">Should a RAG pipeline use a lightweight first-stage ranker, a final reranker, or both? An arXiv preprint compared all three configurations with the same input candidates and budgets. Some cascades answered more accurately than the final reranker alone but fell short of the first-stage ranker alone. Using only the final reranker as a baseline can give the wrong impression of what the second stage adds.</p>

<p lang="zh-CN">在 NoLiMa 32K 上用 Gemma 作答时，作者在 CrossEncoder 或 Provence 前加入轻量粗排，相比对应的单独精排，答题准确率提高 4.02 至 9.43 个百分点，在线剪枝速度达到原来的 1.57 至 1.88 倍。这个加速数字衡量的是剪枝环节。实验中的收益随作答模型、重排器搭配和级联结构而变。</p>

<p lang="en">On NoLiMa 32K with Gemma as the reader, adding a lightweight first stage before CrossEncoder or Provence raised answer accuracy by 4.02 to 9.43 percentage points over the corresponding standalone reranker. Online pruning ran 1.57 to 1.88 times as fast. That speedup applies to the pruning step. Gains varied with the reader, the reranker pairing, and the cascade configuration.</p>

<p lang="zh-CN">长文档问答团队评审重排改版时，可以固定候选集和预算，把三种配置放在同一张表里，分别记录关键证据保留率、最终答题准确率和在线剪枝耗时。这样能直接看出，精排接在粗排之后是否带来了足以抵消额外开销的收益。<a href="https://arxiv.org/abs/2611.33844">arXiv 预印本</a></p>

<p lang="en">For a long-document QA review, hold the candidate set and budget fixed and log evidence retention, final answer accuracy, and online pruning time for all three configurations. The comparison shows whether adding the final reranker improves results enough to justify its cost. <a href="https://arxiv.org/abs/2611.33844">arXiv preprint</a></p>
