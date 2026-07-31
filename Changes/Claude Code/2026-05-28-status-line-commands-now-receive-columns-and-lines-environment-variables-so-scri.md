---
card_id: claude-code-2026-05-28-fe5ca3
date: '2026-05-28'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1167
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-27-added-reload-skills-command-to-re-scan-skill-directories-without-restarting-the|claude-code-2026-05-27-8c63c5]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: d4921a29e7b36ba0aa31f10ab7efaeb46f1b5836126d0a913a5fd43e2f757e40
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-21-renamed-simplify-to-code-review-it-now-reports-correctness-bugs-at-a-chosen-effo|claude-code-2026-05-21-b0bdbe]]'
- '[[Changes/Claude Code/2026-05-27-code-review-fix-now-applies-review-findings-to-your-working-tree-after-the-revie|claude-code-2026-05-27-667596]]'
- '[[Changes/Claude Code/2026-05-27-added-reload-skills-command-to-re-scan-skill-directories-without-restarting-the|claude-code-2026-05-27-8c63c5]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-28-v2-1-153-github-330532213-2fa9c18a|claude-code-2026-05-28-v2-1-153-github-330532213-2fa9c18a]]'
theme: developer-workflow
type: change
---

# Status line commands now receive `COLUMNS` and `LINES` environment variables so

<!-- chronolog:begin region="description" -->
Status line commands now receive `COLUMNS` and `LINES` environment variables so scripts can size output to the terminal width
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Status line commands now receive `COLUMNS` and `LINES` environment variables so scripts can size output to the terminal width
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.153
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-27-added-reload-skills-command-to-re-scan-skill-directories-without-restarting-the|claude-code-2026-05-27-8c63c5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1167
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes