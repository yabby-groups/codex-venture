---
category: "coding"
summaryEn: "Gemini CLI now parses PowerShell commands asynchronously to keep the progress spinner responsive during parsing."
summaryZh: "Gemini CLI 改用异步方式解析 PowerShell 命令，避免解析期间进度动画卡住。"
tags: ["gemini-cli", "powershell"]
titleEn: "Gemini CLI 0.71.0 fixes a spinner freeze during PowerShell parsing"
titleZh: "Gemini CLI 0.71.0 修复解析 PowerShell 命令时的进度动画卡顿"
published: "2026-11-25T20:08:46+08:00"
sources: [{"title": "Release v0.71.0", "url": "https://github.com/google-gemini/gemini-cli/releases/tag/v0.71.0"}]
---
<p lang="zh-CN">Gemini CLI v0.71.0 于 2026 年 11 月 24 日发布。使用 PowerShell 的用户此前可能在 CLI 解析命令时看到进度动画卡住。发布记录显示，@tadipavan 将核心与命令行界面的 PowerShell 命令解析改为异步，以避免解析阻塞进度动画。</p>

<p lang="en">Gemini CLI v0.71.0 was released on November 24, 2026. Users running PowerShell commands could previously see the CLI’s progress spinner freeze during parsing. According to the release notes, @tadipavan made PowerShell command parsing asynchronous in the core and CLI so parsing would no longer block the spinner.</p>
