---
category: "models"
summaryEn: "A 30-case pilot found that a source-only instruction reduced unsupported claims in two models. Scoring each answer separately also helped flag cases where the assistant overstated what the source said."
summaryZh: "一项 30 个案例的试点发现，要求仅依据材料作答后，两款模型的无依据陈述减少。逐问评分还能标记答案把原文说得过于绝对的情况。"
tags: ["evaluation", "grounding", "question-answering"]
titleEn: "A part-by-part test for what AI adds when sources leave gaps"
titleZh: "资料只答了三问中的两问，逐问评分能查出 AI 补写了什么"
editorial: {"score": 81, "tier": "standard", "audience": "core"}
published: "2026-11-28T18:02:25+08:00"
sources: [{"title": "When the Knowledge Runs Out: A Part-Level Pilot Evaluation of How Language Models Handle Partially Covered Questions", "url": "https://arxiv.org/abs/2611.33428"}]
---
<p lang="zh-CN">一份材料只覆盖三问中的两问，整题评分可能掩盖助手在第三问里补写的内容。11 月 26 日发布的一篇 arXiv 预印本把评分拆到子问题，并单独标记一种容易漏掉的情况：答案的主体有材料支持，却附带了一条无依据的断言。 <a href="https://arxiv.org/abs/2611.33428">arXiv 预印本</a></p>

<p lang="en">When a document covers two parts of a three-part question, a single score can hide what the assistant adds to the third answer. An arXiv preprint released on November 26 scores each part separately and flags a subtle failure: a supported answer that also contains an unsupported claim. <a href="https://arxiv.org/abs/2611.33428">arXiv preprint</a></p>

<p lang="zh-CN">在 30 个试点案例中，作者报告，加入一句“只依据所给材料作答”后，Claude Haiku 4.5 的无依据陈述率从 0.71 降到 0.00，Llama 3.1 8B 从 0.90 降到 0.06。人工标注仍发现，判断答案是否把原文说得更绝对尤其困难，例如把“许多求职网站禁止机器人”概括成一律禁止。</p>

<p lang="en">Across 30 pilot cases, the authors report that adding a single instruction to answer only from the supplied material reduced the unsupported-claim rate from 0.71 to 0.00 for Claude Haiku 4.5 and from 0.90 to 0.06 for Llama 3.1 8B. Human annotators still found it especially hard to judge when an answer overstated the source, such as turning a restriction on many job sites into a blanket ban.</p>

<p lang="zh-CN">知识库团队可以把这种设计用作回归测试。准备一份刻意留有缺项的材料，逐问检查助手是否准确回答了有证据的部分、是否指出缺少哪些信息，以及是否擅自扩大了原文的适用范围。论文中的降幅仅来自这两款模型在小规模试点上的结果。</p>

<p lang="en">Knowledge-base teams can adapt the design for regression testing. Leave a deliberate gap in a short reference and check each answer for correct use of evidence, acknowledgment of missing information, and any expansion of the source’s scope. The reported reductions come from a small pilot with two models.</p>
