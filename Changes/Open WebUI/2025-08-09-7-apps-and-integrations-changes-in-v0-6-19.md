---
card_id: open-webui-2025-08-09-046229
date: '2025-08-09'
description: "Open WebUI · 2025-08-09 · Apps and Integrations: 7 changes in v0.6.19
  — \U0001F6E0️ **Improved Tool Call Handling for GPT-OSS Models**: Implemented robust
  handling for…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 870
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6fb638c49edd4168c44417a5ad51e030fab6fd6f76410a2e876fba476b2f1b93
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-09-046229
  comparison: ''
  date: '2025-08-09'
  description: 'Open WebUI — v0.6.19: 7 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F6E0️ **Improved Tool Call Handling for GPT-OSS Models**: Implemented
      robust handling for tool calls specifically for GPT-OSS models, ensuring proper
      function execution and integration."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '⚙️ **Configurable Datalab Marker API & Advanced Processing Options**:
      Enhanced Datalab Marker API integration, allowing administrators to configure
      custom API base URLs for self-hosting and to specify comprehensive processing
      options via a new ''additional_config'' JSON parameter. This replaces the deprecated
      language selection feature and provides granular control over document extraction,
      with streamlined API endpoint resolution for more robust self-hosted deployments.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F517 **Custom CORS Scheme Support**: Introduced a new environment
      variable 'CORS_ALLOW_CUSTOM_SCHEME' that allows administrators to define custom
      URL schemes (e.g., 'app://') for CORS origins, enabling greater flexibility
      for local development or desktop client integrations."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4E6 **Redis Cluster Connection Restored**: Fixed an issue where
      the backend was unable to connect to Redis in cluster mode, now ensuring seamless
      integration with scalable Redis cluster deployments."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6E0️ **OpenAPI Tool Integration for Array Parameters Fixed**: Resolved
      a critical bug where external tools using array parameters (e.g., for tags)
      would fail when used with OpenAI models. The system now correctly generates
      the required 'items' property in the function schema, restoring functionality
      and preventing '400 Bad Request' errors."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F527 **Improved Azure URL Detection**: The logic for identifying
      Azure OpenAI endpoints has been made more robust, ensuring all valid Azure URLs
      are now correctly detected for a smoother connection setup."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '❗ **Docling Integration Upgraded to v1 API (Breaking Change)**: The integration
      with the Docling document processing engine has been updated to its new, stable
      ''/v1'' API. This is required for compatibility with Docling version 1.0.0 and
      newer. As a result, older versions of Docling are no longer supported. Users
      who rely on Docling for document ingestion **must upgrade** their docling-serve
      instance to ensure continued functionality.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-apps-and-integrations-changes-in-v0-6-19
  source_release: open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v0.6.19
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-05-24-apps-and-integrations-changes-in-v0-1-17|24
  Apps and Integrations changes in v0.1.17]]'
- '[[Changes/Gemini CLI/2025-08-06-26-apps-and-integrations-changes-in-v0-1-18|26
  Apps and Integrations changes in v0.1.18]]'
- '[[Changes/Gamma/2025-08-08-we-ve-just-launched-our-generate-api-in-beta-for-gamma-pro-users-now-you-can-cre|We’ve
  just launched our Generate API in beta for Gamma Pro users! Now you can…]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v0.6.19
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v0.6.19

