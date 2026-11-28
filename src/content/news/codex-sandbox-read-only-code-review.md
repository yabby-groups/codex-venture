---
category: "coding"
summaryEn: "OpenAI’s engineering write-up shows how Codex permission profiles can allow online documentation lookups while keeping source files read-only during code review."
summaryZh: "OpenAI 的工程文章给出了 Codex 权限配置档的评审用例。开发者可以开放网络查文档，同时保持源码只读。"
tags: ["codex"]
titleEn: "Codex can look up online docs during code review with source files set to read-only"
titleZh: "用 Codex 评审代码时，可以联网查文档并保持源码只读"
blocks: [{"columns": [{"en": "Task", "zh": "任务"}, {"en": "Filesystem access", "zh": "文件系统权限"}, {"en": "Network access", "zh": "网络权限"}], "kind": "comparison", "rows": [[{"en": "Review code and consult online docs", "zh": "评审代码并查在线文档"}, {"en": "Keep source files read-only", "zh": "源码保持只读"}, {"en": "Allow network access", "zh": "允许联网"}], [{"en": "Organize local photos", "zh": "整理本地照片"}, {"en": "Allow reads and writes in the designated photo directory", "zh": "允许读取和修改指定照片目录"}, {"en": "Block network access", "zh": "禁止联网"}]], "title": {"en": "Permissions for two local tasks", "zh": "两种本地任务的权限搭配"}}]
editorial: {"score": 64, "tier": "standard", "audience": "core"}
published: "2026-11-28T11:45:41+08:00"
sources: [{"title": "Inside the Codex sandbox", "url": "https://openai.com/index/inside-the-codex-sandbox"}]
---
<p lang="zh-CN">OpenAI 的 Michael Bolin 在 2026 年 11 月 18 日发表的工程文章中，以代码评审为例说明 Codex 的本地命令权限如何搭配。评审需要查在线文档时，可以允许联网，同时让命令只能读取源码。<a href="https://openai.com/index/inside-the-codex-sandbox">OpenAI 工程文章</a></p>

<p lang="en">In an OpenAI engineering article published on November 18, 2026, Michael Bolin uses code review to show how permissions for local Codex commands can be combined. When a review requires online documentation, developers can allow network access while keeping source files read-only. <a href="https://openai.com/index/inside-the-codex-sandbox">OpenAI engineering article</a></p>

<p lang="zh-CN">权限配置档定义 Codex 会话的文件系统和网络限制。为团队设置评审配置档时，可以先确认命令需要读取哪些文件、任务是否需要联网，再为确实要修改本地文件的任务单独设定写入范围。</p>

<p lang="en">Permission profiles define filesystem and network limits for a Codex session. When setting up a review profile for a team, identify which files commands need to read and whether the task needs network access. Set a separate writable scope for tasks that need to change local files.</p>
