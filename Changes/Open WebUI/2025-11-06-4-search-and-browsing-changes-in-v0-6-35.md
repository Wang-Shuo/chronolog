---
card_id: open-webui-2025-11-06-6dbc50
date: '2025-11-06'
description: "Open WebUI · 2025-11-06 · Search and Browsing: 4 changes in v0.6.35
  — \U0001F517 Web search SSL verification is now asynchronous, preventing the website
  from hanging…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing:
    An experimental model that knows when and how to browse the internet]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 959
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: search-browsing
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ee9aa8211267e924dfdf8e9eda169b4f679a04541d3e4592022e73675fcbf894
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-11-06-6dbc50
  comparison: ''
  date: '2025-11-06'
  description: 'Open WebUI — v0.6.35: 4 Search and Browsing changes'
  evidence:
  - quote: "\U0001F517 Web search SSL verification is now asynchronous, preventing
      the website from hanging during web search operations. [#18714](https://github.com/open-webui/open-webui/pull/18714),
      [#18699](https://github.com/open-webui/open-webui/issues/18699)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F30D Web search results now correctly use HTTP proxy environment
      variables when WEB_SEARCH_TRUST_ENV is enabled. [#18667](https://github.com/open-webui/open-webui/pull/18667),
      [#7008](https://github.com/open-webui/open-webui/discussions/7008)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F50D Google Programmable Search Engine now properly includes referer
      headers, enabling API keys with HTTP referrer restrictions configured in Google
      Cloud Console. [#18871](https://github.com/open-webui/open-webui/pull/18871),
      [#18870](https://github.com/open-webui/open-webui/issues/18870)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  - quote: "\U0001F50D Chat preview loading in the search modal now works correctly
      for all search results by fixing an index boundary check that previously caused
      out-of-bounds errors. [#18911](https://github.com/open-webui/open-webui/pull/18911)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-search-and-browsing-changes-in-v0-6-35
  source_release: open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234
  source_type: github_releases
  theme: search-browsing
  title: 4 Search and Browsing changes in v0.6.35
  type: change
related_changes:
- '[[Changes/Replit/2025-10-03-app-themes-font-improvements|App Themes font improvements]]'
- '[[Changes/Open WebUI/2025-10-07-2-search-and-browsing-changes-in-v0-6-33|2 Search
  and Browsing changes in v0.6.33]]'
- '[[Changes/Gemini CLI/2025-10-22-refactor-core-migrate-web-search-tool-to-tool-names-by-abhipatel12-in-https-gith|refactor(core):
  migrate web search tool to tool-names]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234]]'
source_type: github_releases
theme: search-browsing
title: 4 Search and Browsing changes in v0.6.35
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Search and Browsing changes in v0.6.35

**Open WebUI** · 2025-11-06 · [[Themes/search-browsing|Search and Browsing]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.35) · from [[Releases/Open WebUI/open-webui-2025-11-06-v0-6-35-github-260376122-7fa65234|v0.6.35]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔗 Web search SSL verification is now asynchronous, preventing the website from hanging during web search operations. [#18714](https://github.com/open-webui/open-webui/pull/18714), [#18699](https://github.com/open-webui/open-webui/issues/18699)

> 🌍 Web search results now correctly use HTTP proxy environment variables when WEB_SEARCH_TRUST_ENV is enabled. [#18667](https://github.com/open-webui/open-webui/pull/18667), [#7008](https://github.com/open-webui/open-webui/discussions/7008)

> 🔍 Google Programmable Search Engine now properly includes referer headers, enabling API keys with HTTP referrer restrictions configured in Google Cloud Console. [#18871](https://github.com/open-webui/open-webui/pull/18871), [#18870](https://github.com/open-webui/open-webui/issues/18870)

> 🔍 Chat preview loading in the search modal now works correctly for all search results by fixing an index boundary check that previously caused out-of-bounds errors. [#18911](https://github.com/open-webui/open-webui/pull/18911)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.35
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-11-06-chat-controls-button-is-now-properly-hidden-on-mobile-for-users-without-admin-or|📱 Chat controls button is now properly hidden on mobile for users without admin…]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-11-06-3-voice-and-audio-changes-in-v0-6-35|3 Voice and Audio changes in v0.6.35]] · Voice and Audio
- [[Changes/Open WebUI/2025-11-06-10-model-support-changes-in-v0-6-35|10 Model Support changes in v0.6.35]] · Model Support
- [[Changes/Open WebUI/2025-11-06-2-multimodal-input-changes-in-v0-6-35|2 Multimodal Input changes in v0.6.35]] · Multimodal Input
- [[Changes/Open WebUI/2025-11-06-4-safety-and-privacy-changes-in-v0-6-35|4 Safety and Privacy changes in v0.6.35]] · Safety and Privacy
- [[Changes/Open WebUI/2025-11-06-3-developer-workflow-changes-in-v0-6-35|3 Developer Workflow changes in v0.6.35]] · Developer Workflow
- [[Changes/Open WebUI/2025-11-06-10-interface-experience-changes-in-v0-6-35|10 Interface Experience changes in v0.6.35]] · Interface Experience
- [[Changes/Open WebUI/2025-11-06-3-editor-experience-changes-in-v0-6-35|3 Editor Experience changes in v0.6.35]] · Editor Experience
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
## Nearby in Search and Browsing

- Earlier: 2025-10-22 · Gemini CLI · [[Changes/Gemini CLI/2025-10-22-refactor-core-migrate-web-search-tool-to-tool-names-by-abhipatel12-in-https-gith|refactor(core): migrate web search tool to tool-names]]
- Later: 2025-11-09 · Codex CLI · [[Changes/Codex CLI/2025-11-09-6367-sdk-add-network-access-and-web-search-options-to-typescript-sdk|♯6367 – SDK: add network_access and web_search options to TypeScript SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-browsing-an-experimental-model-that-knows-when-and-how-to-browse-the-internet|Browsing: An experimental model that knows when and how to browse the internet]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-11-06-6dbc50&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-11-06-4-search-and-browsing-changes-in-v0-6-35.md%0ACard%20ID%3A%20open-webui-2025-11-06-6dbc50%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.35%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->