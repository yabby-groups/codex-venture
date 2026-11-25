---
category: "open-source"
summaryEn: "LiteLLM v1.110.4 updates nginx and zlib in the standalone UI image. Refreshing end-user restrictions now reads only records for restricted customers."
summaryZh: "LiteLLM v1.110.4 更新了独立 UI 镜像中的 nginx 和 zlib，并把刷新终端用户限制时的数据库读取范围缩小到受限制客户的记录。"
tags: ["litellm", "containers", "database"]
titleEn: "LiteLLM v1.110.4 updates UI image dependencies and reduces reads during restriction refreshes"
titleZh: "LiteLLM v1.110.4 更新 UI 镜像依赖，减少刷新用户限制时的数据库读取"
published: "2026-11-25T19:28:24+08:00"
sources: [{"title": "v1.110.4", "url": "https://github.com/BerriAI/litellm/releases/tag/v1.110.4"}]
---
<p lang="zh-CN">LiteLLM 于 2026 年 11 月 25 日发布 v1.110.4，将独立 UI 镜像内的 nginx 和 zlib 分别更新至 1.31.10 和 1.4。维护者在发布说明中表示，升级无需额外操作。<a href="https://github.com/BerriAI/litellm/releases/tag/v1.110.4">官方发布说明</a></p>

<p lang="en">LiteLLM released v1.110.4 on November 25, 2026, updating nginx to 1.31.10 and zlib to 1.4 in its standalone UI image. The maintainers say the upgrade requires no additional steps. <a href="https://github.com/BerriAI/litellm/releases/tag/v1.110.4">Official release notes</a></p>

<p lang="zh-CN">此版本还缩小了刷新终端用户限制时的数据库读取范围。刷新现在只读取受限制客户的记录，省去了对整张终端用户表的读取。发布说明列出 v1.108.17、v1.109.5 和 v1.111.0 也包含这些改动。</p>

<p lang="en">The release also reduces how much data LiteLLM reads when refreshing end-user restrictions. The refresh now reads only records for restricted customers, eliminating the previous read of the entire end-user table. The release notes list v1.108.17, v1.109.5, and v1.111.0 as also containing these changes.</p>
