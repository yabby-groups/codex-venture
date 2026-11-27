---
category: "coding"
summaryEn: "kaju sends comments back to Claude Code with the quoted terminal output and lets reviewers bundle several notes into one submission."
summaryZh: "kaju 把批注连同选中的终端原文发回 Claude Code，也支持把多条意见攒在一起提交。"
tags: ["claude-code", "macos", "iterm2", "plan-review"]
titleEn: "How kaju attaches review comments to Claude Code output"
titleZh: "kaju 如何给 Claude Code 的终端输出加批注"
type: "insights"
version: "Public kaju documentation, verified 2026-11-27"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T08:21:07+08:00"
sources: [{"title": "Show HN: Kaju – Annotate, comment and collaborate with Claude Code", "url": "https://github.com/aigeano/kaju"}, {"title": "README", "url": "https://api.github.com/repos/aigeano/kaju/readme"}, {"title": "LICENSE", "url": "https://api.github.com/repos/aigeano/kaju/license"}]
---
<p lang="zh-CN">审阅 Claude Code 的长计划时，一条修改意见往往只针对其中一小段。aigeano 的 <a href="https://api.github.com/repos/aigeano/kaju/readme">kaju README</a>把审阅操作设计成从终端选区开始。选中输出后，Claude Code 会将选区复制到剪贴板，用户可通过快捷键写下批注。</p>

<p lang="en">When reviewing a long Claude Code plan, a comment often applies to just one passage. The <a href="https://api.github.com/repos/aigeano/kaju/readme">kaju README</a> from aigeano starts the review with a terminal selection. Claude Code copies the selection to the clipboard, and the reviewer opens a comment with a hotkey.</p>

<p lang="zh-CN">项目文档给出两种提交方式。单条反馈可以连同原文引句立即送回 Claude Code。审阅整份计划或说明时，可以先把多条批注收在侧栏，再一次提交。公开资料展示的是反馈如何附上原文并回到会话，实际节省的时间仍待测量。</p>

<p lang="en">The project documents two ways to submit feedback. A single comment can go straight back to Claude Code with the quoted text. For a full plan or explainer, reviewers can collect comments in a side panel and submit them together. The materials show how feedback returns to the session with its source text. Time savings remain unmeasured.</p>

<p lang="zh-CN">这个交接涉及明确的系统权限。按 README 的说明，在 iTerm2 中首次发批注时，macOS 会要求授予 Automation 权限，让 kaju 定位会话并向其中输入文字。仓库附有 <a href="https://api.github.com/repos/aigeano/kaju/license">Apache 2.0 许可证</a>。</p>

<p lang="en">That handoff has a documented permission requirement. According to the README, macOS asks for Automation access on the first comment in iTerm2 so kaju can locate the session and type into it. The repository includes an <a href="https://api.github.com/repos/aigeano/kaju/license">Apache 2.0 license</a>.</p>
