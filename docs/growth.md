# 增长运营

VPS scheduler 每六小时调度 `growth-demand`。采集器复用 robots 检查、HTTP 限流、预算和来源退避。HN Ask 与 Codex GitHub Issues 的问题进入私有卷 `growth/opportunities.json`。重合词组只作为近似去重依据。讨论数量和独立域名是需求代理指标。未测的评分维度用 null 保存。

已有 practices 任务核验候选并安排编辑和独立读者审核。发布任务完成后，verify 核对 Cloudflare 版本与页面，再为文章生成 X、Bluesky 和社区审核记录。分发文件按 URL、标题和摘要的内容指纹去重。分发只生成草稿。

每日 VPS 统计完成后写入 `growth/reports`。报告保留 1、7、28 日窗口和来源覆盖，搜索曝光满 100 且 CTR 低于 2% 的页面进入研究清单。运营人员可在私有卷读取报告和候选。现有 GitHub Analytics Actions 负责私有数据仓库中的同步和周月复盘。

编辑基线的版本为 1。旧的私有策略可沿用栏目权重和候选上限。模型只可建议这两个字段，审核阈值由版本化基线定义。策略历史记录证据、观察周期和回退值。

来源 API、使用条件和预算见 [免费采集运营说明](free-collection.md)。
