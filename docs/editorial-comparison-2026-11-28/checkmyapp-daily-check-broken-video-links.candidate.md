---
category: "coding"
summaryEn: "CheckMyApp reported that a daily check found one unavailable YouTube video linked twice in a live guide. The case gives teams a concrete reason to recheck external links between deploys."
summaryZh: "CheckMyApp 称，一次日常检查发现线上指南在两处引用了同一个已无法访问的 YouTube 视频。这个案例说明了为何可以在两次部署之间复查外链。"
tags: ["production-testing", "link-checking", "checkmyapp"]
titleEn: "A daily CheckMyApp run found one unavailable video linked twice in a live guide"
titleZh: "CheckMyApp 日检发现线上指南两次引用同一个失效视频"
type: "stories"
version: "CheckMyApp’s published case and check schedule as reviewed on 2026-11-25"
verified: "2026-11-25"
status: "current"
tested: false
published: "2026-11-25T21:04:05+08:00"
sources: [{"title": "Show HN: CheckMyApp – checks your live app with each deploy from coding agent", "url": "https://checkmyapp.dev/"}]
---

<p lang="zh-CN">CheckMyApp 在官网披露了一次对 meetbashar.com 的日常检查。线上冥想指南在两处链接到同一个 YouTube 视频，两次访问均返回 404。按服务商的记录，同轮检查的另外 30 个视频链接仍可访问。<a href="https://checkmyapp.dev/">CheckMyApp 案例</a></p>

<p lang="en">CheckMyApp published the results of a daily check on meetbashar.com. A live meditation guide linked to the same YouTube video in two places, and both requests returned a 404. The vendor reports that the other 30 video links in that run were available. <a href="https://checkmyapp.dev/">CheckMyApp case report</a></p>

<p lang="zh-CN">外部视频即使在站点没有部署新版本时也可能失效。按 CheckMyApp 的说明，接入其 GitHub App 后，标为关键的路径会在每次关联部署后检查。其他选定路径每天复查，也会在对应页面发生变化时重跑。该案例来自服务商的一次公开检查，指南后来是否修复仍待核实。<a href="https://checkmyapp.dev/">CheckMyApp 检查频率说明</a></p>

<p lang="en">An external video can become unavailable between site deploys. CheckMyApp says that after teams connect its GitHub App, it checks critical journeys after each connected deploy. Other selected journeys run daily and when their pages change. The case comes from a single check published by the vendor, and any subsequent repair remains unverified. <a href="https://checkmyapp.dev/">CheckMyApp scheduling documentation</a></p>
