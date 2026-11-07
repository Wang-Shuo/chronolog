---
card_id: openclaw-2026-10-10-28bf65
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Pricing Model: 4 changes in v2026.10.1 — The
  selected provider receives bounded request text, up to two recent visible exchanges…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 3013
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 000778747cbd557f747cbb2066d20eceed629c34a6194c6e4d9198d1923844eb
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-28bf65
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 4 Pricing Model changes'
  evidence:
  - quote: The selected provider receives bounded request text, up to two recent visible
      exchanges, tool-return and error counts, and prompt-hook text. Hosted evaluations
      can cost money, and judgments can be wrong. Turning assistance off stops new
      automatic evaluations; evaluations already sent may still transmit data and
      restrict tools. Explicit decision_evaluate calls have separate controls.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Plugins can subscribe to session changes instead of repeatedly reading
      everything, with cleanup and fallback reads for changes outside the subscription.
      Authors also gain draft-reset controls and reusable meeting builders and thread-binding
      validation.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Plugins can subscribe to changed session keys and invalidation tags, with
      unsubscribe and fallback reads for changes outside the subscription. #163820
      . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Switching or replacing a Codex chat protects the new chat from delayed
      commands and cleanup. Child assignments survive parent-thread replacement on
      the same connection, and an interrupted chat can resume after stopping and subscription
      cleanup succeed, while sibling chats continue.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-pricing-model-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: pricing-model
  title: 4 Pricing Model changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-09-get-a-warning-before-your-credits-run-out|Get a warning
  before your credits run out]]'
- '[[Changes/Raycast/2026-10-09-ai-made-ai-requests-smaller-so-local-models-reply-to-a-simple-message-much-faste|AI
  : Made AI requests smaller, so local models reply to a simple message much faster…]]'
- '[[Changes/Raycast/2026-10-09-ai-made-ai-requests-smaller-so-local-models-reply-to-a-simple-message-much-faste-aebf65|AI
  : Made AI requests smaller, so local models reply to a simple message much faster…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: pricing-model
title: 4 Pricing Model changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Pricing Model changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The selected provider receives bounded request text, up to two recent visible exchanges, tool-return and error counts, and prompt-hook text. Hosted evaluations can cost money, and judgments can be wrong. Turning assistance off stops new automatic evaluations; evaluations already sent may still transmit data and restrict tools. Explicit decision_evaluate calls have separate controls.

> Plugins can subscribe to session changes instead of repeatedly reading everything, with cleanup and fallback reads for changes outside the subscription. Authors also gain draft-reset controls and reusable meeting builders and thread-binding validation.

> Plugins can subscribe to changed session keys and invalidation tags, with unsubscribe and fallback reads for changes outside the subscription. #163820 . Thanks @steipete .

> Switching or replacing a Codex chat protects the new chat from delayed commands and cleanup. Child assignments survive parent-thread replacement on the same connection, and an interrupted chat can resume after stopping and subscription cleanup succeed, while sibling chats continue.

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-10-09 · Raycast · [[Changes/Raycast/2026-10-09-ai-made-ai-requests-smaller-so-local-models-reply-to-a-simple-message-much-faste-aebf65|AI : Made AI requests smaller, so local models reply to a simple message much faster…]]
- Later: 2026-10-12 · Lovable · [[Changes/Lovable/2026-10-12-see-how-much-usage-your-free-allowances-cover|See how much usage your free allowances cover]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-28bf65&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-4-pricing-model-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-28bf65%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->