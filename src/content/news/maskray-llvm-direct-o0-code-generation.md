---
category: "coding"
summaryEn: "In MaskRay’s experiment, a direct code generator built with Claude Code cut compiler instruction counts by 14% on x86-64 and 21% on AArch64 in clang -O0 -g builds. Generated code grew 10% on x86-64 and stayed roughly the same size on AArch64."
summaryZh: "MaskRay 借助 Claude Code 实验了一条直接生成机器码的路径。在 clang -O0 -g 构建中，编译器执行的指令数在 x86-64 上减少 14%，在 AArch64 上减少 21%。x86-64 的生成代码增大 10%，AArch64 上则大致持平。"
tags: ["llvm", "clang", "claude-code", "compilers"]
titleEn: "How MaskRay used Claude Code to test a shorter path from LLVM IR to machine code"
titleZh: "MaskRay 如何用 Claude Code 试验 LLVM -O0 直出机器码"
type: "stories"
version: "2026-11-26 LLVM experiment, clang -O0 -g on x86-64 and AArch64"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T20:00:15+08:00"
sources: [{"title": "A direct -O0 code generator for LLVM", "url": "https://maskray.me/blog/llvm-direct-o0-code-generator"}]
---
<p lang="zh-CN">在 LLVM 的 <code>-O0</code> 构建中，即使关闭优化，后端仍要花时间做指令选择、寄存器分配和机器级处理。MaskRay 在 2026 年 11 月 26 日发表的实验记录中描述了一条更短的路径：逐个函数从 LLVM IR 直接生成机器码字节，省去构建 <code>MachineFunction</code> 的步骤。遇到直接路径无法处理的函数，编译器就对该函数回退到常规流水线。</p>

<p lang="en">Even with optimizations disabled, LLVM’s <code>-O0</code> back end still spends time selecting instructions, allocating registers, and running machine-level passes. In a November 26, 2026 write-up, MaskRay describes a shorter path that emits machine-code bytes directly from LLVM IR without building a <code>MachineFunction</code>. When the direct path cannot handle a function, the compiler falls back to its regular pipeline for that function.</p>

<p lang="zh-CN">据 MaskRay 自述，Claude Code 编写了大部分实验代码，也起草了文章。MaskRay 负责引导实验并编辑文稿。缩短流水线后，仍要核对两种输出路径：作者报告，<code>clang -S</code> 输出的汇编经汇编后，与 <code>clang -c</code> 直接生成的机器码一致。</p>

<p lang="en">MaskRay says Claude Code wrote most of the experimental code and drafted the post. MaskRay guided the experiment and edited the write-up. The shorter pipeline still had to keep both output paths in agreement. MaskRay reports that assembling the output of <code>clang -S</code> produced the same machine code as <code>clang -c</code>.</p>

<p lang="zh-CN">MaskRay 报告，在编译时间追踪器的 <code>clang -O0 -g</code> 构建中，编译器执行的指令数在 x86-64 上减少 14%，在 AArch64 上减少 21%。生成代码的体积在 x86-64 上增加 10%，在 AArch64 上大致相同。这些数字来自作者的实验记录，分别衡量编译器执行的指令数和生成代码的体积。<a href="https://maskray.me/blog/llvm-direct-o0-code-generator">MaskRay 的实验原文</a></p>

<p lang="en">On the compile-time tracker’s <code>clang -O0 -g</code> builds, MaskRay reports that the compiler executed 14% fewer instructions on x86-64 and 21% fewer on AArch64. The generated code was 10% larger on x86-64 and roughly the same size on AArch64. These figures come from the author’s experiment and measure compiler instruction counts and generated code size, respectively. <a href="https://maskray.me/blog/llvm-direct-o0-code-generator">Read MaskRay’s write-up</a></p>
