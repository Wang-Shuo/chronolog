---
card_id: open-webui-2026-05-09-eedebd
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Other changes: 5 changes in v0.9.3 — \U0001F510
  **Profile image forwarding control.** Administrators can now disable external profile
  image…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9c93b208a1cc84a50094e1a03d6174053fbf8de7ed77b06db64637fc45bef42b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-eedebd
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 5 other changes'
  evidence:
  - quote: "\U0001F510 **Profile image forwarding control.** Administrators can now
      disable external profile image URL forwarding with the \"ENABLE_PROFILE_IMAGE_URL_FORWARDING\"
      setting to prevent browser metadata leaks to third-party servers. [#24420](https://github.com/open-webui/open-webui/pull/24420)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F504 **Replaceable tool embed updates.** Pipes and Tools can now
      overwrite previously emitted rich-UI embeds in-place by passing a `replace`
      flag on the `embeds` event, enabling live dashboards and progress panels that
      update without stacking duplicate entries."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F310 **Translation updates.** Translations for Chinese, Catalan,
      Filipino, and Korean were enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F6E1️ **Webhook avatar URL validation.** Channel webhook profile
      image URLs are now validated before saving, preventing invalid or unsafe avatar
      URLs from being accepted. [#24370](https://github.com/open-webui/open-webui/pull/24370)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: '⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-other-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: uncategorized
  title: 5 other changes in v0.9.3
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: uncategorized
title: 5 other changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 5 other changes in v0.9.3

**Open WebUI** · 2026-05-09 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **Profile image forwarding control.** Administrators can now disable external profile image URL forwarding with the "ENABLE_PROFILE_IMAGE_URL_FORWARDING" setting to prevent browser metadata leaks to third-party servers. [#24420](https://github.com/open-webui/open-webui/pull/24420)

> 🔄 **Replaceable tool embed updates.** Pipes and Tools can now overwrite previously emitted rich-UI embeds in-place by passing a `replace` flag on the `embeds` event, enabling live dashboards and progress panels that update without stacking duplicate entries.

> 🌐 **Translation updates.** Translations for Chinese, Catalan, Filipino, and Korean were enhanced and expanded.

> 🛡️ **Webhook avatar URL validation.** Channel webhook profile image URLs are now validated before saving, preventing invalid or unsafe avatar URLs from being accepted. [#24370](https://github.com/open-webui/open-webui/pull/24370)

> ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-05-09-5-search-and-browsing-changes-in-v0-9-3|5 Search and Browsing changes in v0.9.3]] · Search and Browsing
- [[Changes/Open WebUI/2026-05-09-10-voice-and-audio-changes-in-v0-9-3|10 Voice and Audio changes in v0.9.3]] · Voice and Audio
- [[Changes/Open WebUI/2026-05-09-5-editor-experience-changes-in-v0-9-3|5 Editor Experience changes in v0.9.3]] · Editor Experience
- [[Changes/Open WebUI/2026-05-09-8-interface-experience-changes-in-v0-9-3|8 Interface Experience changes in v0.9.3]] · Interface Experience
- [[Changes/Open WebUI/2026-05-09-4-context-window-changes-in-v0-9-3|4 Context Window changes in v0.9.3]] · Context Window
- [[Changes/Open WebUI/2026-05-09-3-apps-and-integrations-changes-in-v0-9-3|3 Apps and Integrations changes in v0.9.3]] · Apps and Integrations
- [[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2 Automation and Scheduling changes in v0.9.3]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-05-09-22-developer-workflow-changes-in-v0-9-3|22 Developer Workflow changes in v0.9.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-05-09-4-reliability-and-performance-changes-in-v0-9-3|4 Reliability and Performance changes in v0.9.3]] · Reliability and Performance
- [[Changes/Open WebUI/2026-05-09-4-account-and-access-changes-in-v0-9-3|4 Account and Access changes in v0.9.3]] · Account and Access
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-eedebd&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-5-other-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-eedebd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->