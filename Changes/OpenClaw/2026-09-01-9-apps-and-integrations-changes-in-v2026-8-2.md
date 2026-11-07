---
card_id: openclaw-2026-09-01-b3d385
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Apps and Integrations: 9 changes in v2026.8.2
  — In Discord and Slack , long turns are calmer too, with one stable acknowledgement…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2818
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 441b057b68c61f4b40b0a5e558167c54cd013f9ec4f3a60e9c50b2ab98f5d9ac
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-b3d385
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 9 Apps and Integrations changes'
  evidence:
  - quote: In Discord and Slack , long turns are calmer too, with one stable acknowledgement,
      useful milestones, and prompt approvals or failures instead of a running list
      of every tool action.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Telegram keeps rich-button labels in reply context and keeps its model
      picker usable after a configuration reload, while long WhatsApp replies keep
      their formatting and quote context across split messages. Slack Enterprise Grid
      plugin approvals now stay with the intended workspace from the direct message
      through the approval click.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: That separation carries through the rest of the channel's work. Matrix
      can finish room activity while an account stops or restarts, Doctor preserves
      the supported QQBot multi-account layout, and SMS work stops when its credential
      disappears or is replaced. Messages and actions from an installed channel plugin
      also stay with the plugin the operator selected.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Packaged TypeScript plugins now choose a runnable compiled entry more consistently
      across common build layouts, and file-URL entry points can load and refresh
      through the native loader, including the Windows path that previously failed.
      Exact beta updates keep eligible official plugins aligned with the beta core
      that was actually installed, while explicit selectors and third-party pins stay
      in place and a missing matching artifact remains a visible warning rather than
      proof of alignment.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: A managed update waiting for capability review keeps the previous plugin
      and stops before restarting, while npm failures that produced no output now
      identify the timeout, signal, or exit that ended the command. Published Plugin
      SDK imports and older command categories also remain compatible across the upgrade,
      without bringing retired docking features back.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Plugin repair is more useful when it refuses to guess. Doctor and the registry
      CLI now show which persisted plugin records differ, verify a manual refresh
      before reporting success, and only suggest an exact npm repair target that exists.
      A verified stale linked-plugin record can also be removed after the healthy
      configured-path replacement is confirmed, without weakening uninstall ownership
      checks.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Two trust boundaries remain important. Migrated compatibility allowlists
      preserve bundled providers and explicit denies, but the landed repair retains
      an automated-review concern around mixed eligibility and scoped environment
      propagation. A bundled plugin selected through a configured path also keeps
      its bundled behavior across built and unbuilt states, but ignored dist or node_modules
      descendants beneath a bundled tree may still inherit bundled trust, so this
      release does not establish that nested path boundary as safe.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Several lower-level safeguards now fail earlier and reveal less. Oversized
      MCP responses and events are bounded before parsing, routine diagnostics keep
      ClawDock credentials out, long-secret redaction stays safe within its supported
      size, and optional image components move to patched dependency versions without
      making them mandatory.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Gateway integrations now reject an oversized MCP HTTP response or individual
      SSE event before parsing it, while healthy long-lived streams can continue beyond
      that amount in total. ClawDock inspection keeps credential values and prefixes
      out of ordinary diagnostics, and redaction handles accepted long secrets without
      crashing.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-apps-and-integrations-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 9 Apps and Integrations changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2
  Apps and Integrations changes in v2.1.257]]'
- '[[Changes/Codex CLI/2026-09-01-16-apps-and-integrations-changes-in-rust-v0-152-0|16
  Apps and Integrations changes in rust-v0.152.0]]'
- '[[Changes/Lovable/2026-09-01-connect-a-tool-from-a-pasted-api-key|Connect a tool
  from a pasted API key]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 9 Apps and Integrations changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> In Discord and Slack , long turns are calmer too, with one stable acknowledgement, useful milestones, and prompt approvals or failures instead of a running list of every tool action.

> Telegram keeps rich-button labels in reply context and keeps its model picker usable after a configuration reload, while long WhatsApp replies keep their formatting and quote context across split messages. Slack Enterprise Grid plugin approvals now stay with the intended workspace from the direct message through the approval click.

> That separation carries through the rest of the channel's work. Matrix can finish room activity while an account stops or restarts, Doctor preserves the supported QQBot multi-account layout, and SMS work stops when its credential disappears or is replaced. Messages and actions from an installed channel plugin also stay with the plugin the operator selected.

> Packaged TypeScript plugins now choose a runnable compiled entry more consistently across common build layouts, and file-URL entry points can load and refresh through the native loader, including the Windows path that previously failed. Exact beta updates keep eligible official plugins aligned with the beta core that was actually installed, while explicit selectors and third-party pins stay in place and a missing matching artifact remains a visible warning rather than proof of alignment.

> A managed update waiting for capability review keeps the previous plugin and stops before restarting, while npm failures that produced no output now identify the timeout, signal, or exit that ended the command. Published Plugin SDK imports and older command categories also remain compatible across the upgrade, without bringing retired docking features back.

> Plugin repair is more useful when it refuses to guess. Doctor and the registry CLI now show which persisted plugin records differ, verify a manual refresh before reporting success, and only suggest an exact npm repair target that exists. A verified stale linked-plugin record can also be removed after the healthy configured-path replacement is confirmed, without weakening uninstall ownership checks.

> Two trust boundaries remain important. Migrated compatibility allowlists preserve bundled providers and explicit denies, but the landed repair retains an automated-review concern around mixed eligibility and scoped environment propagation. A bundled plugin selected through a configured path also keeps its bundled behavior across built and unbuilt states, but ignored dist or node_modules descendants beneath a bundled tree may still inherit bundled trust, so this release does not establish that nested path boundary as safe.

> Several lower-level safeguards now fail earlier and reveal less. Oversized MCP responses and events are bounded before parsing, routine diagnostics keep ClawDock credentials out, long-secret redaction stays safe within its supported size, and optional image components move to patched dependency versions without making them mandatory.

> Gateway integrations now reject an oversized MCP HTTP response or individual SSE event before parsing it, while healthy long-lived streams can continue beyond that amount in total. ClawDock inspection keeps credential values and prefixes out of ordinary diagnostics, and redaction handles accepted long secrets without crashing.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-01-9-voice-and-audio-changes-in-v2026-8-2|9 Voice and Audio changes in v2026.8.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-01-3-context-window-changes-in-v2026-8-2|3 Context Window changes in v2026.8.2]] · Context Window
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-01-3-mobile-and-desktop-changes-in-v2026-8-2|3 Mobile and Desktop changes in v2026.8.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-01-another-382-changes-in-v2026-8-2-primarily-affect-the-people-who-build-test-docu|Another 382 changes in v2026.8.2 primarily affect the people who build, test…]] · Files and Data
- [[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage and status views now carry cumulative output-token totals through tool calls…]] · Pricing Model
- [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-01-3-interface-experience-changes-in-v2026-8-2|3 Interface Experience changes in v2026.8.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account and Access changes in v2026.8.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-01 · Lovable · [[Changes/Lovable/2026-09-01-connect-a-tool-from-a-pasted-api-key|Connect a tool from a pasted API key]]
- Later: 2026-09-02 · Claude Code · [[Changes/Claude Code/2026-09-02-5-apps-and-integrations-changes-in-v2-1-259|5 Apps and Integrations changes in v2.1.259]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-b3d385&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-b3d385%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->