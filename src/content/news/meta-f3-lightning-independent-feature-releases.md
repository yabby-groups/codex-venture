---
category: "coding"
summaryEn: "Meta’s ads ranking teams can deploy and roll back individual features while retaining shared computation. Meta reports about 3.6× the rollout speed for comparable extraction features, with no increase in infrastructure compute cost."
summaryZh: "Meta 广告排序团队可以逐项上线和回滚特征，同时保留共享计算。据 Meta 报告，可比的抽取特征上线速度约为旧版的 3.6 倍，基础设施计算成本未增加。"
tags: ["meta", "f3-lightning", "feature-serving", "ml-infrastructure"]
titleEn: "Meta’s F3 Lightning lets features ship independently on a shared execution plan"
titleZh: "Meta F3 Lightning 让特征独立上线和回滚，保留共享计算"
blocks: [{"kind": "notice", "text": {"en": "Meta reports that comparable extraction features reached production about 3.6 times as fast as under the previous F3, with no increase in infrastructure compute cost. That figure describes rollout speed for those features.", "zh": "据 Meta 报告，可比的抽取特征上线速度约为旧版 F3 的 3.6 倍，基础设施计算成本没有增加。这个数字衡量的是这类特征的上线速度。"}, "title": {"en": "What Meta measured", "zh": "Meta 的测量口径"}}]
editorial: {"score": 78, "tier": "standard"}
published: "2026-11-27T23:00:13+08:00"
sources: [{"title": "F3 Lightning: How Meta Accelerates Ads ML Features to Production at Scale", "url": "https://engineering.fb.com/2026/11/03/ml-applications/f3-lightning-how-meta-accelerates-ads-ml-features-to-production"}]
---
<p lang="zh-CN">在 Meta 的广告排序系统里，一次请求可能需要计算超过 2 万项特征。旧版 Facebook Feature Framework（F3）把特征合进一张计算图，以便复用中间结果，但整张图也是发布单元，一条无效定义就能卡住整批。Meta 工程博客于 2026 年 11 月 3 日介绍了 F3 Lightning，作者为 Xiaohe Dong、Jonathan He、Jesus Francisco Anaya Gonzalez、Purbesh Sahoo 和 Daniel Wang。</p>

<p lang="en">A single request in Meta’s ads ranking system can require more than 20,000 features. The previous Facebook Feature Framework (F3) merged features into one graph so they could reuse intermediate results. The whole graph also shipped as one unit, so a single invalid definition could block the release. Xiaohe Dong, Jonathan He, Jesus Francisco Anaya Gonzalez, Purbesh Sahoo, and Daniel Wang introduced F3 Lightning on Meta’s engineering blog on November 3, 2026.</p>

<p lang="zh-CN">早期原型按特征发布后，失去了部分共享计算，CPU 用量随之上升。F3 Lightning 让每项特征独立编译、验证、部署和回滚，同时保留统一的执行计划。稳定的计算标识让不同特征可以引用同一项计算，共享内存缓冲区和稠密索引则支持直接按数组下标访问。</p>

<p lang="en">Early per-feature release prototypes lost some shared computation and used more CPU. F3 Lightning lets teams compile, validate, deploy, and roll back each feature independently while retaining one execution plan. Stable computation IDs let different features reference the same computation, and a shared memory buffer and dense index mapping support direct array access.</p>

<p lang="zh-CN">如果你的特征平台也用同一张图执行和发布，可以先检查两件事。一条无效定义会阻塞多少无关特征？回滚一项特征会波及哪些已上线变更？评估拆分效果时，把特征上线耗时和相当请求负载下的服务 CPU 用量放在一起看。<a href="https://engineering.fb.com/2026/11/03/ml-applications/f3-lightning-how-meta-accelerates-ads-ml-features-to-production">Meta 工程博客</a></p>

<p lang="en">If your platform also uses one graph for both execution and releases, check how many unrelated features one invalid definition can block and which live changes a single-feature rollback would affect. When evaluating a change to the release unit, track time to production alongside serving CPU usage under comparable request loads. <a href="https://engineering.fb.com/2026/11/03/ml-applications/f3-lightning-how-meta-accelerates-ads-ml-features-to-production">Meta engineering blog</a></p>
