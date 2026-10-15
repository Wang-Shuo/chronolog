# W1 PR 2 验收记录：卡片、Release 与 Theme 页面模板 — 2026-10-15

**范围：** [设计评审](../design-review-2026-10-15.md) W1 的 U3（Release / Theme 标题与 title 一致）、U4 与 P4（卡片五段式模板、空区域不渲染、移除 Lag Days 等伪精度字段）、C7（Release 摘要与 "Tracked N of M"）、C9（关系链接使用标题）、U8（frontmatter `description`）、P10 的卡片反馈链接，以及首页 / 产品页的主题显示名。本记录对应交付分支 `codex/w1-card-template`；人工批准、合并与部署后才算上线。

- 代码基线：`codex/w1-title-generation` / `1e7be66`（已作为 [PR #7](https://github.com/Wang-Shuo/chronolog/pull/7) 合并为 `main` / `8373f65`）。
- 执行日期与时区：2026-10-15，Asia/Shanghai。实施：Opus 5.5 子 agent；验收：Claude Fable 5.1（受 Wang-Shuo 委托）；最终人工批准：Wang-Shuo。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，`input_kind: replay`，不计入 C1 日常调度。
- 运行 ID：`w1-card-template-20261015-r2`（应用）与 `w1-card-template-20261015-r2-idem`（不应用的幂等复跑）。

## 变更内容

- `_scripts/writer.py`
  - 卡片正文改为六个机器区域：`header`（H1 + 产品 · 日期 · 主题 · 官方来源 · 所属 Release）、`evidence`（官方原文引用）、`context`（同一 Release 的其他变化）、`nearby`（同主题、不同 Release 的前后一条）、`relations`（仅在有 `evolves_from` 或扩散记录时出现，扩散只保留一句“已追踪集合中最早的同主题条目”）、`footer`（预填 card_id 与来源的 GitHub Issue 反馈链接）。移除 `description` 区域、"No evidence-backed evolution relationship assigned."、8 行扩散键值对与空的 `## Editor Notes`。
  - frontmatter 新增机器字段 `description`（产品 · 日期 · 主题：原文，≤ 160 字符），供 Quartz 的 `<meta>` / OG 使用；卡片、Release、Theme 页均有。
  - 骨架迁移：对 change / release / theme 页面，若机器区域之外没有人工文本（只剩旧 H1 与固定小标题），整体替换为新模板；若有人工文本，保留原结构、只替换已有区域，并记录到 `_pipeline/<run-id>/writer-migration-pending.json`（非阻塞，manifest 记录计数）。渲染幂等。
  - Release：H1 为 `{Product} · {Title}`（标题已含产品名时只用标题），摘要优先官方摘要，否则按主题汇总；"Tracked N of M candidate lines."，M 由 `split_release_lines` 计算并以 `candidate_line_count` 持久化在 `record` 中。
  - Theme：H1 与 `title` 使用词表 `display_name`；首页与产品页的主题链接、"Most represented themes" 同样使用显示名；`relation_link` 以目标卡标题作为链接文字。
- `_scripts/common.py`：`load_site`；`_scripts/sources.yaml` 新增 `site.repository`。
- `_scripts/history.py`、`_scripts/pipeline.py`：历史合并保留 `candidate_line_count`；写入阶段传入配置根目录；迁移待办计入 manifest。
- 测试：`tests/test_writer.py`、`tests/test_reliable_pipeline.py` 新增模板、迁移、幂等、Release 标题与计数、显示名、反馈链接、邻近卡片等用例。黄金样本未改。
- 文档：随本 PR 提交 `docs/design-review-2026-10-15.md`、README 指向，以及 PR 1 验收记录的上线补记。

## 复现命令

在交付分支根目录安装 Python/Node 依赖后：

```sh
python -m _scripts.operations --mode generate --apply \
  --run-id w1-card-template-20261015-r2 \
  --output _pipeline/w1-card-template-20261015-r2 \
  --collection docs/acceptance/m3-evidence/live-generation-38668187171/generation/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog --production
python -m _scripts.operations --mode generate \
  --run-id w1-card-template-20261015-r2-idem \
  --output _pipeline/w1-card-template-20261015-r2-idem \
  --collection docs/acceptance/m3-evidence/live-generation-38668187171/generation/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog --production
```

## 验收项与结果

| 项目 | 预期 | 实际 |
| --- | --- | --- |
| `pytest -q` | 全部通过 | 268 passed（PR 1 基线 240） |
| 应用回放 | candidate-applied，0 冲突，0 DLQ | 见 [quality.json](w1-evidence/card-template-r2/quality.json)：2,768 个文件修改（Changes 1,949、Releases 790、Themes 25、Products 3、index 1），tests / vault / build / publication 均 passed；[publication.json](w1-evidence/card-template-r2/publication.json) |
| 幂等复跑 | no-change | 见 [quality.json](w1-evidence/card-template-r2-idem/quality.json)：0 个文件变化，门禁全部通过 |
| 迁移待办 | 0 | 两次运行 `writer_migration_pending` 均为 0，无 pending 文件 |
| 卡片结构 | 六个区域、区域外无文本、H1 等于 title、无 Editor Notes / Lag Days、description ≤ 160 | 1,949 / 1,949 全部满足 |
| 邻近卡片 | 不重复同 Release 卡片 | 3,838 条邻近链接，0 条指向同 Release |
| Release | H1 等于 title、无旧 "Tracked cards:"、`record.candidate_line_count` 存在 | 790 / 790；742 个 `Product · Title`，48 个仅标题；523 个使用官方摘要、267 个使用汇总 |
| Theme | H1 等于 display_name | 25 / 25 |
| 路径与 `card_id` | 不变 | `git diff --name-status` 无非 `M` 项；diff 中 `card_id` 行 0 |

## 已知限制

- "Tracked 3 of 88 candidate lines" 如实暴露了每 Release 最多 5 张卡的采样规则（设计评审 P3，W2 处理）；在此之前它是读者了解覆盖面的必要说明。
- 卡片 H1 现在位于 `header` 机器区域内，直接改 H1 会触发 `machine_hash` 冲突；人工备注应写在最后一个区域之后，标题修正走 `editorial.yaml` / `human_overrides`（策展层）。
- 产品页与首页未做骨架迁移（本 PR 不改其结构）；未发布的 superseded 卡片与禁用产品的旧卡保留旧骨架。
- 同一 Release 内的碎片卡仍以兄弟卡形式并列（P3）。

## 结论

通过。待交付 PR 的最终 head 获人工批准、`quality` 检查成功并合并部署后，再以公共站点校验记为上线。
