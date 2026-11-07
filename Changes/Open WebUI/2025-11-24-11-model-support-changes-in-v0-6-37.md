---
card_id: open-webui-2025-11-24-d38a09
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Model Support: 11 changes in v0.6.37 — \U0001F5BC️
  Large stream chunk handling was implemented to support models that generate images
  directly…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1050
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d70c7983ffe3a9c5ee0c700c90cbdb07d026168d5effa0efc1d3c465185d0fba
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-d38a09
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 11 Model Support changes'
  evidence:
  - quote: "\U0001F5BC️ Large stream chunk handling was implemented to support models
      that generate images directly in their output responses, with configurable buffer
      size via \"CHAT_STREAM_RESPONSE_CHUNK_MAX_BUFFER_SIZE\" environment variable,
      resolving compatibility issues with models like Gemini 2.5 Flash Image. [#18884](https://github.com/open-webui/open-webui/pull/18884),
      [#17626](https://github.com/open-webui/open-webui/issues/17626)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F5BC️ Streaming response middleware now handles images in delta
      updates with automatic base64 conversion, enabling proper display of images
      from models using the \"choices[0].delta.images.image_url\" format such as Gemini
      2.5 Flash Image Preview on OpenRouter. [#19073](https://github.com/open-webui/open-webui/pull/19073),
      [#19019](https://github.com/open-webui/open-webui/issues/19019)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: ⚡ Workspace models page now supports server-side pagination dramatically
      improving load times and usability for instances with large numbers of workspace
      models.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4CC Default pinned models can now be configured by administrators
      for all new users, mirroring the behavior of default models where admin-configured
      defaults apply only to users who haven't customized their pinned models, configurable
      via \"DEFAULT_PINNED_MODELS\" environment variable. [#19273](https://github.com/open-webui/open-webui/pull/19273)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F3F7️ Tag suggestions are now context-aware, displaying only relevant
      tags when creating or editing models versus chat conversations, preventing confusion
      between model and chat tags. [#19135](https://github.com/open-webui/open-webui/issues/19135)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F916 Model update functionality now works correctly, resolving a
      database parameter binding error that prevented saving changes to model configurations
      via the Save & Update button. [#19335](https://github.com/open-webui/open-webui/issues/19335)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F916 Azure OpenAI models now support the \"reasoning_effort\" parameter,
      enabling proper configuration of reasoning capabilities for models like GPT-5.1
      which default to no reasoning without this setting. [#19290](https://github.com/open-webui/open-webui/issues/19290)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F916 Models with very long IDs can now be deleted correctly, resolving
      URL length limitations that previously prevented management operations on such
      models. [#18230](https://github.com/open-webui/open-webui/pull/18230)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F916 Model-level streaming settings now correctly apply to API requests,
      ensuring \"Stream Chat Response\" toggle properly controls the streaming parameter.
      [#19154](https://github.com/open-webui/open-webui/issues/19154)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F3A8 Gemini image edit settings now display correctly in the admin
      panel, fixing an incorrect configuration key reference that prevented proper
      rendering of edit options. [#19200](https://github.com/open-webui/open-webui/pull/19200)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F4DD Notes chat feature now correctly submits messages to the completions
      endpoint, resolving errors that prevented AI model interactions. [#19079](https://github.com/open-webui/open-webui/pull/19079)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 11-model-support-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in v0.6.37
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-11-24-opus-4-5-gpt-4-1-and-gpt-5-mini-are-now-available-in-github-copilot-cli|Opus
  4.5, GPT-4.1 and GPT-5-Mini are now available in GitHub Copilot CLI]]'
- "[[Changes/Open WebUI/2025-11-24-model-cloning-is-now-available-in-admin-settings-allowing-administrators-to-quic|\U0001F916
  Model cloning is now available in admin settings, allowing administrators…]]"
- "[[Changes/Open WebUI/2025-11-24-default-group-assignment-is-now-available-for-new-users-allowing-administrators|\U0001F465
  Default group assignment is now available for new users, allowing administrators…]]"
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in v0.6.37

**Open WebUI** · 2025-11-24 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖼️ Large stream chunk handling was implemented to support models that generate images directly in their output responses, with configurable buffer size via "CHAT_STREAM_RESPONSE_CHUNK_MAX_BUFFER_SIZE" environment variable, resolving compatibility issues with models like Gemini 2.5 Flash Image. [#18884](https://github.com/open-webui/open-webui/pull/18884), [#17626](https://github.com/open-webui/open-webui/issues/17626)

> 🖼️ Streaming response middleware now handles images in delta updates with automatic base64 conversion, enabling proper display of images from models using the "choices[0].delta.images.image_url" format such as Gemini 2.5 Flash Image Preview on OpenRouter. [#19073](https://github.com/open-webui/open-webui/pull/19073), [#19019](https://github.com/open-webui/open-webui/issues/19019)

> ⚡ Workspace models page now supports server-side pagination dramatically improving load times and usability for instances with large numbers of workspace models.

> 📌 Default pinned models can now be configured by administrators for all new users, mirroring the behavior of default models where admin-configured defaults apply only to users who haven't customized their pinned models, configurable via "DEFAULT_PINNED_MODELS" environment variable. [#19273](https://github.com/open-webui/open-webui/pull/19273)

> 🏷️ Tag suggestions are now context-aware, displaying only relevant tags when creating or editing models versus chat conversations, preventing confusion between model and chat tags. [#19135](https://github.com/open-webui/open-webui/issues/19135)

> 🤖 Model update functionality now works correctly, resolving a database parameter binding error that prevented saving changes to model configurations via the Save & Update button. [#19335](https://github.com/open-webui/open-webui/issues/19335)

> 🤖 Azure OpenAI models now support the "reasoning_effort" parameter, enabling proper configuration of reasoning capabilities for models like GPT-5.1 which default to no reasoning without this setting. [#19290](https://github.com/open-webui/open-webui/issues/19290)

> 🤖 Models with very long IDs can now be deleted correctly, resolving URL length limitations that previously prevented management operations on such models. [#18230](https://github.com/open-webui/open-webui/pull/18230)

> 🤖 Model-level streaming settings now correctly apply to API requests, ensuring "Stream Chat Response" toggle properly controls the streaming parameter. [#19154](https://github.com/open-webui/open-webui/issues/19154)

> 🎨 Gemini image edit settings now display correctly in the admin panel, fixing an incorrect configuration key reference that prevented proper rendering of edit options. [#19200](https://github.com/open-webui/open-webui/pull/19200)

> 📝 Notes chat feature now correctly submits messages to the completions endpoint, resolving errors that prevented AI model interactions. [#19079](https://github.com/open-webui/open-webui/pull/19079)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-24-3-search-and-browsing-changes-in-v0-6-37|3 Search and Browsing changes in v0.6.37]] · Search and Browsing
- [[Changes/Open WebUI/2025-11-24-model-cloning-is-now-available-in-admin-settings-allowing-administrators-to-quic|🤖 Model cloning is now available in admin settings, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin|🔐 Granular sharing permissions are now available with two-tiered control separating…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-5-interface-experience-changes-in-v0-6-37|5 Interface Experience changes in v0.6.37]] · Interface Experience
- [[Changes/Open WebUI/2025-11-24-granular-import-and-export-permissions-are-now-available-for-workspace-items-int|🔐 Granular import and export permissions are now available for workspace items…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-prompt-autocompletion-is-now-available-independently-of-the-rich-text-input-sett|✍️ Prompt autocompletion is now available independently of the rich text input…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-rag-template-query-placeholder-escaping-logic-was-corrected-to-prevent-unintende|📝 RAG template query placeholder escaping logic was corrected to prevent unintended…]] · Context Window
- [[Changes/Open WebUI/2025-11-24-default-group-assignment-is-now-available-for-new-users-allowing-administrators|👥 Default group assignment is now available for new users, allowing administrators…]] · Model Support
- [[Changes/Open WebUI/2025-11-24-2-voice-and-audio-changes-in-v0-6-37|2 Voice and Audio changes in v0.6.37]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-24-7-account-and-access-changes-in-v0-6-37|7 Account and Access changes in v0.6.37]] · Account and Access
- [[Changes/Open WebUI/2025-11-24-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-11-24-ui-scale-adjustment-is-now-available-in-interface-settings-allowing-users-to-inc|🎨 UI scale adjustment is now available in interface settings, allowing users…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-11-24-2-files-and-data-changes-in-v0-6-37|2 Files and Data changes in v0.6.37]] · Files and Data
- [[Changes/Open WebUI/2025-11-24-api-key-creation-is-now-controlled-by-granular-user-and-group-permissions-with-t|🔐 API key creation is now controlled by granular user and group permissions…]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-24-4-image-generation-changes-in-v0-6-37|4 Image Generation changes in v0.6.37]] · Image Generation
- [[Changes/Open WebUI/2025-11-24-websocket-and-redis-configuration-options-are-now-available-including-debug-logg|🔧 WebSocket and Redis configuration options are now available including debug…]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-24-pwa-installations-on-ios-now-properly-refresh-after-server-container-restarts-re|📱 PWA installations on iOS now properly refresh after server container restarts…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-24-9-reliability-and-performance-changes-in-v0-6-37|9 Reliability and Performance changes in v0.6.37]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-24-4-apps-and-integrations-changes-in-v0-6-37|4 Apps and Integrations changes in v0.6.37]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-24-password-policy-enforcement-is-now-available-with-configurable-validation-rules|🔐 Password policy enforcement is now available with configurable validation rules…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-24-other-changes-in-v0-6-37|24 other changes in v0.6.37]] · Other changes
- [[Changes/Open WebUI/2025-11-24-daily-active-user-metric-is-now-available-for-monitoring-tracking-unique-users-a|📊 Daily active user metric is now available for monitoring, tracking unique users…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-base64-image-conversion-is-now-available-for-markdown-content-in-chat-responses|💨 Base64 image conversion is now available for markdown content in chat responses…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-11-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-24-opus-4-5-gpt-4-1-and-gpt-5-mini-are-now-available-in-github-copilot-cli|Opus 4.5, GPT-4.1 and GPT-5-Mini are now available in GitHub Copilot CLI]]
- Later: 2025-11-24 · Windsurf · [[Changes/Windsurf/2025-11-24-1-12-36-claude-opus-4-5-changelog-banner|1.12.36 Claude Opus 4.5 changelog banner]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-d38a09&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-11-model-support-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-d38a09%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->