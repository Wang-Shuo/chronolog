---
card_id: claude-code-2026-04-01-69c505
date: '2026-04-01'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1081
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-01-fixed-ui-crash-when-malformed-tool-input-reached-the-permission-dialog|claude-code-2026-04-01-4a94e1]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a72addaadeda7ebb74066aa706267b427d66fcbb9fef9e434ef012fce443c06d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|claude-code-2026-03-27-6bd5a2]]'
- '[[Changes/Claude Code/2026-04-01-added-husky-to-protected-directories-acceptedits-mode|claude-code-2026-04-01-1f4229]]'
- '[[Changes/Claude Code/2026-04-01-fixed-ui-crash-when-malformed-tool-input-reached-the-permission-dialog|claude-code-2026-04-01-4a94e1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b|claude-code-2026-04-01-v2-1-90-github-304453197-996aad1b]]'
theme: safety-privacy
type: change
---

# Hardened PowerShell tool permission checks: fixed trailing `&` background job by

<!-- chronolog:begin region="description" -->
Hardened PowerShell tool permission checks: fixed trailing `&` background job bypass, `-ErrorAction Break` debugger hang, archive-extraction TOCTOU, and parse-fail fallback deny-rule degradation
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Hardened PowerShell tool permission checks: fixed trailing `&` background job bypass, `-ErrorAction Break` debugger hang, archive-extraction TOCTOU, and parse-fail fallback deny-rule degradation
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.90
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-01-fixed-ui-crash-when-malformed-tool-input-reached-the-permission-dialog|claude-code-2026-04-01-4a94e1]]
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