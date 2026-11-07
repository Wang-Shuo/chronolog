---
card_id: open-webui-2026-10-10-245834
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Enterprise and Administration: 5 changes in
  v0.12.0 — \U0001F512 **Password changes sign out everywhere without Redis.** Changing
  a password…"
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2461
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 32053f37dc9e2fc9c0eecc5903bd5f11319e99ccdfb957491cd91f8145f0d921
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-245834
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 5 Enterprise and Administration changes'
  evidence:
  - quote: "\U0001F512 **Password changes sign out everywhere without Redis.** Changing
      a password, by the user or an administrator, now signs that account out on every
      device even on installations without Redis, where existing sessions stayed valid
      until they expired. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F91D **Sharing a shared folder.** Only a folder's owner or an administrator
      can now change who a folder is shared with, where anyone with write access to
      it could also share it with other people or groups. [Commit](https://github.com/open-webui/open-webui/commit/8145774e329c7174437944b1dd361fef9a50639a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F576️ **Enforced temporary chats hold on every route.** Users with
      Enforce Temporary Chat can no longer save chats by calling the chat API directly
      or through import, clone and fork, where only the web interface stopped them;
      admins are not affected and existing chats still open. [Commit](https://github.com/open-webui/open-webui/commit/d04f78b3bfbeca383d78830391faa9639554fae4),
      [#31633](https://github.com/open-webui/open-webui/issues/31633)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F451 **First admin keeps its protection.** On Postgres, an account
      created in the same second as the first admin, as happens when a script sets
      up an instance, can no longer be taken for the primary admin, which let other
      admins demote or delete the real first admin and made that account impossible
      to edit, lock or delete. [#32157](https://github.com/open-webui/open-webui/pull/32157)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⭐ **Default model kept on settings save.** Saving the Interface settings
      no longer replaces your chosen default model with the administrator's default
      or cuts a multi-model default down to its first model. [#30953](https://github.com/open-webui/open-webui/pull/30953),
      [#30952](https://github.com/open-webui/open-webui/issues/30952)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-enterprise-and-administration-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: enterprise-admin
  title: 5 Enterprise and Administration changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-09-enterprise-credit-balances-now-appear-as-numbers|Enterprise
  credit balances now appear as numbers]]'
- '[[Changes/Lovable/2026-10-09-publish-every-app-in-your-workspace-under-your-own-domain|Publish
  every app in your workspace under your own domain]]'
- '[[Changes/Runway/2026-10-09-workspace-admins-can-now-set-a-credit-cap-on-any-project-giving-each-team-or-cli|Project
  Credit Caps]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: enterprise-admin
title: 5 Enterprise and Administration changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Enterprise and Administration changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/enterprise-admin|Enterprise and Administration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔒 **Password changes sign out everywhere without Redis.** Changing a password, by the user or an administrator, now signs that account out on every device even on installations without Redis, where existing sessions stayed valid until they expired. [Commit](https://github.com/open-webui/open-webui/commit/24e30d1cbdaab624dfe20f479f805e6791cf0226)

> 🤝 **Sharing a shared folder.** Only a folder's owner or an administrator can now change who a folder is shared with, where anyone with write access to it could also share it with other people or groups. [Commit](https://github.com/open-webui/open-webui/commit/8145774e329c7174437944b1dd361fef9a50639a)

> 🕶️ **Enforced temporary chats hold on every route.** Users with Enforce Temporary Chat can no longer save chats by calling the chat API directly or through import, clone and fork, where only the web interface stopped them; admins are not affected and existing chats still open. [Commit](https://github.com/open-webui/open-webui/commit/d04f78b3bfbeca383d78830391faa9639554fae4), [#31633](https://github.com/open-webui/open-webui/issues/31633)

> 👑 **First admin keeps its protection.** On Postgres, an account created in the same second as the first admin, as happens when a script sets up an instance, can no longer be taken for the primary admin, which let other admins demote or delete the real first admin and made that account impossible to edit, lock or delete. [#32157](https://github.com/open-webui/open-webui/pull/32157)

> ⭐ **Default model kept on settings save.** Saving the Interface settings no longer replaces your chosen default model with the administrator's default or cuts a multi-model default down to its first model. [#30953](https://github.com/open-webui/open-webui/pull/30953), [#30952](https://github.com/open-webui/open-webui/issues/30952)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]] · Model Support
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-10-09 · Runway · [[Changes/Runway/2026-10-09-workspace-admins-can-now-set-a-credit-cap-on-any-project-giving-each-team-or-cli|Project Credit Caps]]
- Later: 2026-10-10 · OpenClaw · [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-245834&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-245834%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->