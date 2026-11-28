---
category: "coding"
summaryEn: "Cloudflare reports that code changes and adjustments to model choice and reasoning effort cut the average cost per AI review from $2.43 to $0.77 against its two most expensive weeks before the changes."
summaryZh: "Cloudflare 报告称，经代码优化以及模型和推理力度调整，AI 审查的平均单次费用较改造前最贵两周从 2.43 美元降至 0.77 美元。"
tags: ["cloudflare", "code-review", "inference-cost"]
titleEn: "Cloudflare cuts its average AI code review cost to $0.77"
titleZh: "Cloudflare 将 AI 代码审查的平均单次费用降至 0.77 美元"
editorial: {"score": 80, "tier": "standard", "audience": "core"}
published: "2026-11-28T16:16:20+08:00"
sources: [{"title": "Cutting our inference bill by 68% by being obsessive about optimization", "url": "https://blog.cloudflare.com/obsessive-inference-optimization"}]
---
<p lang="zh-CN">Cloudflare 的 AI 代码审查器沿用原有的协调器、专门审查代理和风险分档，平均单次费用却比此前翻了一倍。Cloudflare 工程师 Ryan Skidmore 在 2026 年 10 月 19 日发表的复盘中写道，团队把各档审查的占比固定后重新计算费用，发现上涨趋势仍然存在。按这个口径，3 月平均每次花费 1.22 美元，8 月升至 2.32 美元。<a href="https://blog.cloudflare.com/obsessive-inference-optimization">Cloudflare 工程复盘</a></p>

<p lang="en">Cloudflare's AI code reviewer kept the same coordinator, specialist reviewers, and risk tiers, yet its average cost per review doubled. In an October 19, 2026 write-up, Cloudflare engineer Ryan Skidmore said the team recalculated costs with a fixed mix of review tiers and found that the upward trend persisted. On that basis, the average rose from $1.22 in March to $2.32 in August. <a href="https://blog.cloudflare.com/obsessive-inference-optimization">Cloudflare engineering write-up</a></p>

<p lang="zh-CN">以改造前费用最高的两周为基准，Cloudflare 报告称，平均单次费用从 2.43 美元降至 0.77 美元，降幅为 68%。审查中位耗时也由 4 分 09 秒缩短到 1 分 32 秒。团队估计，约四成节省来自审查器代码优化，其余来自模型选择和推理力度的调整。维护类似系统的团队可以借用固定档位占比的做法，判断单次成本上涨是否仅由高成本任务增多造成。</p>

<p lang="en">Using the two most expensive weeks before the changes as its baseline, Cloudflare reported a 68% drop in average cost per review, from $2.43 to $0.77. Median review time fell from 4 minutes 9 seconds to 1 minute 32 seconds. The team attributed about 40% of the savings to changes in the reviewer's code and the rest to model selection and reasoning effort. Teams running similar systems can hold the tier mix steady to check whether a rise in cost per review comes solely from handling more expensive tasks.</p>
