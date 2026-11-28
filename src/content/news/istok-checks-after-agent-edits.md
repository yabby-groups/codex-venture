---
category: "coding"
summaryEn: "Istok’s developer describes recording both the check result and a fingerprint of the code it ran on. Reviewers can use the same rule to decide when an agent’s last edit calls for a fresh test run."
summaryZh: "Istok 开发者介绍了如何同时记录检查结果和受检代码的指纹。审阅者可以用同一条验收规则判断 Agent 的最后一次编辑是否需要触发重测。"
tags: ["istok", "coding-agents", "code-review", "testing"]
titleEn: "How to tell when an agent’s passing tests are out of date"
titleZh: "Agent 跑完测试又改了代码，怎样判断通过记录已过期？"
blocks: [{"kind": "notice", "text": {"en": "A passing check covers the command that ran and the code state it checked. Reviewers still decide whether that command covers the behavior that matters for the change.", "zh": "通过记录只能说明该命令在对应代码状态下通过。所选命令是否覆盖本次改动的关键行为，仍由审阅者判断。"}, "title": {"en": "What a passing check establishes", "zh": "通过记录能证明什么"}}]
type: "workflows"
version: "Istok check recording as described on 2026-11-24"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 84, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:01:54+08:00"
sources: [{"title": "My coding agent says \"done\". Here's how I make it prove it", "url": "https://dev.to/vtima/my-coding-agent-says-done-heres-how-i-make-it-prove-it-b38"}]
---
<p lang="zh-CN">Timur Valitov 让编码 Agent 修正分账后余下几分钱的分配。测试一度通过，Agent 随后又改了舍入逻辑，破坏了正确的结果。审阅者看到的是一句「测试全过」，当时的通过结果却对应最后一次编辑之前的代码。</p>

<p lang="en">Timur Valitov asked a coding agent to fix how leftover cents were distributed when splitting a bill. The tests passed, then the agent changed the rounding logic and broke the result. The reviewer saw a claim that all tests passed, but the passing run covered the code before that last edit.</p>

<p lang="zh-CN">Valitov 介绍的 Istok 是一个本地 CLI 和 MCP 服务。Agent 把检查交给 Istok 执行，由 Istok 保存退出码与输出，并记录受检代码的指纹。按作者的描述，指纹同时包含 Git 提交和该提交之上的改动。即使提交没变，审阅者也有依据判断后来编辑的工作区是否仍对应那次检查。</p>

<p lang="en">Valitov describes Istok as a local CLI and MCP server. The agent hands off a check to Istok, which runs it, stores the exit code and output, and fingerprints the code it checked. According to Valitov, that fingerprint includes the Git commit and changes on top of it. Even if the commit stays the same, reviewers have a way to tell whether later edits changed the working tree that was checked.</p>

<h2><span lang="zh-CN">把检查记录接到合并决定上</span><span lang="en">Use the check record to make the merge decision</span></h2>

<p lang="zh-CN">交给 Agent 修改代码前，先约定一条足以覆盖本次行为的检查命令。完成最后一次编辑后，由检查工具执行命令，并交付命令、退出码、输出和受检代码状态。审阅者先把记录与待合并的代码对上，再看检查结果。如果代码在检查之后又发生变化，就针对当前状态重跑相关检查，再作合并决定。</p>

<p lang="en">Before handing the change to an agent, agree on a check command that covers the behavior being changed. After the final edit, have the check runner execute it and hand over the command, exit code, output, and code state it checked. During review, match the record to the code awaiting merge before interpreting the result. If the code changed after the run, rerun the relevant check on the current state before deciding whether to merge.</p>

<p lang="zh-CN">本文依据 Valitov 的开发者自述，适用范围是文中描述的检查机制。具体 Istok 版本和自动阻止交付的条件仍待核实。<a href="https://dev.to/vtima/my-coding-agent-says-done-heres-how-i-make-it-prove-it-b38">Valitov 的原文</a></p>

<p lang="en">This workflow draws on Valitov’s developer account and covers the check mechanism he describes. The exact Istok version and the conditions for automatic enforcement remain unverified. <a href="https://dev.to/vtima/my-coding-agent-says-done-heres-how-i-make-it-prove-it-b38">Valitov’s original post</a></p>
