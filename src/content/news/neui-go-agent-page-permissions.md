---
category: "coding"
summaryEn: "Neui ties an in-app agent’s access to the current user and screen. A design review can start by listing what the agent may read, click, and call on a single page."
summaryZh: "Neui 将应用内代理的权限与当前用户和页面关联。评估时可以从一页开始，列清代理能读的数据、能操作的控件和能调用的函数。"
tags: ["go", "doors", "agent-permissions"]
titleEn: "In a Go app, Neui lets developers decide what the agent can see and do"
titleZh: "用 Neui 在 Go 页面里声明代理能看什么、做什么"
type: "insights"
version: "Neui README reviewed 2026-11-27"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 77, "tier": "standard", "audience": "core"}
published: "2026-11-28T02:00:54+08:00"
sources: [{"title": "Show HN: Neui – Go web apps with a built-in AI agent", "url": "https://github.com/doors-dev/neui"}, {"title": "README", "url": "https://api.github.com/repos/doors-dev/neui/readme"}]
---
<p lang="zh-CN">给 Go 应用加助手时，表单提交和退款可以作为两个不同的授权决定。Neui 基于服务端 Go Web 框架 Doors。项目 README 描述的做法是在构建界面时选择代理可以读取和操作的部分，并把需受控开放的服务端操作封装成 Go 函数。代理在当前用户的会话内运行，可用能力会随用户和页面状态更新。<a href="https://api.github.com/repos/doors-dev/neui/readme">Neui README</a></p>

<p lang="en">When adding an assistant to a Go app, submitting a form and issuing a refund can be two separate permission decisions. Neui builds on Doors, a server-driven Go web framework. Its README describes choosing what an agent can read and operate as you build the UI, and exposing selected server-side actions as Go functions. The agent runs in the current user’s session, with capabilities that update with the user and screen state. <a href="https://api.github.com/repos/doors-dev/neui/readme">Neui README</a></p>

<p lang="zh-CN">用订单页做设计评审时，可以列出代理完成任务需要读取的字段、可以复用的页面操作，以及只对管理员开放的服务端函数。采用前需要估算把页面放进 Doors 并声明这些能力的改动量。之后可以用普通用户和管理员会话分别检查能力列表，并验证页面切换或权限变化后旧能力是否仍可调用。这些检查来自架构设计，README 描述的权限行为仍需在目标应用中验证。</p>

<p lang="en">For a design review of an order page, list the fields the agent needs to read, the existing UI actions it can reuse, and the server functions reserved for administrators. Before adopting Neui, estimate the work needed to build the page in Doors and declare those capabilities. Then check the available actions in both regular and administrator sessions, including whether a previously available action can still be called after navigation or a permission change. These are design checks. The behavior described in the README still needs verification in the target app.</p>
