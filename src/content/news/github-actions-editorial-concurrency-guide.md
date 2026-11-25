---
titleZh: "在 GitHub Actions 中串行写入编辑队列"
titleEn: "Serialize editorial queue writes in GitHub Actions"
summaryZh: "按 GitHub 官方文档配置共享并发组，让更新同一队列的任务依次执行，并理解默认等待行为。"
summaryEn: "Use GitHub’s documented concurrency groups to serialize jobs that update shared editorial state and understand the default pending-run behavior."
type: "tutorials"
category: "coding"
published: "2026-11-25T20:59:04+08:00"
verified: "2026-11-25"
version: "GitHub Actions documentation, 2026-11-25"
status: "current"
tested: false
tags: ["ai-practice"]
sources: [{"title": "GitHub Actions concurrency documentation", "url": "https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency"}]
blocks: [{"kind": "code", "title": {"zh": "复核命令", "en": "Commands to reproduce"}, "language": "bash", "file": "", "code": "concurrency:\n  group: editorial-state\n  cancel-in-progress: false"}]
---

<p lang="zh-CN">多个工作流如果从同一个 Git 分支恢复队列，可能以同一份旧状态开始处理。再各自写回时，后一次写入可能发生冲突。把更新同一队列的工作流放进同一个并发组，可以让 GitHub 一次只运行一项。</p>

<p lang="en">When several workflows restore a queue from the same Git branch, they can start from the same old state and conflict when they later write it back. Give workflows that update that queue the same concurrency group so GitHub runs them one at a time.</p>

<p lang="zh-CN">设置位置取决于共享状态的范围。如果准备、编辑和发布共同占用一次队列写入，应使用工作流级别的 concurrency。若只有一个 Job 写入，官方文档也支持 Job 级别的设置。下面示例适用于同一仓库里共享 editorial-state 分支的工作流。</p>

<p lang="en">Set concurrency at the scope that owns the shared state. Use workflow-level concurrency when preparation, editing, and publication together hold a queue write. GitHub also documents job-level concurrency if a single job owns the write. The example targets workflows in the same repository sharing an editorial-state branch.</p>

<p lang="zh-CN">默认设置只保留一个待运行项，后续等待项可以替换它。cancel-in-progress: false 保住正在运行的一项。若调度工作不能丢，按官方文档评估更多等待项的设置，或把到期任务保存在队列状态中，让后续触发重新领取。本文是官方文档整理，示例未在单独仓库执行。</p>

<p lang="en">The default keeps one pending run, which a newer pending run can replace. Setting cancel-in-progress to false protects the active run. If scheduled work must survive, evaluate the documented larger queue or persist due work so a later trigger can claim it. This guide is based on GitHub’s documentation, and the example was not run in a separate repository.</p>
