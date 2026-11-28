---
category: "coding"
summaryEn: "Cursor's Agent SDK gives PR agents regression tests that can assert tool calls, arguments, and reply structure in CI. The release also lists a replay entry point for GitHub PRs."
summaryZh: "Cursor Agent SDK 支持在 CI 中检查 PR 代理的工具调用、参数和回复结构。发布日志还列出了 GitHub PR 的回放入口。"
tags: ["cursor", "agents", "evals", "ci"]
titleEn: "Cursor Agent SDK brings regression tests to PR agents"
titleZh: "Cursor Agent SDK 为 PR 代理加入回归测试"
editorial: {"score": 69, "tier": "standard", "audience": "core"}
published: "2026-11-28T16:16:20+08:00"
sources: [{"title": "Agent SDK", "url": "https://cursor.com/changelog/agent-sdk"}]
---
<p lang="zh-CN">Cursor 在 2026 年 10 月 20 日发布 Agent SDK，让团队把响应拉取请求（PR）事件的代理写成一个代码项目。指令、带类型的工具和事件接入分别管理。同一 PR 上的后续互动可以续接原会话，会话记录包含消息和工具调用。<a href="https://cursor.com/changelog/agent-sdk">Cursor 发布日志</a></p>

<p lang="en">Cursor released its Agent SDK on October 20, 2026, letting teams package a pull request (PR) agent as a code project. Instructions, typed tools, and event channels live in separate parts of the project. Follow-ups on the same PR can resume the original session, which records messages and tool calls. <a href="https://cursor.com/changelog/agent-sdk">Cursor changelog</a></p>

<p lang="zh-CN">给 PR 分流代理写回归测试时，可以用一条固定消息检查它调用了哪个工具、传入了什么参数，以及回复是否符合预期结构。测试可以在本地或 CI 中运行。发布日志还列出了 GitHub PR 的回放入口。事件接入则覆盖 GitHub、GitLab 和 Bitbucket。代理可部署到 Cursor 或团队自己的基础设施。</p>

<p lang="en">For a PR triage agent, a regression test can send a fixed message and check which tool the agent calls, what arguments it passes, and whether the reply has the expected structure. The tests can run locally or in CI. The changelog lists a replay entry point for GitHub PRs, while event support covers GitHub, GitLab, and Bitbucket. Teams can deploy the agent to Cursor or their own infrastructure.</p>
