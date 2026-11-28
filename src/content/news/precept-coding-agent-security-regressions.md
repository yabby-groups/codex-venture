---
category: "coding"
summaryEn: "In the PRECEPT preprint, coding agents often fixed an issue after seeing a failing security test, yet the same kind of issue recurred in roughly a quarter of fresh sessions. Teams can check whether a fix carries over by testing a different task against the same security requirement."
summaryZh: "PRECEPT 预印本发现，编码 Agent 看到失败的安全测试后通常能修复问题，但换到新会话，同类问题仍有约四分之一的复发率。团队可以用不同任务和同一条安全要求检查修复经验是否迁移。"
tags: ["coding-agents", "secure-coding", "regression-testing"]
titleEn: "Coding agents fixed security issues, then repeated them in fresh sessions"
titleZh: "编码 Agent 修好安全问题后，换个会话仍可能重犯"
blocks: [{"kind": "notice", "text": {"en": "For repository acceptance, record the security requirement in a rule a reviewer can inspect. Start a fresh agent session, assign a different task that must satisfy the same requirement, and run the repository’s security regression checks. Record the result separately from the original fix.", "zh": "做仓库验收时，把安全要求写成可供人工审查的规则。开启新会话，交给 Agent 一个仍须满足同一要求的不同任务，再运行仓库的安全回归检查。将这次结果与原修复分开记录。"}, "title": {"en": "Check whether the fix carries over", "zh": "检查修复经验能否迁移"}}]
editorial: {"score": 84, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:02:47+08:00"
sources: [{"title": "PRECEPT: Security Self-Improvement of Coding Agents via Evolving Principles", "url": "https://arxiv.org/abs/2611.33519"}]
---
<p lang="zh-CN">合并一次安全修复后，代码审查者还要判断 Agent 在下一项任务中能否守住同一条安全要求。11 月 26 日的 arXiv 记录显示，PRECEPT 预印本 v1 在 14 组任务序列中考察了 Codex、Claude Code 和 Qwen Code。作者报告，给 Agent 看失败的安全测试后，修复成功率为 85.7%。到了新会话，同类问题的复发率为 26.7%，接近此前未见过该问题的对照条件下的 27.5%。</p>

<p lang="en">After merging a security fix, code reviewers still need to know whether the agent can uphold the same requirement on its next task. In the PRECEPT v1 preprint listed by arXiv on November 26, the authors examined Codex, Claude Code, and Qwen Code across 14 task sequences. They report that the agents fixed the issue 85.7% of the time after seeing a failing security test. In a fresh session, the same class of issue recurred 26.7% of the time, close to 27.5% for agents that had never encountered it.</p>

<p lang="zh-CN">作者还尝试把修复记录放进持久上下文，但记录的作用仍局限于原任务所属的一类任务。论文提出 PRECEPT，让安全规则根据 Agent 实际出现的错误逐步修订。摘要中的上述数字描述的是论文要解决的跨会话问题。团队可以据此把原修复是否通过和新任务是否通过设为两项独立的验收记录。<a href="https://arxiv.org/abs/2611.33519">arXiv 预印本</a></p>

<p lang="en">The authors also tried saving the fix in persistent context, but its usefulness stayed tied to the original task family. The paper proposes PRECEPT, which revises security rules in response to the agent’s observed mistakes. The figures above describe the cross-session problem the method aims to address. Teams can track the original fix and the fresh-task regression check as separate acceptance results. <a href="https://arxiv.org/abs/2611.33519">arXiv preprint</a></p>
