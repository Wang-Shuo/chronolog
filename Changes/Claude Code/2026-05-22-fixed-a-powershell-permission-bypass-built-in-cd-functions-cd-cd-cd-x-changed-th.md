---
card_id: claude-code-2026-05-22-e2e039
date: '2026-05-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1132
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-15-powershell-tool-now-passes-executionpolicy-bypass-opt-out-with-claude-code-power|claude-code-2026-05-15-e48e4c]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: bde380ae55673efdf50eb1253e343f2e291fc58ee531d28dab76f304fea4eba4
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-08-fixed-bash-permission-prompts-showing-an-internal-parser-diagnostic-instead-of-a|claude-code-2026-05-08-05c237]]'
- '[[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|claude-code-2026-05-14-45e9aa]]'
- '[[Changes/Claude Code/2026-05-15-powershell-tool-now-passes-executionpolicy-bypass-opt-out-with-claude-code-power|claude-code-2026-05-15-e48e4c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f|claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f]]'
theme: safety-privacy
type: change
---

# Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `c

<!-- chronolog:begin region="description" -->
Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later command read outside the workspace
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later command read outside the workspace
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.149
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-15-powershell-tool-now-passes-executionpolicy-bypass-opt-out-with-claude-code-power|claude-code-2026-05-15-e48e4c]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1132
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes