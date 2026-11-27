---
category: "image"
summaryEn: "oMyImage’s design offers three checks for browser-based image tools: decoded pixel limits, model delivery, and where each format is decoded."
summaryZh: "从 oMyImage 的分流方案提炼三项设计检查：解码后的像素上限、模型文件的交付方式，以及各格式的解码位置。"
tags: ["omyimage", "onnx", "browser-inference"]
titleEn: "How oMyImage keeps a 28 MB model in the browser and decodes HEIC on the server"
titleZh: "oMyImage 如何把 28 MB 模型留在浏览器，把 HEIC 解码放到服务端"
type: "workflows"
version: "oMyImage deployment described on 2026-11-27"
verified: "2026-11-28"
status: "current"
tested: false
editorial: {"score": 80, "tier": "standard", "audience": "core"}
published: "2026-11-28T04:01:06+08:00"
sources: [{"title": "Image AI in the browser or on a CPU server: what we run where, and why", "url": "https://dev.to/mishrakalpesh9555/image-ai-in-the-browser-or-on-a-cpu-server-what-we-run-where-and-why-53b8"}]
---
<p lang="zh-CN">一张压缩后很小的照片，解码后仍可能撑满浏览器画布。oMyImage 的 kalp m 在项目文章里记录了按解码后的像素量判断处理路径的做法，并提到 Safari 在超过画布面积限制时可能返回空白。若要把图片编辑功能放到浏览器，先用解码后的宽高评估浏览器路径，再为服务端路径设定独立的输入上限。作者描述的后端只有四个虚拟 CPU，还与另一套工具共享。<a href="https://dev.to/mishrakalpesh9555/image-ai-in-the-browser-or-on-a-cpu-server-what-we-run-where-and-why-53b8">项目原文</a></p>

<p lang="en">A small compressed photo can still overwhelm a browser canvas once decoded. In a write-up about oMyImage, kalp m describes routing images by decoded pixel count and notes that Safari can return a blank canvas above its area limit. To plan browser-based image editing, use the decoded dimensions to decide whether the browser can process an image, then set a separate input limit for server jobs. The project’s backend, as described by the author, shares four virtual CPUs with another set of tools. <a href="https://dev.to/mishrakalpesh9555/image-ai-in-the-browser-or-on-a-cpu-server-what-we-run-where-and-why-53b8">Project write-up</a></p>

<p lang="zh-CN">浏览器内的物体移除还需要让模型文件通过托管平台的部署检查。作者记录的 MI-GAN ONNX 文件为 28,079,181 字节，超过了文中所述的 Cloudflare Pages 单文件 25 MiB 上限。项目把模型拆成两份，浏览器并行拉取并写入同一块预分配缓冲区，再对合并后的完整文件核验 SHA-256。沿用这个设计时，把分片下载、合并和校验完成作为加载模型的前置条件。</p>

<p lang="en">Browser-based object removal also depends on getting the model through the hosting platform’s deployment checks. The MI-GAN ONNX file in the write-up is 28,079,181 bytes, above the 25 MiB single-file limit the author cites for Cloudflare Pages. The project splits the model into two parts, fetches them in parallel into one preallocated buffer, then verifies the SHA-256 of the assembled file. If you adopt the same pattern, make download, assembly, and verification prerequisites for loading the model.</p>

<p lang="zh-CN">格式也可以单独决定处理路径。kalp m 将 HEIC 放到服务端解码，给出的原因是该项目的许可选择。评审自己的方案时，逐项记录格式在哪里解码、像素上限在哪里检查，以及模型通过哪些步骤进入浏览器。浏览器表现和部署细节来自作者记录，本站未运行该项目，也未测量浏览器阈值。</p>

<p lang="en">File format can also determine the processing path. Kalp m attributes server-side HEIC decoding to the project’s licensing choices. When reviewing your own design, record where each format is decoded, where you enforce pixel limits, and how the browser receives the model. The browser behavior and deployment details come from the author’s account. We did not run the project or measure browser limits.</p>
