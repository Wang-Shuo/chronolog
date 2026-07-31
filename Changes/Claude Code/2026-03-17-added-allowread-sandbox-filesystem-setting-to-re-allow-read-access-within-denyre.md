---
card_id: claude-code-2026-03-17-468805
date: '2026-03-17'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1066
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|claude-code-2026-03-12-bcb8f1]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 54b5bc8d0a99e1734ba4a543b8a4d05ce234f4c42345875962c6830fb0f1117c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|claude-code-2026-03-07-85bd62]]'
- '[[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|claude-code-2026-03-11-933354]]'
- '[[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|claude-code-2026-03-12-bcb8f1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
theme: safety-privacy
type: change
---

# Added `allowRead` sandbox filesystem setting to re-allow read access within `den

<!-- chronolog:begin region="description" -->
Added `allowRead` sandbox filesystem setting to re-allow read access within `denyRead` regions
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `allowRead` sandbox filesystem setting to re-allow read access within `denyRead` regions
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|claude-code-2026-03-12-bcb8f1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1066
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes