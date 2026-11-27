---
category: "coding"
summaryEn: "Harny connects local models served by Ollama, LM Studio, or llama.cpp to VS Code and VSCodium. A small edit and an existing test give you a concrete way to check whether your model can handle editor tool calls."
summaryZh: "Harny 把 Ollama、LM Studio 或 llama.cpp 提供的本地模型接入 VS Code 和 VSCodium。用一次小改动和一项现有测试，就能检查自己的模型能否完成编辑器里的工具调用。"
tags: ["harny", "vscodium", "vs-code", "local-llms"]
titleEn: "Harny brings local coding models into VSCodium and VS Code"
titleZh: "Harny 让本地模型在 VSCodium 和 VS Code 里改代码"
type: "insights"
version: "Project documentation snapshot, 2026-11-27"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 66, "tier": "standard", "audience": "core"}
published: "2026-11-28T04:01:12+08:00"
sources: [{"title": "Show HN: Harny – AI coding agent for VSCodium/VS Code tuned for small/local LLMs", "url": "https://harny.dev/"}]
---
<p lang="zh-CN">如果你已经在用 Ollama、LM Studio 或 llama.cpp 跑本地模型，Harny 提供了一个在 VSCodium 或 VS Code 里调用这些模型的入口。开发者 SPLTEK 在项目主页上说明，扩展通过兼容 OpenAI Chat Completions API 的接口连接模型，可以读取和编辑项目文件、运行命令，并为每个文件夹保留一条会话。VSCodium 用户可从主页进入 Open VSX，VS Code 用户可从同一页面进入 VS Code Marketplace。<a href="https://harny.dev/">Harny 项目主页</a></p>

<p lang="en">If you already run a local model with Ollama, LM Studio, or llama.cpp, Harny gives you a way to use it from VSCodium or VS Code. Developer SPLTEK says the extension connects through an OpenAI Chat Completions-compatible API, can read and edit project files and run commands, and keeps one persistent conversation per folder. The project site links to Open VSX for VSCodium users and the VS Code Marketplace for VS Code users. <a href="https://harny.dev/">Harny project site</a></p>

<p lang="zh-CN">主页用一个请求为 HTTP 请求加上退避重试并运行测试的任务来展示工具调用。界面展示了读取相关文件和调用测试命令，选用的模型是 DeepSeek。本文依据项目主页撰写，尚未运行扩展。小型本地模型能否稳定完成同类任务，仍需在自己的环境里验证。</p>

<p lang="en">The project page illustrates tool calling with a task that asks the agent to add retry backoff to HTTP requests and run tests. The example shows the agent reading the relevant file and invoking the test command with a DeepSeek model selected. This account is based on the project page. We haven’t run the extension, so the reliability of smaller local models on similar tasks remains to be checked in your own setup.</p>

<p lang="zh-CN">从主页找到对应的扩展入口后，可以先选自己已经在用的本地后端，在熟悉的项目里试一次范围明确的小改动。让模型先读目标文件，再改一处代码并运行现有的相关测试。检查实际改动和测试结果，就能看出这次调用在哪一步完成、在哪一步停下。</p>

<p lang="en">After finding the extension listing for your editor, start with the local backend you already use and pick a small, well-defined change in a familiar project. Ask the model to read the target file, make one edit, and run the relevant existing test. Review the diff and test result to see which steps it completed and where it stopped.</p>
