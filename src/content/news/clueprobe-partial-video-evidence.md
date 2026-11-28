---
category: "models"
summaryEn: "ClueProbe adds a middle category for video questions with partial evidence. Teams can use it to test whether a model makes tentative inferences when the footage supports them."
summaryZh: "ClueProbe 为视频问答增设“可推测”一档。团队可以据此检查模型能否根据部分线索作出推测，并表达相应的不确定性。"
tags: ["video-language-models", "evaluation", "partial-evidence"]
titleEn: "ClueProbe tests whether video models can reason from partial clues"
titleZh: "ClueProbe 测试视频模型能否根据部分线索作出推测"
editorial: {"score": 83, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:16:12+08:00"
sources: [{"title": "Out of Sight, Not Out of Clues: Can Video LLMs Guess from Partial Evidence?", "url": "https://arxiv.org/abs/2611.34126"}]
---
<p lang="zh-CN">视频漏掉了关键动作时，画面里仍可能留有支持推测的线索。11 月 26 日公布的 ClueProbe v1 预印本将 598 段真实视频中的 1,721 道人工标注问题分为可回答、可推测和不可回答三档。作者也有控制地调整措辞或视觉输入，以区分模型能否看到线索与能否判断线索是否充分。<a href="https://arxiv.org/abs/2611.34126">预印本</a></p>

<p lang="en">A video can miss the decisive action and still contain clues that support a tentative inference. The ClueProbe v1 preprint, announced on November 26, groups 1,721 human-annotated questions from 598 real-world videos into three categories: answerable, guessable, and unanswerable. The authors also vary the wording or visual input under controlled conditions to distinguish whether a model sees the clues from whether it judges them sufficient. <a href="https://arxiv.org/abs/2611.34126">Preprint</a></p>

<p lang="zh-CN">在评估的 10 个视频语言模型中，作者观察到模型很少在只有部分线索时恰当地表达推测。论文中的定向微调实验把恰当推测率从 1.6% 提高到 40.4%。做视频摘要或复核验收时，可以按三档分别评分，检查模型能否陈述可见事实、指出推测依据并表达不确定性，以及在线索缺失时说明无法判断。</p>

<p lang="en">Across the 10 video-language models evaluated, the authors found that models rarely made appropriately tentative inferences from partial clues. In the paper’s targeted fine-tuning experiment, the appropriate-guessing rate rose from 1.6% to 40.4%. Teams testing video summarization or review can score the three cases separately and check whether the model states visible facts, names the clues behind a tentative inference, and says when the footage gives it too little to judge.</p>
