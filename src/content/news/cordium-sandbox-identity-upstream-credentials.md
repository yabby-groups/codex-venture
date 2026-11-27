---
category: "open-source"
summaryEn: "Cordium pairs Kubernetes sandboxes with Octelium access policies so an authorized workspace can reach internal services without holding their upstream application credentials."
summaryZh: "Cordium 将 Kubernetes 沙箱与 Octelium 的访问策略结合，使获准访问内部服务的工作区无需持有上游应用凭据。"
tags: ["cordium", "kubernetes", "sandboxing", "identity"]
titleEn: "How Cordium gives sandboxes access to services without handing them credentials"
titleZh: "Cordium 如何让沙箱访问内部服务而无需持有上游凭据"
type: "insights"
version: "Cordium README verified 2026-11-27"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T18:03:28+08:00"
sources: [{"title": "Show HN: Sandbox platform on Kubernetes for secure remote access without secrets", "url": "https://github.com/octelium/cordium"}]
---
<p lang="zh-CN">代码代理在沙箱里执行任务时，可能还得访问团队的数据库或内部 API。Cordium 的项目文档把这两件事放在同一个 Kubernetes 工作环境里。工作负载在隔离的 Workspace 中运行，Octelium 根据身份和策略提供对上游资源的访问。<a href="https://github.com/octelium/cordium">Cordium 项目文档</a></p>

<p lang="en">A coding agent running inside a sandbox may still need access to a team database or internal API. Cordium’s project documentation brings both parts of that workflow into one Kubernetes environment. Workloads run in isolated Workspaces, and Octelium provides access to upstream resources based on identity and policy. <a href="https://github.com/octelium/cordium">Cordium project documentation</a></p>

<p lang="zh-CN">按项目描述，这种设计让获准访问资源的 Workspace 无需持有相应的上游应用凭据，例如数据库密码或 API 密钥。运行任务和决定任务可以访问哪些资源，由此有了各自的控制点。README 描述的是单租户自托管架构及其访问边界，核对范围截至 2026 年 11 月 27 日。</p>

<p lang="en">According to the project, this design lets an authorized Workspace use an upstream resource without holding its application credentials, such as a database password or API key. It gives teams separate controls for running a job and deciding which resources that job can access. The scope here is the single-tenant, self-hosted architecture and access model described in the README verified November 27, 2026.</p>
