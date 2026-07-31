---
card_id: claude-code-2026-03-14-d75873
date: '2026-03-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]'
  lag_days: 1092
  role: follower
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|claude-code-2026-03-12-e3878f]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: ab347d9f238f7acfcfb91e0a6a1e93c5cb57cda6595b09f7cdd168e26b578d45
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-07-added-fmt-comm-cmp-numfmt-expr-test-printf-getconf-seq-tsort-and-pr-to-the-bash|claude-code-2026-03-07-de91e9]]'
- '[[Changes/Claude Code/2026-03-10-added-exitworktree-tool-to-leave-an-enterworktree-session|claude-code-2026-03-10-e6cb03]]'
- '[[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|claude-code-2026-03-12-e3878f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc|claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc]]'
theme: developer-workflow
type: change
---

# Added `worktree.sparsePaths` setting for `claude --worktree` in large monorepos

<!-- chronolog:begin region="description" -->
Added `worktree.sparsePaths` setting for `claude --worktree` in large monorepos to check out only the directories you need via git sparse-checkout
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `worktree.sparsePaths` setting for `claude --worktree` in large monorepos to check out only the directories you need via git sparse-checkout
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|claude-code-2026-03-12-e3878f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: developer-workflow
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-18-built-in-terminal|cursor-2023-03-18-76a713]]
- Lag Days: 1092
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes