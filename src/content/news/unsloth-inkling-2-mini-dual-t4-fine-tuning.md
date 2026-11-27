---
category: "open-source"
summaryEn: "Unsloth’s maintainers report about 26 seconds per step for Inkling 2 Mini fine-tuning on Kaggle’s free dual-T4 setup. The beta supports GGUF and merged 16-bit export."
summaryZh: "Unsloth 维护者报告，Inkling 2 Mini 可在 Kaggle 免费双 T4 环境中微调，约 26 秒一步。该 beta 支持导出 GGUF 和合并后的 16 位模型。"
tags: ["unsloth", "inkling-2-mini", "fine-tuning", "gguf"]
titleEn: "Unsloth beta supports Inkling 2 Mini fine-tuning on dual T4s and GGUF export"
titleZh: "Unsloth beta 支持用双 T4 微调 Inkling 2 Mini，并导出 GGUF"
editorial: {"score": 76, "tier": "standard", "audience": "core"}
published: "2026-11-28T02:30:58+08:00"
sources: [{"title": "Inkling finetuning + perf fixes", "url": "https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta"}]
---
<p lang="zh-CN">如果手头只有一张 15 GB T4，Unsloth 11 月 25 日的 beta 发布说明给出了一个选卡依据。维护者报告，Inkling 2 Mini 的微调配置能在 Kaggle 的免费双 T4 环境中运行，约 26 秒一步。单张 15 GB T4 装不下该配置。单步耗时可作为同类配置的排期参考。<a href="https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta">官方发布说明</a></p>

<p lang="en">Unsloth’s November 25 beta release notes give anyone with access to a single 15 GB T4 a concrete GPU constraint. The maintainers report that their Inkling 2 Mini fine-tuning setup runs on Kaggle’s free dual-T4 environment at about 26 seconds per step. The setup exceeds the memory of one 15 GB T4. The reported step time offers a planning reference for similar setups. <a href="https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta">Official release notes</a></p>

<p lang="zh-CN">这个 beta 支持用 LoRA 或 QLoRA 微调 Inkling 2 Mini，训练范围可以包括视觉层。开跑前也可以按交付格式筛选方案。训练后的模型可以导出为 GGUF 或合并后的 16 位模型。合并后的 4 位模型仍超出该 beta 的导出范围。</p>

<p lang="en">The beta supports fine-tuning Inkling 2 Mini with LoRA or QLoRA, including the option to train the vision layers. Decide which output you need before starting the run. The fine-tuned model can be exported as GGUF or as a merged 16-bit model. Merged 4-bit export remains outside the beta’s supported formats.</p>
