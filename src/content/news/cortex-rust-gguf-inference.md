---
category: "open-source"
summaryEn: "A new Rust inference engine provides a CPU path for local GGUF models. Its documented scope is limited to GGUF v3 with one- and two-dimensional tensors and excludes MoE models."
summaryZh: "新开源的 Rust 推理引擎 Cortex 可在 CPU 上加载本地 GGUF 模型。当前文档列出的范围仅限 GGUF v3 和一维、二维张量，暂不支持 MoE 模型。"
tags: ["rust", "gguf", "local-inference"]
titleEn: "Cortex brings local GGUF inference to Rust on CPU"
titleZh: "开源推理引擎 Cortex 用 Rust 在 CPU 上运行本地 GGUF 模型"
published: "2026-11-27T08:33:19+08:00"
sources: [{"title": "0x00ef-team/cortex-llm", "url": "https://github.com/0x00ef-team/cortex-llm"}]
---
<p lang="zh-CN">新建的 Cortex 仓库提供了一个用 Rust 编写的 LLM 推理引擎。维护者在 README 中给出了从 Rust 代码加载本地 GGUF 模型的示例，并说明 CPU 推理路径无需 GPU。需要在纯 CPU 环境评估本地推理的 Rust 开发者，可以先用手头的模型文件检查格式和架构是否符合要求。<a href="https://github.com/0x00ef-team/cortex-llm">项目仓库</a></p>

<p lang="en">The new Cortex repository provides an LLM inference engine written in Rust. The maintainers’ README shows how to load a local GGUF model from Rust and documents a CPU inference path that runs without a GPU. Rust developers evaluating local inference on CPU-only machines can start by checking whether their model files match the documented format and architecture requirements. <a href="https://github.com/0x00ef-team/cortex-llm">Project repository</a></p>

<p lang="zh-CN">当前文档只列出 GGUF v3 支持，张量限于一维和二维，暂不支持混合专家（MoE）模型。项目代码可在 MIT 与 Apache 2.0 两种许可证中任选其一。</p>

<p lang="en">The current documentation lists support for GGUF v3 only, limits tensors to one or two dimensions, and excludes mixture-of-experts (MoE) models. The project code is available under a choice of MIT or Apache 2.0.</p>
