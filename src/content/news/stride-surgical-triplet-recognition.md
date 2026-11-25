---
category: "models"
summaryEn: "In preprint experiments, adding information from nearby frames reduced false alarms in surgical video recognition by 41% but slowed responses at the start and end of interactions."
summaryZh: "预印本实验显示，引入邻近帧的信息使手术视频识别的误报减少了 41%，但在交互开始或结束时响应更慢。"
tags: ["stride"]
titleEn: "STRIDE cuts false alarms in surgical video recognition using nearby frames"
titleZh: "STRIDE 利用邻近帧减少手术视频识别误报"
published: "2026-11-25T19:50:11+08:00"
sources: [{"title": "A Closed-Form Temporal Readout for Surgical Triplet Recognition", "url": "https://arxiv.org/abs/2611.28240"}]
---
<p lang="zh-CN">Lemar Abdi 等人在 2026 年 11 月 20 日提交的 arXiv 预印本中提出 STRIDE，用于识别手术视频中哪种器械对哪个解剖目标执行了什么动作。STRIDE 对现有识别器在几个固定时间窗口内输出的特征和 logits 取平均，再通过岭回归将这些信息与当前帧的输出结合。回归可在 CPU 上用闭式解拟合。</p>

<p lang="en">In an arXiv preprint submitted on November 20, 2026, Lemar Abdi and colleagues introduced STRIDE to identify which instrument performs which action on which anatomical target in surgical video. STRIDE averages an existing recognizer’s features and logits over several fixed time windows, then uses ridge regression to combine those averages with the current frame’s outputs. The regression has a closed-form solution that can be fitted on a CPU.</p>

<p lang="zh-CN">作者在九种现有识别方法上测试了 STRIDE。在 27 个方法与数据集的组合中，有 24 个组合的三元组平均精度（AP_IVT）有所提升，最大增幅为 7.4 个百分点。作者还报告误报减少了 41%，代价是在交互开始或结束时响应更慢。预印本称，代码将在论文获接收后公开。</p>

<p lang="en">The authors tested STRIDE with nine existing recognition methods. Triplet average precision (AP_IVT) improved in 24 of 27 method–dataset combinations, with a maximum gain of 7.4 percentage points. The authors also reported 41% fewer false alarms, with slower responses when interactions began or ended. The preprint says the code will be released upon acceptance.</p>
