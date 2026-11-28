---
category: "open-source"
summaryEn: "Cloudflare released its Kitesurf browser engine under Apache 2.0. Developers can run it locally or deploy it to their own Workers account and connect with Puppeteer."
summaryZh: "Cloudflare 以 Apache 2.0 许可证发布 Kitesurf 浏览器引擎。开发者可在本地运行，也可部署到自己的 Workers 账户，再用 Puppeteer 连接。"
tags: ["cloudflare-workers", "kitesurf", "puppeteer", "browser-automation"]
titleEn: "Cloudflare open-sources Kitesurf, a browser engine that runs on Workers"
titleZh: "Cloudflare 开源 Kitesurf，可在 Workers 上运行浏览器引擎"
editorial: {"score": 74, "tier": "standard", "audience": "core"}
published: "2026-11-28T12:33:25+08:00"
sources: [{"title": "Kitesurf is now open source", "url": "https://blog.cloudflare.com/kitesurf-open-source"}]
---
<p lang="zh-CN">Cloudflare 于 2026 年 11 月 13 日在 GitHub 上以 Apache 2.0 许可证开源 Kitesurf。Celso Martinho、Rui Figueira、Bernardo Pereira 和 Luís Duarte 在发布公告中写道，开发者可以在本地运行和修改代码，也可以把自己的实例部署到自己的 Cloudflare Workers 账户。</p>

<p lang="en">Cloudflare released Kitesurf on GitHub under the Apache 2.0 license on November 13, 2026. In the announcement, Celso Martinho, Rui Figueira, Bernardo Pereira, and Luís Duarte said developers can run and modify the code locally or deploy their own instance to their Cloudflare Workers account.</p>

<p lang="zh-CN">Kitesurf 是面向 AI Agent 的无状态浏览器引擎。它能在 Workers 上解析 HTML、应用 CSS、执行页面 JavaScript 并生成截图，无需单独维护浏览器容器。引擎支持 Chrome DevTools Protocol（CDP），已有 Puppeteer 脚本的团队可以沿用这个客户端来试用新后端。</p>

<p lang="en">Kitesurf is a stateless browser engine for AI agents. It parses HTML, applies CSS, runs page JavaScript, and captures screenshots on Workers without a separate browser container to maintain. It supports the Chrome DevTools Protocol (CDP), so teams with existing Puppeteer scripts can use the same client to try the new backend.</p>

<p lang="zh-CN">可以先选一个自有站点的页面，检查 JavaScript 执行后关键内容是否出现、交互是否按预期完成，以及截图是否符合要求。需要跨步骤保留登录或页面状态的流程，应单独验证其状态能否在现有调用方式下延续。<a href="https://blog.cloudflare.com/kitesurf-open-source">Cloudflare 开源公告</a></p>

<p lang="en">A first trial could use a page you control to check whether key content appears after JavaScript runs, interactions behave as expected, and the screenshot meets your needs. For workflows that depend on login or page state across steps, check separately whether your existing sequence of calls preserves that state. <a href="https://blog.cloudflare.com/kitesurf-open-source">Cloudflare’s open-source announcement</a></p>
