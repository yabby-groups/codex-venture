---
category: "models"
summaryEn: "MRFlow releases weights for generating brain MRI volumes from radiology reports. Teams evaluating it as a noncommercial research baseline should account for a gated VAE download and measure report-to-image agreement separately."
summaryZh: "MRFlow 发布从放射科报告生成脑部 MRI 体数据的权重。把它纳入非商业研究基线前，需确认 VAE 下载权限，并单独评估报告与生成影像的一致性。"
tags: ["mrflow", "mri", "medical-imaging"]
titleEn: "MRFlow releases weights for generating 3D brain MRI from radiology reports"
titleZh: "MRFlow 发布权重，可从放射科报告生成三维脑部 MRI"
blocks: [{"kind": "notice", "text": {"en": "Check that you can access the VAE in the gated FLUX.1-schnell repository. The MRFlow card says to accept the repository’s license and sign in to Hugging Face before downloading it.", "zh": "先确认能否取得 FLUX.1-schnell 仓库中的 VAE。按 MRFlow 模型卡的说明，下载前需接受该仓库的许可并登录 Hugging Face。"}, "title": {"en": "A separate download for the VAE", "zh": "VAE 需要单独下载"}}]
editorial: {"score": 71, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T22:45:33+08:00"
sources: [{"title": "teodora-spasojevic-fau/MRFlow", "url": "https://huggingface.co/teodora-spasojevic-fau/MRFlow"}]
---
<p lang="zh-CN">11 月 25 日上线的 MRFlow 权重可用于一个具体的非商业研究原型：以放射科报告为条件，生成三维脑部 MRI 体数据。项目模型卡列出的权重包括去噪器和微调后的 NeuroBERT，两者均采用 CC BY-NC-SA 4.0，带有非商业使用和相同方式共享条件。<a href="https://huggingface.co/teodora-spasojevic-fau/MRFlow">MRFlow 模型卡</a></p>

<p lang="en">The MRFlow weights posted on November 25 give researchers a candidate for a specific noncommercial prototype that generates 3D brain MRI volumes conditioned on radiology reports. The project’s model card lists weights for the denoiser and fine-tuned NeuroBERT, both under CC BY-NC-SA 4.0, which carries noncommercial and share-alike terms. <a href="https://huggingface.co/teodora-spasojevic-fau/MRFlow">MRFlow model card</a></p>

<p lang="zh-CN">模型卡的图像质量评估覆盖 MR-RATE 的 1,000 个测试序列，每种序列与成像平面组合各有 100 个样本，采用 FVD 和 FID 类指标。如果实验关心生成影像能否体现报告所描述的发现，可以另设一致性评估，逐项核对报告中的发现是否出现在生成体数据中。</p>

<p lang="en">The model card’s image-quality evaluation covers 1,000 MR-RATE test series, with 100 per sequence and imaging-plane combination, using FVD and FID metrics. If the research question is whether the generated images reflect the findings described in the report, add a separate evaluation that checks each reported finding against the generated volume.</p>
