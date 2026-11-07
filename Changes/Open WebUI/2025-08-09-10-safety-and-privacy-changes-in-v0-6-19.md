---
card_id: open-webui-2025-08-09-ddbd92
date: '2025-08-09'
description: "Open WebUI · 2025-08-09 · Safety and Privacy: 10 changes in v0.6.19
  — \U0001F510 **Encrypted SQLite Database with SQLCipher**: You can now encrypt your
  entire SQLite…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1838
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4036cf16a7162c78eb4318c011a377b5ba45497f64f5c281c5d88a4a9aca67b3
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-09-ddbd92
  comparison: ''
  date: '2025-08-09'
  description: 'Open WebUI — v0.6.19: 10 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F510 **Encrypted SQLite Database with SQLCipher**: You can now encrypt
      your entire SQLite database at rest using SQLCipher. By setting the 'DATABASE_TYPE'
      to 'sqlite+sqlcipher' and providing a 'DATABASE_PASSWORD', all data is transparently
      encrypted, providing an essential security layer for protecting sensitive information
      in self-hosted deployments. Note that this requires additional system libraries
      and the 'sqlcipher3-wheels' Python package."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6C2 **Granular Chat Controls Permissions**: Administrators can
      now manage chat settings with greater detail. The main \"Chat Controls\" permission
      now acts as a master switch, while new granular toggles for \"Valves\", \"System
      Prompts\", and \"Advanced Parameters\" allow for more specific control over
      which sections are visible to users inside the panel."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F512 **Admin Workspace Privacy Control**: Introduced the 'ENABLE_ADMIN_WORKSPACE_CONTENT_ACCESS'
      environment variable (defaults to 'True') allowing administrators to control
      their access privileges to workspace items (Knowledge, Models, Prompts, Tools).
      When disabled, administrators adhere to the same access control rules as regular
      users, enhancing data separation for multi-tenant deployments."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F441️ **Password Visibility Toggle for Input Fields**: Password
      fields across the application (login, registration, user management, and account
      settings) now utilize a new 'SensitiveInput' component, providing a consistent
      toggle to reveal/hide passwords for improved usability and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6E1️ **Hardened Channel Message Security**: Fixed a key permission
      flaw that allowed users with channel access to edit or delete messages belonging
      to others. The system now correctly enforces that users can only modify their
      own messages, protecting data integrity in shared channels."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6E1️ **Hardened OAuth Security by Removing JWT from URL**: Fixed
      a critical security vulnerability where the authentication token was exposed
      in the URL after a successful OAuth login. The token is now transferred via
      a browser cookie, preventing potential leaks through browser history or server
      logs and protecting user sessions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6E1️ **Hardened Chat Completion API Security**: The chat completion
      API endpoint now includes an explicit ownership check, ensuring non-admin users
      cannot access chats that do not belong to them and preventing potential unauthorized
      access."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4DD **Note Access in Knowledge Retrieval Fixed**: Corrected a permission
      oversight in knowledge retrieval, ensuring users can always use their own notes
      as a source for RAG without needing explicit sharing permissions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F9D1⚖️ **Restored Admin Access to User Feedback**: Fixed a permission
      issue that blocked administrators from viewing or editing user feedback they
      didn't create, ensuring they can properly manage all evaluations across the
      platform."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F510 **Hardened OpenTelemetry Exporter Configuration**: The OTLP
      HTTP exporter no longer uses a potentially insecure explicit flag, improving
      security by relying on the connection URL's protocol (HTTP/HTTPS) to ensure
      transport safety."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-safety-and-privacy-changes-in-v0-6-19
  source_release: open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243
  source_type: github_releases
  theme: safety-privacy
  title: 10 Safety and Privacy changes in v0.6.19
  type: change
related_changes:
- '[[Changes/Claude/2025-08-06-claude-code-security-reviews|Claude Code Security Reviews]]'
- '[[Changes/Gemini CLI/2025-08-06-4-safety-and-privacy-changes-in-v0-1-18|4 Safety
  and Privacy changes in v0.1.18]]'
- '[[Changes/Codex CLI/2025-08-07-new-onboarding-flow-that-uses-sandbox-workspace-write-and-ask-for-approval-on-re|new
  onboarding flow that uses…]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243]]'
