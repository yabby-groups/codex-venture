---
titleZh: "从候选证据到静态文章的编辑工作流"
titleEn: "An editorial workflow from candidate evidence to a static article"
summaryZh: "用结构化输出交接采集、编辑和发布，并验证证据可追溯。"
summaryEn: "Hand off collection, editing, and publishing through structured output with traceable evidence."
type: "workflows"
category: "agents"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Commit 68ba256"
status: "current"
tested: false
tags: ["github-actions","automation","venture"]
sources: [{"title":"An editorial workflow from candidate evidence to a static article – primary reference","url":"https://github.com/yabby-groups/codex-venture/blob/68ba256/.github/workflows/venture.yml"}]
---
<p lang="zh-CN">对小型技术媒体，输入可以是有时间戳的候选记录，输出是双语 Markdown。Codex Venture 的采集任务先保存候选，编辑任务为整批证据返回结构化结果，发布任务从受信的提交运行校验，再构建和推送。</p>

<p lang="en">For a small technical publication, inputs can be timestamped candidate records and the output can be bilingual Markdown. Codex Venture’s collection job saves candidates, the editor returns structured results for a batch, and the publish job runs validation from a trusted commit before building and pushing.</p>

<p lang="zh-CN">复用这套流程需要 GitHub Actions、Codex CLI、模型凭据和一个可构建的 Astro 站点。维护者决定来源、预算与发稿门槛，脚本检查候选 ID 和引用。模型容量受现有预算与计费约束。部署后的 URL 与版本指纹属于独立验收项。公开工作流提供可复用配置。</p>

<p lang="en">Reusing the workflow takes GitHub Actions, Codex CLI, model credentials, and a buildable Astro site. Maintainers set sources, budget, and publishing criteria, while scripts validate candidate IDs and citations. Model capacity depends on the configured budget and billing. Verify public URLs and the release fingerprint after deployment. The public workflow provides the reusable configuration.</p>
