---
card_id: open-webui-2026-07-27-1897a4
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Automation and Scheduling: 9 changes in v0.11.0
  — \U0001F9FA **Automations that file their chats away.** An automation can now be
  pointed at…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 937
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 01590190fd059691b50085bf19272809af82166adb27d51f79dc53771f62060b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-1897a4
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 9 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F9FA **Automations that file their chats away.** An automation can
      now be pointed at one of your folders, from the dialog, the editor or by asking
      the assistant, so each run lands there instead of loose in your chat list, and
      the folder is cleared automatically if it is later deleted. [Commit](https://github.com/open-webui/open-webui/commit/f798d05586a140f1a6b51f1e51b2b2a63d079d45),
      [Commit](https://github.com/open-webui/open-webui/commit/bab71ed08b5af6f4a8ff2daa02792baae9edab03),
      [Commit](https://github.com/open-webui/open-webui/commit/db5c092299471444c356216d5ef39b382ba1aa1e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4BE **Import notes and automations.** Notes can now be brought
      in from text and markdown files, and automations can be exported and imported
      as files, so you can move them between instances. [Commit](https://github.com/open-webui/open-webui/commit/f8350360dfd60ff890b73fe2f39aaf20a52ad28b),
      [Commit](https://github.com/open-webui/open-webui/commit/2018546a7baeb853bb4d98e2fb2a092ef20aa431)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F570️ **Faster automation scheduling.** Working out when an automation
      that repeats every few minutes or hours runs next is now near instant, instead
      of taking twenty seconds or more and slowing further each year. [Commit](https://github.com/open-webui/open-webui/commit/b3aead23da6cf8ebeedbd9fa3b97c7ac1a3f54ec),
      [#26954](https://github.com/open-webui/open-webui/issues/26954)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6A5 **Automation limits in chat.** Automations that the assistant
      creates or reschedules on your behalf now respect the same maximum count and
      minimum interval as the ones you set up yourself, instead of being able to exceed
      both. [#27523](https://github.com/open-webui/open-webui/pull/27523), [#27121](https://github.com/open-webui/open-webui/issues/27121)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F319 **Date pickers in dark mode.** The calendar and clock icons
      on date and time fields are now visible in dark mode, across the calendar, automation
      schedules, account settings and analytics. [#27275](https://github.com/open-webui/open-webui/pull/27275),
      [#27274](https://github.com/open-webui/open-webui/issues/27274)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5D3️ **Automation dialog on narrow screens.** The buttons along
      the bottom of the automation dialog now sit on their own row on a phone, instead
      of the schedule and model pickers wrapping and pushing Cancel into the middle.
      [#27027](https://github.com/open-webui/open-webui/pull/27027)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9ED **Sidebar access from the automation editor.** Opening an automation
      on a phone no longer hides the sidebar button, so you can move around without
      leaving the editor first."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⏰ **Recurring automation scheduling.** Automations that repeat every few
      minutes or hours now align to the clock and are no longer wrongly rejected as
      having no upcoming runs when the server clock is ahead of your timezone. [Commit](https://github.com/open-webui/open-webui/commit/b3aead23da6cf8ebeedbd9fa3b97c7ac1a3f54ec),
      [#26954](https://github.com/open-webui/open-webui/issues/26954)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F510 **Administrators no longer reach other people's automations.**
      Viewing, editing, running and deleting an automation is now limited to the person
      who created it, so an administrator with a link to someone else's automation
      is refused rather than allowed through. [Commit](https://github.com/open-webui/open-webui/commit/f798d05586a140f1a6b51f1e51b2b2a63d079d45)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-automation-and-scheduling-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: automation-scheduling
  title: 9 Automation and Scheduling changes in v0.11.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel
  setup warnings are now available as structured Doctor lint findings…]]'
- '[[Changes/Dify/2026-07-17-2-automation-and-scheduling-changes-in-1-16-0|2 Automation
  and Scheduling changes in 1.16.0]]'
- '[[Changes/Gemini CLI/2026-07-22-feat-caretaker-triage-implement-main-worker-execution-loop-and-egress-action-pub|feat(caretaker-triage):
  implement main worker execution loop and egress action publisher]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: automation-scheduling
title: 9 Automation and Scheduling changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Automation and Scheduling changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🧺 **Automations that file their chats away.** An automation can now be pointed at one of your folders, from the dialog, the editor or by asking the assistant, so each run lands there instead of loose in your chat list, and the folder is cleared automatically if it is later deleted. [Commit](https://github.com/open-webui/open-webui/commit/f798d05586a140f1a6b51f1e51b2b2a63d079d45), [Commit](https://github.com/open-webui/open-webui/commit/bab71ed08b5af6f4a8ff2daa02792baae9edab03), [Commit](https://github.com/open-webui/open-webui/commit/db5c092299471444c356216d5ef39b382ba1aa1e)

> 💾 **Import notes and automations.** Notes can now be brought in from text and markdown files, and automations can be exported and imported as files, so you can move them between instances. [Commit](https://github.com/open-webui/open-webui/commit/f8350360dfd60ff890b73fe2f39aaf20a52ad28b), [Commit](https://github.com/open-webui/open-webui/commit/2018546a7baeb853bb4d98e2fb2a092ef20aa431)

> 🕰️ **Faster automation scheduling.** Working out when an automation that repeats every few minutes or hours runs next is now near instant, instead of taking twenty seconds or more and slowing further each year. [Commit](https://github.com/open-webui/open-webui/commit/b3aead23da6cf8ebeedbd9fa3b97c7ac1a3f54ec), [#26954](https://github.com/open-webui/open-webui/issues/26954)

> 🚥 **Automation limits in chat.** Automations that the assistant creates or reschedules on your behalf now respect the same maximum count and minimum interval as the ones you set up yourself, instead of being able to exceed both. [#27523](https://github.com/open-webui/open-webui/pull/27523), [#27121](https://github.com/open-webui/open-webui/issues/27121)

> 🌙 **Date pickers in dark mode.** The calendar and clock icons on date and time fields are now visible in dark mode, across the calendar, automation schedules, account settings and analytics. [#27275](https://github.com/open-webui/open-webui/pull/27275), [#27274](https://github.com/open-webui/open-webui/issues/27274)

> 🗓️ **Automation dialog on narrow screens.** The buttons along the bottom of the automation dialog now sit on their own row on a phone, instead of the schedule and model pickers wrapping and pushing Cancel into the middle. [#27027](https://github.com/open-webui/open-webui/pull/27027)

> 🧭 **Sidebar access from the automation editor.** Opening an automation on a phone no longer hides the sidebar button, so you can move around without leaving the editor first.

> ⏰ **Recurring automation scheduling.** Automations that repeat every few minutes or hours now align to the clock and are no longer wrongly rejected as having no upcoming runs when the server clock is ahead of your timezone. [Commit](https://github.com/open-webui/open-webui/commit/b3aead23da6cf8ebeedbd9fa3b97c7ac1a3f54ec), [#26954](https://github.com/open-webui/open-webui/issues/26954)

> 🔐 **Administrators no longer reach other people's automations.** Viewing, editing, running and deleting an automation is now limited to the person who created it, so an administrator with a link to someone else's automation is refused rather than allowed through. [Commit](https://github.com/open-webui/open-webui/commit/f798d05586a140f1a6b51f1e51b2b2a63d079d45)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
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
## Nearby in Automation and Scheduling

- Earlier: 2026-07-22 · Gemini CLI · [[Changes/Gemini CLI/2026-07-22-feat-caretaker-triage-implement-main-worker-execution-loop-and-egress-action-pub|feat(caretaker-triage): implement main worker execution loop and egress action publisher]]
- Later: 2026-07-29 · OpenHands · [[Changes/OpenHands/2026-07-29-chore-bump-software-agent-sdk-to-1-38-0-and-automation-to-1-4-1-by-hieptl-in-htt|chore: bump software-agent-sdk to 1.38.0 and automation to 1.4.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-1897a4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-1897a4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->