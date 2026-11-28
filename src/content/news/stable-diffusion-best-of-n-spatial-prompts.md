---
category: "image"
summaryEn: "In a Stable Diffusion 3.5 Medium preprint, reviewers found a correct image among eight base-model samples for 52% of prompts specifying relative positions. A single sample from the Flow-GRPO checkpoint was correct for 92%."
summaryZh: "一项 Stable Diffusion 3.5 Medium 预印本发现，在要求相对位置的提示词上，人工从 8 张基础模型图里找到正确结果的比例为 52%，Flow-GRPO 检查点单张出图的正确率为 92%。"
tags: ["stable-diffusion", "flow-grpo", "best-of-n", "text-to-image"]
titleEn: "Stable Diffusion study finds eight base samples still trail one RL sample on spatial prompts"
titleZh: "Stable Diffusion 构图对照：有相对位置要求时，基础模型 8 张仍落后于后训练模型 1 张"
editorial: {"score": 82, "tier": "standard", "audience": "core"}
published: "2026-11-28T18:15:41+08:00"
sources: [{"title": "How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models", "url": "https://arxiv.org/abs/2611.33232"}]
---
<p lang="zh-CN">如果提示词要求杯子出现在盘子左边，多生成几张能弥补模型在构图上的差距吗？11 月 26 日发布的一篇 arXiv 预印本用 398 条新的 GenEval 风格提示词，对比了 Stable Diffusion 3.5 Medium 基础模型和经过强化学习后训练的公开 Flow-GRPO 检查点。<a href="https://arxiv.org/abs/2611.33232">预印本摘要</a></p>

<p lang="en">If a prompt asks for a cup to the left of a plate, can generating more images close the gap in spatial accuracy? In an arXiv preprint posted November 26, the authors compared the Stable Diffusion 3.5 Medium base model with its public Flow-GRPO checkpoint, post-trained with reinforcement learning, on 398 new GenEval-style prompts. <a href="https://arxiv.org/abs/2611.33232">Preprint abstract</a></p>

<p lang="zh-CN">在要求相对位置的提示词中，人工从 8 张基础模型图里找到正确结果的比例为 52%，后训练检查点单张出图的正确率为 92%。约五分之四的提示词没有位置要求。在这组提示词上，人工从最多 3 张基础模型图里挑出正确结果的比例，与后训练检查点单张出图的正确率相近。</p>

<p lang="en">For prompts specifying relative positions, human reviewers found a correct result among eight base-model images for 52% of prompts. A single image from the post-trained checkpoint was correct for 92%. Roughly four in five prompts had no position requirement. For those prompts, human reviewers found a correct result among up to three base-model images about as often as one image from the post-trained checkpoint was correct.</p>

<p lang="zh-CN">如果用视觉语言模型自动选图，采样预算要单独估算。在没有位置要求的那组提示词上，从 16 张基础模型图里自动选出一张，表现与后训练检查点单张相近。把全部提示词纳入预先设定的主测试，并要求两套自动评审都判定图像合格时，基础模型的 16 选 1 方案落后 9.3 个百分点。</p>

<p lang="en">If you use a vision-language model to pick images, estimate that sampling budget separately. On prompts without position requirements, automatically picking one of 16 base-model images performed roughly on par with a single image from the post-trained checkpoint. In the prespecified primary test across all prompts, which required both automated judges to pass an image, the base model’s best-of-16 setup trailed by 9.3 percentage points.</p>

<p lang="zh-CN">对本地出图，这组结果可以用来安排试验顺序。只要求对象和属性的提示词，可以先少量采样并人工挑图。左右等相对位置必须准确时，可以优先试后训练检查点，再用自己常用的提示词对照。这些比例来自预印本中的这组检查点和提示词。</p>

<p lang="en">For a local workflow, these results suggest what to try first. If your prompt specifies only objects and attributes, start with a small batch and pick by hand. If relative placement matters, try the post-trained checkpoint first and compare results on prompts you actually use. The reported rates apply to the checkpoints and prompts in the preprint.</p>
