---
card_id: open-webui-2026-01-09-b666ae
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Image Generation: 4 changes in v0.7.0 — \U0001F916
  **Native Function Calling with Built-in Tools.** Users can now ask models to perform…"
diffusion:
  first_in_tracked: "[[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|\U0001F3A8
    DALL-E Integration]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 670
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3fe24347fde5a51fa08ddf8747cdd351459ebdfc509d5fc4e0925732bed37503
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-b666ae
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 4 Image Generation changes'
  evidence:
  - quote: "\U0001F916 **Native Function Calling with Built-in Tools.** Users can
      now ask models to perform multi-step tasks that combine web research, knowledge
      base queries, note-taking, and image generation in a single conversation—for
      example, \"research the latest on X, save key findings to a note, and generate
      an infographic.\" Requires models with native function calling support and function
      calling mode set to \"Native\" in Chat Controls. [#19397](https://github.com/open-webui/open-webui/issues/19397),
      [Commit](https://github.com/open-webui/open-webui/commit/5c1d52231a3997a17381c48639bd7e339262cf7c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F5BC️ Administrators and Action developers can now control image
      generation denoising steps per-request using a steps parameter, allowing Actions
      and API calls to override the global IMAGE_STEPS configuration for both ComfyUI
      and Automatic1111 engines. [#20337](https://github.com/open-webui/open-webui/pull/20337)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F4AD Users no longer experience data corruption when switching between
      chats during background operations like image generation, where messages from
      one chat would appear in another chat's history. [#20266](https://github.com/open-webui/open-webui/pull/20266)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F5BC️ Users with image generation enabled no longer see false vision
      capability warnings, allowing them to send follow-up messages after generating
      images and to send images to non-vision models for image editing. [#20129](https://github.com/open-webui/open-webui/issues/20129),
      [#20256](https://github.com/open-webui/open-webui/pull/20256)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-image-generation-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: image-generation
  title: 4 Image Generation changes in v0.7.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2025-12-16-we-ve-introduced-a-new-and-improved-version-of-chatgpt-images-powered-by-our-bes-a63d5c|ChatGPT
  Images on Web and Mobile (iOS & Android)]]'
- '[[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation
  changes in v0.6.42]]'
- "[[Changes/Open WebUI/2025-12-22-image-action-button-fixed-restoring-the-ability-to-trigger-image-generation-edit|\U0001F3A8
  Image action button fixed, restoring the ability to trigger image generation…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: image-generation
title: 4 Image Generation changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Image Generation changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/image-generation|Image Generation]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🤖 **Native Function Calling with Built-in Tools.** Users can now ask models to perform multi-step tasks that combine web research, knowledge base queries, note-taking, and image generation in a single conversation—for example, "research the latest on X, save key findings to a note, and generate an infographic." Requires models with native function calling support and function calling mode set to "Native" in Chat Controls. [#19397](https://github.com/open-webui/open-webui/issues/19397), [Commit](https://github.com/open-webui/open-webui/commit/5c1d52231a3997a17381c48639bd7e339262cf7c)

> 🖼️ Administrators and Action developers can now control image generation denoising steps per-request using a steps parameter, allowing Actions and API calls to override the global IMAGE_STEPS configuration for both ComfyUI and Automatic1111 engines. [#20337](https://github.com/open-webui/open-webui/pull/20337)

> 💭 Users no longer experience data corruption when switching between chats during background operations like image generation, where messages from one chat would appear in another chat's history. [#20266](https://github.com/open-webui/open-webui/pull/20266)

> 🖼️ Users with image generation enabled no longer see false vision capability warnings, allowing them to send follow-up messages after generating images and to send images to non-vision models for image editing. [#20129](https://github.com/open-webui/open-webui/issues/20129), [#20256](https://github.com/open-webui/open-webui/pull/20256)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2025-12-22 · Open WebUI · [[Changes/Open WebUI/2025-12-22-image-action-button-fixed-restoring-the-ability-to-trigger-image-generation-edit|🎨 Image action button fixed, restoring the ability to trigger image generation…]]
- Later: 2026-01-10 · Ollama · [[Changes/Ollama/2026-01-10-new-experimental-support-for-image-generation-models-powered-by-mlx|New experimental support for image generation models, powered by MLX]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-10 · Open WebUI · [[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|🎨 DALL-E Integration]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-b666ae&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-4-image-generation-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-b666ae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->