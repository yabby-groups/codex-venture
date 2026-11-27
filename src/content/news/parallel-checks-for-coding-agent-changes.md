---
category: "coding"
summaryEn: "Magnus Ekdahl ran agent review, human review, and integration tests in parallel. Across the first 24 changes, he reported a 16% reduction in time to readiness for team review after adjusting for waits and stalls."
summaryZh: "Magnus Ekdahl 将代理审查、人工审查和集成测试并行启动。他报告称，在最初 24 项变更中，排除等待和停滞差异后，改动进入团队评审前的用时缩短了 16%。"
tags: ["coding-agents", "code-review", "integration-testing"]
titleEn: "Starting integration tests alongside code review shortened the wait for team review"
titleZh: "集成测试与代码审查并行，改动更早进入团队评审"
type: "stories"
version: "Magnus Ekdahl’s November 25, 2026 account and first 24 changes"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T22:01:43+08:00"
sources: [{"title": "Fix the process around coding agents before adding more of them", "url": "https://oxtan-maker.github.io/parallix/articles/parallel-ai-coding-bottleneck"}]
---
<p lang="zh-CN">在 2026 年 11 月 25 日发表的文章中，Magnus Ekdahl 描述了一处返工瓶颈。代码代理完成修改后，代理审查、人工审查和集成测试依次进行。集成测试一旦在末尾失败，修好的改动就得再走两轮审查，还需要有人转交诊断信息。</p>

<p lang="en">In an article published on November 25, 2026, Magnus Ekdahl described a source of rework. Once a coding agent finished a change, agent review, human review, and integration tests ran in sequence. A late integration test failure meant the repaired change had to go through both reviews again, and someone had to relay the diagnostics.</p>

<p lang="zh-CN">Ekdahl 将三个环节同时启动。如果自动检查失败，流程会撤回已发出的人工审查请求，由代理立即根据诊断信息修复。进入团队评审前，当前代码修订仍需通过全部三项检查。这种安排也意味着，自动检查报错时，人工审查可能已经开始。</p>

<p lang="en">Ekdahl started all three checks together. If an automated check failed, the workflow withdrew the human review request and sent the diagnostics to an agent for immediate repair. The current revision still had to pass all three checks before team review. With this setup, a human reviewer may already have started by the time an automated check fails.</p>

<p lang="zh-CN">作者的模型预计，从实现完成到可提交团队评审的用时会缩短 22%。在改动流程后的前 24 项变更中，Ekdahl 报告称，排除等待和停滞差异后，用时缩短了 16%。这是单一流程的小样本结果，衡量的是进入团队评审前的用时。</p>

<p lang="en">The author’s model predicted a 22% reduction in time from implementation to readiness for team review. For the first 24 changes under the new process, Ekdahl reported a 16% reduction after adjusting for differences in waits and stalls. The result covers one workflow and a small sample, with measurement ending when changes were ready for team review.</p>
