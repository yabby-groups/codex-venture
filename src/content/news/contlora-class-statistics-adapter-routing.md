---
category: "models"
summaryEn: "CONTLORA uses class statistics to select LoRA adapters without retaining training images or per-example features. In three matched comparisons, its mean final accuracy was within 0.07 percentage points of the baseline that kept those features."
summaryZh: "CONTLORA 用类别统计量选择 LoRA 适配器，训练时无需保留图像或逐样本特征。在三项匹配对照中，其平均最终准确率与保留逐样本特征的方案最多相差 0.07 个百分点。"
tags: ["continual-learning", "lora", "image-classification"]
titleEn: "CONTLORA Routes LoRA Adapters With Class Statistics Instead of Stored Examples"
titleZh: "CONTLORA 用类别统计量选择 LoRA 适配器，省去逐样本特征存储"
editorial: {"score": 69, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T17:16:13+08:00"
sources: [{"title": "The Geometry Is the Memory: Task-Density Routing for Continual LoRA", "url": "https://arxiv.org/abs/2611.33487"}]
---
<p lang="zh-CN">视觉分类器分批学习新类别时，保留旧 LoRA 适配器只是其中一步，推理时还要为新输入选出合适的适配器。11 月 26 日发布的预印本提出 CONTLORA，通过冻结表征上的高斯类别模型选择适配器，再用累积的特征矩构建类平衡岭分类器。作者报告，训练过程无需保留旧图像或逐样本特征向量。</p>

<p lang="en">When an image classifier learns new classes in stages, keeping the older LoRA adapters is only one step. At inference time it still needs to pick the right adapter for each input. A November 26 preprint introduces CONTLORA, which uses Gaussian class models in a frozen representation to select an adapter and accumulated feature moments to construct a class-balanced ridge classifier. The authors report training without retaining old images or per-example feature vectors.</p>

<p lang="zh-CN">论文报告，CONTLORA 在划分为 20 个任务的 CIFAR-100 上达到 88.55% 的准确率，在 CUB-200 上达到 86.99%。三个组件匹配的基准中，它的平均最终准确率与独立训练、保留逐样本特征的对照最多相差 0.07 个百分点。作者的消融还发现，提高正确任务的覆盖率未必能提高分类准确率。评估这种方法时，可以分别测适配器路由和最终分类，观察错误在哪一步出现。</p>

<p lang="en">The paper reports 88.55% accuracy on CIFAR-100 split into 20 tasks and 86.99% on CUB-200. Across three benchmarks with matched components, mean final accuracy differed from an independently trained baseline that retained per-example features by at most 0.07 percentage points. The authors’ ablations also found that better task coverage did not necessarily improve classification. Measuring adapter routing and final classification separately can show where errors arise.</p>
