---
card_id: open-webui-2026-08-25-5584ee
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Reliability and Performance: 10 changes in
  v0.11.1 — \U0001FAB5 **Much faster throughout.** Hundreds of places across the application
  no…"
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2836
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 20516fabb9920516396834f5c14e54199b598a1f1b9f4c12922d8650a7e52a94
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-5584ee
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 10 Reliability and Performance changes'
  evidence:
  - quote: "\U0001FAB5 **Much faster throughout.** Hundreds of places across the application
      no longer assemble detailed log text that is switched off and thrown away unread,
      so sending messages, uploading and indexing files, running searches, signing
      in, and loading admin pages all get that time back, with the largest gains on
      busy servers, in long conversations, and on chats that draw from a large knowledge
      base. [#27834](https://github.com/open-webui/open-webui/pull/27834), [#27837](https://github.com/open-webui/open-webui/pull/27837)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⚙️ **Much faster JSON handling.** Saving and opening chats, reading settings,
      returning results from built-in tools, streaming replies, signing in and signing
      up, working out your permissions, and reading stored chunk details during knowledge
      base searches on Valkey and Oracle vector storage are all handled much faster
      across the application when the "ENABLE_ORJSON" option is turned on. [Commit](https://github.com/open-webui/open-webui/commit/bb0f898b431d5aa45efa7805956657ed9c3dd78d),
      [#28396](https://github.com/open-webui/open-webui/pull/28396), [#27841](https://github.com/open-webui/open-webui/pull/27841),
      [#27807](https://github.com/open-webui/open-webui/pull/27807), [#27805](https://github.com/open-webui/open-webui/pull/27805),
      [#27813](https://github.com/open-webui/open-webui/pull/27813)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E4 **Much faster outbound requests.** Conversations and embedding
      batches sent to Ollama and Anthropic models are packaged for delivery much faster,
      which is most noticeable in long chats when the \"ENABLE_ORJSON\" option is
      turned on. [#27811](https://github.com/open-webui/open-webui/pull/27811), [#27810](https://github.com/open-webui/open-webui/pull/27810)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3C1 **Faster skills on large instances.** Opening the skills list,
      or sending a message that uses one, no longer checks every skill on the instance
      one at a time, so both are far quicker where many skills exist and most of them
      are not yours. [#28798](https://github.com/open-webui/open-webui/pull/28798)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9F1 **Faster folder listings.** Listing your folders now works
      out your group memberships once for the whole listing rather than again for
      every item in every folder. [#28810](https://github.com/open-webui/open-webui/pull/28810)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4EE **Faster handing off a streaming reply.** Passing a reply in
      progress between instances now writes it once rather than converting it back
      and forth and scanning it for characters that only matter elsewhere, which on
      a large non-English conversation took most of the time spent on each write.
      [#28833](https://github.com/open-webui/open-webui/pull/28833)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4BD **Faster saving of long chats.** A chat is now written to the
      database in one go rather than one message at a time, so saving a long conversation
      is much quicker and puts far less strain on the database, and saving one where
      nothing has changed writes nothing at all. [#28806](https://github.com/open-webui/open-webui/pull/28806)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E6 **Faster loading of shared folders.** Folders shared with you
      now load in a couple of queries rather than one for each folder and each owner,
      so the list appears sooner for anyone with many of them. [#28804](https://github.com/open-webui/open-webui/pull/28804)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4E1 **Intermittent connection failures.** Requests to model providers
      and to services on the same network no longer fail intermittently with name
      lookup errors, often surfacing as a misleading model not found message, because
      addresses are resolved through the system again by default, with the faster
      resolver still available through \"AIOHTTP_CLIENT_ASYNC_DNS_RESOLVER\". [#28242](https://github.com/open-webui/open-webui/pull/28242),
      [#28013](https://github.com/open-webui/open-webui/issues/28013), [#28215](https://github.com/open-webui/open-webui/issues/28215)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 10-reliability-and-performance-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: reliability-performance
  title: 10 Reliability and Performance changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-08-24-improved-git-responsiveness-and-reduced-background-cpu-usage-on-large-repositori|Improved
  Git responsiveness and reduced background CPU usage on large repositories…]]'
- '[[Changes/Claude Code/2026-08-25-improved-bash-tool-latency-on-bash-shells-by-replaying-snapshot-functions-withou|Improved
  Bash tool latency on bash shells by replaying snapshot functions without…]]'
- '[[Changes/Dify/2026-08-25-workflow-runtime-stability|Workflow & Runtime Stability]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: reliability-performance
title: 10 Reliability and Performance changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Reliability and Performance changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🪵 **Much faster throughout.** Hundreds of places across the application no longer assemble detailed log text that is switched off and thrown away unread, so sending messages, uploading and indexing files, running searches, signing in, and loading admin pages all get that time back, with the largest gains on busy servers, in long conversations, and on chats that draw from a large knowledge base. [#27834](https://github.com/open-webui/open-webui/pull/27834), [#27837](https://github.com/open-webui/open-webui/pull/27837)

> ⚙️ **Much faster JSON handling.** Saving and opening chats, reading settings, returning results from built-in tools, streaming replies, signing in and signing up, working out your permissions, and reading stored chunk details during knowledge base searches on Valkey and Oracle vector storage are all handled much faster across the application when the "ENABLE_ORJSON" option is turned on. [Commit](https://github.com/open-webui/open-webui/commit/bb0f898b431d5aa45efa7805956657ed9c3dd78d), [#28396](https://github.com/open-webui/open-webui/pull/28396), [#27841](https://github.com/open-webui/open-webui/pull/27841), [#27807](https://github.com/open-webui/open-webui/pull/27807), [#27805](https://github.com/open-webui/open-webui/pull/27805), [#27813](https://github.com/open-webui/open-webui/pull/27813)

> 📤 **Much faster outbound requests.** Conversations and embedding batches sent to Ollama and Anthropic models are packaged for delivery much faster, which is most noticeable in long chats when the "ENABLE_ORJSON" option is turned on. [#27811](https://github.com/open-webui/open-webui/pull/27811), [#27810](https://github.com/open-webui/open-webui/pull/27810)

> 🏁 **Faster skills on large instances.** Opening the skills list, or sending a message that uses one, no longer checks every skill on the instance one at a time, so both are far quicker where many skills exist and most of them are not yours. [#28798](https://github.com/open-webui/open-webui/pull/28798)

> 🧱 **Faster folder listings.** Listing your folders now works out your group memberships once for the whole listing rather than again for every item in every folder. [#28810](https://github.com/open-webui/open-webui/pull/28810)

> 📮 **Faster handing off a streaming reply.** Passing a reply in progress between instances now writes it once rather than converting it back and forth and scanning it for characters that only matter elsewhere, which on a large non-English conversation took most of the time spent on each write. [#28833](https://github.com/open-webui/open-webui/pull/28833)

> 💽 **Faster saving of long chats.** A chat is now written to the database in one go rather than one message at a time, so saving a long conversation is much quicker and puts far less strain on the database, and saving one where nothing has changed writes nothing at all. [#28806](https://github.com/open-webui/open-webui/pull/28806)

> 📦 **Faster loading of shared folders.** Folders shared with you now load in a couple of queries rather than one for each folder and each owner, so the list appears sooner for anyone with many of them. [#28804](https://github.com/open-webui/open-webui/pull/28804)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

> 📡 **Intermittent connection failures.** Requests to model providers and to services on the same network no longer fail intermittently with name lookup errors, often surfacing as a misleading model not found message, because addresses are resolved through the system again by default, with the faster resolver still available through "AIOHTTP_CLIENT_ASYNC_DNS_RESOLVER". [#28242](https://github.com/open-webui/open-webui/pull/28242), [#28013](https://github.com/open-webui/open-webui/issues/28013), [#28215](https://github.com/open-webui/open-webui/issues/28215)

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
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
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
## Nearby in Reliability and Performance

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-workflow-runtime-stability|Workflow & Runtime Stability]]
- Later: 2026-08-25 · Raycast · [[Changes/Raycast/2026-08-25-ui-improved-scrolling-performance-across-the-app|UI : Improved scrolling performance across the app]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-5584ee&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-10-reliability-and-performance-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-5584ee%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->