---
category: "agents"
summaryEn: "Mika’s Android demos show an agent working on a separate screen while the phone stays available for foreground use. The examples range from summarizing group chats to adding an item to a cart and stopping before checkout."
summaryZh: "Mika 的 Android 演示展示了 Agent 如何在独立屏幕上翻群聊、浏览帖子和加购，同时把前台留给用户。购物示例停在结账前。"
tags: ["android", "mika", "mobile-agents"]
titleEn: "Mika operates Android apps on a background screen while you use your phone"
titleZh: "Mika 把 Android 应用操作放到后台屏幕，前台仍可继续使用"
type: "open-source"
version: "Project README and demos reviewed 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
project: "b76b2493494fbb539255bf1367f8b0c21ac81d679898b352d435ecaf02e30848"
editorial: {"score": 76, "tier": "standard", "audience": "core"}
published: "2026-11-28T21:33:12+08:00"
sources: [{"title": "An on-device AI agent for Android", "url": "https://news.ycombinator.com/item?id=50623449"}, {"title": "Targeted research", "url": "https://github.com/wangzan101/mika"}]
---
<p lang="zh-CN">想让手机替你翻群聊，同时继续使用前台应用？Mika 项目文档介绍了一种做法：把 Agent 的应用操作放到独立的后台屏幕。项目团队展示了两种只读任务，让 Mika 翻阅群聊后总结当天讨论，或逐条阅读某位创作者的帖子后汇总近况。<a href="https://github.com/wangzan101/mika">Mika 项目仓库</a></p>

<p lang="en">Want your phone to catch up on a group chat while you keep using another app? Mika’s project documentation describes how it moves the agent’s app interactions to a separate background screen. The team demonstrates two read-only tasks: summarizing the day’s group chat and going through a creator’s recent posts one by one before summarizing them. <a href="https://github.com/wangzan101/mika">Mika repository</a></p>

<p lang="zh-CN">如果想先评估它适不适合自己的手机任务，可以从只读总结看起，再区分会改变应用状态的操作。项目的购物示例把商品加入购物车后停在结账前。发送消息的演示以四倍速播放，实际耗时仍待验证。本文依据 Apache-2.0 项目的仓库说明和演示编写，未运行应用。离线能力、系统权限和适用机型仍待核实。</p>

<p lang="en">If you’re deciding which tasks to try first, start with a read-only summary before moving to actions that change something in an app. In the shopping example, Mika adds an item to the cart and stops before checkout. The messaging demo runs at four times normal speed, so actual completion time remains unverified. This overview draws on the Apache-2.0 project’s documentation and demos. We did not run the app. Offline operation, system permissions, and device compatibility remain unverified.</p>
