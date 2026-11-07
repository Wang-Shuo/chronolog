---
card_id: claude-code-2026-08-25-7640e7
date: '2026-08-25'
description: 'Claude Code · 2026-08-25 · Safety and Privacy: 6 changes in v2.1.246
  — Added an Auto mode tab to `/permissions` for viewing and editing auto mode classifier…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2219
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b48c5e9dbcc824b13ab3ef411c0eab6d8f0885feafcc7c43c2f33a03579244a8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-25-7640e7
  comparison: ''
  date: '2026-08-25'
  description: 'Claude Code — v2.1.246: 6 Safety and Privacy changes'
  evidence:
  - quote: Added an Auto mode tab to `/permissions` for viewing and editing auto mode
      classifier rules
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: Fixed sessions that ended in plan mode resuming outside plan mode in the
      VS Code extension, and in `claude -p --continue`/`--resume` with a permission
      prompt tool, when no permission mode was set
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: Fixed the `Notification` hook not firing while the sandbox "Network request
      outside of sandbox" permission prompt is waiting
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: Fixed Bash permission checks to always require approval for malformed commands
      with a dangling `&&` or `||` operator
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: Fixed MCP tools marked `requiresUserInteraction` still offering "Yes, and
      don't ask again" in their permission prompt; the option wrote an allow rule
      the tool then ignored
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: Changed `claude install` and `claude update` to defer a pending managed-settings
      consent prompt to the next interactive session instead of prompting mid-command
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-246
  source_release: claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.246
  type: change
related_changes:
- '[[Changes/OpenCode/2026-08-21-core-answer-permission-requests-triggered-by-subagents-during-opencode-run|Core
  Answer permission requests triggered by subagents during opencode run]]'
- '[[Changes/Replit/2026-08-21-run-black-box-pen-tests|Run black-box pen tests]]'
- '[[Changes/ElevenLabs/2026-08-24-packages|Packages]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0|claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.246
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.246

**Claude Code** · 2026-08-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.246) · from [[Releases/Claude Code/claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0|v2.1.246]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an Auto mode tab to `/permissions` for viewing and editing auto mode classifier rules

> Fixed sessions that ended in plan mode resuming outside plan mode in the VS Code extension, and in `claude -p --continue`/`--resume` with a permission prompt tool, when no permission mode was set

> Fixed the `Notification` hook not firing while the sandbox "Network request outside of sandbox" permission prompt is waiting

> Fixed Bash permission checks to always require approval for malformed commands with a dangling `&&` or `||` operator

> Fixed MCP tools marked `requiresUserInteraction` still offering "Yes, and don't ask again" in their permission prompt; the option wrote an allow rule the tool then ignored

> Changed `claude install` and `claude update` to defer a pending managed-settings consent prompt to the next interactive session instead of prompting mid-command

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]] · Agent Mode
- [[Changes/Claude Code/2026-08-25-improved-bash-tool-latency-on-bash-shells-by-replaying-snapshot-functions-withou|Improved Bash tool latency on bash shells by replaying snapshot functions without…]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-25-windows-macos-fixed-headless-sessions-not-cleaning-up-stale-entries-in-claude-se|Windows/macOS: Fixed headless sessions not cleaning up stale entries…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-25-added-the-turn-s-completion-time-to-the-end-of-turn-duration-line-e-g-saut-ed-fo|Added the turn's completion time to the end-of-turn duration line…]] · Editor Experience
- [[Changes/Claude Code/2026-08-25-2-developer-workflow-changes-in-v2-1-246|2 Developer Workflow changes in v2.1.246]] · Developer Workflow
- [[Changes/Claude Code/2026-08-25-3-apps-and-integrations-changes-in-v2-1-246|3 Apps and Integrations changes in v2.1.246]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved attribution of usage telemetry to your organization for workload identity…]] · Account and Access
- [[Changes/Claude Code/2026-08-25-goal-changed-idle-sessions-to-start-at-most-three-check-ins-on-long-running-back|/goal: Changed idle sessions to start at most three check-ins on long-running…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-24 · ElevenLabs · [[Changes/ElevenLabs/2026-08-24-packages|Packages]]
- Later: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-16-safety-and-privacy-changes-in-1-17-0|16 Safety and Privacy changes in 1.17.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-25-7640e7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-25-6-safety-and-privacy-changes-in-v2-1-246.md%0ACard%20ID%3A%20claude-code-2026-08-25-7640e7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.246%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->