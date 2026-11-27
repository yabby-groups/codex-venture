---
category: "coding"
summaryEn: "Papertrail pairs BM25 retrieval with a browser-run FLAN-T5-small model and displays the source passage beside each answer. A fictional handbook gives you a simple way to check both stages."
summaryZh: "Papertrail 用 BM25 检索文档，在浏览器内运行 FLAN-T5-small，并把原文放在回答旁边。用虚构手册里的已知事实，可以分别检查检索和生成。"
tags: ["rag", "javascript", "transformers-js", "bm25"]
titleEn: "Build a browser-based RAG workflow with answers readers can check"
titleZh: "在浏览器里做 RAG，让读者能核对回答原文"
blocks: [{"kind": "notice", "text": {"en": "Papertrail publishes its corpus as corpus.json. Browser-side inference still leaves that file downloadable, so use material you can publish.", "zh": "Papertrail 将语料发布为 corpus.json。即使推理在浏览器内完成，这个文件仍可被下载，因此应使用可以公开的材料。"}, "title": {"en": "The corpus is public", "zh": "语料是公开的"}}]
type: "workflows"
version: "Papertrail architecture documented on 2026-11-26"
verified: "2026-11-27"
status: "current"
tested: false
published: "2026-11-27T10:02:34+08:00"
sources: [{"title": "Building a Browser-Based RAG Application with JavaScript and Hugging Face", "url": "https://dev.to/marymar_danytzacallotico/building-a-browser-based-rag-application-with-javascript-and-hugging-face-3mii"}]
---
<p lang="zh-CN">先用一条只有文档里才有的事实检验检索。Marymar Danytza Calloticona Chambilla 在 Papertrail 的八份虚构手册中写入了支持参考代码 ORBIT-42。询问该代码时，预期结果是界面同时显示代码和包含它的原文段落。这个检查可以分别验证检索是否找到了证据，以及模型是否正确使用了证据。</p>

<p lang="en">Start with a fact that appears only in the documents. Marymar Danytza Calloticona Chambilla put the support reference code ORBIT-42 in Papertrail’s collection of eight fictional handbook documents. When you ask for the code, the expected result is to see both the code and the passage containing it. This checks separately whether retrieval found the evidence and whether the model used it correctly.</p>

<h2><span lang="zh-CN">从 Markdown 到可核对的回答</span><span lang="en">From Markdown to an answer you can check</span></h2>

<p lang="zh-CN">准备一小组可公开的 Markdown 文档，构建时生成 corpus.json。浏览器将文本切分并建立 BM25 索引。收到问题后，把排名最高且满足检索条件的段落与问题一起交给 Web Worker，由 Transformers.js 运行量化的 FLAN-T5-small ONNX 模型。界面保留送入模型的原文，供读者核对。</p>

<p lang="en">Start with a small collection of Markdown documents you can publish and build it into corpus.json. The browser splits the text and builds a BM25 index. For each question, pass the highest-ranked qualifying passage and the question to a Web Worker, where Transformers.js runs a quantized FLAN-T5-small ONNX model. Display the passage supplied to the model so readers can check it.</p>

<p lang="zh-CN">如果回答给错了代码，先看显示的段落。段落里没有代码时，检查文档切分和检索词。段落已经包含代码时，检查提示和生成结果。再用一个手册未覆盖的问题检查弱匹配时的表现。Papertrail 的文档方案以 GitHub Pages 为部署目标，模型文件来自 Hugging Face，推理在浏览器内完成。上述检查是依据作者设计提出的预期，本稿未运行应用。</p>

<p lang="en">If the answer gives the wrong code, inspect the displayed passage first. If the passage lacks the code, check chunking and search terms. If it contains the code, inspect the prompt and generation output. Then try a question outside the handbook to see how the system handles a weak match. Papertrail’s documented deployment targets GitHub Pages, fetches model files from Hugging Face, and runs inference in the browser. These checks describe expected behavior based on the author’s design. The application was not run for this article.</p>
