---
titleZh: "16 个 Claude Agent 卡在同一个缺陷后，研究员怎样拆解内核构建"
titleEn: "How a researcher got 16 Claude agents past the same kernel build bug"
summaryZh: "Nicholas Carlini 用 GCC 分担内核编译，把一个争抢修复的大任务拆成可以并行定位的缺陷。"
summaryEn: "Nicholas Carlini used GCC to compile part of the kernel and give agents distinct bugs to investigate."
type: "stories"
category: "agents"
published: "2026-11-25T20:55:05+08:00"
verified: "2026-11-25"
version: "Anthropic account, 2026-02-05"
status: "current"
tested: false
tags: ["ai-stories"]
sources: [{"title": "Nicholas Carlini / Anthropic engineering account", "url": "https://www.anthropic.com/engineering/building-c-compiler"}]
---

<p lang="zh-CN">Anthropic 研究员 Nicholas Carlini 让 16 个 Claude Agent 在共享代码库里从头写 C 编译器。许多编译测试可以单独分派，但构建整个 Linux 内核时，多个 Agent 会撞到同一个缺陷，随后彼此覆盖修复。并发进程越多，仍然只有同一个故障信号。</p>

<p lang="en">Anthropic researcher Nicholas Carlini had 16 Claude agents write a C compiler in a shared repository. Individual compiler tests could be distributed, but when the agents built the whole Linux kernel, they ran into the same defect and overwrote each other’s fixes. More processes still shared a single failure signal.</p>

<p lang="zh-CN">Carlini 修改了验证程序，用 GCC 编译内核的大部分文件，交给新编译器的只是一部分。构建失败时可缩小这一部分，逐步隔离出不同文件里的问题，让 Agent 并行修。后来还需要找出单独编译能通过、组合起来却失败的文件。</p>

<p lang="en">Carlini changed the verifier to compile most of the kernel with GCC and hand a subset to the new compiler. Shrinking a failing subset isolated defects in different files, giving the agents independent work. He later had to find combinations of files that failed together despite passing individually.</p>

<p lang="zh-CN">Carlini 报告称，实验花费约 2 万美元 API 成本，经历近 2,000 次 Claude Code 会话，产出的编译器可以构建 Linux 6.9。他同时记录了仍需 GCC 处理 16 位 x86 启动代码，以及汇编器、链接器的局限。本站依据他的原始记录，未复跑编译实验。可借鉴的决策是先让共用的失败信号变成能独立定位的子问题。</p>

<p lang="en">Carlini reports roughly $20,000 in API costs and nearly 2,000 Claude Code sessions for a compiler that could build Linux 6.9. He also records its continued use of GCC for 16-bit x86 startup code and limitations around assembly and linking. This story draws on his account. Codex Venture did not rerun the compiler experiment. The transferable decision was to turn a shared failure signal into independently diagnosable problems.</p>
