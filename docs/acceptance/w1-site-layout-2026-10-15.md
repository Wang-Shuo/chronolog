# W1 PR 3 验收记录：站点布局、首页与 About 页 — 2026-10-15

**范围：** [设计评审](../design-review-2026-10-15.md) W1 剩余项：U2（Explorer 过滤、Graph 局部化、页脚）、U1 的页头标语与产品色标变量、U7（浅色链接对比度）、P1 / P8 / P9（首页重排、运维信息迁出首页、待审数字移出首页）、C8（覆盖说明读者化）、C10 术语表、P10 的 RSS 限定。本记录对应交付分支 `codex/w1-site-layout`；人工批准、合并与部署后才算上线。

- 代码基线：`main` / `72fc852`（含 W1 PR 1 [PR #7](https://github.com/Wang-Shuo/chronolog/pull/7) 与 PR 2 [PR #8](https://github.com/Wang-Shuo/chronolog/pull/8)）。
- 执行日期与时区：2026-10-15，Asia/Shanghai。实施：Opus 5.5 子 agent；验收：Claude Fable 5.1（受 Wang-Shuo 委托）；最终人工批准：Wang-Shuo。
- 输入：[运行 38668187171 的原始采集包](m3-evidence/live-generation-38668187171/generation/collection.json.gz)，`input_kind: replay`，不计入 C1 日常调度。
- 运行 ID：`w1-site-20261015`（应用）与 `w1-site-20261015-idem`（不应用的幂等复跑）。

## 变更内容

- **根级页面与管线枚举。** `_scripts/validate.py` 新增 `ROOT_PAGES = ("index.md", "About.md")`；事务文件清单、链接校验、候选复制、构建复制、暂存复制、发布范围允许列表（`rolling_pr.VAULT`）、质量报告分类与发布审计（`tests/manual/check_m2_publication.py`）统一使用。新增测试覆盖每一处枚举。
- **About 页。** `writer.render_about_markdown` 生成根级 `About.md`：简介、来源与覆盖（含完整获取时间、快照说明、已知缺口）、卡片生成方法（含每 Release 最多 5 张的采样规则，常量 `MAX_CARDS_PER_RELEASE` 与代码同步）、审核状态（计数、待审 149、告警 0）、术语表、反馈方式。获取时间行沿用 `Last successful fetch:` / `Official browser snapshot captured:` 原措辞，`quality.normalized_page` 对其去时间戳，保证仅时间变化不会生成日常 PR；有测试证明 About 与产品页在不同时间戳下的归一化输出相同。
- **首页。** 迁移为新骨架：头部（定位语 + 计数 + About 链接）→ Latest changes（以数据中最新卡片日期为锚的 30 天窗口，每产品最多 6 条，余数链接产品页；有告警时置顶）→ Start exploring → Products（发布数、区间、以全局最新发布日为锚的 90 天发布数）→ Themes（按词表 category 分组，显示名与计数）→ About the data（每产品一行读者化覆盖说明，无时间戳）。"Pending theme review" 与 "Alert count" 移至 About。
- **产品页。** `coverage` 区域改为一行读者化摘要（`editorial.render_coverage_summary`）加 About 链接；其余结构未动。Claude Code 的读者链接指向 GitHub Releases 页面而非 API 端点。
- **Quartz。** `quartz.layout.ts`：Explorer 隐藏 Changes / Releases / Alerts / tags 并默认展开；Graph 仅在卡片与主题页渲染；关闭阅读时长；页脚链接 GitHub 仓库、About、RSS；页头改为 `_scripts/site_title.tsx`（标题 + 标语，附带站点样式：隐藏全局图谱按钮、产品色标 CSS 变量）。`quartz.config.ts`：浅色链接色 `#9b6a19` → `#8a5c12`（对比度 4.38:1 → 5.41:1）；关闭内置 RSS，新增 `_scripts/feed.tsx` 只收录卡片与 Release 页（30 条，频道描述固定，无 lastBuildDate 以保持可复现）。`quartz/` 目录不在版本控制内，样式因此放在组件 css 字符串中。
- **测试。** `tests/test_quartz_config.py`（布局与配置断言、对比度计算）、`tests/test_writer.py`（首页窗口与分组、迁移与幂等、About 各区、时间戳稳定性）、`tests/test_operations.py`（枚举、暂存保留人工备注、发布审计）等。黄金样本未改。
- **文档。** `docs/m3-operations.md` 第 2 节补一条说明。

## 复现命令

```sh
python -m _scripts.operations --mode generate --apply \
  --run-id w1-site-20261015 --output _pipeline/w1-site-20261015 \
  --collection docs/acceptance/m3-evidence/live-generation-38668187171/generation/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog --production
python -m _scripts.operations --mode generate \
  --run-id w1-site-20261015-idem --output _pipeline/w1-site-20261015-idem \
  --collection docs/acceptance/m3-evidence/live-generation-38668187171/generation/collection.json.gz \
  --base-url wang-shuo.github.io/chronolog --production
```

## 验收项与结果

| 项目 | 预期 | 实际 |
| --- | --- | --- |
| `pytest -q` | 全部通过 | 289 passed（PR 2 基线 268） |
| 应用回放 | candidate-applied，0 冲突，0 DLQ | 见 [quality.json](w1-evidence/site-layout/quality.json)：新增 `About.md`，修改 `index.md` 与 3 个产品页，Changes / Releases / Themes 均 0；四项门禁 passed；[publication.json](w1-evidence/site-layout/publication.json) |
| 幂等复跑 | no-change | 见 [quality.json](w1-evidence/site-layout-idem/quality.json)：0 变化，门禁全部通过 |
| 仅时间戳变化不开 PR | `normalized_page` 输出一致 | 单元测试覆盖 About 与产品页 |
| 构建站点 | About 页存在并在搜索索引中 | `About.html` 存在，`contentIndex.json` 含 `About`，活动页面 2,769 |
| RSS | 30 条，仅卡片与 Release，频道描述固定 | 符合，见 [index.xml](w1-evidence/site-layout/index.xml)；发布审计通过（链接、guid、日期、活动页面） |
| 首页 | 无待审数字、无获取时间戳、无 Graph、有标语 | 符合 |
| 卡片页 | 有局部 Graph，无阅读时长 | 符合 |
| Explorer | 顶层仅 About / Products / Themes | 序列化的 `filterFn` 对顶层目录求值：Changes、Releases 被隐藏 |
| 链接色对比度 | ≥ 4.5:1 | 浅色 5.41:1；`index.css` 含 `--secondary:#8a5c12` |
| 页脚 | 仓库、About、RSS | 符合 |
| 路径与 `card_id` | 卡片与 Release 不变 | `git diff --name-status` 新增仅 `About.md`、`_scripts/feed.tsx`、`_scripts/site_title.tsx` |

## 已知限制

- 首页 "Latest changes" 仍会显示碎片卡（如 "Available in ChatGPT on mobile and web"），属于 P3（W2）。
- 产品页仍是旧骨架（P6，W2），仅覆盖区域读者化。
- 全局图谱只隐藏了按钮，快捷键仍可打开。
- og-image 与站点图标未替换（U1 剩余项），需要在安装脚本中增加静态资源覆盖，另行处理。
- 未做真实浏览器与移动端截图（U9），布局结论来自构建产物检查。

## 结论

通过。待交付 PR 的最终 head 获人工批准、`quality` 检查成功并合并部署后，再以公共站点校验记为上线。
