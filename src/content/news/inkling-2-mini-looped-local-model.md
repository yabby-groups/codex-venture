---
titleZh: "Inkling 2 Mini 循环复用解码层"
titleEn: "Inkling 2 Mini reuses decoder layers in a loop"
summaryZh: "Hugging Face 11 月 20 日介绍了可接收图像和文本、输出文本的 Inkling 2 Mini。模型中间 12 层运行三遍，复用同一份权重。"
summaryEn: "On November 20, Hugging Face introduced Inkling 2 Mini, a text-output model that accepts images and text. Its middle 12 layers run three times with shared weights."
published: "2026-11-24T14:59:51+08:00"
category: "models"
tags: ["inkling", "transformers", "local-llm"]
sources:
  - title: "Hugging Face: Inkling 2 Mini"
    url: https://huggingface.co/blog/inkling2mini
---
<h2><span lang="zh-CN">主要变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">Hugging Face 11 月 20 日介绍了可接收图像和文本、输出文本的 Inkling 2 Mini。模型中间 12 层运行三遍，复用同一份权重。</p>

<p lang="en">On November 20, Hugging Face introduced Inkling 2 Mini, a text-output model that accepts images and text. Its middle 12 layers run three times with shared weights.</p>

<h2><span lang="zh-CN">实际用途</span><span lang="en">Practical use</span></h2>

<p lang="zh-CN">同一组权重多次参与解码，减少了需要存放的独立层。评估本地截图问答或文档助手时，可同时记录显存峰值、首 token 延迟和生成速度。</p>

<p lang="en">Repeating a set of weights reduces the number of distinct layers to store. When evaluating local screenshot Q&A or document assistants, measure peak memory, time to first token and generation speed together.</p>

<h2><span lang="zh-CN">获取与范围</span><span lang="en">Availability and scope</span></h2>

<p lang="zh-CN">发布文提供 Transformers、llama.cpp 和 MLX 的入口。作者给出的最长上下文为 100 万 token，实际可用长度取决于运行时和内存。</p>

<p lang="en">The announcement links to Transformers, llama.cpp and MLX instructions. The authors list a maximum context of one million tokens. Usable length depends on runtime and available memory.</p>
