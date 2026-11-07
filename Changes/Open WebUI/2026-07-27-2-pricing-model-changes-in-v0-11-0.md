---
card_id: open-webui-2026-07-27-e02524
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Pricing Model: 2 changes in v0.11.0 — \U0001FAA7
  **Cheaper tagging after each reply.** Saving the tags generated for a conversation
  now…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1320
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: aa8c5d5ee225036358f207c724886ee26913d4632fb8c57a915fc3c5cae7d4dc
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-e02524
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 2 Pricing Model changes'
  evidence:
  - quote: "\U0001FAA7 **Cheaper tagging after each reply.** Saving the tags generated
      for a conversation now updates just that field instead of loading, rewriting
      and re-reading the whole conversation, which cost more the longer the chat.
      [#27382](https://github.com/open-webui/open-webui/pull/27382)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F522 **Usage now reports the latest call separately.** In a response's
      usage block, \"prompt_tokens\" and \"completion_tokens\" now carry the counts
      from the most recent model call rather than the running total, while \"input_tokens\",
      \"output_tokens\" and \"total_tokens\" stay cumulative, so anything reading
      the first pair for billing should read the second set instead. [Commit](https://github.com/open-webui/open-webui/commit/df94268e892cbb66675170a6c78846aef23f6e89),
      [#27031](https://github.com/open-webui/open-webui/issues/27031)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-pricing-model-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: pricing-model
  title: 2 Pricing Model changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Replit/2026-07-24-lower-prices-across-replit-cloud|Lower prices across
  Replit Cloud]]'
- '[[Changes/Replit/2026-07-24-billing|Billing]]'
- '[[Changes/Replit/2026-07-24-more-flexibility-when-changing-your-pro-plan|More flexibility
  when changing your Pro plan]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: pricing-model
title: 2 Pricing Model changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Pricing Model changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪧 **Cheaper tagging after each reply.** Saving the tags generated for a conversation now updates just that field instead of loading, rewriting and re-reading the whole conversation, which cost more the longer the chat. [#27382](https://github.com/open-webui/open-webui/pull/27382)

> 🔢 **Usage now reports the latest call separately.** In a response's usage block, "prompt_tokens" and "completion_tokens" now carry the counts from the most recent model call rather than the running total, while "input_tokens", "output_tokens" and "total_tokens" stay cumulative, so anything reading the first pair for billing should read the second set instead. [Commit](https://github.com/open-webui/open-webui/commit/df94268e892cbb66675170a6c78846aef23f6e89), [#27031](https://github.com/open-webui/open-webui/issues/27031)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-07-24 · Replit · [[Changes/Replit/2026-07-24-more-flexibility-when-changing-your-pro-plan|More flexibility when changing your Pro plan]]
- Later: 2026-07-28 · Cursor · [[Changes/Cursor/2026-07-28-local-pricing-at-649-per-month-tax-inclusive-billed-in-inr-with-upi-or-card|Local pricing at ₹649 per month, tax inclusive, billed in INR with UPI or card]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-e02524&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-2-pricing-model-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-e02524%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->