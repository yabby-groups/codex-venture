---
category: "open-source"
summaryEn: "RepoFleet packages shared Claude Code rules, Git hooks, and checks so maintainers can update them across repositories and review each change in a pull request."
summaryZh: "RepoFleet 将 Claude Code 的共用规则、Git hooks 和检查打包，方便维护者跨仓库分发更新，并在各自的拉取请求中审阅改动。"
tags: ["repofleet", "claude-code", "git-hooks"]
titleEn: "RepoFleet distributes shared Claude Code rules across repositories via pull requests"
titleZh: "RepoFleet 通过拉取请求向多个仓库分发 Claude Code 共用规则"
editorial: {"score": 65, "tier": "standard", "audience": "core"}
published: "2026-11-28T10:05:59+08:00"
sources: [{"title": "mwitkewiz1/RepoFleet", "url": "https://github.com/mwitkewiz1/RepoFleet"}]
---
<p lang="zh-CN">维护多个仓库时，改一条 Claude Code 共用规则往往要在每个仓库里改一遍。新公开的 RepoFleet 把规则、Git hooks 和检查放进同一个工具包，再通过拉取请求把更新送到各仓库。维护者可以在合并前逐库查看差异。</p>

<p lang="en">A change to a shared Claude Code rule can mean editing the same file across several repositories. The newly public RepoFleet bundles rules, Git hooks, and checks into a kit and sends updates to each repository through pull requests. Maintainers can review each repository’s diff before merging.</p>

<p lang="zh-CN">项目的 CLI 根据仓库清单提供总览。README 给出了 <code>examples/roster.json</code> 作为清单模板，仓库路径相对于清单文件解析。项目围绕 Claude Code 设计，要求 Node.js 24 和 Git，采用 MIT 许可。也可以单独采用 <code>kit/</code> 中的规则和检查。</p>

<p lang="en">The project’s CLI provides an overview of the repositories listed in a roster. The README points to <code>examples/roster.json</code> as a template, with repository paths resolved relative to the roster file. RepoFleet is designed for Claude Code, requires Node.js 24 and Git, and uses the MIT license. The rules and checks in <code>kit/</code> can also be adopted on their own.</p>

<p lang="zh-CN">项目作者在 README 中称，自 2026 年 10 月 14 日起，已在自己的九个仓库使用这套工具包。已有自定义 hooks 的仓库尤其适合在合并前查看 PR 差异，核对本地设置会受到哪些影响。本文依据项目文档撰写，未运行工具。<a href="https://github.com/mwitkewiz1/RepoFleet">RepoFleet 项目仓库</a></p>

<p lang="en">The project author says in the README that they have used the kit across nine of their own repositories since October 14, 2026. In repositories with custom hooks, the pull request diff gives maintainers a place to check how the update affects local settings before merging. This report is based on the project documentation. We did not run the tool. <a href="https://github.com/mwitkewiz1/RepoFleet">RepoFleet repository</a></p>
