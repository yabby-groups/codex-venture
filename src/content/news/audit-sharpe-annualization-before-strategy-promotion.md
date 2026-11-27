---
category: "coding"
summaryEn: "A switch from daily to per-trade returns left a trading system using the same Sharpe annualization factor. Trace the metric through optimization and deployment gates, then rerun validation for the affected strategies."
summaryZh: "回测从日收益改为单笔交易收益后，旧的夏普年化因子抬高了低频策略的得分。沿优化目标和上线门槛追查错误指标，再对受影响的策略重新验证。"
tags: ["backtesting", "sharpe-ratio", "validation"]
titleEn: "Audit Sharpe annualization before promoting a trading strategy"
titleZh: "策略上线前，如何查出夏普比率的年化频率错配"
blocks: [{"kind": "notice", "text": {"en": "Square-root annualization scales a ratio under assumptions about return behavior. If trades overlap, cluster, or are separated by long idle periods, check whether a daily portfolio return series better represents the strategy’s exposure over time.", "zh": "平方根年化依赖对收益行为的假设。如果交易重叠、集中发生，或策略长期空仓，应检查按日计算的组合收益能否更好地反映策略随时间变化的风险敞口。"}, "title": {"en": "Check the annualization assumptions", "zh": "核查年化假设"}}]
type: "workflows"
version: "Mara Zimmerli’s November 27, 2026 retrospective"
verified: "2026-11-27"
status: "current"
tested: false
editorial: {"score": 81, "tier": "standard"}
published: "2026-11-27T22:59:51+08:00"
sources: [{"title": "Promotion-Gate – Wie der Sharpe-Fehler Strategien aufbläst", "url": "https://dev.to/zuckerkurs/promotion-gate-wie-der-sharpe-fehler-strategien-aufblast-1lg2"}]
---
<p lang="zh-CN">维护策略上线门槛时，先从最终得分追溯到输入序列。Mara Zimmerli 在 2026 年 11 月 27 日发表的复盘中写道，她的系统把夏普比率的输入从日收益换成了单笔交易收益，年化因子却保留了 √252。低频策略因此容易得到偏高的分数。同一指标还流向了四个决策环节，导致修正公式后仍要重新检查此前的筛选结果。</p>

<p lang="en">When auditing a strategy’s go-live gate, trace the final score back to its input series. In a retrospective published on November 27, 2026, Mara Zimmerli wrote that her system switched the Sharpe ratio input from daily returns to per-trade returns but kept the √252 annualization factor. This inflated scores for low-frequency strategies. The same metric fed four decision points, so correcting the formula still left earlier selections to review.</p>

<h2><span lang="zh-CN">从指标口径查到策略名单</span><span lang="en">Trace the metric through to the shortlist</span></h2>

<p lang="zh-CN">给每个消费夏普比率的环节记录三项信息：收益按什么单位采样、空仓期如何处理、年化因子从哪里来。如果输入是每年约 252 个交易日的日收益序列，并计入空仓日，常见的缩放因子是 √252。如果确实要按笔度量，Zimmerli 建议检查缩放因子是否对应每年的交易次数。把通过的策略按交易频率分组，看高分是否异常集中在低频组，再回溯这些策略使用的收益口径。</p>

<p lang="en">For each consumer of the Sharpe ratio, record the return sampling unit, how idle periods are handled, and where the annualization factor comes from. For a daily series spanning roughly 252 trading days per year and including days without a position, √252 is a common scaling factor. For a per-trade metric, Zimmerli recommends checking that the scaling factor reflects annual trade frequency. Group passing strategies by trade frequency, look for unusually high scores in the low-frequency group, and trace those strategies back to their return inputs.</p>

<p lang="zh-CN">如果优化目标也用了错误的指标，就先修正目标，再重新运行回测和滚动样本外验证，让候选策略在统一口径下重新接受筛选。复核时保存新旧策略名单、收益序列口径和每个门槛的结果，以便追溯哪些上线决定需要重做。本文依据 Zimmerli 的一手复盘整理，所给摘录支持错配及其传播路径。</p>

<p lang="en">If the optimizer used the faulty metric, correct the objective first, then rerun the backtest and walk-forward validation so candidates are selected on a consistent basis. Keep the old and new shortlists, the return-series definitions, and the outcome at each gate so you can trace which go-live decisions need revisiting. This workflow draws on Zimmerli’s firsthand account, whose supplied excerpt documents the mismatch and how it spread through the system.</p>
