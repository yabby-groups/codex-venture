---
titleZh: "Docling 2.152 可取消排队中的 PDF 解析"
titleEn: "Docling 2.152 cancels queued PDF parsing"
summaryZh: "文档转换停止时，新版可以取消仍在队列中的 PDF 解析，并增加媒体轨道与 MLX 解析支持。"
summaryEn: "The release can cancel PDF parsing still in the queue when conversion stops and adds media tracks and MLX parsing support."
published: "2026-11-24T15:01:03+08:00"
category: "open-source"
tags: ["docling", "rag", "document-parsing"]
sources:
  - title: "docling v2.152.0 release notes"
    url: https://github.com/docling-project/docling/releases/tag/v2.152.0
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 23 日（北京时间），docling 发布 v2.152.0。文档转换停止时，新版可以取消仍在队列中的 PDF 解析，并增加媒体轨道与 MLX 解析支持。</p>

<p lang="en">docling published v2.152.0 on November 23 (China Standard Time). The release can cancel PDF parsing still in the queue when conversion stops and adds media tracks and MLX parsing support.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">对于给知识库批量导入文档的后台服务，用户取消请求后，排队任务可以及早退出。新版还允许服务端选择默认管线，并为 Nemotron 3.5 Parse 加入原生 MLX 支持。</p>

<p lang="en">In a background service that imports documents into a knowledge base, queued work can exit when a user cancels a conversion. The release also lets the server choose the default pipeline and adds native MLX support for Nemotron 3.5 Parse.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">从版本页获取更新。分别验证排队和已开始解析的任务，并用多栏表格、扫描 PDF 等真实文档检查导入质量。</p>

<p lang="en">Get the update from the release page. Test queued and already-running jobs separately, and check import quality on representative inputs such as scanned PDFs and multi-column tables.</p>
