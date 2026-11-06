---
card_id: open-webui-2025-08-28-3a42bf
date: '2025-08-28'
description: "Open WebUI · 2025-08-28 · Other changes: 7 changes in v0.6.26 — \U0001F4F1
  **Pull-to-Refresh Support**: Added pull-to-refresh functionality allowing user to
  easily…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 249d1fb8a2a40bcd6029725760d5ca9ea69231722af8e3d806453170aeef2a88
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-28-3a42bf
  comparison: ''
  date: '2025-08-28'
  description: 'Open WebUI — v0.6.26: 7 other changes'
  evidence:
  - quote: "\U0001F4F1 **Pull-to-Refresh Support**: Added pull-to-refresh functionality
      allowing user to easily refresh the interface by pulling down on the navbar
      area. This resolves timeout issues that occurred when temporarily switching
      away from the app during long AI response generations, eliminating the need
      to close and relaunch the PWA."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F4E6 **Slimmed Default Install with Optional Full Dependencies**:
      Installing Open WebUI via pip now defaults to a slimmer package; PostgreSQL
      support is no longer included by default—simply use 'pip install open-webui[all]'
      to include all optional dependencies for full feature compatibility."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: '⚠️ **Chat Error Feedback Restored**: Fixed an issue where various backend
      errors (tool server failures, API connection issues, malformed responses) would
      cause chats to load indefinitely without providing user feedback. The system
      now properly displays error messages when failures occur during chat generation,
      allowing users to understand issues and retry as needed instead of waiting indefinitely.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F4CB **Citation Error Handling Improved**: Fixed an issue where
      malformed citation or source objects from external tools, pipes, or filters
      would cause JavaScript errors and make the chat interface completely unresponsive.
      The system now gracefully handles missing or undefined citation properties,
      allowing conversations to load properly even when tools generate defective citation
      events."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F465 **Group User Add API Endpoint Fixed**: Fixed an issue where
      the \"/api/v1/groups/id/{group_id}/users/add\" API endpoint would accept requests
      without errors but fail to actually add users to groups. The system now properly
      initializes and deduplicates user ID lists, ensuring users are correctly added
      to and removed from groups via API calls."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F6E0️ **External Tool Server Error Handling Improved**: Fixed an
      issue where unreachable or misconfigured external tool servers would cause JavaScript
      errors and prevent the interface from loading properly. The system now gracefully
      handles connection failures, displays appropriate error messages, and filters
      out inaccessible servers while maintaining full functionality for working connections."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  - quote: "\U0001F4AC **RTL Text Orientation in Messages Fixed**: Fixed text alignment
      issues in user messages and AI responses for Right-to-Left languages, ensuring
      proper text direction based on user language settings. Code blocks now consistently
      use Left-to-Right orientation regardless of the user's language preference,
      maintaining code readability across all supported languages."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 7-other-changes-in-v0-6-26
  source_release: open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3
  source_type: github_releases
  theme: uncategorized
  title: 7 other changes in v0.6.26
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3]]'
source_type: github_releases
theme: uncategorized
title: 7 other changes in v0.6.26
type: change
---

<!-- chronolog:begin region="header" -->
# 7 other changes in v0.6.26

**Open WebUI** · 2025-08-28 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.26) · from [[Releases/Open WebUI/open-webui-2025-08-28-v0-6-26-github-243127257-72de72e3|v0.6.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📱 **Pull-to-Refresh Support**: Added pull-to-refresh functionality allowing user to easily refresh the interface by pulling down on the navbar area. This resolves timeout issues that occurred when temporarily switching away from the app during long AI response generations, eliminating the need to close and relaunch the PWA.

> 📦 **Slimmed Default Install with Optional Full Dependencies**: Installing Open WebUI via pip now defaults to a slimmer package; PostgreSQL support is no longer included by default—simply use 'pip install open-webui[all]' to include all optional dependencies for full feature compatibility.

> ⚠️ **Chat Error Feedback Restored**: Fixed an issue where various backend errors (tool server failures, API connection issues, malformed responses) would cause chats to load indefinitely without providing user feedback. The system now properly displays error messages when failures occur during chat generation, allowing users to understand issues and retry as needed instead of waiting indefinitely.

> 📋 **Citation Error Handling Improved**: Fixed an issue where malformed citation or source objects from external tools, pipes, or filters would cause JavaScript errors and make the chat interface completely unresponsive. The system now gracefully handles missing or undefined citation properties, allowing conversations to load properly even when tools generate defective citation events.

> 👥 **Group User Add API Endpoint Fixed**: Fixed an issue where the "/api/v1/groups/id/{group_id}/users/add" API endpoint would accept requests without errors but fail to actually add users to groups. The system now properly initializes and deduplicates user ID lists, ensuring users are correctly added to and removed from groups via API calls.

> 🛠️ **External Tool Server Error Handling Improved**: Fixed an issue where unreachable or misconfigured external tool servers would cause JavaScript errors and prevent the interface from loading properly. The system now gracefully handles connection failures, displays appropriate error messages, and filters out inaccessible servers while maintaining full functionality for working connections.

> 💬 **RTL Text Orientation in Messages Fixed**: Fixed text alignment issues in user messages and AI responses for Right-to-Left languages, ensuring proper text direction based on user language settings. Code blocks now consistently use Left-to-Right orientation regardless of the user's language preference, maintaining code readability across all supported languages.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-28-2-model-support-changes-in-v0-6-26|2 Model Support changes in v0.6.26]] · Model Support
- [[Changes/Open WebUI/2025-08-28-2-context-window-changes-in-v0-6-26|2 Context Window changes in v0.6.26]] · Context Window
- [[Changes/Open WebUI/2025-08-28-code-block-copy-button-content-fixed-fixed-an-issue-where-the-copy-button-in-cod|📋 Code Block Copy Button Content Fixed]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-28-2-safety-and-privacy-changes-in-v0-6-26|2 Safety and Privacy changes in v0.6.26]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-28-2-reliability-and-performance-changes-in-v0-6-26|2 Reliability and Performance changes in v0.6.26]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-28-2-interface-experience-changes-in-v0-6-26|2 Interface Experience changes in v0.6.26]] · Interface Experience
- [[Changes/Open WebUI/2025-08-28-2-account-and-access-changes-in-v0-6-26|2 Account and Access changes in v0.6.26]] · Account and Access
- [[Changes/Open WebUI/2025-08-28-pdf-export-content-mismatch-fixed-resolved-an-issue-where-exporting-a-pdf-of-one|📄 PDF Export Content Mismatch Fixed]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-28-2-accessibility-and-localization-changes-in-v0-6-26|2 Accessibility and Localization changes in v0.6.26]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-28-2-search-and-browsing-changes-in-v0-6-26|2 Search and Browsing changes in v0.6.26]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-28-configurable-file-upload-processing-mode-added-process-in-background-query-param|📁 Configurable File Upload Processing Mode]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-28-3-files-and-data-changes-in-v0-6-26|3 Files and Data changes in v0.6.26]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-28-3a42bf&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-28-7-other-changes-in-v0-6-26.md%0ACard%20ID%3A%20open-webui-2025-08-28-3a42bf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->