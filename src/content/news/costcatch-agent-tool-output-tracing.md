---
category: "coding"
summaryEn: "Costcatch wraps an existing agent command so developers can investigate whether a large tool result keeps adding to model input. Its cost figures are a starting point for diagnosis."
summaryZh: "Costcatch 可以套在现有 Agent 启动命令外，帮助排查一段过长的工具输出是否反复进入模型输入。费用数字可作为诊断线索。"
tags: ["costcatch", "agent-observability", "cli"]
titleEn: "Costcatch traces tool output that can drive up agent costs"
titleZh: "用 Costcatch 排查工具输出是否推高 Agent 开销"
type: "open-source"
version: "Project README reviewed 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
project: "16c1bc94eeac7d2ec914aefab71a5a55a50f9e0e696cf2d6b28f5c90f1a9057f"
editorial: {"score": 68, "tier": "standard", "audience": "core"}
published: "2026-11-28T12:04:16+08:00"
sources: [{"title": "Show HN: Costcatch – A CLI tool for Agent cost tracking and Debugging", "url": "https://news.ycombinator.com/item?id=50627927"}, {"title": "Targeted research", "url": "https://github.com/RonakRahane/costcatch"}]
---
<p lang="zh-CN">一次工具调用返回了很长的结果，开销可能延续到后续几轮。如果 Agent 每轮都把会话历史发回模型，同一段输出就可能反复进入模型输入。Costcatch 的项目文档给出的 Python 接入示例是 <code>costcatch python my_agent.py</code>。项目作者称，把 CLI 放在现有启动命令前即可追踪，无需修改 Agent 代码，追踪数据保存在本机。<a href="https://github.com/RonakRahane/costcatch">项目 README</a></p>

<p lang="en">A tool call that returns a long result can drive up input usage for several turns. If an agent sends the conversation history back to the model each time, the same output can appear in multiple requests. Costcatch’s documentation gives <code>costcatch python my_agent.py</code> as its Python example. The project says the CLI wraps the existing launch command without changes to the agent’s code and keeps trace data on the local machine. <a href="https://github.com/RonakRahane/costcatch">Project README</a></p>

<p lang="zh-CN">排查时可以从首次出现长输出的工具调用查起，再看后续轮次是否继续携带这段内容。本文依据项目文档，未运行追踪或核对供应商账单。金额可作为排查线索，实际收费以供应商账单为准。</p>

<p lang="en">Start with the tool call that first produced the long output, then check whether later turns carried it forward. This article is based on the documentation, with no trace run or provider bill checked. Treat the cost figures as diagnostic estimates and consult the provider’s bill for actual charges.</p>
