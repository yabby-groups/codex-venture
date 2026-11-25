---
category: "models"
summaryEn: "An arXiv preprint gives a condition for stability to carry over from a Koopman latent model to the nonlinear system and tests a controller design across four simulated benchmarks."
summaryZh: "一篇 arXiv 预印本给出 Koopman 潜在模型的稳定性传递到非线性系统的条件，并在四个仿真基准中检验了一种控制器设计。"
tags: ["robotics", "control-theory", "koopman", "preprint"]
titleEn: "Koopman study shows when model stability carries over to robot control"
titleZh: "Koopman 研究给出模型稳定性传递到机器人系统的条件"
published: "2026-11-25T19:50:11+08:00"
sources: [{"title": "Making Koopman Control Guarantees Hold on Robots", "url": "https://arxiv.org/abs/2611.20402"}]
---
<p lang="zh-CN">用 Koopman 模型设计机器人控制器时，设计者可以在近似线性的潜在空间中分析稳定性。控制器运行时，每一步却要重新编码由非线性系统产生的实际状态。Abulikemu Abuduweili 和 Changliu Liu 在 11 月 23 日修订的预印本中给出一个稳定性传递条件：在目标点的嵌入切空间上，潜在模型须与真实闭环动力学达到一阶匹配。作者还推导了近似匹配时的稳定裕度。</p>

<p lang="en">When designing robot controllers with Koopman models, engineers can analyze stability in an approximately linear latent space. During operation, the controller re-encodes the state produced by the nonlinear system at every step. In a preprint revised on November 23, Abulikemu Abuduweili and Changliu Liu give a condition for stability to carry over: the latent model must reproduce the true closed-loop dynamics to first order on the embedding’s tangent space at the target. They also derive a stability margin for approximate matching.</p>

<p lang="zh-CN">作者提出的 Tangent-Invariant Koopman（TIK）方法利用离线状态转移数据估计目标附近的系统动力学，并将一阶匹配纳入模型设计。在四个开环不稳定的仿真基准中，40 个标准 Koopman 控制器都能稳定各自的潜在模型，却在仿真的非线性系统上表现为局部不稳定。40 个 TIK 控制器均实现了局部稳定。</p>

<p lang="en">The authors’ Tangent-Invariant Koopman (TIK) method estimates the system dynamics near the target from offline state transitions and builds first-order matching into the model. Across four simulated benchmarks with open-loop instability, all 40 standard Koopman controllers stabilized their latent models but were locally unstable on the simulated nonlinear systems. All 40 TIK controllers achieved local stability.</p>
