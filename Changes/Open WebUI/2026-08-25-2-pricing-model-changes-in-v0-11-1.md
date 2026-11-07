---
card_id: open-webui-2026-08-25-3dd521
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Pricing Model: 2 changes in v0.11.1 — \U0001F9FC
  **Less work per update in a long chat.** Each update saved while a reply streams
  no longer…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2967
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a91a42372c32bec86218176704f13fd81a12a48791404aa3db715bc312be3cb3
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-3dd521
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 2 Pricing Model changes'
  evidence:
  - quote: "\U0001F9FC **Less work per update in a long chat.** Each update saved
      while a reply streams no longer re-examines the entire conversation, only the
      part being added, so the cost of an update stops growing with the length of
      the chat. [#28820](https://github.com/open-webui/open-webui/pull/28820)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9F5 **Cheaper saving of a reply as it streams.** The resume snapshot
      taken on every piece of a streamed reply no longer rebuilds the whole answer
      each time, so the cost of a save stops growing with the length of the reply.
      [#28821](https://github.com/open-webui/open-webui/pull/28821)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-pricing-model-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: pricing-model
  title: 2 Pricing Model changes in v0.11.1
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-08-24-swift-sdk|Swift SDK]]'
- '[[Changes/OpenCode/2026-08-24-removed-outdated-opencode-go-first-month-discount-messaging-and-pricing|Removed
  outdated OpenCode Go first-month discount messaging and pricing]]'
- '[[Changes/Dify/2026-08-25-7-pricing-model-changes-in-1-17-0|7 Pricing Model changes
  in 1.17.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: pricing-model
title: 2 Pricing Model changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Pricing Model changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧼 **Less work per update in a long chat.** Each update saved while a reply streams no longer re-examines the entire conversation, only the part being added, so the cost of an update stops growing with the length of the chat. [#28820](https://github.com/open-webui/open-webui/pull/28820)

> 🧵 **Cheaper saving of a reply as it streams.** The resume snapshot taken on every piece of a streamed reply no longer rebuilds the whole answer each time, so the cost of a save stops growing with the length of the reply. [#28821](https://github.com/open-webui/open-webui/pull/28821)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-7-pricing-model-changes-in-1-17-0|7 Pricing Model changes in 1.17.0]]
- Later: 2026-08-26 · Cline · [[Changes/Cline/2026-08-26-cost-estimates-are-no-longer-shown-for-providers-billed-by-a-flat-rate-subscript|Cost estimates are no longer shown for providers billed by a flat-rate subscription…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-3dd521&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-2-pricing-model-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-3dd521%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->