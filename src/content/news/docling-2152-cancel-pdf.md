---
titleZh: "点了取消，队列里的 PDF 还要解析吗？Docling 2.152 改了这一点"
titleEn: "Can queued PDFs skip parsing after you cancel? Docling 2.152 changes that"
summaryZh: "给知识库批量导入 PDF 时，Docling 现在可以在转换停止后取消尚在排队的解析任务。"
summaryEn: "Docling can now cancel queued PDF parsing when a conversion stops, a useful change for bulk knowledge-base imports."
published: "2026-11-24T15:01:03+08:00"
category: "open-source"
tags: ["docling", "rag", "document-parsing"]
sources:
  - title: "docling v2.152.0 release notes"
    url: https://github.com/docling-project/docling/releases/tag/v2.152.0
updated: "2026-11-28"
---
<p lang="zh-CN">知识库后台收到取消请求后，那些还没轮到解析的 PDF 可以不用开工了。Docling 11 月 23 日发布的 2.152.0 支持在转换停止时取消排队任务。应用层的取消请求得先传到转换流程，队列里的变化才有意义。</p>

<p lang="en">PDFs still waiting in the queue can skip parsing once the conversion stops. Docling added this in 2.152.0 on November 23. For a knowledge-base import, the first thing to check is whether clicking Cancel actually reaches the conversion layer.</p>

<p lang="zh-CN">升级时，可以用一批 PDF 分开检查两件事：取消后排队项是否跳过，以及已经开跑的任务会怎样。发布说明明确提到的是排队任务。<a href="https://github.com/docling-project/docling/releases/tag/v2.152.0">Docling 发布说明</a></p>

<p lang="en">When testing the upgrade, check two things separately: whether queued jobs are skipped after cancellation and what happens to a job already running. The release notes specifically cover queued work. <a href="https://github.com/docling-project/docling/releases/tag/v2.152.0">Docling release notes</a></p>
