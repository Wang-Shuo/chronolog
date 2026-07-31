---
card_id: claude-code-2026-03-17-fa1290
date: '2026-03-17'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1066
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-17-fixed-always-allow-on-compound-bash-commands-e-g-cd-src-npm-test-saving-a-single|claude-code-2026-03-17-8c3bdf]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: d37e683a849fde88df4fe62985d8a2e8123a35e3e583e73d8caee18989d49f18
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|claude-code-2026-03-12-bcb8f1]]'
- '[[Changes/Claude Code/2026-03-17-added-allowread-sandbox-filesystem-setting-to-re-allow-read-access-within-denyre|claude-code-2026-03-17-468805]]'
- '[[Changes/Claude Code/2026-03-17-fixed-always-allow-on-compound-bash-commands-e-g-cd-src-npm-test-saving-a-single|claude-code-2026-03-17-8c3bdf]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
theme: safety-privacy
type: change
---

# Fixed PreToolUse hooks returning `"allow"` bypassing `deny` permission rules, in

<!-- chronolog:begin region="description" -->
Fixed PreToolUse hooks returning `"allow"` bypassing `deny` permission rules, including enterprise managed settings
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed PreToolUse hooks returning `"allow"` bypassing `deny` permission rules, including enterprise managed settings
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-17-fixed-always-allow-on-compound-bash-commands-e-g-cd-src-npm-test-saving-a-single|claude-code-2026-03-17-8c3bdf]]
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