---
titleZh: "用两页 HTML 检查 Pagefind 双语索引"
titleEn: "Check a bilingual Pagefind index with two HTML pages"
summaryZh: "本站用 Pagefind 1.6.0 跑了一个双语样本，确认索引为中文和英文生成了独立的语言条目。"
summaryEn: "A two-page fixture indexed by Pagefind 1.6.0 produced separate entries for Chinese and English."
type: "tutorials"
category: "coding"
published: "2026-11-25T20:55:05+08:00"
verified: "2026-11-25"
version: "Pagefind 1.6.0"
status: "current"
tested: true
tags: ["ai-practice"]
sources: [{"title": "Pagefind 1.6.0", "url": "https://github.com/cloudcannon/pagefind/releases/tag/v1.6.0"}, {"title": "本站双语索引探针 / Bilingual indexing probe", "url": "https://github.com/yabby-groups/codex-venture/blob/main/scripts/practice_probe.py"}]
blocks: [{"kind": "code", "title": {"zh": "复核命令", "en": "Commands to reproduce"}, "language": "bash", "file": "", "code": "npm ci --ignore-scripts\npython3 scripts/practice_probe.py"}]
---

<p lang="zh-CN">排查静态站搜索时，可以先确认构建器识别到了预期语言。准备两份 HTML，分别设置 html lang 为 en 和 zh-CN，并将可检索内容放进带 data-pagefind-body 的 main 元素。把样本放进临时目录，使试验和正式站的索引互不覆盖。</p>

<p lang="en">When debugging static search, start by checking that the indexer detected the expected languages. Create two HTML files with lang set to en and zh-CN, and put searchable content in a main element marked with data-pagefind-body. Use a temporary directory to keep the fixture and production indexes apart.</p>

<p lang="zh-CN">本站在 Darwin arm64 上使用站点锁定的 Pagefind 1.6.0，在临时目录运行 pagefind --site .。命令退出码为 0，输出包含 Discovered 2 languages: en, zh-cn 和 Indexed 2 pages。我们再从 pagefind/pagefind-entry.json 核对了两个语言键。</p>

<p lang="en">On Darwin arm64 we ran the site’s locked Pagefind 1.6.0 with pagefind --site . in a temporary directory. It exited with code 0 and printed “Discovered 2 languages: en, zh-cn” and “Indexed 2 pages.” We checked both language keys in pagefind/pagefind-entry.json.</p>

<p lang="zh-CN">如果只生成一个语言键，先检查两份输入 HTML 的 html lang 和构建目录。这个样本采用每页一种声明语言，适合检查索引覆盖。中英文在同一 URL 内的查询行为和分词相关性，需要用实际站点的搜索结果确认。</p>

<p lang="en">If only one language key appears, check the html lang declaration in each input and verify the build directory. This fixture uses one declared language per page and checks index coverage. Use searches on the actual site to evaluate mixed-language pages and tokenization quality.</p>
