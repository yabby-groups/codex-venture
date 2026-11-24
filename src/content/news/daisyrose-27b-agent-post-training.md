---
titleZh: "DaisyRose-27B 公开长任务强化学习权重"
titleEn: "DaisyRose-27B releases weights trained on long-horizon tasks"
summaryZh: "RadixArk 11 月 18 日发布以 Qwen3.8-27B 为底座的权重，并介绍使用 Miles 进行长任务强化学习的方法。"
summaryEn: "On November 18, RadixArk released weights based on Qwen3.8-27B and described how it used Miles for reinforcement learning on long-horizon tasks."
published: "2026-11-24T14:59:51+08:00"
category: "models"
tags: ["daisyrose", "agent-training", "qwen"]
sources:
  - title: "RadixArk release and evaluation"
    url: https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin
---
<h2><span lang="zh-CN">主要变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">RadixArk 11 月 18 日发布以 Qwen3.8-27B 为底座的权重，并介绍使用 Miles 进行长任务强化学习的方法。</p>

<p lang="en">On November 18, RadixArk released weights based on Qwen3.8-27B and described how it used Miles for reinforcement learning on long-horizon tasks.</p>

<h2><span lang="zh-CN">实际用途</span><span lang="en">Practical use</span></h2>

<p lang="zh-CN">开发者可以在同一套工具、步骤预算和测试仓库上比较底座与新权重。发布方报告 Terminal-Bench 4.1 的 pass@1 从 5.6% 升至 12.0%，并在各项基准中采用 BF16 或 FP8 较高的成绩。</p>

<p lang="en">Developers can compare the base and new weights with the same tools, step budget and test repositories. The publisher reports Terminal-Bench 4.1 pass@1 rising from 5.6% to 12.0%, using the higher BF16 or FP8 result on each benchmark.</p>

<h2><span lang="zh-CN">获取与范围</span><span lang="en">Availability and scope</span></h2>

<p lang="zh-CN">权重按 Apache 2.0 提供，原文链接模型卡和 SGLang 部署说明。训练会话通过摘要跨越多个轨迹，推理上下文仍为 256K token。</p>

<p lang="en">Weights are available under Apache 2.0. The announcement links to the model card and SGLang deployment recipes. Training sessions use summaries across trajectories, while inference context is 256K tokens.</p>
