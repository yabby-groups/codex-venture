---
category: "models"
summaryEn: "VisionQ’s top judge matched paper authors on 69% of questions, yet some choices changed when the images were reordered and most accuracy held when the scoring criterion was removed."
summaryZh: "VisionQ 中表现最好的模型有 69% 的答案与原论文作者一致。换序会改变它的部分选择，删掉评分标准后它仍保留大部分准确率。"
tags: ["vision-language-models", "benchmarks", "model-evaluation"]
titleEn: "VisionQ Finds That Reordering Images Can Change a Vision Model’s Verdict"
titleZh: "VisionQ 发现调换图片顺序会改变视觉模型的部分判断"
editorial: {"score": 80, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T12:45:54+08:00"
sources: [{"title": "VisionQ: Benchmarking VLM Judges on Criterion-Specific Comparisons of Computer Vision Method Outputs", "url": "https://arxiv.org/abs/2610.00666"}]
---
<p lang="zh-CN">让视觉模型从几张图里挑出最锐利的一张，可以先把原样图片换个顺序，看看它是否还选同一张。11 月 26 日更新的 VisionQ 预印本用来自 1,409 篇 CVPR 和 ICCV 论文的图像对比构建了盲测选择题，每题只考一个标准，参考答案取自原论文作者认定的最佳结果。<a href="https://arxiv.org/abs/2610.00666">VisionQ 预印本</a></p>

<p lang="en">If a vision model picks the sharpest image from a set, try changing the order and see whether it still picks the same image. The VisionQ preprint, updated on November 26, turns image comparisons from 1,409 CVPR and ICCV papers into blind multiple-choice questions. Each question tests one criterion, and its reference answer comes from the original paper’s authors’ choice of the best result. <a href="https://arxiv.org/abs/2610.00666">VisionQ preprint</a></p>

<p lang="zh-CN">在 21 个受测评审模型中，表现最好的模型有 69% 的答案与原论文作者一致，随机基线为 32%。研究团队发现，省略题目的评分标准后，该模型仍保留了大部分准确率，而调换选项顺序会改变部分答案。把这两项检查分别加进图像评审用例，可以观察选择是否受位置影响，以及评分标准是否会改变判断。稳定性和与论文作者的一致率衡量的是不同表现。</p>

<p lang="en">The strongest of the 21 judges agreed with the original authors on 69% of questions, versus a 32% chance baseline. It retained most of its accuracy when the researchers removed the scoring criterion, and it changed some answers when they reordered the options. Running those two checks separately in an image review workflow can reveal whether position affects the pick and whether stating the criterion changes the judgment. Stability and agreement with the original authors measure different aspects of performance.</p>
