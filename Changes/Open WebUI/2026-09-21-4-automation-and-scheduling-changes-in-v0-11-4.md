---
card_id: open-webui-2026-09-21-d28d8a
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Automation and Scheduling: 4 changes in v0.11.4
  — \U0001F5D1️ **Quick delete shortcut.** Holding Shift over a note in the list or
  grid, or…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 993
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8497eebffeca0949314b4b0dfef599e52a1bc12f99f72decffc9412a926101d7
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-d28d8a
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 4 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F5D1️ **Quick delete shortcut.** Holding Shift over a note in the
      list or grid, or over a row on the automations page, turns its trailing controls
      into a delete button, removing the entry in one click rather than the three
      the menu and its confirmation ask for. [#29635](https://github.com/open-webui/open-webui/pull/29635),
      [#29633](https://github.com/open-webui/open-webui/issues/29633), [#29640](https://github.com/open-webui/open-webui/pull/29640),
      [#29637](https://github.com/open-webui/open-webui/issues/29637)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⏰ **Automation schedule parsing.** An automation whose rule puts the time
      in "DTSTART" is now read at that hour, rather than listed at midnight and opened
      at nine, which moved when it ran as soon as it was saved again. [Commit](https://github.com/open-webui/open-webui/commit/540467b90a430e47e536c20710878b342de659fb)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⌛ **Stalled schedules and stuck tasks.** A schedule whose rule takes too
      long to work out no longer holds up the round that evaluates it and is skipped
      with a warning, and background tasks shared through Redis now expire once their
      worker falls silent, after "REDIS_TASK_TTL" seconds. [Commit](https://github.com/open-webui/open-webui/commit/5fb869db221d9599a576e8e2eea9c3314947d25e)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5E8️ **Channel model terminals.** A model with a terminal chosen
      in the workspace had that choice honoured in a chat but dropped where it answered
      in a channel or ran as a channel automation, so it worked without one; it now
      carries the same terminal everywhere, alongside the tools, filters and features
      it already carried. [Commit](https://github.com/open-webui/open-webui/commit/c78ad89934095c4e42e3f059d400a24fe5681de2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 4-automation-and-scheduling-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: automation-scheduling
  title: 4 Automation and Scheduling changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-17-automate-your-workspace-with-the-lovable-api|Automate
  your workspace with the Lovable API]]'
- '[[Changes/OpenHands/2026-09-17-feat-automations-select-saved-agent-profiles-by-neubig-in-https-github-com-openh|feat(automations):
  select saved agent profiles]]'
- '[[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14
  Automation and Scheduling changes in v2026.9.5]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: automation-scheduling
title: 4 Automation and Scheduling changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Automation and Scheduling changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🗑️ **Quick delete shortcut.** Holding Shift over a note in the list or grid, or over a row on the automations page, turns its trailing controls into a delete button, removing the entry in one click rather than the three the menu and its confirmation ask for. [#29635](https://github.com/open-webui/open-webui/pull/29635), [#29633](https://github.com/open-webui/open-webui/issues/29633), [#29640](https://github.com/open-webui/open-webui/pull/29640), [#29637](https://github.com/open-webui/open-webui/issues/29637)

> ⏰ **Automation schedule parsing.** An automation whose rule puts the time in "DTSTART" is now read at that hour, rather than listed at midnight and opened at nine, which moved when it ran as soon as it was saved again. [Commit](https://github.com/open-webui/open-webui/commit/540467b90a430e47e536c20710878b342de659fb)

> ⌛ **Stalled schedules and stuck tasks.** A schedule whose rule takes too long to work out no longer holds up the round that evaluates it and is skipped with a warning, and background tasks shared through Redis now expire once their worker falls silent, after "REDIS_TASK_TTL" seconds. [Commit](https://github.com/open-webui/open-webui/commit/5fb869db221d9599a576e8e2eea9c3314947d25e)

> 🗨️ **Channel model terminals.** A model with a terminal chosen in the workspace had that choice honoured in a chat but dropped where it answered in a channel or ran as a channel automation, so it worked without one; it now carries the same terminal everywhere, alongside the tools, filters and features it already carried. [Commit](https://github.com/open-webui/open-webui/commit/c78ad89934095c4e42e3f059d400a24fe5681de2)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-09-19 · OpenClaw · [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-d28d8a&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-d28d8a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->