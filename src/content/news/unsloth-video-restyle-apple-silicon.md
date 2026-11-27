---
category: "video"
summaryEn: "Unsloth’s v0.1.922-beta can restyle an entire clip on Apple Silicon Macs. Unsloth estimates GPU memory use at about 31 GiB for q8_0 and 42 GiB for bf16."
summaryZh: "Unsloth v0.1.922-beta 支持在 Apple Silicon Mac 上重绘整段视频。发布方估计 q8_0 约需 31 GiB GPU 内存，bf16 约需 42 GiB。"
tags: ["unsloth", "apple-silicon", "video-restyle"]
titleEn: "Unsloth brings Video Restyle to Apple Silicon Macs"
titleZh: "Unsloth 测试版支持在 Apple Silicon Mac 上重绘整段视频"
blocks: [{"kind": "notice", "text": {"en": "The memory figures are estimates from the release notes. On Apple Silicon, the GPU shares unified memory with the system and other apps, so the Mac’s advertised capacity alone cannot establish how much memory will be available for a render.", "zh": "内存数字是发布说明给出的估计值。Apple Silicon 的 GPU 与系统和其他应用共享统一内存，仅凭 Mac 的标称容量无法判断渲染时有多少内存可用。"}, "title": {"en": "How to read the memory figures", "zh": "如何看内存要求"}}]
editorial: {"score": 65, "tier": "standard", "audience": "core"}
published: "2026-11-28T04:45:33+08:00"
sources: [{"title": "Inkling Mini + Bug fixes", "url": "https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta"}]
---
<p lang="zh-CN">Unsloth 在 2026 年 11 月 20 日发布的 v0.1.922-beta 中，将 Video Restyle 带到了 Apple Silicon Mac。手上已有视频素材的创作者可以用它在本机按新风格重绘整段片段。<a href="https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta">Unsloth 发布说明</a></p>

<p lang="en">Unsloth brought Video Restyle to Apple Silicon Macs in v0.1.922-beta, released November 20, 2026. Creators can use it to re-render an entire existing clip in a new style on their Mac. <a href="https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta">Unsloth release notes</a></p>

<p lang="zh-CN">按 Unsloth 给出的 GPU 内存估计，q8_0 约需 31 GiB，bf16 约需 42 GiB。如果手头机器能留出接近 31 GiB 的可用内存，可以先评估 q8_0。计划用 bf16 时，则按约 42 GiB 估算余量。</p>

<p lang="en">Unsloth estimates GPU memory use at about 31 GiB for q8_0 and 42 GiB for bf16. If your Mac can make close to 31 GiB available, q8_0 is the option to evaluate first. If you plan to use bf16, budget around 42 GiB.</p>
