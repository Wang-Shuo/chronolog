---
card_id: open-webui-2026-10-16-dd5ea1
date: '2026-10-16'
description: "Open WebUI · 2026-10-16 · Safety and Privacy: 2 changes in v0.12.3 —
  \U0001F510 **End-to-end encrypted chats.** Direct messages and private group channels
  can now hold…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2271
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d090b90c9e4c27053858f379b24c53aefe1b20d915202debdebaede457020a64
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-16-dd5ea1
  comparison: ''
  date: '2026-10-16'
  description: 'Open WebUI — v0.12.3: 2 Safety and Privacy changes'
  evidence:
  - quote: "\U0001F510 **End-to-end encrypted chats.** Direct messages and private
      group channels can now hold a temporary end-to-end encrypted chat: a member
      picks Encrypted Chat in the channel menu, the other members see \"Encrypted
      chat in progress\" with a Join link, messages of up to 16 KiB are encrypted
      in the browser with MLS and only passed through the server without being saved,
      participants can verify each other by comparing codes and see when others are
      typing, and the chat is cleared when you leave or reload and ends when channel
      membership or access changes. Administrators turn it on under Admin Settings
      > General > Encrypted channels or with \"ENABLE_ENCRYPTED_CHANNELS\" and grant
      it with the new Encrypted Channels permission, off by default or set with \"USER_PERMISSIONS_FEATURES_ENCRYPTED_CHANNELS\",
      and it needs websocket connections with websocket server logging off and HTTPS
      in production. [Commit](https://github.com/open-webui/open-webui/commit/7dc91de86c41866f4170602f074c39dbf1609377),
      [Commit](https://github.com/open-webui/open-webui/commit/0b3812f2857b4c65fd1ab931f40de4f1264edc46),
      [Commit](https://github.com/open-webui/open-webui/commit/b1e876896caee5bf30a010fb414a9249ec7f59a2),
      [Commit](https://github.com/open-webui/open-webui/commit/4dedaaf6e2292c2c4fb48668eee1292cfd7de2d0)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  - quote: "\U0001F4EE **Redis permissions for room channels.** With \"WEBSOCKET_REDIS_ROOM_CHANNELS\"
      on, the Redis user now needs the PUBLISH, SUBSCRIBE, UNSUBSCRIBE and PING permissions
      and access to the \"&socketio\" and \"&socketio#\\*\" channels, while PSUBSCRIBE
      is no longer used; a missing permission is logged with how to fix it. [Commit](https://github.com/open-webui/open-webui/commit/362b01d0b2ba677858a5af85caf3dd8544c5e6df)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 2-safety-and-privacy-changes-in-v0-12-3
  source_release: open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v0.12.3
  type: change
related_changes:
- '[[Changes/Cline/2026-10-16-cline-cloud-sessions-rolling-out-gradually-run-a-task-in-a-hosted-sandbox-on-a-g|Cline
  Cloud sessions, rolling out gradually]]'
- '[[Changes/Lovable/2026-10-16-lovable-writes-and-runs-tests-for-the-rules-you-change|Lovable
  writes and runs tests for the rules you change]]'
- '[[Changes/Lovable/2026-10-16-require-approval-or-block-publishing-with-workspace-policies|Require
  approval or block publishing with workspace policies]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v0.12.3
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v0.12.3

