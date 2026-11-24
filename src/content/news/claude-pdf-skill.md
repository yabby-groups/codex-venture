---
titleZh: "Anthropic PDF Skill 的表格提取方法"
titleEn: "How Anthropic’s PDF Skill extracts tables"
summaryZh: "用一份无敏感信息的样本判断 PDF 是否适合直接提取。"
summaryEn: "Use a nonsensitive sample to decide whether a PDF can be extracted directly."
type: "skills"
category: "coding"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Claude Code / main"
status: "current"
tested: false
project: "claude-pdf"
tags: ["agent-skills","claude"]
sources: [{"title":"How Anthropic’s PDF Skill extracts tables – primary reference","url":"https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md"},{"title":"Anthropic skills repository","url":"https://github.com/anthropics/skills"},{"title":"PDF skill license","url":"https://github.com/anthropics/skills/blob/main/skills/pdf/LICENSE.txt"}]
updated: "2026-11-24"
blocks: [{"kind": "code", "title": {"zh": "在 Claude Code 中安装", "en": "Install in Claude Code"}, "language": "text", "code": "/plugin marketplace add anthropics/skills\n/plugin install document-skills@anthropic-agent-skills"}, {"kind": "code", "title": {"zh": "指定页码和输出格式", "en": "Specify a page and output format"}, "language": "text", "code": "Use the PDF skill to extract the table on page 2 of sample.pdf as CSV. Mark any ambiguous cells for manual review."}]
resource: {"id": "claude-pdf", "type": "skills", "name": "Anthropic PDF Skill", "summary": ["提取 PDF 表格、读取文本和处理页面。", "Extract PDF tables and text and manipulate pages."], "categories": [["文档处理", "Document processing"]], "site": "https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md", "repository": "https://github.com/anthropics/skills", "platforms": ["Claude Code"], "license": "Apache-2.0", "install": "Claude Code Marketplace", "featured": true}
---
<p lang="zh-CN">Anthropic 的 PDF 技能文档给出 pypdf 读写页面与 pdfplumber 提取表格的两套做法。对于版式固定的账单，可以先用 pdfplumber 处理一页，再逐列核对标题、金额和跨行单元格。</p>

<p lang="en">Anthropic’s PDF skill documents page operations with pypdf and table extraction with pdfplumber. For a fixed-layout invoice, try pdfplumber on one page and check column headings, amounts, and cells spanning multiple rows.</p>

<p lang="zh-CN">使用对应阅读库的 Python 环境，按 Anthropic 技能仓库的安装说明启用 document-skills，再用自然语言指定文件、页码与输出格式。扫描件需要识别文字，表格错位仍需人工核对。PDF 技能目录附 Apache 2.0 许可证。仅给会话样本目录权限，并按宿主的数据政策处理文件。本文依据仓库文档整理。</p>

<p lang="en">Use a Python environment with the relevant libraries, enable document-skills according to Anthropic’s repository instructions, and specify the file, page numbers, and output format in your request. Scans need OCR and misaligned tables need manual checks. The PDF skill directory includes an Apache 2.0 license. Limit access to sample files and follow the host’s data policy. This profile is based on the repository documentation.</p>
