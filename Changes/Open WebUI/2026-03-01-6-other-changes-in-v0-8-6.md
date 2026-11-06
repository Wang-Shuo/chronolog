---
card_id: open-webui-2026-03-01-e4688d
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Other changes: 6 changes in v0.8.6 — \U0001F3AF
  **Action button priority sorting.** Action buttons under assistant messages now
  appear in a…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 101a00fab2ac98319969916219905c3da98fc4898ccb930f7af24a114d72eea2
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-e4688d
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 6 other changes'
  evidence:
  - quote: "\U0001F3AF **Action button priority sorting.** Action buttons under assistant
      messages now appear in a consistent order based on the priority field from function
      Valves, allowing developers to control button placement. [#21790](https://github.com/open-webui/open-webui/pull/21790)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F310 **Translation updates.** Translations for German, Portuguese
      (Brazil), Simplified Chinese, Traditional Chinese, Catalan, and Spanish were
      enhanced and expanded."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4CB **Audit log stdout.** Audit logs now correctly appear on stdout
      when the ENABLE_AUDIT_STDOUT environment variable is set to true, aligning runtime
      behavior with the intended configuration. [#21777](https://github.com/open-webui/open-webui/pull/21777)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F3AF **Function valve priority resolution.** Function priorities
      defined in code are now correctly applied when no custom value has been saved
      in the database, ensuring consistent action button and filter ordering. [#21841](https://github.com/open-webui/open-webui/pull/21841)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F3AD **TailwindCSS gray color theme.** Custom gray color palette
      is now correctly applied to the CSS root theme layer, fixing an issue where
      --color-gray-x variables were missing. [#21900](https://github.com/open-webui/open-webui/pull/21900),
      [#21899](https://github.com/open-webui/open-webui/issues/21899)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F4CE **Broken documentation links.** Fixed broken links in the backend
      config and admin settings that pointed to outdated documentation locations.
      [#21904](https://github.com/open-webui/open-webui/pull/21904)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-other-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: uncategorized
  title: 6 other changes in v0.8.6
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: uncategorized
title: 6 other changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 6 other changes in v0.8.6

**Open WebUI** · 2026-03-01 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🎯 **Action button priority sorting.** Action buttons under assistant messages now appear in a consistent order based on the priority field from function Valves, allowing developers to control button placement. [#21790](https://github.com/open-webui/open-webui/pull/21790)

> 🌐 **Translation updates.** Translations for German, Portuguese (Brazil), Simplified Chinese, Traditional Chinese, Catalan, and Spanish were enhanced and expanded.

> 📋 **Audit log stdout.** Audit logs now correctly appear on stdout when the ENABLE_AUDIT_STDOUT environment variable is set to true, aligning runtime behavior with the intended configuration. [#21777](https://github.com/open-webui/open-webui/pull/21777)

> 🎯 **Function valve priority resolution.** Function priorities defined in code are now correctly applied when no custom value has been saved in the database, ensuring consistent action button and filter ordering. [#21841](https://github.com/open-webui/open-webui/pull/21841)

> 🎭 **TailwindCSS gray color theme.** Custom gray color palette is now correctly applied to the CSS root theme layer, fixing an issue where --color-gray-x variables were missing. [#21900](https://github.com/open-webui/open-webui/pull/21900), [#21899](https://github.com/open-webui/open-webui/issues/21899)

> 📎 **Broken documentation links.** Fixed broken links in the backend config and admin settings that pointed to outdated documentation locations. [#21904](https://github.com/open-webui/open-webui/pull/21904)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21 Reliability and Performance changes in v0.8.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-01-2-search-and-browsing-changes-in-v0-8-6|2 Search and Browsing changes in v0.8.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]] · Interface Experience
- [[Changes/Open WebUI/2026-03-01-3-account-and-access-changes-in-v0-8-6|3 Account and Access changes in v0.8.6]] · Account and Access
- [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]] · Model Support
- [[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer Workflow changes in v0.8.6]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-e4688d&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-6-other-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-e4688d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->