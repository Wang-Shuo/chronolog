---
card_id: openclaw-2026-09-05-9c0dca
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Mobile and Desktop: 10 changes in v2026.9.2
  — You can adjust how long OpenClaw waits to combine a burst of messages without…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2855
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6772cefd2c7eff91d6b8e678b37dfc3853814db5a25ea3b880bf75749c23db6e
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-9c0dca
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 10 Mobile and Desktop changes'
  evidence:
  - quote: You can adjust how long OpenClaw waits to combine a burst of messages without
      reconnecting Discord, Feishu, iMessage, Mattermost, Microsoft Teams, Signal,
      Slack, Telegram, or WhatsApp. New work uses the saved delay, while a setting
      change alone leaves an already pending batch on its existing schedule. Acknowledgement-reaction
      scope also applies to new turns without reconnecting the supported channels,
      and work already in progress keeps the policy it started with.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Tlon summary requests refresh their history after an account restarts,
      and long IRC replies retain literal code and link destinations across messages.
      WhatsApp now delivers the final failure explanation instead of discarding it
      with intermediate error noise. For a confirmed iMessage helper stall, OpenClaw
      attempts bounded recovery for later actions, which can relaunch Messages.app
      and delay the original error by up to 30 seconds; the failed action is still
      reported and is never automatically resent.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Update both apps, then use iPhone Settings → Apple Watch → Message Delivery
      to inspect replies or a Delivery uncertain warning. Check the original conversation
      before resending uncertain work. Older unsent messages that lack enough delivery
      information appear as Needs review, and the original 48-hour deadline still
      applies to new deliveries and their saved replies.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When you want to reuse part of a reply, Select Text opens an iOS selection
      sheet so you can copy a passage without taking the whole message. Code blocks
      gain a raw-code copy button on both iOS and Mac, tall Mermaid previews keep
      their first and last nodes reachable, and native Swarm progress responds to
      settings changes without reconnecting or bringing back an older enabled state.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Android task progress now sits in its own attached panel above the message
      composer, expanding upward while the editor and its controls stay in place.
      Progress cards show labeled bars alongside their text and links, and the Effort
      and Permissions sheets keep their choices reachable on smaller screens. Policy
      default and Default model have distinct labels, so checking permissions is less
      easily confused with resetting a model choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Android Stop, Forget, and reconnect now finish against the connection you
      selected, preventing pending secondary connections or old credential writes
      from reviving a connection you retired. Changing focus also preserves a handshake
      that is already underway. Disconnect shows Offline while retaining pairing;
      forgetting a Gateway removes its local saved connection, but does not revoke
      pairing on the remote Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: In the active iOS app, other enabled Gateways can stay connected while
      you use the focused one, including through temporary discovery gaps. With Background
      App Refresh enabled, the iPhone can also request opportunities to update its
      last-seen status and attempt a reconnect without a push relay. iOS controls
      that background schedule , and may suspend connections when the app is no longer
      active.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: These phone readings include processor count rather than CPU load. iOS
      omits disk usage, Android storage appears only when it can be sampled, and suspension
      or a lost connection can pause fresh readings.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: You can choose Original, Heritage, Clawmark, Origami, Pincer, or Open C
      in Settings → General → Dock icon , with light and dark previews side by side
      and the selection saved for each OpenClaw profile. Custom designs change the
      Dock icon while the app is running; Finder and the Dock after quitting continue
      to use Original. On macOS 26 and later, Original follows the system's Icon &
      widget style setting.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Desktop work now stays with the machine you selected through approval,
      reconnects, and taking control, while computer actions account for the screenshot
      the model actually sees. Browser connections also get clearer startup failures
      and more careful cleanup, so returning to a task is less likely to mean sorting
      out a stuck launch button or a tab that another session is still using.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-mobile-and-desktop-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 10 Mobile and Desktop changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-03-42068-https-github-com-openai-codex-pull-42068-detect-standalone-installs-from-t|♯42068((source
  link) Detect standalone installs…]]'
