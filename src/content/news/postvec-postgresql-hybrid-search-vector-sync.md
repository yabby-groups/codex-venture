---
category: "open-source"
summaryEn: "Postvec combines BM25 and semantic search in one SQL call and keeps document embeddings in sync with their source text. Its PostgreSQL 18 example gives teams a starting point for evaluating whether the extension can take over vector synchronization."
summaryZh: "Postvec 在一次 SQL 调用中融合 BM25 和语义检索，并随正文更新同步文档向量。仓库的 PostgreSQL 18 示例可用于评估扩展能否接手向量同步任务。"
tags: ["postgresql", "postvec", "hybrid-search", "embeddings"]
titleEn: "Postvec brings hybrid search and automatic vector sync to PostgreSQL"
titleZh: "Postvec 将混合检索和自动向量同步带入 PostgreSQL"
editorial: {"score": 72, "tier": "standard", "audience": "core"}
published: "2026-11-28T21:02:05+08:00"
sources: [{"title": "Show HN: Postvec – switching embedding models in Postgres without re-embedding", "url": "https://news.ycombinator.com/item?id=50627889"}, {"title": "Targeted research", "url": "https://github.com/univec-ai/postvec"}]
---
<p lang="zh-CN">Postvec 的官方仓库给出了一个 PostgreSQL 18 本地容器示例，从一张含正文列的文档表开始，为该列启用嵌入模型。按 README 的描述，扩展会在正文变化时同步向量，并在一次 SQL 调用中融合 BM25 关键词检索和语义检索。</p>

<p lang="en">Postvec’s official repository shows a local PostgreSQL 18 container example that starts with a document table and enables an embedding model on its text column. According to the README, the extension keeps vectors in sync when the text changes and combines BM25 keyword search with semantic search in a single SQL call.</p>

<p lang="zh-CN">已有 PostgreSQL 知识库的团队可以选一列有代表性的正文，检查更新后能否检索到新内容，再判断现有的向量同步任务能否交给扩展。部署时还需要决定嵌入推理放在哪里。仓库列出三种选择，分别是在 PostgreSQL 内运行、连接独立的 postvec-server，以及调用托管嵌入 API。<a href="https://github.com/univec-ai/postvec">Postvec 官方仓库</a></p>

<p lang="en">Teams with a PostgreSQL knowledge base can start with a representative text column and check whether an edit becomes searchable before deciding whether to hand vector synchronization over to the extension. Deployment also involves choosing where embeddings are generated. The repository lists three options: inside PostgreSQL, through a separate postvec-server, or via a hosted embedding API. <a href="https://github.com/univec-ai/postvec">Official Postvec repository</a></p>
