---
category: "coding"
summaryEn: "Gabriel Ebner’s preprint describes a Lean 4 proof that SafeJIT’s RISC-V and x86-64 executables cannot crash on any input within a Linux user-process model."
summaryZh: "Gabriel Ebner 的预印本介绍了一项 Lean 4 证明。SafeJIT 的 RISC-V 和 x86-64 可执行文件在给定的 Linux 用户进程模型中处理任意输入都不会崩溃。"
tags: ["javascript", "jit", "lean-4", "formal-verification"]
titleEn: "How SafeJIT’s crash-freedom proof reaches machine code"
titleZh: "SafeJIT 如何把无崩溃证明推进到机器码"
type: "insights"
version: "arXiv:2611.28436, submitted 2026-11-21"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T08:21:07+08:00"
sources: [{"title": "SafeJIT: A Speculating JIT Engine Verified Down to the Machine Code", "url": "https://arxiv.org/abs/2611.28436"}]
---
<p lang="zh-CN">推测式即时编译器会利用运行时收集的类型信息生成机器码。省掉一个本应保留的类型检查，或者在推测失效时未能退回通用执行路径，都可能使进程崩溃。Gabriel Ebner 在 2026 年 11 月 21 日提交的 <a href="https://arxiv.org/abs/2611.28436">SafeJIT 预印本</a>中，用一个小型 JavaScript 引擎研究如何把这类崩溃纳入机器可检验的证明。</p>

<p lang="en">A speculating JIT uses type information gathered at runtime to generate machine code. Dropping a necessary type check or failing to fall back when an assumption breaks can crash the process. In the <a href="https://arxiv.org/abs/2611.28436">SafeJIT preprint</a>, submitted November 21, 2026, Gabriel Ebner uses a small JavaScript engine to study how to cover these failures with a machine-checked proof.</p>

<p lang="zh-CN">据作者摘要，Lean 4 定理覆盖静态链接的 RISC-V 和 x86-64 可执行文件，并使用 Sail 指令集模型逐条解释机器指令。证明范围从解析器和字节码解释器一直延伸到 JIT 可能生成的机器码、去优化路径和垃圾回收器。C 编译器、汇编器和链接器无需被当作可信组件。</p>

<p lang="en">According to the abstract, the Lean 4 theorem covers statically linked RISC-V and x86-64 executables, with Sail instruction-set models giving meaning to each machine instruction. The proof spans the parser, bytecode interpreter, machine code the JIT can generate, deoptimization paths, and garbage collector. It does not require trusting the C compiler, assembler, or linker.</p>

<p lang="zh-CN">这里的结论有明确边界。作者证明的是这两种架构上的特定二进制文件在给定 Linux 用户进程模型中对任意输入都不会崩溃。定理的适用范围由这些二进制文件和进程模型共同界定。</p>

<p lang="en">The theorem is defined around specific binaries and a Linux user-process model. Within that model, the author proves that those binaries cannot crash on any input.</p>