source_type: github_releases
theme: safety-privacy
title: 10 Safety and Privacy changes in v0.6.19
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Safety and Privacy changes in v0.6.19

**Open WebUI** · 2025-08-09 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.19) · from [[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|v0.6.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Encrypted SQLite Database with SQLCipher**: You can now encrypt your entire SQLite database at rest using SQLCipher. By setting the 'DATABASE_TYPE' to 'sqlite+sqlcipher' and providing a 'DATABASE_PASSWORD', all data is transparently encrypted, providing an essential security layer for protecting sensitive information in self-hosted deployments. Note that this requires additional system libraries and the 'sqlcipher3-wheels' Python package.

> 🛂 **Granular Chat Controls Permissions**: Administrators can now manage chat settings with greater detail. The main "Chat Controls" permission now acts as a master switch, while new granular toggles for "Valves", "System Prompts", and "Advanced Parameters" allow for more specific control over which sections are visible to users inside the panel.

> 🔒 **Admin Workspace Privacy Control**: Introduced the 'ENABLE_ADMIN_WORKSPACE_CONTENT_ACCESS' environment variable (defaults to 'True') allowing administrators to control their access privileges to workspace items (Knowledge, Models, Prompts, Tools). When disabled, administrators adhere to the same access control rules as regular users, enhancing data separation for multi-tenant deployments.

> 👁️ **Password Visibility Toggle for Input Fields**: Password fields across the application (login, registration, user management, and account settings) now utilize a new 'SensitiveInput' component, providing a consistent toggle to reveal/hide passwords for improved usability and security.

> 🛡️ **Hardened Channel Message Security**: Fixed a key permission flaw that allowed users with channel access to edit or delete messages belonging to others. The system now correctly enforces that users can only modify their own messages, protecting data integrity in shared channels.

> 🛡️ **Hardened OAuth Security by Removing JWT from URL**: Fixed a critical security vulnerability where the authentication token was exposed in the URL after a successful OAuth login. The token is now transferred via a browser cookie, preventing potential leaks through browser history or server logs and protecting user sessions.

> 🛡️ **Hardened Chat Completion API Security**: The chat completion API endpoint now includes an explicit ownership check, ensuring non-admin users cannot access chats that do not belong to them and preventing potential unauthorized access.

> 📝 **Note Access in Knowledge Retrieval Fixed**: Corrected a permission oversight in knowledge retrieval, ensuring users can always use their own notes as a source for RAG without needing explicit sharing permissions.

> 🧑⚖️ **Restored Admin Access to User Feedback**: Fixed a permission issue that blocked administrators from viewing or editing user feedback they didn't create, ensuring they can properly manage all evaluations across the platform.

> 🔐 **Hardened OpenTelemetry Exporter Configuration**: The OTLP HTTP exporter no longer uses a potentially insecure explicit flag, improving security by relying on the connection URL's protocol (HTTP/HTTPS) to ensure transport safety.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps and Integrations changes in v0.6.19]] · Apps and Integrations
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
- [[Changes/Open WebUI/2025-08-09-3-collaboration-changes-in-v0-6-19|3 Collaboration changes in v0.6.19]] · Collaboration
- [[Changes/Open WebUI/2025-08-09-3-accessibility-and-localization-changes-in-v0-6-19|3 Accessibility and Localization changes in v0.6.19]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-09-13-interface-experience-changes-in-v0-6-19|13 Interface Experience changes in v0.6.19]] · Interface Experience
- [[Changes/Open WebUI/2025-08-09-29-other-changes-in-v0-6-19|29 other changes in v0.6.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-08-07 · Codex CLI · [[Changes/Codex CLI/2025-08-07-new-onboarding-flow-that-uses-sandbox-workspace-write-and-ask-for-approval-on-re|new onboarding flow that uses…]]
- Later: 2025-08-10 · Open WebUI · [[Changes/Open WebUI/2025-08-10-opentelemetry-configuration-consistency-fixed-an-issue-where-opentelemetry-metri|🛠️ OpenTelemetry Configuration Consistency]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-09-ddbd92&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-09-10-safety-and-privacy-changes-in-v0-6-19.md%0ACard%20ID%3A%20open-webui-2025-08-09-ddbd92%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->