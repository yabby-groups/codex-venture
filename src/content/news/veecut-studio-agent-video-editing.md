---
category: "open-source"
summaryEn: "VeeCut Studio uses built-in editing recipes to turn a recording into a first cut. A coding agent and the desktop editor work on the same project, so creators can refine the timeline by hand."
summaryZh: "VeeCut Studio 让编码代理按内置规则把录屏剪成初稿。创作者可以在桌面编辑器里打开同一个项目，接着手工调整时间线。"
tags: ["video-editing", "coding-agents", "rust"]
titleEn: "VeeCut Studio pairs agent-made rough cuts with a desktop timeline"
titleZh: "VeeCut Studio 让编码代理剪初稿，再用桌面时间线精修"
type: "open-source"
version: "Repository documentation reviewed 2026-11-28"
verified: "2026-11-28"
status: "current"
tested: false
project: "48ffe04b1dad1d157ac878a4b52ef0cac34aaa79b29562dfb2abb54d8f74084c"
editorial: {"score": 74, "tier": "standard", "audience": "core"}
published: "2026-11-28T09:16:26+08:00"
sources: [{"title": "Demonbane18/veecut-studio", "url": "https://github.com/Demonbane18/veecut-studio"}]
---
<p lang="zh-CN">剪产品演示录屏时，可以先让编码代理出一版粗剪，再在桌面编辑器里调整某处切点或字幕。Demonbane18 的 VeeCut Studio README 描述了这条流程：把录屏放进文件夹，由代理调用 VeeCut 命令行工具，按内置规则完成剪切、构图、字幕和混音，再渲染初稿。</p>

<p lang="en">For a product demo recording, a coding agent can make the rough cut, leaving you to fine-tune a cut or caption in the desktop editor. Demonbane18’s VeeCut Studio README describes the workflow: put the recording in a folder, have the agent call the VeeCut CLI, and let built-in rules handle cuts, framing, captions, and audio mixing before rendering a draft.</p>

<p lang="zh-CN">项目文档列出十种视频类型的剪辑规则，并说明创作者可以用英语、塔加洛语或 Taglish 提修改意见。命令行和桌面编辑器通过同一个 Editor API 修改项目，文档说明这些更改可以撤销。评估是否适合现有工作流时，可以先看自己的片型有没有对应规则，以及团队是否方便用这些语言反馈。</p>

<p lang="en">The documentation lists editing recipes for ten video types and says creators can give revision notes in English, Tagalog, or Taglish. The CLI and desktop editor modify the project through the same Editor API, and the documentation says those changes can be undone. To assess the fit, check whether a recipe covers the videos you make and whether your team can give feedback in one of the documented languages.</p>

<p lang="zh-CN">项目采用 MIT 许可证。本文依据截至 2026 年 11 月 28 日的官方文档，未运行剪辑流程。<a href="https://github.com/Demonbane18/veecut-studio">VeeCut Studio 官方仓库</a></p>

<p lang="en">The project uses the MIT license. This article is based on official documentation as of November 28, 2026. The editing workflow was not run. <a href="https://github.com/Demonbane18/veecut-studio">Official VeeCut Studio repository</a></p>
