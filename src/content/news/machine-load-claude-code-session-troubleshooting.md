---
category: "coding"
summaryEn: "machine-load groups background jobs and Docker containers by the Claude Code session or project that started them, giving Mac developers a place to look when several sessions compete for resources."
summaryZh: "machine-load 把后台任务和 Docker 容器归到发起它们的 Claude Code 会话或项目，方便 Mac 用户在多个会话争用资源时缩小排查范围。"
tags: ["claude-code", "macos", "troubleshooting"]
titleEn: "Which Claude Code session is slowing down your Mac?"
titleZh: "Mac 卡顿时，怎么找出占资源的 Claude Code 会话？"
type: "insights"
version: "macOS · Claude Code · README 核对于 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T16:02:11+08:00"
sources: [{"title": "Show HN: Machine-load – see which AI coding session is slowing your Mac", "url": "https://github.com/Stak-Technologies/machine-load"}]
---
<p lang="zh-CN">Mac 上同时跑着几个 Claude Code 会话时，看到一排同名的 node 进程，很难判断该先查哪项工作。Stak Technologies 在 machine-load 的 README 中描述了一种按会话排查的方式：把子进程、已脱离父进程的后台任务和 Docker 容器，归到启动它们的 Claude Code 会话或项目下。</p>

<p lang="en">When several Claude Code sessions are running on a Mac, a list of identically named node processes offers little help in deciding where to look first. In the machine-load README, Stak Technologies describes a session-based view that groups child processes, detached background jobs, and Docker containers under the Claude Code session or project that started them.</p>

<p lang="zh-CN">遇到卡顿时，可以在 Claude Code 中打开 /load，先看最近 30 分钟的负载走势，再按 CPU 或内存用量给明细排序。负载图用来判断卡顿是否伴随负载上升，排序则帮助缩小检查范围，比如先查看某个会话名下的后台任务，再决定是否暂停它。</p>

<p lang="en">During a slowdown, open /load in Claude Code to check the past 30 minutes of load, then sort the details by CPU or memory usage. The chart helps you see whether load rose around the slowdown. Sorting narrows the search so you can inspect a session’s background jobs before deciding whether to pause one.</p>

<p lang="zh-CN">machine-load 仅支持 macOS，仓库采用 MIT 许可。Stak Technologies 将其作为第三方工具按现状提供，且不提供支持。上述排查方式依据 README 整理，复杂进程树和容器的归因准确性未经实测。<a href="https://github.com/Stak-Technologies/machine-load">项目仓库</a></p>

<p lang="en">machine-load is macOS-only, and the repository uses the MIT license. Stak Technologies provides it as an unsupported third-party tool. This troubleshooting approach comes from the README. Attribution accuracy for complex process trees and containers has not been tested for this article. <a href="https://github.com/Stak-Technologies/machine-load">Project repository</a></p>
