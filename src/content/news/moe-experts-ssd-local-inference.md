---
titleZh: "技术专题：把 MoE 专家权重放在 SSD 上意味着什么"
titleEn: "What streaming MoE expert weights from SSD changes"
summaryZh: "Hugging Face 11 月 18 日刊载了一项本地推理实验，比较将部分专家权重放在 SSD、内存或显存中的做法。"
summaryEn: "On November 18, Hugging Face published a local inference experiment comparing placement of expert weights on SSD, in RAM and in GPU memory."
published: "2026-11-24T14:59:51+08:00"
category: "open-source"
tags: ["transformers", "moe", "inference"]
sources:
  - title: "Hugging Face: Streaming MoE experts"
    url: https://huggingface.co/blog/moe-expert-streaming
---
<h2><span lang="zh-CN">主要变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">Hugging Face 11 月 18 日刊载了一项本地推理实验，比较将部分专家权重放在 SSD、内存或显存中的做法。</p>

<p lang="en">On November 18, Hugging Face published a local inference experiment comparing placement of expert weights on SSD, in RAM and in GPU memory.</p>

<h2><span lang="zh-CN">实际用途</span><span lang="en">Practical use</span></h2>

<p lang="zh-CN">MoE 每步只启用部分专家。将较少使用的权重留在 SSD 可降低常驻内存，但访问新专家时会增加读取开销。长提示词预填充和逐 token 生成可能呈现不同的瓶颈。</p>

<p lang="en">MoE activates only some experts per step. Leaving less-used weights on SSD reduces resident memory but adds reads when a different expert is needed. Long-prompt prefill and token-by-token generation can hit different bottlenecks.</p>

<h2><span lang="zh-CN">获取与范围</span><span lang="en">Availability and scope</span></h2>

<p lang="zh-CN">原文提供比较方案和实验条件。复现实验时应固定模型、量化、上下文和并发，并分开记录冷启动、预填充和生成。结果依赖具体 SSD、硬件及软件版本。</p>

<p lang="en">The article gives comparisons and experiment conditions. When reproducing them, pin the model, quantization, context and concurrency, then record cold start, prefill and generation separately. Results depend on the SSD, hardware and software versions.</p>
