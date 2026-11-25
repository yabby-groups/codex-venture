---
category: "open-source"
summaryEn: "Ollama 0.40.18 drops JetPack 5 support in its llama.cpp update and introduces Metal optimizations for Inkling2 inference."
summaryZh: "Ollama 0.40.18 随 llama.cpp 更新移除 JetPack 5 支持，并加入面向 Inkling2 推理的 Metal 优化。"
tags: ["ollama", "jetpack", "metal"]
titleEn: "Ollama 0.40.18 drops JetPack 5 support and optimizes Inkling2 on Metal"
titleZh: "Ollama 0.40.18 移除 JetPack 5 支持，并优化 Inkling2 的 Metal 推理"
published: "2026-11-25T20:02:48+08:00"
sources: [{"title": "v0.40.18", "url": "https://github.com/ollama/ollama/releases/tag/v0.40.18"}]
---
<p lang="zh-CN">Ollama 于 2026 年 11 月 24 日发布 v0.40.18。发布说明将 JetPack 5 支持的移除列在 @pdevine 提交的 llama.cpp 更新中，该更新将 llama.cpp 升至 b12651。仍依赖 JetPack 5 的部署需要在升级 Ollama 前评估平台兼容性。</p>

<p lang="en">Ollama released v0.40.18 on November 24, 2026. The release notes list the removal of JetPack 5 support in @pdevine’s update to llama.cpp build b12651. Deployments that still rely on JetPack 5 need to account for the compatibility change before upgrading Ollama.</p>

<p lang="zh-CN">同一版本还纳入了 @dhiltgen 针对 Inkling2 的 Metal 优化，涉及解码、预填充和草稿生成轮次。<a href="https://github.com/ollama/ollama/releases/tag/v0.40.18">Ollama 发布说明</a></p>

<p lang="en">The release also includes @dhiltgen’s Metal optimizations for Inkling2, covering decoding, prefill, and draft rounds. <a href="https://github.com/ollama/ollama/releases/tag/v0.40.18">Ollama release notes</a></p>
