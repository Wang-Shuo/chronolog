---
card_id: open-webui-2026-07-27-680390
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Account and Access: 15 changes in v0.11.0
  — \U0001F5C4️ **LDAP group synchronization.** Administrators can now map LDAP groups
  to Open WebUI…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1215
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0476c2fa69374bd837d6ca2f57959aed4e1715ecaaced8801aacfa6bd7ba6305
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-680390
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 15 Account and Access changes'
  evidence:
  - quote: "\U0001F5C4️ **LDAP group synchronization.** Administrators can now map
      LDAP groups to Open WebUI groups from the authentication settings, with optional
      automatic creation of missing groups, so a user's group memberships are kept
      in step with the directory each time they sign in. [#27263](https://github.com/open-webui/open-webui/pull/27263),
      [#18015](https://github.com/open-webui/open-webui/issues/18015)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4CE **Attach anything with the at menu.** Typing an at sign in
      the message input now searches your folders, knowledge collections, and individual
      files as well as your models, and pasting a link offers it as a web page or
      YouTube attachment. [Commit](https://github.com/open-webui/open-webui/commit/e8b4c7f9e212253267b8c79dc5360894f0d91bec)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F39A️ **Switch for single sign-on.** OAuth and OIDC now have their
      own on and off switch in the authentication settings, matching the LDAP one
      above it, so sign-in through a provider can be turned off without clearing the
      configuration. [#26988](https://github.com/open-webui/open-webui/pull/26988)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5B2️ **One sign-in attempt at a time.** The sign-in, sign-up and
      LDAP form now disables its buttons while a request is in flight, so a slow response
      no longer turns repeated clicks or Enter presses into several concurrent attempts.
      [#27416](https://github.com/open-webui/open-webui/pull/27416), [#27264](https://github.com/open-webui/open-webui/issues/27264)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6C2 **Trusted clients for token exchange.** Administrators can
      now list which OAuth clients may have their tokens exchanged for a session,
      through a new \"OAUTH_TOKEN_EXCHANGE_TRUSTED_CLIENT_IDS\" setting, so a token
      a person obtained by signing in to an unrelated application of the same provider
      can no longer be turned into a session as that person. [#27546](https://github.com/open-webui/open-webui/pull/27546),
      [Commit](https://github.com/open-webui/open-webui/commit/b190dcf3caa00dc8b7b9c7312828298d9143f60d),
      [Commit](https://github.com/open-webui/open-webui/commit/c4332be71e6e9c314e8a13b9d2819a6932561630)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6AA **Throttle for token exchange.** Administrators can now cap
      how often the OAuth token exchange endpoint may be called from one address through
      new \"OAUTH_TOKEN_EXCHANGE_RATE_LIMIT\" and \"OAUTH_TOKEN_EXCHANGE_RATE_LIMIT_WINDOW\"
      settings, which bound automated attempts with leaked or guessed tokens and stay
      off until set. [Commit](https://github.com/open-webui/open-webui/commit/453b9fb0291c0de8957a2713988c7c53dbcc5465)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F50F **PKCE for every sign-in provider.** The code challenge setting
      now applies to Google, Microsoft and GitHub sign-in as well as OpenID Connect,
      so the same protection covers every provider. [Commit](https://github.com/open-webui/open-webui/commit/40320c113637f80e0466e30cae63ab9ac1ba596e),
      [#27302](https://github.com/open-webui/open-webui/pull/27302)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F524 **Embeddings through the OpenAI-compatible API.** Integrations
      built on OpenAI client libraries can now create embeddings through the Ollama
      proxy, so embedding requests go through the same sign-in and model access rules
      as chat instead of needing direct access to Ollama. [#27332](https://github.com/open-webui/open-webui/pull/27332),
      [Commit](https://github.com/open-webui/open-webui/commit/9f00b62b3a005b030ffaf638fd1da4c27e3c0586),
      [#27328](https://github.com/open-webui/open-webui/discussions/27328), [Docs:#1331](https://github.com/open-webui/docs/pull/1331)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F512 **Terminal file preview isolation.** Previewing an HTML file
      in the system terminal now runs it in an isolated context by default, closing
      a cross-site scripting hole that could expose your login session or, for privileged
      accounts, run code on the server. [#26907](https://github.com/open-webui/open-webui/pull/26907)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F587️ **Sign-in profile pictures fetched safely.** The profile picture
      pulled in when someone signs in through a provider is now fetched through the
      same protected path as other outbound requests, so a host that changes its address
      between the check and the fetch can no longer point it at an internal service,
      taking the forwarded sign-in token with it. [#26699](https://github.com/open-webui/open-webui/pull/26699)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F511 **Connecting a remote MCP server over OAuth.** Setting up a
      remote MCP server now reports plainly when its sign-in details cannot be discovered,
      rather than saving an unusable connection that failed with a server error the
      moment you tried to authorise it. [#26654](https://github.com/open-webui/open-webui/pull/26654),
      [#26647](https://github.com/open-webui/open-webui/issues/26647)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F463 **First sign-in through a trusted header.** Two requests arriving
      together for someone signing in for the first time through a trusted header
      no longer create two accounts for the same person, and the database now refuses
      a second account for an address that already exists, whatever its capitalisation.
      [Commit](https://github.com/open-webui/open-webui/commit/b190dcf3caa00dc8b7b9c7312828298d9143f60d),
      [Commit](https://github.com/open-webui/open-webui/commit/50e050e1957de40caa9df479b4c0d9b814f1f623),
      [#27571](https://github.com/open-webui/open-webui/pull/27571), [#27117](https://github.com/open-webui/open-webui/issues/27117)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3AB **Expired identity tokens sent to tools.** A sign-in session
      is now refreshed before the earliest of its tokens expires, so tools and pipes
      that forward your identity no longer hand a downstream service a token it rejects.
      [#27520](https://github.com/open-webui/open-webui/pull/27520), [#27066](https://github.com/open-webui/open-webui/issues/27066)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3AB **Sign-in tokens that never expire.** A provider that returns
      no expiry and no way to refresh is now taken at its word, instead of being given
      an invented one-hour lifetime that left the session unusable afterwards. [Commit](https://github.com/open-webui/open-webui/commit/98656b7c5e29383b61d2113164466b8d4ab1d424),
      [#26802](https://github.com/open-webui/open-webui/pull/26802), [#26141](https://github.com/open-webui/open-webui/issues/26141)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F511 **Signing in after a session expires.** An expired session
      now cleanly returns you to the sign-in page and back to where you were afterwards,
      instead of bouncing you away from the sign-in page or leaving a stale session
      behind. [Commit](https://github.com/open-webui/open-webui/commit/609cc6ad9b597c6a3f4df6f9dba93d6ff6ec1f18),
      [Commit](https://github.com/open-webui/open-webui/commit/29782aba01b8f34625949170dc9ee9e1c5872893),
      [#26751](https://github.com/open-webui/open-webui/pull/26751), [#26731](https://github.com/open-webui/open-webui/issues/26731)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 15-account-and-access-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: account-access
  title: 15 Account and Access changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9
  Account and Access changes in rust-v0.145.0]]'
- '[[Changes/v0/2026-07-21-2-account-and-access-changes-in-slash-commands-the-shopify|2
  Account and Access changes in Slash commands, the Shopify…]]'
- '[[Changes/Lovable/2026-07-24-report-abuse-and-submit-appeals-with-guided-forms|Report
  abuse and submit appeals with guided forms]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: account-access
title: 15 Account and Access changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Account and Access changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗄️ **LDAP group synchronization.** Administrators can now map LDAP groups to Open WebUI groups from the authentication settings, with optional automatic creation of missing groups, so a user's group memberships are kept in step with the directory each time they sign in. [#27263](https://github.com/open-webui/open-webui/pull/27263), [#18015](https://github.com/open-webui/open-webui/issues/18015)

> 📎 **Attach anything with the at menu.** Typing an at sign in the message input now searches your folders, knowledge collections, and individual files as well as your models, and pasting a link offers it as a web page or YouTube attachment. [Commit](https://github.com/open-webui/open-webui/commit/e8b4c7f9e212253267b8c79dc5360894f0d91bec)

> 🎚️ **Switch for single sign-on.** OAuth and OIDC now have their own on and off switch in the authentication settings, matching the LDAP one above it, so sign-in through a provider can be turned off without clearing the configuration. [#26988](https://github.com/open-webui/open-webui/pull/26988)

> 🖲️ **One sign-in attempt at a time.** The sign-in, sign-up and LDAP form now disables its buttons while a request is in flight, so a slow response no longer turns repeated clicks or Enter presses into several concurrent attempts. [#27416](https://github.com/open-webui/open-webui/pull/27416), [#27264](https://github.com/open-webui/open-webui/issues/27264)

> 🛂 **Trusted clients for token exchange.** Administrators can now list which OAuth clients may have their tokens exchanged for a session, through a new "OAUTH_TOKEN_EXCHANGE_TRUSTED_CLIENT_IDS" setting, so a token a person obtained by signing in to an unrelated application of the same provider can no longer be turned into a session as that person. [#27546](https://github.com/open-webui/open-webui/pull/27546), [Commit](https://github.com/open-webui/open-webui/commit/b190dcf3caa00dc8b7b9c7312828298d9143f60d), [Commit](https://github.com/open-webui/open-webui/commit/c4332be71e6e9c314e8a13b9d2819a6932561630)

> 🚪 **Throttle for token exchange.** Administrators can now cap how often the OAuth token exchange endpoint may be called from one address through new "OAUTH_TOKEN_EXCHANGE_RATE_LIMIT" and "OAUTH_TOKEN_EXCHANGE_RATE_LIMIT_WINDOW" settings, which bound automated attempts with leaked or guessed tokens and stay off until set. [Commit](https://github.com/open-webui/open-webui/commit/453b9fb0291c0de8957a2713988c7c53dbcc5465)

> 🔏 **PKCE for every sign-in provider.** The code challenge setting now applies to Google, Microsoft and GitHub sign-in as well as OpenID Connect, so the same protection covers every provider. [Commit](https://github.com/open-webui/open-webui/commit/40320c113637f80e0466e30cae63ab9ac1ba596e), [#27302](https://github.com/open-webui/open-webui/pull/27302)

> 🔤 **Embeddings through the OpenAI-compatible API.** Integrations built on OpenAI client libraries can now create embeddings through the Ollama proxy, so embedding requests go through the same sign-in and model access rules as chat instead of needing direct access to Ollama. [#27332](https://github.com/open-webui/open-webui/pull/27332), [Commit](https://github.com/open-webui/open-webui/commit/9f00b62b3a005b030ffaf638fd1da4c27e3c0586), [#27328](https://github.com/open-webui/open-webui/discussions/27328), [Docs:#1331](https://github.com/open-webui/docs/pull/1331)

> 🔒 **Terminal file preview isolation.** Previewing an HTML file in the system terminal now runs it in an isolated context by default, closing a cross-site scripting hole that could expose your login session or, for privileged accounts, run code on the server. [#26907](https://github.com/open-webui/open-webui/pull/26907)

> 🖇️ **Sign-in profile pictures fetched safely.** The profile picture pulled in when someone signs in through a provider is now fetched through the same protected path as other outbound requests, so a host that changes its address between the check and the fetch can no longer point it at an internal service, taking the forwarded sign-in token with it. [#26699](https://github.com/open-webui/open-webui/pull/26699)

> 🔑 **Connecting a remote MCP server over OAuth.** Setting up a remote MCP server now reports plainly when its sign-in details cannot be discovered, rather than saving an unusable connection that failed with a server error the moment you tried to authorise it. [#26654](https://github.com/open-webui/open-webui/pull/26654), [#26647](https://github.com/open-webui/open-webui/issues/26647)

> 👣 **First sign-in through a trusted header.** Two requests arriving together for someone signing in for the first time through a trusted header no longer create two accounts for the same person, and the database now refuses a second account for an address that already exists, whatever its capitalisation. [Commit](https://github.com/open-webui/open-webui/commit/b190dcf3caa00dc8b7b9c7312828298d9143f60d), [Commit](https://github.com/open-webui/open-webui/commit/50e050e1957de40caa9df479b4c0d9b814f1f623), [#27571](https://github.com/open-webui/open-webui/pull/27571), [#27117](https://github.com/open-webui/open-webui/issues/27117)

> 🎫 **Expired identity tokens sent to tools.** A sign-in session is now refreshed before the earliest of its tokens expires, so tools and pipes that forward your identity no longer hand a downstream service a token it rejects. [#27520](https://github.com/open-webui/open-webui/pull/27520), [#27066](https://github.com/open-webui/open-webui/issues/27066)

> 🎫 **Sign-in tokens that never expire.** A provider that returns no expiry and no way to refresh is now taken at its word, instead of being given an invented one-hour lifetime that left the session unusable afterwards. [Commit](https://github.com/open-webui/open-webui/commit/98656b7c5e29383b61d2113164466b8d4ab1d424), [#26802](https://github.com/open-webui/open-webui/pull/26802), [#26141](https://github.com/open-webui/open-webui/issues/26141)

> 🔑 **Signing in after a session expires.** An expired session now cleanly returns you to the sign-in page and back to where you were afterwards, instead of bouncing you away from the sign-in page or leaving a stale session behind. [Commit](https://github.com/open-webui/open-webui/commit/609cc6ad9b597c6a3f4df6f9dba93d6ff6ec1f18), [Commit](https://github.com/open-webui/open-webui/commit/29782aba01b8f34625949170dc9ee9e1c5872893), [#26751](https://github.com/open-webui/open-webui/pull/26751), [#26731](https://github.com/open-webui/open-webui/issues/26731)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-24 · Lovable · [[Changes/Lovable/2026-07-24-report-abuse-and-submit-appeals-with-guided-forms|Report abuse and submit appeals with guided forms]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-6-account-and-access-changes-in-1-16-1|6 Account and Access changes in 1.16.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-680390&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-15-account-and-access-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-680390%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->