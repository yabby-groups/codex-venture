# 2026-11-28 编辑对照实验

使用生产编辑容器另开一次独立读者审核会话。交替安排原稿为 A、B，向读者审核提供两版全文、一手依据与相关已刊清单。版本全文、审核意见和原始文件的 SHA-256 随本记录保留。

## docling-2152-cancel-pdf

原稿为 A，候选为 B。审核选择 `B`。正式文章采用候选。

- [原稿](docling-2152-cancel-pdf.original.md)
- [候选](docling-2152-cancel-pdf.candidate.md)

### 独立阅读意见

A、B 均为 core，面向维护小型知识库和 RAG 批量导入的开发者。A 的标题准确，首段却把取消、媒体轨道和 MLX 挤在一起，末段的扫描件和表格检查又分散了关注点。B 用“点了取消，队列里的 PDF 还要解析吗？”切入，读者马上得到两项升级验收检查：取消有没有传到转换层，取消后排队项和运行项分别怎么表现。中文有动作感，英文标题略绕，正文两段均易扫读。适合首页短讯。建议把验收写成“让一项先开跑、另一项留在队列，再从应用端取消”，并标注排队项应跳过、运行项只记录观察结果。A actionable=true，B actionable=true。按趣味与点击／实用或启发／新颖／深度／表达与双语／收藏分享计，A 14/16/9/7/7/5＝58，B 19/20/9/9/8/7＝72。

### 版本 A 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。GitHub 发布记录支持北京时间 11 月 23 日、停止转换时取消排队解析、服务端选择默认管线、媒体轨道及 Nemotron 3.5 Parse 的原生 MLX 支持。中英一致。用户取消请求必须传到转换流程，这个前提值得明说。扫描件和表格是建议测试项，稿件没有声称实测或质量提升。已刊 PPTX 图表支持稿是另一项更新。稿件转述并署源，无转载素材、凭据、个人资料或私有指标。

### 版本 B 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。发布说明第 #5456 项支持排队范围，不能用于判断已启动任务的行为。两种语言均把应用层的 Cancel 传递列为检查项，未声称实测。发布日与记录相符。已有 PPTX 稿不覆盖此次变更。发布说明有出处，无转载素材、凭据、个人资料或私有指标。

A SHA-256 `d81e7b12c69fc953f312127d4468853b45b21a36dd63175ec3b42159a6036c90`

B SHA-256 `cc1137837b4b0e8b1349ab00469485662f016e659fec3ace5d3eec0eb4159337`

## uxkin-website-design-copilot-design-md

原稿为 B，候选为 A。审核选择 `B`。正式文章保留原稿。

- [原稿](uxkin-website-design-copilot-design-md.original.md)
- [候选](uxkin-website-design-copilot-design-md.candidate.md)

### 独立阅读意见

A、B 均为 core，面向用 Copilot 制作产品站的独立开发者和创作者。A 的首页与定价页开场有场景，正文随后停在目录描述与版本号，读者看不到文件存哪些规则、由谁消费，两个段落还链向同一份 API 元数据。B 的标题给了具体用途，首段用颜色角色、字体、间距和组件规则说明 DESIGN.md 里有什么，次段给出先审文件、再跨页复用和审查现有页的做法。两种语言信息齐全，第二段略密。适合首页的短篇项目发现。建议在账号限制旁补上技能实际要求的 VS Code 1.109+ 和 GitHub Copilot，以免把免 UXKIN 账号理解为无其他前置条件。A actionable=false，B actionable=true。按六项顺序，A 12/9/7/4/7/3＝42，B 18/19/11/9/8/7＝72。

### 版本 A 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。Open VSX 展示页未取回，注册 API 仍支持 1.0.0、11 月 1 日、声明的引擎范围 ^1.96.0 及发布者对 DESIGN.md、响应式建页和审查的描述。两种语言均说明未验证效果。^1.96.0 是包的声明，README 另列技能需要 VS Code 1.109+ 和 GitHub Copilot。无已刊冲突，转述有归属，无素材转载、凭据或个人信息。

### 版本 B 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。展示页未取回，注册 API 和版本 README 支持发布日期、三项技能、输出到 DESIGN.md 和项目设计令牌、三类屏幕检查，以及免 UXKIN 账号和可选 MCP 搜索需套餐的区别。首页和定价页共用规则是基于文档的应用示例，两版明确写了未运行。无已刊冲突，无参考站素材转载、凭据或个人信息。若补充 MCP 使用建议，应同时说明该服务会收到搜索词。

B SHA-256 `7bce4644de2c695cd962ba09c6d3d02ed383c2de1842b04c49e3a83e6bd674be`

A SHA-256 `ca54146d7f2b585fee89e00fc1838ec707276c41a8b3dfe7f8b0965d0070aeb1`

## pagefind-bilingual-index-fixture

原稿为 A，候选为 B。审核选择 `B`。正式文章采用候选。

- [原稿](pagefind-bilingual-index-fixture.original.md)
- [候选](pagefind-bilingual-index-fixture.candidate.md)

### 独立阅读意见

A、B 均为 core，面向维护双语静态站的独立开发者和创作者。A 开头就给出 HTML lang 和 data-pagefind-body，且保留了“Indexed 2 pages”和元数据路径，但复核命令缺运行目录和依赖说明。B 从“搜索少了一种语言”入手，给出仓库根目录、Node.js、npm、Python 3 和预期的 en、zh-cn，最后把单键失败和双键通过引向不同的下一步。中英正文都短，命令和结果容易找到。适合首页教程位。建议 B 保留 A 的 pagefind/pagefind-entry.json 路径，并把可复核的源码链接固定到执行时所用提交。A actionable=true（教程内容可操作，日期门禁独立未过），B actionable=true。按六项顺序，A 14/18/9/10/8/6＝65，B 18/22/9/11/9/8＝77。

