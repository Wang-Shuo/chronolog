---
card_id: claude-code-2026-03-17-feecd4
date: '2026-03-17'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1095
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-14-added-worktree-sparsepaths-setting-for-claude-worktree-in-large-monorepos-to-che|claude-code-2026-03-14-d75873]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c520eddf6aac34911c894fcf05a955c07a8114a1aed0c3af748b2b8507e27ea6
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-10-added-exitworktree-tool-to-leave-an-enterworktree-session|claude-code-2026-03-10-e6cb03]]'
- '[[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|claude-code-2026-03-12-e3878f]]'
- '[[Changes/Claude Code/2026-03-14-added-worktree-sparsepaths-setting-for-claude-worktree-in-large-monorepos-to-che|claude-code-2026-03-14-d75873]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721|claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721]]'
theme: developer-workflow
type: change
---

# Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach the

<!-- chronolog:begin region="description" -->
Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach the outer terminal when running inside tmux with `set -g allow-passthrough on`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach the outer terminal when running inside tmux with `set -g allow-passthrough on`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-14-added-worktree-sparsepaths-setting-for-claude-worktree-in-large-monorepos-to-che|claude-code-2026-03-14-d75873]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1095
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes