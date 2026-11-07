---
card_id: open-webui-2026-06-29-bf5148
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Automation and Scheduling: 6 changes in v0.10.0
  — \U0001F4CB **Clone automations.** Automations now have a Clone option in their
  menu, so you…"
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 909
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5dfdadc2ea09e009001820c757a6acc156f40d903cfca997f5267aa5aeabc146
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-bf5148
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 6 Automation and Scheduling changes'
  evidence:
  - quote: "\U0001F4CB **Clone automations.** Automations now have a Clone option
      in their menu, so you can duplicate one as a starting point. [#25790](https://github.com/open-webui/open-webui/pull/25790)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Faster URL safety checks.** The safety check on fetched URLs now resolves
      addresses off the main loop, so it no longer blocks other work. [#25825](https://github.com/open-webui/open-webui/pull/25825)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Non-blocking uploads and link fetches.** Hashing uploaded files and
      fetching URLs now run off the main loop, so large uploads and link previews
      don't hold up other requests. [#25822](https://github.com/open-webui/open-webui/pull/25822)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **More blocking work moved off the main loop.** Additional blocking operations
      in audio, pipelines, and plugin handling now run in worker threads, keeping
      the server responsive under load. [#26381](https://github.com/open-webui/open-webui/pull/26381)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⏰ **Scheduled automations stop for deactivated accounts.** Scheduled automations
      now re-check the owner's account status and permissions before each run, so
      they stop when an account is deactivated or has automations access revoked.
      [#26047](https://github.com/open-webui/open-webui/pull/26047)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⏰ **Scheduled automations with session-auth tools work.** Automations that
      use session-authenticated tools or terminals now authenticate correctly when
      running on a schedule, instead of failing. [Commit](https://github.com/open-webui/open-webui/commit/5b1c42e81a3ef3ad5ce5852dbf84020cb5e2498c),
      [#26247](https://github.com/open-webui/open-webui/pull/26247), [#26137](https://github.com/open-webui/open-webui/issues/26137)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-automation-and-scheduling-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: automation-scheduling
  title: 6 Automation and Scheduling changes in v0.10.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-23-add-loop-alias-for-the-every-command|Add
  /loop alias for the /every command]]'
- '[[Changes/GitHub Copilot CLI/2026-06-24-handle-wakeup-misfires-with-a-graceful-message-when-no-self-paced-schedule-is-ac|Handle
  wakeup misfires with a graceful message when no self-paced schedule is active]]'
- '[[Changes/Dify/2026-06-25-2-automation-and-scheduling-changes-in-1-15-0|2 Automation
  and Scheduling changes in 1.15.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: automation-scheduling
title: 6 Automation and Scheduling changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Automation and Scheduling changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📋 **Clone automations.** Automations now have a Clone option in their menu, so you can duplicate one as a starting point. [#25790](https://github.com/open-webui/open-webui/pull/25790)

> ⚡ **Faster URL safety checks.** The safety check on fetched URLs now resolves addresses off the main loop, so it no longer blocks other work. [#25825](https://github.com/open-webui/open-webui/pull/25825)

> ⚡ **Non-blocking uploads and link fetches.** Hashing uploaded files and fetching URLs now run off the main loop, so large uploads and link previews don't hold up other requests. [#25822](https://github.com/open-webui/open-webui/pull/25822)

> ⚡ **More blocking work moved off the main loop.** Additional blocking operations in audio, pipelines, and plugin handling now run in worker threads, keeping the server responsive under load. [#26381](https://github.com/open-webui/open-webui/pull/26381)

> ⏰ **Scheduled automations stop for deactivated accounts.** Scheduled automations now re-check the owner's account status and permissions before each run, so they stop when an account is deactivated or has automations access revoked. [#26047](https://github.com/open-webui/open-webui/pull/26047)

> ⏰ **Scheduled automations with session-auth tools work.** Automations that use session-authenticated tools or terminals now authenticate correctly when running on a schedule, instead of failing. [Commit](https://github.com/open-webui/open-webui/commit/5b1c42e81a3ef3ad5ce5852dbf84020cb5e2498c), [#26247](https://github.com/open-webui/open-webui/pull/26247), [#26137](https://github.com/open-webui/open-webui/issues/26137)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer Workflow changes in v0.10.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-06-25 · Dify · [[Changes/Dify/2026-06-25-2-automation-and-scheduling-changes-in-1-15-0|2 Automation and Scheduling changes in 1.15.0]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr auto now starts a self-paced loop that fixes one thing per run and paces itself…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-bf5148&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-bf5148%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->