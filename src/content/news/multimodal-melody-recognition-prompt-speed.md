---
category: "audio"
summaryEn: "Seven of 21 multimodal models reliably recognized melodies with labeled examples. Example speed shifted peak performance and titles biased predictions, giving audio evaluators two variables to control."
summaryZh: "21 个多模态模型中，7 个在有标签示例的条件下能可靠识别旋律。示例速度会改变最佳识别表现所在的区间，标题也会影响预测。音频评测可以分别控制这两个变量。"
tags: ["multimodal-models", "audio-evaluation", "melody-recognition"]
titleEn: "Example speed shifts where audio models best recognize melodies"
titleZh: "示例播放速度会改变音频模型最擅长识别旋律的区间"
editorial: {"score": 74, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T22:02:47+08:00"
sources: [{"title": "Psychophysics of Duration Perception in Multimodal Large Language Models", "url": "https://arxiv.org/abs/2611.33176"}]
---
<p lang="zh-CN">同一首曲子换个播放速度，多模态模型的识别成绩也可能跟着提示里的示例速度变动。11 月 26 日的 arXiv 记录列出了这项预印本的 v1。作者把旋律放慢，以人类识别表现为基线评测了 21 个模型。没有带标签的上下文示例时，多数模型无法认出熟悉的旋律。加入示例后，7 个模型能可靠识别，多数达到最佳表现的速度落在人类识别的中位区间内。</p>

<p lang="en">When a melody is played at different speeds, a multimodal model’s best recognition performance can shift with the speed of the examples in its prompt. In a v1 preprint listed by arXiv on November 26, the authors slowed down melodies and tested 21 models against a human baseline. Most models failed to identify familiar melodies without labeled in-context examples. With examples, seven recognized melodies reliably, and most of those seven peaked within the median human recognition band.</p>

<p lang="zh-CN">作者还发现，给出旋律标题会让预测产生偏差。做音乐检索或音频标注评测时，可以先隐藏标题，用同一旋律的多个速度版本测识别率，再固定待识别音频、单独调整示例速度。如果第二步的结果仍发生变化，就可以量出示例速度对这套评测的影响。论文中的结果适用于这项旋律识别任务。<a href="https://arxiv.org/abs/2611.33176">arXiv 预印本</a></p>

<p lang="en">The authors also found that melody titles biased predictions. For a music retrieval or audio labeling evaluation, hide the titles and measure recognition across several speeds of the same melody. Then hold the test clip fixed and vary only the example speed. Any change in that second step measures how sensitive the evaluation is to example speed. The reported results cover this melody recognition task. <a href="https://arxiv.org/abs/2611.33176">arXiv preprint</a></p>
