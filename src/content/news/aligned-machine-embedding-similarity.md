---
category: "models"
summaryEn: "An initial evaluation of 12 embedding models found partial agreement with human similarity judgments. Among the multimodal models tested, agreement was higher for image-to-image comparisons than for image-to-text comparisons."
summaryZh: "首轮评估发现，12 个受测嵌入模型与人的相似性判断仅部分一致。受测多模态模型在图图比较上的一致性高于图文比较。"
tags: ["embeddings", "multimodal", "retrieval", "evaluation"]
titleEn: "Aligned Machine tests embedding similarity against human choices"
titleZh: "Aligned Machine 用人工二选一检验嵌入模型的相似度排序"
editorial: {"score": 78, "tier": "standard", "audience": "core"}
published: "2026-11-28T21:46:05+08:00"
sources: [{"title": "Aligned Machine: A Benchmark for Evaluating Multimodal Embedding Similarity via Human Comparative Judgements", "url": "https://arxiv.org/abs/2611.33594"}]
---
<p lang="zh-CN">给素材库选嵌入模型时，可以把两对素材摆在一起，请用户选出更相似的一对，再看模型的排序是否与用户一致。Jiechen Li、Hannah Groos 和 Brinnae Bent 在 2026 年 11 月 25 日提交的预印本中介绍了采用这一方法的 Aligned Machine。作者报告，首轮有 115 名参与者，共贡献 2,875 条配对标注，涉及 872 个不同配对。<a href="https://arxiv.org/abs/2611.33594">arXiv 预印本</a></p>

<p lang="en">When choosing an embedding model for a media library, you can show users two pairs of items, ask which pair is more similar, and check whether the model ranks them the same way. Jiechen Li, Hannah Groos, and Brinnae Bent describe this approach in their Aligned Machine preprint, submitted on November 25, 2026. The authors report that 115 participants contributed 2,875 pair annotations covering 872 distinct pairs in the first round. <a href="https://arxiv.org/abs/2611.33594">arXiv preprint</a></p>

<p lang="zh-CN">作者用这些判断评估了 12 个嵌入模型，发现模型与人的判断仅部分一致。在受测多模态模型中，图图比较比图文比较更符合人的判断。对同时支持图搜图和以文搜图的团队，可以按真实查询类型收集二选一判断，并分别统计一致率，再决定哪些候选模型值得进入产品测试。论文结果来自该基准的首轮数据。</p>

<p lang="en">The authors used those judgments to evaluate 12 embedding models and found only partial agreement with people. Among the multimodal models tested, image-to-image comparisons agreed with human judgments more often than image-to-text comparisons. Teams that support both kinds of search can collect forced-choice judgments for each query type and score them separately before deciding which models to test in their product. The reported results come from the benchmark’s initial data.</p>
