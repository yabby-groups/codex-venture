---
category: "agents"
summaryEn: "Browser Automation in Foundry Agent Service is generally available with live viewing, human takeover, session recording, and traces. VNet injection for private sites remains in preview."
summaryZh: "Foundry Agent Service 的浏览器自动化已正式可用，支持实时查看、人工接管、会话录制和追踪。访问私有站点所需的 VNet 注入仍处于预览阶段。"
tags: ["microsoft-foundry", "browser-automation", "azure-playwright-workspaces"]
titleEn: "Microsoft Foundry browser automation reaches GA with human session takeover"
titleZh: "Microsoft Foundry 浏览器自动化正式可用，操作人员可接管代理会话"
blocks: [{"kind": "notice", "text": {"en": "VNet injection for access to private websites is in preview. Microsoft listed sign-in profile reuse as an upcoming preview.", "zh": "用于访问私有网站的 VNet 注入仍处于预览阶段。微软将登录配置复用列为即将推出的预览功能。"}, "title": {"en": "Check these dependencies before the pilot", "zh": "试点前确认这两项依赖"}}]
editorial: {"score": 72, "tier": "standard", "audience": "core"}
published: "2026-11-28T11:34:36+08:00"
sources: [{"title": "Browser Automation Tool in Microsoft Foundry : Ignite’26 Announcements", "url": "https://devblogs.microsoft.com/foundry/browser-automation-tool-ignite"}]
---
<p lang="zh-CN">如果代理跑到企业旧门户的登录页，操作人员可以用 Live View 查看当前浏览器会话，再用 Take control 接手登录或纠正操作。微软博客作者 Nandini 和 Abhinav 于 2026 年 11 月 18 日宣布，Foundry Agent Service 的 Browser Automation 工具已正式可用。该工具由 Azure Playwright Workspaces 提供支持，为代理运行提供隔离的云浏览器会话。</p>

<p lang="en">When an agent reaches the sign-in page of a legacy internal portal, an operator can use Live View to inspect the current browser session and Take control to sign in or correct an action. Microsoft blog authors Nandini and Abhinav announced on November 18, 2026, that the Browser Automation tool in Foundry Agent Service is generally available. Powered by Azure Playwright Workspaces, it provides isolated cloud browser sessions for agent runs.</p>

<p lang="zh-CN">会话录制和追踪也已正式可用。试点团队可以先约定谁负责登录或异常接手，再用录制和追踪复盘代理走到了哪一步、人工何时介入。<a href="https://devblogs.microsoft.com/foundry/browser-automation-tool-ignite">微软发布说明</a></p>

<p lang="en">Session recording and traces are also generally available. Pilot teams can assign someone to handle sign-ins and exceptions, then use the recording and traces to review how far the agent got and when a person stepped in. <a href="https://devblogs.microsoft.com/foundry/browser-automation-tool-ignite">Microsoft’s announcement</a></p>
