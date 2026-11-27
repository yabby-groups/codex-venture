---
category: "agents"
summaryEn: "Browser Use 1.0.4 batches screenshot cleanup to preserve prompt-cache reuse. In the project’s 200-task benchmark, average model cost per task fell by about 52% as the score moved from 76.0 to 76.1."
summaryZh: "Browser Use 1.0.4 批量清理旧截图，让提示词缓存可以复用更久。项目方在 200 项任务的基准测试中报告，平均每任务模型成本下降约 52%，分数从 76.0 变为 76.1。"
tags: ["browser-use", "prompt-caching", "browser-automation"]
titleEn: "Browser Use 1.0.4 batches screenshot cleanup to preserve prompt-cache reuse"
titleZh: "Browser Use 1.0.4 批量清理旧截图，减少提示词缓存失效"
editorial: {"score": 83, "tier": "standard", "audience": "core"}
published: "2026-11-28T07:32:25+08:00"
sources: [{"title": "browser-use 1.0.4", "url": "https://github.com/browser-use/browser-use/releases/tag/1.0.4"}]
---
<p lang="zh-CN">在 Browser Use 1.0.3 中，每次加入新截图都可能触发一次清理。删掉旧截图虽然缩短了历史，却也改写了较早的消息，使模型服务商无法复用改写位置之后的提示词缓存。11 月 13 日发布的 1.0.4 改为等到有 20 条工具结果带截图时，再集中清理旧截图，减少长任务中改写历史的次数。</p>

<p lang="en">In Browser Use 1.0.3, adding a screenshot could trigger a cleanup. Removing old screenshots shortened the history but also rewrote earlier messages, preventing the model provider from reusing the prompt cache beyond the point of the edit. Version 1.0.4, released November 13, waits until 20 tool results contain screenshots before clearing old ones in a batch, so long runs rewrite their history less often.</p>

<p lang="zh-CN">项目方在 200 项任务的 BU Bench v2.1 中报告，从 1.0.3 升至 1.0.4 后，平均每任务模型成本从 0.434 美元降至 0.208 美元，基准分数从 76.0 变为 76.1。这组数字对应项目方的版本对比。排查自己的长任务账单时，可以把逐步缓存读取量和历史改写点对齐，再用同一组任务比较调整前后的完成率和模型成本。<a href="https://github.com/browser-use/browser-use/releases/tag/1.0.4">发布说明</a></p>

<p lang="en">Across 200 tasks in BU Bench v2.1, the project reported that average model cost per task fell from $0.434 in 1.0.3 to $0.208 in 1.0.4, while the benchmark score moved from 76.0 to 76.1. Those figures come from the project’s version comparison. To investigate costs on your own long runs, line up cache reads at each step with edits to the conversation history, then compare completion rates and model costs on the same tasks before and after changing the cleanup policy. <a href="https://github.com/browser-use/browser-use/releases/tag/1.0.4">Release notes</a></p>
