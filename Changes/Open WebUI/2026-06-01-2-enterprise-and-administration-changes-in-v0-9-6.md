---
card_id: open-webui-2026-06-01-a34b9a
date: '2026-06-01'
description: "Open WebUI · 2026-06-01 · Enterprise and Administration: 2 changes in
  v0.9.6 — \U0001F513 **Cross-user file exfiltration via image URLs.** When a chat
  message…"
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2330
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 237e1fe42db1b83abb1c7044332e37da5ff4d10c31464162e85c22e06695c3f8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-a34b9a
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 2 Enterprise and Administration changes'
  evidence:
  - quote: "\U0001F513 **Cross-user file exfiltration via image URLs.** When a chat
      message references a file by id in an \"image_url\" field, the server now resolves
      that file only for its owner, an administrator, or a user with an explicit read
      grant, preventing other authenticated users from extracting a file's contents
      by routing it through the model. [#24625](https://github.com/open-webui/open-webui/pull/24625),
      [Commit](https://github.com/open-webui/open-webui/commit/c75fe8e74b72617c51282cc3ea0a2e8d9cdd9140)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F195 **First admin signup after a reset.** Creating the first administrator
      account is no longer blocked by a previously stored signup setting, so a fresh
      or reset instance can always be bootstrapped. [#24821](https://github.com/open-webui/open-webui/pull/24821)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-enterprise-and-administration-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: enterprise-admin
  title: 2 Enterprise and Administration changes in v0.9.6
  type: change
related_changes:
- '[[Changes/Gamma/2026-05-29-api-delete-is-here|API delete is here]]'
- '[[Changes/Replit/2026-05-29-teams-and-enterprise|Teams and Enterprise]]'
- '[[Changes/Replit/2026-05-29-upgrade-to-enterprise-without-leaving-replit|Upgrade
  to Enterprise without leaving Replit]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: enterprise-admin
title: 2 Enterprise and Administration changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Enterprise and Administration changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/enterprise-admin|Enterprise and Administration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔓 **Cross-user file exfiltration via image URLs.** When a chat message references a file by id in an "image_url" field, the server now resolves that file only for its owner, an administrator, or a user with an explicit read grant, preventing other authenticated users from extracting a file's contents by routing it through the model. [#24625](https://github.com/open-webui/open-webui/pull/24625), [Commit](https://github.com/open-webui/open-webui/commit/c75fe8e74b72617c51282cc3ea0a2e8d9cdd9140)

> 🆕 **First admin signup after a reset.** Creating the first administrator account is no longer blocked by a previously stored signup setting, so a fresh or reset instance can always be bootstrapped. [#24821](https://github.com/open-webui/open-webui/pull/24821)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-5-reliability-and-performance-changes-in-v0-9-6|5 Reliability and Performance changes in v0.9.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-05-29 · Replit · [[Changes/Replit/2026-05-29-upgrade-to-enterprise-without-leaving-replit|Upgrade to Enterprise without leaving Replit]]
- Later: 2026-06-02 · Claude · [[Changes/Claude/2026-06-02-enterprise-plans-can-manage-admin-permissions-with-custom-roles|Enterprise plans can manage admin permissions with custom roles]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-a34b9a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-a34b9a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->