---
category: "models"
summaryEn: "TRIAGE screens embodied models against the platform’s sensor coverage and control deadline before ranking candidates or spending time on fine-tuning."
summaryZh: "TRIAGE 提议先按平台的传感器覆盖和控制时限筛选具身模型，再给通过门槛的候选排序，决定哪些值得微调。"
tags: ["embodied-ai", "robotics", "model-selection"]
titleEn: "TRIAGE screens embodied models for sensor coverage and latency before fine-tuning"
titleZh: "TRIAGE 给具身模型选型设两道门槛：传感器覆盖与端到端延迟"
editorial: {"score": 74, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T17:45:22+08:00"
sources: [{"title": "Triage Before Fine-Tuning: Feasibility-Gated Selection and Monitored Adaptation of Embodied Foundation Models for a Fixed Physical Platform", "url": "https://arxiv.org/abs/2611.33772"}]
---
<p lang="zh-CN">给一台相机和控制周期都已定下来的机器人选模型，TRIAGE 预印本建议先确认传感器能否提供模型所需的信息，再测从输入到输出的端到端延迟。11 月 26 日的 arXiv v1 公告把这两项作为选型门槛。通过后，再用十分钟本地日志做初步探测，按目标任务表现排序，最后监测微调过程并在发布前做闭环验证。</p>

<p lang="en">When selecting a model for a robot with fixed cameras and a fixed control cycle, the TRIAGE preprint proposes checking whether the sensors provide the inputs the model needs and measuring end-to-end latency. The November 26 arXiv v1 announcement treats both checks as prerequisites. The authors then propose probing eligible models with ten minutes of local logs, ranking them by performance relevant to the target task, monitoring fine-tuning, and validating the result in closed loop before release.</p>

<p lang="zh-CN">作者报告，在论文所用的驾驶基准上，相同像素预算下，缩窄视场引发的规划变化幅度为降低分辨率时的 2.2 至 5.7 倍。团队可以据此把视场覆盖、端到端控制时限和闭环验收结果写进选型表，再决定在哪些候选上投入微调预算。<a href="https://arxiv.org/abs/2611.33772">论文摘要</a></p>

<p lang="en">In the driving benchmarks used in the study, the authors report that narrowing the field of view changed plans 2.2 to 5.7 times as much as reducing resolution at the same pixel budget. Teams can record field-of-view coverage, the end-to-end control deadline, and closed-loop acceptance results together when deciding where to spend their fine-tuning budget. <a href="https://arxiv.org/abs/2611.33772">Paper abstract</a></p>
