---
category: "models"
summaryEn: "The GeoCAM preprint uses GPS-derived overlap as a training signal. Its authors report better sonar–photo retrieval on the BenthiCat SSS-CAM dataset without manually labeling seabed scenes."
summaryZh: "GeoCAM 预印本以 GPS 数据估算的覆盖重叠为训练信号。作者报告，在无需人工标注海底场景的情况下，该方法改善了 BenthiCat SSS-CAM 数据集上的声呐与照片检索。"
tags: ["geocam", "self-supervised-learning", "sonar"]
titleEn: "GeoCAM uses geographic overlap to match sonar images with underwater photos"
titleZh: "GeoCAM 利用地理覆盖重叠匹配声呐图像与水下照片"
published: "2026-11-26T23:34:19+08:00"
sources: [{"title": "GeoCAM: Self-Supervised Sonar-Optical Representation Learning via Geographic Overlap Supervision", "url": "https://arxiv.org/abs/2611.34218"}]
---
<p lang="zh-CN">Fadi Abdeladhim Zidi、Andrea De Salve、Giuseppe Celeste、Abdellah Zakaria Sellam、Paolo Spagnolo 和 Cosimo Distante 于 2026 年 11 月 25 日向 arXiv 提交了 GeoCAM 预印本。论文处理的是海底调查中的配对问题：同一个侧扫声呐图块可能对应多张水下照片，研究者希望利用这些对应关系学习两类影像的共同表示。</p>

<p lang="en">Fadi Abdeladhim Zidi, Andrea De Salve, Giuseppe Celeste, Abdellah Zakaria Sellam, Paolo Spagnolo, and Cosimo Distante submitted the GeoCAM preprint to arXiv on November 25, 2026. The paper tackles a pairing problem in seabed surveys. A single side-scan sonar tile can correspond to several underwater photos, and the authors use those relationships to learn a shared representation for both types of imagery.</p>

<p lang="zh-CN">GeoCAM 先汇总同一声呐图块对应的多张照片，再根据 GPS 数据估算的覆盖范围重叠程度，为声呐与照片的配对分配不同的训练权重。训练依赖地理元数据，无需人工标注海底场景类别。作者报告，在 BenthiCat SSS-CAM 数据集上，与论文采用的对比学习基线相比，GeoCAM 改善了跨模态检索和对齐，有助于找出记录同一片海底的声呐图块与照片。</p>

<p lang="en">GeoCAM aggregates the photos associated with a sonar tile, then assigns training weights to sonar–photo pairs based on how much their GPS-derived footprints overlap. Training relies on geographic metadata and requires no manual seabed scene labels. On the BenthiCat SSS-CAM dataset, the authors report improved cross-modal retrieval and alignment over their contrastive learning baselines, helping match sonar tiles and photos that cover the same patch of seabed.</p>
