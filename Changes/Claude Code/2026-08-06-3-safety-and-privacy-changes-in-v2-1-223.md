---
card_id: claude-code-2026-08-06-f5ae80
date: '2026-08-06'
description: 'Claude Code · 2026-08-06 · Safety and Privacy: 3 changes in v2.1.223
  — Fixed a Bash permission bypass where a crafted command could hide parts of itself
  from…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1208
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d072257fe9ff60019f36719d4da181685c4c051e30812c82c7d9864159f27c03
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-06-f5ae80
  comparison: ''
  date: '2026-08-06'
  description: 'Claude Code — v2.1.223: 3 Safety and Privacy changes'
  evidence:
  - quote: Fixed a Bash permission bypass where a crafted command could hide parts
      of itself from permission checks
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.223
  - quote: Fixed permission prompts so commands padded with tabs or invisible Unicode
      can no longer hide part of the command from the approval dialog
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.223
  - quote: Fixed a permission gap where an agent definition's `bypassPermissions`
      mode ignored the org bypass-permissions disable policy
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.223
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-223
  source_release: claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.223
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety
  and Privacy changes in v2.1.219]]'
- '[[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved
  auto mode safety]]'
- '[[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety
  and Privacy changes in v2.1.221]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d|claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.223
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.223

**Claude Code** · 2026-08-06 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.223) · from [[Releases/Claude Code/claude-code-2026-08-06-v2-1-223-github-365870283-03a5b13d|v2.1.223]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed a Bash permission bypass where a crafted command could hide parts of itself from permission checks

> Fixed permission prompts so commands padded with tabs or invisible Unicode can no longer hide part of the command from the approval dialog

> Fixed a permission gap where an agent definition's `bypassPermissions` mode ignored the org bypass-permissions disable policy

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.223
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-06-2-developer-workflow-changes-in-v2-1-223|2 Developer Workflow changes in v2.1.223]] · Developer Workflow
- [[Changes/Claude Code/2026-08-06-2-context-window-changes-in-v2-1-223|2 Context Window changes in v2.1.223]] · Context Window
- [[Changes/Claude Code/2026-08-06-2-agent-mode-changes-in-v2-1-223|2 Agent Mode changes in v2.1.223]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-04 · Claude Code · [[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety and Privacy changes in v2.1.221]]
- Later: 2026-08-07 · Claude Code · [[Changes/Claude Code/2026-08-07-2-safety-and-privacy-changes-in-v2-1-224|2 Safety and Privacy changes in v2.1.224]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-06-f5ae80&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-06-3-safety-and-privacy-changes-in-v2-1-223.md%0ACard%20ID%3A%20claude-code-2026-08-06-f5ae80%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.223%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->