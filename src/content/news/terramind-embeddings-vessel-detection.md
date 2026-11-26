---
category: "models"
summaryEn: "A Sentinel-1 preprint reports a detection ROC-AUC of 0.95 using compressed TerraMind embeddings. The median localization error was about 300 meters for vessels longer than 100 meters."
summaryZh: "一项基于 Sentinel-1 数据的预印本报告称，使用 TerraMind 压缩嵌入检测船舶的 ROC-AUC 为 0.95。对长度超过 100 米的船舶，定位误差中位数约为 300 米。"
tags: ["terramind", "sentinel-1", "remote-sensing", "research"]
titleEn: "Researchers test compressed TerraMind embeddings for vessel detection"
titleZh: "研究人员用 TerraMind 压缩嵌入测试船舶检测"
published: "2026-11-27T02:45:44+08:00"
sources: [{"title": "Enhancing Maritime Domain Awareness using Latent Space Representations", "url": "https://arxiv.org/abs/2611.34899"}]
---
<p lang="zh-CN">Rikard Vinge 等人在 2026 年 11 月 25 日提交的预印本中，用 TerraMind 生成的压缩嵌入检测、定位和分类船舶。研究针对 Sentinel-1 的合成孔径雷达影像，检验压缩后的数据保留了多少信息，可供下游分析使用。<a href="https://arxiv.org/abs/2611.34899">arXiv 预印本</a></p>

<p lang="en">In a preprint submitted on November 25, 2026, Rikard Vinge and colleagues used compressed TerraMind embeddings to detect, locate, and classify vessels. The study used Sentinel-1 synthetic aperture radar imagery to test how much information the compressed data retained for downstream analysis. <a href="https://arxiv.org/abs/2611.34899">arXiv preprint</a></p>

<p lang="zh-CN">作者报告，船舶检测的 ROC-AUC 为 0.95。对长度超过 100 米的船舶，定位误差中位数约为 300 米。常见船型的 AIS 类型代码分类准确率为 62%，且分类结果与船长高度相关。这些结果为遥感团队评估压缩嵌入能否满足船舶检测、定位和船型分类各自的精度要求提供了参考。</p>

<p lang="en">The authors reported a detection ROC-AUC of 0.95 and a median localization error of about 300 meters for vessels longer than 100 meters. Accuracy for common AIS vessel type codes was 62%, with classification results strongly correlated with vessel length. The results give remote sensing teams separate benchmarks for judging whether compressed embeddings meet their needs for detection, localization, and vessel classification.</p>
