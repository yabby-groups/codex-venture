---
category: "coding"
summaryEn: "CheckMyApp says a daily check found two unavailable YouTube links in a live guide, illustrating what teams can catch by rechecking published pages on a schedule."
summaryZh: "CheckMyApp 称，一次日常检查在已上线的指南中发现两处失效的 YouTube 链接，展示了定期复查生产页面能发现哪类故障。"
tags: ["production-testing", "link-checking", "checkmyapp"]
titleEn: "How a daily CheckMyApp run found broken video links in a live guide"
titleZh: "CheckMyApp 如何在日常检查中发现线上指南的失效视频链接"
type: "stories"
version: "CheckMyApp’s published case and check schedule as reviewed on 2026-11-25"
verified: "2026-11-25"
status: "current"
tested: false
published: "2026-11-25T21:04:05+08:00"
sources: [{"title": "Show HN: CheckMyApp – checks your live app with each deploy from coding agent", "url": "https://checkmyapp.dev/"}]
---
<p lang="zh-CN">一篇已经上线的指南也会出现新故障。CheckMyApp 在官网分享了一个例子：它对 meetbashar.com 运行日常检查时，发现指南中的 YouTube 视频有两处链接返回 404。按该服务商的记录，同轮检查中的另外 30 个视频链接仍可访问。<a href="https://checkmyapp.dev/">CheckMyApp 案例</a></p>

<p lang="en">A guide can develop a problem after it goes live. In an example published by CheckMyApp, a daily check of meetbashar.com found YouTube links returning 404 in two places in a guide. The vendor says the other 30 video links checked in the same run remained available. <a href="https://checkmyapp.dev/">CheckMyApp’s example</a></p>

<p lang="zh-CN">CheckMyApp 的做法是定期在生产站点走一遍用户选定的路径。按官网说明，团队接入 GitHub App 后，可以让关键路径在每次关联部署后重跑。其他选定路径每天检查一次，也会在对应页面变化时重跑。需要登录的路径使用测试账户。<a href="https://checkmyapp.dev/">检查频率和账户说明</a></p>

<p lang="en">CheckMyApp periodically runs selected user journeys against the live site. Its documentation says teams can connect the GitHub App to rerun critical journeys after each connected deployment. Other selected journeys run daily and when their pages change. Journeys that require signing in use a test account. <a href="https://checkmyapp.dev/">Check schedules and account setup</a></p>

<p lang="zh-CN">这个案例的结果限于一次由服务商披露的检查。记录到两处失效链接说明了定期检查能发现哪类问题。链接后来是否修复，以及日常检查能覆盖多少故障，仍待验证。</p>

<p lang="en">The evidence comes from a single check reported by the vendor. The two failures illustrate the kind of issue a scheduled check can surface. Whether the links were repaired and how many failures routine checks catch remain open questions.</p>
