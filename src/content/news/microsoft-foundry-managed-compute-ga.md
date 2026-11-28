---
category: "models"
summaryEn: "Microsoft Foundry’s Managed Compute is generally available for serving open models on dedicated GPUs. Teams can check the hourly price of a single instance in the deployment wizard and try representative prompts in the Playground."
summaryZh: "Microsoft Foundry 的 Managed Compute 正式可用，支持在专用 GPU 上部署开放模型。团队可在部署向导查看单实例小时价，并在 Playground 用代表性提示做初筛。"
tags: ["microsoft-foundry", "managed-compute", "model-serving", "gpu"]
titleEn: "Foundry Managed Compute goes GA with hourly pricing shown for single-instance deployments"
titleZh: "Foundry Managed Compute 正式可用，部署向导可查看单实例小时价"
blocks: [{"kind": "notice", "text": {"en": "Record the model, deployment location, template, context length, serving runtime, GPU configuration, and hourly price shown for one instance. Use those settings to give engineering and procurement a common starting point for the budget review.", "zh": "记录模型、部署位置、模板、上下文长度、服务运行时、GPU 配置和向导显示的单实例小时价，方便工程和采购基于同一套配置评审预算。"}, "title": {"en": "What to capture for the budget review", "zh": "预算评审要记录的配置"}}]
editorial: {"score": 65, "tier": "standard", "audience": "core"}
published: "2026-11-28T10:45:28+08:00"
sources: [{"title": "Serve open models in production with Foundry Managed Compute", "url": "https://devblogs.microsoft.com/foundry/managed-compute-ga"}]
---
<p lang="zh-CN">微软于 2026 年 11 月 20 日宣布 Microsoft Foundry 的 Managed Compute 正式可用。Inference 团队可以在专用 GPU 上部署开放模型，由微软配备 GPU、维护容器并运行推理服务。Manoj Bableshwar 在<a href="https://devblogs.microsoft.com/foundry/managed-compute-ga">微软 Foundry 公告</a>中介绍了美国和欧盟 Data Zone 选项，以及按模型提供的 NVIDIA A100、H100、H200 或 AMD MI300X GPU。</p>

<p lang="en">Microsoft announced general availability of Managed Compute in Microsoft Foundry on November 20, 2026. Inference teams can deploy open models on dedicated GPUs, with Microsoft provisioning the hardware, maintaining containers, and operating the serving runtime. In the <a href="https://devblogs.microsoft.com/foundry/managed-compute-ga">Microsoft Foundry announcement</a>, Manoj Bableshwar describes US and EU Data Zone options and GPU choices that vary by model, including NVIDIA A100, H100, and H200 GPUs and AMD MI300X GPUs.</p>

<p lang="zh-CN">做首轮成本评估时，可在 Foundry 模型目录按部署选项筛选 Managed Compute，选定目标模型后，按所需部署位置和工作负载选择可用模板。模板决定上下文长度、服务运行时和 GPU 配置。先在部署向导里查看一台实例的小时价。部署就绪后，在 Playground 试几条代表性提示，检查输出是否满足应用的基本要求。</p>

<p lang="en">For a first cost estimate, filter the Foundry model catalog by the Managed Compute deployment option. After selecting a model, choose an available template that fits your deployment location and workload. The template sets the context length, serving runtime, and GPU configuration. Check the hourly price for one instance in the deployment wizard. Once the deployment is ready, run a few representative prompts in the Playground to see whether the outputs meet your application’s basic requirements.</p>
