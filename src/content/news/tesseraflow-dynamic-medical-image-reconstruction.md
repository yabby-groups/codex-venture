---
category: "models"
summaryEn: "TesseraFlow combines low-resolution frame context with full-resolution tiles later in sampling. Its authors report reconstructing about one 256 × 256 frame per second in their experiments."
summaryZh: "TesseraFlow 先利用低分辨率的整帧信息，再在采样后期处理全分辨率分块。预印本作者报告，实验中重建 256 × 256 图像约需每帧一秒。"
tags: ["tesseraflow", "medical-imaging", "image-reconstruction"]
titleEn: "TesseraFlow uses tiled sampling to speed up dynamic medical image reconstruction"
titleZh: "TesseraFlow 用分块采样加快动态医学影像重建"
published: "2026-11-25T07:51:11+08:00"
sources: [{"title": "TesseraFlow: Scalable Video Diffusion for Dynamic Medical Imaging Inverse Problems", "url": "https://arxiv.org/abs/2611.29099"}]
---
<p lang="zh-CN">动态医学影像重建需要从测量数据恢复一系列随时间变化的画面。11 月 24 日公开的 TesseraFlow 预印本把计算量集中到采样后期。编码器每一步读取各帧的低分辨率视图，浅层解码器先在低分辨率下工作，随后转向全分辨率的时空分块。</p>

<p lang="en">Dynamic medical image reconstruction recovers a sequence of frames from measurement data. In the TesseraFlow preprint posted November 24, the authors concentrate higher-resolution computation in later sampling steps. An encoder reads a low-resolution view of each frame at every step, while a shallow decoder starts at low resolution and later switches to full-resolution space-time tiles.</p>

<p lang="zh-CN">配套采样器 ReTile 在每一步随机移动分块网格并重新加噪，将每步计算压到一次网络前向。作者报告，完整方法重建 256 × 256 图像时约每秒一帧，比实验中的分块和潜空间视频先验快 20 至 367 倍。作者还报告，在所测的心脏、脑部和腹部 MRI 以及肺部 CT 任务中，重建质量可达到或超过最佳生成式基线。这些数字来自论文作者的实验。<a href="https://arxiv.org/abs/2611.29099">查看 arXiv 预印本</a></p>

<p lang="en">The accompanying sampler, ReTile, randomly shifts the tile grid and adds noise again at each step, reducing the computation to one network pass per step. The authors report about one reconstructed 256 × 256 frame per second, 20 to 367 times faster than the patch-based and latent video priors in their experiments. They also report reconstruction quality matching or exceeding the best generative baseline on the tested cardiac, brain, and abdominal MRI and lung CT tasks. These figures come from the authors’ experiments. <a href="https://arxiv.org/abs/2611.29099">arXiv preprint</a></p>
