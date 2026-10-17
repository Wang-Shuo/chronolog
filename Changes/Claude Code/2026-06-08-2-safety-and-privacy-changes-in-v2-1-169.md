---
card_id: claude-code-2026-06-08-009926
date: '2026-06-08'
description: 'Claude Code · 2026-06-08 · Safety and Privacy: 2 changes in v2.1.169
  — Added `--safe-mode` flag (and `CLAUDE_CODE_SAFE_MODE`) to start Claude Code with
  all…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1149
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f8506f9bdf85e0f42d6c60cf132274e0822c0de757eec4a1c8032c75f8ec2307
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-08-009926
  comparison: ''
  date: '2026-06-08'
  description: 'Claude Code — v2.1.169: 2 Safety and Privacy changes'
  evidence:
  - quote: Added `--safe-mode` flag (and `CLAUDE_CODE_SAFE_MODE`) to start Claude
      Code with all customizations (CLAUDE.md, plugins, skills, hooks, MCP servers)
      disabled for troubleshooting
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.169
  - quote: Fixed stale permission and dialog prompts reappearing every time you reattached
      to a remote session whose worker had died while waiting on them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.169
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-169
  source_release: claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.169
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-04-fixed-org-managed-permission-rules-not-applying-for-the-entire-session-when-the|Fixed
  org-managed permission rules not applying for the entire session…]]'
- '[[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]]'
- '[[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened
  cross-session messaging]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d|claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.169
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.169

**Claude Code** · 2026-06-08 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.169) · from [[Releases/Claude Code/claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d|v2.1.169]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--safe-mode` flag (and `CLAUDE_CODE_SAFE_MODE`) to start Claude Code with all customizations (CLAUDE.md, plugins, skills, hooks, MCP servers) disabled for troubleshooting

> Fixed stale permission and dialog prompts reappearing every time you reattached to a remote session whose worker had died while waiting on them

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.169
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-08-2-agent-mode-changes-in-v2-1-169|2 Agent Mode changes in v2.1.169]] · Agent Mode
- [[Changes/Claude Code/2026-06-08-2-interface-experience-changes-in-v2-1-169|2 Interface Experience changes in v2.1.169]] · Interface Experience
- [[Changes/Claude Code/2026-06-08-the-claude-md-is-too-long-warning-threshold-now-scales-with-the-model-s-context|The "CLAUDE.md is too long" warning threshold now scales with the model's context window]] · Context Window
- [[Changes/Claude Code/2026-06-08-auto-updater-on-windows-now-stops-retrying-within-a-session-once-claude-exe-is-h|Auto-updater on Windows now stops retrying within a session once claude.exe…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-06-08-background-sessions-now-preserve-ide-chrome-bare-remote-control-and-other-flags|Background sessions now preserve --ide, --chrome, --bare, --remote-control…]] · Editor Experience
- [[Changes/Claude Code/2026-06-08-background-sessions-are-now-told-that-shared-checkout-edits-are-blocked-until-th|Background sessions are now told that shared-checkout edits are blocked until they…]] · Developer Workflow
- [[Changes/Claude Code/2026-06-08-improved-the-error-message-shown-when-your-organization-has-disabled-api-key-aut|Improved the error message shown when your organization has disabled API key…]] · Account and Access
- [[Changes/Claude Code/2026-06-08-workflows-now-opens-immediately-even-while-a-turn-is-in-progress|/workflows now opens immediately even while a turn is in progress]] · Automation and Scheduling
- [[Changes/Claude Code/2026-06-08-added-a-disablebundledskills-setting-and-claude-code-disable-bundled-skills-envi|Added a disableBundledSkills setting and CLAUDE_CODE_DISABLE_BUNDLED_SKILLS…]] · Model Support
- [[Changes/Claude Code/2026-06-08-added-cd-command-to-move-a-session-to-a-new-working-directory-without-breaking-t|Added /cd command to move a session to a new working directory without breaking…]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-06 · Claude Code · [[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened cross-session messaging]]
- Later: 2026-06-10 · Claude Code · [[Changes/Claude Code/2026-06-10-2-safety-and-privacy-changes-in-v2-1-172|2 Safety and Privacy changes in v2.1.172]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-08-009926&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-08-2-safety-and-privacy-changes-in-v2-1-169.md%0ACard%20ID%3A%20claude-code-2026-06-08-009926%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.169%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->