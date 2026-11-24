---
titleZh: Codex CLI 0.172.0 加入会话跳转并修复恢复行为
titleEn: Codex CLI 0.172.0 adds session navigation and fixes resume behavior
summaryZh: 更新允许从记录中的线程链接进入已保存会话，并修复了恢复会话时读取原有权限与目录配置的行为。
summaryEn: The update opens saved sessions from thread links and fixes how resume restores permissions and working directories.
published: "2026-11-24T13:45:00+08:00"
category: coding
tags: [codex, cli]
sources:
  - title: Codex CLI 0.172.0 release notes
    url: https://github.com/openai/codex/releases/tag/rust-v0.172.0
---
<h2><span lang="zh-CN">会话链接可以直接打开记录</span><span lang="en">Thread links can open saved sessions</span></h2>

<p lang="zh-CN">OpenAI 的版本说明显示，用户可以从会话记录和转录文本中的线程链接打开已保存的会话或子 Agent 会话。命令中心的会话列表也新增了 Ctrl+Up 与 Ctrl+Down 分组切换。</p>

<p lang="en">OpenAI’s release notes say thread links in session results and transcripts can open saved conversations or subagent threads. The command center also adds Ctrl+Up and Ctrl+Down shortcuts for moving between session groups.</p>

<h2><span lang="zh-CN">恢复任务时的配置</span><span lang="en">Configuration when resuming a task</span></h2>

<p lang="zh-CN">发布说明记载，codex exec resume 会恢复已保存的沙箱权限、工作目录和可写路径，显式指定的新设置仍可覆盖它们。对依赖会话恢复的脚本来说，这项修复关系到续跑时在哪个目录执行，以及哪些路径能写入。</p>

<p lang="en">According to the release notes, codex exec resume restores saved sandbox permissions, the working directory and writable roots unless explicitly overridden. For scripts that resume sessions, the fix affects where a resumed run executes and which paths it can write to.</p>
