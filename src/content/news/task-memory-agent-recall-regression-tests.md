---
category: "agents"
summaryEn: "A TASK Memory preprint identifies three ways agents misuse retrieved records. Teams can turn those failures into regression tests that score retrieval and final answers separately."
summaryZh: "TASK Memory 预印本梳理了 Agent 取回记忆后仍会出现的三类错误。开发团队可以据此设计回归用例，分别验收检索结果和最终答案。"
tags: ["agent-memory", "evaluation", "activation-steering"]
titleEn: "TASK Memory shows how agents get answers wrong even after finding the right record"
titleZh: "TASK Memory 研究发现，Agent 找到正确记录后仍可能答错"
blocks: [{"kind": "notice", "text": {"en": "TASK requires access to model activations and the ability to apply a removable weight edit. Teams using a hosted API can still use the paper’s three failure cases to test their own memory systems.", "zh": "TASK 需要访问模型激活，并能对权重施加可移除的编辑。使用托管 API 的团队仍可用论文中的三类失败场景测试自己的记忆系统。"}, "title": {"en": "What TASK requires", "zh": "TASK 的接入条件"}}]
editorial: {"score": 85, "tier": "featured", "audience": "core"}
published: "2026-11-28T12:15:49+08:00"
sources: [{"title": "TASK Memory: Beyond Text-Only Memory with Activation Steering and Knowledge Editing against Memory Hallucination", "url": "https://arxiv.org/abs/2611.34762"}]
---
<p lang="zh-CN">Jinkun Zhao 和 Wenjun Wu 于 2026 年 11 月 25 日提交的 TASK Memory 预印本，在五个开放模型上研究了记忆取回后仍然答错的情况。在同一事实的新旧记录都保留的实验中，53% 的回答给出了已被替换的旧值。只统计检索命中率，会漏掉这类回答错误。<a href="https://arxiv.org/abs/2611.34762">arXiv 预印本</a></p>

<p lang="en">In the TASK Memory preprint submitted on November 25, 2026, Jinkun Zhao and Wenjun Wu studied how five open models got answers wrong even after retrieving a memory. When both versions of a revised fact stayed in memory, 53% of answers gave the superseded value. Retrieval hit rate alone would miss those errors. <a href="https://arxiv.org/abs/2611.34762">arXiv preprint</a></p>

<p lang="zh-CN">作者提出的 TASK 把事实内容保留在文本里，用可移除的权重编辑为记忆提供模型内地址，再用一对激活引导向量按查询决定是否采纳这条记忆。作者报告，在预注册、只测试一次的实验中，十个模型与数据集组合里，模型忽略记忆的比例均降至 1.5% 或以下。这个数字对应的是忽略记忆这一类错误。</p>

<p lang="en">TASK keeps the facts in text, uses a removable weight edit to give the memory an address inside the model, and uses a pair of activation steering vectors to decide whether to apply the memory for each query. In a preregistered, single-run evaluation, the authors reported memory-ignoring rates of 1.5% or lower across all ten model–dataset combinations. That figure applies specifically to cases where the model ignored the memory.</p>

<p lang="zh-CN">给客服机器人或个人助手做上线验收时，可以为每条用例分别记录检索结果和最终答案。用一条与模型旧知识冲突的新记录，检查答案是否采纳更新。让两个相似对象同时出现在记录里，检查事实有没有用错对象。保留同一事实的两版记录，再问当前值，检查模型是否选对版本。</p>

<p lang="en">Before shipping memory in a support bot or personal assistant, log both what was retrieved and what the assistant answered. Give it a new record that conflicts with an older fact the model knows and check whether it uses the update. Include records about two similar entities and check that it applies each fact to the right one. Keep two versions of a fact, ask for the current value, and check which version it uses.</p>
