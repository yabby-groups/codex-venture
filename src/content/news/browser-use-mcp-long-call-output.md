---
category: "agents"
summaryEn: "Browser Use 1.0.7 returns partial output from long MCP calls within 50 seconds. A follow-up call with empty code retrieves more output from the same execution."
summaryZh: "Browser Use 1.0.7 会在 50 秒内为耗时较长的 MCP 调用返回已有输出。客户端随后可传入空代码，续取同一次执行的后续输出。"
tags: ["browser-use", "mcp", "cursor"]
titleEn: "Browser Use 1.0.7 lets MCP clients fetch more output from long browser tasks"
titleZh: "Browser Use 1.0.7 支持续取长耗时 MCP 浏览器任务的输出"
editorial: {"score": 75, "tier": "standard", "audience": "core"}
published: "2026-11-28T05:02:13+08:00"
sources: [{"title": "browser-use 1.0.7", "url": "https://github.com/browser-use/browser-use/releases/tag/1.0.7"}]
---
<p lang="zh-CN">Browser Use 在 11 月 20 日发布的 1.0.7 中调整了 MCP 的 browser_exec 响应方式。对 Cursor 等设有 60 秒请求上限的客户端，耗时较长的调用会在 50 秒内返回当时已有的输出，浏览器执行单元随后继续运行。能在 50 秒内完成的调用仍按原有方式返回。</p>

<p lang="en">Browser Use 1.0.7, released on November 20, changed how its MCP browser_exec tool responds to long calls. Clients with a 60-second request limit, such as Cursor, receive the output available so far within 50 seconds, while the browser execution keeps running. Calls that finish within 50 seconds respond as before.</p>

<p lang="zh-CN">例如，在自有站点做页面验收时，如果检查需要等待后台任务生成预览，第一批输出可能只记录了页面已打开。收到这批输出后，再调用一次 browser_exec，这次传入空代码，即可取回后续输出。页面验收是否完成，要看输出中是否已经包含预期的检查结果。交互顺序依据 <a href="https://github.com/browser-use/browser-use/releases/tag/1.0.7">Browser Use 1.0.7 发布说明</a>。</p>

<p lang="en">For example, if an acceptance check on your own site waits for a background job to generate a preview, the first response may only show that the page opened. After receiving that response, call browser_exec again with empty code to retrieve further output. Check for the expected result in the output before marking the acceptance check complete. This sequence follows the <a href="https://github.com/browser-use/browser-use/releases/tag/1.0.7">Browser Use 1.0.7 release notes</a>.</p>
