---
titleZh: "TensorRT-LLM 1.3 预览支持 Rubin"
titleEn: "TensorRT-LLM 1.3 previews Rubin support"
summaryZh: "NVIDIA 新版推理运行时扩展了多种模型的硬件支持，并为部分 Mamba 混合模型加入前缀缓存。"
summaryEn: "NVIDIA’s inference runtime expands hardware support for several models and adds prefix caching for some hybrid Mamba models."
published: "2026-11-24T15:01:03+08:00"
category: "open-source"
tags: ["tensorrt-llm", "inference", "quantization"]
sources:
  - title: "TensorRT-LLM v1.3.0 release notes"
    url: https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 20 日（北京时间），TensorRT-LLM 发布 v1.3.0。NVIDIA 新版推理运行时扩展了多种模型的硬件支持，并为部分 Mamba 混合模型加入前缀缓存。</p>

<p lang="en">TensorRT-LLM published v1.3.0 on November 20 (China Standard Time). NVIDIA’s inference runtime expands hardware support for several models and adds prefix caching for some hybrid Mamba models.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">部署者需要按模型和 GPU 检查支持矩阵。比如 Qwen3.5 的 NVFP4 支持列于 Blackwell，Kimi K3 的部分并行配置需要 GB300 级别的显存。对重复系统提示词的服务，可在目标硬件上检查缓存命中及首 token 延迟。</p>

<p lang="en">Check the support matrix by model and GPU. For example, Qwen3.5 NVFP4 support is listed for Blackwell, and one Kimi K3 parallel configuration requires GB300-class GPU memory. Services with repeated system prompts can measure cache hits and time to first token on their target hardware.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">安装入口和已知限制见版本页。Rubin 仍处于预览阶段，生产升级前应在实际上下文长度和并发量下测试。</p>

<p lang="en">See the release page for installation and known limitations. Rubin remains in preview. Test with production context lengths and concurrency before upgrading.</p>
