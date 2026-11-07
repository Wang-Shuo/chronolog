---
card_id: open-webui-2025-08-21-4193ba
date: '2025-08-21'
description: "Open WebUI · 2025-08-21 · Safety and Privacy: 6 changes in v0.6.23 —
  \U0001F512 **Configurable Code Interpreter Module Blacklist**: Introduced the…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 858
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c5895512378f13aea4455391ffcf3d7e7a3416445413d81932e68c98869781c1
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-21-4193ba
  comparison: ''
  date: '2025-08-21'
  description: 'Open WebUI — v0.6.23: 6 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F512 **Configurable Code Interpreter Module Blacklist**: Introduced
      the \"CODE_INTERPRETER_BLACKLISTED_MODULES\" environment variable, allowing
      administrators to specify Python modules that are forbidden from being imported
      or executed within the code interpreter. This significantly enhances the security
      posture by mitigating risks associated with arbitrary code execution, such as
      unauthorized data access, system manipulation, or outbound connections."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4E6 **Improved Docker Image Compatibility for Arbitrary UIDs**:
      Fixed issues preventing the Open WebUI container from running in environments
      with arbitrary User IDs (UIDs), such as OpenShift's restricted Security Context
      Constraints (SCC). The Dockerfile has been updated to correctly set file system
      permissions for \"/app\" and \"/root\" directories, ensuring they are writable
      by processes running with a supplemental GID 0, thus resolving permission errors
      for Python libraries and application caches."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F4AC **Resolved Temporary Chat and Permission Enforcement Issues**:
      Fixed a bug where temporary chats (identified by \"chat_id = local\") incorrectly
      triggered database checks, leading to 404 errors. This also resolves the issue
      where the 'USER_PERMISSIONS_CHAT_TEMPORARY_ENFORCED' setting was not functioning
      as intended, ensuring temporary chat mode now works correctly for user roles."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F510 **Admin Model Visibility for Administrators**: Private models
      remained visible and usable for administrators in the chat model selector, even
      when the intended privacy setting (\"ENABLE_ADMIN_WORKSPACE_CONTENT_ACCESS\"
      - now renamed to \"BYPASS_ADMIN_ACCESS_CONTROL\") was disabled. This ensures
      consistent enforcement of model access controls and adherence to the principle
      of least privilege."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F5C4️ **Resolved Azure PostgreSQL pgvector Extension Permissions**:
      Fixed an issue preventing the creation of \"pgvector\" and \"pgcrypto\" extensions
      on Azure PostgreSQL Flexible Servers due to permission limitations (e.g., 'Only
      members of \"azure_pg_admin\" are allowed to use \"CREATE EXTENSION\"'). The
      extension creation process now includes a conditional check, ensuring seamless
      deployment and compatibility with Azure PostgreSQL environments even with restricted
      database user permissions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  - quote: "\U0001F41B **Resolved Exception with Missing Group Permissions**: Fixed
      an exception that occurred in the access control logic when group permission
      objects were missing or null. The system now correctly handles cases where groups
      may not have explicit permission definitions, ensuring that 'None' checks prevent
      errors and maintain application stability when processing user permissions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-safety-and-privacy-changes-in-v0-6-23
  source_release: open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v0.6.23
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-13-ensure-sandbox-build-script-is-cross-platform-by-wldoooon-in-https-github-com-go|ensure
  sandbox build script is cross-platform]]'
- '[[Changes/Gemini CLI/2025-08-14-7-safety-and-privacy-changes-in-v0-1-21|7 Safety
  and Privacy changes in v0.1.21]]'
- '[[Changes/Codex CLI/2025-08-20-2464-https-github-com-openai-codex-pull-2464-docs-document-writable-roots-for-sa|♯2464((source
  link) docs: document writable_roots…]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v0.6.23
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v0.6.23

