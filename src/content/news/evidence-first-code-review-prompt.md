---
titleZh: "可复制的改动审查提示词"
titleEn: "A copyable prompt for reviewing a code change"
summaryZh: "要求 Agent 把可复现的问题和缺少的证据分别写出。"
summaryEn: "Ask an agent to distinguish reproducible findings from gaps in evidence."
type: "prompts"
category: "coding"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "Repository instructions / 68ba256"
status: "current"
tested: false
tags: ["code-review","evidence"]
sources: [{"title":"A copyable prompt for reviewing a code change – primary reference","url":"https://github.com/yabby-groups/codex-venture/blob/68ba256/AGENTS.md"}]
---
<p lang="zh-CN">适合能读取代码差异、相关调用点和测试结果的编程 Agent。输入包含变更意图、基础提交、待审差异和运行结果。把下方提示词复制到审查会话，并附上这些材料。</p>

<p lang="en">Use this with a coding agent that can read diffs, relevant call sites, and test results. Supply the change intent, base commit, proposed diff, and run results. Copy the prompt below into the review session and attach those inputs.</p>

<p lang="zh-CN"><code>以只读方式审查给定差异。每条发现提供文件和行号、触发条件、受影响的调用者以及最小验证方法。根据实际影响排序。分别列出已经运行的检查和仍缺的证据。未发现具体问题时，报告检查范围和剩余不确定性。</code> 这段提示词由本站整理，适合人工复核的报告。Agent 无法访问的数据和未运行的测试仍需维护者核查。</p>

<p lang="en">Review the supplied diff in read-only mode. For each finding give the file and line, triggering condition, affected caller, and smallest verification step. Order findings by impact. List checks that actually ran and evidence still missing. When there is no concrete finding, report the review scope and remaining uncertainty. This is an original template for a human-reviewed report. Maintainers still need to check inaccessible data and tests that were not run.</p>
