---
category: "coding"
summaryEn: "Replay fixed bugs under the same grading rules to see where review instructions improve precision and which bugs the reviewer consistently misses."
summaryZh: "用统一评分规则回放已修复的缺陷，检查审查规则在哪些案例中提高精确率，又有哪些缺陷始终被漏掉。"
tags: ["ai-code-review", "evaluation", "reviewreplay"]
titleEn: "How to evaluate AI code review with bugs your team already fixed"
titleZh: "用团队已经修复的缺陷评估 AI 代码审查"
type: "workflows"
version: "ReviewReplay author’s 21-case evaluation, November 2026"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T00:04:30+08:00"
sources: [{"title": "I replayed 21 real bugs to Claude Code. A review skill helped in Python and not in Go.", "url": "https://dev.to/ggauravj05/i-replayed-21-real-bugs-to-claude-code-a-review-skill-helped-in-python-and-not-in-go-1paa"}]
---
<p lang="zh-CN">团队评估 AI 代码审查规则时，可以从已经修复的缺陷中挑选案例。Gaurav Jadhav 在 ReviewReplay 的作者文章里描述了这个做法。每个案例需要一份经过人工确认的答案，说明缺陷在哪里、为什么发生，以及哪项修复支持这个判断。定位引入缺陷的提交时，作者结合修复消息引用的提交或拉取请求，以及修复所改行的 Git 历史。<a href="https://dev.to/ggauravj05/i-replayed-21-real-bugs-to-claude-code-a-review-skill-helped-in-python-and-not-in-go-1paa">Gaurav Jadhav 的原文</a></p>

<p lang="en">Teams evaluating AI code review instructions can start with bugs they have already fixed. Gaurav Jadhav describes this approach in his write-up of ReviewReplay. Each case needs a human-checked answer key that records where the bug is, why it occurs, and which fix supports that judgment. To identify the change that introduced the bug, Jadhav uses commits or pull requests referenced in the fix message alongside the Git history of the lines changed by the fix. <a href="https://dev.to/ggauravj05/i-replayed-21-real-bugs-to-claude-code-a-review-skill-helped-in-python-and-not-in-go-1paa">Gaurav Jadhav’s article</a></p>

<p lang="zh-CN">按作者的方法，从缺陷引入前的父提交导出工作区，省略 Git 历史，再把引入缺陷的改动作为未提交的变更交给只读审查器。对同一批案例分别运行两种审查配置，保持案例和评分规则一致。作者对每种配置的每个案例运行三次。报告可按语言记录被识别的已知缺陷、严重发现中判定为正确的比例，以及每次都漏掉的案例，供团队决定审查规则在哪些仓库值得试用。</p>

<p lang="en">Following Jadhav’s procedure, export a workspace from the parent of the bug-introducing commit, omit Git history, and present the bug-introducing change as an uncommitted diff to a read-only reviewer. Run both review configurations against the same cases under the same grading rules. Jadhav ran each configuration three times per case. The report can group results by language and record known bugs caught, the share of serious findings graded as correct, and cases missed on every run. Those outputs give the team a basis for deciding where to trial the review instructions.</p>

<p lang="zh-CN">Jadhav 报告，在 12 个 Python 缺陷案例中，启用审查技能后，严重发现的精确率由 72% 升至 82%。在合计 9 个 JavaScript、TypeScript 和 Go 案例中，这一比例由 91% 降至 79%。21 个缺陷里有 4 个在所有运行中都被漏掉。数字来自作者的样本与评分，后三种语言只有合并结果。采用前可用团队自己的历史缺陷复查效果。</p>

<p lang="en">Jadhav reports that enabling the review skill raised precision on serious findings from 72% to 82% across 12 Python bug cases. Across nine JavaScript, TypeScript, and Go cases combined, it fell from 91% to 79%. Four of the 21 bugs were missed on every run. The figures reflect the author’s sample and grading, with one pooled result for the latter three languages. Teams can check the effect on their own historical bugs before adopting the instructions.</p>
