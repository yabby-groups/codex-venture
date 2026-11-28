---
category: "coding"
summaryEn: "Cursor cloud agents can now host internal web apps behind Cursor single sign-on. Teams can share a live link, and the publishing flow checks for common credential exposures."
summaryZh: "Cursor 云端 Agent 可托管接入 Cursor 单点登录的内部 Web 应用。团队可以直接分享上线链接，发布流程会检查常见的凭据暴露问题。"
tags: ["cursor", "cloud-agents", "deployment"]
titleEn: "Cursor cloud agents can now publish internal web apps"
titleZh: "Cursor 云端 Agent 可将内部应用发布为团队链接"
editorial: {"score": 68, "tier": "standard", "audience": "core"}
published: "2026-11-28T13:45:52+08:00"
sources: [{"title": "Build Live Apps in Cursor", "url": "https://cursor.com/changelog/build-live-apps"}]
---
<p lang="zh-CN">团队做了一张活动报名页，现在可以用 Cursor 把它发布成同事能打开的链接。Cursor 在 2026 年 11 月 5 日的更新日志中介绍了这项功能。启动云端 Agent 后，明确告诉它要构建一个应用，Agent 就会搭建网页、配置托管，并用 Cursor 单点登录（SSO）保护访问。</p>

<p lang="en">A team building an event signup page can now publish it from Cursor and share the link with coworkers. Cursor introduced the feature in its November 5, 2026 changelog. Start a cloud agent and explicitly ask it to build an app. The agent scaffolds the site, provisions hosting, and sets up access through Cursor single sign-on (SSO).</p>

<p lang="zh-CN">如果报名页需要保存提交记录，云端 Agent 可以按需创建 Postgres 数据库。如果应用要连接团队已有的系统，Cursor 会请求连接所需的凭据。发布时，由用户选定一个唯一域名，Cursor 会返回可分享的访问链接。</p>

<p lang="en">If the page needs to save signups, the cloud agent can provision a Postgres database. If the app connects to an existing team system, Cursor asks for the credentials it needs. When publishing, you choose a unique domain and Cursor returns a link you can share.</p>

<p lang="zh-CN">Cursor 表示，发布流程会检查应用文件中是否写入了密钥，以及是否存在其他常见的凭据暴露问题。检查失败时，Agent 会指出需要修复的地方。按 11 月 5 日的更新日志，部署支持 Cursor Origin 和 GitHub 上的新建或现有仓库，GitLab 接入仍在计划中。<a href="https://cursor.com/changelog/build-live-apps">Cursor 官方更新日志</a></p>

<p lang="en">Cursor says its publishing checks look for secrets written into app files and other common credential exposures. If a check fails, the agent identifies what needs fixing. The November 5 changelog lists deployment support for new and existing repositories on Cursor Origin and GitHub, with GitLab support planned. <a href="https://cursor.com/changelog/build-live-apps">Cursor changelog</a></p>
