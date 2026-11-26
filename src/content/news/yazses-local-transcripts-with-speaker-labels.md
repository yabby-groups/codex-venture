---
category: "audio"
summaryEn: "Use the YazSes CLI to transcribe an existing recording or a live meeting locally, then check who said what before sharing the transcript."
summaryZh: "用 YazSes CLI 在本地转写已有录音或实时会议，并在分享前核对说话人标签。"
tags: ["yazses", "transcription", "speaker-diarization"]
titleEn: "Transcribe meetings locally with speaker labels in YazSes"
titleZh: "用 YazSes 在本地生成带说话人标签的会议转写"
blocks: [{"kind": "notice", "text": {"en": "The maintainer says live meeting audio is deleted after processing by default. Set retain_audio = true before the meeting if you need to keep the recording for review.", "zh": "维护者说明，实时会议的音频默认在处理后删除。如果需要保留录音供复核，请在会议前设置 retain_audio = true。"}, "title": {"en": "Audio retention", "zh": "录音保留设置"}}]
type: "tutorials"
version: "YazSes CLI file transcription and live meeting mode, November 26, 2026 maintainer guide"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T03:02:50+08:00"
sources: [{"title": "Offline meeting transcripts with speaker labels, and why telling it the speaker count made it worse", "url": "https://dev.to/mskazemi/offline-meeting-transcripts-with-speaker-labels-and-why-telling-it-the-speaker-count-made-it-worse-2dge"}]
---
<p lang="zh-CN">手里已有一段多人录音时，可以用 YazSes 生成带说话人标签的 Markdown 初稿。维护者 Mohsen Seyedkazemi Ardebili 的使用说明覆盖已有文件和实时会议两种入口，并说明转写和说话人区分可在普通 CPU 上本地运行。以下步骤依据维护者说明整理，未独立实测。<a href="https://dev.to/mskazemi/offline-meeting-transcripts-with-speaker-labels-and-why-telling-it-the-speaker-count-made-it-worse-2dge">维护者使用说明</a></p>

<p lang="en">If you already have a recording with several speakers, YazSes can produce a Markdown draft with speaker labels. Maintainer Mohsen Seyedkazemi Ardebili documents two paths, one for existing files and one for live meetings, and says that transcription and speaker diarization can run locally on a standard CPU. The steps below come from the maintainer’s guide and were not independently tested. <a href="https://dev.to/mskazemi/offline-meeting-transcripts-with-speaker-labels-and-why-telling-it-the-speaker-count-made-it-worse-2dge">Maintainer’s guide</a></p>

<p lang="zh-CN">已有 YazSes CLI 和 FFmpeg 可解码的录音时，运行 <code>yazses transcribe interview.m4a --diarize --format md</code>。把示例文件名换成实际路径。预期结果是带说话人标签的 Markdown 文本。发布纪要前，抽查几处说话人交替的位置，确认身份后再用 <code>--rename</code> 将通用标签替换为姓名。</p>

<p lang="en">With the YazSes CLI available and a recording FFmpeg can decode, run <code>yazses transcribe interview.m4a --diarize --format md</code>. Replace the example filename with your recording’s path. Expect Markdown text with speaker labels. Before sharing the minutes, spot-check a few speaker changes against the recording and use <code>--rename</code> to replace generic labels once you have confirmed the identities.</p>

<p lang="zh-CN">实时会议功能默认关闭。先运行 <code>yazses features enable meeting</code>，再用 <code>yazses meeting start</code> 开始，用 <code>yazses meeting stop</code> 结束。结束后检查该次会议的输出目录，其中应有带标签的 <code>transcript.md</code>、<code>transcript.json</code> 和质量报告。如果实时记录没有启动，先确认会议功能是否已启用。</p>

<p lang="en">Live meeting transcription is disabled by default. Run <code>yazses features enable meeting</code>, then use <code>yazses meeting start</code> to begin and <code>yazses meeting stop</code> to finish. Check the meeting’s output folder for a labeled <code>transcript.md</code>, <code>transcript.json</code>, and a quality report. If the live session fails to start, first check whether the meeting feature is enabled.</p>
