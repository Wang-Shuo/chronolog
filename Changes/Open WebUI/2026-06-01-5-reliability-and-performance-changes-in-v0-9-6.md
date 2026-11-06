---
card_id: open-webui-2026-06-01-ee98ee
date: '2026-06-01'
description: 'Open WebUI · 2026-06-01 · Reliability and Performance: 5 changes in
  v0.9.6 — ⚡ **Faster initial page loads.** The configuration endpoint that loads
  on every…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1264
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8bd441db05ca3b829c9e9d7ae433cec364c45d867431ec240eadfdb02fd6e8ab
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-01-ee98ee
  comparison: ''
  date: '2026-06-01'
  description: 'Open WebUI — v0.9.6: 5 Reliability and Performance changes'
  evidence:
  - quote: ⚡ **Faster initial page loads.** The configuration endpoint that loads
      on every page visit no longer runs an unnecessary user-count query, making the
      initial application load lighter on the database, especially on instances with
      many users. [Commit](https://github.com/open-webui/open-webui/commit/0adc090dcbe636c9c9645d8ec7f6b89ea514870b)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F680 **Faster tool-enabled chat completions.** Chat completions
      that use multiple tools now start faster because the tools they reference are
      fetched from the database in a single batch query instead of one query per tool.
      [#24808](https://github.com/open-webui/open-webui/pull/24808), [Commit](https://github.com/open-webui/open-webui/commit/cc94a90b4d4d690bc7cb9f7124f2d6e552973970)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F4C9 **Faster websocket disconnect cleanup.** Disconnecting from
      a collaborative session no longer triggers a scan across the entire Redis keyspace,
      using a per-session index instead, which keeps disconnects cheap on large deployments.
      [#25466](https://github.com/open-webui/open-webui/issues/25466), [Commit](https://github.com/open-webui/open-webui/commit/c7de057a4a54cc80f366ad949417e78fae756d4c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F504 **General improvements.** Various improvements were implemented
      across the application to enhance performance, stability, and security."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  - quote: "\U0001F9F5 **Channel thread and pinned message stability.** Opening a
      channel thread or the pinned messages view no longer fails to render when a
      message or its data is missing. [#25209](https://github.com/open-webui/open-webui/pull/25209)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 5-reliability-and-performance-changes-in-v0-9-6
  source_release: open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e
  source_type: github_releases
  theme: reliability-performance
  title: 5 Reliability and Performance changes in v0.9.6
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-28-renamed-the-effort-slider-labels-from-speed-intelligence-to-faster-smarter-for-c|Renamed
  the /effort slider labels…]]'
- '[[Changes/Lovable/2026-05-28-improvements-and-bug-fixes|Improvements and bug fixes]]'
- '[[Changes/Claude Code/2026-05-29-improved-performance-of-long-and-resumed-conversations-by-eliminating-redundant|Improved
  performance of long and resumed conversations by eliminating redundant…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e]]'
source_type: github_releases
theme: reliability-performance
title: 5 Reliability and Performance changes in v0.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Reliability and Performance changes in v0.9.6

