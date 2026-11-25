---
category: "open-source"
summaryEn: "Ray 2.57.2 backports certificate trust fixes to the 2.57 series, covering Docker images, wheel builds, and virtualenv-based runtime environments. It also updates aiohttp and Brotli to address security issues."
summaryZh: "Ray 2.57.2 为 2.57 系列回补证书信任修复，覆盖 Docker 镜像、wheel 构建和基于 virtualenv 的运行时环境，并更新 aiohttp 和 Brotli 以修复安全问题。"
tags: ["ray", "python", "security"]
titleEn: "Ray 2.57.2 backports certificate trust fixes to the 2.57 series"
titleZh: "Ray 2.57.2 为 2.57 系列回补证书信任修复"
published: "2026-11-25T19:28:24+08:00"
sources: [{"title": "Ray-2.57.2", "url": "https://github.com/ray-project/ray/releases/tag/ray-2.57.2"}]
---
<p lang="zh-CN">Ray 于 2026 年 11 月 24 日发布 2.57.2，把已进入 2.58.2 和 2.59.1 的证书信任修复带回 2.57 系列。Ray 团队在发布说明中称，eMudhra 中间 CA 的密钥于 10 月 20 日被报告泄露。pip 除了使用系统信任库，还信任自带的 certifi 证书包，因此只更新操作系统的 CA 证书无法覆盖 pip 的信任来源。</p>

<p lang="en">Ray released 2.57.2 on November 24, 2026, bringing the certificate trust fixes already shipped in 2.58.2 and 2.59.1 to the 2.57 series. The Ray team says the eMudhra intermediate CA keys were reported compromised on October 20. Because pip also trusts its bundled certifi certificates, updating the operating system’s CA certificates alone leaves part of pip’s trust configuration unaddressed.</p>

<p lang="zh-CN">修复覆盖 Ray 的 Docker 镜像、Windows 和 macOS 的 wheel 构建流程，以及 Ray 通过 virtualenv 创建的运行时环境。该版本还把 <code>ray[default]</code> 的 aiohttp 最低版本提高到 3.14.4，并更新 Docker 镜像及项目固定依赖中的 Brotli。</p>

<p lang="en">The fix covers Ray’s Docker images, its Windows and macOS wheel build pipelines, and runtime environments Ray creates with virtualenv. The release also raises the minimum aiohttp version for <code>ray[default]</code> to 3.14.4 and updates Brotli in the Docker images and Ray’s pinned dependencies.</p>
