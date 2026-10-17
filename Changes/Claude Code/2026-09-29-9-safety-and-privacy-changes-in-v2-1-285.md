---
card_id: claude-code-2026-09-29-e45c3e
date: '2026-09-29'
description: 'Claude Code · 2026-09-29 · Safety and Privacy: 9 changes in v2.1.285
  — Fixed `claude -p --permission-prompt-tool`: a background subagent''s permission
  request…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1262
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0847ef9141d7bce00e0891cc95ffd19b00b4cd5902c0f9562fb5b3c2b14adfdc
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-29-e45c3e
  comparison: ''
  date: '2026-09-29'
  description: 'Claude Code — v2.1.285: 9 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed `claude -p --permission-prompt-tool`: a background subagent''s permission
      request now goes to the prompt tool instead of being auto-denied'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: 'Fixed fork subagents not keeping the session''s plan mode or `dontAsk`
      mode: a fork now runs under its parent''s permission mode and cannot exit plan
      mode'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Fixed hooks and SDK permission callbacks seeing a missing or outdated plan
      on ExitPlanMode when the plan was written in the same response
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Fixed auto mode skipping its classifier for Artifact tool asset uploads
      and reads of someone else's artifact when you had approved that artifact earlier
      in another permission mode
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Fixed a reply sent from `claude agents` to a background session waiting
      on a permission prompt sometimes approving the pending command
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Improved per-turn performance when many permission deny rules and MCP tools
      are configured
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed the one-time offer to make auto mode your default permission mode
      to also show on third-party providers and with telemetry off, when your user
      settings default to another mode
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed `claude -p` and Python Agent SDK sessions on third-party providers
      or with telemetry off to start in auto mode when no permission mode is configured,
      like interactive sessions; `--permission-mode` still overrides it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  - quote: Changed sandbox settings so project settings cannot widen or turn off an
      admin-required sandbox, replace the proxy behind a managed deny list, extend
      a strict allowlist, or reopen managed read-denies
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-safety-and-privacy-changes-in-v2-1-285
  source_release: claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in v2.1.285
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security
  history in ChatGPT]]'
- '[[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety
  and Privacy changes in v2.1.283]]'
- '[[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety
  and Privacy changes in v2.1.284]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in v2.1.285
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in v2.1.285

**Claude Code** · 2026-09-29 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.285) · from [[Releases/Claude Code/claude-code-2026-09-29-v2-1-285-github-399375132-96b3ffbc|v2.1.285]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed `claude -p --permission-prompt-tool`: a background subagent's permission request now goes to the prompt tool instead of being auto-denied

> Fixed fork subagents not keeping the session's plan mode or `dontAsk` mode: a fork now runs under its parent's permission mode and cannot exit plan mode

> Fixed hooks and SDK permission callbacks seeing a missing or outdated plan on ExitPlanMode when the plan was written in the same response

> Fixed auto mode skipping its classifier for Artifact tool asset uploads and reads of someone else's artifact when you had approved that artifact earlier in another permission mode

> Fixed a reply sent from `claude agents` to a background session waiting on a permission prompt sometimes approving the pending command

> Improved per-turn performance when many permission deny rules and MCP tools are configured

> Changed the one-time offer to make auto mode your default permission mode to also show on third-party providers and with telemetry off, when your user settings default to another mode

> Changed `claude -p` and Python Agent SDK sessions on third-party providers or with telemetry off to start in auto mode when no permission mode is configured, like interactive sessions; `--permission-mode` still overrides it

> Changed sandbox settings so project settings cannot widen or turn off an admin-required sandbox, replace the proxy behind a managed deny list, extend a strict allowlist, or reopen managed read-denies

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.285
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-29-2-context-window-changes-in-v2-1-285|2 Context Window changes in v2.1.285]] · Context Window
- [[Changes/Claude Code/2026-09-29-claude-tag-added-direct-messages-with-claude-for-members-on-an-enterprise-plan-s|Claude Tag Added direct messages with Claude for members on an Enterprise plan…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-29-6-mobile-and-desktop-changes-in-v2-1-285|6 Mobile and Desktop changes in v2.1.285]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-29-improved-responsiveness-when-leaving-the-ctrl-o-transcript-view-in-long-sessions|Improved responsiveness when leaving the ctrl+o transcript view in long sessions…]] · Interface Experience
- [[Changes/Claude Code/2026-09-29-3-model-support-changes-in-v2-1-285|3 Model Support changes in v2.1.285]] · Model Support
- [[Changes/Claude Code/2026-09-29-14-apps-and-integrations-changes-in-v2-1-285|14 Apps and Integrations changes in v2.1.285]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-29-fixed-the-powershell-tool-s-permission-check-skipping-deny-and-ask-rules-and-cac|Fixed the PowerShell tool's permission check skipping deny and ask rules…]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-29-changed-team-and-enterprise-sessions-and-sessions-whose-sign-in-plan-claude-code|Changed Team and Enterprise sessions, and sessions whose sign-in plan Claude Code…]] · Account and Access
- [[Changes/Claude Code/2026-09-29-2-editor-experience-changes-in-v2-1-285|2 Editor Experience changes in v2.1.285]] · Editor Experience
- [[Changes/Claude Code/2026-09-29-2-agent-mode-changes-in-v2-1-285|2 Agent Mode changes in v2.1.285]] · Agent Mode
- [[Changes/Claude Code/2026-09-29-changed-memory-so-that-auto-memory-can-no-longer-be-turned-on-from-a-background|Changed /memory so that Auto-memory can no longer be turned on from a background…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-29-3-developer-workflow-changes-in-v2-1-285|3 Developer Workflow changes in v2.1.285]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]]
- Later: 2026-09-30 · Claude Code · [[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety and Privacy changes in v2.1.286]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-29-e45c3e&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-29-9-safety-and-privacy-changes-in-v2-1-285.md%0ACard%20ID%3A%20claude-code-2026-09-29-e45c3e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.285%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->