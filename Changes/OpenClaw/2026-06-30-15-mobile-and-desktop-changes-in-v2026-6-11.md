---
card_id: openclaw-2026-06-30-3473d4
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Mobile and Desktop: 15 changes in v2026.6.11
  — Across Telegram , WhatsApp , Matrix , Google Chat , iMessage , Feishu , and Mattermost…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2788
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 035ef757a6e431221d172216f1afc7ddb451abf6960af93e23ca57d81f38a4a8
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-3473d4
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 15 Mobile and Desktop changes'
  evidence:
  - quote: Across Telegram , WhatsApp , Matrix , Google Chat , iMessage , Feishu ,
      and Mattermost , replies, commands, queued messages, and attachments are less
      likely to be dropped, duplicated, misrouted, or attached to the wrong conversation.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Previously allowed messages keep reaching named accounts after legacy
      multi-account channel upgrades, with inherited DM and group access rules preserved
      across Mattermost, Discord, Slack, Telegram, Signal, WhatsApp, iMessage, and
      IRC. #95550 Thanks @amknight.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'WhatsApp users can approve or deny prompts by reaction without the prompt
      staying stuck when WhatsApp identifies the same direct chat differently, while
      group approvals remain tied to the correct group and person. #95935 Thanks @mcaxtr.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'WhatsApp''s final answer now stays quoted to the follow-up message a user
      just sent when replying to an older OpenClaw message, instead of arriving unquoted
      or pointing back to the older bot reply. #96220 Thanks @mcaxtr.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Mobile operators with operator.approvals can now see and resolve chat-triggered
      exec approvals on the iOS device that started the request, including while the
      app is open, without relying only on push notifications. #95175 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'macOS users are less likely to see a false port-conflict failure when
      stopping or updating a managed gateway, because OpenClaw briefly waits for normal
      shutdown to release the port while still reporting conflicts that persist. #95886
      Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Android users can now open Health log and Skill rows in Settings for readable
      details, making it easier to troubleshoot gateway activity, check skill setup
      and status, and understand how to pair with an existing setup code. #95148 Thanks
      @tosko4.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Android users can now refresh and resolve gateway command approvals from
      the in-app Approvals screen, choosing Allow Once, Always, or Deny while connected.
      #95593 Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: iOS push relay setup failures are easier to pinpoint because registration
      diagnostics show where setup stopped while keeping sensitive push credentials
      out of logs. f2b8668 Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Additional Control UI , mobile, and desktop fixes improve display accuracy,
      accessibility, onboarding, and app behavior.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'New iOS users now reach OpenClaw''s welcome and onboarding before iOS
      asks for local-network access, while existing users still get the request when
      opening gateway setup or otherwise needing LAN gateway discovery. #96181 Thanks
      @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'macOS gateway operators now get a warning before reinstall, repair, or
      restart overwrites custom LaunchAgent wrapper behavior, while openclaw status
      distinguishes CLI-only missing-secret checks from the installed service. #90537
      Related #90518 . Thanks @turbotheturtle, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'On Windows, installer-created gateway tasks now run in the background
      without a console window that users could accidentally close and stop the gateway.
      #95480 Related #89231 . Thanks @cameronweller, @mikasa0818, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: On Windows, OpenClaw startup and TUI Codex handoff now find bun , codex
      , and other runtime binaries through the trusted system locator even when another
      where command appears earlier on PATH. 72b9bc7 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: On Windows, Crabbox commands launched through Node package shims now receive
      provider flags, shell commands, and special shell characters as entered instead
      of losing or reinterpreting them. 54d24cd Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-mobile-and-desktop-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 15 Mobile and Desktop changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile
  and Desktop changes in v0.10.0]]'
