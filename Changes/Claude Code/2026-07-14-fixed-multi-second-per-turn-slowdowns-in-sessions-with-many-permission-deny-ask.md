---
card_id: claude-code-2026-07-14-df06b4
date: '2026-07-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1185
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-14-improved-auto-mode-the-permission-classifier-now-defaults-to-sonnet-5-for-extern|claude-code-2026-07-14-de216e]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 1a1849318f2e18b4aa8a63578c1c85eb0b136365e89516b848834c4af25fd91e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-11-fixed-compound-commands-with-cd-prompting-for-permission-when-the-only-output-re|claude-code-2026-07-11-4ef412]]'
- '[[Changes/Claude Code/2026-07-11-fixed-remote-managed-settings-from-a-non-interactive-run-claude-p-the-sdk-being|claude-code-2026-07-11-aad6e5]]'
- '[[Changes/Claude Code/2026-07-14-improved-auto-mode-the-permission-classifier-now-defaults-to-sonnet-5-for-extern|claude-code-2026-07-14-de216e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-14-v2-1-208-github-353442054-2756b984|claude-code-2026-07-14-v2-1-208-github-353442054-2756b984]]'
theme: safety-privacy
type: change
---

# Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask

<!-- chronolog:begin region="description" -->
Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask rules — rule matchers are now compiled once and cached
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask rules — rule matchers are now compiled once and cached
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.208
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-14-improved-auto-mode-the-permission-classifier-now-defaults-to-sonnet-5-for-extern|claude-code-2026-07-14-de216e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1185
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes