---
titleZh: "用一段提示词让代码审查结果有证据"
titleEn: "A prompt for evidence-based code review"
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
updated: "2026-11-24"
blocks: [{"kind": "code", "title": {"zh": "复制审查提示词", "en": "Copy the review prompt"}, "language": "text", "file": "", "code": "以只读方式审查给定差异。每条发现提供文件和行号、触发条件、受影响的调用者以及最小验证方法。\n按实际影响排序。分开列出已经运行的检查和仍缺的证据。\n未发现具体问题时，报告检查范围和剩余不确定性。\n\nReview the supplied diff in read-only mode. For each finding, give the file and line, trigger, affected caller, and smallest verification step.\nOrder findings by impact. List checks that actually ran and evidence that is still missing.\nIf you find no concrete issue, report the scope and remaining uncertainty."}]
resourceIds: ["evidence-first-code-review"]
---

<p lang="zh-CN">把改动目的、基础提交、差异和已有测试结果附在提示词后。它适用于能读取代码差异和相关调用点的编程 Agent，输出可以直接用来核对每条发现及其影响。</p>

<p lang="en">Attach the change intent, base commit, diff, and existing test results to the prompt. It is for coding agents that can read the diff and its callers, and produces findings you can check individually.</p>

<p lang="zh-CN">如果 Agent 无法访问依赖服务或测试环境，维护者可以从报告末尾的待核实项继续。</p>

<p lang="en">If the agent lacks access to a dependency or test environment, use the remaining evidence gaps as a follow-up list.</p>
