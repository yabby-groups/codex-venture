---
category: "agents"
summaryEn: "Upgrading to langchain-ollama 1.2.0 requires moving off Python 3.10 and using version 0.6.3 or later of the ollama Python dependency."
summaryZh: "升级到 langchain-ollama 1.2.0 时，Python 3.10 用户需要先迁移运行环境，同时确保 ollama Python 依赖包至少为 0.6.3。"
tags: ["langchain", "ollama", "python"]
titleEn: "langchain-ollama 1.2.0 drops Python 3.10 support"
titleZh: "langchain-ollama 1.2.0 停止支持 Python 3.10"
published: "2026-11-26T23:46:34+08:00"
sources: [{"title": "langchain-ollama==1.2.0", "url": "https://github.com/langchain-ai/langchain/releases/tag/langchain-ollama%3D%3D1.2.0"}]
---
<p lang="zh-CN">LangChain 于 11 月 23 日发布 Ollama 集成包 langchain-ollama 1.2.0，停止支持 Python 3.10。仍在 Python 3.10 上运行的项目需要先迁移 Python 环境，再升级这个集成包。<a href="https://github.com/langchain-ai/langchain/releases/tag/langchain-ollama%3D%3D1.2.0">官方发布记录</a></p>

<p lang="en">LangChain released version 1.2.0 of its langchain-ollama integration on November 23, dropping Python 3.10 support. Projects still running Python 3.10 need to move to a newer Python environment before upgrading the integration. <a href="https://github.com/langchain-ai/langchain/releases/tag/langchain-ollama%3D%3D1.2.0">Official release notes</a></p>

<p lang="zh-CN">这次更新还将 Python 依赖包 ollama 的最低版本提高到 0.6.3，以支持思考级别设置。如果项目锁定的 ollama 版本低于 0.6.3，升级时也要调整该依赖。</p>

<p lang="en">The release also raises the minimum version of the ollama Python dependency to 0.6.3 to support thinking-level settings. Projects that pin ollama below 0.6.3 will need to update that dependency as part of the upgrade.</p>
