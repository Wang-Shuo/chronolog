---
card_id: claude-code-2026-05-13-007ea3
date: '2026-05-13'
description: 'Claude Code · 2026-05-13 · Safety and Privacy: 5 changes in v2.1.141
  — Auto mode permission dialog now explains when a `permissions.ask` rule caused
  the prompt'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1123
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8026176549e6d2d80f2c3a229fbd5ccad065b3c444b8e0fd25cb89e654978acb
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-13-007ea3
  comparison: ''
  date: '2026-05-13'
  description: 'Claude Code — v2.1.141: 5 Safety and Privacy changes'
  evidence:
  - quote: Auto mode permission dialog now explains when a `permissions.ask` rule
      caused the prompt
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  - quote: Restored the "view diff in your IDE" option on file-edit permission prompts
      when an IDE is connected
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  - quote: Background agents launched via `/bg` or `←←` now preserve the current permission
      mode instead of reverting to default
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  - quote: Fixed switching permission mode while a tool-permission prompt is open
      not auto-dismissing the prompt when the new setting permits the tool
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  - quote: Fixed pressing Enter while a permission/dialog prompt is open also submitting
      text in the input box
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-safety-and-privacy-changes-in-v2-1-141
  source_release: claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v2.1.141
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added
  sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]]'
- '[[Changes/Claude Code/2026-05-08-2-safety-and-privacy-changes-in-v2-1-136|2 Safety
  and Privacy changes in v2.1.136]]'
- '[[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed
  Skill(name ) permission rules]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v2.1.141
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v2.1.141

**Claude Code** · 2026-05-13 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.141) · from [[Releases/Claude Code/claude-code-2026-05-13-v2-1-141-github-322186176-9f8e2e22|v2.1.141]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Auto mode permission dialog now explains when a `permissions.ask` rule caused the prompt

> Restored the "view diff in your IDE" option on file-edit permission prompts when an IDE is connected

> Background agents launched via `/bg` or `←←` now preserve the current permission mode instead of reverting to default

> Fixed switching permission mode while a tool-permission prompt is open not auto-dismissing the prompt when the new setting permits the tool

> Fixed pressing Enter while a permission/dialog prompt is open also submitting text in the input box

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.141
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-13-2-interface-experience-changes-in-v2-1-141|2 Interface Experience changes in v2.1.141]] · Interface Experience
- [[Changes/Claude Code/2026-05-13-vscode-voice-mode-the-wsl-error-now-suggests-installing-sox-libsox-fmt-pulse-for|VSCode Voice mode]] · Voice and Audio
- [[Changes/Claude Code/2026-05-13-rewind-menu-added-summarize-up-to-here-to-compress-earlier-context-while-keeping|Rewind menu: added "Summarize up to here" to compress earlier context while keeping…]] · Context Window
- [[Changes/Claude Code/2026-05-13-feedback-can-now-include-recent-sessions-last-24-hours-or-7-days-for-issues-span|/feedback can now include recent sessions (last 24 hours or 7 days) for issues…]] · Projects and Workspaces
- [[Changes/Claude Code/2026-05-13-bedrock-awscredentialexport-now-always-runs-when-configured-instead-of-being-ski|Bedrock: awsCredentialExport now always runs when configured instead of being…]] · Account and Access
- [[Changes/Claude Code/2026-05-13-2-apps-and-integrations-changes-in-v2-1-141|2 Apps and Integrations changes in v2.1.141]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-13-4-agent-mode-changes-in-v2-1-141|4 Agent Mode changes in v2.1.141]] · Agent Mode
- [[Changes/Claude Code/2026-05-13-added-anthropic-workspace-id-environment-variable-for-workload-identity-federati|Added ANTHROPIC_WORKSPACE_ID environment variable for workload identity federation]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-11 · Claude Code · [[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed Skill(name ) permission rules]]
- Later: 2026-05-13 · Cursor · [[Changes/Cursor/2026-05-13-environment-governance-and-security-controls|Environment governance and security controls]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-13-007ea3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-13-5-safety-and-privacy-changes-in-v2-1-141.md%0ACard%20ID%3A%20claude-code-2026-05-13-007ea3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.141%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->