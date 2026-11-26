---
category: "audio"
summaryEn: "The speech recognition release changes how its Go bindings link the GNU OpenMP runtime and fixes WTS output in the CLI."
summaryZh: "这次语音识别工具更新调整了 Go 绑定的 GNU OpenMP 链接方式，并修正命令行工具的 WTS 输出。"
tags: ["whisper-cpp", "go", "openmp", "speech-recognition"]
titleEn: "whisper.cpp 1.9.6 changes OpenMP linking for Go builds"
titleZh: "whisper.cpp 1.9.6 调整 Go 构建的 OpenMP 链接方式"
published: "2026-11-26T23:34:19+08:00"
sources: [{"title": "v1.9.6", "url": "https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.6"}]
---
<p lang="zh-CN">whisper.cpp 于 2026 年 11 月 23 日发布 v1.9.6。与 v1.9.5 相比，Go 绑定的 cgo 链接参数从 <code>-fopenmp</code> 改为 <code>-lgomp</code>，直接链接 GNU OpenMP 运行库。从源码构建 Go 集成的用户需要确保链接器能找到该库。</p>

<p lang="en">whisper.cpp released v1.9.6 on November 23, 2026. Compared with v1.9.5, the Go bindings pass <code>-lgomp</code> to the cgo linker in place of <code>-fopenmp</code>, linking directly against the GNU OpenMP runtime. Users who build Go integrations from source need to make sure the linker can find that library.</p>

<p lang="zh-CN">该版本还在发布工作流中加入 API 和 ABI 检查，并修正了命令行工具的 WTS 输出。前者属于项目的发布验证流程，后者影响使用该输出格式的命令行用户。</p>

<p lang="en">The release also adds API and ABI checks to the release workflow and corrects the command-line tool’s WTS output. The checks run as part of the project’s release validation, while the output fix affects CLI users who work with that format.</p>
