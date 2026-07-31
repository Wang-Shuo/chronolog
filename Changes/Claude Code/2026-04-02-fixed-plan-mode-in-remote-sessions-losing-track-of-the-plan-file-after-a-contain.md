---
card_id: claude-code-2026-04-02-76e8e8
date: '2026-04-02'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1082
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|claude-code-2026-04-01-789bcb]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 347640f4fa2ad1cddf8fe53db1de7a1ae2204b1d7d46116cae4eed741d19393a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-01-fixed-ui-crash-when-malformed-tool-input-reached-the-permission-dialog|claude-code-2026-04-01-4a94e1]]'
- '[[Changes/Claude Code/2026-04-01-hardened-powershell-tool-permission-checks-fixed-trailing-background-job-bypass|claude-code-2026-04-01-69c505]]'
- '[[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|claude-code-2026-04-01-789bcb]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc|claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc]]'
theme: safety-privacy
type: change
---

# Fixed plan mode in remote sessions losing track of the plan file after a contain

<!-- chronolog:begin region="description" -->
Fixed plan mode in remote sessions losing track of the plan file after a container restart, which caused permission prompts on plan edits and an empty plan-approval modal
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed plan mode in remote sessions losing track of the plan file after a container restart, which caused permission prompts on plan edits and an empty plan-approval modal
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-01-added-defer-permission-decision-to-pretooluse-hooks-headless-sessions-can-pause|claude-code-2026-04-01-789bcb]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1082
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes