---
category: "coding"
summaryEn: "Claude Code v2.1.323 adds an opt-in mode that uses JavaScript to pass search results into edits, run independent checks in parallel, and make the generated script available in the session transcript."
summaryZh: "Claude Code v2.1.323 加入可选的 Code Mode。它用 JavaScript 把搜索结果交给后续编辑，并行运行独立检查，生成的脚本可在会话记录中查阅。"
tags: ["claude-code", "code-mode", "javascript"]
titleEn: "Claude Code’s experimental Code Mode chains search, edits, and tests in JavaScript"
titleZh: "Claude Code 实验性 Code Mode 用 JavaScript 串联搜索、编辑和测试"
editorial: {"score": 67, "tier": "standard", "audience": "core"}
published: "2026-11-28T08:06:20+08:00"
sources: [{"title": "v2.1.323", "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.323"}, {"title": "Targeted research", "url": "https://code.claude.com/docs/en/code-mode"}]
---
<p lang="zh-CN">Anthropic 在 2026 年 11 月 12 日发布的 Claude Code v2.1.323 中加入了 Code Mode。启用后，Claude 可以生成一段 JavaScript，由 Claude Code 在当前会话里执行，把多次工具调用组织在同一步中。该功能仍处于实验阶段，默认关闭。<a href="https://github.com/anthropics/claude-code/releases/tag/v2.1.323">版本发布说明</a></p>

<p lang="en">Anthropic introduced Code Mode in Claude Code v2.1.323 on November 12, 2026. When enabled, Claude can generate JavaScript that Claude Code runs in the current session, grouping several tool calls into a single step. The feature is experimental and off by default. <a href="https://github.com/anthropics/claude-code/releases/tag/v2.1.323">Release notes</a></p>

<p lang="zh-CN">以跨文件调整重试上限为例，可以先搜索相关实现，再从结果中筛选出目标文件。编辑要等筛选结果，验证新行为的测试也要等编辑完成。如果改完后要跑几项互不依赖的检查，脚本可以并行启动它们，再把各项检查的结果汇总给 Claude。<a href="https://code.claude.com/docs/en/code-mode">Code Mode 官方文档</a></p>

<p lang="en">For a retry-limit change that starts with a search across several files, the script can find the relevant implementations and filter the results to identify which files to edit. The edits depend on that selection, and tests that verify the new behavior depend on the edits being complete. Once the changes are in place, checks that do not depend on one another can run in parallel, with the script collecting their results for Claude. <a href="https://code.claude.com/docs/en/code-mode">Official Code Mode documentation</a></p>

<p lang="zh-CN">对话里会显示工具调用，例如编辑产生的 diff。要核对脚本选了哪些文件、按什么顺序调用工具，按 Ctrl+O 打开会话记录查看器，再展开对应的 Code 行。<a href="https://code.claude.com/docs/en/code-mode">会话记录查看方法</a></p>

<p lang="en">The conversation shows tool activity, such as the diff from an edit. To check which files the script selected and in what order it called the tools, press Ctrl+O to open the transcript viewer, then expand the corresponding Code row. <a href="https://code.claude.com/docs/en/code-mode">Transcript viewer instructions</a></p>
