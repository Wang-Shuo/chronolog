---
card_id: openclaw-2026-10-08-d1c5f4
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Automation and Scheduling: 2 changes in v2026.9.9
  — Docker startup. Fixed an upgrade loop on affected older Linux hosts that repeatedly…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2577
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 87d8423477dad6fe4e893cd07207eae771f53de6e3d5edd71c28a5c0b8fe5d02
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-d1c5f4
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 2 Automation and Scheduling changes'
  evidence:
  - quote: 'Docker startup. Fixed an upgrade loop on affected older Linux hosts that
      repeatedly rejected an unchanged database. Retries reuse verified rollback backups
      instead of making another full set each time; historical backups remain available.
      See the Docker recovery guidance . #162305 by @steipete , with reports and investigation
      by @Ludwigtheo0815 , @rebarshop-24 and @nweishar .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Windows Gateway discovery. An unreadable launcher belonging to an unrelated
      Windows Scheduled Task no longer blocks Gateway discovery just because that
      task is running. Some custom Gateways launched through a single BAT file can
      still go undetected. #166299 by @RomneyDa , with source work by @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 2-automation-and-scheduling-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 2 Automation and Scheduling changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-10-07-advanced-search-automations-and-grouped-agent-actions|Advanced
  Search, Automations, and grouped agent actions]]'
- '[[Changes/Google Antigravity/2026-10-07-scheduled-tasks-are-now-called-automations-you-can-run-a-scheduled-automation-ri|Scheduled
  Tasks are now called Automations]]'
- '[[Changes/Claude Code/2026-10-08-changed-ctrl-c-at-the-idle-prompt-of-an-attached-background-session-to-leave-a-p|Changed
  Ctrl+C at the idle prompt of an attached background session to leave…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 2 Automation and Scheduling changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Automation and Scheduling changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Docker startup. Fixed an upgrade loop on affected older Linux hosts that repeatedly rejected an unchanged database. Retries reuse verified rollback backups instead of making another full set each time; historical backups remain available. See the Docker recovery guidance . #162305 by @steipete , with reports and investigation by @Ludwigtheo0815 , @rebarshop-24 and @nweishar .

> Windows Gateway discovery. An unreadable launcher belonging to an unrelated Windows Scheduled Task no longer blocks Gateway discovery just because that task is running. Some custom Gateways launched through a single BAT file can still go undetected. #166299 by @RomneyDa , with source work by @steipete .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the|Model retries and context]] · Context Window
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-changed-ctrl-c-at-the-idle-prompt-of-an-attached-background-session-to-leave-a-p|Changed Ctrl+C at the idle prompt of an attached background session to leave…]]
- Later: 2026-10-08 · OpenHands · [[Changes/OpenHands/2026-10-08-2-automation-and-scheduling-changes-in-v1-26-0|2 Automation and Scheduling changes in v1.26.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-d1c5f4&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-d1c5f4%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->