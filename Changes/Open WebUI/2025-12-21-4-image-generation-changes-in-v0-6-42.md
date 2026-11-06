---
card_id: open-webui-2025-12-21-e8676b
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Image Generation: 4 changes in v0.6.42 — \U0001F4F8
  Shared chats with generated or edited images now correctly display images when accessed
  by…"
diffusion:
  first_in_tracked: "[[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|\U0001F3A8
    DALL-E Integration]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 651
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cb058d0456be5f537f1f25076ccaf740d1c526395f35c2796fcc060e477eac70
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-e8676b
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 4 Image Generation changes'
  evidence:
  - quote: "\U0001F4F8 Shared chats with generated or edited images now correctly
      display images when accessed by other users by properly linking generated images
      to their chat and message through the chat_file table, ensuring images remain
      accessible in shared chat links. [Commit](https://github.com/open-webui/open-webui/commit/446cc0ac6063402a743e949f50612376ed5a8437),
      [#19393](https://github.com/open-webui/open-webui/issues/19393)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F3A8 OpenAI GPT-IMAGE 1.5 model support was added for image generation
      and editing with automatic image size capabilities. [Commit](https://github.com/open-webui/open-webui/commit/4c2e5c93e9287479f56f780708656136849ccaee)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F3A8 Image editing with reference images now correctly uses both
      previously generated images and newly uploaded reference images. [Commit](https://github.com/open-webui/open-webui/commit/bcd50ed8f1b7387fd700538ae0d74fc72f3c53d0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F9E0 Image generation and editing operations are now explicitly
      injected into system context, improving LLM comprehension even for weaker models
      so they reliably acknowledge operations instead of incorrectly claiming they
      cannot generate images. [Commit](https://github.com/open-webui/open-webui/commit/28b2fcab0cd036dbe646a66fe81890f288c77121)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-image-generation-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: image-generation
  title: 4 Image Generation changes in v0.6.42
  type: change
related_changes:
- '[[Changes/Lovable/2025-11-26-all-new-visual-edits|All new Visual edits]]'
- "[[Changes/Open WebUI/2025-12-02-image-generation-in-temporary-chats-was-fixed-by-correctly-handling-local-chat-s|\U0001F3A8
  Image generation in temporary chats was fixed by correctly handling local chat…]]"
- '[[Changes/ChatGPT/2025-12-16-we-ve-introduced-a-new-and-improved-version-of-chatgpt-images-powered-by-our-bes-a63d5c|ChatGPT
  Images on Web and Mobile (iOS & Android)]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: image-generation
title: 4 Image Generation changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Image Generation changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/image-generation|Image Generation]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📸 Shared chats with generated or edited images now correctly display images when accessed by other users by properly linking generated images to their chat and message through the chat_file table, ensuring images remain accessible in shared chat links. [Commit](https://github.com/open-webui/open-webui/commit/446cc0ac6063402a743e949f50612376ed5a8437), [#19393](https://github.com/open-webui/open-webui/issues/19393)

> 🎨 OpenAI GPT-IMAGE 1.5 model support was added for image generation and editing with automatic image size capabilities. [Commit](https://github.com/open-webui/open-webui/commit/4c2e5c93e9287479f56f780708656136849ccaee)

> 🎨 Image editing with reference images now correctly uses both previously generated images and newly uploaded reference images. [Commit](https://github.com/open-webui/open-webui/commit/bcd50ed8f1b7387fd700538ae0d74fc72f3c53d0)

> 🧠 Image generation and editing operations are now explicitly injected into system context, improving LLM comprehension even for weaker models so they reliably acknowledge operations instead of incorrectly claiming they cannot generate images. [Commit](https://github.com/open-webui/open-webui/commit/28b2fcab0cd036dbe646a66fe81890f288c77121)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2025-12-16 · ChatGPT · [[Changes/ChatGPT/2025-12-16-we-ve-introduced-a-new-and-improved-version-of-chatgpt-images-powered-by-our-bes-a63d5c|ChatGPT Images on Web and Mobile (iOS & Android)]]
- Later: 2025-12-22 · Open WebUI · [[Changes/Open WebUI/2025-12-22-image-action-button-fixed-restoring-the-ability-to-trigger-image-generation-edit|🎨 Image action button fixed, restoring the ability to trigger image generation…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-10 · Open WebUI · [[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|🎨 DALL-E Integration]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-e8676b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-4-image-generation-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-e8676b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->