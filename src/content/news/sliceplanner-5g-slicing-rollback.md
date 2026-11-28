---
category: "agents"
summaryEn: "In an over-the-air test, the authors report that SlicePlanner cut latency violations by up to 86% versus static slicing while maintaining comparable cell throughput."
summaryZh: "作者在空口测试中观察到，相较静态切片，SlicePlanner 最多减少 86% 的延迟违约，小区吞吐相近。"
tags: ["o-ran", "5g", "network-slicing"]
titleEn: "SlicePlanner measures 5G performance before keeping a slice change"
titleZh: "SlicePlanner 改完 5G 切片配置，先实测再决定是否保留"
editorial: {"score": 67, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T22:24:29+08:00"
sources: [{"title": "SlicePlanner: Logic-Guided Agentic AI for Online QoS-Aware Network Slicing in Open RAN", "url": "https://arxiv.org/abs/2611.33664"}]
---
<p lang="zh-CN">SlicePlanner 在改动 5G 切片配置后会重新测量现场指标。实测确认改善才保留新配置，有害变更则回滚。Adhwaa Al-Chaab、Ayman Younis 和 Dario Pompili 在 11 月 25 日提交的预印本中描述了这套控制方案。它会先用服务级别协议约束和控制规则筛选候选动作，再根据动作后的测量结果决定是否提交。</p>

<p lang="en">SlicePlanner measures live performance again after changing a 5G slice configuration. It keeps a change when measurements confirm an improvement and rolls it back if it harms performance. Adhwaa Al-Chaab, Ayman Younis, and Dario Pompili describe the controller in a preprint submitted on November 25. It screens proposed actions against service-level agreement constraints and control rules, then uses post-change measurements to decide whether to commit them.</p>

<p lang="zh-CN">作者用 OpenAirInterface、FlexRIC 和商用 Sierra Wireless 5G 设备进行了空口测试。据报告，在该环境下，SlicePlanner 相较静态切片和基于深度强化学习的切片，延迟违约分别最多减少 86% 和 50%，小区吞吐相近。对准备在 O-RAN 实验床试用自动调参的团队，这项研究给出了三个可一起验收的指标：延迟违约、小区吞吐和有害变更能否回滚。</p>

<p lang="en">The authors ran over-the-air tests with OpenAirInterface, FlexRIC, and commercial Sierra Wireless 5G devices. In that setup, they report up to 86% fewer latency violations than with static slicing and up to 50% fewer than with deep reinforcement learning-based slicing, with comparable cell throughput. For teams trying automated tuning on an O-RAN testbed, the study offers three things to check together: latency violations, cell throughput, and whether harmful changes can be rolled back.</p>
