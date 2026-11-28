---
category: "image"
summaryEn: "Images 2.6 brings GIF creation to OpenAI’s image release. The launch example uses a sprite sheet, giving teams a way to check that a mascot stays on brand across frames and that the loop closes smoothly."
summaryZh: "OpenAI 为 Images 2.6 带来 GIF 创作。发布示例用精灵图规划循环动画，制作团队可以逐帧核对吉祥物的品牌细节，再检查首尾衔接。"
tags: ["openai", "images-2-6", "gif", "sprite-sheets"]
titleEn: "OpenAI’s Images 2.6 shows how to plan a looping mascot GIF"
titleZh: "OpenAI 发布 Images 2.6，用精灵图规划吉祥物 GIF 循环"
editorial: {"score": 69, "tier": "standard", "audience": "core"}
published: "2026-11-28T14:04:28+08:00"
sources: [{"title": "Introducing Images 2.6", "url": "https://openai.com/index/introducing-images-2-6"}]
---
<p lang="zh-CN">OpenAI 于 11 月 4 日发布 Images 2.6，覆盖 ChatGPT、Codex 和 API。发布稿把品牌吉祥物动画列为 GIF 的应用场景，并展示了用一张精灵图规划循环动画的思路。精灵图把连续动作的各帧放在同一张图上，方便制作团队逐帧比较。</p>

<p lang="en">OpenAI released Images 2.6 on November 4 across ChatGPT, Codex, and the API. The announcement highlights brand mascot animation as a use for GIFs and shows how to plan a loop with a sprite sheet. A sprite sheet puts the frames of an action on one image so the production team can compare them side by side.</p>

<p lang="zh-CN">给已有吉祥物写动图需求时，可以先把一个动作拆成起始姿势、动作高点和回到起始姿势的几帧，再列出逐帧保留的轮廓、品牌色和标识。验收时连续播放几轮，观察末帧接回首帧时，位置、大小或姿态是否突然跳变。</p>

<p lang="en">For a mascot you already have, brief a single motion in a few frames that cover the starting pose, the peak of the action, and the return. Specify the silhouette, brand colors, and marks that should stay consistent from frame to frame. Play the result several times and check for jumps in position, scale, or pose where the last frame meets the first.</p>

<p lang="zh-CN">API 提供 GPT-Image-2.6 Flare 和 Sunburst。OpenAI 所说的最快约六秒，特指 Flare 在低质量档生成图像的用时。发布稿把 Sunburst 的中、高质量档定位于更重视细节和多轮编辑一致性的任务。<a href="https://openai.com/index/introducing-images-2-6">OpenAI 发布公告</a></p>

<p lang="en">The API offers GPT-Image-2.6 Flare and Sunburst. OpenAI's figure of as little as six seconds applies to still-image generation with Flare at low quality. The announcement positions Sunburst at medium or high quality for work that needs finer detail and greater consistency across edits. <a href="https://openai.com/index/introducing-images-2-6">OpenAI release announcement</a></p>
