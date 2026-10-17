---
card_id: claude-code-2026-10-14-a6e2a0
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Agent Mode: 3 changes in v2.1.300 — Added
  `$.ui.view({ agentId })` for mods: shows an agent''s transcript in the main view
  when you…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1196
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 14fe6edc2a802f1bd46b2368eae583bb8dbdc634169863821707bdca83545249
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-a6e2a0
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.300: 3 Agent Mode changes'
  evidence:
  - quote: 'Added `$.ui.view({ agentId })` for mods: shows an agent''s transcript
      in the main view when you ask, and `$.ui.view({})` goes back'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Added support for rewriting a workflow agent's `prompt` and `model` in
      the `agent.spawn` mod hook, which could only refuse workflow agents before
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: Changed the `claude-api` skill to leave Managed Agents sessions in place
      unless you ask to archive or delete them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-agent-mode-changes-in-v2-1-300
  source_release: claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0
  source_type: github_releases
  theme: agent-mode
  title: 3 Agent Mode changes in v2.1.300
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-08-3-agent-mode-changes-in-v2-1-295|3 Agent Mode
  changes in v2.1.295]]'
- '[[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode
  changes in v2.1.296]]'
- '[[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode
  changes in v2.1.299]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0]]'
source_type: github_releases
theme: agent-mode
title: 3 Agent Mode changes in v2.1.300
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in v2.1.300

**Claude Code** · 2026-10-14 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.300) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `$.ui.view({ agentId })` for mods: shows an agent's transcript in the main view when you ask, and `$.ui.view({})` goes back

> Added support for rewriting a workflow agent's `prompt` and `model` in the `agent.spawn` mod hook, which could only refuse workflow agents before

> Changed the `claude-api` skill to leave Managed Agents sessions in place unless you ask to archive or delete them

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]] · Context Window
- [[Changes/Claude Code/2026-10-14-7-apps-and-integrations-changes-in-v2-1-300|7 Apps and Integrations changes in v2.1.300]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added a dir prop on a mod's Text for right-to-left text]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-3-mobile-and-desktop-changes-in-v2-1-300|3 Mobile and Desktop changes in v2.1.300]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-14-improved-the-note-claude-3-models-get-about-an-mentioned-pdf-so-they-less-often|Improved the note Claude 3 models get about an @-mentioned PDF, so they less often…]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-editor-experience-changes-in-v2-1-300|2 Editor Experience changes in v2.1.300]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-changed-exit-to-force-kill-background-commands-still-running-1-5-seconds-after-b|Changed exit to force-kill background commands still running 1.5 seconds after being…]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-claude-tag-added-support-for-slack-voice-clips-in-claude-in-slack-claude-reads-s|Claude Tag Added support for Slack voice clips in Claude in Slack]] · Voice and Audio
- [[Changes/Claude Code/2026-10-14-changed-local-session-transcripts-to-also-record-each-api-request-s-system-promp|Changed local session transcripts to also record each API request's system prompt…]] · Collaboration
- [[Changes/Claude Code/2026-10-14-added-advisor-on-claude-platform-on-aws-no-advisor-runs-until-you-pick-one-with|Added /advisor on Claude Platform on AWS]] · Other changes
- [[Changes/Claude Code/2026-10-14-5-other-changes-in-v2-1-300|5 other changes in v2.1.300]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-a6e2a0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-3-agent-mode-changes-in-v2-1-300.md%0ACard%20ID%3A%20claude-code-2026-10-14-a6e2a0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.300%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->