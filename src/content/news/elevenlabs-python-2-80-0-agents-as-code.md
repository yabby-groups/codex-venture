---
category: "agents"
summaryEn: "The Python SDK adds an Agent builder and push and pull commands for teams managing agent configuration in code. It also exposes speaker diarization and name inference in realtime transcription."
summaryZh: "新版 Python SDK 加入 Agent builder 和推送、拉取命令，便于团队用代码管理智能体配置。实时转写也新增说话人区分和姓名推断选项。"
tags: ["elevenlabs", "python", "agents"]
titleEn: "ElevenLabs Python SDK v2.80.0 adds agent configuration as code"
titleZh: "ElevenLabs Python SDK v2.80.0 支持用代码管理智能体配置"
published: "2026-11-25T07:51:11+08:00"
sources: [{"title": "v2.80.0", "url": "https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.80.0"}]
---
<p lang="zh-CN">ElevenLabs 于 2026 年 11 月 24 日发布 Python SDK v2.80.0。维护 ElevenLabs Agents 的团队现在可以用 Agent builder 在代码中定义智能体，再通过 <code>agents.push</code> 和 <code>agents.pull</code> 推送和拉取配置。@PaulAsjes 提交的这组改动还加入了 CLI 项目布局和用于声明客户端工具的 <code>@client_tool</code> 装饰器。</p>

<p lang="en">ElevenLabs released Python SDK v2.80.0 on November 24, 2026. Teams maintaining ElevenLabs Agents can now define agents in code with the Agent builder and use <code>agents.push</code> and <code>agents.pull</code> to push and pull configuration. The changes contributed by @PaulAsjes also add a CLI project layout and a <code>@client_tool</code> decorator for declaring client tools.</p>

<p lang="zh-CN">工具同步有明确范围。按发布记录，推送只管理 webhook 和客户端工具，分支操作不会写入主文件。同一版本中，@Apeksha9389 修复了重启后无法使用同步客户端工具的问题。</p>

<p lang="en">Tool syncing has a defined scope. The release notes say pushes manage only webhook and client tools, and branch operations do not write to the main file. The same release includes a fix from @Apeksha9389 that lets synchronous client tools work after a restart.</p>

<p lang="zh-CN">实时语音转文字也有一项独立更新。@JacekDuszenko 为实时转写封装新增 <code>diarize</code> 和 <code>infer_speaker_names</code> 两个选项，分别用于区分说话人和推断说话人姓名。<a href="https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.80.0">查看发布记录</a></p>

<p lang="en">Realtime speech-to-text received a separate update. @JacekDuszenko added <code>diarize</code> and <code>infer_speaker_names</code> to the realtime transcription wrapper to distinguish speakers and infer their names, respectively. <a href="https://github.com/elevenlabs/elevenlabs-python/releases/tag/v2.80.0">Release notes</a></p>
