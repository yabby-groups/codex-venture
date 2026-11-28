---
category: "models"
summaryEn: "A preprint reports that some supervised fine-tuning settings preserved more of a model’s previous capabilities while delivering similar new-task gains. A fixed set of regression cases can help distinguish otherwise comparable checkpoints."
summaryZh: "预印本报告，部分监督微调配置在新任务收益相近的情况下保留了更多旧能力。固定一组旧任务回归题，可以帮助区分新任务得分接近的检查点。"
tags: ["fine-tuning", "sft", "catastrophic-forgetting"]
titleEn: "Similar fine-tuning gains can hide differences in what a model retains"
titleZh: "微调后的新任务得分相近，旧能力保留却可能差很多"
editorial: {"score": 75, "tier": "standard", "audience": "core"}
published: "2026-11-28T22:02:47+08:00"
sources: [{"title": "Tune for Retention, Not Just Gain: SFT Forgets Far Less than You Think", "url": "https://arxiv.org/abs/2611.34579"}]
---
<p lang="zh-CN">挑选语言模型的微调检查点时，新任务上得分接近的配置，对旧能力的影响可能差很多。11 月 26 日 arXiv 收录的一篇 v1 预印本报告，常规监督微调（SFT）的部分配置通过降低学习率、减小批量，取得了相近的新任务收益，同时少损失甚至几乎不损失原有能力。</p>

<p lang="en">Two fine-tuning configurations can score similarly on a new task and leave a language model with very different levels of its previous capabilities. A v1 preprint listed by arXiv on November 26 reports that some standard supervised fine-tuning (SFT) configurations with lower learning rates and smaller batches delivered similar gains on the new task with little or no forgetting.</p>

<p lang="zh-CN">作者按新任务收益和旧能力保留情况共同选参后，常规 SFT 在实验中可以与自蒸馏微调（SDFT）竞争。作者也指出，SDFT 对超参数选择可能更稳健，但挑选能避免灾难性遗忘的配置时，仍需考察旧能力。下一轮微调可以提前留出一组覆盖既有用途的回归题，用同一套题评估各个候选检查点，再从新任务收益相近的配置里挑选旧能力保留得更好的版本。<a href="https://arxiv.org/abs/2611.34579">arXiv 预印本</a></p>

<p lang="en">When the authors selected hyperparameters using both new-task gains and retention, standard SFT could compete with self-distillation fine-tuning (SDFT) in their experiments. They note that SDFT can be more robust to hyperparameter choices, while still requiring a retention check to identify settings that avoid catastrophic forgetting. For a fine-tuning run, set aside regression cases that cover existing use cases, score each candidate checkpoint on the same cases, and use retention to choose among checkpoints with similar new-task gains. <a href="https://arxiv.org/abs/2611.34579">arXiv preprint</a></p>