### 版本 A 的核查

truth=false, evidence=false, duplication=true, rights=true, safety=true。探针源码及 11 月 28 日回执支持两页构造、临时目录、Darwin arm64、锁定的 1.6.0、退出码 0 及两个语言键。A 标记 11 月 25 日已验证，现有材料缺该日的执行记录，后一次回执无法核实这项时间主张。上游版本页也未取回。双语实验边界一致。无已刊冲突，公开探针有归属，合成文本和节选输出无凭据、个人资料或私有运营指标。

### 版本 B 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。上游版本页未取回，但探针源码、锁文件材料和 11 月 28 日执行回执直接支持本站实验的版本、平台、命令及结果。两种语言都将结果限定在索引语言覆盖，混排页面的查询仍需验证。无已刊冲突，公开脚本有链接，样本是合成文本，稿件无凭据、个人资料或私有运营指标。

A SHA-256 `4203bab308283ff59a5a0d7c68c0b3690edbf2d63e3a726608be65048befb4c1`

B SHA-256 `128c4a5603e125594cfa26da1d9196d442a89eb9706ed623b252c3bc60225d2e`

## checkmyapp-daily-check-broken-video-links

原稿为 B，候选为 A。审核选择 `neither`。正式文章保留原稿。

- [原稿](checkmyapp-daily-check-broken-video-links.original.md)
- [候选](checkmyapp-daily-check-broken-video-links.candidate.md)

### 独立阅读意见

A、B 均为 core，面向用 coding agent 发布产品、负责验收线上站点的独立开发者。A 的“同一个失效视频被引用两次”和另 30 个可用链接构成可记住的开场，读者能带走两次部署之间也要复查外链的想法。B 用“如何”承诺过程，首句泛泛，正文主要是通用调度和测试账号，末段重复检查结果。两版双语可读，A 更紧凑。按成稿的故事类型，两篇都缺这个站点为何选中该指南及发现后的处置，现有记录只支撑一次发现，首页暂缓。建议补站方或检查负责人的可归属记录，交代选择路径的理由和发现后的决定及结果。若只能用现有材料，可改成公开案例短讯，保留“同一视频、两处 404”，并把哪些页面值得做日检写成编辑建议。A actionable=false，B actionable=false。按六项顺序，A 17/13/9/6/8/5＝58，B 13/12/7/6/7/4＝49。

### 版本 A 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。官网公开案例直接支持同一个 YouTube 视频在两处出现、404 ×2 及另 30 个视频链接可用，也支持所述调度规则。仅能核实服务商公布了这些结果，未见独立检查或修复记录，稿件有归因并保留该边界。英中事实一致，无已刊冲突。正文使用公开站名和已披露统计，无截图转载、私有指标、登录信息或个人资料。

### 版本 B 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。官网支持两处链接 404、另 30 个可用链接、部署后和日常调度，以及登录流程使用测试用户。两种语言都按两处链接计数，容易让人误以为涉及两个视频，原始案例明确只有一个。未有修复记录或总体覆盖率证据，稿件均标为待验证。无已刊冲突，转述可追溯，无转载截图、私有指标、账号凭据或个人资料。

B SHA-256 `821876c00f0c75017c1e9493852c14d57082890370fb6699e8762723f6eb0fb2`

A SHA-256 `349f169b01699f05e485b13f73fdf0470f40cc768c0a7555af681fcde2f77e4e`

## ollama-lm-studio-local-api

原稿为 A，候选为 B。审核选择 `B`。正式文章采用候选。

- [原稿](ollama-lm-studio-local-api.original.md)
- [候选](ollama-lm-studio-local-api.candidate.md)

### 独立阅读意见

A、B 均为 core，面向把现有客户端接入本地模型的开发者和本地推理爱好者。A 有比较表、许可证提醒和流式检查，但把 Ollama 原生 API 与 LM Studio 兼容接口分列后，没有回答同一个 OpenAI 客户端能否试两边，也削弱了“怎么选”的价值。B 首段直接给两端口，接着用同一个短请求验响应解析，需要流式才验分段和结束条件。两边都可用时再依桌面界面或既有原生脚本取舍，把基地址与模型标识配置化也给了具体回退方法。中文标题直接，英文标题略长，正文两种语言节奏清楚。适合首页比较位。建议加一条紧凑的验收条件，注明预先启动服务并选已加载的模型，以客户端能读出回复为通过标准。A actionable=false，B actionable=true。按六项顺序，A 14/14/7/7/7/5＝54，B 19/22/9/11/8/8＝77。

### 版本 A 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。官方文档支持 LM Studio 的本地兼容地址、Ollama 的原生 API、macOS CLI 入口和未实测的资料比较范围。中英一致。两栏的比较口径容易让人误读，Ollama 自己的 API 文档也列出 OpenAI 兼容入口。相关已刊是版本变更、单工具检查或客户端集成，没有相同的迁移判断。官方资料经转述并列源，无凭据、个人信息或私有指标。

### 版本 B 的核查

truth=true, evidence=true, duplication=true, rights=true, safety=true。两套官方文档都支持所列 localhost 地址、模型标识和 POST /v1/chat/completions。逐端点查兼容性符合 Ollama 对支持子集的说明，同一请求是建议的验收方法，稿件没有宣称已经比较过输出或性能。中英一致，无同结论已刊稿。文档有归属，无来源素材转载，建议用无敏感内容的本地请求，无凭据、个人信息或私有指标。

A SHA-256 `87139bae3410436d1aee5260d52d0e69515517c6dde36e30bc275986b57b41a1`

B SHA-256 `f2f1150ab94f55e62cbd6abfb707964e4f58689396c1020f445dd2e9a4185e37`
