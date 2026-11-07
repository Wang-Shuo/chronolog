---
card_id: openclaw-2026-09-30-cbbe36
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Pricing Model: 3 changes in v2026.9.7 — On Windows,
  the installer reports failure if the terminal still cannot find OpenClaw. Open a…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3003
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e2ae3b4f9b443919a9635837fb0b9b91fed8c08a4cf749543425448c9345c676
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-cbbe36
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 3 Pricing Model changes'
  evidence:
  - quote: On Windows, the installer reports failure if the terminal still cannot
      find OpenClaw. Open a new terminal and run openclaw doctor as advised. For Windows
      source checkouts running under Bun, a startup fix lets OpenClaw open its databases
      and save device tokens. The FreeBSD installation guide explains the missing
      native Codex binary and the OpenAI API alternative, which requires an API key
      and explicit OpenClaw runtime selection. API usage is billed separately from
      a ChatGPT or Codex subscription. Administrators can also follow a new team server
      deployment guide .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Anthropic connections handle stored subscription credentials and custom
      beta settings more consistently, avoiding related request failures. Prompt caching
      also follows the provider's context settings, and rewinding no longer changes
      an otherwise identical prompt unnecessarily.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: New Fireworks setups use GLM 5.3 Fast instead of the retired GLM 5.2 Fast.
      If you saved the old model, choose a replacement yourself. The bundled cached-input
      cost estimate rises from $0.21 to $0.39 per million tokens.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-pricing-model-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: pricing-model
  title: 3 Pricing Model changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-29-claude-tag-added-direct-messages-with-claude-for-members-on-an-enterprise-plan-s|Claude
  Tag Added direct messages with Claude for members on an Enterprise plan…]]'
- '[[Changes/v0/2026-09-29-chatgpt-plus-and-pro-subscribers-can-now-use-their-chatgpt-subscription-to-build|ChatGPT
  Plus and Pro subscribers can now use their ChatGPT subscription to build in v0]]'
- '[[Changes/v0/2026-09-29-what-happens-if-i-reach-my-chatgpt-usage-limit|What happens
  if I reach my ChatGPT usage limit?]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: pricing-model
title: 3 Pricing Model changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Pricing Model changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> On Windows, the installer reports failure if the terminal still cannot find OpenClaw. Open a new terminal and run openclaw doctor as advised. For Windows source checkouts running under Bun, a startup fix lets OpenClaw open its databases and save device tokens. The FreeBSD installation guide explains the missing native Codex binary and the OpenAI API alternative, which requires an API key and explicit OpenClaw runtime selection. API usage is billed separately from a ChatGPT or Codex subscription. Administrators can also follow a new team server deployment guide .

> Anthropic connections handle stored subscription credentials and custom beta settings more consistently, avoiding related request failures. Prompt caching also follows the provider's context settings, and rewinding no longer changes an otherwise identical prompt unnecessarily.

> New Fireworks setups use GLM 5.3 Fast instead of the retired GLM 5.2 Fast. If you saved the old model, choose a replacement yourself. The bundled cached-input cost estimate rises from $0.21 to $0.39 per million tokens.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-09-29 · v0 · [[Changes/v0/2026-09-29-what-happens-if-i-reach-my-chatgpt-usage-limit|What happens if I reach my ChatGPT usage limit?]]
- Later: 2026-10-01 · Codex CLI · [[Changes/Codex CLI/2026-10-01-49079-update-and-centralize-tui-subscription-labels-etraut-openai|♯49079 Update and centralize TUI subscription labels @etraut-openai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-cbbe36&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-3-pricing-model-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-cbbe36%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->