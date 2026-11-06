---
card_id: open-webui-2026-08-25-86ab25
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Account and Access: 13 changes in v0.11.1
  — \U0001F64B **Mentioning people in a channel.** Typing an at sign in a channel
  now lists that…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1244
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f9b5c9287faf0d6c099f5f49221d908ae4d49914c02655f90bdedcbca63e5803
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-86ab25
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 13 Account and Access changes'
  evidence:
  - quote: "\U0001F64B **Mentioning people in a channel.** Typing an at sign in a
      channel now lists that channel's own members first, before everyone else on
      the server, so the people you are likely to mean are at the top. [Commit](https://github.com/open-webui/open-webui/commit/ba885d0026ad3cce70c7cc36d1d6f59775264a12),
      [Commit](https://github.com/open-webui/open-webui/commit/dcff244f9e87e615ee0a3f345f7f801c5ebe370d),
      [#28883](https://github.com/open-webui/open-webui/issues/28883)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F510 **Terminals that use your own login.** Managed terminals configured
      for session authentication now authenticate the terminal connection with your
      own token, where it previously sent no credentials at all. [Commit](https://github.com/open-webui/open-webui/commit/2dadc5435af77b0638af69200e3af1b9654417b6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F39F **Setting up a tool server that uses OAuth.** Adding one is
      now easier to get right: the connection dialog can authorize the account from
      the dialog itself, the check button tests the sign-in details rather than reporting
      a connection failure that was never going to succeed without them, and it is
      now labelled for what it does rather than suggesting it verifies the whole connection.
      [Commit](https://github.com/open-webui/open-webui/commit/f822605b3563c57030aa200492f68572cadcc4da),
      [#28552](https://github.com/open-webui/open-webui/issues/28552)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAA7 **Profile changes from single sign-on.** A name, email address,
      or picture updated from an identity provider at sign-in now raises an event
      naming what changed, and the rest of the session uses the updated record rather
      than a stale copy. [Commit](https://github.com/open-webui/open-webui/commit/927ce0eae67af1b4a856d3e82fba0601c3b40d02)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F514 **Sign-in and sign-out events for single sign-on.** Signing
      in through an identity provider now raises the same login event that signing
      in with a password does, and signing out says which provider the session came
      from, so a function can set up or tidy up an account in another system when
      someone arrives or leaves. [#27619](https://github.com/open-webui/open-webui/pull/27619),
      [#27613](https://github.com/open-webui/open-webui/issues/27613)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA9F **Honest OAuth settings.** When single sign-on settings come
      from the environment rather than being saved in the application, the admin panel
      now shows them as read-only with a note naming the setting that controls this,
      instead of accepting edits that were silently discarded on the next restart.
      [#28276](https://github.com/open-webui/open-webui/pull/28276)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5DD️ **Changing a password now ends other sessions.** Changing
      your password, or an administrator resetting it for you, now stops every device
      that was already signed in, where they had stayed signed in on the old password
      until their session expired on its own, up to four weeks by default; the device
      making the change is signed out too and asked to sign in again, and this requires
      Redis, without which nothing can be revoked and a warning is now logged saying
      so. [#28725](https://github.com/open-webui/open-webui/pull/28725), [#28647](https://github.com/open-webui/open-webui/discussions/28647)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA79 **Signing in after a long-delayed upgrade.** Accounts on instances
      that were upgraded from a version older than 0.6.41 to 0.9.6 or newer can sign
      in again, where an upgrade step had written their single sign-on identity in
      a form the application could not read afterwards, and a repair step corrects
      the affected accounts on startup. [#28107](https://github.com/open-webui/open-webui/pull/28107),
      [#28101](https://github.com/open-webui/open-webui/issues/28101), [Commit](https://github.com/open-webui/open-webui/commit/bd8378f643dd8a56366ad9d1843b7d40f67cf1f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F511 **Signing in with some identity providers.** Logging in through
      a provider that adds its own vendor-specific information to the header of the
      sign-in token now completes, rather than failing at the final step with a message
      claiming the email or password was wrong. [#28065](https://github.com/open-webui/open-webui/pull/28065),
      [#28062](https://github.com/open-webui/open-webui/issues/28062)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA9E **Matching the right account at sign-in.** Looking up an account
      by its identity provider details now matches the exact value, where the stored
      details were searched as loose text and a value contained within another's could
      be matched instead. [#28624](https://github.com/open-webui/open-webui/pull/28624)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5BC **Downloading a generated image.** Downloading an image from
      its preview now saves the image, where it could silently save a small file containing
      an authentication error instead, and a download that does fail now says so.
      [Commit](https://github.com/open-webui/open-webui/commit/2578174637e48cafa4bcb09adbb1b7f4b545a8d5),
      [#27723](https://github.com/open-webui/open-webui/pull/27723), [#27722](https://github.com/open-webui/open-webui/issues/27722)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FAA2 **Signing people out from the identity provider.** A sign-out
      sent by an identity provider to end someone's session now works, where the check
      that the message was genuine could fail against providers whose signing keys
      need the same authentication as everything else, leaving the person signed in.
      [Commit](https://github.com/open-webui/open-webui/commit/aeda6ff13a25d3b3ba1b303609f35382db22142c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ♻ **Blank errors when a tool server's saved sign-in cannot be read.** A
      tool server whose stored sign-in details cannot be decrypted, which happens
      when "WEBUI_SECRET_KEY" changes since the key protecting them follows it, now
      names the server and says to reconnect it, where every startup logged two errors
      with no message at all. [Commit](https://github.com/open-webui/open-webui/commit/91917b23952af8ca4457f8bb3db70c75ab838fbf),
      [#28666](https://github.com/open-webui/open-webui/pull/28666), [#28665](https://github.com/open-webui/open-webui/issues/28665)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 13-account-and-access-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: account-access
  title: 13 Account and Access changes in v0.11.1
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-08-25-chatgpt-work-s-browser-on-web-and-mobile-can-also-help-you-get-tasks-done-on-som-99be54|ChatGPT
  Work can now complete tasks on signed-in websites]]'
- '[[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved
  attribution of usage telemetry to your organization for workload identity…]]'
- '[[Changes/Dify/2026-08-25-13-account-and-access-changes-in-1-17-0|13 Account and
  Access changes in 1.17.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: account-access
title: 13 Account and Access changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Account and Access changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🙋 **Mentioning people in a channel.** Typing an at sign in a channel now lists that channel's own members first, before everyone else on the server, so the people you are likely to mean are at the top. [Commit](https://github.com/open-webui/open-webui/commit/ba885d0026ad3cce70c7cc36d1d6f59775264a12), [Commit](https://github.com/open-webui/open-webui/commit/dcff244f9e87e615ee0a3f345f7f801c5ebe370d), [#28883](https://github.com/open-webui/open-webui/issues/28883)

> 🔐 **Terminals that use your own login.** Managed terminals configured for session authentication now authenticate the terminal connection with your own token, where it previously sent no credentials at all. [Commit](https://github.com/open-webui/open-webui/commit/2dadc5435af77b0638af69200e3af1b9654417b6)

> 🎟 **Setting up a tool server that uses OAuth.** Adding one is now easier to get right: the connection dialog can authorize the account from the dialog itself, the check button tests the sign-in details rather than reporting a connection failure that was never going to succeed without them, and it is now labelled for what it does rather than suggesting it verifies the whole connection. [Commit](https://github.com/open-webui/open-webui/commit/f822605b3563c57030aa200492f68572cadcc4da), [#28552](https://github.com/open-webui/open-webui/issues/28552)

> 🪧 **Profile changes from single sign-on.** A name, email address, or picture updated from an identity provider at sign-in now raises an event naming what changed, and the rest of the session uses the updated record rather than a stale copy. [Commit](https://github.com/open-webui/open-webui/commit/927ce0eae67af1b4a856d3e82fba0601c3b40d02)

> 🔔 **Sign-in and sign-out events for single sign-on.** Signing in through an identity provider now raises the same login event that signing in with a password does, and signing out says which provider the session came from, so a function can set up or tidy up an account in another system when someone arrives or leaves. [#27619](https://github.com/open-webui/open-webui/pull/27619), [#27613](https://github.com/open-webui/open-webui/issues/27613)

> 🪟 **Honest OAuth settings.** When single sign-on settings come from the environment rather than being saved in the application, the admin panel now shows them as read-only with a note naming the setting that controls this, instead of accepting edits that were silently discarded on the next restart. [#28276](https://github.com/open-webui/open-webui/pull/28276)

> 🗝️ **Changing a password now ends other sessions.** Changing your password, or an administrator resetting it for you, now stops every device that was already signed in, where they had stayed signed in on the old password until their session expired on its own, up to four weeks by default; the device making the change is signed out too and asked to sign in again, and this requires Redis, without which nothing can be revoked and a warning is now logged saying so. [#28725](https://github.com/open-webui/open-webui/pull/28725), [#28647](https://github.com/open-webui/open-webui/discussions/28647)

> 🩹 **Signing in after a long-delayed upgrade.** Accounts on instances that were upgraded from a version older than 0.6.41 to 0.9.6 or newer can sign in again, where an upgrade step had written their single sign-on identity in a form the application could not read afterwards, and a repair step corrects the affected accounts on startup. [#28107](https://github.com/open-webui/open-webui/pull/28107), [#28101](https://github.com/open-webui/open-webui/issues/28101), [Commit](https://github.com/open-webui/open-webui/commit/bd8378f643dd8a56366ad9d1843b7d40f67cf1f9)

> 🔑 **Signing in with some identity providers.** Logging in through a provider that adds its own vendor-specific information to the header of the sign-in token now completes, rather than failing at the final step with a message claiming the email or password was wrong. [#28065](https://github.com/open-webui/open-webui/pull/28065), [#28062](https://github.com/open-webui/open-webui/issues/28062)

> 🪞 **Matching the right account at sign-in.** Looking up an account by its identity provider details now matches the exact value, where the stored details were searched as loose text and a value contained within another's could be matched instead. [#28624](https://github.com/open-webui/open-webui/pull/28624)

> 🖼 **Downloading a generated image.** Downloading an image from its preview now saves the image, where it could silently save a small file containing an authentication error instead, and a download that does fail now says so. [Commit](https://github.com/open-webui/open-webui/commit/2578174637e48cafa4bcb09adbb1b7f4b545a8d5), [#27723](https://github.com/open-webui/open-webui/pull/27723), [#27722](https://github.com/open-webui/open-webui/issues/27722)

> 🪢 **Signing people out from the identity provider.** A sign-out sent by an identity provider to end someone's session now works, where the check that the message was genuine could fail against providers whose signing keys need the same authentication as everything else, leaving the person signed in. [Commit](https://github.com/open-webui/open-webui/commit/aeda6ff13a25d3b3ba1b303609f35382db22142c)

> ♻ **Blank errors when a tool server's saved sign-in cannot be read.** A tool server whose stored sign-in details cannot be decrypted, which happens when "WEBUI_SECRET_KEY" changes since the key protecting them follows it, now names the server and says to reconnect it, where every startup logged two errors with no message at all. [Commit](https://github.com/open-webui/open-webui/commit/91917b23952af8ca4457f8bb3db70c75ab838fbf), [#28666](https://github.com/open-webui/open-webui/pull/28666), [#28665](https://github.com/open-webui/open-webui/issues/28665)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-56-model-support-changes-in-v0-11-1|56 Model Support changes in v0.11.1]] · Model Support
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-13-account-and-access-changes-in-1-17-0|13 Account and Access changes in 1.17.0]]
- Later: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-3-account-and-access-changes-in-v2-1-247|3 Account and Access changes in v2.1.247]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-86ab25&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-13-account-and-access-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-86ab25%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->