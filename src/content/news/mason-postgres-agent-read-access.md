---
category: "agents"
summaryEn: "Mason documents controls for which Postgres data to sync and which rows and columns each agent can read. Query logs record the caller and the SQL it sent."
summaryZh: "Mason 可配置哪些 Postgres 数据进入副本，以及每个代理能读哪些行和列。查询日志记录执行者和发送的 SQL。"
tags: ["postgres", "duckdb", "access-control", "query-logging"]
titleEn: "Give an analytics agent row- and column-level read access with Mason"
titleZh: "用 Mason 按行、按列限制分析代理对 Postgres 数据的读取"
blocks: [{"items": [{"en": "Choose which tables and columns to sync, then pick a sync mode that meets your data freshness requirements.", "zh": "先选要同步的表和列，再根据数据时效要求选同步方式。"}, {"en": "Assign accounts to individual agents and verify which rows and columns each account can query.", "zh": "为每个代理分配独立账户，核对各账户实际能查询哪些行和列。"}, {"en": "Check whether the logs let you trace both successful and denied queries back to the agent that sent them.", "zh": "检查日志能否把成功查询和被拒绝的查询都追溯到对应代理。"}], "kind": "takeaways", "title": {"en": "Three decisions before connecting an agent", "zh": "接入代理前的三个决定"}}]
type: "insights"
version: "Mason public documentation and benchmark, 2026-11-27"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 77, "tier": "standard", "audience": "adjacent"}
published: "2026-11-28T02:00:54+08:00"
sources: [{"title": "Show HN: Mason – A lightweight Postgres read-replica, built on columnar storage", "url": "https://masondata.ai/"}]
---
<p lang="zh-CN">如果分析代理只需要看一个地区的订单，可以在接入前分别决定两件事：哪些表和列要从 Postgres 同步出去，以及代理账户能查询副本中的哪些数据。Mason 官网称，它将选定的数据同步到 DuckDB，支持按需、轮询或逻辑复制，并可用角色权限限制各账户可读的表、列和行。官网还称，查询日志会记录执行者、SQL 和耗时。<a href="https://masondata.ai/">Mason 官网</a></p>

<p lang="en">If an analytics agent only needs orders from one region, there are two decisions to make before connecting it. Choose which tables and columns to sync from Postgres, then decide what the agent’s account can query in the replica. Mason says it syncs selected data into DuckDB on demand, by polling, or through logical replication. It documents role-based controls over tables, columns, and rows, plus query logs that record the caller, SQL, and duration. <a href="https://masondata.ai/">Mason website</a></p>

<p lang="zh-CN">项目方公开的性能示例在一千万条记录上按响应码计数。官网给出的结果是 Postgres 主库 15.7 秒，Mason 0.193 秒，约 81 倍差距。这个数字来自官网列明的环境和单条 SQL，接入前可以用自己的查询核对结果一致性、同步延迟和耗时。权限测试也应覆盖明确需要拒绝的行和列。</p>

<p lang="en">The vendor’s published benchmark groups 10 million records by response code and counts them. Mason reports 15.7 seconds on the Postgres primary and 0.193 seconds on Mason, about an 81-fold difference. The figure comes from one SQL query in the environment listed on the site. Before connecting an agent, use representative queries to check result parity, sync lag, and latency. Include rows and columns the account should be denied in the permissions test.</p>
