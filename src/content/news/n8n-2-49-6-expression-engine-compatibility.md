---
category: "agents"
summaryEn: "n8n 2.49.6 fixes differences in Base64, URL encoding, and formatting results for workflows that rely on consistent output across expression engines."
summaryZh: "n8n 2.49.6 修复了表达式引擎之间的 Base64、URL 编码和格式化结果差异，影响依赖这些输出一致性的工作流。"
tags: ["n8n", "workflow-automation", "expression-engine"]
titleEn: "n8n 2.49.6 aligns encoding and formatting results across expression engines"
titleZh: "n8n 2.49.6 对齐表达式引擎的编码与格式化结果"
published: "2026-11-27T02:33:03+08:00"
sources: [{"title": "n8n@2.49.6", "url": "https://github.com/n8n-io/n8n/releases/tag/n8n%402.49.6"}]
---
<p lang="zh-CN">n8n 于 2026 年 11 月 25 日发布 2.49.6，将隔离式表达式引擎中的 Base64、URL 编码和格式化结果与旧版引擎对齐。对依赖这些表达式输出的工作流，这次修复解决的是两套引擎之间的兼容性问题。</p>

<p lang="en">n8n released 2.49.6 on November 25, 2026. It aligns Base64, URL encoding, and formatting results in the isolated expression engines with the legacy engine. For workflows that depend on these expression outputs, the fix addresses compatibility between the engines.</p>

<p lang="zh-CN">同一版本还让引擎原生执行 <code>urlEncode</code>、<code>base64Decode</code> 和 <code>format</code>。发布说明分别列出了结果对齐和原生执行两项改动。<a href="https://github.com/n8n-io/n8n/releases/tag/n8n%402.49.6">GitHub 发布说明</a></p>

<p lang="en">The release also adds native evaluation for <code>urlEncode</code>, <code>base64Decode</code>, and <code>format</code>. The release notes list native evaluation separately from the changes that align expression results. <a href="https://github.com/n8n-io/n8n/releases/tag/n8n%402.49.6">GitHub release notes</a></p>
