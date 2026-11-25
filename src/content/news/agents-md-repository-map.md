---
titleZh: "把 AGENTS.md 写成可维护的仓库指南"
titleEn: "Write AGENTS.md as a maintainable repository guide"
summaryZh: "把建立环境、运行测试与目录约束集中到 Agent 能读取的位置。"
summaryEn: "Put setup, test commands, and directory conventions where agents can find them."
type: "resources"
category: "coding"
published: "2026-11-24T22:00:00+08:00"
verified: "2026-11-24"
version: "AGENTS.md public guide"
status: "current"
tested: false
tags: ["agents-md","agents"]
sources: [{"title":"Write AGENTS.md as a maintainable repository guide – primary reference","url":"https://agents.md/"}]
resourceIds: ["agents-md"]
---
<p lang="zh-CN">AGENTS.md 项目网站把它描述为面向编程 Agent 的 Markdown 文件。单仓可从根目录的环境准备、测试命令和文件约定开始。多包仓库可给包目录补充自己的运行方式，并按具体 Agent 的查找规则核对实际作用域。</p>

<p lang="en">The AGENTS.md project describes it as a Markdown file for coding agents. Start at the repository root with setup, test commands, and file conventions. In a multipackage repo, add package-level instructions and check the effective scope under your agent’s lookup rules.</p>

<p lang="zh-CN">写入实际可运行的命令，注明应在哪个目录执行。遇到工具迁移时，把文档变更放进同一个提交，避免保留失效命令。公开仓库的说明应排除凭据和私有基础设施信息。</p>

<p lang="en">Use commands that actually work and name their working directories. Update the instructions in the same commit as a tooling migration so old commands do not linger. Keep credentials and private infrastructure details out of guidance in public repositories.</p>
