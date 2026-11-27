---
category: "open-source"
summaryEn: "Docling v2.151.0 can read waterfall charts and treemaps in PPTX files, giving teams more chart types to test before importing slide decks into a knowledge base."
summaryZh: "Docling v2.151.0 可读取 PPTX 中的瀑布图和矩形树图。将演示稿导入知识库前，可以把这两类图表纳入转换抽查。"
tags: ["docling", "pptx"]
titleEn: "Docling adds support for waterfall charts and treemaps in PPTX"
titleZh: "Docling 新增 PPTX 瀑布图和矩形树图读取支持"
editorial: {"score": 69, "tier": "standard", "audience": "core"}
published: "2026-11-27T23:40:59+08:00"
sources: [{"title": "v2.151.0", "url": "https://github.com/docling-project/docling/releases/tag/v2.151.0"}, {"title": "Targeted research", "url": "https://raw.githubusercontent.com/docling-project/docling/v2.151.0/README.md"}]
---
<p lang="zh-CN">Docling 在 11 月 19 日发布的 v2.151.0 中扩展了 PPTX 图表读取支持，新增瀑布图、矩形树图等 Office 2016 图表类型。准备把财务汇报或客户演示稿导入知识库的团队，可以用新版重新转换含这些图表的样本。<a href="https://github.com/docling-project/docling/releases/tag/v2.151.0">官方发布说明</a></p>

<p lang="en">Docling v2.151.0, released November 19, expands PPTX chart reading to include waterfall charts, treemaps, and other Office 2016 chart types. Teams importing financial reports or client decks into a knowledge base can rerun conversion on sample slides containing those charts. <a href="https://github.com/docling-project/docling/releases/tag/v2.151.0">Official release notes</a></p>

<p lang="zh-CN">该版本的 README 给出了 Python 的 DocumentConverter 入口，输入可以是本地路径或 URL。接入检索或问答前，可对照原幻灯片抽查转换结果，确认类别标签、系列名称和关键数值是否足够支撑后续回答。<a href="https://raw.githubusercontent.com/docling-project/docling/v2.151.0/README.md">版本 README</a></p>

<p lang="en">The versioned README shows how to use Python’s DocumentConverter with a local path or URL. Before sending the converted output to a retrieval or Q&amp;A system, spot-check it against the original slides to see whether it preserves the category labels, series names, and key values needed to answer questions. <a href="https://raw.githubusercontent.com/docling-project/docling/v2.151.0/README.md">Versioned README</a></p>
