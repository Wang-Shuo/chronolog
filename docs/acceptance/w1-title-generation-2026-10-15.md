# W1 PR 1 验收记录：Change Card 标题生成 — 2026-10-15

**范围：** [设计评审](../design-review-2026-10-15.md) W1 的 C1（标题生成）与 U3 的卡片部分（H1 与 title 一致）。本记录对应交付分支 `codex/w1-title-generation`；人工批准、合并与部署后才算上线。

- 代码基线：`main` / `5280419`。
- 执行日期与时区：2026-10-15，Asia/Shanghai。实施：Opus 5.5 子 agent；验收：Claude Fable 5.1（受 Wang-Shuo 委托）；最终人工批准：Wang-Shuo。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，与已上线 PR #5 / #6 相同。`input_kind: replay`，没有重新采集，不计入 C1 日常调度。
- 运行 ID：`w1-title-replay-20261015-r3`（r1、r2 为返工中间结果，已被 r3 从 `origin/main` 内容状态重新生成覆盖）。

## 变更内容

- `_scripts/extract.py`：新增 `card_title(line, product_name)`，替换 `line[:80]` 截断。规则：零宽字符与残留列表序号清理 → 厂商第一人称开头改写为产品主语或祈使句（仅覆盖显式规则：introducing / launching / rolling out / expanding / adding / added / improved…、excited to announce (that)、This release introduces…、You can now、Good news!）→ 取第一句（含 `e.g.`/版本号/域名保护，以及小写或 `)` 后紧跟大写的粘连句切分）→ 超过 90 字符时取冒号或破折号前的短标题（≥ 3 词、≥ 16 字符）→ 仍超长时在 ≤ 84 字符的词边界截断并加 `…`，去掉结尾虚词、未闭合括号/引号、不成对反引号 → 去掉结尾句号或冒号，上限 90 字符。`slug`、`card_id`、`description`、`evidence`、主题与影响等级逻辑不变；`extractor_version` 升为 `fallback-v4`。
- `_scripts/validate.py`：`fallback-v4` 沿用按 Release 作用域的 card_id 校验。
- `_scripts/writer.py`：`refresh_generated_heading`。合并已有卡片文件时，若正文第一个 H1 仍等于旧 `record.title`，替换为新标题；其他 H1 视为人工内容保留，不计冲突。H1 不参与 `machine_hash`。
- 测试：`tests/test_extract.py` 新增 57 组标题参数化用例与身份不变测试；`tests/test_m2_content.py` 新增对 M2 固定采集集全部卡片的可读性约束（≤ 90、无首尾空白、不以 `.`/`:` 结尾、反引号成对、显式规则覆盖的厂商口吻不再出现）；`tests/test_writer.py` 新增 H1 刷新与保留两例。黄金样本文件与阈值未改。
- 内容：按上面的 replay 重新生成，2,771 个文件修改，0 新增、0 退役、0 删除；Changes 1,949、Releases 645、`_review` 149、Themes 25、Products 3。卡片 diff 只涉及 `title`、`record.title`、`extractor_version`、`machine_hash` 与 H1。
- 7 张 ChatGPT 卡片的 H1 在 `origin/main` 上已与 `record.title` 不一致（快照文字更新后 record 重生成而 H1 未更新），回放后用脚本一次性改为当前 `record.title`，并核对 `machine_hash` 仍匹配。

## 复现命令

在交付分支根目录安装 Python/Node 依赖后，先把生成内容恢复到基线，再回放：

```sh
git checkout origin/main -- Changes Releases Products Themes _review index.md
python -m _scripts.operations --mode generate --apply \
  --run-id w1-title-replay-20261015-r3 \
  --output _pipeline/w1-title-replay-20261015-r3 \
  --collection docs/acceptance/m3-evidence/live-generation-38668187171/generation/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog --production
```

## 验收项与结果

| 项目 | 预期 | 实际 |
| --- | --- | --- |
| 词中硬截断的标题 | 0 | 0（基线 967，49.6%） |
| 标题 ≥ 78 字符 | 明显下降；完整句允许到 90 | 876（45%；基线 1,348，69%）。其中 912 条（47%）以 `…` 结尾，均在词边界 |
| 显式规则覆盖的厂商口吻开头 | 0 | 0；其余无规则的第一人称开头剩 64 条（3.3%），留待策展 |
| 最长标题 | ≤ 90 | 90 |
| 卡片 H1 等于 `# ` + `record.title` | 1,949 / 1,949 | 1,949 / 1,949 |
| 文件路径、`card_id` | 不变 | `git diff --name-status` 无非 `M` 项；diff 中 `card_id` 行 0 |
| `pytest -q` | 全部通过 | 240 passed（基线 165） |
| 回放门禁 | candidate-applied，0 冲突，0 DLQ | 见 [quality.json](w1-evidence/title-replay-r3/quality.json)：tests / vault / build / publication 均 passed；[publication.json](w1-evidence/title-replay-r3/publication.json)：2,768 个活动页面、30 项 RSS；[vault-validation.json](w1-evidence/title-replay-r3/vault-validation.json)：0 errors |
| 线上效果抽查 | `<title>`、og:title 与 H1 一致 | 构建产物中 Cursor Projects 卡片三者均为 "Cursor launches Projects" |

## 已知限制

- 64 条标题仍为厂商第一人称（"We're making…"、"We're updating…" 等），未做机械改写以避免语法错误；按 C1 策展层处理。
- 39 条改写后的标题重复出现产品名（"ChatGPT expands availability of the ChatGPT app…"），语义正确，不处理。
- 冒号短标题使同一产品内同名标题从 31 增至 37（如 "Improved auto mode" ×4）；列表中有日期区分，接受。
- 2 条标题仍有大写字母前的粘连句（"…in ChatGPT.This applies…"），规则刻意不覆盖大写前缀。
- `description` 与正文仍重复展示引用（C2），卡片正文模板在 W1 PR 2 处理。

## 结论

通过。待交付 PR 的最终 head 获人工批准、`quality` 检查成功并合并部署后，再以公共站点校验记为上线。

## 上线记录（2026-10-15 补记）

- 交付 PR：[PR #7](https://github.com/Wang-Shuo/chronolog/pull/7)，由 Actions 机器人创建；Wang-Shuo 批准最终 head `1e7be66`，合并提交 `8373f65`。
- 检查：dispatch 的 Quality 运行 38687640803 成功；`pull_request` 事件的运行 38687642080 因机器人创建 PR 而处于 action_required，经 API 批准后同样成功，合并状态转为 CLEAN。
- 部署：运行 38691323314 的 build 与 deploy 均成功；公开 `deployment.json` 的 `commit` 为 `8373f6502c94239c04566adac3be6bc086ff66a4`，`built_at` 2026-10-15T06:16:30Z。抽查 Cursor Projects 卡片页 `<title>` 为 "Cursor launches Projects"，`Themes/agent-mode` 时间线显示新标题。
- 结论：已上线。
