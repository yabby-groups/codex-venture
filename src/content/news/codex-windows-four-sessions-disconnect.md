---
category: "agents"
summaryEn: "A Windows user reported losing four active Codex sessions at roughly the same time. Reconnection and normal exit failed, and version 0.165.0 was recorded only after recovery."
summaryZh: "一位 Windows 用户报告，四个运行中的 Codex 会话几乎同时断线，无法重连或正常退出。0.165.0 是恢复后才记录到的版本。"
tags: ["codex-cli", "windows", "terminal", "incident-report"]
titleEn: "Four Codex sessions stopped responding together on Windows"
titleZh: "一位 Windows 用户的四个 Codex 会话几乎同时失去响应"
type: "stories"
version: "Windows 11, Codex CLI and app-server 0.165.0 observed after recovery"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T10:02:45+08:00"
sources: [{"title": "Windows Codex CLI/TUI: Four concurrent sessions disconnect, cannot reconnect, or exit normally", "url": "https://github.com/openai/codex/issues/57650"}]
---
<p lang="zh-CN">2026 年 10 月 28 日，GitHub 用户 benjamins1995 报告，四个分别在不同项目中执行长时间任务的 Codex 终端会话几乎同时停止更新。据其描述，自动重连未能恢复任何一个会话，正常退出也没有响应，多个 Codex 进程仍在运行。</p>

<p lang="en">On October 28, 2026, GitHub user benjamins1995 reported that four Codex terminal sessions running long-lived tasks across separate projects stopped updating at about the same time. According to the report, automatic reconnection restored none of the sessions, normal exit was unresponsive, and several Codex processes kept running.</p>

<p lang="zh-CN">恢复后，报告者在 Windows 11 上看到 Codex CLI 和受管理的 app-server 均为 0.165.0，且服务正在运行。故障发生时的客户端版本和诊断数据均未留存，因此 0.165.0 只能作为恢复后的环境记录。GitHub 将工单标为已完成并关闭，现有记录未说明故障原因或对应的修复版本。</p>

<p lang="en">After recovery, the reporter observed Codex CLI and its managed app-server at version 0.165.0 on Windows 11, with the server running. The CLI version and diagnostic data from the time of the failure were unavailable, so 0.165.0 describes the post-recovery environment. GitHub lists the issue as closed and completed. The available record leaves the cause and any fix version unresolved.</p>
