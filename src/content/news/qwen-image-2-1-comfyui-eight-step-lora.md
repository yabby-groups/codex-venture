---
category: "image"
summaryEn: "jerin8’s LoRA adds an eight-step sampling option for the Qwen-Image 2.1 base checkpoint in ComfyUI. The model card specifies the loader node, adapter strength, sampler, and scheduler."
summaryZh: "jerin8 为 ComfyUI 中的 Qwen-Image 2.1 基础权重提供了一个 8 步采样方案，模型卡给出了加载节点、LoRA 强度、采样器和调度器。"
tags: ["comfyui", "qwen-image", "lora"]
titleEn: "A Qwen-Image 2.1 LoRA brings eight-step sampling to ComfyUI"
titleZh: "Qwen-Image 2.1 第三方 LoRA 提供 ComfyUI 8 步采样配置"
blocks: [{"kind": "notice", "text": {"en": "The model card identifies the license as qwen-research and links to Qwen’s license text. Check those terms before commercial use or redistribution.", "zh": "模型卡将许可标为 qwen-research，并链接到 Qwen 的许可正文。商用或再分发前可查阅原条款。"}, "title": {"en": "License", "zh": "许可"}}]
editorial: {"score": 74, "tier": "standard", "audience": "core"}
published: "2026-11-28T19:01:59+08:00"
sources: [{"title": "jerin8/Qwen-Image-2.1", "url": "https://huggingface.co/jerin8/Qwen-Image-2.1"}, {"title": "Model, dataset or Space card", "url": "https://huggingface.co/jerin8/Qwen-Image-2.1/raw/main/README.md"}]
---
<p lang="zh-CN">jerin8 为已有 Qwen-Image 2.1 工作流的 ComfyUI 用户提供了一个 LoRA。按作者的模型卡，先加载基础版扩散模型 qwen_image_2.1_bf16.safetensors，再用 LoraLoaderModelOnly 挂载适配器，强度设为 1.0。</p>

<p lang="en">jerin8 has published a LoRA for ComfyUI users who already run Qwen-Image 2.1. The model card calls for loading the base diffusion checkpoint, qwen_image_2.1_bf16.safetensors, then attaching the adapter with LoraLoaderModelOnly at strength 1.0.</p>

<p lang="zh-CN">采样器选 Euler，调度器选 Simple，步数设为 8，CFG 设为 1。这组参数可以作为草稿出图的起点。这里的 8 步是模型卡给出的采样设置，实际耗时和画质需要在自己的硬件和工作流上评估。<a href="https://huggingface.co/jerin8/Qwen-Image-2.1/raw/main/README.md">作者模型卡</a></p>

<p lang="en">Use Euler as the sampler and Simple as the scheduler, with 8 steps and CFG 1. These settings give creators a starting point for draft images. The eight-step figure is the sampling setting from the model card. Render time and image quality are best evaluated on the intended hardware and workflow. <a href="https://huggingface.co/jerin8/Qwen-Image-2.1/raw/main/README.md">Author’s model card</a></p>
