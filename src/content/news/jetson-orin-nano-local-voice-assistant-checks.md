---
category: "agents"
summaryEn: "CAVEDU’s JetPack 6.2 setup combines Parakeet, Gemma4 E2B, and Kokoro. Check memory and transcription language before rehearsing the full voice-and-camera pipeline."
summaryZh: "CAVEDU 在 JetPack 6.2 上把 Parakeet、Gemma4 E2B 和 Kokoro 接成端侧链路。离线演示前先核对内存和转写语言，再逐环节试跑。"
tags: ["jetson-orin-nano", "jetpack", "gemma4", "parakeet", "kokoro"]
titleEn: "What to check before a local voice assistant demo on Jetson Orin Nano"
titleZh: "在 Jetson Orin Nano 上演示本地语音助手前，先查内存和识别语言"
blocks: [{"items": [{"en": "Speak a short sentence in a supported language. Check the Parakeet transcript before passing it to Gemma4 E2B.", "zh": "用受支持的语言说一句短句，先核对 Parakeet 的转写，再交给 Gemma4 E2B。"}, {"en": "Give Gemma4 E2B a camera image with a detail you can verify. Check whether the answer describes that detail accurately.", "zh": "用摄像头拍一张有明确可核对细节的图，让 Gemma4 E2B 回答，再核对它是否说对了该细节。"}, {"en": "Send a known sentence to Kokoro and listen through the intended speaker. Once the three checks pass individually, try one complete spoken turn.", "zh": "给 Kokoro 输入一句已知文本，用演示时的扬声器试听。三个环节分别通过后，再跑一轮完整的语音问答。"}], "kind": "steps", "title": {"en": "Check each component before the demo", "zh": "演示前逐环节验收"}}]
type: "workflows"
version: "JetPack 6.2 on Jetson Orin Nano Super"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 71, "tier": "standard", "audience": "core"}
published: "2026-11-28T20:10:38+08:00"
sources: [{"title": "Build a Local Voice Assistant on Jetson Orin Nano with Gemma4", "url": "https://dev.to/cavedu/build-a-local-voice-assistant-on-jetson-orin-nano-with-gemma4-koj"}]
---
<p lang="zh-CN">CAVEDU 的子賢在 JetPack 6.2 上记录了一套 Jetson Orin Nano Super 端侧语音助手配置。Parakeet（parakeet-tdt-0.6b-v3）负责转写，Gemma4 E2B 处理文字和图像，Kokoro 把回答读出来。作者描述的本地运行以预先下载软件和模型为前提。<a href="https://dev.to/cavedu/build-a-local-voice-assistant-on-jetson-orin-nano-with-gemma4-koj">子賢的搭建记录</a></p>

<p lang="en">CAVEDU’s 子賢 documented a local voice assistant on the Jetson Orin Nano Super with JetPack 6.2. Parakeet (parakeet-tdt-0.6b-v3) transcribes speech, Gemma4 E2B handles text and images, and Kokoro reads the reply aloud. The author describes running the components locally after downloading the software and models. <a href="https://dev.to/cavedu/build-a-local-voice-assistant-on-jetson-orin-nano-with-gemma4-koj">The original setup write-up</a></p>

<p lang="zh-CN">筹备演示时，先核对系统版本和摄像头、麦克风、扬声器能否正常使用。原配置建议使用 SSD，并为占用较多内存的应用准备了 8 GB 交换空间。套用这项设置前先检查现有交换空间和开机挂载配置。来源列明语音识别支持英语及多种欧洲语言，中文转写仍待验证。下方验收流程依据作者配置整理，本站未运行。</p>

<p lang="en">Before a demo, check the system version and make sure the camera, microphone, and speaker work. The documented setup recommends an SSD and uses 8 GB of swap for an application that takes up much of the available RAM. Check the existing swap and boot configuration before adopting that setting. The source lists English and several European languages for speech recognition. Chinese transcription remains unverified for this setup. Codex Venture derived the checks below from the write-up and did not run the setup.</p>
