---
card_id: open-webui-2026-02-14-d94f98
date: '2026-02-14'
description: 'Open WebUI · 2026-02-14 · Other changes: 6 changes in v0.8.1 — > [!CAUTION]'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 862a799e8162fb587087895edd306888e9b0fb3d0b2e715e25c5abe12948bab4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-14-d94f98
  comparison: ''
  date: '2026-02-14'
  description: 'Open WebUI — v0.8.1: 6 other changes'
  evidence:
  - quote: '> [!CAUTION]'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: '> ⚠️ **Database Migrations**: This release includes database schema changes;
      we strongly recommend backing up your database and all associated data before
      upgrading in production environments. If you are running a multi-worker, multi-server,
      or load-balanced deployment, all instances must be updated simultaneously, rolling
      updates are not supported and will cause application failures due to schema
      incompatibility.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: "\U0001F310 **Translation updates.** Portuguese (Brazil) translations were
      updated."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: "\U0001F5A5️ **ARM device compatibility fix.** Fixed an issue where upgrading
      to 0.8.0 would fail to start on ARM devices (like Raspberry Pi 4) due to torch
      2.10.0 causing SIGILL errors; now pinned to torch<=2.9.1. [#21385](https://github.com/open-webui/open-webui/pull/21385),
      [#21349](https://github.com/open-webui/open-webui/issues/21349)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: "\U0001F5C3️ **SQLite cascade delete fix.** Deleting chats now properly
      removes all associated messages in SQLite, matching PostgreSQL behavior and
      preventing orphaned data. [#21362](https://github.com/open-webui/open-webui/pull/21362)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  - quote: "\U0001F511 **Password validation regex fix.** Fixed the password validation
      regex by adding the raw string prefix, ensuring escape sequences like d and
      w are interpreted correctly. [#21400](https://github.com/open-webui/open-webui/pull/21400),
      [#21399](https://github.com/open-webui/open-webui/issues/21399)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-other-changes-in-v0-8-1
  source_release: open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77
  source_type: github_releases
  theme: uncategorized
  title: 6 other changes in v0.8.1
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77|open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77]]'
source_type: github_releases
theme: uncategorized
title: 6 other changes in v0.8.1
type: change
---

<!-- chronolog:begin region="header" -->
# 6 other changes in v0.8.1

**Open WebUI** · 2026-02-14 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.1) · from [[Releases/Open WebUI/open-webui-2026-02-14-v0-8-1-github-286288526-aa333d77|v0.8.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > [!CAUTION]

> > ⚠️ **Database Migrations**: This release includes database schema changes; we strongly recommend backing up your database and all associated data before upgrading in production environments. If you are running a multi-worker, multi-server, or load-balanced deployment, all instances must be updated simultaneously, rolling updates are not supported and will cause application failures due to schema incompatibility.

> 🌐 **Translation updates.** Portuguese (Brazil) translations were updated.

> 🖥️ **ARM device compatibility fix.** Fixed an issue where upgrading to 0.8.0 would fail to start on ARM devices (like Raspberry Pi 4) due to torch 2.10.0 causing SIGILL errors; now pinned to torch<=2.9.1. [#21385](https://github.com/open-webui/open-webui/pull/21385), [#21349](https://github.com/open-webui/open-webui/issues/21349)

> 🗃️ **SQLite cascade delete fix.** Deleting chats now properly removes all associated messages in SQLite, matching PostgreSQL behavior and preventing orphaned data. [#21362](https://github.com/open-webui/open-webui/pull/21362)

> 🔑 **Password validation regex fix.** Fixed the password validation regex by adding the raw string prefix, ensuring escape sequences like d and w are interpreted correctly. [#21400](https://github.com/open-webui/open-webui/pull/21400), [#21399](https://github.com/open-webui/open-webui/issues/21399)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-14-2-apps-and-integrations-changes-in-v0-8-1|2 Apps and Integrations changes in v0.8.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-14-2-developer-workflow-changes-in-v0-8-1|2 Developer Workflow changes in v0.8.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-14-public-sharing-security-fix-fixed-a-security-issue-where-users-with-write-access|🛡️ Public sharing security fix. Fixed a security issue where users with write…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-14-2-reliability-and-performance-changes-in-v0-8-1|2 Reliability and Performance changes in v0.8.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-14-web-search-result-count-the-built-in-search-web-tool-now-respects-the-admin-conf|🔍 Web search result count. The built-in search_web tool now respects…]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-14-6-model-support-changes-in-v0-8-1|6 Model Support changes in v0.8.1]] · Model Support
- [[Changes/Open WebUI/2026-02-14-metadata-processing-crash-fix-fixed-a-latent-bug-where-processing-document-metad|📝 Metadata processing crash fix. Fixed a latent bug where processing document…]] · Files and Data
- [[Changes/Open WebUI/2026-02-14-sync-modal-unexpected-appearance-fixed-an-issue-where-the-sync-modal-would-appea|🐛 Sync modal unexpected appearance. Fixed an issue where the Sync Modal would…]] · Collaboration
- [[Changes/Open WebUI/2026-02-14-2-interface-experience-changes-in-v0-8-1|2 Interface Experience changes in v0.8.1]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-14-d94f98&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-14-6-other-changes-in-v0-8-1.md%0ACard%20ID%3A%20open-webui-2026-02-14-d94f98%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->