---
titleZh: "RAGFlow 从文档解析接到检索"
titleEn: "RAGFlow connects document parsing to retrieval"
summaryZh: "RAGFlow 提供文档解析、入库和检索流程，适用于从多份文档搜集问答上下文的团队。"
summaryEn: "RAGFlow provides document parsing, ingestion and retrieval for teams that need to gather Q&A context from multiple documents."
published: "2026-11-24T15:00:30+08:00"
category: "open-source"
updated: "2026-11-24"
tags: ["ragflow", "rag", "knowledge-base"]
sources:
  - title: "infiniflow/ragflow repository and documentation"
    url: https://github.com/infiniflow/ragflow
resource: {"id":"ragflow","type":"open-source","name":"RAGFlow","summary":["RAGFlow 提供文档解析、入库和检索流程，适用于从多份文档搜集问答上下文的团队。","RAGFlow provides document parsing, ingestion and retrieval for teams that need to gather Q&A context from multiple documents."],"site":"https://github.com/infiniflow/ragflow","repository":"https://github.com/infiniflow/ragflow","categories":[["文档检索","Document retrieval"]],"verifiedAt":"2026-11-24"}
---
<p lang="zh-CN">文档进入知识库之前，表格与扫描件都需要先解析。以设备手册为例，如果检索找到型号却漏掉同一行的额定电压，问答模型收到的上下文就已经不完整。评估 RAGFlow 时，可以从这种可核对的问题入手。</p>

<p lang="en">Tables and scanned pages need to be parsed before they enter a knowledge base. In an equipment manual, a retrieved passage that includes a model number but drops the voltage from the same row gives the answer model incomplete context. Start a RAGFlow evaluation with questions whose answers you can verify against the source.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where to use it</span></h2>

<p lang="zh-CN">可用带表格、扫描件和不同标题层级的内部手册建立小型检索测试。观察问题能否找到对应原文，以及表格中的列和值是否仍保持关联。</p>

<p lang="en">Build a small retrieval test with manuals that contain tables, scans and several heading levels. Check whether questions retrieve the right passage and whether values remain associated with the correct table columns.</p>

<h2><span lang="zh-CN">获取与项目状态</span><span lang="en">Getting started and project status</span></h2>

<p lang="zh-CN">仓库给出 Docker 和源码部署方式。首轮试用需要准备容器环境、代表性文档和所用的模型配置。 仓库创建于 2023-12-12，GitHub API 在 11 月 24 日记录的最近推送日期为 2026-11-24（UTC）。许可证为 Apache-2.0。</p>

<p lang="en">The repository documents Docker and source deployments. Prepare a container environment, representative documents and the model configuration for an initial trial. The repository was created on 2023-12-12. On November 24, the GitHub API reported 2026-11-24 as its latest push date (UTC). The license is Apache-2.0.</p>
