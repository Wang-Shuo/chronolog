---
card_id: open-webui-2026-05-09-c022f3
date: '2026-05-09'
description: "Open WebUI · 2026-05-09 · Account and Access: 4 changes in v0.9.3 —
  \U0001F6C2 **MCP OAuth server URL setting.** Static OAuth tool server setups can
  now define a…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2111
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 07403db167b7346b6a2049f1d5ff372bdadec5a82027698d0213fd3bb86bc49b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-05-09-c022f3
  comparison: ''
  date: '2026-05-09'
  description: 'Open WebUI — v0.9.3: 4 Account and Access changes'
  evidence:
  - quote: "\U0001F6C2 **MCP OAuth server URL setting.** Static OAuth tool server
      setups can now define a separate OAuth server URL, making discovery and client
      registration work when authentication endpoints are hosted separately from the
      tool server URL. [Commit](https://github.com/open-webui/open-webui/commit/9907c0a25ae830d134af70022238715f834d20c6),
      [#24164](https://github.com/open-webui/open-webui/pull/24164), [#24216](https://github.com/open-webui/open-webui/issues/24216)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: ⏱️ **MCP OAuth timeout control.** OAuth token exchanges for MCP tool server
      connections now respect the configurable client timeout setting, reducing callback
      failures with slower providers. [Commit](https://github.com/open-webui/open-webui/commit/cde72dab71671645e119564ca9747ce25dd590ad),
      [#24138](https://github.com/open-webui/open-webui/issues/24138)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F511 **Android password autofill support.** Password inputs now
      expose the expected field name metadata, improving password manager autofill
      reliability on Android login pages. [Commit](https://github.com/open-webui/open-webui/commit/60ea4214aa42f1ad22142f1a43535007a2293d16),
      [#24137](https://github.com/open-webui/open-webui/issues/24137)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  - quote: "\U0001F514 **LDAP signup webhook parity.** New accounts created through
      LDAP now trigger the same signup webhook notifications as password and OAuth
      signups, so downstream provisioning and audit automations receive consistent
      events. [Commit](https://github.com/open-webui/open-webui/commit/fd3368c0bff168417e3c49ffd73491c344702339),
      [#24377](https://github.com/open-webui/open-webui/issues/24377)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-account-and-access-changes-in-v0-9-3
  source_release: open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca
  source_type: github_releases
  theme: account-access
  title: 4 Account and Access changes in v0.9.3
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-07-2-account-and-access-changes-in-rust-v0-129-0|2
  Account and Access changes in rust-v0.129.0]]'
- '[[Changes/Codex CLI/2026-05-08-2-account-and-access-changes-in-rust-v0-130-0|2
  Account and Access changes in rust-v0.130.0]]'
- '[[Changes/Replit/2026-05-08-private-publishing-for-everyone|Private publishing
  for everyone]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca]]'
source_type: github_releases
theme: account-access
title: 4 Account and Access changes in v0.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Account and Access changes in v0.9.3

**Open WebUI** · 2026-05-09 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.3) · from [[Releases/Open WebUI/open-webui-2026-05-09-v0-9-3-github-319872270-bb8aabca|v0.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛂 **MCP OAuth server URL setting.** Static OAuth tool server setups can now define a separate OAuth server URL, making discovery and client registration work when authentication endpoints are hosted separately from the tool server URL. [Commit](https://github.com/open-webui/open-webui/commit/9907c0a25ae830d134af70022238715f834d20c6), [#24164](https://github.com/open-webui/open-webui/pull/24164), [#24216](https://github.com/open-webui/open-webui/issues/24216)

> ⏱️ **MCP OAuth timeout control.** OAuth token exchanges for MCP tool server connections now respect the configurable client timeout setting, reducing callback failures with slower providers. [Commit](https://github.com/open-webui/open-webui/commit/cde72dab71671645e119564ca9747ce25dd590ad), [#24138](https://github.com/open-webui/open-webui/issues/24138)

> 🔑 **Android password autofill support.** Password inputs now expose the expected field name metadata, improving password manager autofill reliability on Android login pages. [Commit](https://github.com/open-webui/open-webui/commit/60ea4214aa42f1ad22142f1a43535007a2293d16), [#24137](https://github.com/open-webui/open-webui/issues/24137)

> 🔔 **LDAP signup webhook parity.** New accounts created through LDAP now trigger the same signup webhook notifications as password and OAuth signups, so downstream provisioning and audit automations receive consistent events. [Commit](https://github.com/open-webui/open-webui/commit/fd3368c0bff168417e3c49ffd73491c344702339), [#24377](https://github.com/open-webui/open-webui/issues/24377)

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
- [[Changes/Open WebUI/2026-05-09-sanitized-spreadsheet-html-previews-spreadsheet-previews-now-sanitize-generated|🛡️ Sanitized spreadsheet HTML previews. Spreadsheet previews now sanitize…]] · Files and Data
- [[Changes/Open WebUI/2026-05-09-9-model-support-changes-in-v0-9-3|9 Model Support changes in v0.9.3]] · Model Support
- [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Safety and Privacy
- [[Changes/Open WebUI/2026-05-09-faster-memory-query-performance-per-user-memory-lookups-and-deletions-now-run-mu|⚡ Faster memory query performance. Per-user memory lookups and deletions now run…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-05-09-5-other-changes-in-v0-9-3|5 other changes in v0.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-05-08 · Replit · [[Changes/Replit/2026-05-08-private-publishing-for-everyone|Private publishing for everyone]]
- Later: 2026-05-10 · Open WebUI · [[Changes/Open WebUI/2026-05-10-redirect-based-ssrf-protection-all-outbound-http-requests-now-block-3xx-redirect|🛡️ Redirect-based SSRF protection. All outbound HTTP requests now block 3xx…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-05-09-c022f3&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-05-09-4-account-and-access-changes-in-v0-9-3.md%0ACard%20ID%3A%20open-webui-2026-05-09-c022f3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->