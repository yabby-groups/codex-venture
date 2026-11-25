---
category: "open-source"
summaryEn: "Unsloth’s beta adds LoRA and QLoRA fine-tuning for Inkling 2 Mini and lets users export the result as GGUF for llama.cpp or as merged 16-bit weights."
summaryZh: "Unsloth 测试版支持用 LoRA 或 QLoRA 微调 Inkling 2 Mini，并可将结果导出为供 llama.cpp 使用的 GGUF 或合并后的 16 位权重。"
tags: ["unsloth", "inkling-2-mini", "lora", "qlora", "gguf"]
titleEn: "Unsloth adds Inkling 2 Mini fine-tuning and GGUF export"
titleZh: "Unsloth 加入 Inkling 2 Mini 微调和 GGUF 导出支持"
published: "2026-11-25T19:42:56+08:00"
sources: [{"title": "Inkling finetuning + perf fixes", "url": "https://github.com/unslothai/unsloth/releases/tag/v0.1.924-beta"}]
---
<p lang="zh-CN">Unsloth 在 2026 年 11 月 24 日发布 v0.1.924-beta，为 Inkling 2 Mini 加入 LoRA 和 QLoRA 微调支持，训练范围可覆盖视觉层。按发布说明的测试配置，Mini 可以在 Kaggle 的两张 T4 上训练，单张 15 GB T4 的显存则不足以运行该配置。</p>

<p lang="en">Unsloth released v0.1.924-beta on November 24, 2026, adding LoRA and QLoRA fine-tuning for Inkling 2 Mini, including support for training its vision layers. The release notes report that the Mini training setup fits on two Kaggle T4 GPUs and exceeds the memory available on a single 15 GB T4.</p>

<p lang="zh-CN">微调后的模型可导出为 GGUF 或合并后的 16 位权重。发布说明给出的 Mini 导出示例是一个 17.5 GB 的 Q4_K_M GGUF 文件，可用 llama.cpp 加载。</p>

<p lang="en">Users can export the fine-tuned model as GGUF or merged 16-bit weights. The release notes describe a 17.5 GB Q4_K_M GGUF export of Mini that can run in llama.cpp.</p>
