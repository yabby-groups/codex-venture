# AI 资源目录验收

## 目录与内容

- 九个栏目共享目录布局，首批收录 14 个独立资源。详情沿用已有文章 URL，资源与相关文章通过稳定 ID 关联。
- Skills 首屏由文章日期列表改为搜索、平台筛选、分类与资源卡片。桌面有筛选侧栏，移动端默认折叠高级筛选。Discover 提供目录入口与资源精选，Learn 提供教程、提示词和工作流入口。
- 开源项目卡片使用已有 GitHub 仓库级快照，展示采集日期。缺少 Stars 的资源排在有数据的资源之后。兼容性、安装方式与许可证按已有证据展示。

## 验收结果

| 检查 | 结果 |
| --- | --- |
| Chromium 视口 | Skills 在 1920、1440、1280、768、390、360 像素的浅色和深色模式通过，无横向溢出 |
| 补充页面 | Plugins、MCP、Tools、Models、Open Source、Prompts、Workflows、Resources、Discover、Learn 在 1440 和 390 像素通过布局检查 |
| 搜索与筛选 | 中英文、平台与分类组合、结果数、URL 恢复、清除、空状态、键盘操作通过 |
| 排序与分页 | 名称和 GitHub Stars 排序通过。隔离环境用 17 个条目验证跨页搜索、分页及无 JavaScript 导航 |
| 资源入口 | 文章跳转、Anthropic 官方链接、Skills 安装命令复制、MCP JSON 配置复制通过 |
| 搜索与元数据 | 浏览器验证 Pagefind 可搜到 Playwright 文章。静态构建验证 158 个 HTML 页的站内链接、结构化数据、RSS 和 Sitemap |
| 自动运营 | 本地编辑器写入试验验证新实体、同 ID 仅更新元数据、拒绝缺少来源的更新 |
| 静态检查 | `npm run check` 与 `npm run build` 通过 |

截图包含重构前生产页面与重构后浏览器截图，随交付单独提供。已打开并检查 Skills 桌面浅色和移动端深色截图。移动端调整了搜索排版，并在首次打开时折叠筛选面板。

## 验收范围

- 复制检查覆盖剪贴板内容。第三方安装和配置执行仍待实测。
- 自动运营使用现有 Codex 调用和预算。本次验证了真实写入器，定时生产流程的下一次资源采集与发布仍待观察。
- 参考审查覆盖 skills.sh、Open VSX、Hugging Face Spaces、GitHub Topics 和 MCP Registry。Raycast 返回访问验证，VS Marketplace 和 Hugging Face Models 加载超时。
- 当前资源样本较少。价格、付费模式、权限、隐私和其他细分属性按已有证据呈现，目录未开放缺少数据支撑的筛选项。
