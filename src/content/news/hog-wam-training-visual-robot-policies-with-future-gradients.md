---
category: "models"
summaryEn: "A preprint reports that an auxiliary image-gradient prediction task raised average success from 17% to 24% across four Franka tasks with noisy observations. The auxiliary module is removed at inference."
summaryZh: "预印本报告，在训练时增加图像梯度预测任务后，四项 Franka 任务在带噪观测下的平均成功率从 17% 升至 24%。辅助模块在推理时移除。"
tags: ["robotics", "world-action-models", "visual-robustness", "hog"]
titleEn: "HOG-WAM trains robot policies to handle visual noise without an extra inference module"
titleZh: "HOG-WAM 用训练期梯度预测提升机器人视觉抗噪性"
editorial: {"score": 70, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T13:04:35+08:00"
sources: [{"title": "HOG-WAM: Improving Visual Robustness through Future Gradient Prediction", "url": "https://arxiv.org/abs/2611.34811"}]
---
<p lang="zh-CN">Boxuan Dong、Yupeng Qian、Ying Wu、Heshuai Li、Junhao Tan、Zhenxiong Tan、Weijia Wu 和 Weihao Yu 在 11 月 25 日提交的 HOG-WAM 预印本中，给基于 FastWAM 的机器人策略增加了一项训练任务：从 RGB 特征预测未来演示图像的方向梯度直方图（HOG）。梯度目标直接取自演示图像，负责预测的辅助模块在推理时移除，部署沿用 FastWAM 的 RGB 到动作架构。</p>

<p lang="en">In the HOG-WAM preprint submitted November 25, Boxuan Dong, Yupeng Qian, Ying Wu, Heshuai Li, Junhao Tan, Zhenxiong Tan, Weijia Wu, and Weihao Yu add a training task to a FastWAM-based robot policy. An auxiliary module uses RGB features to predict histograms of oriented gradients (HOG) for future demonstration frames. The targets come directly from the demonstration images. The module is removed at inference, leaving FastWAM’s RGB-to-action architecture in place.</p>

<p lang="zh-CN">作者报告，在四项 Franka 任务中，带噪观测下的平均成功率从 17% 升至 24%，干净观测下从 40% 升至 59%。在 LIBERO Plus 上，整体成功率从 74.49% 升至 75.26%。这些结果来自作者评估，增益随测试场景而异。</p>

<p lang="en">The authors report that average success across four Franka tasks rose from 17% to 24% with noisy observations and from 40% to 59% with clean observations. On LIBERO Plus, overall success rose from 74.49% to 75.26%. The authors’ evaluations show that the size of the gain varies by setting.</p>

<p lang="zh-CN">如果团队要在自己的操作任务中检验这一做法，可以沿用论文的对照思路：固定 RGB 推理架构，比较有无辅助训练目标的策略，并分别记录干净观测、带噪观测和实机任务的成功率。</p>

<p lang="en">Teams testing this idea on their own manipulation tasks can use the paper’s comparison as a starting point. Keep the RGB inference architecture fixed, compare policies trained with and without the auxiliary objective, and report success separately for clean observations, noisy observations, and physical robot tasks.</p>
