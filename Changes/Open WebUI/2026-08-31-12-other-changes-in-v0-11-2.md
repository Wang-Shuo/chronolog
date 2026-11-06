---
card_id: open-webui-2026-08-31-328af6
date: '2026-08-31'
description: 'Open WebUI · 2026-08-31 · Other changes: 12 changes in v0.11.2 — ⚡ **Less
  overhead on every message.** Deployments without pipelines configured, which is
  the…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 59fa45af8d487e891875049f2ca52175eb3f21973c505f4f33d0d802baf5f923
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-31-328af6
  comparison: ''
  date: '2026-08-31'
  description: 'Open WebUI — v0.11.2: 12 other changes'
  evidence:
  - quote: ⚡ **Less overhead on every message.** Deployments without pipelines configured,
      which is the default, no longer pay setup work for them on each chat message
      and background task. [#29146](https://github.com/open-webui/open-webui/pull/29146)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F90F **More room in file previews on touch screens.** File previews
      on phones and tablets no longer show zoom buttons that sit over an already small
      preview, leaving pinch to zoom to do the job. [#29176](https://github.com/open-webui/open-webui/pull/29176),
      [#29152](https://github.com/open-webui/open-webui/issues/29152)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F310 **Translation updates.** Polish, Simplified Chinese, German,
      Irish, Catalan, and Portuguese (Brazil) translations were expanded, corrected,
      and brought up to date with newer interface text. [#29029](https://github.com/open-webui/open-webui/pull/29029),
      [#29043](https://github.com/open-webui/open-webui/pull/29043), [#29108](https://github.com/open-webui/open-webui/pull/29108),
      [#29151](https://github.com/open-webui/open-webui/pull/29151), [#29184](https://github.com/open-webui/open-webui/pull/29184),
      [#29179](https://github.com/open-webui/open-webui/pull/29179), [#29247](https://github.com/open-webui/open-webui/pull/29247),
      [#29217](https://github.com/open-webui/open-webui/pull/29217)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F4A5 **Replies stop breaking mid-chat.** A conversation no longer
      fails in the browser and stops showing the assistant reply until you reload,
      and chats already saved in that state display and can be edited again. [#29250](https://github.com/open-webui/open-webui/pull/29250),
      [#29244](https://github.com/open-webui/open-webui/issues/29244)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F6D1 **Stop works across instances.** Stopping a response now takes
      effect on deployments that spread people across several instances backed by
      a Redis cluster, instead of the reply continuing to the end regardless. [#29165](https://github.com/open-webui/open-webui/pull/29165),
      [#19840](https://github.com/open-webui/open-webui/issues/19840)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F4D6 **Banners with underlined text.** A banner containing underlined
      text now displays instead of failing to render. [#29118](https://github.com/open-webui/open-webui/pull/29118),
      [#29115](https://github.com/open-webui/open-webui/issues/29115)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F4C6 **Moved calendar events stay visible.** Changing an event's
      date no longer makes it disappear from the calendar, and events already stuck
      in that state show up again. [#29085](https://github.com/open-webui/open-webui/pull/29085),
      [#29067](https://github.com/open-webui/open-webui/issues/29067)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F522 **Accurate admin user counts.** The counts on the admin Users
      tabs now follow your search and reset when you switch tabs, instead of showing
      stale or unfiltered numbers. [#29080](https://github.com/open-webui/open-webui/pull/29080),
      [#29079](https://github.com/open-webui/open-webui/issues/29079)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F9F1 **Long setting values stop crushing labels.** Settings rows
      now let long controls shrink inside the available space instead of squeezing
      the label beside them. [#29229](https://github.com/open-webui/open-webui/pull/29229)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F4F2 **Dropdowns stay on screen.** A dropdown near the edge of a
      narrow screen now shifts inward to stay fully visible instead of opening past
      the edge with its option labels cut off. [#29226](https://github.com/open-webui/open-webui/pull/29226),
      [#29225](https://github.com/open-webui/open-webui/issues/29225)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F39B️ **Valves dialog stays in bounds.** A valve whose selected
      options form a long line no longer stretches its input past the edge of the
      dialog and over the page behind it. [#29203](https://github.com/open-webui/open-webui/pull/29203),
      [#29202](https://github.com/open-webui/open-webui/issues/29202)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  - quote: "\U0001F3F7️ **Labels with colons and example URLs translate correctly.**
      Interface text such as `Warning:`, `http://localhost:8000`, and `https://mineru.net/api/v4`
      now appears correctly instead of being misread by the translation system. [#29161](https://github.com/open-webui/open-webui/pull/29161),
      [#29154](https://github.com/open-webui/open-webui/issues/29154)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 12-other-changes-in-v0-11-2
  source_release: open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b
  source_type: github_releases
  theme: uncategorized
  title: 12 other changes in v0.11.2
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b]]'
source_type: github_releases
theme: uncategorized
title: 12 other changes in v0.11.2
type: change
---

<!-- chronolog:begin region="header" -->
# 12 other changes in v0.11.2

**Open WebUI** · 2026-08-31 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.2) · from [[Releases/Open WebUI/open-webui-2026-08-31-v0-11-2-github-379534902-6de0950b|v0.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ⚡ **Less overhead on every message.** Deployments without pipelines configured, which is the default, no longer pay setup work for them on each chat message and background task. [#29146](https://github.com/open-webui/open-webui/pull/29146)

> 🤏 **More room in file previews on touch screens.** File previews on phones and tablets no longer show zoom buttons that sit over an already small preview, leaving pinch to zoom to do the job. [#29176](https://github.com/open-webui/open-webui/pull/29176), [#29152](https://github.com/open-webui/open-webui/issues/29152)

> 🌐 **Translation updates.** Polish, Simplified Chinese, German, Irish, Catalan, and Portuguese (Brazil) translations were expanded, corrected, and brought up to date with newer interface text. [#29029](https://github.com/open-webui/open-webui/pull/29029), [#29043](https://github.com/open-webui/open-webui/pull/29043), [#29108](https://github.com/open-webui/open-webui/pull/29108), [#29151](https://github.com/open-webui/open-webui/pull/29151), [#29184](https://github.com/open-webui/open-webui/pull/29184), [#29179](https://github.com/open-webui/open-webui/pull/29179), [#29247](https://github.com/open-webui/open-webui/pull/29247), [#29217](https://github.com/open-webui/open-webui/pull/29217)

> 💥 **Replies stop breaking mid-chat.** A conversation no longer fails in the browser and stops showing the assistant reply until you reload, and chats already saved in that state display and can be edited again. [#29250](https://github.com/open-webui/open-webui/pull/29250), [#29244](https://github.com/open-webui/open-webui/issues/29244)

> 🛑 **Stop works across instances.** Stopping a response now takes effect on deployments that spread people across several instances backed by a Redis cluster, instead of the reply continuing to the end regardless. [#29165](https://github.com/open-webui/open-webui/pull/29165), [#19840](https://github.com/open-webui/open-webui/issues/19840)

> 📖 **Banners with underlined text.** A banner containing underlined text now displays instead of failing to render. [#29118](https://github.com/open-webui/open-webui/pull/29118), [#29115](https://github.com/open-webui/open-webui/issues/29115)

> 📆 **Moved calendar events stay visible.** Changing an event's date no longer makes it disappear from the calendar, and events already stuck in that state show up again. [#29085](https://github.com/open-webui/open-webui/pull/29085), [#29067](https://github.com/open-webui/open-webui/issues/29067)

> 🔢 **Accurate admin user counts.** The counts on the admin Users tabs now follow your search and reset when you switch tabs, instead of showing stale or unfiltered numbers. [#29080](https://github.com/open-webui/open-webui/pull/29080), [#29079](https://github.com/open-webui/open-webui/issues/29079)

> 🧱 **Long setting values stop crushing labels.** Settings rows now let long controls shrink inside the available space instead of squeezing the label beside them. [#29229](https://github.com/open-webui/open-webui/pull/29229)

> 📲 **Dropdowns stay on screen.** A dropdown near the edge of a narrow screen now shifts inward to stay fully visible instead of opening past the edge with its option labels cut off. [#29226](https://github.com/open-webui/open-webui/pull/29226), [#29225](https://github.com/open-webui/open-webui/issues/29225)

> 🎛️ **Valves dialog stays in bounds.** A valve whose selected options form a long line no longer stretches its input past the edge of the dialog and over the page behind it. [#29203](https://github.com/open-webui/open-webui/pull/29203), [#29202](https://github.com/open-webui/open-webui/issues/29202)

> 🏷️ **Labels with colons and example URLs translate correctly.** Interface text such as `Warning:`, `http://localhost:8000`, and `https://mineru.net/api/v4` now appears correctly instead of being misread by the translation system. [#29161](https://github.com/open-webui/open-webui/pull/29161), [#29154](https://github.com/open-webui/open-webui/issues/29154)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-31-large-tool-calls-stream-faster-through-anthropic-compatible-clients-when-a-strea|🧠 Large tool calls stream faster through Anthropic-compatible…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-31-3-automation-and-scheduling-changes-in-v0-11-2|3 Automation and Scheduling changes in v0.11.2]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-31-3-interface-experience-changes-in-v0-11-2|3 Interface Experience changes in v0.11.2]] · Interface Experience
- [[Changes/Open WebUI/2026-08-31-code-interpreter-starts-on-windows-the-built-in-code-interpreter-now-serves-its|🐍 Code interpreter starts on Windows. The built-in code interpreter now serves…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-31-security-advisory-this-release-includes-security-and-access-control-fixes-we-rec|🛡️ Security Advisory: This release includes security and access-control fixes]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-31-high-contrast-mode-is-now-accessibility-mode-the-interface-setting-previously-ca|🏷️ High Contrast Mode is now Accessibility Mode. The interface setting…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-31-9-developer-workflow-changes-in-v0-11-2|9 Developer Workflow changes in v0.11.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-31-2-files-and-data-changes-in-v0-11-2|2 Files and Data changes in v0.11.2]] · Files and Data
- [[Changes/Open WebUI/2026-08-31-10-model-support-changes-in-v0-11-2|10 Model Support changes in v0.11.2]] · Model Support
- [[Changes/Open WebUI/2026-08-31-2-collaboration-changes-in-v0-11-2|2 Collaboration changes in v0.11.2]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-31-328af6&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-31-12-other-changes-in-v0-11-2.md%0ACard%20ID%3A%20open-webui-2026-08-31-328af6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->