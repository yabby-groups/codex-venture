---
titleZh: "ComfyUI 0.46 增加视频重构图节点"
titleEn: "ComfyUI 0.46 adds video reframing nodes"
summaryZh: "新版引入 LTX 合作伙伴节点，并让视频拼接以首段的帧率和音频为基准。"
summaryEn: "The release adds LTX partner nodes and makes video concatenation follow the first clip’s frame rate and audio."
published: "2026-11-24T15:01:03+08:00"
category: "video"
tags: ["comfyui", "video-generation"]
sources:
  - title: "ComfyUI v0.46.0 release notes"
    url: https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.46.0
---
<h2><span lang="zh-CN">版本变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">11 月 19 日（北京时间），ComfyUI 发布 v0.46.0。新版引入 LTX 合作伙伴节点，并让视频拼接以首段的帧率和音频为基准。</p>

<p lang="en">ComfyUI published v0.46.0 on November 19 (China Standard Time). The release adds LTX partner nodes and makes video concatenation follow the first clip’s frame rate and audio.</p>

<h2><span lang="zh-CN">适用场景</span><span lang="en">Where it matters</span></h2>

<p lang="zh-CN">同一项目常混用不同生成模型的片段。首段决定拼接基准时，可先把目标帧率的片段放到首位，再检查音轨和画面时长。LTX 新节点覆盖重构图、放大和 SDR 转 HDR。</p>

<p lang="en">A project may mix clips from several generators. With the first clip setting the baseline, put a clip with the desired frame rate first and inspect the output audio and duration. The new LTX nodes cover reframing, upscaling and SDR-to-HDR conversion.</p>

<h2><span lang="zh-CN">获取与验证</span><span lang="en">Availability and validation</span></h2>

<p lang="zh-CN">发布页提供代码与完整变更，此版移除了 DirectML 支持。依赖该后端或合作伙伴节点的旧工作流，应先确认运行环境和节点可用性，再迁移。</p>

<p lang="en">The release page provides the code and full changes. This version removes DirectML support. Check runtime and node availability before migrating workflows that depend on that backend or partner nodes.</p>
