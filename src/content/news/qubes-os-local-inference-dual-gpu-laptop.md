---
category: "open-source"
summaryEn: "Gabriele Risso describes a Qubes R4.3 laptop that serves local inference over qrexec, with a dedicated RTX 5080 Laptop GPU for inference and integrated graphics shared among work qubes."
summaryZh: "Gabriele Risso 在一台 Qubes R4.3 笔记本上用 RTX 5080 Laptop GPU 专门运行推理，通过 qrexec 向其他 qube 提供服务，并用集显为日常工作环境提供图形加速。"
tags: ["qubes-os", "local-inference", "gpu-passthrough"]
titleEn: "How a Qubes OS laptop uses two GPUs for local inference and everyday graphics"
titleZh: "一台 Qubes OS 笔记本如何用双 GPU 分担本地推理与图形加速"
type: "stories"
version: "Qubes R4.3 with RTX 5080 Laptop GPU and Arrow Lake integrated graphics"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T22:01:43+08:00"
sources: [{"title": "Local AI Inference on Qubes OS with an Unlocked Blackwell GPU and iGPU SR-IOV [video]", "url": "https://media.ccc.de/v/qubesos26-110899-local-ai-inference-on-q"}]
---
<p lang="zh-CN">Gabriele Risso 在 Qubes OS 会议演讲中介绍了自己使用的一台笔记本。为了让隔离工作环境里的敏感材料留在本机，他把 RTX 5080 Laptop GPU 直通给 Qubes R4.3 上一个专门运行推理的 qube。该环境最初无法初始化显卡，Risso 报告称，关闭集成显卡启动后才完成初始化。</p>

<p lang="en">In a Qubes OS conference talk, Gabriele Risso described a laptop he uses to keep sensitive material from isolated work environments on the machine. He passed an RTX 5080 Laptop GPU through to a dedicated inference qube on Qubes R4.3. The guest initially failed to initialize the card. Risso reported that it initialized after he booted with integrated graphics disabled.</p>

<p lang="zh-CN">显卡初始化后，直通环境中的功耗上限只有 80 W。Risso 将问题追溯到来宾系统缺少的电源管理信息，并在来宾中补齐了这部分信息。他报告称，调整后功耗上限达到 175 W，模型处理输入提示的预填充吞吐量约为每秒 3,700 token。</p>

<p lang="en">Once initialized, the passed-through GPU was still capped at 80 W. Risso traced the problem to power-management information missing from the guest and supplied it there. He reported a 175 W ceiling after the change and roughly 3,700 tokens per second during prefill, when the model processes its input prompt.</p>

<p lang="zh-CN">独显专供推理后，Risso 使用 Arrow Lake 集显的 SR-IOV 虚拟功能为日常工作 qube 提供图形加速。其他 qube 通过 Qubes 的 qrexec 调用推理服务，整个调用留在笔记本上。这些结果来自演讲者报告的单机配置，吞吐数字只覆盖预填充阶段。</p>

<p lang="en">With the discrete GPU dedicated to inference, Risso used SR-IOV virtual functions on the integrated Arrow Lake GPU to provide graphics acceleration to everyday work qubes. Other qubes called the inference service through Qubes’ qrexec, keeping requests on the laptop. The results come from the speaker’s single-machine setup, and the throughput figure covers prefill alone.</p>
