---
titleZh: "RoboTrack 用遮挡场景检验机器人点跟踪"
titleEn: "RoboTrack tests robot point tracking through occlusion"
summaryZh: "Ai2 11 月 23 日介绍了 RoboTrack，包括人工标注的基准、合成训练数据和点跟踪模型。"
summaryEn: "On November 23, Ai2 introduced RoboTrack, including a human-annotated benchmark, synthetic training data and point tracking models."
published: "2026-11-24T14:59:51+08:00"
category: "models"
tags: ["robotrack", "robotics", "computer-vision"]
sources:
  - title: "Ai2: RoboTrack project and artifacts"
    url: https://huggingface.co/blog/allenai/robotrack
---
<h2><span lang="zh-CN">主要变化</span><span lang="en">What changed</span></h2>

<p lang="zh-CN">Ai2 11 月 23 日介绍了 RoboTrack，包括人工标注的基准、合成训练数据和点跟踪模型。</p>

<p lang="en">On November 23, Ai2 introduced RoboTrack, including a human-annotated benchmark, synthetic training data and point tracking models.</p>

<h2><span lang="zh-CN">实际用途</span><span lang="en">Practical use</span></h2>

<p lang="zh-CN">给定视频首帧或某一帧中的点，跟踪器估计它之后的位置、遮挡和重现。用于机器人示范数据时，可检查夹爪盖住物体后，轨迹能否在物体重新出现时接续。</p>

<p lang="en">Given a point in a video frame, tracking estimates its later location, occlusion and reappearance. Robotics teams can use it to check whether trajectories recover after a gripper uncovers an object in demonstration footage.</p>

<h2><span lang="zh-CN">获取与范围</span><span lang="en">Availability and scope</span></h2>

<p lang="zh-CN">项目文链接数据、模型、代码和技术报告。基准的 307 段人工标注视频可用于比较视觉跟踪，部署到机器人仍需评估控制回路与现场相机。</p>

<p lang="en">The project post links to data, models, code and the technical report. The 307 annotated videos support visual tracking comparisons. Robot deployment still requires evaluating the control loop and on-site cameras.</p>
