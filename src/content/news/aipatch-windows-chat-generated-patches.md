---
category: "open-source"
summaryEn: "AiPatch pairs a repository-supplied prompt with a portable Windows x64 executable so users can apply one chat-generated patch across several local files."
summaryZh: "AiPatch 用配套提示词和便携式 Windows x64 程序，把聊天模型生成的一份补丁应用到本地多个文件。"
tags: ["aipatch", "windows", "code-patching"]
titleEn: "AiPatch applies chat-generated edits across local files on Windows"
titleZh: "AiPatch 把网页聊天生成的补丁应用到 Windows 本地项目"
type: "open-source"
version: "Windows x64 README scope"
verified: "2026-11-28"
status: "current"
tested: false
project: "5a743fc14165a5dac5fc7de1c29d41a9bbadf8071e836c507f164b6b76ff6be6"
editorial: {"score": 65, "tier": "standard", "audience": "core"}
published: "2026-11-28T09:35:22+08:00"
sources: [{"title": "NetForgeDev/AiPatch", "url": "https://github.com/NetForgeDev/AiPatch"}]
---
<p lang="zh-CN">如果你在网页聊天里让模型同时修改几个文件，AiPatch 提供了一种把改动写回本地项目的方式。按 NetForgeDev 的 README，Windows x64 用户把便携式程序放进项目目录，用仓库提供的提示词让模型生成补丁，再由本地程序把补丁应用到多个文件。这样就省去了逐个文件定位并粘贴代码的步骤。<a href="https://github.com/NetForgeDev/AiPatch">项目仓库</a></p>

<p lang="en">If you ask a model in a browser chat to edit several files at once, AiPatch offers a way to write those changes back to a local project. NetForgeDev’s README describes a portable Windows x64 executable that runs from the project folder. You use the repository’s prompt to have the model generate a patch, then apply it locally across multiple files. That saves you from finding and pasting each edit by hand. <a href="https://github.com/NetForgeDev/AiPatch">Project repository</a></p>

<p lang="zh-CN">对用 Git 管理的项目，可以在应用补丁后用 Git diff 核对实际改动。仓库采用 MIT 许可证。本文依据项目文档，未运行程序。现有资料未给出可核实的发行版本，也不足以验证 token 节省幅度。</p>

<p lang="en">In a Git-managed project, you can inspect the resulting edits with Git diff. The repository uses the MIT license. This report is based on the project documentation, and the executable was not tested. The available material does not establish a release version or substantiate the claimed token savings.</p>