**Open WebUI** · 2026-10-16 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.3) · from [[Releases/Open WebUI/open-webui-2026-10-16-v0-12-3-github-414903453-58a8a82d|v0.12.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔐 **End-to-end encrypted chats.** Direct messages and private group channels can now hold a temporary end-to-end encrypted chat: a member picks Encrypted Chat in the channel menu, the other members see "Encrypted chat in progress" with a Join link, messages of up to 16 KiB are encrypted in the browser with MLS and only passed through the server without being saved, participants can verify each other by comparing codes and see when others are typing, and the chat is cleared when you leave or reload and ends when channel membership or access changes. Administrators turn it on under Admin Settings > General > Encrypted channels or with "ENABLE_ENCRYPTED_CHANNELS" and grant it with the new Encrypted Channels permission, off by default or set with "USER_PERMISSIONS_FEATURES_ENCRYPTED_CHANNELS", and it needs websocket connections with websocket server logging off and HTTPS in production. [Commit](https://github.com/open-webui/open-webui/commit/7dc91de86c41866f4170602f074c39dbf1609377), [Commit](https://github.com/open-webui/open-webui/commit/0b3812f2857b4c65fd1ab931f40de4f1264edc46), [Commit](https://github.com/open-webui/open-webui/commit/b1e876896caee5bf30a010fb414a9249ec7f59a2), [Commit](https://github.com/open-webui/open-webui/commit/4dedaaf6e2292c2c4fb48668eee1292cfd7de2d0)

> 📮 **Redis permissions for room channels.** With "WEBSOCKET_REDIS_ROOM_CHANNELS" on, the Redis user now needs the PUBLISH, SUBSCRIBE, UNSUBSCRIBE and PING permissions and access to the "&socketio" and "&socketio#\*" channels, while PSUBSCRIBE is no longer used; a missing permission is logged with how to fix it. [Commit](https://github.com/open-webui/open-webui/commit/362b01d0b2ba677858a5af85caf3dd8544c5e6df)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-16-built-in-tools-turned-back-on-stay-on-a-built-in-tool-such-as-memory-that-is-off|🧰 Built-in tools turned back on stay on. A built-in tool such as Memory…]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-16-20-developer-workflow-changes-in-v0-12-3|20 Developer Workflow changes in v0.12.3]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-16-4-files-and-data-changes-in-v0-12-3|4 Files and Data changes in v0.12.3]] · Files and Data
- [[Changes/Open WebUI/2026-10-16-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-16-3-model-support-changes-in-v0-12-3|3 Model Support changes in v0.12.3]] · Model Support
- [[Changes/Open WebUI/2026-10-16-2-account-and-access-changes-in-v0-12-3|2 Account and Access changes in v0.12.3]] · Account and Access
- [[Changes/Open WebUI/2026-10-16-2-enterprise-and-administration-changes-in-v0-12-3|2 Enterprise and Administration changes in v0.12.3]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-16-2-context-window-changes-in-v0-12-3|2 Context Window changes in v0.12.3]] · Context Window
- [[Changes/Open WebUI/2026-10-16-clear-input-selections-shortcut-clearing-the-model-override-selected-tools-and-f|🧹 Clear Input Selections shortcut. Clearing the model override, selected tools…]] · Image Generation
- [[Changes/Open WebUI/2026-10-16-built-in-tools-with-a-custom-tools-parameter-a-model-with-a-custom-parameter-nam|🧩 Built-in tools with a custom tools parameter. A model with a custom parameter…]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-16-4-interface-experience-changes-in-v0-12-3|4 Interface Experience changes in v0.12.3]] · Interface Experience
- [[Changes/Open WebUI/2026-10-16-2-editor-experience-changes-in-v0-12-3|2 Editor Experience changes in v0.12.3]] · Editor Experience
- [[Changes/Open WebUI/2026-10-16-2-collaboration-changes-in-v0-12-3|2 Collaboration changes in v0.12.3]] · Collaboration
- [[Changes/Open WebUI/2026-10-16-translation-updates-translations-for-portuguese-brazil-chinese-traditional-arabi|🌐 Translation updates. Translations for Portuguese (Brazil), Chinese…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-16 · Lovable · [[Changes/Lovable/2026-10-16-require-approval-or-block-publishing-with-workspace-policies|Require approval or block publishing with workspace policies]]
- Later: 2026-10-16 · OpenClaw · [[Changes/OpenClaw/2026-10-16-2-safety-and-privacy-changes-in-v2026-10-4|2 Safety and Privacy changes in v2026.10.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-16-dd5ea1&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-16-2-safety-and-privacy-changes-in-v0-12-3.md%0ACard%20ID%3A%20open-webui-2026-10-16-dd5ea1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->