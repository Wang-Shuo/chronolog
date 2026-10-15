# M3 标题符号修复与验收证据归档 — 2026-10-15

**代码修复、内容回放与本地验收已完成；待本次交付 PR 最终 head 人工批准、合并并部署。当前线上仍是 PR #5 的 `0940c9a`，不能把本地通过视为上线。**

## 交付范围

`wiki_label` 曾无条件把 `$` 转成 `USD `，导致官方 API `$.prompt.media`、`$.ui.view` 以及 `$ARGUMENTS` 等标识符失真。现在保留原始 `$`，金额也保持来源写法；原有 wiki 标签的 Markdown、URL 和分隔符清理保持不变。当前 Quartz 未启用数学公式插件，美元符号无需改写。

新增五组参数化回归覆盖 API、Shell 变量、位置参数、命令替换、多个金额、双美元符号和末尾美元符号，分别检查卡片标题、原始 record、卡片与主题链接、Release 标题及链接。

本次将此前尚未提交的首次真实采集、PR #5 人工批准与公开部署验收记录及证据一并纳入版本控制，并同步开发计划和操作手册。历史报告及其摘要保持原样。

## 回放与验证

- 基线：`0940c9a8bd832b8a029e0fa6ea0e988cba45921e`。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，与已审核 PR #5 相同。此次 `input_kind: replay`，没有重新采集或改变来源时间，不计入 C1 日常调度。
- 生成：42 个文件修改，0 新增、0 删除、0 退役；没有 DLQ 或冲突。逐页比较确认仅恢复标题/链接中的 `$`、重新计算 `machine_hash`，允许 YAML 标题自动折行变化；来源 record、其他元数据与正文内容均保留。
- [测试日志](m3-evidence/dollar-title-replay-20261015/tests.log)：**165 passed**；Vault、Quartz、发布集合及 RSS 检查全部通过。
- [发布报告](m3-evidence/dollar-title-replay-20261015/publication.json)：2,768 个活动页面、30 项 RSS；检查 39,448 个 HTML 链接，无损坏图边或未渲染机器 wiki 链接。
- [专项渲染检查](m3-evidence/dollar-title-replay-20261015/dollar-rendering.json)：42 个包含美元标题或链接的活动页面，其 HTML 文档标题与搜索索引匹配；57 个美元 wiki 链接标签实际渲染为锚点，包含 API 与多个金额。比较考虑 Markdown 的 `\$` 转义及弯引号排版，不转换美元符号。
- [归档清单](m3-evidence/dollar-title-replay-20261015/archive.json)提供报告和复核脚本 SHA-256；原始输入包保留在历史归档中，避免重复保存。

在仓库根目录安装 Python/Node 依赖后，可用原始输入复现。输出目录必须不存在；`--apply` 会事务性更新当前 checkout 的生成文件，宜在此修复分支或独立 checkout 中运行：

```sh
python -m _scripts.operations --mode generate --apply \
  --run-id dollar-title-replay-20261015 \
  --output _pipeline/dollar-title-replay-20261015 \
  --collection docs/acceptance/m3-evidence/live-generation-38668187171/generation/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog --production
python docs/acceptance/m3-evidence/dollar-title-replay-20261015/verify_rendering.py
```

## 验收与后续边界

1. 检查本次机器人 PR 的最终 head 与必需 `quality` 成功状态。
2. 人工核对上述 API 与金额标题，确认来源文字、卡片身份和编辑区未变后 Approve。
3. 合并后由既有部署门禁重新构建发布；通过公共 `deployment.json`、索引和 RSS 校验才能记为本修复上线。

C2 首批真实内容审核发布与 C4 公共站点验收已完成。C1 连续七次真实日常调度、C3 部署失败恢复、C5 独立重跑与恢复交接仍待验收，本次不扩展这些事项。
