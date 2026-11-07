---
card_id: open-webui-2026-04-21-2c05ac
date: '2026-04-21'
description: "Open WebUI · 2026-04-21 · Image Generation: 4 changes in v0.9.0 — \U0001F5BC️
  **ComfyUI request reliability.** ComfyUI image generation and editing now use shared
  async…"
diffusion:
  first_in_tracked: "[[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|\U0001F3A8
    DALL-E Integration]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 772
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5afcb5564df88246cb3c7d0593bddbc702f1fce033360988afc65ee223811c3e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-04-21-2c05ac
  comparison: ''
  date: '2026-04-21'
  description: 'Open WebUI — v0.9.0: 4 Image Generation changes'
  evidence:
  - quote: "\U0001F5BC️ **ComfyUI request reliability.** ComfyUI image generation
      and editing now use shared async connections with consistent SSL handling, making
      image uploads and workflow runs more reliable under concurrent load. [Commit](https://github.com/open-webui/open-webui/commit/5944eda0ff25a284f7157252683bccede741cbe7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Image SSL setting support.** Image generation now respects
      the configured SSL session setting, preventing avoidable connection failures
      in strict certificate environments. [Commit](https://github.com/open-webui/open-webui/commit/128cf41fcedf2638fc8a6acd850d8b0409be1c4e),
      [#23777](https://github.com/open-webui/open-webui/issues/23777)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **Optional image size parameter.** Image generation no longer
      sends the \"size\" field when no size is configured, improving compatibility
      with providers that reject unsupported size arguments. [#23611](https://github.com/open-webui/open-webui/issues/23611),
      [Commit](https://github.com/open-webui/open-webui/commit/869cf9e848b741705dc058550fa1b3f70db47fe8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  - quote: "\U0001F5BC️ **ComfyUI request hangs.** Concurrent image generation and
      editing requests to ComfyUI now complete reliably instead of getting stuck when
      the same user starts multiple requests at once. [#23592](https://github.com/open-webui/open-webui/pull/23592),
      [#23591](https://github.com/open-webui/open-webui/issues/23591)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-image-generation-changes-in-v0-9-0
  source_release: open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a
  source_type: github_releases
  theme: image-generation
  title: 4 Image Generation changes in v0.9.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool
  discovery and image generation are now enabled by default, with higher-detail…]]'
- '[[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153
  Launch image generation by default @won-openai]]'
- '[[Changes/ChatGPT/2026-04-21-we-re-introducing-chatgpt-images-2-0-our-new-image-generation-model-in-chatgpt-c|ChatGPT
  Images 2.0 in ChatGPT]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a]]'
source_type: github_releases
theme: image-generation
title: 4 Image Generation changes in v0.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Image Generation changes in v0.9.0

**Open WebUI** · 2026-04-21 · [[Themes/image-generation|Image Generation]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.0) · from [[Releases/Open WebUI/open-webui-2026-04-21-v0-9-0-github-311589683-2ff57b5a|v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖼️ **ComfyUI request reliability.** ComfyUI image generation and editing now use shared async connections with consistent SSL handling, making image uploads and workflow runs more reliable under concurrent load. [Commit](https://github.com/open-webui/open-webui/commit/5944eda0ff25a284f7157252683bccede741cbe7)

> 🖼️ **Image SSL setting support.** Image generation now respects the configured SSL session setting, preventing avoidable connection failures in strict certificate environments. [Commit](https://github.com/open-webui/open-webui/commit/128cf41fcedf2638fc8a6acd850d8b0409be1c4e), [#23777](https://github.com/open-webui/open-webui/issues/23777)

> 🖼️ **Optional image size parameter.** Image generation no longer sends the "size" field when no size is configured, improving compatibility with providers that reject unsupported size arguments. [#23611](https://github.com/open-webui/open-webui/issues/23611), [Commit](https://github.com/open-webui/open-webui/commit/869cf9e848b741705dc058550fa1b3f70db47fe8)

> 🖼️ **ComfyUI request hangs.** Concurrent image generation and editing requests to ComfyUI now complete reliably instead of getting stuck when the same user starts multiple requests at once. [#23592](https://github.com/open-webui/open-webui/pull/23592), [#23591](https://github.com/open-webui/open-webui/issues/23591)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-04-21-3-files-and-data-changes-in-v0-9-0|3 Files and Data changes in v0.9.0]] · Files and Data
- [[Changes/Open WebUI/2026-04-21-28-model-support-changes-in-v0-9-0|28 Model Support changes in v0.9.0]] · Model Support
- [[Changes/Open WebUI/2026-04-21-5-editor-experience-changes-in-v0-9-0|5 Editor Experience changes in v0.9.0]] · Editor Experience
- [[Changes/Open WebUI/2026-04-21-persistent-chat-payload-efficiency-persisted-chats-now-use-server-side-history-l|🚀 Persistent chat payload efficiency. Persisted chats now use server-side…]] · Multimodal Input
- [[Changes/Open WebUI/2026-04-21-8-context-window-changes-in-v0-9-0|8 Context Window changes in v0.9.0]] · Context Window
- [[Changes/Open WebUI/2026-04-21-24-reliability-and-performance-changes-in-v0-9-0|24 Reliability and Performance changes in v0.9.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-04-21-4-apps-and-integrations-changes-in-v0-9-0|4 Apps and Integrations changes in v0.9.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-04-21-46-developer-workflow-changes-in-v0-9-0|46 Developer Workflow changes in v0.9.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-04-21-8-automation-and-scheduling-changes-in-v0-9-0|8 Automation and Scheduling changes in v0.9.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-04-21-7-memory-and-personalization-changes-in-v0-9-0|7 Memory and Personalization changes in v0.9.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-04-21-2-mobile-and-desktop-changes-in-v0-9-0|2 Mobile and Desktop changes in v0.9.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-04-21-17-interface-experience-changes-in-v0-9-0|17 Interface Experience changes in v0.9.0]] · Interface Experience
- [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-04-21-4-search-and-browsing-changes-in-v0-9-0|4 Search and Browsing changes in v0.9.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-04-21-shared-chat-access-controls-you-can-now-control-who-has-access-to-a-shared-chat|🔗 Shared chat access controls. You can now control who has access to a shared…]] · Collaboration
- [[Changes/Open WebUI/2026-04-21-4-voice-and-audio-changes-in-v0-9-0|4 Voice and Audio changes in v0.9.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-04-21-17-account-and-access-changes-in-v0-9-0|17 Account and Access changes in v0.9.0]] · Account and Access
- [[Changes/Open WebUI/2026-04-21-21-other-changes-in-v0-9-0|21 other changes in v0.9.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2026-04-21 · ChatGPT · [[Changes/ChatGPT/2026-04-21-we-re-introducing-chatgpt-images-2-0-our-new-image-generation-model-in-chatgpt-c|ChatGPT Images 2.0 in ChatGPT]]
- Later: 2026-04-30 · Codex CLI · [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-10 · Open WebUI · [[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|🎨 DALL-E Integration]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-04-21-2c05ac&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-04-21-4-image-generation-changes-in-v0-9-0.md%0ACard%20ID%3A%20open-webui-2026-04-21-2c05ac%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->