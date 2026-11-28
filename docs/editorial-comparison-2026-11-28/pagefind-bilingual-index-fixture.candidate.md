---
titleZh: "双语搜索少了一种语言？拿两页 HTML 查 Pagefind"
titleEn: "Missing a language in search? Check Pagefind with two HTML pages"
summaryZh: "用极小的样本区分索引覆盖问题和站内搜索匹配问题。"
summaryEn: "A tiny fixture helps distinguish missing index coverage from search matching problems."
type: "tutorials"
category: "coding"
published: "2026-11-25T20:55:05+08:00"
verified: "2026-11-28"
version: "Pagefind 1.6.0"
status: "current"
tested: true
tags: ["ai-practice"]
sources: [{"title": "Pagefind 1.6.0", "url": "https://github.com/cloudcannon/pagefind/releases/tag/v1.6.0"}, {"title": "本站双语索引探针 / Bilingual indexing probe", "url": "https://github.com/yabby-groups/codex-venture/blob/main/scripts/practice_probe.py"}]
blocks: [{"kind": "code", "title": {"zh": "复核命令", "en": "Commands to reproduce"}, "language": "bash", "file": "", "code": "npm ci --ignore-scripts\npython3 scripts/practice_probe.py"}]
updated: "2026-11-28"
---
<p lang="zh-CN">如果搜索只剩下一种语言，先做两页最小样本。本站的探针给两页分别设 <code>lang="en"</code> 和 <code>lang="zh-CN"</code>，在带 <code>data-pagefind-body</code> 的区域写入可搜索的短句，然后在临时目录运行 <code>pagefind --site .</code>。</p>

<p lang="en">If search seems to have lost a language, start with two tiny pages. Our probe sets <code>lang="en"</code> on one and <code>lang="zh-CN"</code> on the other, adds searchable text inside <code>data-pagefind-body</code>, and runs <code>pagefind --site .</code> in a temporary directory.</p>

<p lang="zh-CN">在本站公开仓库的根目录运行下方命令，需要 Node.js、npm 和 Python 3。本站 11 月 28 日在 Darwin arm64 上用锁定的 Pagefind 1.6.0 复跑，退出码为 0，索引元数据恰有 <code>en</code> 和 <code>zh-cn</code> 两个语言键。<a href="https://github.com/yabby-groups/codex-venture/blob/main/scripts/practice_probe.py">探针源码</a></p>

<p lang="en">Run the commands below from the root of our public repository with Node.js, npm and Python 3 installed. On November 28, the locked Pagefind 1.6.0 exited with code 0 on Darwin arm64, and the index metadata contained exactly two language keys, <code>en</code> and <code>zh-cn</code>. <a href="https://github.com/yabby-groups/codex-venture/blob/main/scripts/practice_probe.py">Probe source</a></p>

<p lang="zh-CN">只出现一个键时，先查 HTML 的 <code>lang</code> 和索引命令指向的目录。两个键齐全后，再到实际网页检查同一页混排中英文时能不能搜到想要的内容。</p>

<p lang="en">If only one key appears, check each page’s <code>lang</code> and the directory passed to the indexer. Once both keys show up, move to a real page to test whether search finds the right text when Chinese and English share a URL.</p>
