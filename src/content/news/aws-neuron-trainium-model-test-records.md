---
category: "models"
summaryEn: "AWS Neuron’s Hugging Face dataset records model test targets, component versions, test dates, and reasons for exclusion. Engineers can use those fields to identify records relevant to a planned Trainium trial."
summaryZh: "AWS Neuron 在 Hugging Face 的数据集记录了模型测试目标、组件版本、测试日期和排除理由，方便工程师为 Trainium 试跑查找相关记录。"
tags: ["aws-neuron", "trainium", "hugging-face"]
titleEn: "AWS Neuron dataset lists model test records for Trainium deployment planning"
titleZh: "AWS Neuron 数据集记录模型测试结果，供 Trainium 迁移前查询"
editorial: {"score": 65, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T19:01:59+08:00"
sources: [{"title": "aws-neuron/torch-neuronx-model-support", "url": "https://huggingface.co/datasets/aws-neuron/torch-neuronx-model-support"}]
---
<p lang="zh-CN">评估把 Hugging Face 模型迁到 Trainium 时，可以用 AWS Neuron 的 torch-neuronx-model-support 数据集筛选试跑对象。用 model_id 和 target 查找目标记录，再对照 neuronx_cc、torch_neuronx 等组件版本及 tested_at 测试时间。记录还设有显存峰值字段 hbm_peak_gb，可在有值时参考。</p>

<p lang="en">When evaluating a Hugging Face model for Trainium, platform engineers can use AWS Neuron’s torch-neuronx-model-support dataset to shortlist candidates for a trial run. Look up records by model_id and target, then compare component versions such as neuronx_cc and torch_neuronx and check the tested_at timestamp. The hbm_peak_gb field provides a peak memory figure where populated.</p>

<p lang="zh-CN">预览中的两个 trn2 样例将 LoRA 适配器标为 EXCLUDED，理由是它们需要挂载到基础流水线上。这两条记录说明了对应测试为何排除适配器。查看时应把 result 和 exclusion 一起读。Hugging Face 的完整数据查看器因内存上限只显示预览，可在仓库的 Files 页面查看数据文件。<a href="https://huggingface.co/datasets/aws-neuron/torch-neuronx-model-support">AWS Neuron 数据集</a></p>

<p lang="en">Two trn2 rows in the preview mark LoRA adapters as EXCLUDED because they load on top of a base pipeline. These rows document why the adapters were excluded from those tests. Read result alongside exclusion. Hugging Face’s full viewer hit a memory limit and shows only a preview. The repository’s Files tab lists the dataset files. <a href="https://huggingface.co/datasets/aws-neuron/torch-neuronx-model-support">AWS Neuron dataset</a></p>
