---
card_id: claude-code-2026-05-07-b75d47
date: '2026-05-07'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1117
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-06-fixed-permission-mode-flag-being-ignored-when-resuming-a-plan-mode-session-with|claude-code-2026-05-06-ab7de0]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: bd7012b07345ed7ba200f0ce4c4f19bbbd0107d3e4f1d533435a369fe50f1370
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|cursor-2026-05-01-759bfb]]'
- '[[Changes/Claude Code/2026-05-06-fixed-permission-mode-flag-being-ignored-when-resuming-a-plan-mode-session-with|claude-code-2026-05-06-ab7de0]]'
- '[[Changes/ChatGPT/2026-05-07-over-the-coming-weeks-we-ll-be-rolling-out-trusted-contact-an-optional-safety-fe|chatgpt-2026-05-07-d104ca]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|claude-code-2026-05-07-v2-1-133-github-319164825-08653677]]'
theme: safety-privacy
type: change
---

# Added `sandbox.bwrapPath` and `sandbox.socatPath` managed settings (Linux/WSL) t

<!-- chronolog:begin region="description" -->
Added `sandbox.bwrapPath` and `sandbox.socatPath` managed settings (Linux/WSL) to specify custom bubblewrap and socat binary locations
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `sandbox.bwrapPath` and `sandbox.socatPath` managed settings (Linux/WSL) to specify custom bubblewrap and socat binary locations
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-06-fixed-permission-mode-flag-being-ignored-when-resuming-a-plan-mode-session-with|claude-code-2026-05-06-ab7de0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1117
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes