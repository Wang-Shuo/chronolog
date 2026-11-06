---
card_id: open-webui-2025-12-21-6ad272
date: '2025-12-21'
description: "Open WebUI · 2025-12-21 · Model Support: 11 changes in v0.6.42 — \U0001F680
  Models API endpoint performance was optimized through batched model loading, eliminating
  N+1…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1077
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: be3abc4c659dc1638899c4759da75a21946c2ded421f3bb7f5b81f5a6a021899
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-6ad272
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 11 Model Support changes'
  evidence:
  - quote: "\U0001F680 Models API endpoint performance was optimized through batched
      model loading, eliminating N+1 queries and significantly reducing response times
      when filtering models by user permissions. [Commit](https://github.com/open-webui/open-webui/commit/0dd2cfe1f273fbacdbe90300a97c021f2e678656)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F500 Custom model fallback handling was added, allowing workspace-created
      custom models to automatically fall back to the default chat model when their
      configured base model is not found; set \"ENABLE_CUSTOM_MODEL_FALLBACK\" to
      true to enable, preventing workflow disruption when base models are removed
      or renamed, while ensuring other requests remain unaffected. [Commit](https://github.com/open-webui/open-webui/commit/b35aeb8f46e0e278c6f4538382c2b6838e24cc5a),
      [#19985](https://github.com/open-webui/open-webui/pull/19985)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4C8 An experimental chat usage statistics endpoint (GET /api/v1/chats/stats/usage)
      was added with pagination support (50 chats per page) and comprehensive per-chat
      analytics including model usage counts, user and assistant message breakdowns,
      average response times calculated from message timestamps, average content lengths,
      and last activity timestamps; this endpoint remains experimental and not suitable
      for production use as it performs intensive calculations by processing entire
      message histories for each chat without caching. [Commit](https://github.com/open-webui/open-webui/commit/a7993f6f4e4591cd2aaa4718ece9e5623557d019)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F50D Search bar freezing and crashing issues in Models, Chat, and
      Archived Chat pages caused by excessively long queries exceeding server URL
      limits were resolved by truncating queries to 500 characters, and knowledge
      base layout shifting with long names was fixed by adjusting flex container properties.
      [#19832](https://github.com/open-webui/open-webui/pull/19832)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F9E9 Chat overview tab crashes caused by undefined model references
      were resolved by adding proper null checks when accessing deleted or ejected
      models. [#19935](https://github.com/open-webui/open-webui/pull/19935)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F504 MultiResponseMessages component crashes when navigating chat
      history after removing or changing selected models are now prevented through
      proper component re-initialization. [Commit](https://github.com/open-webui/open-webui/commit/870e29e3738da968c396b70532f365a3c2f71995),
      [#18599](https://github.com/open-webui/open-webui/issues/18599)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4F8 Model avatar images now update immediately in the admin models
      list through proper Cache-Control headers, eliminating the need for manual cache
      clearing. [#19959](https://github.com/open-webui/open-webui/pull/19959)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: ⚙️ Model usage settings are now correctly preserved when switching between
      models instead of being unexpectedly cleared or reset. [#19868](https://github.com/open-webui/open-webui/pull/19868),
      [#19549](https://github.com/open-webui/open-webui/issues/19549)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F3AF The DefaultFiltersSelector component in model settings now
      correctly displays when only global toggleable filters are present, enabling
      per-model default configuration. [#20066](https://github.com/open-webui/open-webui/pull/20066)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F503 Ollama model list now automatically refreshes after model deletion,
      preventing deleted models from persisting in the UI and being inadvertently
      re-downloaded during subsequent pull operations. [#19912](https://github.com/open-webui/open-webui/pull/19912)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4DC Tool specification serialization now preserves non-ASCII characters
      including Chinese text, improving LLM comprehension and tool selection accuracy
      by avoiding Unicode escape sequences. [#19942](https://github.com/open-webui/open-webui/pull/19942)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-model-support-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in v0.6.42
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-12-19-2-model-support-changes-in-rust-v0-76-0|2 Model
  Support changes in rust-v0.76.0]]'
- '[[Changes/GitHub Copilot CLI/2025-12-19-enable-disabled-models-directly-in-cli-when-selecting-or-specifying-them|Enable
  disabled models directly in CLI when selecting or specifying them]]'
- '[[Changes/Codex CLI/2025-12-21-3-model-support-changes-in-rust-v0-77-0|3 Model
  Support changes in rust-v0.77.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚀 Models API endpoint performance was optimized through batched model loading, eliminating N+1 queries and significantly reducing response times when filtering models by user permissions. [Commit](https://github.com/open-webui/open-webui/commit/0dd2cfe1f273fbacdbe90300a97c021f2e678656)

> 🔀 Custom model fallback handling was added, allowing workspace-created custom models to automatically fall back to the default chat model when their configured base model is not found; set "ENABLE_CUSTOM_MODEL_FALLBACK" to true to enable, preventing workflow disruption when base models are removed or renamed, while ensuring other requests remain unaffected. [Commit](https://github.com/open-webui/open-webui/commit/b35aeb8f46e0e278c6f4538382c2b6838e24cc5a), [#19985](https://github.com/open-webui/open-webui/pull/19985)

> 📈 An experimental chat usage statistics endpoint (GET /api/v1/chats/stats/usage) was added with pagination support (50 chats per page) and comprehensive per-chat analytics including model usage counts, user and assistant message breakdowns, average response times calculated from message timestamps, average content lengths, and last activity timestamps; this endpoint remains experimental and not suitable for production use as it performs intensive calculations by processing entire message histories for each chat without caching. [Commit](https://github.com/open-webui/open-webui/commit/a7993f6f4e4591cd2aaa4718ece9e5623557d019)

> 🔍 Search bar freezing and crashing issues in Models, Chat, and Archived Chat pages caused by excessively long queries exceeding server URL limits were resolved by truncating queries to 500 characters, and knowledge base layout shifting with long names was fixed by adjusting flex container properties. [#19832](https://github.com/open-webui/open-webui/pull/19832)

> 🧩 Chat overview tab crashes caused by undefined model references were resolved by adding proper null checks when accessing deleted or ejected models. [#19935](https://github.com/open-webui/open-webui/pull/19935)

> 🔄 MultiResponseMessages component crashes when navigating chat history after removing or changing selected models are now prevented through proper component re-initialization. [Commit](https://github.com/open-webui/open-webui/commit/870e29e3738da968c396b70532f365a3c2f71995), [#18599](https://github.com/open-webui/open-webui/issues/18599)

> 📸 Model avatar images now update immediately in the admin models list through proper Cache-Control headers, eliminating the need for manual cache clearing. [#19959](https://github.com/open-webui/open-webui/pull/19959)

> ⚙️ Model usage settings are now correctly preserved when switching between models instead of being unexpectedly cleared or reset. [#19868](https://github.com/open-webui/open-webui/pull/19868), [#19549](https://github.com/open-webui/open-webui/issues/19549)

> 🎯 The DefaultFiltersSelector component in model settings now correctly displays when only global toggleable filters are present, enabling per-model default configuration. [#20066](https://github.com/open-webui/open-webui/pull/20066)

> 🔃 Ollama model list now automatically refreshes after model deletion, preventing deleted models from persisting in the UI and being inadvertently re-downloaded during subsequent pull operations. [#19912](https://github.com/open-webui/open-webui/pull/19912)

> 📜 Tool specification serialization now preserves non-ASCII characters including Chinese text, improving LLM comprehension and tool selection accuracy by avoiding Unicode escape sequences. [#19942](https://github.com/open-webui/open-webui/pull/19942)

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
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-12-21 · Codex CLI · [[Changes/Codex CLI/2025-12-21-3-model-support-changes-in-rust-v0-77-0|3 Model Support changes in rust-v0.77.0]]
- Later: 2025-12-22 · Cline · [[Changes/Cline/2025-12-22-remove-glm-4-6-from-free-models|Remove GLM 4.6 from free models]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-6ad272&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-11-model-support-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-6ad272%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->