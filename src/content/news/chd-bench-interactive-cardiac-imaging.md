---
category: "models"
summaryEn: "On CHD-Bench, Gemini 4 Argon gained up to 20 percentage points in macro F1 by examining cardiac scans interactively. Scores still varied across the three cohorts."
summaryZh: "CHD-Bench 报告，Gemini 4 Argon 通过交互式阅片获得的宏平均 F1 较静态视图最高提升 20 个百分点，三个队列的得分仍有差距。"
tags: ["chd-bench", "medical-imaging", "vision-language-models", "evaluation"]
titleEn: "CHD-Bench tests whether models can better identify heart defects by exploring scans"
titleZh: "CHD-Bench 对照静态视图与交互式阅片，评估模型识别先心病的能力"
editorial: {"score": 75, "tier": "standard"}
published: "2026-11-27T23:08:32+08:00"
sources: [{"title": "CHD-Bench: Diagnosing Congenital Heart Disease through Interactive Examination", "url": "https://arxiv.org/abs/2611.33775"}]
---
<p lang="zh-CN">Gautham Krishnan P 等人于 2026 年 11 月 25 日提交的 CHD-Bench 预印本，把翻阅扫描切片和旋转三维重建纳入先天性心脏病评测。基准收录三个队列的 247 份 CT 和心脏 MRI 扫描，覆盖 38 种先心病类型。任务采用多标签评估，一份扫描可以对应多个诊断标签。</p>

<p lang="en">In the CHD-Bench preprint submitted on November 25, 2026, Gautham Krishnan P and colleagues made scrolling through scan slices and rotating 3D reconstructions part of a benchmark for congenital heart disease. It covers 247 CT and cardiac MRI scans from three cohorts and spans 38 types of congenital heart disease. The evaluation is multi-label, so a scan can carry more than one diagnosis label.</p>

<p lang="zh-CN">作者介绍的开源 CHD-Harness 在 3D Slicer 中向视觉语言模型提供 22 项工具，并记录诊断结果和支撑判断的视图。作者报告，Gemini 4 Argon 搭配 CHD-Harness 在三个队列上的宏平均 F1 分别为 0.63、0.63 和 0.43。与同一模型仅使用静态视图相比，交互式阅片带来的提升最高为 20 个百分点。</p>

<p lang="en">The authors’ open-source CHD-Harness gives a vision-language model access to 22 tools in 3D Slicer and records its diagnoses and supporting views. The authors report that Gemini 4 Argon with CHD-Harness scored 0.63, 0.63, and 0.43 in macro F1 across the three cohorts. Interactive examination improved the same model’s score by up to 20 percentage points compared with static views.</p>

<p lang="zh-CN">医疗影像评测团队可以借鉴这一对照设计，在同一批扫描上比较同一模型的两种阅片方式，并保留支撑视图供复核。三个队列的得分差异说明分队列报告有助于发现整体分数可能掩盖的落差。这些分数反映预印本所定义的基准任务中的表现，临床部署仍需另行验证。<a href="https://arxiv.org/abs/2611.33775">arXiv 预印本</a></p>

<p lang="en">Imaging evaluation teams can use the same design to compare two ways of examining the same scans with the same model and keep the supporting views for review. The spread in scores shows why reporting by cohort can reveal gaps an aggregate score might hide. The scores describe performance on the preprint’s benchmark task. Clinical deployment would require separate validation. <a href="https://arxiv.org/abs/2611.33775">arXiv preprint</a></p>
