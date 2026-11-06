---
card_id: open-webui-2026-02-12-3bfe08
date: '2026-02-12'
description: "Open WebUI · 2026-02-12 · Safety and Privacy: 5 changes in v0.8.0 —
  \U0001F514 **Temporary chat notification privacy.** Notifications from temporary
  chats now only…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1033
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f4b6cc4781060c889419456c7e1c029af6a6fb962521c7d0986c43516a537039
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-12-3bfe08
  comparison: ''
  date: '2026-02-12'
  description: 'Open WebUI — v0.8.0: 5 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F514 **Temporary chat notification privacy.** Notifications from
      temporary chats now only appear on the device where the chat is running, preventing
      privacy leaks across logged-in sessions. [#21292](https://github.com/open-webui/open-webui/pull/21292)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F50C **Independent access control updates.** API endpoints now support
      independent access control updates for models, tools, knowledge bases, and notes,
      enabling finer-grained permission management. [Commit](https://github.com/open-webui/open-webui/commit/0044902c082f8475336cc7d5c57fe3f35ab0555d),
      [Commit](https://github.com/open-webui/open-webui/commit/c259c878060af1b03b702c943e8813d7b4fc3199),
      [Commit](https://github.com/open-webui/open-webui/commit/e3a825769063cee486650cc2eb9a032676e630c5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E0️ **Admin model write permission fix.** Fixed the admin panel
      allowing models to be assigned write permissions, since users with write permission
      are not admins and cannot write. [Commit](https://github.com/open-webui/open-webui/commit/4aedfdc5471a1f13c1084b34b48ea3ed6311cd42)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F512 **Write permission enforcement for tools.** Users without write
      permissions are now properly prevented from editing tools, with a clear error
      message displayed when attempting unauthorized edits. [Commit](https://github.com/open-webui/open-webui/commit/85e92fe3b062ae669985c09495f6ff1baf8176ab),
      [Commit](https://github.com/open-webui/open-webui/commit/91faa9fd5a1cfc5d3ab531d2d91d28db52bcc702)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  - quote: "\U0001F6E1️ **Chat Valves permission enforcement.** The \"Allow Chat Valves\"
      permission is now properly enforced in the integrations menu, preventing users
      from bypassing access restrictions. [#20691](https://github.com/open-webui/open-webui/pull/20691)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-safety-and-privacy-changes-in-v0-8-0
  source_release: open-webui-2026-02-12-v0-8-0-github-285910626-490914ba
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v0.8.0
  type: change
related_changes:
- '[[Changes/Dify/2026-02-11-2-safety-and-privacy-changes-in-1-13-0|2 Safety and Privacy
  changes in 1.13.0]]'
- '[[Changes/Codex CLI/2026-02-12-5-safety-and-privacy-changes-in-rust-v0-100-0|5
  Safety and Privacy changes in rust-v0.100.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-12-permission-prompts-with-long-diffs-are-scrollable-in-alt-screen-mode|Permission
  prompts with long diffs are scrollable in alt-screen mode]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|open-webui-2026-02-12-v0-8-0-github-285910626-490914ba]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v0.8.0

**Open WebUI** · 2026-02-12 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.0) · from [[Releases/Open WebUI/open-webui-2026-02-12-v0-8-0-github-285910626-490914ba|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔔 **Temporary chat notification privacy.** Notifications from temporary chats now only appear on the device where the chat is running, preventing privacy leaks across logged-in sessions. [#21292](https://github.com/open-webui/open-webui/pull/21292)

> 🔌 **Independent access control updates.** API endpoints now support independent access control updates for models, tools, knowledge bases, and notes, enabling finer-grained permission management. [Commit](https://github.com/open-webui/open-webui/commit/0044902c082f8475336cc7d5c57fe3f35ab0555d), [Commit](https://github.com/open-webui/open-webui/commit/c259c878060af1b03b702c943e8813d7b4fc3199), [Commit](https://github.com/open-webui/open-webui/commit/e3a825769063cee486650cc2eb9a032676e630c5)

> 🛠️ **Admin model write permission fix.** Fixed the admin panel allowing models to be assigned write permissions, since users with write permission are not admins and cannot write. [Commit](https://github.com/open-webui/open-webui/commit/4aedfdc5471a1f13c1084b34b48ea3ed6311cd42)

> 🔒 **Write permission enforcement for tools.** Users without write permissions are now properly prevented from editing tools, with a clear error message displayed when attempting unauthorized edits. [Commit](https://github.com/open-webui/open-webui/commit/85e92fe3b062ae669985c09495f6ff1baf8176ab), [Commit](https://github.com/open-webui/open-webui/commit/91faa9fd5a1cfc5d3ab531d2d91d28db52bcc702)

> 🛡️ **Chat Valves permission enforcement.** The "Allow Chat Valves" permission is now properly enforced in the integrations menu, preventing users from bypassing access restrictions. [#20691](https://github.com/open-webui/open-webui/pull/20691)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-12-16-reliability-and-performance-changes-in-v0-8-0|16 Reliability and Performance changes in v0.8.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-12-audio-service-timeout-handling-audio-transcription-and-text-to-speech-requests-n|🔌 Audio service timeout handling. Audio transcription and text-to-speech…]] · Voice and Audio
- [[Changes/Open WebUI/2026-02-12-2-editor-experience-changes-in-v0-8-0|2 Editor Experience changes in v0.8.0]] · Editor Experience
- [[Changes/Open WebUI/2026-02-12-19-model-support-changes-in-v0-8-0|19 Model Support changes in v0.8.0]] · Model Support
- [[Changes/Open WebUI/2026-02-12-27-developer-workflow-changes-in-v0-8-0|27 Developer Workflow changes in v0.8.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-12-5-context-window-changes-in-v0-8-0|5 Context Window changes in v0.8.0]] · Context Window
- [[Changes/Open WebUI/2026-02-12-2-image-generation-changes-in-v0-8-0|2 Image Generation changes in v0.8.0]] · Image Generation
- [[Changes/Open WebUI/2026-02-12-2-memory-and-personalization-changes-in-v0-8-0|2 Memory and Personalization changes in v0.8.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-12-gboard-multi-line-paste-fix-multi-line-text-pasted-from-gboard-on-android-now-in|📱 Gboard multi-line paste fix. Multi-line text pasted from Gboard on Android now…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-02-12-2-collaboration-changes-in-v0-8-0|2 Collaboration changes in v0.8.0]] · Collaboration
- [[Changes/Open WebUI/2026-02-12-6-account-and-access-changes-in-v0-8-0|6 Account and Access changes in v0.8.0]] · Account and Access
- [[Changes/Open WebUI/2026-02-12-async-pipeline-operations-pipeline-operations-now-run-asynchronously-instead-of|🔧 Async pipeline operations. Pipeline operations now run asynchronously instead…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-02-12-5-search-and-browsing-changes-in-v0-8-0|5 Search and Browsing changes in v0.8.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-12-8-interface-experience-changes-in-v0-8-0|8 Interface Experience changes in v0.8.0]] · Interface Experience
- [[Changes/Open WebUI/2026-02-12-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-12-screen-reader-accessibility-screen-reader-users-now-hear-the-password-field-labe|♿ Screen reader accessibility. Screen reader users now hear the password field…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-12-10-files-and-data-changes-in-v0-8-0|10 Files and Data changes in v0.8.0]] · Files and Data
- [[Changes/Open WebUI/2026-02-12-6-apps-and-integrations-changes-in-v0-8-0|6 Apps and Integrations changes in v0.8.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-12-29-other-changes-in-v0-8-0|29 other changes in v0.8.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-12-permission-prompts-with-long-diffs-are-scrollable-in-alt-screen-mode|Permission prompts with long diffs are scrollable in alt-screen mode]]
- Later: 2026-02-13 · Claude Code · [[Changes/Claude Code/2026-02-13-2-safety-and-privacy-changes-in-v2-1-41|2 Safety and Privacy changes in v2.1.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-12-3bfe08&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-12-5-safety-and-privacy-changes-in-v0-8-0.md%0ACard%20ID%3A%20open-webui-2026-02-12-3bfe08%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->