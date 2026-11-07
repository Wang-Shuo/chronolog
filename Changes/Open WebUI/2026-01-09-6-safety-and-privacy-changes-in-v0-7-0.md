---
card_id: open-webui-2026-01-09-7cb0ee
date: '2026-01-09'
description: "Open WebUI · 2026-01-09 · Safety and Privacy: 6 changes in v0.7.0 —
  \U0001F465 Administrators now have three granular group sharing permission options
  instead of a…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1991
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 235b5172dccd8264bbda45b3a20ec586082e2bba15d7debbb6ce778cd9c5ddc3
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-01-09-7cb0ee
  comparison: ''
  date: '2026-01-09'
  description: 'Open WebUI — v0.7.0: 6 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F465 Administrators now have three granular group sharing permission
      options instead of a simple on/off toggle, allowing them to choose between \"No
      one\", \"Members\", or \"Anyone\" for who can share content to each group. [Commit](https://github.com/open-webui/open-webui/commit/ca514cd3eda2524b8da472ef17c0ccb216bac2e8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F512 Users are now protected from stored XSS vulnerabilities in
      iFrame embeds for citations and response messages through configurable same-origin
      sandbox settings instead of hardcoded values. [#20209](https://github.com/open-webui/open-webui/pull/20209),
      [#20210](https://github.com/open-webui/open-webui/pull/20210)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F511 Image Generation, Web Search, and Audio (TTS/STT) API endpoints
      now enforce permission checks on the backend, closing a security gap where disabled
      features could previously be accessed via direct API calls. [#20471](https://github.com/open-webui/open-webui/pull/20471)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F6E0️ Tools and Tool Servers (MCP and OpenAPI) now enforce access
      control checks on the backend, ensuring users can only access tools they have
      permission to use even via direct API calls. [#20443](https://github.com/open-webui/open-webui/issues/20443),
      [Commit](https://github.com/open-webui/open-webui/commit/9b06fdc8fe1c933071610336be05f11e77e6c8eb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F510 Scripts or integrations that directly called Image Generation,
      Web Search, or Audio APIs while those features were disabled in the Admin UI
      will now receive 403 Forbidden errors, as backend permission enforcement has
      been added to match frontend restrictions. [#20471](https://github.com/open-webui/open-webui/pull/20471)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  - quote: "\U0001F465 The default group sharing permission changed from \"Members\"
      to \"Anyone\", meaning users can now share content to any group configured with
      \"Anyone\" permission regardless of their membership in that group. [Commit](https://github.com/open-webui/open-webui/commit/ca514cd3eda2524b8da472ef17c0ccb216bac2e8)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-safety-and-privacy-changes-in-v0-7-0
  source_release: open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v0.7.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-2|2 Safety
  and Privacy changes in v2.1.2]]'
- '[[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-3|2 Safety
  and Privacy changes in v2.1.3]]'
- '[[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety
  and Privacy changes in rust-v0.80.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v0.7.0

**Open WebUI** · 2026-01-09 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.7.0) · from [[Releases/Open WebUI/open-webui-2026-01-09-v0-7-0-github-275585328-a4da522c|v0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 👥 Administrators now have three granular group sharing permission options instead of a simple on/off toggle, allowing them to choose between "No one", "Members", or "Anyone" for who can share content to each group. [Commit](https://github.com/open-webui/open-webui/commit/ca514cd3eda2524b8da472ef17c0ccb216bac2e8)

> 🔒 Users are now protected from stored XSS vulnerabilities in iFrame embeds for citations and response messages through configurable same-origin sandbox settings instead of hardcoded values. [#20209](https://github.com/open-webui/open-webui/pull/20209), [#20210](https://github.com/open-webui/open-webui/pull/20210)

> 🔑 Image Generation, Web Search, and Audio (TTS/STT) API endpoints now enforce permission checks on the backend, closing a security gap where disabled features could previously be accessed via direct API calls. [#20471](https://github.com/open-webui/open-webui/pull/20471)

> 🛠️ Tools and Tool Servers (MCP and OpenAPI) now enforce access control checks on the backend, ensuring users can only access tools they have permission to use even via direct API calls. [#20443](https://github.com/open-webui/open-webui/issues/20443), [Commit](https://github.com/open-webui/open-webui/commit/9b06fdc8fe1c933071610336be05f11e77e6c8eb)

> 🔐 Scripts or integrations that directly called Image Generation, Web Search, or Audio APIs while those features were disabled in the Admin UI will now receive 403 Forbidden errors, as backend permission enforcement has been added to match frontend restrictions. [#20471](https://github.com/open-webui/open-webui/pull/20471)

> 👥 The default group sharing permission changed from "Members" to "Anyone", meaning users can now share content to any group configured with "Anyone" permission regardless of their membership in that group. [Commit](https://github.com/open-webui/open-webui/commit/ca514cd3eda2524b8da472ef17c0ccb216bac2e8)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-01-09-3-editor-experience-changes-in-v0-7-0|3 Editor Experience changes in v0.7.0]] · Editor Experience
- [[Changes/Open WebUI/2026-01-09-users-on-windows-now-see-correctly-preserved-line-breaks-when-using-the-clipboar|📋 Users on Windows now see correctly preserved line breaks when using…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-01-09-2-memory-and-personalization-changes-in-v0-7-0|2 Memory and Personalization changes in v0.7.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-01-09-4-search-and-browsing-changes-in-v0-7-0|4 Search and Browsing changes in v0.7.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-01-09-3-apps-and-integrations-changes-in-v0-7-0|3 Apps and Integrations changes in v0.7.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-01-09-5-files-and-data-changes-in-v0-7-0|5 Files and Data changes in v0.7.0]] · Files and Data
- [[Changes/Open WebUI/2026-01-09-3-context-window-changes-in-v0-7-0|3 Context Window changes in v0.7.0]] · Context Window
- [[Changes/Open WebUI/2026-01-09-9-reliability-and-performance-changes-in-v0-7-0|9 Reliability and Performance changes in v0.7.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-01-09-3-account-and-access-changes-in-v0-7-0|3 Account and Access changes in v0.7.0]] · Account and Access
- [[Changes/Open WebUI/2026-01-09-4-image-generation-changes-in-v0-7-0|4 Image Generation changes in v0.7.0]] · Image Generation
- [[Changes/Open WebUI/2026-01-09-5-interface-experience-changes-in-v0-7-0|5 Interface Experience changes in v0.7.0]] · Interface Experience
- [[Changes/Open WebUI/2026-01-09-11-model-support-changes-in-v0-7-0|11 Model Support changes in v0.7.0]] · Model Support
- [[Changes/Open WebUI/2026-01-09-24-developer-workflow-changes-in-v0-7-0|24 Developer Workflow changes in v0.7.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-01-09-3-voice-and-audio-changes-in-v0-7-0|3 Voice and Audio changes in v0.7.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-01-09-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-01-09-26-other-changes-in-v0-7-0|26 other changes in v0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-09 · Codex CLI · [[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety and Privacy changes in rust-v0.80.0]]
- Later: 2026-01-12 · OpenCode · [[Changes/OpenCode/2026-01-12-core-add-password-authentication-and-improve-server-security|Core Add password authentication and improve server security]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-01-09-7cb0ee&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-01-09-6-safety-and-privacy-changes-in-v0-7-0.md%0ACard%20ID%3A%20open-webui-2026-01-09-7cb0ee%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->