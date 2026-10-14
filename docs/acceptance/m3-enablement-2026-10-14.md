# M3 GitHub 启用记录 — 2026-10-14

用户已指定 [Wang-Shuo/chronolog](https://github.com/Wang-Shuo/chronolog)，并确认使用 GitHub Pages 部署。

## 当前状态

- 已核对：远端为可公开访问的空仓库，尚无分支；本地 `origin` 已连接该仓库。
- 部署目标：GitHub Pages，预期地址 `https://wang-shuo.github.io/chronolog/`，当前未上线。
- 已安装官方 GitHub CLI 2.102.0，并核对官方 SHA-256；尚未登录，待用户完成浏览器授权。
- 工程基线：[M3 本地验收记录](m3-2026-10-13.md)，最新完整 Python 回归 151 项通过。此前的离线、真实失败采集和代码摘要是历史证据，保留原貌。
- 已形成可审阅交付提交 `17f3e73`，分支为 `codex/m3-delivery`；本地 `main` 仍保留 `997692d` 基线。
- 已对 `17f3e73` 使用正式 base URL `wang-shuo.github.io/chronolog` 完成全部本地门禁：151 项测试通过，构建、Vault、2,756 个活动页面及 RSS 30 项均通过。证据：[报告](m3-evidence/github-preflight-20261014/quality.json)、[测试](m3-evidence/github-preflight-20261014/tests.log)、[发布检查](m3-evidence/github-preflight-20261014/publication.json)。这证明本地构建可用，不代表已上线。

## 启用顺序及证据

1. 完成 `gh auth login --hostname github.com --git-protocol https --web --scopes workflow`，核对当前账号及仓库写权限。
2. 将已有本地基线作为远端默认分支，提交 M1–M3 交付至独立分支，创建可审阅 PR；保存提交 SHA、PR URL 和实际 Quality 运行链接。
3. 设置 Pages 来源为 GitHub Actions，设置 `CHRONOLOG_BASE_URL=wang-shuo.github.io/chronolog`，配置 required check 与人工批准规则。
4. 配置生成机器人的身份。当前实现要求 PR 作者与人工批准人不同；个人账号创建的 PR 需要另一名人类批准，机器人创建的 PR 可由仓库所有者批准。不得为首次部署删除最终 head 审核门禁。
5. 合并已审核 PR，验证部署提交、公共页面、索引与 RSS；失败则按[运行手册](../m3-operations.md)恢复并保存结果。
6. 完成真实新增内容批次和连续七次真实日常调度，补齐 C1–C5。

远端权限、Pages 设置、bot secret、PR、Actions 和公共站点均需实际结果证明；当前不标记通过。