**Open WebUI** · 2025-08-21 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.23) · from [[Releases/Open WebUI/open-webui-2025-08-21-v0-6-23-github-241603918-5e4a7f46|v0.6.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 **Configurable Code Interpreter Module Blacklist**: Introduced the "CODE_INTERPRETER_BLACKLISTED_MODULES" environment variable, allowing administrators to specify Python modules that are forbidden from being imported or executed within the code interpreter. This significantly enhances the security posture by mitigating risks associated with arbitrary code execution, such as unauthorized data access, system manipulation, or outbound connections.

> 📦 **Improved Docker Image Compatibility for Arbitrary UIDs**: Fixed issues preventing the Open WebUI container from running in environments with arbitrary User IDs (UIDs), such as OpenShift's restricted Security Context Constraints (SCC). The Dockerfile has been updated to correctly set file system permissions for "/app" and "/root" directories, ensuring they are writable by processes running with a supplemental GID 0, thus resolving permission errors for Python libraries and application caches.

> 💬 **Resolved Temporary Chat and Permission Enforcement Issues**: Fixed a bug where temporary chats (identified by "chat_id = local") incorrectly triggered database checks, leading to 404 errors. This also resolves the issue where the 'USER_PERMISSIONS_CHAT_TEMPORARY_ENFORCED' setting was not functioning as intended, ensuring temporary chat mode now works correctly for user roles.

> 🔐 **Admin Model Visibility for Administrators**: Private models remained visible and usable for administrators in the chat model selector, even when the intended privacy setting ("ENABLE_ADMIN_WORKSPACE_CONTENT_ACCESS" - now renamed to "BYPASS_ADMIN_ACCESS_CONTROL") was disabled. This ensures consistent enforcement of model access controls and adherence to the principle of least privilege.

> 🗄️ **Resolved Azure PostgreSQL pgvector Extension Permissions**: Fixed an issue preventing the creation of "pgvector" and "pgcrypto" extensions on Azure PostgreSQL Flexible Servers due to permission limitations (e.g., 'Only members of "azure_pg_admin" are allowed to use "CREATE EXTENSION"'). The extension creation process now includes a conditional check, ensuring seamless deployment and compatibility with Azure PostgreSQL environments even with restricted database user permissions.

> 🐛 **Resolved Exception with Missing Group Permissions**: Fixed an exception that occurred in the access control logic when group permission objects were missing or null. The system now correctly handles cases where groups may not have explicit permission definitions, ensuring that 'None' checks prevent errors and maintain application stability when processing user permissions.

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
- [[Changes/Open WebUI/2025-08-21-2-voice-and-audio-changes-in-v0-6-23|2 Voice and Audio changes in v0.6.23]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-21-2-accessibility-and-localization-changes-in-v0-6-23|2 Accessibility and Localization changes in v0.6.23]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-21-7-model-support-changes-in-v0-6-23|7 Model Support changes in v0.6.23]] · Model Support
- [[Changes/Open WebUI/2025-08-21-resolved-image-generation-api-size-parameter-issue-fixed-a-bug-where-the-api-v1|🖼️ Resolved Image Generation API Size Parameter Issue]] · Image Generation
- [[Changes/Open WebUI/2025-08-21-resolved-code-block-input-issue-with-shift-enter-fixed-a-bug-where-typing-three|📝 Resolved Code Block Input Issue with Shift+Enter]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-21-5-apps-and-integrations-changes-in-v0-6-23|5 Apps and Integrations changes in v0.6.23]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-21-3-account-and-access-changes-in-v0-6-23|3 Account and Access changes in v0.6.23]] · Account and Access
- [[Changes/Open WebUI/2025-08-21-23-other-changes-in-v0-6-23|23 other changes in v0.6.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-08-20 · Codex CLI · [[Changes/Codex CLI/2025-08-20-2464-https-github-com-openai-codex-pull-2464-docs-document-writable-roots-for-sa|♯2464((source link) docs: document writable_roots…]]
- Later: 2025-08-22 · Replit · [[Changes/Replit/2025-08-22-soc-2-type-ii-certification|SOC 2 Type II certification]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-21-4193ba&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-21-6-safety-and-privacy-changes-in-v0-6-23.md%0ACard%20ID%3A%20open-webui-2025-08-21-4193ba%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->