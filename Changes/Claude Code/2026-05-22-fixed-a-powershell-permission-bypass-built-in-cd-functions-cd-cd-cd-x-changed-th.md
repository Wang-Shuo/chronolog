---
card_id: claude-code-2026-05-22-e2e039
date: '2026-05-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1132
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 7f55b12d81ae848ea5aa4dd9d46368dd5199735b77aacd0445ff80bb296f338a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-22-e2e039
  comparison: ''
  date: '2026-05-22'
  description: 'Claude Code — v2.1.149: Fixed a PowerShell permission bypass: built-in
    `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected,
    letting a later command read outside the workspace'
  evidence:
  - quote: 'Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`,
      `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later
      command read outside the workspace'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.149
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-a-powershell-permission-bypass-built-in-cd-functions-cd-cd-cd-x-changed-th
  source_release: claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: 'Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`,
    `c'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-08-added-settings-automode-hard-deny-for-auto-mode-classifier-rules-that-block-unco|claude-code-2026-05-08-32284a]]'
- '[[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|claude-code-2026-05-14-45e9aa]]'
- '[[Changes/Claude Code/2026-05-15-powershell-tool-now-passes-executionpolicy-bypass-opt-out-with-claude-code-power|claude-code-2026-05-15-e48e4c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f|claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f]]'
source_type: github_releases
theme: safety-privacy
title: 'Fixed a PowerShell permission bypass: built-in cd functions (cd.., cd\, c'
type: change
---

# Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `c

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.149: Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later command read outside the workspace
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later command read outside the workspace
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.149
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1132
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes