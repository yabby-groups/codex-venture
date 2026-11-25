---
titleZh: "Codex Venture 怎样用 Codex 自动发布 AI 资讯？"
titleEn: "How Codex Venture uses Codex to publish AI news"
summaryZh: "从一批候选资料到一篇公开文章，看看 Codex 如何交稿、脚本如何拦截无法追溯的引用，以及维护者怎样确认部署。"
summaryEn: "Follow a batch of source records through editing, citation checks, and verification on the live site."
type: "workflows"
category: "agents"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Commit 68ba256"
status: "current"
tested: false
tags: ["github-actions","automation","venture"]
sources: [{"title":"An editorial workflow from candidate evidence to a static article – primary reference","url":"https://github.com/yabby-groups/codex-venture/blob/68ba256/.github/workflows/venture.yml"}]
updated: "2026-11-24"
blocks: [{"kind": "workflow", "title": {"zh": "一篇文章怎样进入公开站点", "en": "How an article reaches the live site"}, "items": [{"zh": "采集候选 · 记录保存后把本轮候选作为构建产物交给编辑任务。", "en": "Collect candidates · Save dated records and pass the batch as an Actions artifact."}, {"zh": "批量编辑 · Codex 返回双语文章、引用的候选 ID 和跳过的记录。", "en": "Edit the batch · Codex returns bilingual articles, cited candidate IDs, and skipped records."}, {"zh": "校验与构建 · 独立任务核对来源和正文格式，再构建 Astro 站点。", "en": "Validate and build · A separate job checks sources and body format, then builds Astro."}, {"zh": "推送与验收 · 推送通过校验的新文章，检查公网路由和内容指纹。", "en": "Push and verify · Push validated new articles, then check public routes and the content fingerprint."}]}, {"kind": "figure", "title": {"zh": "发布后的公开文章", "en": "The published article"}, "assetType": "product-screenshot", "src": "/article-media/venture-publication-before.jpg", "source": "https://codex-venture.com/news/venture-evidence-publication-workflow/", "rights": "Codex Venture 原创截图 / First-party site capture", "width": 960, "height": 600, "verified": "2026-11-24", "alt": {"zh": "改版前的站点正文和核实记录", "en": "The article and verification record before the redesign"}, "caption": {"zh": "2026 年 11 月 24 日从公网打开的旧版页面。标题下方显示该文采用的工作流提交和核实日期。", "en": "The previous layout captured from the live site on November 24, 2026. The workflow commit and verification date appeared below the headline."}}]
resourceIds: ["venture-publication"]
---

<p lang="zh-CN">给一个小型资讯站做自动发布，最难回答的问题是：模型写下这句话时，引用的是哪份资料？Codex Venture 的办法是为每批候选分配记录 ID。编辑任务用这些 ID 引用资料，发布任务再把引用转换成读者可打开的来源链接。</p>

<p lang="en">For a small automated news site, a practical question is where each reported update came from. Codex Venture assigns IDs to candidate records. The editor cites those IDs, and the publishing job turns them into source links readers can open.</p>

<h2><span lang="zh-CN">把选题决定交给编辑，把发稿条件写进程序</span><span lang="en">Let the editor choose stories and the pipeline enforce publication rules</span></h2>

<p lang="zh-CN">采集任务传入带日期、链接和摘要的候选。Codex CLI 一次处理一批，决定哪些有独立报道价值，再交回双语正文及候选 ID。维护者设置消息来源、模型和预算。证据不够时，编辑可以交回空文章列表。</p>

<p lang="en">The collector passes dated candidates with links and excerpts to Codex CLI in one batch. The editor selects items worth covering and returns bilingual copy with candidate IDs. Maintainers configure sources, models, and budgets. The editor can return an empty article list when evidence is thin.</p>

<h2><span lang="zh-CN">什么情况下发稿会停下来？</span><span lang="en">What stops an article from going live?</span></h2>

<p lang="zh-CN">假设编辑在正文里加入一个本批没有提供的链接。发布脚本会把正文链接和候选资料比对，校验失败时不会推送文章。通过校验后，Astro 构建还会检查站内链接、搜索索引和站点地图。</p>

<p lang="en">Suppose the editor adds a link that was never in the batch. The publish script compares body links with the candidate records and stops the push if they do not match. After validation, the Astro build also checks internal links, the search index, and the sitemap.</p>

<h2><span lang="zh-CN">怎样确认读者看到了新版本？</span><span lang="en">How do you confirm readers can see the new version?</span></h2>

<p lang="zh-CN">维护者可以把公开站点的 release.txt 和本次构建生成的内容指纹比对，再打开新文章确认对应路由。复用这套流程需要 GitHub Actions、Codex CLI、模型凭据和可构建的 Astro 站点。本文依据下方公开提交梳理。</p>

<p lang="en">Maintainers can compare the public release.txt with the build’s content fingerprint, then open the article to confirm its route. Reusing the setup requires GitHub Actions, Codex CLI, model credentials, and an Astro site that builds. This walkthrough draws on the public commit linked below.</p>