**Open WebUI** · 2026-06-01 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.9.6) · from [[Releases/Open WebUI/open-webui-2026-06-01-v0-9-6-github-332798378-d8dc258e|v0.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Faster initial page loads.** The configuration endpoint that loads on every page visit no longer runs an unnecessary user-count query, making the initial application load lighter on the database, especially on instances with many users. [Commit](https://github.com/open-webui/open-webui/commit/0adc090dcbe636c9c9645d8ec7f6b89ea514870b)

> 🚀 **Faster tool-enabled chat completions.** Chat completions that use multiple tools now start faster because the tools they reference are fetched from the database in a single batch query instead of one query per tool. [#24808](https://github.com/open-webui/open-webui/pull/24808), [Commit](https://github.com/open-webui/open-webui/commit/cc94a90b4d4d690bc7cb9f7124f2d6e552973970)

> 📉 **Faster websocket disconnect cleanup.** Disconnecting from a collaborative session no longer triggers a scan across the entire Redis keyspace, using a per-session index instead, which keeps disconnects cheap on large deployments. [#25466](https://github.com/open-webui/open-webui/issues/25466), [Commit](https://github.com/open-webui/open-webui/commit/c7de057a4a54cc80f366ad949417e78fae756d4c)

> 🔄 **General improvements.** Various improvements were implemented across the application to enhance performance, stability, and security.

> 🧵 **Channel thread and pinned message stability.** Opening a channel thread or the pinned messages view no longer fails to render when a message or its data is missing. [#25209](https://github.com/open-webui/open-webui/pull/25209)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-01-bulk-enable-or-disable-automations-automations-can-now-be-enabled-or-disabled-in|🔘 Bulk enable or disable automations. Automations can now be enabled or disabled…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-01-4-context-window-changes-in-v0-9-6|4 Context Window changes in v0.9.6]] · Context Window
- [[Changes/Open WebUI/2026-06-01-2-memory-and-personalization-changes-in-v0-9-6|2 Memory and Personalization changes in v0.9.6]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-01-keyboard-and-screen-reader-access-to-menus-the-integrations-more-options-and-use|♿ Keyboard and screen reader access to menus. The integrations, more-options…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-01-4-interface-experience-changes-in-v0-9-6|4 Interface Experience changes in v0.9.6]] · Interface Experience
- [[Changes/Open WebUI/2026-06-01-4-editor-experience-changes-in-v0-9-6|4 Editor Experience changes in v0.9.6]] · Editor Experience
- [[Changes/Open WebUI/2026-06-01-5-files-and-data-changes-in-v0-9-6|5 Files and Data changes in v0.9.6]] · Files and Data
- [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-01-startup-on-non-unicode-consoles-open-webui-no-longer-crashes-at-startup-when-the|🥾 Startup on non-Unicode consoles. Open WebUI no longer crashes at startup…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-01-youtube-short-link-transcripts-pasting-a-youtu-be-short-link-into-a-chat-now-loa|📺 YouTube short link transcripts. Pasting a "youtu.be" short link into a chat…]] · Multimodal Input
- [[Changes/Open WebUI/2026-06-01-9-search-and-browsing-changes-in-v0-9-6|9 Search and Browsing changes in v0.9.6]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-01-shared-chat-file-write-protection-access-to-a-file-through-a-shared-chat-now-onl|🔐 Shared-chat file write protection. Access to a file through a shared chat now…]] · Collaboration
- [[Changes/Open WebUI/2026-06-01-2-enterprise-and-administration-changes-in-v0-9-6|2 Enterprise and Administration changes in v0.9.6]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-01-image-generation-with-non-standard-response-headers-image-generation-now-works-w|🖌️ Image generation with non-standard response headers. Image generation now…]] · Image Generation
- [[Changes/Open WebUI/2026-06-01-6-account-and-access-changes-in-v0-9-6|6 Account and Access changes in v0.9.6]] · Account and Access
- [[Changes/Open WebUI/2026-06-01-12-model-support-changes-in-v0-9-6|12 Model Support changes in v0.9.6]] · Model Support
- [[Changes/Open WebUI/2026-06-01-4-apps-and-integrations-changes-in-v0-9-6|4 Apps and Integrations changes in v0.9.6]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-01-4-voice-and-audio-changes-in-v0-9-6|4 Voice and Audio changes in v0.9.6]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-01-20-other-changes-in-v0-9-6|20 other changes in v0.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-05-29 · Claude Code · [[Changes/Claude Code/2026-05-29-improved-performance-of-long-and-resumed-conversations-by-eliminating-redundant|Improved performance of long and resumed conversations by eliminating redundant…]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-improved-auto-mode-classifier-latency-by-reducing-reasoning-on-routine-actions-l|Improved auto mode classifier latency by reducing reasoning on routine actions…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-01-ee98ee&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-01-5-reliability-and-performance-changes-in-v0-9-6.md%0ACard%20ID%3A%20open-webui-2026-06-01-ee98ee%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->