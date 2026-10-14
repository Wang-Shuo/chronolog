# M3 GitHub 启用记录 — 2026-10-14

用户已指定 [Wang-Shuo/chronolog](https://github.com/Wang-Shuo/chronolog)，并确认使用 GitHub Pages 部署。

## 当前状态

- 初次核对远端为空仓库；现已推送 `main` 基线和 `codex/m3-delivery` 交付分支，本地 `origin` 已连接。
- 部署目标：GitHub Pages，预期地址 `https://wang-shuo.github.io/chronolog/`，当前未上线。
- 已安装官方 GitHub CLI 2.102.0，并核对官方 SHA-256；用户已完成授权，核对账号为 `Wang-Shuo`，具有该仓库 admin/push 权限。
- 工程基线：[M3 本地验收记录](m3-2026-10-13.md)，最新完整 Python 回归 151 项通过。此前的离线、真实失败采集和代码摘要是历史证据，保留原貌。
- 已形成可审阅交付提交 `17f3e73`，分支为 `codex/m3-delivery`；`main` 从 `997692d` 基线新增首次设置提交 `9c15d32`，尚未合并内容交付。
- 已对 `17f3e73` 使用正式 base URL `wang-shuo.github.io/chronolog` 完成全部本地门禁：151 项测试通过，构建、Vault、2,756 个活动页面及 RSS 30 项均通过。证据：[报告](m3-evidence/github-preflight-20261014/quality.json)、[测试](m3-evidence/github-preflight-20261014/tests.log)、[发布检查](m3-evidence/github-preflight-20261014/publication.json)。这证明本地构建可用，不代表已上线。
- [初始 PR #1](https://github.com/Wang-Shuo/chronolog/pull/1) 的 [Quality 38558911489](https://github.com/Wang-Shuo/chronolog/actions/runs/38558911489) 已通过；原始 artifact 已下载至[归档目录](m3-evidence/github-quality-38558911489/archive.json)。该次检查基于 head `7bf3392` 的 GitHub 测试合并提交 `eb85dd5`，不代表后续 head 已通过，也不计为日常调度。
- Pages API 已确认 `build_type=workflow`、HTTPS 开启；仓库变量 `CHRONOLOG_BASE_URL=wang-shuo.github.io/chronolog` 已保存。
- `main` 分支保护已启用：要求 `quality` 检查、分支与主分支同步、至少一名批准者、更新撤销旧批准；管理员也受约束，禁止强推和删除。
- 用户明确授权开启仓库级 Actions 创建/批准 PR 设置；API 已确认 `can_approve_pull_request_reviews=true`，默认 workflow 权限保持 `read`。当前建 PR 工作流只创建 PR，不执行批准；部署门禁仍拒绝机器人批准。
- 默认分支的手动 `Open initial delivery PR` 工作流已[运行成功](https://github.com/Wang-Shuo/chronolog/actions/runs/38561392052)，创建[机器人交付 PR #2](https://github.com/Wang-Shuo/chronolog/pull/2)，作者已核对为 `app/github-actions`。原人工账号创建的 PR #1 已关闭保留历史。首次设置提交 `9c15d32` 不包含站点部署。
- PR #2 的最终 head 需要完成 Quality 检查，再由 Wang-Shuo 在 GitHub 批准。后续变更会撤销旧批准；只有最终 head 审核通过并合并，才触发部署。

## 启用顺序及证据

1. 完成 `gh auth login --hostname github.com --git-protocol https --web --scopes workflow`，核对当前账号及仓库写权限。
2. 将已有本地基线作为远端默认分支，提交 M1–M3 交付至独立分支，创建可审阅 PR；保存提交 SHA、PR URL 和实际 Quality 运行链接。
3. 设置 Pages 来源为 GitHub Actions，设置 `CHRONOLOG_BASE_URL=wang-shuo.github.io/chronolog`，配置 required check 与人工批准规则。
4. 配置生成机器人的身份。当前实现要求 PR 作者与人工批准人不同；个人账号创建的 PR 需要另一名人类批准，机器人创建的 PR 可由仓库所有者批准。不得为首次部署删除最终 head 审核门禁。
5. 合并已审核 PR，验证部署提交、公共页面、索引与 RSS；失败则按[运行手册](../m3-operations.md)恢复并保存结果。
6. 完成真实新增内容批次和连续七次真实日常调度，补齐 C1–C5。

Pages 与分支规则已配置，首次远端 CI 已通过，机器人交付 PR 已创建。最终 head 人工批准、合并与公共站点仍待完成；当前不将 M3 整体验收标记通过。首次建 PR 使用临时 `GITHUB_TOKEN`，不等同于日常生成的 `CHRONOLOG_BOT_TOKEN` 已配置；日常生成的 token、快照补充和连续运行仍按运行手册启用并验收。
