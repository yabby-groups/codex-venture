---
category: "models"
summaryEn: "Liang Song’s preprint proposes per-response proofs that let clients verify inference claims for a closed-weight model API while keeping model weights and internal prompts private."
summaryZh: "Liang Song 的预印本提出为闭源模型 API 的单条回复生成证明，让客户端核验推理声明，同时保护模型权重和内部提示词。"
tags: ["verifiable-inference", "llm-serving", "research"]
titleEn: "FlashProve-Next proposes verifiable proofs for individual LLM API replies"
titleZh: "FlashProve-Next 提议让大模型 API 的每条回复都可核验"
published: "2026-11-27T03:03:38+08:00"
sources: [{"title": "FlashProve-Next: Verifiable Inference for Production LLM APIs", "url": "https://arxiv.org/abs/2611.33741"}]
---
<p lang="zh-CN">调用闭源模型 API 时，客户端拿到一条回复，却难以核验服务端实际使用的模型和数值精度。Liang Song 于 11 月 25 日提交的 FlashProve-Next 预印本提出，让服务端为单条回复生成可验证的证明，同时保留原生浮点推理和随机采样。</p>

<p lang="en">When a closed-weight model API returns a reply, the client has little visibility into which model or numerical precision the provider actually used. In the FlashProve-Next preprint submitted November 25, Liang Song proposes having the provider generate a verifiable proof for each reply while retaining native floating-point inference and random sampling.</p>

<p lang="zh-CN">按作者的设计，证明可隐藏模型权重、内部提示词、推理过程及激活值。作者还报告在 Blackwell 硬件上用五个模型做了校准，所测计算块和数据行均未出现误拒。该结果对应校准样本，生产 API 的端到端开销仍有待验证。</p>

<p lang="en">The proposed proofs are designed to conceal model weights, internal prompts, reasoning traces, and activations. Song also reports zero false rejections among the tested computation blocks and rows in a five-model calibration on Blackwell hardware. That result covers the calibration samples. End-to-end overhead for a production API remains to be established.</p>
