---
card_id: claude-code-2026-04-01-789bcb
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1081
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|claude-code-2026-04-01-69c505]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: b2314f0c51551f1eff605fa7e89b068faafc0ccfd7f634f754b6e87bd786bc88
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-01-added-husky-to-protected-directories-acceptedits-mode|claude-code-2026-04-01-1f4229]]'
- '[[Changes/Claude Code/2026-04-01-fixed-ui-crash-when-malformed-tool-input-reached-the-permission-dialog|claude-code-2026-04-01-4a94e1]]'
- '[[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|claude-code-2026-04-01-69c505]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
theme: safety-privacy
type: change
---

# Added `"defer"` permission decision to `PreToolUse` hooks — headless sessions ca

<!-- chronolog:begin region="description" -->
Added `"defer"` permission decision to `PreToolUse` hooks — headless sessions can pause at a tool call and resume with `-p --resume` to have the hook re-evaluate
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `"defer"` permission decision to `PreToolUse` hooks — headless sessions can pause at a tool call and resume with `-p --resume` to have the hook re-evaluate
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|claude-code-2026-04-01-69c505]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1081
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes