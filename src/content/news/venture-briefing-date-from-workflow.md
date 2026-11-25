---
titleZh: "让 CI 日期决定简报 URL"
titleEn: "Let the CI edition date determine the briefing URL"
summaryZh: "简报标题可以由模型起草，文件名可以在写入前由编辑批次的日期一次确定。"
summaryEn: "Let the model draft the headline and derive the filename from the edition date before writing."
type: "workflows"
category: "coding"
published: "2026-11-25T20:55:05+08:00"
verified: "2026-11-25"
version: "Commit 7ce66fc"
status: "current"
tested: false
tags: ["ai-practice"]
sources: [{"title": "Codex Venture 发布修复 / Publishing fix", "url": "https://github.com/yabby-groups/codex-venture/commit/7ce66fcd747541789aefd021111f4f43d0940f25"}]
---

<p lang="zh-CN">简报的文件名同时决定网址和归档位置。本站曾在发布端依赖编辑返回的 slug，模型填写的日期一旦与批次日期不一致，写入校验便会拒绝稿件。只改提示词仍要求模型每次都重现一个程序已经知道的值。</p>

<p lang="en">The briefing filename determines its URL and archive position. When the publishing job relied on the editor’s slug, a date that differed from the batch date caused the writer to reject the draft. A prompt fix would still ask the model to reproduce a value the program already knew.</p>

<p lang="zh-CN">本站的修复是在发布端核对批次时间，然后替换简报 slug。日报采用 YYYY-MM-DD，周报加 weekly- 前缀。写入函数继续校验日期和目标文件名，并拒绝覆盖已有稿件。这样即使模型返回错误日期，站点也会保留约定的归档 URL。</p>

<p lang="en">The fix checks the batch timestamp in the publishing job and replaces the briefing slug. Daily editions use YYYY-MM-DD, and weekly editions add the weekly- prefix. The writer still checks the date and destination and refuses to overwrite an existing file. The archive URL follows the publishing convention even if the model supplies the wrong date.</p>

<p lang="zh-CN">复用时，先在准备任务按编辑时区计算 edition_date，再将它随批次传到发布任务。用跨午夜的批次、带 weekly- 的批次和已有目标文件分别检查日期交接、前缀和重复发布。本文依据公开修复提交，未量化变更后的失败率。</p>

<p lang="en">To reuse the pattern, compute edition_date in the editorial timezone during preparation and carry it with the batch. Test a batch that crosses midnight, a weekly edition, and an existing destination to check the handoff, prefix, and repeat-publication behavior. This guide draws on the public fix. The post-change failure rate was not measured.</p>
