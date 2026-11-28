---
category: "models"
summaryEn: "Apple’s Depth Pro 2 research team released code and weights for estimating per-pixel depth in meters at native resolution. Compositors can try it as a source for foreground and background mattes on existing footage."
summaryZh: "苹果 Depth Pro 2 研究团队公开了代码和权重，可按原始分辨率估计逐像素深度并以米为单位输出。后期团队可用现有素材评估它生成前后景遮罩的效果。"
tags: ["apple", "depth-pro-2", "monocular-depth", "compositing"]
titleEn: "Apple releases Depth Pro 2 code and weights for full-resolution video depth"
titleZh: "苹果公开 Depth Pro 2 代码和权重，可按原始分辨率估计视频深度"
blocks: [{"kind": "notice", "text": {"en": "For a depth-based matte, try a short clip with a moving subject. Check whether the mask spills across the subject’s outline, then watch consecutive frames for jumps in the foreground–background boundary.", "zh": "评估深度遮罩时，可以选一段主体在移动的短片。先看遮罩是否溢出主体轮廓，再连看多帧，观察前后景分界是否跳动。"}, "title": {"en": "Two checks for your footage", "zh": "实拍素材的两项检查"}}]
editorial: {"score": 74, "tier": "standard", "audience": "core"}
published: "2026-11-28T10:45:28+08:00"
sources: [{"title": "Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth", "url": "https://machinelearning.apple.com/research/depth-pro-2-monocular"}]
---
<p lang="zh-CN">要给普通相机拍摄的片段制作深度遮罩，可以先用逐像素深度图划分前后景。苹果研究团队在 2026 年 11 月发表的 Depth Pro 2 论文介绍了一套可处理单张照片、视频和实时相机画面的网络。它按输入的原始分辨率输出深度图，以米为单位估计每个像素对应的距离。作者已公开代码和模型权重，入口见<a href="https://machinelearning.apple.com/research/depth-pro-2-monocular">苹果研究页面</a>。</p>

<p lang="en">A per-pixel depth map can help separate foreground and background when making a matte from ordinary camera footage. In a November 2026 paper, Apple researchers introduced Depth Pro 2, a network that handles still images, video, and live camera feeds. It outputs depth maps at the input’s native resolution and estimates each pixel’s distance in meters. The authors released code and model weights through the <a href="https://machinelearning.apple.com/research/depth-pro-2-monocular">Apple research page</a>.</p>

<p lang="zh-CN">论文作者 Peiyun Hu 等人指出，单帧方法往往保留更清晰的物体边缘，多帧方法则更容易维持帧间稳定。他们用同一个网络处理照片和视频，并在论文评估中报告了轮廓清晰度和时间一致性两方面的改善。合成时，可把以米为单位的单目估计值作为调整遮罩阈值的起点，再用自己的素材检查边缘和帧间表现。</p>

<p lang="en">Paper authors Peiyun Hu and colleagues note that single-frame methods tend to preserve sharper object edges, while multi-frame methods tend to produce steadier results over time. They use the same network for images and video and report improvements in both edge sharpness and temporal consistency in their evaluation. For compositing, use the estimated distances in meters as a starting point for tuning the matte threshold, then check edges and frame-to-frame behavior on your own footage.</p>