- '[[Changes/Gemini/2026-06-30-hand-off-the-heavy-lifting-to-gemini-spark-now-available-in-the-macos-app|Hand
  off the heavy lifting to Gemini Spark, now available in the macOS app]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-2-mobile-and-desktop-changes-in-v1-0-66|2
  Mobile and Desktop changes in v1.0.66]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 15 Mobile and Desktop changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Mobile and Desktop changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Across Telegram , WhatsApp , Matrix , Google Chat , iMessage , Feishu , and Mattermost , replies, commands, queued messages, and attachments are less likely to be dropped, duplicated, misrouted, or attached to the wrong conversation.

> Previously allowed messages keep reaching named accounts after legacy multi-account channel upgrades, with inherited DM and group access rules preserved across Mattermost, Discord, Slack, Telegram, Signal, WhatsApp, iMessage, and IRC. #95550 Thanks @amknight.

> WhatsApp users can approve or deny prompts by reaction without the prompt staying stuck when WhatsApp identifies the same direct chat differently, while group approvals remain tied to the correct group and person. #95935 Thanks @mcaxtr.

> WhatsApp's final answer now stays quoted to the follow-up message a user just sent when replying to an older OpenClaw message, instead of arriving unquoted or pointing back to the older bot reply. #96220 Thanks @mcaxtr.

> Mobile operators with operator.approvals can now see and resolve chat-triggered exec approvals on the iOS device that started the request, including while the app is open, without relying only on push notifications. #95175 Thanks @joshavant.

> macOS users are less likely to see a false port-conflict failure when stopping or updating a managed gateway, because OpenClaw briefly waits for normal shutdown to release the port while still reporting conflicts that persist. #95886 Thanks @fuller-stack-dev.

> Android users can now open Health log and Skill rows in Settings for readable details, making it easier to troubleshoot gateway activity, check skill setup and status, and understand how to pair with an existing setup code. #95148 Thanks @tosko4.

> Android users can now refresh and resolve gateway command approvals from the in-app Approvals screen, choosing Allow Once, Always, or Deny while connected. #95593 Thanks @solvely-colin.

> iOS push relay setup failures are easier to pinpoint because registration diagnostics show where setup stopped while keeping sensitive push credentials out of logs. f2b8668 Thanks @joshavant.

> Additional Control UI , mobile, and desktop fixes improve display accuracy, accessibility, onboarding, and app behavior.

> New iOS users now reach OpenClaw's welcome and onboarding before iOS asks for local-network access, while existing users still get the request when opening gateway setup or otherwise needing LAN gateway discovery. #96181 Thanks @joshavant.

> macOS gateway operators now get a warning before reinstall, repair, or restart overwrites custom LaunchAgent wrapper behavior, while openclaw status distinguishes CLI-only missing-secret checks from the installed service. #90537 Related #90518 . Thanks @turbotheturtle, @vincentkoc.

> On Windows, installer-created gateway tasks now run in the background without a console window that users could accidentally close and stop the gateway. #95480 Related #89231 . Thanks @cameronweller, @mikasa0818, @vincentkoc.

> On Windows, OpenClaw startup and TUI Codex handoff now find bun , codex , and other runtime binaries through the trusted system locator even when another where command appears earlier on PATH. 72b9bc7 Thanks @vincentkoc.

> On Windows, Crabbox commands launched through Node package shims now receive provider flags, shell commands, and special shell characters as entered instead of losing or reinterpreting them. 54d24cd Thanks @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-5-collaboration-changes-in-v2026-6-11|5 Collaboration changes in v2026.6.11]] · Collaboration
- [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Memory and Personalization
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-6-voice-and-audio-changes-in-v2026-6-11|6 Voice and Audio changes in v2026.6.11]] · Voice and Audio
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur|When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…]] · Pricing Model
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-2-mobile-and-desktop-changes-in-v1-0-66|2 Mobile and Desktop changes in v1.0.66]]
- Later: 2026-06-30 · OpenCode · [[Changes/OpenCode/2026-06-30-7-mobile-and-desktop-changes-in-v1-17-12|7 Mobile and Desktop changes in v1.17.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-3473d4&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-3473d4%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->