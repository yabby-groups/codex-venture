---
category: "models"
summaryEn: "In a study of 51,240 stories, five models produced more similar narratives from identical prompts than from different prompts with similar meanings. Masking features tied to the prompts barely changed the authors’ convergence measure."
summaryZh: "一项覆盖 51,240 篇故事的研究发现，五个模型收到同一条提示词时，写出的故事比收到语义相近但不同的提示词时更相似。屏蔽与提示内容相关的叙事特征后，趋同指标变化很小。"
tags: ["storyscope", "creative-writing", "model-evaluation"]
titleEn: "Five Models, One Prompt, and More Similar Stories"
titleZh: "同一条提示词发给五个模型，写出的故事更相似"
editorial: {"score": 84, "tier": "standard", "audience": "core"}
published: "2026-11-28T17:31:21+08:00"
sources: [{"title": "Residual Cross-Model Narrative Convergence under Shared Prompts: Auditing Prompt Controls and Narrative Measurement", "url": "https://arxiv.org/abs/2611.34015"}]
---
<p lang="zh-CN">如果一份创作简报同时发给五个模型，收到的五份大纲能提供多少不同的故事走向？一篇 11 月 26 日列入 arXiv 公告的预印本用 StoryScope 语料检验了这个问题。论文作者分析了五个模型根据 10,248 条共同提示词生成的 51,240 篇故事，用七个维度的 213 项叙事特征衡量不同模型写出的故事有多相似。</p>

<p lang="en">If you send one creative brief to five models, how many different story directions will you get back? A preprint listed in arXiv’s November 26 announcements examined that question using the StoryScope corpus. The authors analyzed 51,240 stories that five models generated from 10,248 shared prompts, measuring similarity across 213 narrative features in seven dimensions.</p>

<p lang="zh-CN">作者把同一条提示词生成的故事，与使用不同但语义相近的提示词生成的故事作比较。屏蔽被判定为与提示内容相关的特征后，等权平均残余趋同指数由 0.409 变为 0.406。在这套语料、叙事特征和对照下，屏蔽前后的结果接近。</p>

<p lang="en">The authors compared stories written from identical prompts with stories written from different but semantically similar prompts. After masking features judged relevant to the prompt content, the equally weighted mean Residual Convergence Index moved from 0.409 to 0.406. The two estimates were close for this corpus, feature set, and comparison baseline.</p>

<p lang="zh-CN">创作团队可以做一个小规模对照。先固定简报换模型，再固定一个模型改写简报，每份大纲都按人物动机、冲突推进和结局逐项比较。提案会上就能看到，在这次任务里，换模型和换简报分别带来了哪些新的故事选择。<a href="https://arxiv.org/abs/2611.34015">arXiv 预印本</a></p>

<p lang="en">A writing team can run a small comparison of its own. Keep the brief fixed and switch models, then keep one model fixed and revise the brief. Compare the outlines on character motivation, how the conflict develops, and how it ends. At the pitch meeting, the team can see which new story choices each change produced for that assignment. <a href="https://arxiv.org/abs/2611.34015">arXiv preprint</a></p>
