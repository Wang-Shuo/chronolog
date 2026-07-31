---
card_id: claude-code-2026-05-15-e48e4c
date: '2026-05-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1125
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|claude-code-2026-05-14-45e9aa]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a63616e1f1d57a7515ff24bedadbacde9b9a343feee95d4d37cc12570061cbf1
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|claude-code-2026-05-07-b75d47]]'
- '[[Changes/Claude Code/2026-05-08-fixed-bash-permission-prompts-showing-an-internal-parser-diagnostic-instead-of-a|claude-code-2026-05-08-05c237]]'
- '[[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|claude-code-2026-05-14-45e9aa]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c]]'
theme: safety-privacy
type: change
---

# PowerShell tool now passes `-ExecutionPolicy Bypass`. Opt out with `CLAUDE_CODE_

<!-- chronolog:begin region="description" -->
PowerShell tool now passes `-ExecutionPolicy Bypass`. Opt out with `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> PowerShell tool now passes `-ExecutionPolicy Bypass`. Opt out with `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|claude-code-2026-05-14-45e9aa]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1125
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes