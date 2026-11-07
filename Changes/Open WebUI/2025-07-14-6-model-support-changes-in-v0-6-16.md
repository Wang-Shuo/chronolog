---
card_id: open-webui-2025-07-14-714767
date: '2025-07-14'
description: 'Open WebUI · 2025-07-14 · Model Support: 6 changes in v0.6.16 — ⏱️ **Configurable
  Model List Cache TTL**: Take control over model list caching with the new…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 917
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8d349b8494141c4c9313442422d4bf9df880ca19a4ce81e1ecadc83ced9740af
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-07-14-714767
  comparison: ''
  date: '2025-07-14'
  description: 'Open WebUI — v0.6.16: 6 Model Support changes'
  evidence:
  - quote: '⏱️ **Configurable Model List Cache TTL**: Take control over model list
      caching with the new MODEL_LIST_CACHE_TTL environment variable. Set a custom
      cache duration in seconds to balance performance and freshness, reducing API
      requests in stable environments or ensuring rapid updates when models change
      frequently.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  - quote: "\U0001F516 **Reference Notes as Knowledge or in Chats**: Use any note
      as knowledge for a model or folder, or reference it directly from chat—integrate
      living documentation into your Retrieval Augmented Generation workflows or discussions,
      bridging knowledge and action."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  - quote: '↕️ **Resizable System Prompt Fields**: Conveniently resize system prompt
      input fields to comfortably view and edit lengthy or complex instructions, improving
      the user experience for advanced model configuration.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  - quote: "\U0001F527 **Granular Update Check Control**: Gain finer control over
      outbound connections with the new ENABLE_VERSION_UPDATE_CHECK flag. This allows
      administrators to disable version update checks independently of the full OFFLINE_MODE,
      perfect for environments with restricted internet access that still need to
      download embedding models."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  - quote: "\U0001F9FE **Ollama API Compatibility**: Fixed model parameter naming
      in the API to ensure uninterrupted compatibility for all Ollama endpoints."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  - quote: 'ℹ️ **Consistent Model Description Rendering**: Model descriptions now
      render Markdown correctly in the main chat interface, matching the formatting
      seen in the model selection dropdown for a consistent user experience.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-model-support-changes-in-v0-6-16
  source_release: open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v0.6.16
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-07-10-added-new-config-option-model-supports-reasoning-summaries-https-github-com-open|Added
  new config option]]'
- '[[Changes/Dify/2025-07-10-4-model-support-changes-in-1-6-0|4 Model Support changes
  in 1.6.0]]'
- '[[Changes/Gemini CLI/2025-07-11-5-model-support-changes-in-v0-1-10|5 Model Support
  changes in v0.1.10]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf|open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v0.6.16
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v0.6.16

**Open WebUI** · 2025-07-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.16) · from [[Releases/Open WebUI/open-webui-2025-07-14-v0-6-16-github-232298341-b0885edf|v0.6.16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⏱️ **Configurable Model List Cache TTL**: Take control over model list caching with the new MODEL_LIST_CACHE_TTL environment variable. Set a custom cache duration in seconds to balance performance and freshness, reducing API requests in stable environments or ensuring rapid updates when models change frequently.

> 🔖 **Reference Notes as Knowledge or in Chats**: Use any note as knowledge for a model or folder, or reference it directly from chat—integrate living documentation into your Retrieval Augmented Generation workflows or discussions, bridging knowledge and action.

> ↕️ **Resizable System Prompt Fields**: Conveniently resize system prompt input fields to comfortably view and edit lengthy or complex instructions, improving the user experience for advanced model configuration.

> 🔧 **Granular Update Check Control**: Gain finer control over outbound connections with the new ENABLE_VERSION_UPDATE_CHECK flag. This allows administrators to disable version update checks independently of the full OFFLINE_MODE, perfect for environments with restricted internet access that still need to download embedding models.

> 🧾 **Ollama API Compatibility**: Fixed model parameter naming in the API to ensure uninterrupted compatibility for all Ollama endpoints.

> ℹ️ **Consistent Model Description Rendering**: Model descriptions now render Markdown correctly in the main chat interface, matching the formatting seen in the model selection dropdown for a consistent user experience.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.16
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-07-14-2-automation-and-scheduling-changes-in-v0-6-16|2 Automation and Scheduling changes in v0.6.16]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-07-14-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-07-14-4-context-window-changes-in-v0-6-16|4 Context Window changes in v0.6.16]] · Context Window
- [[Changes/Open WebUI/2025-07-14-instant-folder-based-chat-creation-start-a-new-chat-directly-from-any-folder-jus|📁 Instant Folder-Based Chat Creation]] · Projects and Workspaces
- [[Changes/Open WebUI/2025-07-14-4-reliability-and-performance-changes-in-v0-6-16|4 Reliability and Performance changes in v0.6.16]] · Reliability and Performance
- [[Changes/Open WebUI/2025-07-14-4-interface-experience-changes-in-v0-6-16|4 Interface Experience changes in v0.6.16]] · Interface Experience
- [[Changes/Open WebUI/2025-07-14-accessibility-high-contrast-theme-enhancements-major-accessibility-overhaul-with|🎨 Accessibility & High-Contrast Theme Enhancements]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-07-14-3-safety-and-privacy-changes-in-v0-6-16|3 Safety and Privacy changes in v0.6.16]] · Safety and Privacy
- [[Changes/Open WebUI/2025-07-14-3-account-and-access-changes-in-v0-6-16|3 Account and Access changes in v0.6.16]] · Account and Access
- [[Changes/Open WebUI/2025-07-14-3-files-and-data-changes-in-v0-6-16|3 Files and Data changes in v0.6.16]] · Files and Data
- [[Changes/Open WebUI/2025-07-14-audio-mime-type-registration-issues-with-audio-file-content-types-have-been-reso|🔄 Audio MIME Type Registration]] · Voice and Audio
- [[Changes/Open WebUI/2025-07-14-seamless-iphone-image-uploads-effortlessly-upload-photos-from-iphones-and-other|📷 Seamless iPhone Image Uploads]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-07-14-4-collaboration-changes-in-v0-6-16|4 Collaboration changes in v0.6.16]] · Collaboration
- [[Changes/Open WebUI/2025-07-14-3-editor-experience-changes-in-v0-6-16|3 Editor Experience changes in v0.6.16]] · Editor Experience
- [[Changes/Open WebUI/2025-07-14-20-other-changes-in-v0-6-16|20 other changes in v0.6.16]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-07-11 · Gemini CLI · [[Changes/Gemini CLI/2025-07-11-5-model-support-changes-in-v0-1-10|5 Model Support changes in v0.1.10]]
- Later: 2025-07-15 · Cline · [[Changes/Cline/2025-07-15-add-kimi-k2-as-trending-model-by-celestial-vault-in-https-github-com-cline-cline|Add kimi-k2 as trending model]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-07-14-714767&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-07-14-6-model-support-changes-in-v0-6-16.md%0ACard%20ID%3A%20open-webui-2025-07-14-714767%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.16%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->