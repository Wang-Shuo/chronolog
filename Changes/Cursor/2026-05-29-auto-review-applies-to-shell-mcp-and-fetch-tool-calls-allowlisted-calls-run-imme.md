---
card_id: cursor-2026-05-29-e786d9
date: '2026-05-29'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1139
  role: variant
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|cursor-2026-05-01-759bfb]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: a88708b765c2b7e94a2faf66ef125b5630931837c80e7eaa8c385fc8163d9f11
product: cursor
product_name: Cursor
related_changes:
- '[[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|claude-code-2026-05-14-45e9aa]]'
- '[[Changes/Claude Code/2026-05-15-powershell-tool-now-passes-executionpolicy-bypass-opt-out-with-claude-code-power|claude-code-2026-05-15-e48e4c]]'
- '[[Changes/Claude Code/2026-05-22-fixed-a-powershell-permission-bypass-built-in-cd-functions-cd-cd-cd-x-changed-th|claude-code-2026-05-22-e2e039]]'
source_release: '[[Releases/Cursor/cursor-2026-05-29-3-6-https-cursor-com-changelog-auto-review-c5d7c919|cursor-2026-05-29-3-6-https-cursor-com-changelog-auto-review-c5d7c919]]'
theme: safety-privacy
type: change
---

# Auto-review applies to Shell, MCP, and Fetch tool calls. Allowlisted calls run i

<!-- chronolog:begin region="description" -->
Auto-review applies to Shell, MCP, and Fetch tool calls. Allowlisted calls run immediately, and calls that can be sandboxed run in the sandbox. All other agent actions go to a classifier subagent that decides whether to allow the call, try a different approach, or ask for your approval.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Auto-review applies to Shell, MCP, and Fetch tool calls. Allowlisted calls run immediately, and calls that can be sandboxed run in the sandbox. All other agent actions go to a classifier subagent that decides whether to allow the call, try a different approach, or ask for your approval.
>
> Source: https://cursor.com/changelog/auto-review
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|cursor-2026-05-01-759bfb]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: variant
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1139
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes