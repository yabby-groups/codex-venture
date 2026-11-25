---
category: "agents"
summaryEn: "Graphiti’s 0.32 series removes the Kuzu driver and enforces group membership on affected UUID operations when callers supply a group ID."
summaryZh: "Graphiti 0.32 系列移除了 Kuzu 驱动，并在调用方提供组 ID 时校验相关 UUID 操作的组归属。"
tags: ["graphiti", "kuzu", "knowledge-graphs"]
titleEn: "Graphiti 0.32 drops Kuzu support and adds UUID group checks"
titleZh: "Graphiti 0.32 移除 Kuzu 驱动，为 UUID 操作加入组归属校验"
published: "2026-11-25T19:42:56+08:00"
sources: [{"title": "v0.32.1 - Relate driver, concurrent ingestion, group isolation, and Kuzu removal", "url": "https://github.com/getzep/graphiti/releases/tag/v0.32.1"}]
---
<p lang="zh-CN">Graphiti 在 2026 年 11 月 24 日发布 v0.32.1，作为 v0.32.0 在 GitHub 上的替代发行版。功能变动来自 v0.32.0，其中一项是移除 Kuzu 驱动。依赖该驱动的部署需要在升级前迁移到受支持的后端。</p>

<p lang="en">Graphiti published v0.32.1 on November 24, 2026, as the replacement for its v0.32.0 GitHub release. The functional changes came in v0.32.0 and include the removal of the Kuzu driver. Deployments that depend on it need to move to a supported backend before upgrading.</p>

<p lang="zh-CN">在受影响的 UUID 操作中，调用方传入 group_id 后，如果 UUID 属于其他组，Graphiti 会返回对应的节点或边未找到错误，并阻止该次读写。显式传入 UUID 调用 add_episode 时，省略 group_id 会让查找局限在默认组。</p>

<p lang="en">For affected UUID operations, supplying a group_id alongside a UUID that belongs to another group now raises the corresponding node- or edge-not-found error and prevents the read or write. When add_episode receives an explicit UUID and no group_id, its lookup is limited to the default group.</p>
