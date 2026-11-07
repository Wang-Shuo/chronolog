---
card_id: open-webui-2026-03-09-c87f70
date: '2026-03-09'
description: "Open WebUI · 2026-03-09 · Account and Access: 2 changes in v0.8.10 —
  \U0001F510 **OAuth error handling.** Fixed a bug where bare except clauses silently
  caught…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2050
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 18a477080a5092b4d65e07adcce5809d6bbf707ca481de46bdd5bb64e98a9b6f
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-09-c87f70
  comparison: ''
  date: '2026-03-09'
  description: 'Open WebUI — v0.8.10: 2 Account and Access changes'
  evidence:
  - quote: "\U0001F510 **OAuth error handling.** Fixed a bug where bare except clauses
      silently caught SystemExit and KeyboardInterrupt, preventing clean process shutdown
      during OAuth authentication. [#22420](https://github.com/open-webui/open-webui/pull/22420)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  - quote: "\U0001F510 **OAuth error URL encoding.** Fixed OAuth error messages with
      special characters causing malformed redirect URLs; error messages are now properly
      URL-encoded. [#22415](https://github.com/open-webui/open-webui/pull/22415)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-account-and-access-changes-in-v0-8-10
  source_release: open-webui-2026-03-09-v0-8-10-github-294485945-5852a771
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v0.8.10
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-03-08-microsoft-oauth-refresh-token-fix-fixed-a-bug-where-microsoft-oauth-refresh-toke|\U0001F510
  Microsoft OAuth refresh token fix. Fixed a bug where Microsoft OAuth refresh…]]"
- '[[Changes/ElevenLabs/2026-03-09-saml-sso-for-ios-and-android-enterprise-customers-using-saml-based-identity-prov|SAML
  SSO for iOS and Android]]'
- '[[Changes/GitHub Copilot CLI/2026-03-09-login-flow-no-longer-hangs-on-ubuntu-when-system-keyring-is-unresponsive|Login
  flow no longer hangs on Ubuntu when system keyring is unresponsive]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|open-webui-2026-03-09-v0-8-10-github-294485945-5852a771]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v0.8.10
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v0.8.10

**Open WebUI** · 2026-03-09 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.10) · from [[Releases/Open WebUI/open-webui-2026-03-09-v0-8-10-github-294485945-5852a771|v0.8.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **OAuth error handling.** Fixed a bug where bare except clauses silently caught SystemExit and KeyboardInterrupt, preventing clean process shutdown during OAuth authentication. [#22420](https://github.com/open-webui/open-webui/pull/22420)

> 🔐 **OAuth error URL encoding.** Fixed OAuth error messages with special characters causing malformed redirect URLs; error messages are now properly URL-encoded. [#22415](https://github.com/open-webui/open-webui/pull/22415)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-09-teams-webhook-crash-fixed-a-typeerror-crash-in-the-teams-webhook-handler-when-us|📨 Teams webhook crash. Fixed a TypeError crash in the Teams webhook handler…]] · Collaboration
- [[Changes/Open WebUI/2026-03-09-2-search-and-browsing-changes-in-v0-8-10|2 Search and Browsing changes in v0.8.10]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-09-2-developer-workflow-changes-in-v0-8-10|2 Developer Workflow changes in v0.8.10]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-09-azure-speech-transcription-errors-improved-azure-ai-speech-error-handling-to-dis|🎤 Azure speech transcription errors. Improved Azure AI Speech error handling…]] · Voice and Audio
- [[Changes/Open WebUI/2026-03-09-3-model-support-changes-in-v0-8-10|3 Model Support changes in v0.8.10]] · Model Support
- [[Changes/Open WebUI/2026-03-09-2-reliability-and-performance-changes-in-v0-8-10|2 Reliability and Performance changes in v0.8.10]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-09-12-other-changes-in-v0-8-10|12 other changes in v0.8.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-03-09 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-09-login-flow-no-longer-hangs-on-ubuntu-when-system-keyring-is-unresponsive|Login flow no longer hangs on Ubuntu when system keyring is unresponsive]]
- Later: 2026-03-09 · v0 · [[Changes/v0/2026-03-09-improved-error-messages-when-project-creation-or-oauth-flows-fail|Improved error messages when project creation or OAuth flows fail]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-09-c87f70&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-09-2-account-and-access-changes-in-v0-8-10.md%0ACard%20ID%3A%20open-webui-2026-03-09-c87f70%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->