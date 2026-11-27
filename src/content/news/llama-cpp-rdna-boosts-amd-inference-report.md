---
category: "models"
summaryEn: "A devnull.land author reports faster input processing and token generation with an AMD-focused llama.cpp fork. The figures describe a single account with limited setup details."
summaryZh: "devnull.land 作者报告，面向 AMD 的 llama.cpp 分支提高了其本地推理的预填充和生成吞吐量。现有记录只覆盖一次使用体验，配置细节有限。"
tags: ["llama-cpp", "amd", "local-inference"]
titleEn: "A local inference report on AMD finds faster prefill and generation with a llama.cpp fork"
titleZh: "一次 AMD 本地推理记录中，llama.cpp 分支提高了预填充和生成速度"
type: "insights"
version: "llama-cpp-rdna-boosts, November 26, 2026 first-person report"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T14:04:02+08:00"
sources: [{"title": "AMD-specific fork of llama.cpp", "url": "https://devnull.land/amd-specific-llama-cpp"}]
---
<p lang="zh-CN">devnull.land 在 2026 年 11 月 26 日发表了一篇 AMD 本地推理体验，记录了作者试用 llama.cpp 分支 llama-cpp-rdna-boosts 后的两项变化。据作者报告，预填充速度从约 700 提升到 1,300 token/s，生成速度从约 35 提升到 55 token/s。<a href="https://devnull.land/amd-specific-llama-cpp">原文</a></p>

<p lang="en">In a November 26, 2026 post about local inference on AMD hardware, the author of devnull.land reported two changes after trying llama-cpp-rdna-boosts, a fork of llama.cpp. Prefill rose from about 700 to 1,300 tokens per second, and generation rose from about 35 to 55 tokens per second. <a href="https://devnull.land/amd-specific-llama-cpp">Original post</a></p>

<p lang="zh-CN">预填充处理输入，影响生成开始前的等待。生成吞吐量反映输出展开的速度。两项数字回答的是不同问题，实际感受取决于输入和输出各有多长。</p>

<p lang="en">Prefill processes the input and contributes to the wait before generation begins. Generation throughput measures how quickly the output arrives once generation is underway. How much either improvement matters depends on the lengths of the input and output.</p>

<p lang="zh-CN">本批摘录中的数字来自作者自报，精确显卡型号、模型、运行参数和输出质量仍待核实。现有材料只支持描述这一次体验。</p>

<p lang="en">The figures are self-reported. The supplied excerpt leaves the exact GPU, model, runtime settings, and output quality unverified, so the finding applies to this individual account.</p>
