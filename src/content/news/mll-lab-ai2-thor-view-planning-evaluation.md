---
category: "models"
summaryEn: "MLL-Lab’s AI2-THOR model card reports lower P2V and higher V2P scores after viewpoint-planning fine-tuning. The results show why single-step tasks warrant separate scores in active-vision evaluations."
summaryZh: "MLL-Lab 的 AI2-THOR 模型卡显示，视角规划微调后，P2V 分数下降而 V2P 分数上升。做主动视觉评测时，两类单步题值得分别计分。"
tags: ["ai2-thor", "qwen2-5-vl", "active-vision"]
titleEn: "MLL-Lab’s AI2-THOR fine-tune posts mixed single-step results"
titleZh: "MLL-Lab 的 AI2-THOR 视角规划微调让两类单步题一升一降"
editorial: {"score": 71, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T19:01:59+08:00"
sources: [{"title": "MLL-Lab/VGD-Qwen2.5-VL-7B-AI2-THOR", "url": "https://huggingface.co/MLL-Lab/VGD-Qwen2.5-VL-7B-AI2-THOR"}, {"title": "Model, dataset or Space card", "url": "https://huggingface.co/MLL-Lab/VGD-Qwen2.5-VL-7B-AI2-THOR/raw/main/README.md"}]
---
<p lang="zh-CN">MLL-Lab 在 VGD-Qwen2.5-VL-7B-AI2-THOR 的模型卡里报告了两项单步选择题的不同变化。与基础模型 Qwen2.5-VL-7B-Instruct 相比，P2V 成功率从 28.6% 降到 19.8%，V2P 则从 22.2% 升到 30.6%。这组数值来自作者更新后的 AI2-THOR 测试，实验采用 Habitat-Sim 渲染和水平面动作空间。</p>

<p lang="en">MLL-Lab’s model card for VGD-Qwen2.5-VL-7B-AI2-THOR reports two single-step multiple-choice tasks moving in opposite directions. Compared with base Qwen2.5-VL-7B-Instruct, P2V success fell from 28.6% to 19.8%, while V2P rose from 22.2% to 30.6%. The figures come from the authors’ updated AI2-THOR tests, which use Habitat-Sim renders and a horizontal-plane action space.</p>

<p lang="zh-CN">设计主动视觉验收时，可以沿用模型卡的分组方式，把视角规划按参考路径至多两步和超过两步分开，并单列单步题。作者将权重的适用范围限定在特定渲染风格、相机模型和离散动作空间下的模拟视角规划。<a href="https://huggingface.co/MLL-Lab/VGD-Qwen2.5-VL-7B-AI2-THOR/raw/main/README.md">MLL-Lab 模型卡</a></p>

<p lang="en">For an active-vision evaluation, the card offers a way to group viewpoint-planning results by reference paths of up to two actions and paths of more than two, with separate scores for single-step tasks. The authors scope the weights to simulated viewpoint planning with a specific rendering style, camera model, and discrete action space. <a href="https://huggingface.co/MLL-Lab/VGD-Qwen2.5-VL-7B-AI2-THOR/raw/main/README.md">MLL-Lab model card</a></p>
