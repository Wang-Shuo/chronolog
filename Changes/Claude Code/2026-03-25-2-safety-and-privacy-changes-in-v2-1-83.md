---
card_id: claude-code-2026-03-25-aff743
date: '2026-03-25'
description: 'Claude Code · 2026-03-25 · Safety and Privacy: 2 changes in v2.1.83
  — Added `sandbox.failIfUnavailable` setting to exit with an error when sandbox is
  enabled…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1074
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e75cd9db1db8004bc1d0eb08fdf2928926e6b7c07aa0ae0cf38518c162a4847e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-25-aff743
  comparison: ''
  date: '2026-03-25'
  description: 'Claude Code — v2.1.83: 2 Safety and Privacy changes'
  evidence:
  - quote: Added `sandbox.failIfUnavailable` setting to exit with an error when sandbox
      is enabled but cannot start, instead of running unsandboxed
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud
      provider credentials from subprocess environments (Bash tool, hooks, MCP stdio
      servers)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-83
  source_release: claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.83
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety
  and Privacy changes in v2.1.77]]'
- '[[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed
  custom status line showing nothing when workspace trust is blocking it]]'
- '[[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety
  and Privacy changes in v2.1.81]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.83
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.83

**Claude Code** · 2026-03-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.83) · from [[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|v2.1.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `sandbox.failIfUnavailable` setting to exit with an error when sandbox is enabled but cannot start, instead of running unsandboxed

> Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider credentials from subprocess environments (Bash tool, hooks, MCP stdio servers)

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]] · Agent Mode
- [[Changes/Claude Code/2026-03-25-2-interface-experience-changes-in-v2-1-83|2 Interface Experience changes in v2.1.83]] · Interface Experience
- [[Changes/Claude Code/2026-03-25-3-editor-experience-changes-in-v2-1-83|3 Editor Experience changes in v2.1.83]] · Editor Experience
- [[Changes/Claude Code/2026-03-25-3-reliability-and-performance-changes-in-v2-1-83|3 Reliability and Performance changes in v2.1.83]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-25-6-apps-and-integrations-changes-in-v2-1-83|6 Apps and Integrations changes in v2.1.83]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-25-added-managed-settings-d-drop-in-directory-alongside-managed-settings-json-letti|Added managed-settings.d/ drop-in directory alongside managed-settings.json…]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-20 · Claude Code · [[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety and Privacy changes in v2.1.81]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-25-aff743&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-25-2-safety-and-privacy-changes-in-v2-1-83.md%0ACard%20ID%3A%20claude-code-2026-03-25-aff743%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->