---
category: "models"
summaryEn: "A RoBERTa-large study found sizable few-shot gains on the datasets used to shape the method. The smaller gap on held-out data makes closed-form heads a baseline worth testing on your own labels."
summaryZh: "冻结 RoBERTa-large 后仍可用标注数据拟合分类头。开发集上的小样本优势更明显，留出集比较则提醒团队用自己的数据决定是否值得微调。"
tags: ["text-classification", "roberta", "few-shot-learning"]
titleEn: "A frozen RoBERTa encoder gives small text classifiers another baseline before LoRA"
titleZh: "小样本文本分类在试 LoRA 前，可以先测冻结 RoBERTa 加闭式分类头"
editorial: {"score": 74, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:31:35+08:00"
sources: [{"title": "Fine-Tuning Without Gradients? Closed-Form, LLM-Written Classifiers on a Frozen Encoder", "url": "https://arxiv.org/abs/2611.33972"}]
---
<p lang="zh-CN">冻结 RoBERTa-large，再用标注数据闭式求解分类头，能做到什么程度？Md Nasir Uddin 等人 11 月 25 日提交的预印本报告，在六套留出数据上，这个方案平均领先 LoRA，与全量微调相差不到 0.5 分。不过，这六套数据上的预注册检验均未通过。在 8,192 条标注的比较中，基于提示的微调领先该方案 1.30 分。<a href="https://arxiv.org/abs/2611.33972">arXiv 预印本</a></p>

<p lang="en">How far can a closed-form classifier head take a frozen RoBERTa-large encoder? In a preprint submitted November 25, Md Nasir Uddin and colleagues report that their approach beat LoRA on average across six held-out datasets and came within half a point of full fine-tuning. None of the preregistered tests passed on those six datasets. At 8,192 labels, prompt-based fine-tuning led the approach by 1.30 points. <a href="https://arxiv.org/abs/2611.33972">arXiv preprint</a></p>

<p lang="zh-CN">论文中的大语言模型负责辅助编写分类程序。程序通过填空式提示读取冻结编码器的多个层，用标注数据拟合候选分类头，再通过交叉拟合选择。在参与形成这套方案的 11 套开发数据上，每类只有 16 条标注时，它领先全量微调和 LoRA 约 3.8 到 5.3 分。做工单路由或文本打标时，可以把冻结编码器加闭式分类头列入首轮对比，用自己的留出集判断这项优势能否迁移到实际任务。</p>

<p lang="en">The language model helped write the classifier programs. The programs used fill-in-the-blank prompts to read several layers of the frozen encoder, fitted candidate heads on labeled data, and selected among them by cross-fitting. On the 11 development datasets that helped shape the method, it led full fine-tuning and LoRA by 3.8 to 5.3 points with 16 labels per class. For ticket routing or text labeling, a frozen encoder with a closed-form head is worth including in the first round of baselines. Use a held-out set from your own project to see whether the advantage carries over.</p>
