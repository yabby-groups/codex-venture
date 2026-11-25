---
category: "agents"
summaryEn: "In Cerulion’s paired simulation test, Gemini 3.8 Flash succeeded on 73 of 100 starting states with the harness and on 25 with the baseline interface. The results give robotics developers a measure of how tool interfaces can affect performance with the same model."
summaryZh: "Cerulion 的配对仿真测试显示，Gemini 3.8 Flash 在 100 个初始状态中的成功次数从基线接口下的 25 次增至使用 Cerulion 框架时的 73 次。结果为机器人开发者评估工具接口对同一模型表现的影响提供了参考。"
tags: ["cerulion", "libero-pro", "robotics", "benchmarks"]
titleEn: "Cerulion reports higher robotics simulation success with its tool harness"
titleZh: "Cerulion 公布机器人仿真对照结果，工具框架提高任务成功次数"
published: "2026-11-25T19:28:24+08:00"
sources: [{"title": "Show HN: Cerulion – Harness for Robotics, Gemini 3.8 Flash Matches GPT-6 Astra", "url": "https://github.com/cerulion-inc/cerulion"}]
---
<p lang="zh-CN">Cerulion 在项目 README 中公开了一组 LIBERO-PRO 机器人仿真对照结果。项目团队让 16 个模型分别在 Cerulion 框架和一个已发表的三工具接口下运行，每种条件都使用相同的 100 个初始状态，并保持仿真器、运行预算和成功判定规则一致。这样的配对设计让机器人开发者能在同一模型上比较两种工具接口的表现。</p>

<p lang="en">Cerulion published a controlled comparison on the LIBERO-PRO robotics simulation benchmark in its project README. The team ran 16 models through the same 100 starting states under two conditions, using the Cerulion harness or a previously published three-tool interface. Both runs used the same simulator, budget, and success criteria. The paired design lets robotics developers compare how the same model performs with each interface.</p>

<p lang="zh-CN">据项目团队报告，Gemini 3.8 Flash 使用 Cerulion 时在 100 个初始状态中成功了 73 次，使用三工具接口时成功了 25 次。对多重比较进行 Holm 校正后，16 个模型中有 9 个的提升达到统计显著。这些数字的适用范围是该仿真基准及其运行条件。<a href="https://github.com/cerulion-inc/cerulion">项目 README</a></p>

<p lang="en">The team reported that Gemini 3.8 Flash succeeded on 73 of the 100 starting states with Cerulion and on 25 with the three-tool interface. After Holm correction for multiple comparisons, 9 of the 16 models showed statistically significant gains. The figures apply to this simulation benchmark under the reported test conditions. <a href="https://github.com/cerulion-inc/cerulion">Project README</a></p>
