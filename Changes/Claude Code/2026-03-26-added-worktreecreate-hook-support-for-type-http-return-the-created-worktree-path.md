---
card_id: claude-code-2026-03-26-b1182f
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1104
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|claude-code-2026-03-20-d05f5d]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 49d8e7c88df11f8932387aa541db2be6be18ca66b1d94ff42a40147e6a8c05e2
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|claude-code-2026-03-17-feecd4]]'
- '[[Changes/Claude Code/2026-03-20-resuming-a-session-that-was-in-a-worktree-now-switches-back-to-that-worktree|claude-code-2026-03-20-c20f4f]]'
- '[[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|claude-code-2026-03-20-d05f5d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
theme: developer-workflow
type: change
---

# Added `WorktreeCreate` hook support for `type: "http"` — return the created work

<!-- chronolog:begin region="description" -->
Added `WorktreeCreate` hook support for `type: "http"` — return the created worktree path via `hookSpecificOutput.worktreePath` in the response JSON
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `WorktreeCreate` hook support for `type: "http"` — return the created worktree path via `hookSpecificOutput.worktreePath` in the response JSON
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-20-added-bare-flag-for-scripted-p-calls-skips-hooks-lsp-plugin-sync-and-skill-direc|claude-code-2026-03-20-d05f5d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1104
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes