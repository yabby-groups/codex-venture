---
category: "open-source"
summaryEn: "Unsloth Desktop v0.1.921-beta reduces repeat prompt processing in local chats that use MCP tools. The project measured 83% to 87% fewer prompt tokens processed in its own tool tests."
summaryZh: "Unsloth Desktop v0.1.921-beta 减少了本地 MCP 对话多轮接话时的重复处理。项目方在自己的工具测试中报告，提示词 token 处理量下降了 83% 至 87%。"
tags: ["unsloth", "mcp", "local-inference"]
titleEn: "Unsloth Desktop beta reduces repeated prompt processing in MCP chats"
titleZh: "Unsloth Desktop 测试版减少 MCP 对话的重复提示词处理"
editorial: {"score": 63, "tier": "standard", "audience": "core"}
published: "2026-11-28T05:02:13+08:00"
sources: [{"title": "Bug Fixes + Faster images +Inkling Mini + faster MCP chats", "url": "https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta"}]
---
<p lang="zh-CN">在本地对话里调用 MCP 工具后，下一条追问仍会用到之前的对话。Unsloth 在 11 月 20 日发布的 Desktop v0.1.921-beta 中改了这一环节。按项目方的说明，使用 MCP 工具的对话无需在每条新消息到来时重新处理整段历史。</p>

<p lang="en">After an MCP tool call in a local chat, the next follow-up still draws on the earlier conversation. Unsloth changed how its desktop app handles that history in v0.1.921-beta, released on November 20. According to the project, chats that use MCP tools no longer reprocess the entire conversation with every new message.</p>

<p lang="zh-CN">Unsloth 在自己的工具测试中报告，提示词 token 处理量减少了 83% 至 87%。如果想判断本地长对话接话时的体感是否改善，可以在相同模型和工具配置下，分别观察提示词 token 处理量与发出追问后等到回复开始的时间。测试数字来自 <a href="https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta">Unsloth 的 beta 发布说明</a>。</p>

<p lang="en">Unsloth reported processing 83% to 87% fewer prompt tokens in its own tool tests. To gauge how the change feels in a long local chat, keep the model and tool configuration fixed and track both the prompt tokens processed and the time from sending a follow-up to seeing the reply begin. The test figures come from <a href="https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta">Unsloth’s beta release notes</a>.</p>
