---
card_id: open-webui-2026-09-21-fe2a5f
date: '2026-09-21'
description: 'Open WebUI · 2026-09-21 · Enterprise and Administration: 5 changes in
  v0.11.4 — ✏️ **Interface text you can reword.** An administrator can now replace
  the…'
diffusion:
  first_in_tracked: '[[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export
    members as CSV (for Enterprise Plans) Quickly download a list of the people…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2442
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 317c9b6fd002fa2e89a9148b827be73bda2fa6f70589d37cb5a88d55ec90f515
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-fe2a5f
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 5 Enterprise and Administration changes'
  evidence:
  - quote: ✏️ **Interface text you can reword.** An administrator can now replace
      the interface's own wording language by language from a panel in the admin settings,
      with a replacement refused where it drops one of the placeholders the original
      fills in. [Commit](https://github.com/open-webui/open-webui/commit/67ac1a4e937271a02bfb02a330aa99dc8192cbf4)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4C0 **Bundled charts and formatting.** Drawing a chart with seaborn
      in code the browser runs fetched the library over the internet at that moment
      rather than taking it from what ships, and the code editor's Format button failed
      outright for anyone who is not an administrator; both now work from what comes
      with the application, offline included. [#30148](https://github.com/open-webui/open-webui/pull/30148),
      [#30145](https://github.com/open-webui/open-webui/issues/30145)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5DC️ **Per-field settings saves.** Only the settings actually changed
      are now stored, rather than the whole object, so another tab's older copy no
      longer overwrites them and a default an administrator changes still reaches
      everyone, and pinning a model, reordering the list or picking a default from
      outside the settings window now saves the same way. [Commit](https://github.com/open-webui/open-webui/commit/98a920168e2eea435ac15e1ad3d679946631e41d),
      [#30183](https://github.com/open-webui/open-webui/pull/30183)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3F7️ **Tag cleanup after deletion.** An administrator deleting
      someone else's chat tidied unused tags out of their own account rather than
      the owner's, leaving the owner with tags nothing points at. [#30171](https://github.com/open-webui/open-webui/pull/30171)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F2 **Integrations tab is opt-in.** The Integrations tab in personal
      settings, where tool and terminal connections of your own are managed, is now
      hidden until an administrator turns on Direct Integrations under Integrations
      or sets \"ENABLE_DIRECT_INTEGRATIONS\", and hiding it leaves existing connections
      working. [Commit](https://github.com/open-webui/open-webui/commit/6d8e63e3666e1b1aa5540ffda0816be5f40c5271),
      [Commit](https://github.com/open-webui/open-webui/commit/c82634b9d01adadbf9780ff84a0a8168fdc4fdea)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-enterprise-and-administration-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: enterprise-admin
  title: 5 Enterprise and Administration changes in v0.11.4
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2
  Enterprise and Administration changes in v2026.9.5]]'
- '[[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install
  the CLI on FreeBSD with install-cli.sh using system Node and npm]]'
- '[[Changes/Lovable/2026-09-21-set-a-default-design-system-for-each-group|Set a default
  design system for each group]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: enterprise-admin
title: 5 Enterprise and Administration changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Enterprise and Administration changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/enterprise-admin|Enterprise and Administration]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ✏️ **Interface text you can reword.** An administrator can now replace the interface's own wording language by language from a panel in the admin settings, with a replacement refused where it drops one of the placeholders the original fills in. [Commit](https://github.com/open-webui/open-webui/commit/67ac1a4e937271a02bfb02a330aa99dc8192cbf4)

> 📀 **Bundled charts and formatting.** Drawing a chart with seaborn in code the browser runs fetched the library over the internet at that moment rather than taking it from what ships, and the code editor's Format button failed outright for anyone who is not an administrator; both now work from what comes with the application, offline included. [#30148](https://github.com/open-webui/open-webui/pull/30148), [#30145](https://github.com/open-webui/open-webui/issues/30145)

> 🗜️ **Per-field settings saves.** Only the settings actually changed are now stored, rather than the whole object, so another tab's older copy no longer overwrites them and a default an administrator changes still reaches everyone, and pinning a model, reordering the list or picking a default from outside the settings window now saves the same way. [Commit](https://github.com/open-webui/open-webui/commit/98a920168e2eea435ac15e1ad3d679946631e41d), [#30183](https://github.com/open-webui/open-webui/pull/30183)

> 🏷️ **Tag cleanup after deletion.** An administrator deleting someone else's chat tidied unused tags out of their own account rather than the owner's, leaving the owner with tags nothing points at. [#30171](https://github.com/open-webui/open-webui/pull/30171)

> 🧲 **Integrations tab is opt-in.** The Integrations tab in personal settings, where tool and terminal connections of your own are managed, is now hidden until an administrator turns on Direct Integrations under Integrations or sets "ENABLE_DIRECT_INTEGRATIONS", and hiding it leaves existing connections working. [Commit](https://github.com/open-webui/open-webui/commit/6d8e63e3666e1b1aa5540ffda0816be5f40c5271), [Commit](https://github.com/open-webui/open-webui/commit/c82634b9d01adadbf9780ff84a0a8168fdc4fdea)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-09-21 · Lovable · [[Changes/Lovable/2026-09-21-set-a-default-design-system-for-each-group|Set a default design system for each group]]
- Later: 2026-09-22 · OpenHands · [[Changes/OpenHands/2026-09-22-feat-open-git-sync-to-org-admins-on-cloud-backends-by-hieptl-in-https-github-com|feat: open Git Sync to org admins on cloud backends]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-01-14 · Notion · [[Changes/Notion/2020-01-14-export-members-as-csv-for-enterprise-plans-quickly-download-a-list-of-the-people|Export members as CSV (for Enterprise Plans) Quickly download a list of the people…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-fe2a5f&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-fe2a5f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->