---
category: "coding"
summaryEn: "Use SelfHostCost’s JSON snapshot to shortlist orderable plans and compare renewal prices and prepayment terms. Its Atom feed flags verified price changes for follow-up."
summaryZh: "用 SelfHostCost 的 JSON 快照筛选可下单的托管方案，比较续费价格与预付条件，再通过 Atom feed 跟踪已核实的价格变动。"
tags: ["n8n", "self-hosting", "atom", "pricing"]
titleEn: "Track n8n hosting prices with a dated JSON snapshot and an Atom feed"
titleZh: "用带日期的 JSON 快照和 Atom feed 跟踪 n8n 托管价格"
blocks: [{"kind": "notice", "text": {"en": "SelfHostCost says it read the JSON snapshot on November 25, 2026, and that the hosting rows in that snapshot were checked on November 24. Use each row’s `checked` date when assessing a newer snapshot.", "zh": "SelfHostCost 称其于 2026 年 11 月 25 日读取 JSON 快照，其中托管商条目的核查日期为 11 月 24 日。查看后续快照时，以各条目的 `checked` 日期判断信息是否仍然适用。"}, "title": {"en": "Snapshot dates", "zh": "快照日期"}}]
type: "workflows"
version: "SelfHostCost documentation and snapshot described on 2026-11-26"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T14:03:50+08:00"
sources: [{"title": "Track n8n hosting prices from a dated JSON file and an Atom feed, not pricing pages", "url": "https://dev.to/selfhostcost/track-n8n-hosting-prices-from-a-dated-json-file-and-an-atom-feed-not-pricing-pages-2282"}]
---
<p lang="zh-CN">筛选 n8n 托管方案时，先看方案能否下单，再比较首期和续费支出。独立价格追踪器 SelfHostCost 在其发布说明中介绍了两种公开资料：包含方案字段的 JSON 数据集，以及发布已核实价格变动的 Atom feed。这个工作流根据维护方公开说明整理。</p>

<p lang="en">When shortlisting n8n hosting plans, check which plans you can order before comparing introductory and renewal costs. The independent price tracker SelfHostCost describes two public sources in its write-up: a JSON dataset with plan details and an Atom feed for verified price changes. This workflow is based on the maintainer’s documentation.</p>

<p lang="zh-CN">从 JSON 的托管商条目中筛出 <code>availability</code> 为 <code>orderable</code> 的方案。把首期月价、续费月价和预付月数放在同一行，同时保留 <code>checked</code>、<code>source</code> 和备注。这样，审批预算的人可以看出低月价是否需要长期预付，以及报价是否还要加上 PostgreSQL 等费用。</p>

<p lang="en">Filter the hosting rows to plans whose <code>availability</code> is <code>orderable</code>. Put the introductory monthly price, renewal monthly price, and prepaid months on the same line, alongside <code>checked</code>, <code>source</code>, and the notes. That gives the budget reviewer enough context to see whether a low monthly price requires a long prepayment or carries an extra cost such as PostgreSQL.</p>

<p lang="zh-CN">将 Atom feed 接入 n8n，把价格通知作为重新查看 JSON 对应条目的触发条件。下单或迁移前，由负责人打开该条目的 <code>source</code>，确认供应商当前的价格、预付要求和可用性。若清单中找不到原本考虑的方案，先回看未筛选数据中的可用性状态，区分不可下单与容量不足。</p>

<p lang="en">Connect the Atom feed to n8n and use a price alert to trigger a review of the matching JSON row. Before ordering or migrating, have the person responsible open the row’s <code>source</code> and confirm the vendor’s current price, prepayment requirement, and availability. If a plan disappears from the shortlist, check its availability in the unfiltered data to distinguish an unorderable plan from one that is out of capacity.</p>
