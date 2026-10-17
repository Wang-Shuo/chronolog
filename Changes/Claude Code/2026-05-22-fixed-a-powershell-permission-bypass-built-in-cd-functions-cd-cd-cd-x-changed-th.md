---
card_id: claude-code-2026-05-22-e2e039
date: '2026-05-22'
description: 'Claude Code · 2026-05-22 · Safety and Privacy: Fixed a PowerShell permission
  bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1132
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: ef6e6b608d814112f15c96c0cc39849088a634df670708f4d75257cb1cde36cc
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
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-a-powershell-permission-bypass-built-in-cd-functions-cd-cd-cd-x-changed-th
  source_release: claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed a PowerShell permission bypass
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-08-added-settings-automode-hard-deny-for-auto-mode-classifier-rules-that-block-unco|Added
  settings.autoMode.hard_deny for auto mode classifier rules that block…]]'
- '[[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|Added
  new claude agents flags]]'
- '[[Changes/Claude Code/2026-05-15-powershell-tool-now-passes-executionpolicy-bypass-opt-out-with-claude-code-power|PowerShell
  tool now passes -ExecutionPolicy Bypass]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f|claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f]]'
source_type: github_releases
superseded: true
theme: safety-privacy
title: Fixed a PowerShell permission bypass
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed a PowerShell permission bypass

**Claude Code** · 2026-05-22 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.149) · from [[Releases/Claude Code/claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f|v2.1.149]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later command read outside the workspace
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.149
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-22-markdown-output-now-renders-gfm-task-list-checkboxes-todo-x-done-instead-of-plai|Markdown output now renders GFM task list checkboxes (-   todo / - x done)…]] · Interface Experience
- [[Changes/Claude Code/2026-05-22-usage-now-shows-a-per-category-breakdown-of-what-s-driving-your-limits-usage-ski|/usage now shows a per-category breakdown of what's driving your limits usage]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-22-diff-detail-view-can-now-be-scrolled-with-the-keyboard-arrows-j-k-pgup-pgdn-spac|/diff detail view can now be scrolled with the keyboard…]] · Editor Experience
- [[Changes/Claude Code/2026-05-22-enterprise-added-the-allowallclaudeaimcps-managed-setting-to-load-claude-ai-clou|Enterprise: added the allowAllClaudeAiMcps managed setting to load claude.ai cloud…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-15 · Claude Code · [[Changes/Claude Code/2026-05-15-powershell-tool-now-passes-executionpolicy-bypass-opt-out-with-claude-code-power|PowerShell tool now passes -ExecutionPolicy Bypass]]
- Later: 2026-05-29 · Cursor · [[Changes/Cursor/2026-05-29-auto-review-applies-to-shell-mcp-and-fetch-tool-calls-allowlisted-calls-run-imme|Auto-review applies to Shell, MCP, and Fetch tool calls]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-22-e2e039&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-22-fixed-a-powershell-permission-bypass-built-in-cd-functions-cd-cd-cd-x-changed-th.md%0ACard%20ID%3A%20claude-code-2026-05-22-e2e039%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.149%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->