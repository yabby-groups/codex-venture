---
category: "models"
summaryEn: "WorldPhy gives robotics teams 300 tasks for assessing physical plausibility in generated video. Its authors report that 13 world models struggled to satisfy detailed physical constraints consistently across scenarios."
summaryZh: "WorldPhy 用 300 项任务评估机器人生成视频的物理合理性。作者报告，受测的 13 个世界模型难以在不同场景中持续满足细粒度物理约束。"
tags: ["benchmark", "robotics", "world-models"]
titleEn: "WorldPhy tests whether generated robot videos obey physical constraints"
titleZh: "WorldPhy 检验机器人生成视频是否符合物理约束"
published: "2026-11-27T02:33:03+08:00"
sources: [{"title": "WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics", "url": "https://arxiv.org/abs/2611.34130"}]
---
<p lang="zh-CN">Ziyuan Chu、Mingzhi Zheng、Kaiyue Zhang、Jinan Zhang 和 Linchao Zhu 于 2026 年 11 月 25 日向 arXiv 提交 WorldPhy 预印本。基准的 300 项任务各提供一张起始图像和一条任务指令，覆盖不同场景、任务类别、视角和机器人配置。研究人员可以用它检查生成视频中的机器人动作和物体交互是否符合物理约束。</p>

<p lang="en">Ziyuan Chu, Mingzhi Zheng, Kaiyue Zhang, Jinan Zhang, and Linchao Zhu submitted the WorldPhy preprint to arXiv on November 25, 2026. Each of its 300 tasks provides a starting image and an instruction. The tasks span different scenes, task categories, viewpoints, and robot configurations. Researchers can use them to assess whether robot movements and object interactions in generated videos respect physical constraints.</p>

<p lang="zh-CN">作者用超过 1.2 万条人工标注训练 WorldPhyReward，让它在六项物理维度和一项指令遵循维度上给出分数和理由。作者报告，在这组任务中，受测的 13 个世界模型难以在不同场景中持续生成符合细粒度物理约束的视频。对使用生成视频评估机器人任务的团队，这套基准提供了分别检查物理合理性和指令遵循情况的办法。<a href="https://arxiv.org/abs/2611.34130">arXiv 预印本</a></p>

<p lang="en">The authors trained WorldPhyReward on more than 12,000 human annotations to provide scores and explanations across six physics dimensions and one instruction-following dimension. They report that the 13 world models they tested struggled to respect fine-grained physical constraints consistently across scenarios. For teams evaluating generated videos of robot tasks, the benchmark provides a way to assess physical plausibility and instruction following separately. <a href="https://arxiv.org/abs/2611.34130">arXiv preprint</a></p>
