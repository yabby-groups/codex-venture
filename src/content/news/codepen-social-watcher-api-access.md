---
category: "coding"
summaryEn: "A developer building a Slack feed for CodePen’s social replies spent weeks on the project. An AI agent could handle the API integrations, but each platform still required manual setup."
summaryZh: "一位开发者用 AI 为 CodePen 搭建社交回复汇总工具。代理可以处理 API 对接，但各平台仍需人工开通访问，项目前后花了数周。"
tags: ["codepen", "coding-agents", "api-integrations", "slack"]
titleEn: "Why building CodePen’s social reply tracker with AI still took weeks"
titleZh: "用 AI 为 CodePen 搭建社交回复监控，为何仍花了数周"
type: "stories"
version: "CodePen social media watcher, as described in the November 2026 account"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T10:02:45+08:00"
sources: [{"title": "Apps I've Vibe-Coded Lately That Are Pretty Damn Useful to Me", "url": "https://blog.master.dev/apps-ive-vibe-coded-lately-that-are-pretty-damn-useful-to-me-actually"}]
---
<p lang="zh-CN">CodePen 在九个社交平台上都有账号。逐个平台查看回复，对整个团队来说负担太重。master.dev 这篇自述的作者把目标定得很具体：让一个定时运行的云函数收集直接互动，把消息或链接汇总到 Slack，再由团队成员亲自回复。</p>

<p lang="en">CodePen had accounts on nine social platforms, and keeping up with replies on each one was too much to ask of the whole team. The author of the master.dev post set a concrete goal for a scheduled cloud function: collect direct interactions, send messages or links to Slack, and let team members reply in person.</p>

<p lang="zh-CN">按作者的说法，语言模型可以处理各平台不同的 API 对接，但逐个平台申请和配置 API 密钥仍需要人工参与，整个过程持续了数周。作者还指出，在这九个平台中，TikTok 是唯一没有提供这类互动读取 API 的平台。</p>

<p lang="en">In the author’s account, the language model could handle the differences between platform APIs, while provisioning API keys still took human work. Getting the project done took weeks. The author also identified TikTok as the one platform in the group without an API for reading this kind of engagement.</p>

<p lang="zh-CN">这段经历为类似的内部工具提供了一个工期判断：即使代理能写对接代码，平台逐一开通访问的时间也要单独估算。自述记录了作者的开发经历，实际节省了多少工时、上线后覆盖了哪些互动，仍缺少数据。</p>

<p lang="en">For similar internal tools, the account suggests budgeting separately for platform access even when an agent can write the integration code. The post documents the author’s development experience. Time savings and actual coverage after deployment remain unquantified.</p>
