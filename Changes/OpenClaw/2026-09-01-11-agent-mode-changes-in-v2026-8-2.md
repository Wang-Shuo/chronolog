---
card_id: openclaw-2026-09-01-05afc2
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Agent Mode: 11 changes in v2026.8.2 — First-run
  setup now waits for the thing it just configured to become real. Model Setup keeps
  the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1153
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 71ef800a9b596ce3695d5f6abf0292ea5d886d0844f3149e28cad7f0220144dc
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-05afc2
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 11 Agent Mode changes'
  evidence:
  - quote: First-run setup now waits for the thing it just configured to become real.
      Model Setup keeps the chosen model through a reconnect, stays pending until
      the saved settings are active, and shows the actual recovery reason when the
      running Gateway is not ready yet. Guided CLI setup asks for an agent only when
      a step actually belongs to one, keeps that choice through the rest of the flow,
      and lets people add an agent without copying credentials when that is not what
      they want.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: The command surface is simpler around those handoffs too. Manual docking
      and focus commands are gone without compatibility aliases, and /session unbind
      is now the supported way to detach a bound conversation without ending its agent
      session.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: The Home agent can now stay docked beside current Control UI work with
      its normal conversation history, tools, approvals, queue, attachments, and draft-preserving
      handoff to the full page, so asking for help no longer means leaving the thing
      you are working on.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Forwarded messages in the Control UI now show which agent sent them through
      that agent's avatar or stable initials, including in direct conversations where
      the identity used to disappear.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Default sessions also keep the configured agent, transcript, and consultation
      together, generated consultation instructions no longer appear as a second message
      from the user, and later spoken requests can continue after the first exchange.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: The conversation itself carries more of what the person sent and what the
      operator configured. Inline emoji no longer collapse into bare parentheses,
      multi-part replies follow the selected agent's pacing, and configured users,
      groups, and rooms are available when choosing where to send a message.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Skills added after OpenClaw starts are easier to bring into the next turn.
      A new project or workspace .agents/skills directory is detected without restarting
      the Gateway, Windows path casing no longer changes which source a skill belongs
      to, and colon-rich plain text in the approved description , read_when , and
      summary fields remains readable without relaxing structured metadata.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Human approvals and corrections also move ahead of agent-to-agent traffic
      in busy sessions, while Stop catches the selected running and waiting helper-agent
      work beneath the task you chose. Finished helper work that cannot deliver its
      result leaves one recoverable follow-up alert, and messages sent between sessions
      say whether they were queued or added to work already in progress.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: When several agents share one OpenClaw installation, replies, commands,
      tasks, plugins, media, and connected conversations now stay with the agent that
      owns them more consistently. The same ownership follows work into shortened
      conversations, detached reviews, and coding tools, so one agent is less likely
      to answer with another agent's context or permissions.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Unattended work can now find and organize other sessions owned by the same
      agent without extra setup, and connected coding sessions keep same-named work
      separate when different agents resume, control, cancel, or clean it up.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Normal replies also respect how much tool progress each agent is set to
      show, and ordinary requests are less likely to be diverted into an irrelevant
      answer about the current model.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 11-agent-mode-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: agent-mode
  title: 11 Agent Mode changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-08-31-elevenagents|ElevenAgents]]'
- '[[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode
  changes in v2.1.257]]'
- '[[Changes/Codex CLI/2026-09-01-4-agent-mode-changes-in-rust-v0-152-0|4 Agent Mode
  changes in rust-v0.152.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: agent-mode
title: 11 Agent Mode changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Agent Mode changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> First-run setup now waits for the thing it just configured to become real. Model Setup keeps the chosen model through a reconnect, stays pending until the saved settings are active, and shows the actual recovery reason when the running Gateway is not ready yet. Guided CLI setup asks for an agent only when a step actually belongs to one, keeps that choice through the rest of the flow, and lets people add an agent without copying credentials when that is not what they want.

> The command surface is simpler around those handoffs too. Manual docking and focus commands are gone without compatibility aliases, and /session unbind is now the supported way to detach a bound conversation without ending its agent session.

> The Home agent can now stay docked beside current Control UI work with its normal conversation history, tools, approvals, queue, attachments, and draft-preserving handoff to the full page, so asking for help no longer means leaving the thing you are working on.

> Forwarded messages in the Control UI now show which agent sent them through that agent's avatar or stable initials, including in direct conversations where the identity used to disappear.

> Default sessions also keep the configured agent, transcript, and consultation together, generated consultation instructions no longer appear as a second message from the user, and later spoken requests can continue after the first exchange.

> The conversation itself carries more of what the person sent and what the operator configured. Inline emoji no longer collapse into bare parentheses, multi-part replies follow the selected agent's pacing, and configured users, groups, and rooms are available when choosing where to send a message.

> Skills added after OpenClaw starts are easier to bring into the next turn. A new project or workspace .agents/skills directory is detected without restarting the Gateway, Windows path casing no longer changes which source a skill belongs to, and colon-rich plain text in the approved description , read_when , and summary fields remains readable without relaxing structured metadata.

> Human approvals and corrections also move ahead of agent-to-agent traffic in busy sessions, while Stop catches the selected running and waiting helper-agent work beneath the task you chose. Finished helper work that cannot deliver its result leaves one recoverable follow-up alert, and messages sent between sessions say whether they were queued or added to work already in progress.

> When several agents share one OpenClaw installation, replies, commands, tasks, plugins, media, and connected conversations now stay with the agent that owns them more consistently. The same ownership follows work into shortened conversations, detached reviews, and coding tools, so one agent is less likely to answer with another agent's context or permissions.

> Unattended work can now find and organize other sessions owned by the same agent without extra setup, and connected coding sessions keep same-named work separate when different agents resume, control, cancel, or clean it up.

> Normal replies also respect how much tool progress each agent is set to show, and ordinary requests are less likely to be diverted into an irrelevant answer about the current model.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-9-voice-and-audio-changes-in-v2026-8-2|9 Voice and Audio changes in v2026.8.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-01-3-context-window-changes-in-v2026-8-2|3 Context Window changes in v2026.8.2]] · Context Window
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-01-3-mobile-and-desktop-changes-in-v2026-8-2|3 Mobile and Desktop changes in v2026.8.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-01-another-382-changes-in-v2026-8-2-primarily-affect-the-people-who-build-test-docu|Another 382 changes in v2026.8.2 primarily affect the people who build, test…]] · Files and Data
- [[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage and status views now carry cumulative output-token totals through tool calls…]] · Pricing Model
- [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2|9 Apps and Integrations changes in v2026.8.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-01-3-interface-experience-changes-in-v2026-8-2|3 Interface Experience changes in v2026.8.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account and Access changes in v2026.8.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-01 · Codex CLI · [[Changes/Codex CLI/2026-09-01-4-agent-mode-changes-in-rust-v0-152-0|4 Agent Mode changes in rust-v0.152.0]]
- Later: 2026-09-02 · Claude Code · [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-05afc2&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-11-agent-mode-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-05afc2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->