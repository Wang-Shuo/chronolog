---
card_id: claude-code-2026-05-07-6fb4d0
date: '2026-05-07'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1146
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-06-added-claude-code-package-manager-auto-update-when-set-on-homebrew-or-winget-ins|claude-code-2026-05-06-3f1ca0]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 0306a947d2e4d930d0eaa5f8f7f61c6a8f6edbac7cc2bb9d2f16bd1803570ec0
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-23-added-prurltemplate-setting-to-point-the-footer-pr-badge-at-a-custom-code-review|claude-code-2026-04-23-cf1efd]]'
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|claude-code-2026-04-28-33dc91]]'
- '[[Changes/Claude Code/2026-05-06-added-claude-code-package-manager-auto-update-when-set-on-homebrew-or-winget-ins|claude-code-2026-05-06-3f1ca0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|claude-code-2026-05-07-v2-1-133-github-319164825-08653677]]'
theme: developer-workflow
type: change
---

# Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktre

<!-- chronolog:begin region="description" -->
Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`'s base back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed commits in new worktrees
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`'s base back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed commits in new worktrees
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-06-added-claude-code-package-manager-auto-update-when-set-on-homebrew-or-winget-ins|claude-code-2026-05-06-3f1ca0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1146
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes