---
card_id: openclaw-2026-09-11-315279
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Mobile and Desktop: 16 changes in v2026.9.4
  — A slim message navigator on the left lets you preview a message before jumping
  to it, so…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2861
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ed9e91e16a8fcd7a9b6908b625a0d509410d85e52b224134f0891128ffc0a776
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-315279
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 16 Mobile and Desktop changes'
  evidence:
  - quote: A slim message navigator on the left lets you preview a message before
      jumping to it, so you can find a particular answer without scrolling through
      the whole conversation. In shared chats, previews also show who wrote the message
      when that information is available. It appears on desktop when there is enough
      room and covers the messages already loaded.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: For Windows installations using OpenClaw’s standard launcher, stopping
      the scheduled Gateway task now stops the work it started too, allowing a fresh
      start without a leftover copy getting in the way. Early startup failures also
      reach the log. Custom executable wrappers or extra command-shell layers can
      still prevent startup. Slow Windows service checks get another chance during
      updates, but a check that keeps hanging can make the wait much longer; if the
      service cannot be checked, the update stops before replacing the app.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you use a custom label at the start of your Claw’s WhatsApp replies,
      it no longer gets added to messages coming from other people. Your outgoing
      labels still work, and incoming messages keep what the sender wrote.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: The Android app helps you keep your place while reading, see what your
      Claw has done, and reply from notifications. There are also clearer ways to
      reconnect the mobile apps, fixes for Mac setup, and changes that keep a sleeping
      Linux desktop from interrupting OpenClaw on another computer.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: The Android app keeps your place while a reply arrives or you resize the
      window. Read earlier messages without being pulled away, then use Jump to latest
      to catch up. You can also open tool details to see what your Claw did, while
      dashboard chats tuck completed steps away and leave the answer visible.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Android waits for your selected files to finish loading before enabling
      Send, so your message cannot go out with its caption but without the attachment.
      If you cancel a file or it fails to load, the caption stays in place for you
      to keep working on.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When Android or iPhone cannot reach the computer running OpenClaw, the
      app now explains the problem and offers Retry. iPhone retries the connection
      you were setting up, and connections that appear to use Tailscale show relevant
      setup help. Android may need a moment to finish closing the previous connection
      before trying again.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: The iPhone app now makes clear how many conversations are showing and how
      many there are in total, including in its translated messages. If some have
      not loaded yet, use Refresh to load the rest.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Putting your Linux desktop to sleep no longer tells OpenClaw on another
      computer to pause, including when you connect over SSH. Saved SSH connections
      also use their configured port. If you keep a password or token in a separate
      file or environment setting, reconnecting preserves that setup so later launches
      can read the updated secret. Settings overwritten by an older version still
      need to be restored manually.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Opening Desktop from a chat now takes you to the computer running that
      chat, and the view stays connected while you type in another pane alongside
      it. Desktop support must be enabled, and you start by watching until you choose
      Take control.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: To paste text from your own computer, choose Take control, open Keyboard,
      and paste there once the connection is ready. Paste shortcuts used directly
      on the desktop view are sent to the remote computer. If someone else takes control,
      the notice now shows their signed-in name or user ID when available.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: You can choose a cloud computer’s operating system for a profile or an
      individual session when your provider offers it. Native Windows runs Windows
      commands, while WSL2 gives you a Linux environment on Windows. Mac workers on
      AWS require a Dedicated Host and On-Demand capacity; desktop access and reusable
      worker images remain Linux-only. The operating-system guide covers availability,
      with separate setup requirements for native Windows .
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Provider availability governs which cloud choices you can use. Conceptual
      illustration, not a screenshot. Desktop access and reusable worker images remain
      Linux-only in this release.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Supported cloud computers can also keep their files, installed tools, and
      desktop through an OpenClaw update . A message that has not started can continue
      once the worker is updated, but work already underway is not automatically repeated.
      The computer must support the update and reconnect; this cannot recover a machine
      lost by the provider.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: On Linux, affected SSH commands can finish instead of being stopped too
      early. Commands on macOS and Linux also avoid a false cleanup error after successful
      work. Restart OpenClaw if you updated with --no-restart to get that cleanup
      fix.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Release tools make interrupted publishing easier to investigate and recover
      from. Checks for older releases match the features those versions contain, while
      mobile release jobs get fixes for build preparation and troubleshooting. The
      checks that read older releases directly from Git require Git 2.45 or newer.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 16-mobile-and-desktop-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 16 Mobile and Desktop changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Windsurf/2026-09-10-introducing-fusion-in-devin-desktop-and-devin-cli-https-exafunction-github-io-pu|!Introducing
  Fusion in Devin Desktop and Devin…]]'
