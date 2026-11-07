---
card_id: openclaw-2026-10-08-043912
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Agent Mode: 4 changes in v2026.9.9 — Google
  Chat and Slack threads. Google Chat replies stay in their original thread when threading
  is…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1190
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 93488ead8accabbd5b936c36d33cabeab08ce2932b152ee786eea8351c554001
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-043912
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 4 Agent Mode changes'
  evidence:
  - quote: 'Google Chat and Slack threads. Google Chat replies stay in their original
      thread when threading is enabled, even if typing indicators fail. Slack replies
      from CLI-backed agents also retain the originating thread when no other destination
      was requested. Google Chat guidance , Slack thread guidance , #136689 by @ScientificProgrammer
      and @obviyus , with validation by @danieljimz ; #160751 by @maxpuppet and @obviyus
      .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: Claude CLI background replies. A child agent's completed task no longer
      takes the place of its parent's pending reply, allowing the parent to return
      its answer. ed472c0 .
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Tool Search guidance. If an agent tries to use an available direct-only
      tool through Tool Search , the error explains how to call it directly instead
      of sending the agent back to a fruitless search. #161055 by @obviyus , reported
      by @jgs-jeeves .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: Agent-to-agent credentials. An A2A connection rejects a token whose environment
      variable is missing instead of accepting or sending the placeholder text. Supply
      the missing variable and reload or restart OpenClaw to restore the connection.
      521ae23 by @eleqtrizit .
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-agent-mode-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: agent-mode
  title: 4 Agent Mode changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-10-07-2-agent-mode-changes-in-hub-v2-21-1-advanced-search|2
  Agent Mode changes in HUB v2.21.1 — Advanced Search…]]'
- '[[Changes/Claude Code/2026-10-08-4-agent-mode-changes-in-v2-1-295|4 Agent Mode
  changes in v2.1.295]]'
- '[[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent
  Mode changes in rust-v0.162.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: agent-mode
title: 4 Agent Mode changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Google Chat and Slack threads. Google Chat replies stay in their original thread when threading is enabled, even if typing indicators fail. Slack replies from CLI-backed agents also retain the originating thread when no other destination was requested. Google Chat guidance , Slack thread guidance , #136689 by @ScientificProgrammer and @obviyus , with validation by @danieljimz ; #160751 by @maxpuppet and @obviyus .

> Claude CLI background replies. A child agent's completed task no longer takes the place of its parent's pending reply, allowing the parent to return its answer. ed472c0 .

> Tool Search guidance. If an agent tries to use an available direct-only tool through Tool Search , the error explains how to call it directly instead of sending the agent back to a fruitless search. #161055 by @obviyus , reported by @jgs-jeeves .

> Agent-to-agent credentials. An A2A connection rejects a token whose environment variable is missing instead of accepting or sending the placeholder text. Supply the missing variable and reload or restart OpenClaw to restore the connection. 521ae23 by @eleqtrizit .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-08 · Codex CLI · [[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent Mode changes in rust-v0.162.0]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-043912&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-4-agent-mode-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-043912%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->