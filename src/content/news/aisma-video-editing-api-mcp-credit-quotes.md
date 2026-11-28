---
category: "video"
summaryEn: "Aisma quotes the credit cost before editing a 2–60 second clip. Creators can integrate the quote into a REST workflow or confirm spending through an MCP-connected assistant."
summaryZh: "Aisma 在编辑 2 至 60 秒的短片前给出点数报价。创作者可以把报价接入 REST 工作流，也可以通过连接 MCP 的助手确认支出。"
tags: ["aisma", "video-editing", "rest-api", "mcp"]
titleEn: "Aisma quotes credit costs before video edits through REST or MCP"
titleZh: "Aisma 通过 REST 和 MCP 提供短片编辑的点数报价"
editorial: {"score": 73, "tier": "standard", "audience": "core"}
published: "2026-11-28T21:02:05+08:00"
sources: [{"title": "Show HN: Aisma – edit footage you shot from a text brief, via REST API or MCP", "url": "https://news.ycombinator.com/item?id=50627633"}, {"title": "Targeted research", "url": "https://aisma.ai/developers"}]
---
<p lang="zh-CN">Aisma 的开发者接口可以用自然语言修改一段已拍好的镜头，例如替换背景或服装。输入须为 2 至 60 秒的 MP4 或 MOV，文件最大 500 MB。一次编辑可以附带最多 10 张参考图。流程从上传和报价开始，提交编辑后可取回结果。</p>

<p lang="en">Aisma’s developer interfaces accept plain-language instructions for editing a clip you’ve already shot, such as replacing a background or changing an outfit. The input must be a 2–60 second MP4 or MOV up to 500 MB. An edit can include up to 10 reference images. The workflow starts with upload and pricing, followed by submission and result retrieval.</p>

<p lang="zh-CN">按 Aisma 的开发者文档，用脚本时可以通过个人 API 密钥调用 REST API，并用 Webhook 接收任务状态。通过助手编辑时，远程 MCP 使用 OAuth 登录，文档称助手会在消耗点数前征询用户。两种入口共用 Aisma 账户的点数，结果都进入该账户的素材库。<a href="https://aisma.ai/developers">Aisma 开发者文档</a></p>

<p lang="en">According to Aisma’s developer documentation, scripts can use a personal key for the REST API and receive job updates via webhooks. The remote MCP server uses OAuth, and Aisma says the assistant asks before spending credits. Both routes draw from the same Aisma credit balance and save results to the account’s library. <a href="https://aisma.ai/developers">Aisma developer documentation</a></p>
