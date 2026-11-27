---
category: "coding"
summaryEn: "Run scheduled Lighthouse checks on key URLs, flag low scores by device strategy, and verify each alert before treating it as a regression."
summaryZh: "定时检查关键 URL，按设备策略标记 Lighthouse 低分，并在判定性能回归前复跑核查。"
tags: ["lighthouse", "apify", "python", "web-performance"]
titleEn: "Set up scheduled Lighthouse alerts for key pages"
titleZh: "给关键页面设置 Lighthouse 定时告警"
blocks: [{"kind": "notice", "text": {"en": "For a scheduled alert, include the URL, device strategy, score, and one Lighthouse finding. Review the mobile and desktop results separately.", "zh": "定时告警可附上 URL、设备测试策略、分数和一条 Lighthouse 优化建议。移动端和桌面端结果分开查看。"}, "title": {"en": "What to put in the alert", "zh": "告警里放什么"}}]
type: "workflows"
version: "Fjord Labs Actor documentation excerpt · 2026-11-26"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T08:17:31+08:00"
sources: [{"title": "Catch a Core Web Vitals regression the day you deploy (Python and a cron job)", "url": "https://dev.to/fjordlabs/catch-a-core-web-vitals-regression-the-day-you-deploy-python-and-a-cron-job-47c0"}]
---
<p lang="zh-CN">同一个页面的移动端和桌面端表现可能不同。Fjord Labs 在其维护的 Apify 审计工具使用说明中，将两种测试策略应用到一小组关键 URL，由 Python 定期读取结果。输入是页面清单、测试策略和 Lighthouse 性能分数阈值，输出按页面与策略查看。<a href="https://dev.to/fjordlabs/catch-a-core-web-vitals-regression-the-day-you-deploy-python-and-a-cron-job-47c0">Fjord Labs 原文</a></p>

<p lang="en">A page can behave differently on mobile and desktop. In its guide to the Apify audit tool it maintains, Fjord Labs applies both test strategies to a short list of important URLs and uses Python to read the results on a schedule. The inputs are the page list, test strategies, and a Lighthouse performance threshold. Results are reviewed by page and strategy. <a href="https://dev.to/fjordlabs/catch-a-core-web-vitals-regression-the-day-you-deploy-python-and-a-cron-job-47c0">Fjord Labs’ guide</a></p>

<p lang="zh-CN">准备可运行该 Actor 的 Apify 凭据，先用少量页面试跑。按文档预期，调用完成后可从结果数据集读取各行，低于阈值的行带有 alert 标记。确认能按 URL 和设备策略找到对应结果后，再交给 cron 定时运行。</p>

<p lang="en">Prepare Apify credentials for the Actor and start with a small batch of pages. The documented behavior is that a completed run makes rows available in a result dataset, with an alert flag on rows below the threshold. Once you can match results to their URLs and test strategies, schedule the run with cron.</p>

<p lang="zh-CN">收到告警后，用同一测试策略复跑，再检查 Lighthouse 给出的优化项。实验室分数会波动，阈值只说明该次运行的分数偏低。查看真实用户体验时，先确认是否有该 URL 的现场数据，并把整个站点来源的汇总数据单独解读。</p>

<p lang="en">When an alert arrives, rerun the same test strategy and review the improvement opportunities Lighthouse reports. Lab scores fluctuate, and a threshold flag describes the score for that run. To assess real-user experience, check whether field data is available for the exact URL and interpret origin-wide data separately.</p>
