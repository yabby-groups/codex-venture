---
category: "agents"
summaryEn: "Graphiti MCP Server 1.1.5 adds group isolation checks to five tools that read or modify graph data. It also replaces 1.1.4, whose release job failed to publish Docker images."
summaryZh: "Graphiti MCP Server 1.1.5 为五个图谱读写工具加入分组隔离检查，并替代因发布任务失败而没有 Docker 镜像的 1.1.4。"
tags: ["graphiti", "mcp"]
titleEn: "Graphiti MCP Server 1.1.5 adds group isolation to five tools"
titleZh: "Graphiti MCP Server 1.1.5 为五个工具加入分组隔离检查"
published: "2026-11-25T19:42:56+08:00"
sources: [{"title": "mcp-v1.1.5 - Group isolation for MCP tools", "url": "https://github.com/getzep/graphiti/releases/tag/mcp-v1.1.5"}]
---
<p lang="zh-CN">Graphiti 于 2026 年 11 月 24 日发布 MCP Server 1.1.5，为五个涉及事件、实体关系和 Saga 摘要的工具加入分组检查。对按组存放图谱数据的部署，这些工具会在所选组内处理请求。传入属于其他组的 UUID 时，工具会返回错误，阻止该次操作读取或修改其他组的数据。</p>

<p lang="en">Graphiti released MCP Server 1.1.5 on November 24, 2026, adding group checks to five tools that work with episodes, entity relationships, and saga summaries. In deployments that organize graph data by group, these tools now operate within the selected group. If a UUID belongs to a different group, the tool returns an error and prevents the operation from reading or modifying that group’s data.</p>

<p lang="zh-CN">官方发布说明将 1.1.5 列为 1.1.4 的替代版本。1.1.4 的发布任务失败，未生成 Docker 镜像。MCP Server 1.1.5 要求 graphiti-core 0.32.0 或更高版本，其 Docker 镜像使用 0.32.1。</p>

<p lang="en">The official release notes identify 1.1.5 as the replacement for 1.1.4, whose release job failed before publishing Docker images. MCP Server 1.1.5 requires graphiti-core 0.32.0 or later, and its Docker images use 0.32.1.</p>
