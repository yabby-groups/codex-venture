---
category: "agents"
summaryEn: "Muxlio’s example pairs an immutable plan with persistent run records, pauses after 10 unsuccessful checks, and leaves the push decision to a person."
summaryZh: "Muxlio 的官网示例按不可变计划执行并保存每次尝试的记录，10 次检查未通过后暂停，推送由人决定。"
tags: ["muxlio", "coding-agents", "workflow-orchestration"]
titleEn: "How Muxlio records coding-agent retries and hands off local commits"
titleZh: "Muxlio 怎样记录编码代理的重试，并把本地提交交给人审阅"
type: "insights"
version: "官网工作流示例，2026-11-28 核对 / Workflow example reviewed 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T10:04:10+08:00"
sources: [{"title": "Muxlio: Durable workflow orchestration for AI agents and tools", "url": "https://muxlio.github.io/muxlio"}]
---
<p lang="zh-CN">当编码代理连续处理多个小功能时，测试失败后往往需要回看计划、失败尝试和留下的产物。Muxlio 官网把一份计划和一次运行分开记录。协调器按提交时的不可变 JSON 计划执行，计划带有内容摘要，每次运行的状态、尝试、日志和产物则会保存下来。<a href="https://muxlio.github.io/muxlio">Muxlio 官网</a></p>

<p lang="en">When a coding agent works through a batch of small features, a failed test can send you back to inspect the plan, the earlier attempts, and their artifacts. The Muxlio site describes separate records for the plan and each run. The coordinator executes the submitted immutable JSON plan, which carries a content digest, and saves each run’s state, attempts, logs, and artifacts. <a href="https://muxlio.github.io/muxlio">Muxlio website</a></p>

<p lang="zh-CN">官网示例让代理依次实现功能、审查改动并运行检查。检查失败则进入修复和重试，累计 10 次检查未通过就暂停。检查通过后，示例在本地提交，由人审阅提交并决定何时推送。这里的 10 次是示例流程给出的上限。</p>

<p lang="en">In the site’s example, agents implement a feature, review the change, and run checks. A failed check triggers repair and another attempt, and the run pauses after 10 unsuccessful checks. Once the checks pass, the example creates a local commit for a person to review and decide when to push. The 10-attempt limit belongs to that example.</p>

<p lang="zh-CN">借用这个例子设计自己的流程时，可以先定下允许提交的检查结果、达到重试上限时要查看的日志和产物，以及由谁接手。本文依据官网示例，未运行该流程，实际的暂停与重新接手过程仍需在部署环境中验证。</p>

<p lang="en">To adapt the example, decide which checks must pass before committing, which logs and artifacts someone should inspect at the retry limit, and who takes over. This article is based on the official example and did not run it. The pause and handoff still need verification in the deployment environment.</p>
