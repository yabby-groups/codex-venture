---
titleZh: "mistral.rs 提供本地模型 CLI、服务和 SDK"
titleEn: "mistral.rs provides a local model CLI, server and SDK"
summaryZh: "mistral.rs 是 Rust 推理项目，提供 CLI 与 SDK，可在支持的环境中走 Metal 或 CUDA 等后端。"
summaryEn: "mistral.rs is a Rust inference project with a CLI and SDKs that can use backends such as Metal or CUDA where supported."
published: "2026-11-24T15:00:30+08:00"
category: "open-source"
tags: ["mistral-rs", "inference", "apple-silicon"]
sources:
  - title: "EricLBuehler/mistral.rs repository and documentation"
    url: https://github.com/EricLBuehler/mistral.rs
---
<h2><span lang="zh-CN">项目用途</span><span lang="en">What it does</span></h2>

<p lang="zh-CN">mistral.rs 是 Rust 推理项目，提供 CLI 与 SDK，可在支持的环境中走 Metal 或 CUDA 等后端。</p>

<p lang="en">mistral.rs is a Rust inference project with a CLI and SDKs that can use backends such as Metal or CUDA where supported.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where to use it</span></h2>

<p lang="zh-CN">适合想将模型嵌入应用、或者通过 API 暴露给其他本地进程的开发者。README 记录 0.9.5 已为支持的 Metal 模型默认启用分页注意力并调整内存规划。</p>

<p lang="en">It suits developers who want to embed a model or expose it through an API to other local processes. The README notes that 0.9.5 defaults to paged attention for supported Metal models and changes memory planning.</p>

<h2><span lang="zh-CN">获取与项目状态</span><span lang="en">Getting started and project status</span></h2>

<p lang="zh-CN">按仓库文档选择平台构建和模型。换版本时可查分页注意力升级指南，并以实际模型与上下文检验内存余量。 仓库创建于 2024-02-26，GitHub API 在 11 月 24 日记录的最近推送日期为 2026-11-20（UTC）。许可证为 MIT。</p>

<p lang="en">Choose a platform build and model from the repo docs. When upgrading, consult the paged-attention migration guide and test memory headroom with your model and context length. The repository was created on 2024-02-26. On November 24, the GitHub API reported 2026-11-20 as its latest push date (UTC). The license is MIT.</p>
