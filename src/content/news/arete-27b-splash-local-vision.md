---
category: "models"
summaryEn: "Duckets’ Arete-27B package gives Mac users two documented ways to try image question answering locally, through Splash CLI or LM Studio. The model card gives no memory or speed figures."
summaryZh: "Duckets 的 Arete-27B 模型包为 Mac 用户提供了两条本地看图问答路径，可用 Splash CLI 启动，或在 LM Studio 中加载。模型卡未给出内存需求和速度数据。"
tags: ["arete-27b", "mlx", "splash", "lm-studio", "vision"]
titleEn: "Arete-27B-Splash brings local image Q&A to Splash CLI and LM Studio"
titleZh: "Arete-27B-Splash 可通过 Splash CLI 和 LM Studio 试用本地看图问答"
blocks: [{"kind": "notice", "text": {"en": "This brief is based on the model card. Memory requirements, inference speed, and image-answer quality on Apple Silicon still need hands-on verification.", "zh": "本文依据模型卡整理。Apple Silicon 上的内存需求、推理速度和看图回答质量仍待实测。"}, "title": {"en": "What still needs testing", "zh": "待实测的项目"}}]
editorial: {"score": 55, "tier": "standard", "audience": "core"}
published: "2026-11-28T08:46:10+08:00"
sources: [{"title": "Duckets/Arete-27B-Splash", "url": "https://huggingface.co/Duckets/Arete-27B-Splash"}, {"title": "Model, dataset or Space card", "url": "https://huggingface.co/Duckets/Arete-27B-Splash/raw/main/README.md"}]
---
<p lang="zh-CN">想在 Mac 上用 Arete-27B 做看图问答，可以从 Duckets 在 Hugging Face 提供的 Arete-27B-Splash 入手。模型卡把 NousResearch/Arete-27B 列为基础模型，并将这个包标为 MLX、图文输入生成文本。<a href="https://huggingface.co/Duckets/Arete-27B-Splash">模型下载页</a></p>

<p lang="en">Mac users who want to try Arete-27B for image question answering can start with Duckets’ Arete-27B-Splash package on Hugging Face. The model card names NousResearch/Arete-27B as the base model and lists MLX and image-text-to-text support. <a href="https://huggingface.co/Duckets/Arete-27B-Splash">Model download page</a></p>

<p lang="zh-CN">如果已经在用 LM Studio，模型卡建议把下载的文件夹放进模型目录，再在加载对话框中选择 Splash 运行时或 MLX 引擎。使用 Splash CLI 时，卡片给出的启动命令是 <code>splash serve --model Duckets/Arete-27B-Splash</code>。卡片标注的语言为英语，许可证为 Apache-2.0。<a href="https://huggingface.co/Duckets/Arete-27B-Splash/raw/main/README.md">上游模型卡</a></p>

<p lang="en">For LM Studio, the card directs users to put the downloaded folder in their models directory and select the Splash runtime or MLX engine in the load dialog. For Splash CLI, it gives the command <code>splash serve --model Duckets/Arete-27B-Splash</code>. The card lists English as the language and Apache-2.0 as the license. <a href="https://huggingface.co/Duckets/Arete-27B-Splash/raw/main/README.md">Upstream model card</a></p>
