---
card_id: cursor-2026-06-04-020531
date: '2026-06-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1145
  role: variant
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Cursor/2026-06-03-teams-are-the-operating-unit-for-a-department-region-or-subsidiary-this-is-what|cursor-2026-06-03-df00e8]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: 4ded14a3975fc0022d384a56c20b45e75b75792ae43a4211448906c1ed660418
product: cursor
product_name: Cursor
related_changes:
- '[[Changes/Claude Code/2026-06-03-claude-agents-json-now-includes-waitingfor-showing-what-a-waiting-session-is-blo|claude-code-2026-06-03-cc3caf]]'
- '[[Changes/Cursor/2026-06-03-enterprise-customers-can-now-manage-multiple-cursor-teams-from-one-place-with-di|cursor-2026-06-03-812ca7]]'
- '[[Changes/Cursor/2026-06-03-teams-are-the-operating-unit-for-a-department-region-or-subsidiary-this-is-what|cursor-2026-06-03-df00e8]]'
source_release: '[[Releases/Cursor/cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856|cursor-2026-06-04-custom-stores-custom-tools-and-auto-review-for-the-cursor-sdk-ht-612f6856]]'
theme: safety-privacy
type: change
---

# You can now hand the local agent your own tools by passing function definitions

<!-- chronolog:begin region="description" -->
You can now hand the local agent your own tools by passing function definitions through local.customTools, on Agent.create() or per send(). The SDK exposes them to the agent through a built-in MCP server called custom-user-tools, so the model calls your code through the same path and the same permission gate as any other MCP tool.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> You can now hand the local agent your own tools by passing function definitions through local.customTools, on Agent.create() or per send(). The SDK exposes them to the agent through a built-in MCP server called custom-user-tools, so the model calls your code through the same path and the same permission gate as any other MCP tool.
>
> Source: https://cursor.com/changelog/sdk-updates-jun-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Cursor/2026-06-03-teams-are-the-operating-unit-for-a-department-region-or-subsidiary-this-is-what|cursor-2026-06-03-df00e8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: variant
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1145
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes