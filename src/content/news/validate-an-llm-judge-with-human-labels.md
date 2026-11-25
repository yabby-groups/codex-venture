---
category: "coding"
summaryEn: "Start with a recurring product failure, have a domain expert label held-out examples, and review the model judge’s missed failures and false alarms before relying on it."
summaryZh: "从一种反复出现的产品失败入手，请领域专家标注留出样本，再用漏判和误判记录判断模型裁判是否适合投入使用。"
tags: ["evals", "llm-as-a-judge", "human-labeling"]
titleEn: "How to validate an LLM judge on one product failure"
titleZh: "用人工标签验证模型裁判：从一种产品失败入手"
blocks: [{"kind": "notice", "text": {"en": "Agreement applies to the rubric, sampled cases, and judge configuration you tested. When any of those change, check agreement again before using the scores to make a release decision.", "zh": "一致性结果只适用于本轮使用的判定规则、样本和裁判配置。任何一项变化后，先重新核对一致性，再用评分做发布决策。"}, "title": {"en": "When to rerun validation", "zh": "何时重新验证"}}]
type: "workflows"
version: "文档分析 / Documentation-based workflow. Judge guide revision 2026-09-01 and field guide publication 2025-03-24."
verified: "2026-11-25"
status: "current"
tested: false
published: "2026-11-25T20:56:31+08:00"
sources: [{"title": "Using LLM-as-a-Judge For Evaluation: A Complete Guide", "url": "https://hamel.dev/blog/posts/llm-judge"}, {"title": "A Field Guide to Rapidly Improving AI Products", "url": "https://hamel.dev/blog/posts/field-guide"}]
---
<p lang="zh-CN">当团队说不清一个回答为什么只得了 3 分，先回到实际输出，找出用户能感知的一种失败。Hamel Husain 在评估实战指南中把错误分析放在产品迭代的起点，并在模型裁判指南中建议由领域专家参与判断，再用人工标签验证模型裁判。下面是一套基于两篇指南设计的小规模工作流。<a href="https://hamel.dev/blog/posts/field-guide">评估实战指南</a> · <a href="https://hamel.dev/blog/posts/llm-judge">模型裁判指南</a></p>

<p lang="en">If your team can’t explain why an answer received a three, go back to the actual outputs and identify one failure a user would notice. Hamel Husain’s field guide puts error analysis at the start of product iteration. His guide to model judges calls for domain expert input and validation against human labels. The small-scale workflow below draws on both guides. <a href="https://hamel.dev/blog/posts/field-guide">Field guide</a> · <a href="https://hamel.dev/blog/posts/llm-judge">Model judge guide</a></p>

<h2><span lang="zh-CN">把失败写成一条可判定的规则</span><span lang="en">Turn one failure into a rule you can apply</span></h2>

<p lang="zh-CN">准备一批可供领域专家审阅的输入、输出及必要上下文。以客服助手为例，可以请专家找出助手给出承诺、但所附政策内容并不支持该承诺的案例。把规则写成一个能回答“是”或“否”的问题，并单独标记证据缺失的案例，交给人工复核。先用几条典型和边界样例确认规则含义，再用这些样例编写裁判提示词，要求给出标签和一句依据。</p>

<p lang="en">Give a domain expert a batch of inputs, outputs, and the context needed to review them. For a support assistant, the expert might look for promises that the accompanying policy text fails to support. Phrase the rubric as a yes-or-no question, and flag cases with missing evidence for human review. Use a few clear and borderline cases to settle the wording, then use those examples to write a judge prompt that returns a label and one sentence of reasoning.</p>

<h2><span lang="zh-CN">用留出的人工标签检查分歧</span><span lang="en">Check disagreements on held-out human labels</span></h2>

<p lang="zh-CN">请专家在看不到模型判断的情况下，给一批未用于编写提示词的样本打标签。逐条对照，分别记录裁判漏掉的失败和误报的失败，再检查分歧究竟来自规则含糊、输入缺少上下文，还是裁判忽略了已有证据。若根据这些分歧修改规则或提示词，下一轮确认应使用另一批留出样本。交付物包括判定规则、人工标签、裁判配置和分歧清单，由团队根据漏判与误判的代价决定用在哪些场景。</p>

<p lang="en">Have the expert label a batch that was held out of prompt development, without seeing the model’s judgments. Compare the labels case by case, tally missed failures and false alarms separately, and check whether each disagreement stems from ambiguous wording, missing context, or evidence the judge overlooked. If those cases lead you to revise the rubric or prompt, confirm the revision on a fresh held-out batch. Keep the rubric, human labels, judge configuration, and disagreement log so the team can decide where to use the judge based on the cost of each error.</p>
