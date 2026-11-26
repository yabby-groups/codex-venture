# VPS 自主运营

默认 Compose 项目启动 scheduler、collector、editor 和 publisher。Nginx 只在 `preview` profile 下提供本机静态预览。生产内容由 VPS 推送 GitHub main，Cloudflare 从 main 独立构建。

## 部署

在目标 Linux VPS 上安装 Docker Engine 和 Compose v2。使用同一个 Compose 项目名更新和恢复，以便继续使用原有卷。

```sh
git clone https://github.com/yabby-groups/codex-venture.git
cd codex-venture
cp .env.example .env
mkdir -m 0700 secrets
touch secrets/github_read secrets/github_write secrets/codex_api_key
chmod 0444 secrets/github_read secrets/github_write secrets/codex_api_key
docker compose build
docker compose up -d --wait
docker compose exec -T scheduler venture init
docker compose exec -T scheduler venture doctor
```

通过安全文件传输填入 secrets。Compose 在容器里以 UID 1000 运行。上面的 0700 父目录和 0444 文件适用于 Compose 本地文件挂载，确保容器用户能读文件且宿主其他普通用户无法遍历目录。只读 GitHub token 给 collector。具备该仓库 contents write 权限的发布 token 给 publisher。模型 API key 给 editor。授权的模型、推理参数和预算从现有 Actions 配置复制到 `.env`，权限设为 0600。费用上限开启时，单价配置与币种须覆盖所用模型，历史已耗费用须来自可核对的私有账单。

默认 validation 模式可导入当时的 Hosted 快照并发起真实采集，不调用模型或写 main。生产切换使用新的 Compose 项目名或新的卷，以便从最终快照开始。

```sh
docker compose exec -T scheduler venture import-state origin/venture-state
docker compose exec -T scheduler venture resume
docker compose exec -T scheduler venture run collect
docker compose exec -T scheduler venture queue
docker compose exec -T scheduler venture report
```

## 生产所有权切换

1. 在 VPS 验证四个容器、真实采集、预算配置、工作区权限及挂载的凭据。记录当前 main、公网 release marker、Actions 最后运行与 VPS 镜像版本。
2. 将 GitHub 仓库变量 `VENTURE_OPERATIONS_OWNER` 设为 `vps`，随后禁用 `venture.yml` 调度。检查所有正在排队或运行的旧生产任务，包括调用可复用 workflow 的任务，等待它们结束。排查曾安装的主机 cron。
3. 记录最终 `venture-state` SHA。将私有分析仓库及原托管账单分别做私有归档。运营导入会额外保存整个状态分支树的 tar。将 tar 和 VPS 备份复制到受保护的异机存储。
4. 在生产 Compose 数据卷中导入最终状态 SHA。设置 `VENTURE_MODE=production` 和 `VENTURE_HOSTED_DRAINED=true` 后重新创建容器，确保四个服务都读到同一配置。导入时当天已有 token 和调用计数作为不可覆盖的预算基线。配置费用上限时，可通过 `venture legacy-cost 日期 金额` 导入同币种且覆盖当天托管调用的费用余额依据。缺少该证据时等到北京时间新预算日。
5. 执行 `venture resume`。跟踪采集、模型收据、发布 commit 与验证状态。用连续 72 小时的数据记录四个服务状态、预算、真实新增分类、部署和恢复事件。

```sh
docker compose exec -T scheduler venture import-state origin/venture-state
docker compose up -d --wait --force-recreate
docker compose exec -T scheduler venture resume
docker compose exec -T scheduler venture report
```

把一次 `docker compose exec -T scheduler venture` 简记为以下命令中的 `venture`。

- 浏览队列和来源用 `venture queue`、`venture sources`、`venture budget`。
- 手动加入统一队列用 `venture run collect`、`venture run news`、`venture run practices`、`venture run stories`、`venture run resource-sync`。
- 暂停新领取用 `venture pause`。已经领取的任务完成或等待退出恢复。用 `venture resume` 恢复。
- 重试确定可重放的终止任务用 `venture retry ID`。未知模型结果会保留预留，等待模型侧账单对账。
- `venture backup` 排队生成 SQLite 一致快照、源数据和待恢复发布记录。自动保留最新 14 份运行备份。Docker 日志按服务轮转。
- 恢复前暂停并停止四个容器，保留卷。执行 `docker compose run --rm --no-deps scheduler restore BACKUP_ID`，再执行 `docker compose up -d --wait` 和 `venture doctor`。恢复后为暂停状态，已经产生且会被恢复删除的预算记录会拒绝恢复。

## 更新和回退

更新前生成备份并记下其目录名、当前 Git SHA 与镜像 ID。暂停并等待正在运行的任务退出。执行 `git pull --ff-only`、`docker compose up -d --build --wait`、`venture doctor` 和 `venture resume`。需要回退镜像时先暂停，切回上一版 Git 快照，用相同 Compose 项目和卷重建并检查。涉及状态结构变更时用对应版本的备份恢复。

切回 GitHub Hosted 前暂停 VPS、清空运行中的租约并核对发布恢复队列。归档 VPS SQLite 和状态文件。执行 `venture export-hosted` 生成托管兼容运行状态，包含 VPS 预留和结算过的 token。确认私有账单包含 VPS 已用费用。使用可信工作区和原状态分支父提交，在确认差异与分支兼容后按原 `ops/hosted-state save` 正常快进写入分支。然后停止 VPS 四个服务，删除 GitHub 运营所有权变量并重新启用 `venture.yml`。

## 故障排查

| 观察 | 排查 |
| --- | --- |
| 服务心跳中断 | 用 `docker compose ps` 和 `docker compose logs --tail=100 SERVICE` 检查退出原因、资源上限和健康状态。 |
| 本地请求预算暂停 | `venture sources` 显示窗口和恢复时刻。资源扫描预留新闻请求空间。服务端退避单独处理。 |
| 模型任务显示 blocked | 检查供应商账单、该任务收据和凭据有效性。超时可能已计费，账单未知期间保留额度。 |
| 有 Git SHA，公网尚未通过 | 检查 verify 队列和 Cloudflare 部署记录。Git 拒绝非快进时重新获取 main、重新验收同一结果，避免再次生成。 |
| 长时间无新增 | 检查 report 的内容、来源失败率、候选积压、预算和公网验证状态。 |
| 磁盘紧张 | 检查两个卷、已轮转日志、构建缓存与备份。排队批次和响应直接存在 SQLite 中。只有服务停止并完成备份后才离线清理数据库。 |