**Open WebUI** · 2025-08-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.19) · from [[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|v0.6.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛠️ **Improved Tool Call Handling for GPT-OSS Models**: Implemented robust handling for tool calls specifically for GPT-OSS models, ensuring proper function execution and integration.

> ⚙️ **Configurable Datalab Marker API & Advanced Processing Options**: Enhanced Datalab Marker API integration, allowing administrators to configure custom API base URLs for self-hosting and to specify comprehensive processing options via a new 'additional_config' JSON parameter. This replaces the deprecated language selection feature and provides granular control over document extraction, with streamlined API endpoint resolution for more robust self-hosted deployments.

> 🔗 **Custom CORS Scheme Support**: Introduced a new environment variable 'CORS_ALLOW_CUSTOM_SCHEME' that allows administrators to define custom URL schemes (e.g., 'app://') for CORS origins, enabling greater flexibility for local development or desktop client integrations.

> 📦 **Redis Cluster Connection Restored**: Fixed an issue where the backend was unable to connect to Redis in cluster mode, now ensuring seamless integration with scalable Redis cluster deployments.

> 🛠️ **OpenAPI Tool Integration for Array Parameters Fixed**: Resolved a critical bug where external tools using array parameters (e.g., for tags) would fail when used with OpenAI models. The system now correctly generates the required 'items' property in the function schema, restoring functionality and preventing '400 Bad Request' errors.

> 🔧 **Improved Azure URL Detection**: The logic for identifying Azure OpenAI endpoints has been made more robust, ensuring all valid Azure URLs are now correctly detected for a smoother connection setup.

> ❗ **Docling Integration Upgraded to v1 API (Breaking Change)**: The integration with the Docling document processing engine has been updated to its new, stable '/v1' API. This is required for compatibility with Docling version 1.0.0 and newer. As a result, older versions of Docling are no longer supported. Users who rely on Docling for document ingestion **must upgrade** their docling-serve instance to ensure continued functionality.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-09-2-editor-experience-changes-in-v0-6-19|2 Editor Experience changes in v0.6.19]] · Editor Experience
- [[Changes/Open WebUI/2025-08-09-3-enterprise-and-administration-changes-in-v0-6-19|3 Enterprise and Administration changes in v0.6.19]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-09-2-mobile-and-desktop-changes-in-v0-6-19|2 Mobile and Desktop changes in v0.6.19]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-09-2-search-and-browsing-changes-in-v0-6-19|2 Search and Browsing changes in v0.6.19]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-09-customizable-floating-quick-actions-with-tool-support-take-full-control-of-your|✍️ Customizable Floating Quick Actions with Tool Support]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-08-09-15-reliability-and-performance-changes-in-v0-6-19|15 Reliability and Performance changes in v0.6.19]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-09-2-files-and-data-changes-in-v0-6-19|2 Files and Data changes in v0.6.19]] · Files and Data
- [[Changes/Open WebUI/2025-08-09-folder-system-prompt-variables-restored-fixed-a-bug-where-prompt-variables-e-g-c|📁 Folder System Prompt Variables Restored]] · Context Window
- [[Changes/Open WebUI/2025-08-09-admin-first-whisper-language-priority-the-global-whisper-language-setting-now-ac|🗣️ Admin-First Whisper Language Priority]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-09-2-developer-workflow-changes-in-v0-6-19|2 Developer Workflow changes in v0.6.19]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-09-enhanced-memory-stability-and-security-refactored-memory-update-and-delete-opera|🧠 Enhanced Memory Stability and Security]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-09-11-model-support-changes-in-v0-6-19|11 Model Support changes in v0.6.19]] · Model Support
- [[Changes/Open WebUI/2025-08-09-4-account-and-access-changes-in-v0-6-19|4 Account and Access changes in v0.6.19]] · Account and Access
- [[Changes/Open WebUI/2025-08-09-10-safety-and-privacy-changes-in-v0-6-19|10 Safety and Privacy changes in v0.6.19]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-09-3-collaboration-changes-in-v0-6-19|3 Collaboration changes in v0.6.19]] · Collaboration
- [[Changes/Open WebUI/2025-08-09-3-accessibility-and-localization-changes-in-v0-6-19|3 Accessibility and Localization changes in v0.6.19]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-09-13-interface-experience-changes-in-v0-6-19|13 Interface Experience changes in v0.6.19]] · Interface Experience
- [[Changes/Open WebUI/2025-08-09-29-other-changes-in-v0-6-19|29 other changes in v0.6.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-08-08 · Gamma · [[Changes/Gamma/2025-08-08-we-ve-just-launched-our-generate-api-in-beta-for-gamma-pro-users-now-you-can-cre|We’ve just launched our Generate API in beta for Gamma Pro users! Now you can…]]
- Later: 2025-08-11 · Dify · [[Changes/Dify/2025-08-11-6-apps-and-integrations-changes-in-1-7-2|6 Apps and Integrations changes in 1.7.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-09-046229&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-09-7-apps-and-integrations-changes-in-v0-6-19.md%0ACard%20ID%3A%20open-webui-2025-08-09-046229%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->