---
category: "agents"
summaryEn: "InferEdge’s evalkit turns failures from real agent runs into cases that domain experts can review before teams use them to check changes to prompts, tools, or skills."
summaryZh: "InferEdge 的 evalkit 把真实运行中的失败整理成评测用例，经领域专家审核后，可用于检查提示词、工具或技能的改动。"
tags: ["evalkit", "agent-evaluation", "regression-testing"]
titleEn: "How evalkit turns agent failures into expert-reviewed regression cases"
titleZh: "evalkit 如何把智能体失败变成经专家审核的回归用例"
type: "insights"
version: "InferEdge 项目文档 / InferEdge project documentation"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T00:04:42+08:00"
sources: [{"title": "Show HN: Evalkit for Improving Your Agents", "url": "https://inferedge-ai.github.io/evalkit"}]
---
<p lang="zh-CN">InferEdge 在 evalkit 的项目文档中把领域专家的审核放在失败挖掘和评测运行之间。系统从智能体的真实运行记录中找出失败，将其整理为候选用例，再由熟悉业务的人用自然语言确认什么结果算正确。这样，运行轨迹中的一次失败可以转成带有明确验收标准的回归用例。</p>

<p lang="en">In its evalkit documentation, InferEdge puts domain-expert review between mining failures and running evaluations. The system turns failures from real agent runs into candidate cases. Someone who knows the business then reviews in plain language what should count as a correct result. That gives a failure from a run trace an explicit acceptance criterion for regression testing.</p>

<p lang="zh-CN">审核通过的用例可以执行并产出分数和运行轨迹。按文档描述，编码智能体负责串联评测流程，evalkit 保存用例、审核、运行和历史记录，并对提示词、工具或技能给出带文件引用的修改建议。应用修改后可重跑同一批用例，检查结果是否符合先前确认的标准。现有文档摘录说明了流程设计，实际改进幅度仍待核实。<a href="https://inferedge-ai.github.io/evalkit">InferEdge 项目文档</a></p>

<p lang="en">Approved cases can be run to produce scores and trajectories. The documentation describes a coding agent driving the loop while evalkit stores cases, reviews, runs, and history and suggests file-linked changes to prompts, tools, or skills. After applying a change, teams can rerun the same cases against the criteria they approved earlier. The available documentation describes the workflow, while the size of any real-world improvement remains unverified. <a href="https://inferedge-ai.github.io/evalkit">InferEdge project documentation</a></p>
