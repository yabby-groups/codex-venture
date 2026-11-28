---
category: "agents"
summaryEn: "EgoUseBench uses 693 tasks to test computer-use agents under three conditions, from explicit instructions to a live first-person view that can change during execution."
summaryZh: "EgoUseBench 用 693 道任务评测电脑操作 Agent，覆盖明确指令、执行前录像和执行中持续更新的第一人称画面三种条件。"
tags: ["egousebench", "computer-use", "wearables"]
titleEn: "EgoUseBench tests computer-use agents as the wearer’s view changes"
titleZh: "EgoUseBench 测试第一人称视野变化时电脑助手如何应对"
editorial: {"score": 70, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T14:16:01+08:00"
sources: [{"title": "EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts", "url": "https://arxiv.org/abs/2611.34466"}]
---
<p lang="zh-CN">用户在电脑助手执行到一半时换了正在指的物品，助手需要重新判断目标，还可能要重审已经完成的操作。11 月 26 日公告的 EgoUseBench 预印本把这类情境纳入电脑操作 Agent 评测。作者从超过 74 小时的真实第一人称录像中构造了 693 道任务。</p>

<p lang="en">If a user switches the object they’re referring to midway through a task, a computer-use agent needs to update its target and may have to revisit an action it already took. EgoUseBench, introduced in a preprint announced on November 26, brings situations like this into computer-use evaluation. The authors built 693 tasks from more than 74 hours of real-world first-person recordings.</p>

<p lang="zh-CN">基准设置了三种输入条件。第一种只给明确指令，第二种在执行前提供预录的第一人称画面，第三种在执行期间持续提供观察，让用户意图可以随情境变化。这组条件界定了评测设计。现有摘要摘录能确认任务规模和输入方式，模型表现仍待进一步核实。</p>

<p lang="en">The benchmark uses three input settings. One gives explicit instructions only. A second provides prerecorded first-person footage before execution. A third supplies observations throughout execution as the user’s intent evolves. The available abstract excerpt describes the scope and design of the benchmark. Model performance remains to be verified.</p>

<p lang="zh-CN">验收智能眼镜或带摄像头的助手时，可以让用户在执行中途换一个目标，分别记录助手有没有重新确认用户指的是哪件物品，以及有没有判断前一步仍然有效。</p>

<p lang="en">When testing a smart-glasses or camera-enabled assistant, have the user switch targets mid-task. Record whether the assistant checks which object the user now means and whether it reassesses the action it already took.</p>
