---
card_id: open-webui-2025-12-21-77b187
date: '2025-12-21'
description: 'Open WebUI · 2025-12-21 · Safety and Privacy: 6 changes in v0.6.42 —
  ✨ Knowledge base file management was enhanced with automatic list refresh after
  file…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 980
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a7c68f44caed6fc4f66e561fcb789a404ba6d33503fda137b12836ff2e4624b4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-77b187
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: 6 Safety and Privacy changes'
  evidence:
  - quote: ✨ Knowledge base file management was enhanced with automatic list refresh
      after file operations ensuring immediate UI updates, improved permission validation
      at the model layer, and automatic channel-file association for files uploaded
      with channel metadata. [Commit](https://github.com/open-webui/open-webui/commit/c15201620d03a9b60b800a34d8dc3426722c5b8b)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4DD Notes feature now supports server-side search and filtering
      with view options for notes created by the user versus notes shared with them,
      customizable sorting by name or date in both list and grid view modes within
      a redesigned interface featuring consolidated note management controls in a
      unified header, group-based permission sharing with read, write, and read-only
      access control displaying note authorship and sharing status for better collaboration,
      and paginated infinite scroll for improved performance with large note collections.
      [Commit](https://github.com/open-webui/open-webui/commit/9b24cddef6c4862bd899eb8d6332cafff54e871d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F468\U0001F469\U0001F467\U0001F466 The \"ENABLE_PUBLIC_ACTIVE_USERS_COUNT\"
      environment variable now allows restricting active user count visibility to
      administrators, reducing backend load and addressing privacy concerns in large
      deployments. [#20027](https://github.com/open-webui/open-webui/pull/20027),
      [#13026](https://github.com/open-webui/open-webui/issues/13026)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F4A5 UI crashes and white screen errors caused by null chat lists
      during loading or network failures were prevented by adding null safety checks
      to chat iteration in folder placeholders and archived chat modals. [#19898](https://github.com/open-webui/open-webui/pull/19898)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F512 Temporary chat permission enforcement now correctly prevents
      users from enabling the feature through personal settings when disabled in default
      or group permissions. [#19785](https://github.com/open-webui/open-webui/issues/19785)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  - quote: "\U0001F50F Administrators can now delete read-only knowledge bases from
      deleted users, resolving permission issues that previously prevented cleanup
      of orphaned read-only content. [Commit](https://github.com/open-webui/open-webui/commit/59d6eb2badf46f9c2b1e879484ac33432915b575)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-safety-and-privacy-changes-in-v0-6-42
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v0.6.42
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-12-19-2-safety-and-privacy-changes-in-rust-v0-76-0|2 Safety
  and Privacy changes in rust-v0.76.0]]'
- '[[Changes/GitHub Copilot CLI/2025-12-19-add-url-permission-controls-which-affect-common-shell-commands-which-access-the|Add
  URL permission controls which affect common shell commands which access the web]]'
- '[[Changes/Codex CLI/2025-12-21-2-safety-and-privacy-changes-in-rust-v0-77-0|2 Safety
  and Privacy changes in rust-v0.77.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v0.6.42
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v0.6.42

**Open WebUI** · 2025-12-21 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✨ Knowledge base file management was enhanced with automatic list refresh after file operations ensuring immediate UI updates, improved permission validation at the model layer, and automatic channel-file association for files uploaded with channel metadata. [Commit](https://github.com/open-webui/open-webui/commit/c15201620d03a9b60b800a34d8dc3426722c5b8b)

> 📝 Notes feature now supports server-side search and filtering with view options for notes created by the user versus notes shared with them, customizable sorting by name or date in both list and grid view modes within a redesigned interface featuring consolidated note management controls in a unified header, group-based permission sharing with read, write, and read-only access control displaying note authorship and sharing status for better collaboration, and paginated infinite scroll for improved performance with large note collections. [Commit](https://github.com/open-webui/open-webui/commit/9b24cddef6c4862bd899eb8d6332cafff54e871d)

> 👨👩👧👦 The "ENABLE_PUBLIC_ACTIVE_USERS_COUNT" environment variable now allows restricting active user count visibility to administrators, reducing backend load and addressing privacy concerns in large deployments. [#20027](https://github.com/open-webui/open-webui/pull/20027), [#13026](https://github.com/open-webui/open-webui/issues/13026)

> 💥 UI crashes and white screen errors caused by null chat lists during loading or network failures were prevented by adding null safety checks to chat iteration in folder placeholders and archived chat modals. [#19898](https://github.com/open-webui/open-webui/pull/19898)

> 🔒 Temporary chat permission enforcement now correctly prevents users from enabling the feature through personal settings when disabled in default or group permissions. [#19785](https://github.com/open-webui/open-webui/issues/19785)

> 🔏 Administrators can now delete read-only knowledge bases from deleted users, resolving permission issues that previously prevented cleanup of orphaned read-only content. [Commit](https://github.com/open-webui/open-webui/commit/59d6eb2badf46f9c2b1e879484ac33432915b575)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of|⚡ External reranker operations were optimized to prevent event loop blocking…]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-12-21 · Codex CLI · [[Changes/Codex CLI/2025-12-21-2-safety-and-privacy-changes-in-rust-v0-77-0|2 Safety and Privacy changes in rust-v0.77.0]]
- Later: 2025-12-22 · Cursor · [[Changes/Cursor/2025-12-22-improved-stability-around-how-the-agent-respects-auto-run-preferences-to-prevent|Improved stability around how the agent respects auto-run preferences to prevent…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-77b187&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-6-safety-and-privacy-changes-in-v0-6-42.md%0ACard%20ID%3A%20open-webui-2025-12-21-77b187%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->