---
card_id: open-webui-2025-11-24-016a5b
date: '2025-11-24'
description: "Open WebUI · 2025-11-24 · Search and Browsing: 3 changes in v0.6.37
  — \U0001F50D Azure AI Search is now supported as a web search provider, enabling
  integration with…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 977
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4ab104014a6675cbf6372cdf6e21c019cfbc4d509b86b8b238f75a4f4c080567
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-24-016a5b
  comparison: ''
  date: '2025-11-24'
  description: 'Open WebUI — v0.6.37: 3 Search and Browsing changes'
  evidence:
  - quote: "\U0001F50D Azure AI Search is now supported as a web search provider,
      enabling integration with Azure's cognitive search services via \"AZURE_AI_SEARCH_API_KEY\",
      \"AZURE_AI_SEARCH_ENDPOINT\", and \"AZURE_AI_SEARCH_INDEX_NAME\" configuration.
      [#19104](https://github.com/open-webui/open-webui/pull/19104)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F50D Perplexity Search now supports custom API endpoints via \"PERPLEXITY_SEARCH_API_URL\"
      configuration and automatically forwards user information headers to enable
      personalized search experiences. [#19147](https://github.com/open-webui/open-webui/pull/19147)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  - quote: "\U0001F50D User information headers can now be optionally forwarded to
      external web search engines when \"ENABLE_FORWARD_USER_INFO_HEADERS\" is enabled.
      [#19043](https://github.com/open-webui/open-webui/pull/19043)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-search-and-browsing-changes-in-v0-6-37
  source_release: open-webui-2025-11-24-v0-6-37-github-264669867-8b715894
  source_type: github_releases
  theme: search-browsing
  title: 3 Search and Browsing changes in v0.6.37
  type: change
related_changes:
- '[[Changes/Open WebUI/2025-11-06-4-search-and-browsing-changes-in-v0-6-35|4 Search
  and Browsing changes in v0.6.35]]'
- '[[Changes/Codex CLI/2025-11-09-6367-sdk-add-network-access-and-web-search-options-to-typescript-sdk|♯6367
  – SDK: add network_access and web_search options to TypeScript SDK]]'
- '[[Changes/Codex CLI/2025-11-13-2-search-and-browsing-changes-in-rust-v0-58-0|2
  Search and Browsing changes in rust-v0.58.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|open-webui-2025-11-24-v0-6-37-github-264669867-8b715894]]'
source_type: github_releases
theme: search-browsing
title: 3 Search and Browsing changes in v0.6.37
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Search and Browsing changes in v0.6.37

**Open WebUI** · 2025-11-24 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.37) · from [[Releases/Open WebUI/open-webui-2025-11-24-v0-6-37-github-264669867-8b715894|v0.6.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔍 Azure AI Search is now supported as a web search provider, enabling integration with Azure's cognitive search services via "AZURE_AI_SEARCH_API_KEY", "AZURE_AI_SEARCH_ENDPOINT", and "AZURE_AI_SEARCH_INDEX_NAME" configuration. [#19104](https://github.com/open-webui/open-webui/pull/19104)

> 🔍 Perplexity Search now supports custom API endpoints via "PERPLEXITY_SEARCH_API_URL" configuration and automatically forwards user information headers to enable personalized search experiences. [#19147](https://github.com/open-webui/open-webui/pull/19147)

> 🔍 User information headers can now be optionally forwarded to external web search engines when "ENABLE_FORWARD_USER_INFO_HEADERS" is enabled. [#19043](https://github.com/open-webui/open-webui/pull/19043)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.37
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Open WebUI/2025-11-24-11-model-support-changes-in-v0-6-37|11 Model Support changes in v0.6.37]] · Model Support
- [[Changes/Open WebUI/2025-11-24-9-reliability-and-performance-changes-in-v0-6-37|9 Reliability and Performance changes in v0.6.37]] · Reliability and Performance
- [[Changes/Open WebUI/2025-11-24-4-apps-and-integrations-changes-in-v0-6-37|4 Apps and Integrations changes in v0.6.37]] · Apps and Integrations
- [[Changes/Open WebUI/2025-11-24-password-policy-enforcement-is-now-available-with-configurable-validation-rules|🔐 Password policy enforcement is now available with configurable validation rules…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-24-other-changes-in-v0-6-37|24 other changes in v0.6.37]] · Other changes
- [[Changes/Open WebUI/2025-11-24-daily-active-user-metric-is-now-available-for-monitoring-tracking-unique-users-a|📊 Daily active user metric is now available for monitoring, tracking unique users…]] · Other changes
- [[Changes/Open WebUI/2025-11-24-base64-image-conversion-is-now-available-for-markdown-content-in-chat-responses|💨 Base64 image conversion is now available for markdown content in chat responses…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Search and Browsing

- Earlier: 2025-11-13 · Codex CLI · [[Changes/Codex CLI/2025-11-13-2-search-and-browsing-changes-in-rust-v0-58-0|2 Search and Browsing changes in rust-v0.58.0]]
- Later: 2025-11-26 · Lovable · [[Changes/Lovable/2025-11-26-better-commit-messages|Better commit messages]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-24-016a5b&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-24-3-search-and-browsing-changes-in-v0-6-37.md%0ACard%20ID%3A%20open-webui-2025-11-24-016a5b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.37%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->