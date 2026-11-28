---
category: "agents"
summaryEn: "Partial Routing uses past runs to guide which subtasks a lead model hands to a cheaper model. The authors report a higher ViBench score at 19% lower cost and a higher Terminal-Bench 4.0 pass rate at similar cost. A separate test found gains from giving the lead a task breakdown alone."
summaryZh: "Partial Routing 用历史运行记录判断哪些子任务适合交给低成本模型。作者报告，ViBench 得分提高、成本降低 19%，Terminal-Bench 4.0 的通过率在成本相近时提高。仅提供子任务拆解的对照也取得了收益。"
tags: ["model-routing", "agents", "benchmarks"]
titleEn: "Partial Routing uses past runs to decide which subtasks go to cheaper models"
titleZh: "Partial Routing 用历史运行记录决定哪些子任务交给低成本模型"
editorial: {"score": 79, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:32:15+08:00"
sources: [{"title": "Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows", "url": "https://arxiv.org/abs/2611.33402"}]
---
<p lang="zh-CN">11 月 26 日发布的 Partial Routing 预印本提出，让能力较强的主模型在执行中决定哪些子任务交给成本较低的模型。作者从两种模型的历史运行记录中找出反复出现的子任务，衡量各自的完成质量和成本，再把这些结果写成委派指引。主模型据此决定何时委派、委派什么，两种模型都无需重新训练。</p>

<p lang="en">The Partial Routing preprint, posted November 26, proposes letting a more capable lead model decide during a run which subtasks to hand to a cheaper model. The authors identify recurring subtasks in both models’ past runs, measure each model’s quality and cost on those subtasks, and turn the results into delegation guidance. The lead uses that guidance to decide when and what to delegate, with no retraining required for either model.</p>

<p lang="zh-CN">在留出的基准任务上，作者报告，当委派参数 δ 设为 0.75 时，相比主模型独立执行，ViBench 得分从 70.2 升至 78.5，成本降低 19%。Terminal-Bench 4.0 的通过率从 54% 升至 61%，成本相近。这些数字来自预印本摘要所述的两项基准测试。</p>

<p lang="en">On held-out benchmark tasks, the authors report that setting the delegation parameter δ to 0.75 raised the ViBench score from 70.2 to 78.5 while cutting cost by 19% compared with the lead model running alone. On Terminal-Bench 4.0, the pass rate rose from 54% to 61% at a similar cost. These figures cover the two benchmark evaluations described in the preprint abstract.</p>

<p lang="zh-CN">对评估多步骤编码 Agent 的团队，论文还提供了一组实用的对照。作者报告，仅让主模型拿到子任务拆解，两项基准的成本也都下降，Terminal-Bench 4.0 的通过率也有所提高。在同一批留出任务上比较主模型直跑、主模型按拆解执行以及按拆解委派三种方案，就能分别衡量任务拆解的收益和引入第二个模型带来的额外变化。<a href="https://arxiv.org/abs/2611.33402">arXiv 预印本</a></p>

<p lang="en">The paper also offers a useful control for teams evaluating multistep coding agents. The authors report that giving the lead model the subtask breakdown alone reduced costs on both benchmarks and improved the Terminal-Bench 4.0 pass rate. Comparing three setups on the same held-out tasks—a lead model running on its own, a lead model given the breakdown, and a lead model that can delegate—lets teams measure the gains from task decomposition and the additional effect of bringing in a second model. <a href="https://arxiv.org/abs/2611.33402">arXiv preprint</a></p>