- '[[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile
  and Desktop changes in v2026.9.1]]'
- '[[Changes/OpenCode/2026-09-04-desktop-increase-the-open-in-app-icon-size-for-better-visibility|Desktop
  Increase the open-in app icon size for better visibility]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 10 Mobile and Desktop changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Mobile and Desktop changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> You can adjust how long OpenClaw waits to combine a burst of messages without reconnecting Discord, Feishu, iMessage, Mattermost, Microsoft Teams, Signal, Slack, Telegram, or WhatsApp. New work uses the saved delay, while a setting change alone leaves an already pending batch on its existing schedule. Acknowledgement-reaction scope also applies to new turns without reconnecting the supported channels, and work already in progress keeps the policy it started with.

> Tlon summary requests refresh their history after an account restarts, and long IRC replies retain literal code and link destinations across messages. WhatsApp now delivers the final failure explanation instead of discarding it with intermediate error noise. For a confirmed iMessage helper stall, OpenClaw attempts bounded recovery for later actions, which can relaunch Messages.app and delay the original error by up to 30 seconds; the failed action is still reported and is never automatically resent.

> Update both apps, then use iPhone Settings → Apple Watch → Message Delivery to inspect replies or a Delivery uncertain warning. Check the original conversation before resending uncertain work. Older unsent messages that lack enough delivery information appear as Needs review, and the original 48-hour deadline still applies to new deliveries and their saved replies.

> When you want to reuse part of a reply, Select Text opens an iOS selection sheet so you can copy a passage without taking the whole message. Code blocks gain a raw-code copy button on both iOS and Mac, tall Mermaid previews keep their first and last nodes reachable, and native Swarm progress responds to settings changes without reconnecting or bringing back an older enabled state.

> Android task progress now sits in its own attached panel above the message composer, expanding upward while the editor and its controls stay in place. Progress cards show labeled bars alongside their text and links, and the Effort and Permissions sheets keep their choices reachable on smaller screens. Policy default and Default model have distinct labels, so checking permissions is less easily confused with resetting a model choice.

> Android Stop, Forget, and reconnect now finish against the connection you selected, preventing pending secondary connections or old credential writes from reviving a connection you retired. Changing focus also preserves a handshake that is already underway. Disconnect shows Offline while retaining pairing; forgetting a Gateway removes its local saved connection, but does not revoke pairing on the remote Gateway.

> In the active iOS app, other enabled Gateways can stay connected while you use the focused one, including through temporary discovery gaps. With Background App Refresh enabled, the iPhone can also request opportunities to update its last-seen status and attempt a reconnect without a push relay. iOS controls that background schedule , and may suspend connections when the app is no longer active.

> These phone readings include processor count rather than CPU load. iOS omits disk usage, Android storage appears only when it can be sampled, and suspension or a lost connection can pause fresh readings.

> You can choose Original, Heritage, Clawmark, Origami, Pincer, or Open C in Settings → General → Dock icon , with light and dark previews side by side and the selection saved for each OpenClaw profile. Custom designs change the Dock icon while the app is running; Finder and the Dock after quitting continue to use Original. On macOS 26 and later, Original follows the system's Icon & widget style setting.

> Desktop work now stays with the machine you selected through approval, reconnects, and taking control, while computer actions account for the screenshot the model actually sees. Browser connections also get clearer startup failures and more careful cleanup, so returning to a task is less likely to mean sorting out a stuck launch button or a tab that another session is still using.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-04 · OpenCode · [[Changes/OpenCode/2026-09-04-desktop-increase-the-open-in-app-icon-size-for-better-visibility|Desktop Increase the open-in app icon size for better visibility]]
- Later: 2026-09-05 · Qoder · [[Changes/Qoder/2026-09-05-installer-better-process-detection-and-install-recovery-on-windows|Installer: Better process detection and install recovery on Windows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-9c0dca&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-9c0dca%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->