---
category: "video"
summaryEn: "Diffusers 0.43.0 adds Pika H3 Flex, which accepts a first frame, a last frame, or both and generates video with synchronized stereo audio."
summaryZh: "Diffusers 0.43.0 新增 Pika H3 Flex，可用首帧、末帧或两张图共同作为输入，生成带同步立体声音频的视频。"
tags: ["diffusers", "pika-h3-flex", "video-generation", "image-to-video"]
titleEn: "Diffusers adds Pika H3 Flex for video with first- and last-frame inputs"
titleZh: "Diffusers 接入 Pika H3 Flex，支持用首尾帧生成有声视频"
blocks: [{"kind": "notice", "text": {"en": "The six steps refer to the generation process. The release notes describe synchronized stereo audio as part of the video output.", "zh": "六步指生成过程。发布说明将同步立体声音频列为视频的输出之一。"}, "title": {"en": "What the pipeline produces", "zh": "生成步数与输出"}}]
editorial: {"score": 64, "tier": "standard", "audience": "core"}
published: "2026-11-28T10:34:35+08:00"
sources: [{"title": "Diffusers 0.43.0: MiniMax-H3-Image, Pika H3 Flex, P-H3-Image, Kandinsky S2V, and PAN 2", "url": "https://github.com/huggingface/diffusers/releases/tag/v0.43.0"}]
---
<p lang="zh-CN">手上已有开场分镜和结尾产品图的创作者，可以把两张图分别作为首帧和末帧交给 Pika H3 Flex。GitHub 用户 sayakpaul 于 2026 年 11 月 12 日发布的 Diffusers 0.43.0 说明列出，这项新集成可以生成视频和与画面同步的立体声音频。<a href="https://github.com/huggingface/diffusers/releases/tag/v0.43.0">发布说明</a></p>

<p lang="en">Creators with an opening storyboard and a closing product shot can provide them to Pika H3 Flex as the first and last frames. In the Diffusers 0.43.0 notes published on November 12, 2026, GitHub user sayakpaul describes the new integration as generating video with synchronized stereo audio. <a href="https://github.com/huggingface/diffusers/releases/tag/v0.43.0">Release notes</a></p>

<h2><span lang="zh-CN">按手头素材选择输入</span><span lang="en">Choose inputs based on the assets you have</span></h2>

<ul><li><span lang="zh-CN">只有开场图时，把它作为首帧输入。</span><span lang="en">If you have only an opening image, use it as the first-frame input.</span></li><li><span lang="zh-CN">只有收尾图时，把它作为末帧输入。</span><span lang="en">If you have only a closing image, use it as the last-frame input.</span></li><li><span lang="zh-CN">首尾画面都已选定时，同时提供首帧和末帧。</span><span lang="en">If both shots are set, supply both the first and last frames.</span></li><li><span lang="zh-CN">素材是文字描述或多模态参考时，选择对应的模块化工作流。</span><span lang="en">If you have a text description or multimodal references, choose the corresponding modular workflow.</span></li></ul>
