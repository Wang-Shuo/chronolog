---
card_id: open-webui-2025-11-06-3ca1a4
date: '2025-11-06'
description: "Open WebUI · 2025-11-06 · Model Support: 10 changes in v0.6.35 — \U0001F5BC️
  Image generation system received a comprehensive overhaul with major new capabilities…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1032
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 45585c174006a2fb0edafe425c3a2b0f89f10aaa1a0fc0b4aeac3475d76488ae
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-06-3ca1a4
  comparison: ''
  date: '2025-11-06'
  description: 'Open WebUI — v0.6.35: 10 Model Support changes'
  evidence:
  - quote: "\U0001F5BC️ Image generation system received a comprehensive overhaul
      with major new capabilities including full image editing support allowing users
      to modify existing images using text prompts with OpenAI, Gemini, or ComfyUI
      engines, adding Gemini 2.5 Flash Image (Nano Banana) support, Qwen Image Edit
      integration, resolution of base64-encoded image display issues, streamlined
      AUTOMATIC1111 configuration by consolidating parameters into a flexible JSON
      parameters field, and enhanced UI with a code editor modal for ComfyUI workflow
      management. [#17434](https://github.com/open-webui/open-webui/pull/17434), [#16976](https://github.com/open-webui/open-webui/issues/16976),
      [Commit](https://github.com/open-webui/open-webui/commit/8e5690aab4f632a57027e2acf880b8f89a8717c0),
      [Commit](https://github.com/open-webui/open-webui/commit/72f8539fd2e679fec0762945f22f4b8a6920afa0),
      [Commit](https://github.com/open-webui/open-webui/commit/8d34fcb586eeee1fac6da2f991518b8a68b00b72),
      [Commit](https://github.com/open-webui/open-webui/commit/72900cd686de1fa6be84b5a8a2fc857cff7b91b8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F3A4 Mistral Voxtral model support was added for text-to-speech,
      including voxtral-small and voxtral-mini models with both transcription and
      chat completion API support. [#18934](https://github.com/open-webui/open-webui/pull/18934)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F527 UI freeze when querying models with knowledge bases containing
      inconsistent distance metrics is resolved by properly initializing the distances
      array in citations. [#18585](https://github.com/open-webui/open-webui/pull/18585)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F916 Duplicate model IDs from multiple OpenAI endpoints are now
      automatically deduplicated server-side, preventing frontend crashes for users
      with unified gateway proxies that aggregate multiple providers. [Commit](https://github.com/open-webui/open-webui/commit/fdf7ca11d4f3cc8fe63e81c98dc0d1e48e52ba36)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F527 OpenAPI specification endpoint conflict between \"/api/v1/models\"
      and \"/api/v1/models/\" is resolved by changing the models router endpoint to
      \"/list\", preventing duplicate operationId errors when generating TypeScript
      API clients. [#18758](https://github.com/open-webui/open-webui/issues/18758)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F3F7️ Model tags are now de-duplicated case-insensitively in both
      the model selector and workspace models page, preventing duplicate entries with
      different capitalization from appearing in filter dropdowns. [#18716](https://github.com/open-webui/open-webui/pull/18716),
      [#18711](https://github.com/open-webui/open-webui/issues/18711)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4AD Details tags for reasoning content are now correctly identified
      and rendered even when the same tag is present in user messages. [#18840](https://github.com/open-webui/open-webui/pull/18840),
      [#18294](https://github.com/open-webui/open-webui/issues/18294)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4CA Mermaid and Vega rendering errors now display inline with the
      code instead of showing repetitive toast notifications, improving user experience
      when models generate invalid diagram syntax. [Commit](https://github.com/open-webui/open-webui/commit/fdc0f04a8b7dd0bc9f9dc0e7e30854f7a0eea3e9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F4CB File list is now cleared when switching to models that do not
      support file uploads, preventing files from being sent to incompatible models.
      [#18496](https://github.com/open-webui/open-webui/pull/18496)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F310 \"Attach Webpage\" button now displays with correct disabled
      styling when a model does not support file uploads. [#18483](https://github.com/open-webui/open-webui/pull/18483)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-model-support-changes-in-v0-6-35
  source_release: open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234
  source_type: github_releases
  theme: model-support
  title: 10 Model Support changes in v0.6.35
  type: change
related_changes:
- '[[Changes/ChatGPT/2025-11-05-you-can-now-interrupt-long-running-queries-such-as-deep-research-or-gpt-5-pro-to|Interrupt
  ChatGPT]]'
- '[[Changes/Ollama/2025-11-05-2-model-support-changes-in-v0-12-10|2 Model Support
  changes in v0.12.10]]'
- '[[Changes/Cline/2025-11-06-complete-telemetry-attribution-for-model-provider-tracking-by-nickbaumann98-in-h|Complete
  telemetry attribution for model/provider tracking]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234]]'
source_type: github_releases
theme: model-support
title: 10 Model Support changes in v0.6.35
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Model Support changes in v0.6.35

**Open WebUI** · 2025-11-06 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.35) · from [[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|v0.6.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖼️ Image generation system received a comprehensive overhaul with major new capabilities including full image editing support allowing users to modify existing images using text prompts with OpenAI, Gemini, or ComfyUI engines, adding Gemini 2.5 Flash Image (Nano Banana) support, Qwen Image Edit integration, resolution of base64-encoded image display issues, streamlined AUTOMATIC1111 configuration by consolidating parameters into a flexible JSON parameters field, and enhanced UI with a code editor modal for ComfyUI workflow management. [#17434](https://github.com/open-webui/open-webui/pull/17434), [#16976](https://github.com/open-webui/open-webui/issues/16976), [Commit](https://github.com/open-webui/open-webui/commit/8e5690aab4f632a57027e2acf880b8f89a8717c0), [Commit](https://github.com/open-webui/open-webui/commit/72f8539fd2e679fec0762945f22f4b8a6920afa0), [Commit](https://github.com/open-webui/open-webui/commit/8d34fcb586eeee1fac6da2f991518b8a68b00b72), [Commit](https://github.com/open-webui/open-webui/commit/72900cd686de1fa6be84b5a8a2fc857cff7b91b8)

> 🎤 Mistral Voxtral model support was added for text-to-speech, including voxtral-small and voxtral-mini models with both transcription and chat completion API support. [#18934](https://github.com/open-webui/open-webui/pull/18934)

> 🔧 UI freeze when querying models with knowledge bases containing inconsistent distance metrics is resolved by properly initializing the distances array in citations. [#18585](https://github.com/open-webui/open-webui/pull/18585)

> 🤖 Duplicate model IDs from multiple OpenAI endpoints are now automatically deduplicated server-side, preventing frontend crashes for users with unified gateway proxies that aggregate multiple providers. [Commit](https://github.com/open-webui/open-webui/commit/fdf7ca11d4f3cc8fe63e81c98dc0d1e48e52ba36)

> 🔧 OpenAPI specification endpoint conflict between "/api/v1/models" and "/api/v1/models/" is resolved by changing the models router endpoint to "/list", preventing duplicate operationId errors when generating TypeScript API clients. [#18758](https://github.com/open-webui/open-webui/issues/18758)

> 🏷️ Model tags are now de-duplicated case-insensitively in both the model selector and workspace models page, preventing duplicate entries with different capitalization from appearing in filter dropdowns. [#18716](https://github.com/open-webui/open-webui/pull/18716), [#18711](https://github.com/open-webui/open-webui/issues/18711)

> 💭 Details tags for reasoning content are now correctly identified and rendered even when the same tag is present in user messages. [#18840](https://github.com/open-webui/open-webui/pull/18840), [#18294](https://github.com/open-webui/open-webui/issues/18294)

> 📊 Mermaid and Vega rendering errors now display inline with the code instead of showing repetitive toast notifications, improving user experience when models generate invalid diagram syntax. [Commit](https://github.com/open-webui/open-webui/commit/fdc0f04a8b7dd0bc9f9dc0e7e30854f7a0eea3e9)

> 📋 File list is now cleared when switching to models that do not support file uploads, preventing files from being sent to incompatible models. [#18496](https://github.com/open-webui/open-webui/pull/18496)

> 🌐 "Attach Webpage" button now displays with correct disabled styling when a model does not support file uploads. [#18483](https://github.com/open-webui/open-webui/pull/18483)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-06-chat-controls-button-is-now-properly-hidden-on-mobile-for-users-without-admin-or|📱 Chat controls button is now properly hidden on mobile for users without admin…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-06-3-voice-and-audio-changes-in-v0-6-35|3 Voice and Audio changes in v0.6.35]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-06-2-multimodal-input-changes-in-v0-6-35|2 Multimodal Input changes in v0.6.35]] · Multimodal Input
- [[Changes/Open WebUI/2025-11-06-4-safety-and-privacy-changes-in-v0-6-35|4 Safety and Privacy changes in v0.6.35]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-06-3-developer-workflow-changes-in-v0-6-35|3 Developer Workflow changes in v0.6.35]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-06-10-interface-experience-changes-in-v0-6-35|10 Interface Experience changes in v0.6.35]] · Interface Experience
- [[Changes/Open WebUI/2025-11-06-3-editor-experience-changes-in-v0-6-35|3 Editor Experience changes in v0.6.35]] · Editor Experience
- [[Changes/Open WebUI/2025-11-06-4-search-and-browsing-changes-in-v0-6-35|4 Search and Browsing changes in v0.6.35]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-06-3-reliability-and-performance-changes-in-v0-6-35|3 Reliability and Performance changes in v0.6.35]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-06-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-06-3-context-window-changes-in-v0-6-35|3 Context Window changes in v0.6.35]] · Context Window
- [[Changes/Open WebUI/2025-11-06-edit-button-is-now-available-in-the-three-dot-menu-of-models-in-the-workspace-se|✏️ Edit button is now available in the three-dot menu of models in the workspace…]] · Model Support
- [[Changes/Open WebUI/2025-11-06-screen-reader-support-was-enhanced-by-wrapping-messages-in-semantic-elements-wit|♿ Screen reader support was enhanced by wrapping messages in semantic elements…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-06-external-document-loaders-can-now-optionally-forward-user-information-headers-wh|📄 External document loaders can now optionally forward user information headers…]] · Pricing Model
- [[Changes/Open WebUI/2025-11-06-3-files-and-data-changes-in-v0-6-35|3 Files and Data changes in v0.6.35]] · Files and Data
- [[Changes/Open WebUI/2025-11-06-2-apps-and-integrations-changes-in-v0-6-35|2 Apps and Integrations changes in v0.6.35]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-06-5-account-and-access-changes-in-v0-6-35|5 Account and Access changes in v0.6.35]] · Account and Access
- [[Changes/Open WebUI/2025-11-06-22-other-changes-in-v0-6-35|22 other changes in v0.6.35]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-11-06 · Cline · [[Changes/Cline/2025-11-06-complete-telemetry-attribution-for-model-provider-tracking-by-nickbaumann98-in-h|Complete telemetry attribution for model/provider tracking]]
- Later: 2025-11-07 · Codex CLI · [[Changes/Codex CLI/2025-11-07-introducing-our-new-model-gpt-5-codex-mini-a-more-compact-and-cost-efficient-ver|Introducing our new model GPT-5-Codex-Mini]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-06-3ca1a4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-06-10-model-support-changes-in-v0-6-35.md%0ACard%20ID%3A%20open-webui-2025-11-06-3ca1a4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->