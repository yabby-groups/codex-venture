---
category: "agents"
summaryEn: "A preprint tested 14 metrics on 805 agent-memory snapshots. None reliably warned of declining performance on held-out tasks, and mean cosine similarity gave a median lead time of zero."
summaryZh: "一项预印本用 805 个 Agent 记忆快照检验了 14 项指标，均未能可靠预警留出任务表现下滑。平均余弦相似度的中位预警提前量为零。"
tags: ["agent-memory", "evaluation", "monitoring"]
titleEn: "Study Finds No Reliable Early Warning in 14 Agent Memory Metrics"
titleZh: "研究检验 14 项 Agent 记忆指标，均未能可靠预警任务表现下滑"
editorial: {"score": 87, "tier": "featured", "audience": "core"}
published: "2026-11-28T17:16:13+08:00"
sources: [{"title": "Semantic Density Does Not Predict Agent-Memory Collapse", "url": "https://arxiv.org/abs/2611.33184"}]
---
<p lang="zh-CN">持续写入文本记忆的 Agent，能否在任务成功率下降前发出告警？11 月 26 日发布的 arXiv 预印本用 13 种记忆方法的 805 个快照检验了 14 项指标。按作者用于判断留出任务表现开始下滑的主要判据，平均两两余弦相似度的中位预警提前量为零，其他指标也未能可靠预警。改用峰值后的检查点衡量下滑时，近邻拥挤度等指标有时更早变化，但预警表现未能稳定超过直接数记忆条目。</p>

<p lang="en">Can an agent that keeps adding to its text memory raise an alarm before its task success rate drops? An arXiv preprint released November 26 tested 14 metrics on 805 snapshots from 13 memory methods. Under the authors’ primary criterion for the onset of a decline on held-out tasks, mean pairwise cosine similarity gave a median lead time of zero, and none of the other metrics gave a reliable early warning. Using the checkpoint after peak accuracy as an alternative marker, measures such as nearest-neighbor crowding sometimes moved earlier, but did not consistently outperform a simple count of memory entries.</p>

<p lang="zh-CN">作者随后把原有分类器直接用于最长 5,000 道制作任务的 PropWorld 实验。分类器将表现稳定的限容记忆库中 56.9% 的检查点误报为异常，在任务成功率降为零后也只识别出 18% 的检查点。维护类似 Agent 时，可以在每个记忆版本上运行同一套留出回归任务，同时记录条目数和相似度，再检查这些指标能否在自己的工作负载上提供提前量。</p>

<p lang="en">The authors then applied their classifiers unchanged to PropWorld runs of up to 5,000 crafting tasks. The classifiers falsely flagged 56.9% of checkpoints from size-limited stores with stable performance and detected only 18% of checkpoints after task success fell to zero. Teams maintaining similar agents can run the same held-out regression tasks at each memory revision, log entry counts and similarity scores, and check whether either signal provides lead time on their own workloads.</p>