- '[[Changes/Windsurf/2026-09-10-devin-desktop|Devin Desktop]]'
- '[[Changes/Claude Code/2026-09-11-changed-skills-synced-from-claude-ai-in-cloud-sessions-to-be-named-anthropic-ski|Changed
  skills synced from claude.ai in cloud sessions to be named…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 16 Mobile and Desktop changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Mobile and Desktop changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> A slim message navigator on the left lets you preview a message before jumping to it, so you can find a particular answer without scrolling through the whole conversation. In shared chats, previews also show who wrote the message when that information is available. It appears on desktop when there is enough room and covers the messages already loaded.

> For Windows installations using OpenClaw’s standard launcher, stopping the scheduled Gateway task now stops the work it started too, allowing a fresh start without a leftover copy getting in the way. Early startup failures also reach the log. Custom executable wrappers or extra command-shell layers can still prevent startup. Slow Windows service checks get another chance during updates, but a check that keeps hanging can make the wait much longer; if the service cannot be checked, the update stops before replacing the app.

> If you use a custom label at the start of your Claw’s WhatsApp replies, it no longer gets added to messages coming from other people. Your outgoing labels still work, and incoming messages keep what the sender wrote.

> The Android app helps you keep your place while reading, see what your Claw has done, and reply from notifications. There are also clearer ways to reconnect the mobile apps, fixes for Mac setup, and changes that keep a sleeping Linux desktop from interrupting OpenClaw on another computer.

> The Android app keeps your place while a reply arrives or you resize the window. Read earlier messages without being pulled away, then use Jump to latest to catch up. You can also open tool details to see what your Claw did, while dashboard chats tuck completed steps away and leave the answer visible.

> Android waits for your selected files to finish loading before enabling Send, so your message cannot go out with its caption but without the attachment. If you cancel a file or it fails to load, the caption stays in place for you to keep working on.

> When Android or iPhone cannot reach the computer running OpenClaw, the app now explains the problem and offers Retry. iPhone retries the connection you were setting up, and connections that appear to use Tailscale show relevant setup help. Android may need a moment to finish closing the previous connection before trying again.

> The iPhone app now makes clear how many conversations are showing and how many there are in total, including in its translated messages. If some have not loaded yet, use Refresh to load the rest.

> Putting your Linux desktop to sleep no longer tells OpenClaw on another computer to pause, including when you connect over SSH. Saved SSH connections also use their configured port. If you keep a password or token in a separate file or environment setting, reconnecting preserves that setup so later launches can read the updated secret. Settings overwritten by an older version still need to be restored manually.

> Opening Desktop from a chat now takes you to the computer running that chat, and the view stays connected while you type in another pane alongside it. Desktop support must be enabled, and you start by watching until you choose Take control.

> To paste text from your own computer, choose Take control, open Keyboard, and paste there once the connection is ready. Paste shortcuts used directly on the desktop view are sent to the remote computer. If someone else takes control, the notice now shows their signed-in name or user ID when available.

> You can choose a cloud computer’s operating system for a profile or an individual session when your provider offers it. Native Windows runs Windows commands, while WSL2 gives you a Linux environment on Windows. Mac workers on AWS require a Dedicated Host and On-Demand capacity; desktop access and reusable worker images remain Linux-only. The operating-system guide covers availability, with separate setup requirements for native Windows .

> Provider availability governs which cloud choices you can use. Conceptual illustration, not a screenshot. Desktop access and reusable worker images remain Linux-only in this release.

> Supported cloud computers can also keep their files, installed tools, and desktop through an OpenClaw update . A message that has not started can continue once the worker is updated, but work already underway is not automatically repeated. The computer must support the update and reconnect; this cannot recover a machine lost by the provider.

> On Linux, affected SSH commands can finish instead of being stopped too early. Commands on macOS and Linux also avoid a false cleanup error after successful work. Restart OpenClaw if you updated with --no-restart to get that cleanup fix.

> Release tools make interrupted publishing easier to investigate and recover from. Checks for older releases match the features those versions contain, while mobile release jobs get fixes for build preparation and troubleshooting. The checks that read older releases directly from Git require Git 2.45 or newer.

