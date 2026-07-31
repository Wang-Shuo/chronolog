---
card_id: claude-code-2026-03-12-0c4477
date: '2026-03-12'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat|chatgpt-2023-07-20-4592e6]]'
  lag_days: 966
  role: follower
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-06-reduced-startup-memory-by-426kb-for-users-without-custom-ca-certificates|claude-code-2026-03-06-159dc2]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 0c5e0034967943cbb1735c5ea2a60196987366daa97f9c5e9931052c3b59eb8f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-26-claude-automatically-saves-useful-context-to-auto-memory-manage-with-memory|claude-code-2026-02-26-1aa3a7]]'
- '[[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|claude-code-2026-02-28-29e9b3]]'
- '[[Changes/Claude Code/2026-03-06-reduced-startup-memory-by-426kb-for-users-without-custom-ca-certificates|claude-code-2026-03-06-159dc2]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae|claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae]]'
theme: memory
type: change
---

# Added `autoMemoryDirectory` setting to configure a custom directory for auto-mem

<!-- chronolog:begin region="description" -->
Added `autoMemoryDirectory` setting to configure a custom directory for auto-memory storage
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `autoMemoryDirectory` setting to configure a custom directory for auto-memory storage
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.74
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-06-reduced-startup-memory-by-426kb-for-users-without-custom-ca-certificates|claude-code-2026-03-06-159dc2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: memory
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat|chatgpt-2023-07-20-4592e6]]
- Lag Days: 966
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes