---
card_id: open-webui-2026-03-01-87fcf5
date: '2026-03-01'
description: "Open WebUI · 2026-03-01 · Account and Access: 3 changes in v0.8.6 —
  \U0001F504 **OAuth profile sync on login.** Administrators can now enable automatic
  synchronization…"
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2042
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5d9abfc5575d7cc95f93d645ebbe59f918e24806788712af0dc077b0cb5ea953
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-01-87fcf5
  comparison: ''
  date: '2026-03-01'
  description: 'Open WebUI — v0.8.6: 3 Account and Access changes'
  evidence:
  - quote: "\U0001F504 **OAuth profile sync on login.** Administrators can now enable
      automatic synchronization of user profile name and email from OAuth providers
      on login via the OAUTH_UPDATE_NAME_ON_LOGIN and OAUTH_UPDATE_EMAIL_ON_LOGIN
      environment variables. [#21787](https://github.com/open-webui/open-webui/pull/21787),
      [Commit](https://github.com/open-webui/open-webui/commit/9478c5e7ac8254b5f522c006da0c1c49bb282727)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F510 **OAuth session database error.** OAuth login no longer fails
      with a database error when creating sessions, fixing the \"'NoneType' object
      has no attribute 'id'\" and \"can't adapt type 'dict'\" errors that occurred
      during OAuth group creation. [#21788](https://github.com/open-webui/open-webui/issues/21788)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  - quote: "\U0001F511 **Password manager autofill.** Password manager autofill (like
      iCloud Passwords, 1Password, Bitwarden) now correctly captures filled-in passwords,
      fixing login failures where the password appeared filled but was sent as empty.
      [#21869](https://github.com/open-webui/open-webui/pull/21869), [Commit](https://github.com/open-webui/open-webui/commit/9dff497abf821dfba6eb8ea65e48a657ee91fd71)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 3-account-and-access-changes-in-v0-8-6
  source_release: open-webui-2026-03-01-v0-8-6-github-291846033-263bca05
  source_type: github_releases
  theme: account-access
  title: 3 Account and Access changes in v0.8.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-26-2-account-and-access-changes-in-rust-v0-106-0|2
  Account and Access changes in rust-v0.106.0]]'
- '[[Changes/Gemini CLI/2026-02-27-3-account-and-access-changes-in-v0-31-0|3 Account
  and Access changes in v0.31.0]]'
- '[[Changes/Claude Code/2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic|Added
  manual URL paste fallback during MCP OAuth authentication]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|open-webui-2026-03-01-v0-8-6-github-291846033-263bca05]]'
source_type: github_releases
theme: account-access
title: 3 Account and Access changes in v0.8.6
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Account and Access changes in v0.8.6

**Open WebUI** · 2026-03-01 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.6) · from [[Releases/Open WebUI/open-webui-2026-03-01-v0-8-6-github-291846033-263bca05|v0.8.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔄 **OAuth profile sync on login.** Administrators can now enable automatic synchronization of user profile name and email from OAuth providers on login via the OAUTH_UPDATE_NAME_ON_LOGIN and OAUTH_UPDATE_EMAIL_ON_LOGIN environment variables. [#21787](https://github.com/open-webui/open-webui/pull/21787), [Commit](https://github.com/open-webui/open-webui/commit/9478c5e7ac8254b5f522c006da0c1c49bb282727)

> 🔐 **OAuth session database error.** OAuth login no longer fails with a database error when creating sessions, fixing the "'NoneType' object has no attribute 'id'" and "can't adapt type 'dict'" errors that occurred during OAuth group creation. [#21788](https://github.com/open-webui/open-webui/issues/21788)

> 🔑 **Password manager autofill.** Password manager autofill (like iCloud Passwords, 1Password, Bitwarden) now correctly captures filled-in passwords, fixing login failures where the password appeared filled but was sent as empty. [#21869](https://github.com/open-webui/open-webui/pull/21869), [Commit](https://github.com/open-webui/open-webui/commit/9dff497abf821dfba6eb8ea65e48a657ee91fd71)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21 Reliability and Performance changes in v0.8.6]] · Reliability and Performance
- [[Changes/Open WebUI/2026-03-01-2-search-and-browsing-changes-in-v0-8-6|2 Search and Browsing changes in v0.8.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-03-01-oauth-session-token-decryption-oauth-sessions-are-now-properly-detached-from-the|🔓 OAuth session token decryption. OAuth sessions are now properly detached…]] · Context Window
- [[Changes/Open WebUI/2026-03-01-individual-user-sharing-control-administrators-can-now-disable-individual-user-s|🔐 Individual user sharing control. Administrators can now disable individual…]] · Collaboration
- [[Changes/Open WebUI/2026-03-01-4-interface-experience-changes-in-v0-8-6|4 Interface Experience changes in v0.8.6]] · Interface Experience
- [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-01-8-model-support-changes-in-v0-8-6|8 Model Support changes in v0.8.6]] · Model Support
- [[Changes/Open WebUI/2026-03-01-9-developer-workflow-changes-in-v0-8-6|9 Developer Workflow changes in v0.8.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-03-01-6-other-changes-in-v0-8-6|6 other changes in v0.8.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic|Added manual URL paste fallback during MCP OAuth authentication]]
- Later: 2026-03-02 · Codex CLI · [[Changes/Codex CLI/2026-03-02-3-account-and-access-changes-in-rust-v0-107-0|3 Account and Access changes in rust-v0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-01-87fcf5&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-01-3-account-and-access-changes-in-v0-8-6.md%0ACard%20ID%3A%20open-webui-2026-03-01-87fcf5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->