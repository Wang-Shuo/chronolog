---
card_id: claude-code-2026-07-21-7c3261
date: '2026-07-21'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1221
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-19-claude-no-longer-runs-the-verify-and-code-review-skills-on-its-own-invoke-them-w|claude-code-2026-07-19-3944a0]]'
extractor_version: fallback-v2
impact: significant
machine_hash: dff5672c2c4fcff90a04a871908b449c369ad0353cd4e57b2aff234ba4717241
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-10-commit-push-pr-now-auto-allows-git-push-to-the-repo-s-configured-push-remote-rem|claude-code-2026-07-10-6bcc0f]]'
- '[[Changes/Claude Code/2026-07-10-added-directory-path-suggestions-to-cd-matching-add-dir-behavior|claude-code-2026-07-10-e508b3]]'
- '[[Changes/Claude Code/2026-07-19-claude-no-longer-runs-the-verify-and-code-review-skills-on-its-own-invoke-them-w|claude-code-2026-07-19-3944a0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d|claude-code-2026-07-21-v2-1-217-github-357601516-b5c19f5d]]'
theme: developer-workflow
type: change
---

# Improved footer PR badge links to be clickable hyperlinks even when terminal sup

<!-- chronolog:begin region="description" -->
Improved footer PR badge links to be clickable hyperlinks even when terminal support can't be detected (e.g. over ssh/tmux); set `FORCE_HYPERLINK=0` to opt out
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved footer PR badge links to be clickable hyperlinks even when terminal support can't be detected (e.g. over ssh/tmux); set `FORCE_HYPERLINK=0` to opt out
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.217
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-19-claude-no-longer-runs-the-verify-and-code-review-skills-on-its-own-invoke-them-w|claude-code-2026-07-19-3944a0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1221
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes