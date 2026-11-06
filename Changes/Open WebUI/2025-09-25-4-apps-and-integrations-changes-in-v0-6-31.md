---
card_id: open-webui-2025-09-25-0445e4
date: '2025-09-25'
description: "Open WebUI · 2025-09-25 · Apps and Integrations: 4 changes in v0.6.31
  — \U0001F50C MCP (streamable HTTP) server support was added alongside existing OpenAPI
  server…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 917
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2bf359c7088c1bdf5d12f065ca79633bce9be0b37d9d0e5ad396712284697c7e
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-09-25-0445e4
  comparison: ''
  date: '2025-09-25'
  description: 'Open WebUI — v0.6.31: 4 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F50C MCP (streamable HTTP) server support was added alongside existing
      OpenAPI server integration, allowing users to connect both server types through
      an improved server configuration interface. [#15932](https://github.com/open-webui/open-webui/issues/15932)
      [#16651](https://github.com/open-webui/open-webui/pull/16651), [Commit](https://github.com/open-webui/open-webui/commit/fd7385c3921eb59af76a26f4c475aedb38ce2406),
      [Commit](https://github.com/open-webui/open-webui/commit/777e81f7a8aca957a359d51df8388e5af4721a68),
      [Commit](https://github.com/open-webui/open-webui/commit/de7f7b3d855641450f8e5aac34fbae0665e0b80e),
      [Commit](https://github.com/open-webui/open-webui/commit/f1bbf3a91e4713039364b790e886e59b401572d0),
      [Commit](https://github.com/open-webui/open-webui/commit/c55afc42559c32a6f0c8beb0f1bb18e9360ab8af),
      [Commit](https://github.com/open-webui/open-webui/commit/61f20acf61f4fe30c0e5b0180949f6e1a8cf6524)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: "\U0001F50D Perplexity Websearch API integration was added as a new search
      engine option, providing access to the new websearch functionality provided
      by Perplexity. [#17756](https://github.com/open-webui/open-webui/issues/17756),
      [Commit](https://github.com/open-webui/open-webui/pull/17747/commits/7f411dd5cc1c29733216f79e99eeeed0406a2afe)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: ☁️ OneDrive integration was improved to support separate client IDs for
      personal and business authentication, enabling both integrations to work simultaneously.
      [#17619](https://github.com/open-webui/open-webui/pull/17619), [Docs](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint),
      [Docs](https://docs.openwebui.com/getting-started/env-configuration/#onedrive)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  - quote: ☁️ OneDrive environment variable configuration was updated to use separate
      ONEDRIVE_CLIENT_ID_PERSONAL and ONEDRIVE_CLIENT_ID_BUSINESS variables for better
      client ID separation, while maintaining backward compatibility with the legacy
      ONEDRIVE_CLIENT_ID variable. [Docs](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint),
      [Docs](https://docs.openwebui.com/getting-started/env-configuration/#onedrive)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-apps-and-integrations-changes-in-v0-6-31
  source_release: open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v0.6.31
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-09-23-2-apps-and-integrations-changes-in-rust-v0-40-0|2
  Apps and Integrations changes in rust-v0.40.0]]'
- '[[Changes/Gemini CLI/2025-09-24-5-apps-and-integrations-changes-in-v0-6-0|5 Apps
  and Integrations changes in v0.6.0]]'
- '[[Changes/Cline/2025-09-25-rename-mcp-tab-installed-to-configure-by-saoudrizwan-in-https-github-com-cline-c|Rename
  MCP tab ''Installed'' to ''Configure'']]'
source_release: '[[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v0.6.31
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v0.6.31

**Open WebUI** · 2025-09-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.31) · from [[Releases/Open WebUI/open-webui-2025-09-25-v0-6-31-github-250127383-773b3ead|v0.6.31]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔌 MCP (streamable HTTP) server support was added alongside existing OpenAPI server integration, allowing users to connect both server types through an improved server configuration interface. [#15932](https://github.com/open-webui/open-webui/issues/15932) [#16651](https://github.com/open-webui/open-webui/pull/16651), [Commit](https://github.com/open-webui/open-webui/commit/fd7385c3921eb59af76a26f4c475aedb38ce2406), [Commit](https://github.com/open-webui/open-webui/commit/777e81f7a8aca957a359d51df8388e5af4721a68), [Commit](https://github.com/open-webui/open-webui/commit/de7f7b3d855641450f8e5aac34fbae0665e0b80e), [Commit](https://github.com/open-webui/open-webui/commit/f1bbf3a91e4713039364b790e886e59b401572d0), [Commit](https://github.com/open-webui/open-webui/commit/c55afc42559c32a6f0c8beb0f1bb18e9360ab8af), [Commit](https://github.com/open-webui/open-webui/commit/61f20acf61f4fe30c0e5b0180949f6e1a8cf6524)

> 🔍 Perplexity Websearch API integration was added as a new search engine option, providing access to the new websearch functionality provided by Perplexity. [#17756](https://github.com/open-webui/open-webui/issues/17756), [Commit](https://github.com/open-webui/open-webui/pull/17747/commits/7f411dd5cc1c29733216f79e99eeeed0406a2afe)

> ☁️ OneDrive integration was improved to support separate client IDs for personal and business authentication, enabling both integrations to work simultaneously. [#17619](https://github.com/open-webui/open-webui/pull/17619), [Docs](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint), [Docs](https://docs.openwebui.com/getting-started/env-configuration/#onedrive)

> ☁️ OneDrive environment variable configuration was updated to use separate ONEDRIVE_CLIENT_ID_PERSONAL and ONEDRIVE_CLIENT_ID_BUSINESS variables for better client ID separation, while maintaining backward compatibility with the legacy ONEDRIVE_CLIENT_ID variable. [Docs](https://docs.openwebui.com/tutorials/integrations/onedrive-sharepoint), [Docs](https://docs.openwebui.com/getting-started/env-configuration/#onedrive)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.31
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-09-25-editor-collaboration-functionality-was-refactored-to-reduce-package-size-by-390k|⚡ Editor collaboration functionality was refactored to reduce package size by 390KB…]] · Collaboration
- [[Changes/Open WebUI/2025-09-25-2-editor-experience-changes-in-v0-6-31|2 Editor Experience changes in v0.6.31]] · Editor Experience
- [[Changes/Open WebUI/2025-09-25-rag-query-generation-is-now-skipped-when-all-attached-files-are-set-to-full-cont|🔍 RAG query generation is now skipped when all attached files are set to full…]] · Context Window
- [[Changes/Open WebUI/2025-09-25-3-safety-and-privacy-changes-in-v0-6-31|3 Safety and Privacy changes in v0.6.31]] · Safety and Privacy
- [[Changes/Open WebUI/2025-09-25-4-model-support-changes-in-v0-6-31|4 Model Support changes in v0.6.31]] · Model Support
- [[Changes/Open WebUI/2025-09-25-enhanced-user-interface-accessibility-through-the-addition-of-unique-element-ids|♿ Enhanced user interface accessibility through the addition of unique element IDs…]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-09-25-2-search-and-browsing-changes-in-v0-6-31|2 Search and Browsing changes in v0.6.31]] · Search and Browsing
- [[Changes/Open WebUI/2025-09-25-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-09-25-image-generation-model-selection-was-centralized-to-enable-dynamic-model-overrid|🎨 Image generation model selection was centralized to enable dynamic model override…]] · Image Generation
- [[Changes/Open WebUI/2025-09-25-4-interface-experience-changes-in-v0-6-31|4 Interface Experience changes in v0.6.31]] · Interface Experience
- [[Changes/Open WebUI/2025-09-25-file-upload-handling-was-improved-to-properly-recognize-uploaded-files-even-when|📎 File upload handling was improved to properly recognize uploaded files even…]] · Files and Data
- [[Changes/Open WebUI/2025-09-25-2-account-and-access-changes-in-v0-6-31|2 Account and Access changes in v0.6.31]] · Account and Access
- [[Changes/Open WebUI/2025-09-25-5-reliability-and-performance-changes-in-v0-6-31|5 Reliability and Performance changes in v0.6.31]] · Reliability and Performance
- [[Changes/Open WebUI/2025-09-25-2-developer-workflow-changes-in-v0-6-31|2 Developer Workflow changes in v0.6.31]] · Developer Workflow
- [[Changes/Open WebUI/2025-09-25-17-other-changes-in-v0-6-31|17 other changes in v0.6.31]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-09-25 · Cline · [[Changes/Cline/2025-09-25-rename-mcp-tab-installed-to-configure-by-saoudrizwan-in-https-github-com-cline-c|Rename MCP tab 'Installed' to 'Configure']]
- Later: 2025-09-26 · Codex CLI · [[Changes/Codex CLI/2025-09-26-4-apps-and-integrations-changes-in-rust-v0-42-0|4 Apps and Integrations changes in rust-v0.42.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-09-25-0445e4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-09-25-4-apps-and-integrations-changes-in-v0-6-31.md%0ACard%20ID%3A%20open-webui-2025-09-25-0445e4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.31%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->