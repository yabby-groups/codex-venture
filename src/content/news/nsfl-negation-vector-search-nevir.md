---
category: "models"
summaryEn: "The training-free NSFL framework combines scores for individual search conditions with contextual adjustments. On NevIR, the share of pairs with both queries answered correctly rose from 25.6% to 50.8%."
summaryZh: "免训练框架 NSFL 将检索条件分别打分，再按上下文修正。论文报告，NevIR 上两条查询均答对的测试对占比从 25.6% 升至 50.8%。"
tags: ["nsfl", "vector-search", "nevir", "rag"]
titleEn: "NSFL scores search conditions separately and raises NevIR pair accuracy to 50.8%"
titleZh: "NSFL 拆分向量检索条件，NevIR 成对准确率升至 50.8%"
editorial: {"score": 78, "tier": "standard", "audience": "core"}
published: "2026-11-28T15:31:57+08:00"
sources: [{"title": "NSFL: A Post-Training Neuro-Symbolic Fuzzy Logic Framework for Boolean Operators in Neural Embeddings", "url": "https://arxiv.org/abs/2604.10604"}]
---
<p lang="zh-CN">给向量检索做回归测试时，可以成对检查仅在否定条件上不同的查询，观察排序是否随条件改变，并要求两条查询的排序都正确才算通过。论文作者提出的免训练框架 NSFL 将查询拆成基本条件，用各条件的相似度作为基础分，再用上下文带来的相似度变化修正组合打分。</p>

<p lang="en">For a vector search regression test, pair queries that differ only in a negation condition. Check whether the rankings change accordingly and count the pair as a pass only if both rankings are correct. The authors’ training-free NSFL framework uses similarity scores for individual conditions as a starting point, then adjusts the combined score based on how context changes those similarities.</p>

<p lang="zh-CN">论文摘要报告，NSFL 在 NevIR 上把成对准确率从 25.6% 提高到 50.8%。按两条查询都须答对的标准，仍有 49.2% 的测试对未通过。对维护 RAG 或文档搜索的团队，成对测试可以直接检查加入排除条件后，系统是否按预期重新排序。</p>

<p lang="en">The abstract reports that NSFL raised pairwise accuracy on NevIR from 25.6% to 50.8%. Under the requirement to get both queries right, 49.2% of pairs still failed. For teams maintaining RAG or document search, paired tests can check directly whether adding an exclusion condition changes the ranking as intended.</p>

<p lang="zh-CN">研究来源为 2026 年 11 月 26 日的 arXiv v2 公告及摘要。<a href="https://arxiv.org/abs/2604.10604">原始记录</a></p>

<p lang="en">Research source: the November 26, 2026 arXiv v2 announcement and abstract. <a href="https://arxiv.org/abs/2604.10604">Original record</a></p>