Source: https://docs.openclaw.ai/releases/2026.9.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-11-messages-arriving-while-openclaw-is-paused-now-wait-until-it-is-ready-again-and|Messages arriving while OpenClaw is paused now wait until it is ready again…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-11-images-you-send-stay-visible-while-the-conversation-updates-and-scrolling-back-t|Images you send stay visible while the conversation updates, and scrolling back…]] · Files and Data
- [[Changes/OpenClaw/2026-09-11-7-automation-and-scheduling-changes-in-v2026-9-4|7 Automation and Scheduling changes in v2026.9.4]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-11-with-diagnostic-recording-enabled-openrouter-can-return-finished-music-or-a-usag|With diagnostic recording enabled, OpenRouter can return finished music…]] · Music Generation
- [[Changes/OpenClaw/2026-09-11-18-developer-workflow-changes-in-v2026-9-4|18 Developer Workflow changes in v2026.9.4]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-11-2-reliability-and-performance-changes-in-v2026-9-4|2 Reliability and Performance changes in v2026.9.4]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-11-the-bundled-video-frames-skill-and-its-helper-script-have-been-removed-if-you-us|The bundled video-frames skill and its helper script have been removed]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-11-5-interface-experience-changes-in-v2026-9-4|5 Interface Experience changes in v2026.9.4]] · Interface Experience
- [[Changes/OpenClaw/2026-09-11-14-memory-and-personalization-changes-in-v2026-9-4|14 Memory and Personalization changes in v2026.9.4]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-11-you-can-now-answer-your-claw-s-questions-and-enter-secrets-from-the-terminal-wit|Answer your Claw’s questions and enter secrets from the terminal, with clearer…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-11-2-image-generation-changes-in-v2026-9-4|2 Image Generation changes in v2026.9.4]] · Image Generation
- [[Changes/OpenClaw/2026-09-11-3-pricing-model-changes-in-v2026-9-4|3 Pricing Model changes in v2026.9.4]] · Pricing Model
- [[Changes/OpenClaw/2026-09-11-you-can-now-reach-the-official-app-store-listing-straight-from-the-iphone-setup|Reach the official App Store listing straight from the iPhone setup guide]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-5-editor-experience-changes-in-v2026-9-4|5 Editor Experience changes in v2026.9.4]] · Editor Experience
- [[Changes/OpenClaw/2026-09-11-you-can-now-choose-deepgram-flux-to-turn-incoming-voice-notes-into-text-your-cla|Choose Deepgram Flux to turn incoming voice notes into text your Claw can use…]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-8-voice-and-audio-changes-in-v2026-9-4|8 Voice and Audio changes in v2026.9.4]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-12-safety-and-privacy-changes-in-v2026-9-4|12 Safety and Privacy changes in v2026.9.4]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-11-22-apps-and-integrations-changes-in-v2026-9-4|22 Apps and Integrations changes in v2026.9.4]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-20-model-support-changes-in-v2026-9-4|20 Model Support changes in v2026.9.4]] · Model Support
- [[Changes/OpenClaw/2026-09-11-14-account-and-access-changes-in-v2026-9-4|14 Account and Access changes in v2026.9.4]] · Account and Access
- [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an|Search installed and available plugins together, browse by purpose, and keep…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-3-search-and-browsing-changes-in-v2026-9-4|3 Search and Browsing changes in v2026.9.4]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-11-you-can-now-enable-desktop-access-for-azure-cloud-workers-whether-openclaw-manag|Enable desktop access for Azure cloud workers , whether OpenClaw manages them…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-3-collaboration-changes-in-v2026-9-4|3 Collaboration changes in v2026.9.4]] · Collaboration
- [[Changes/OpenClaw/2026-09-11-25-agent-mode-changes-in-v2026-9-4|25 Agent Mode changes in v2026.9.4]] · Agent Mode
- [[Changes/OpenClaw/2026-09-11-2-context-window-changes-in-v2026-9-4|2 Context Window changes in v2026.9.4]] · Context Window
- [[Changes/OpenClaw/2026-09-11-56-other-changes-in-v2026-9-4|56 other changes in v2026.9.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-11 · Claude Code · [[Changes/Claude Code/2026-09-11-changed-skills-synced-from-claude-ai-in-cloud-sessions-to-be-named-anthropic-ski|Changed skills synced from claude.ai in cloud sessions to be named…]]
- Later: 2026-09-11 · Raycast · [[Changes/Raycast/2026-09-11-window-management-added-minimize-on-this-display-a-per-monitor-show-desktop-that|Window Management : Added Minimize on This Display , a per-monitor Show Desktop…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-315279&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-16-mobile-and-desktop-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-315279%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->