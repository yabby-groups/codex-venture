---
category: "image"
summaryEn: "Apple researchers report that allocating the same latent capacity to smaller regions at inference improves local 3D detail. The method gives teams working within a single GPU’s memory budget another reconstruction setup to test."
summaryZh: "苹果研究团队报告，在推理时将相同的潜变量容量分配给更小的区域，可以改善 3D 局部细节。受单卡显存约束的团队可以把分块推理纳入重建对照实验。"
tags: ["3d-reconstruction", "inference", "gpu-memory"]
titleEn: "Apple’s Split-and-Scale reuses a 3D tokenizer across smaller regions to recover fine detail"
titleZh: "苹果 Split-and-Scale 用同一个 3D tokenizer 分块重建局部细节"
editorial: {"score": 65, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T12:15:49+08:00"
sources: [{"title": "Split-and-Scale Latent 3D Representations", "url": "https://machinelearning.apple.com/research/split-scale-latent-3d"}]
---
<p lang="zh-CN">当 3D 重建丢失复杂物体的局部细节时，苹果研究团队提出把同一个预训练 tokenizer 用在更小的空间区域。Dorian Chan、Muhammed Kocabas、Xiaoming Zhao、Oncel Tuzel 和 Jen-Hao Rick Chang 在苹果研究网站标为 2026 年 11 月发表的 NeurIPS 论文中介绍了 Split-and-Scale。论文将 3D 场景表示为坐标的连续函数，让 tokenizer 在推理时对每个小区域使用相同的潜变量容量。<a href="https://machinelearning.apple.com/research/split-scale-latent-3d">苹果研究论文页面</a></p>

<p lang="en">When 3D reconstruction loses fine detail on complex objects, Apple researchers propose applying the same pretrained tokenizer to smaller spatial regions. Dorian Chan, Muhammed Kocabas, Xiaoming Zhao, Oncel Tuzel, and Jen-Hao Rick Chang introduce Split-and-Scale in a NeurIPS paper that Apple’s research site dates to November 2026. The method represents a 3D scene as a continuous function of its coordinates, so the tokenizer can apply the same latent capacity to each smaller region at inference time. <a href="https://machinelearning.apple.com/research/split-scale-latent-3d">Apple research page</a></p>

<p lang="zh-CN">作者报告，在论文所用的连续坐标表示和实验设置下，分块推理的重建质量可与超出单卡显存限制的更大模型相当。对于能按区域运行 tokenizer 的重建管线，可以固定输入和 tokenizer，对照整场景推理与分块推理，分别记录局部几何质量、峰值显存和推理耗时。</p>

<p lang="en">In their experiments with continuous coordinate representations, the authors report reconstruction quality comparable to that of larger models that exceeded single-GPU memory limits. If a reconstruction pipeline can run its tokenizer on individual regions, engineers can hold the input and tokenizer fixed, compare whole-scene and tiled inference, and measure local geometry quality, peak GPU memory, and runtime.</p>
