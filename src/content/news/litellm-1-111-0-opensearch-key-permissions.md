---
category: "open-source"
summaryEn: "LiteLLM Proxy can forward OpenSearch index requests and grant read and write access separately for each key. The release also adds Claude Fable 5.2 entries across three platforms."
summaryZh: "LiteLLM Proxy 现在可以转发 OpenSearch 索引请求，并按密钥分别授予读、写权限。该版本还新增了三个平台的 Claude Fable 5.2 条目。"
tags: ["litellm", "opensearch", "claude"]
titleEn: "LiteLLM v1.111.0 adds per-key OpenSearch read and write grants"
titleZh: "LiteLLM v1.111.0 新增 OpenSearch 按密钥读写授权"
published: "2026-11-25T20:02:48+08:00"
sources: [{"title": "v1.111.0", "url": "https://github.com/BerriAI/litellm/releases/tag/v1.111.0"}]
---
<p lang="zh-CN">LiteLLM 于 2026 年 11 月 25 日发布 v1.111.0。这个版本让代理可以转发 OpenSearch 索引请求，管理员可按代理密钥分别授予读、写权限。例如，只负责查询的客户端可以使用仅获读权限的密钥。</p>

<p lang="en">LiteLLM released v1.111.0 on November 25, 2026. The proxy can now forward OpenSearch index requests, with separate read and write grants for each proxy key. A client that only runs queries can use a key with read access alone.</p>

<p lang="zh-CN">模型接入方面，发布记录列出了 Anthropic 的 Claude Fable 5.2、Claude Platform on AWS 上的对应版本，以及 Azure AI 上的标准和 Fast 条目。代理的剩余预算指标也已更新，会计入已承诺的支出。</p>

<p lang="en">The release also adds Claude Fable 5.2 entries for Anthropic and Claude Platform on AWS, plus standard and Fast entries for Azure AI. The proxy’s remaining-budget indicators now account for committed spend.</p>
