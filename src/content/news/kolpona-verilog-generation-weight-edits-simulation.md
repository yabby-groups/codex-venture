---
category: "models"
summaryEn: "Kolpona’s authors report 31.7% pass@1 for Qwen3.5-4B on VerilogEval v2, 55.4% after editing 16 neurons, and 77.6% with the full framework, which uses simulation to select designs."
summaryZh: "在 VerilogEval v2 上，Kolpona 作者报告 Qwen3.5-4B 的 pass@1 从 31.7% 升到权重编辑后的 55.4%，加入含仿真筛选的完整框架后达到 77.6%。"
tags: ["verilog", "rtl", "qwen", "model-editing"]
titleEn: "Kolpona lifts Verilog pass@1 from 31.7% to 77.6% with weight edits and simulation"
titleZh: "Kolpona 的 Verilog 生成通过率从 31.7% 升至 77.6%，权重编辑版达到 55.4%"
blocks: [{"kind": "notice", "text": {"en": "The 22.2-point gap between the edited model and the full framework reflects the combined inference workflow. Isolating the contribution of simulation-based selection would require a separate comparison with the candidate-generation process held fixed.", "zh": "权重编辑版与完整框架之间的 22.2 个百分点反映了整套推理流程的增益。要单独估计仿真筛选的贡献，需要固定候选生成流程，再做一组对照。"}, "title": {"en": "What the benchmark isolates", "zh": "这组成绩能拆出哪部分增益"}}]
editorial: {"score": 76, "tier": "standard", "audience": "vertical"}
published: "2026-11-28T21:33:12+08:00"
sources: [{"title": "Kolpona: An Agentic Framework with Gradient-Free Neuron Programming for RTL Generation", "url": "https://arxiv.org/abs/2611.33973"}]
---
<p lang="zh-CN">如果团队已经有 Verilog testbench，评估 RTL 生成时可以先测同一个模型的三种用法。Kolpona 预印本于 11 月 25 日提交。Musa Tur Farazi、Md Nasir Uddin、Soumik Bhattacharjee、Tishna Sabrina 和 Chowdhury Mohammad Rakin Haider 报告，在 VerilogEval v2 上，Qwen3.5-4B 的 pass@1 为 31.7%，编辑 16 个神经元后单独运行模型达到 55.4%，接入完整框架后达到 77.6%。<a href="https://arxiv.org/abs/2611.33973">Kolpona 预印本</a></p>

<p lang="en">If your team already has Verilog testbenches, you can evaluate RTL generation by testing three setups with the same model. In the Kolpona preprint submitted November 25, Musa Tur Farazi, Md Nasir Uddin, Soumik Bhattacharjee, Tishna Sabrina, and Chowdhury Mohammad Rakin Haider report that Qwen3.5-4B scored 31.7% pass@1 on VerilogEval v2. Editing 16 neurons brought the standalone model to 55.4%, and the full framework reached 77.6%. <a href="https://arxiv.org/abs/2611.33973">Kolpona preprint</a></p>

<p lang="zh-CN">Kolpona 无需梯度训练即可修改权重，用新任务上的 testbench 结果判断是否保留每次修改。推理时，能调用工具的 Agent 提出设计，筛选环节根据规范、候选设计和仿真结果，每题交付一个设计。团队可以在同一组自有任务上比较基础模型、仅编辑权重的模型和完整流程，并用相同的 testbench 判分。这样能先量化权重编辑带来的变化，再测加入整套推理流程后的收益。</p>

<p lang="en">Kolpona edits model weights without gradient training and uses testbench results on fresh tasks to decide whether to keep each edit. At inference time, tool-using agents propose designs, and a selection stage uses the specification, candidates, and simulation results to deliver one design per task. To evaluate the approach on your own designs, score the base model, the weight-edited model, and the full workflow on the same tasks with the same testbenches. That measures the effect of weight editing before testing the gain from adding the full inference workflow.</p>
