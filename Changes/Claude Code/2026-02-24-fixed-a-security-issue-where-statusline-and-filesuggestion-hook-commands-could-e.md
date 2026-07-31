---
card_id: claude-code-2026-02-24-b4a332
date: '2026-02-24'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1045
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-19-permission-suggestions-are-now-populated-when-safety-checks-trigger-an-ask-respo|claude-code-2026-02-19-e3327d]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 36d98f210c5b814ffa8f7eb4da4d7d7a872c1f745efc3dc7533622209e3bb9c7
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-10-fixed-bash-permission-matching-for-commands-using-environment-variable-wrappers|claude-code-2026-02-10-bb3bbc]]'
- '[[Changes/Claude Code/2026-02-13-fixed-permission-wait-time-being-included-in-subagent-elapsed-time-display|claude-code-2026-02-13-b41cef]]'
- '[[Changes/Claude Code/2026-02-19-permission-suggestions-are-now-populated-when-safety-checks-trigger-an-ask-respo|claude-code-2026-02-19-e3327d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c]]'
theme: safety-privacy
type: change
---

# Fixed a security issue where `statusLine` and `fileSuggestion` hook commands cou

<!-- chronolog:begin region="description" -->
Fixed a security issue where `statusLine` and `fileSuggestion` hook commands could execute without workspace trust acceptance in interactive mode.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a security issue where `statusLine` and `fileSuggestion` hook commands could execute without workspace trust acceptance in interactive mode.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-19-permission-suggestions-are-now-populated-when-safety-checks-trigger-an-ask-respo|claude-code-2026-02-19-e3327d]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1045
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes