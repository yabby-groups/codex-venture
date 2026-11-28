---
category: "agents"
summaryEn: "On a benchmark covering 12 groups of medical tasks, explicitly guiding agents to read and apply a skill raised skill-use accuracy by 43.94 percentage points on average."
summaryZh: "在覆盖 12 组医学相关任务的基准中，明确引导 Agent 阅读并应用技能，技能使用准确率平均提高 43.94 个百分点。"
tags: ["skills", "agent-harnesses", "evaluation"]
titleEn: "MedSkill-E² tests whether agents follow skills they already have"
titleZh: "技能已可用，Agent 有没有照做？MedSkill-E² 用同题对照检验"
editorial: {"score": 79, "tier": "standard", "audience": "core"}
published: "2026-11-28T18:02:25+08:00"
sources: [{"title": "MedSkill-E$^{2}$: Evaluating and Evolving Skills for Medical Agents", "url": "https://arxiv.org/abs/2611.34250"}]
---
<p lang="zh-CN">技能已经可用时，Agent 执行任务仍可能漏掉其中一条关键规则。11 月 26 日发布的 MedSkill-E² 预印本在 12 组医学相关任务中比较两种条件：让 Agent 自主使用可用技能，以及明确引导它阅读并应用同一份技能。 <a href="https://arxiv.org/abs/2611.34250">arXiv 预印本</a></p>

<p lang="en">An agent can have access to a skill and still miss a critical rule while carrying out a task. The MedSkill-E² preprint, released on November 26, compares two conditions across 12 groups of medical tasks: autonomous use of an available skill and explicit guidance to read and apply that same skill. <a href="https://arxiv.org/abs/2611.34250">arXiv preprint</a></p>

<p lang="zh-CN">作者报告，所有受测的模型与运行框架组合都出现了差距，显式引导下的技能使用准确率平均高出 43.94 个百分点。同一模型在不同框架下自主使用技能的准确率最多相差 38.96 个百分点。这些数字适用于论文中的医学基准。</p>

<p lang="en">The authors report a gap for every model and harness combination they tested. Explicit guidance raised skill-use accuracy by 43.94 percentage points on average. For the same model, autonomous skill-use accuracy varied by as much as 38.96 points across harnesses. These figures describe the paper’s medical benchmark.</p>

<p lang="zh-CN">维护编码 Agent 技能的团队可以借用这个对照设计。在相同任务和环境下各跑一轮，第二轮明确要求阅读并应用技能，再用同一份清单逐条核对关键约束。两轮结果的差异可以指出哪些规则在自主执行中容易漏用。</p>

<p lang="en">Teams that maintain coding-agent skills can borrow the comparison. Run the same task twice under the same setup, explicitly ask the agent to read and apply the skill in the second run, and score both outputs against the same checklist of critical constraints. Differences between the two runs can highlight rules the agent tends to miss on its own.</p>
