---
card_id: claude-code-2026-05-21-b0bdbe
date: '2026-05-21'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1160
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-with-an-optional-effort-level-e-g-code-review-hi|claude-code-2026-05-21-796b5a]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 7dbfef51346b7442ff2bfa31bd1088af8e1e7cfecf51851a784e6a7f582a865c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-08-improved-visual-consistency-across-slash-command-dialogs-standardized-footer-hin|claude-code-2026-05-08-c64f98]]'
- '[[Changes/Claude Code/2026-05-15-added-worktree-bgisolation-none-setting-to-let-background-sessions-edit-the-work|claude-code-2026-05-15-85301e]]'
- '[[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-with-an-optional-effort-level-e-g-code-review-hi|claude-code-2026-05-21-796b5a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-21-v2-1-147-github-327133263-73928fcd|claude-code-2026-05-21-v2-1-147-github-327133263-73928fcd]]'
theme: developer-workflow
type: change
---

# Renamed `/simplify` to `/code-review`. It now reports correctness bugs at a chos

<!-- chronolog:begin region="description" -->
Renamed `/simplify` to `/code-review`. It now reports correctness bugs at a chosen effort level (e.g., `/code-review high`); pass `--comment` to post findings as inline GitHub PR comments. The old cleanup-and-fix behavior has been removed
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Renamed `/simplify` to `/code-review`. It now reports correctness bugs at a chosen effort level (e.g., `/code-review high`); pass `--comment` to post findings as inline GitHub PR comments. The old cleanup-and-fix behavior has been removed
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.147
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-with-an-optional-effort-level-e-g-code-review-hi|claude-code-2026-05-21-796b5a]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1160
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes