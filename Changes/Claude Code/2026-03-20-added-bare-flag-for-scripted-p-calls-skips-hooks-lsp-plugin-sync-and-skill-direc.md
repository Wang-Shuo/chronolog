---
card_id: claude-code-2026-03-20-d05f5d
date: '2026-03-20'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1098
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|claude-code-2026-03-20-c20f4f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 1516874563c734c8cbe7ff098af03b912c02324f878dfb366c5ced720312175f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-14-added-worktree-sparsepaths-setting-for-claude-worktree-in-large-monorepos-to-che|claude-code-2026-03-14-d75873]]'
- '[[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|claude-code-2026-03-17-feecd4]]'
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|claude-code-2026-03-20-c20f4f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe|claude-code-2026-03-20-v2-1-81-github-299621655-10d2d4fe]]'
theme: developer-workflow
type: change
---

# Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and

<!-- chronolog:begin region="description" -->
Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `--bare` flag for scripted `-p` calls — skips hooks, LSP, plugin sync, and skill directory walks; requires `ANTHROPIC_API_KEY` or an `apiKeyHelper` via `--settings` (OAuth and keychain auth disabled); auto-memory fully disabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.81
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|claude-code-2026-03-20-c20f4f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1098
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes