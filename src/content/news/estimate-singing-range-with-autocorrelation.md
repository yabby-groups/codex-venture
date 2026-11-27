---
category: "audio"
summaryEn: "Estimate the pitch of a recorded vocal glide with autocorrelation, then map the lowest and highest steady pitches to musical notes."
summaryZh: "用自相关估算滑音录音的基频，再把最低和最高的稳定音高换算成音名。"
tags: ["audio", "numpy", "pitch-tracking"]
titleEn: "Estimate your singing range from a recording with NumPy"
titleZh: "用 NumPy 从录音估算歌唱音域"
type: "workflows"
version: "NumPy autocorrelation method and mono WAV input"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T22:01:31+08:00"
sources: [{"title": "How to Find Your Singing Range With Python: Pitch Tracking From Scratch in Under 50 Lines", "url": "https://dev.to/taniaalwan/how-to-find-your-singing-range-with-python-pitch-tracking-from-scratch-in-60-lines-5hl8"}]
---
<p lang="zh-CN">在安静的房间录一段滑音，从舒适的低音缓慢滑到舒适的高音，再滑回来。保持与麦克风的距离稳定，导出单声道 WAV。Tania Alwan 的 NumPy 教程以这种录音为输入，建议在出现用力或不适前停下，因为短促的尖声也可能被追踪器计入结果。<a href="https://dev.to/taniaalwan/how-to-find-your-singing-range-with-python-pitch-tracking-from-scratch-in-60-lines-5hl8">原教程</a></p>

<p lang="en">In a quiet room, record a slow glide from a comfortable low note to a comfortable high note and back. Keep a steady distance from the microphone and export a mono WAV. Tania Alwan’s NumPy tutorial uses this recording as its input and recommends stopping before you strain, since a brief squeak can still register in the pitch estimate. <a href="https://dev.to/taniaalwan/how-to-find-your-singing-range-with-python-pitch-tracking-from-scratch-in-60-lines-5hl8">Original tutorial</a></p>

<p lang="zh-CN">把录音切成短帧，用自相关比较每一帧与自身移位后的相似程度。找到代表重复周期的滞后量后，用采样率除以该滞后量（以样本计），得到以 Hz 表示的基频估计。再用 <code>69 + 12 * log2(f / 440)</code> 换算为 MIDI 音高，取最近的整数即可得到最接近的半音。用 440 Hz 检查换算是否返回 MIDI 69，也就是 A4。</p>

<p lang="en">Split the recording into short frames and use autocorrelation to compare each frame with shifted copies of itself. Once you identify the lag corresponding to the repeating period, divide the sample rate by that lag in samples to estimate the fundamental frequency in hertz. Convert it with <code>69 + 12 * log2(f / 440)</code> and round to the nearest integer to get the nearest MIDI semitone. Use 440 Hz as a conversion check. It should return MIDI 69, or A4.</p>

<p lang="zh-CN">检查估计序列两端所对应的录音片段，再记录可稳定唱出的最低和最高音。若某个极值只出现在短促的破音处，重录一遍舒适的滑音再比较。本流程依据 Alwan 的教程整理，输出是这段录音中的音域估计。</p>

<p lang="en">Listen to the parts of the recording that produced the lowest and highest estimates, then record the lowest and highest notes you can sing steadily. If an extreme comes from a brief voice break, record another comfortable glide and compare. This workflow follows Alwan’s tutorial and estimates the range captured in that recording.</p>
