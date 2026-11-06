---
card_id: open-webui-2025-08-21-dc7270
date: '2025-08-21'
description: "Open WebUI · 2025-08-21 · Apps and Integrations: 5 changes in v0.6.23
  — \U0001F464 **Expanded User Profile Details**: Introduced new user profile fields
  including…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 882
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 15c831bc27f0fb0d3f07b6ba83818bbc3baa4f3754e3f39bb88e1e145e855a62
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-dc7270
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 5 Apps and Integrations changes'
  evidence:
  - quote: "\U0001F464 **Expanded User Profile Details**: Introduced new user profile
      fields including username, bio, gender, and date of birth, allowing for more
      comprehensive user customization and information management. This enhancement
      includes corresponding updates to the database schema, API, and user interface
      for seamless integration."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F527 **Enhanced External Tool Server Compatibility**: Improved handling
      of responses from external tool servers, allowing both the backend and frontend
      to process plain text content in addition to JSON, ensuring greater flexibility
      and integration with diverse tool outputs."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: '⚙️ **Configurable Tool Call Timeout**: Introduced the "AIOHTTP_CLIENT_TIMEOUT"
      environment variable, allowing administrators to specify custom timeout durations
      for external tool calls, which is crucial for integrations with tools that have
      varying or extended response times.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F6E0️ **Improved Tool Callable Generation for Google genai SDK**:
      Enhanced the creation of tool callables to directly support native function
      calling within the Google 'genai' SDK. This refactoring ensures proper signature
      inference and removes extraneous parameters, enabling seamless integration for
      advanced AI workflows using Google's generative AI models."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4E5 **Fixed Community Function Import Compatibility**: Resolved
      an issue that prevented the successful import of function files downloaded from
      openwebui.com due to schema differences. The system now correctly processes
      these files, allowing for seamless integration of community-contributed functions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-apps-and-integrations-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v0.6.23
  type: change
related_changes:
- '[[Changes/OpenHands/2025-08-20-2-apps-and-integrations-changes-in-0-54-0|2 Apps
  and Integrations changes in 0.54.0]]'
- '[[Changes/Cline/2025-08-21-feat-telemetry-add-mcp-tool-usage-tracking-by-nighttrek-in-https-github-com-clin|feat(telemetry):
  Add MCP tool usage tracking]]'
- '[[Changes/Cursor/2025-08-21-cursor-now-supports-mcp-elicitation-a-new-feature-in-the-mcp-spec-that-allows-se|Support
  for MCP elicitation]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 👤 **Expanded User Profile Details**: Introduced new user profile fields including username, bio, gender, and date of birth, allowing for more comprehensive user customization and information management. This enhancement includes corresponding updates to the database schema, API, and user interface for seamless integration.

> 🔧 **Enhanced External Tool Server Compatibility**: Improved handling of responses from external tool servers, allowing both the backend and frontend to process plain text content in addition to JSON, ensuring greater flexibility and integration with diverse tool outputs.

> ⚙️ **Configurable Tool Call Timeout**: Introduced the "AIOHTTP_CLIENT_TIMEOUT" environment variable, allowing administrators to specify custom timeout durations for external tool calls, which is crucial for integrations with tools that have varying or extended response times.

> 🛠️ **Improved Tool Callable Generation for Google genai SDK**: Enhanced the creation of tool callables to directly support native function calling within the Google 'genai' SDK. This refactoring ensures proper signature inference and removes extraneous parameters, enabling seamless integration for advanced AI workflows using Google's generative AI models.

> 📥 **Fixed Community Function Import Compatibility**: Resolved an issue that prevented the successful import of function files downloaded from openwebui.com due to schema differences. The system now correctly processes these files, allowing for seamless integration of community-contributed functions.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-21-8-interface-experience-changes-in-v0-6-23|8 Interface Experience changes in v0.6.23]] · Interface Experience
- [[Changes/Open WebUI/2025-08-21-restored-message-toolbar-icons-for-empty-messages-with-files-fixed-an-issue-wher|🐛 Restored Message Toolbar Icons for Empty Messages with Files]] · Editor Experience
- [[Changes/Open WebUI/2025-08-21-3-search-and-browsing-changes-in-v0-6-23|3 Search and Browsing changes in v0.6.23]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-21-resolved-silently-dropped-streaming-response-chunks-fixed-an-issue-where-the-fin|💬 Resolved Silently Dropped Streaming Response Chunks]] · Files and Data
- [[Changes/Open WebUI/2025-08-21-3-mobile-and-desktop-changes-in-v0-6-23|3 Mobile and Desktop changes in v0.6.23]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-21-6-reliability-and-performance-changes-in-v0-6-23|6 Reliability and Performance changes in v0.6.23]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-21-2-voice-and-audio-changes-in-v0-6-23|2 Voice and Audio changes in v0.6.23]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]] · Model Support
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-08-21 · Cursor · [[Changes/Cursor/2025-08-21-cursor-now-supports-mcp-elicitation-a-new-feature-in-the-mcp-spec-that-allows-se|Support for MCP elicitation]]
- Later: 2025-08-22 · Open WebUI · [[Changes/Open WebUI/2025-08-22-tool-server-loading-and-visibility-restored-resolved-an-issue-where-connected-to|🛠️ Tool Server Loading and Visibility Restored]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-dc7270&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-5-apps-and-integrations-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-dc7270%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->