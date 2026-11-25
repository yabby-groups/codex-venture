---
titleZh: "Rumble-2-Flash 开放多语种语音识别权重"
titleEn: "Rumble-2-Flash releases multilingual speech recognition weights"
summaryZh: "11 月 18 日公布的 Rumble-2-Flash 是一个 5 亿参数的语音识别模型，发布方列出超过 40 种语言。"
summaryEn: "Announced on November 18, Rumble-2-Flash is a 500-million-parameter speech recognition model, with more than 40 languages listed by the publisher."
published: "2026-11-24T14:59:51+08:00"
category: "audio"
tags: ["rumble", "speech-to-text", "transformers"]
sources:
  - title: "Rumble-2-Flash release and benchmark"
    url: https://huggingface.co/blog/rumble-2-flash
verified: "2026-11-24"
resourceIds: ["rumble-2-flash"]
---
<h2><span lang="zh-CN">主要变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 18 日公布的 Rumble-2-Flash 是一个 5 亿参数的语音识别模型，发布方列出超过 40 种语言。</p>

<p lang="en">Announced on November 18, Rumble-2-Flash is a 500-million-parameter speech recognition model, with more than 40 languages listed by the publisher.</p>

<h2><span lang="zh-CN">实际用途</span><span lang="en">Practical use</span></h2>

<p lang="zh-CN">模型采用 Qwen3-ASR 架构，可用于字幕草稿或语音搜索索引。发布方引用的多语种排行榜结果覆盖九种语言。部署前应按自己的语言、背景噪声和专有名词分组评估。</p>

<p lang="en">The Qwen3-ASR architecture can serve subtitle drafting or speech-search indexing. The multilingual leaderboard result cited by the publisher covers nine languages. Evaluate your target languages, background noise and proper names separately.</p>

<h2><span lang="zh-CN">获取与范围</span><span lang="en">Availability and scope</span></h2>

<p lang="zh-CN">权重采用 Apache 2.0 许可。发布文提供 Transformers 示例，并列出 vLLM 支持。长录音和混合语种录音适合纳入验收样本。</p>

<p lang="en">The weights use Apache 2.0. The announcement includes a Transformers example and lists vLLM support. Include long recordings and mixed-language clips in acceptance tests.</p>
