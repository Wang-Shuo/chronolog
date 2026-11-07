---
card_id: openclaw-2026-09-30-a634d1
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Mobile and Desktop: 14 changes in v2026.9.7
  — The prerelease compiler now supports build hosts on macOS arm64/x64, Linux arm/arm64/x64…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2880
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2b5ca46c20f06e3b8f8a2f569749de9ee7e948beb71507e92d8025494dc61e1e
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-a634d1
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 14 Mobile and Desktop changes'
  evidence:
  - quote: The prerelease compiler now supports build hosts on macOS arm64/x64, Linux
      arm/arm64/x64, and Windows arm64/x64. BSD, AIX, SunOS, and other Linux architectures
      no longer have compiler packages, so check your build host before upgrading.
      This restriction concerns building OpenClaw, not running an installed copy.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Local macOS packaging restores the committed Swift dependency versions
      before preparing each build, avoiding dependency drift when reusing a build
      cache. If a later step changes a dependency, the error names the changed version.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Returning to a chat can reopen its existing desktop or live browser tab.
      Dashboard gallery navigation also keeps widget interactions when you return,
      though a browser reload still clears unsaved state. Self-contained HTML and
      SVG widgets can now use up to 10 MiB including their wrapper; registered-source
      widgets and Discord keep their smaller limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Phone layouts give conversation titles more room and keep the New Session
      message box within reach. Menus and composers adapt to the space your browser
      reports around the keyboard, as explained in the mobile layout guidance . Filter
      sheets also stay open when you tap their headings or padding.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: On macOS and Linux, Bun headless nodes running the fixed updater can prepare
      later automatic updates without Node or npm. Windows still requires npm. Bun
      release discovery and OpenClaw package downloads use public npm even when npm
      is configured with a private mirror. If your installation requires that mirror,
      disable nodeHost.autoUpdate.enabled and use your normal update process. Node-based
      services can also recover from a missing Node executable by selecting a supported
      replacement; custom wrappers need their own repair.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Authorized users can approve or deny OpenClaw changes in the chat where
      they requested them, using supported buttons or /approve . Existing approver
      rules still apply, and typing “yes” does not approve a change. Reaction approvals
      also work on iMessage, Signal, and WhatsApp prompts; forwarded Signal reactions
      remain opt-in.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The Android APK was skipped for this release, and official verification
      lists app version 2026.8.2. The Android items below describe changes in the
      tagged source.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Full Mac chat windows now use the web chat interface by default on compatible
      Gateways, including for existing Native users. Rich replies and conversation
      controls sit alongside the Mac sidebar, menus and Cmd-K search. Quick Chat and
      iOS keep their native interface. The Mac window also keeps it while native drafts
      or queued messages need attention, or if web chat cannot load.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Dashboards opened inside the Android or Mac app can use the app's existing
      device approval, avoiding a second approval prompt. The Linux/Tauri companion
      supports this for its remote Primary Gateway dashboard. Update both the app
      and the Gateway-hosted Control UI to use it. On Mac, the Primary dashboard also
      keeps that approval through refreshes and reconnects.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: On iOS, typing and your first sent message stay visible while the app finishes
      finding your agent. On iPad, resizing the window or opening the sidebar keeps
      your chat and unsent draft in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: If iOS setup reports a storage problem when switching Gateways, it keeps
      your setup code and existing connection. Fix the storage problem before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Android model search supports multiple words and small spelling mistakes
      in longer words. The Effort gauge follows your adjustments even with Fast mode
      on, shown by a separate bolt. To check token use and costs, open Chat actions
      → Context ; the usage ring has moved out of the writing area.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Linux fixes a Quick Chat widget crash on X11 and shows clearer update instructions.
      On opt-in Windows desktop-test builds, the updater keeps the app and downloaded
      update available if the installer fails to launch, so you can retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Terminals on Bun have separate requirements. Node-free terminals on macOS
      and Linux need a compatible Bun build; stock Bun 1.4.2 still needs Node. This
      update does not change the apps' Bun versions. Some Bun builds can also take
      about 30 seconds to close a desktop command that launched an app.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-mobile-and-desktop-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 14 Mobile and Desktop changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-29-suppressed-console-windows-flashing-on-windows-when-codex-launches-background-pr|Suppressed
  console windows flashing on Windows when Codex launches background…]]'
- '[[Changes/Windsurf/2026-09-29-devin-desktop|Devin Desktop]]'
- '[[Changes/Google Antigravity/2026-09-30-on-windows-and-linux-a-left-click-on-the-tray-icon-now-reopens-or-focuses-the-an|On
  Windows and Linux, a left-click on the tray icon now reopens or focuses…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 14 Mobile and Desktop changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Mobile and Desktop changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The prerelease compiler now supports build hosts on macOS arm64/x64, Linux arm/arm64/x64, and Windows arm64/x64. BSD, AIX, SunOS, and other Linux architectures no longer have compiler packages, so check your build host before upgrading. This restriction concerns building OpenClaw, not running an installed copy.

> Local macOS packaging restores the committed Swift dependency versions before preparing each build, avoiding dependency drift when reusing a build cache. If a later step changes a dependency, the error names the changed version.

> Returning to a chat can reopen its existing desktop or live browser tab. Dashboard gallery navigation also keeps widget interactions when you return, though a browser reload still clears unsaved state. Self-contained HTML and SVG widgets can now use up to 10 MiB including their wrapper; registered-source widgets and Discord keep their smaller limits.

> Phone layouts give conversation titles more room and keep the New Session message box within reach. Menus and composers adapt to the space your browser reports around the keyboard, as explained in the mobile layout guidance . Filter sheets also stay open when you tap their headings or padding.

> On macOS and Linux, Bun headless nodes running the fixed updater can prepare later automatic updates without Node or npm. Windows still requires npm. Bun release discovery and OpenClaw package downloads use public npm even when npm is configured with a private mirror. If your installation requires that mirror, disable nodeHost.autoUpdate.enabled and use your normal update process. Node-based services can also recover from a missing Node executable by selecting a supported replacement; custom wrappers need their own repair.

> Authorized users can approve or deny OpenClaw changes in the chat where they requested them, using supported buttons or /approve . Existing approver rules still apply, and typing “yes” does not approve a change. Reaction approvals also work on iMessage, Signal, and WhatsApp prompts; forwarded Signal reactions remain opt-in.

> The Android APK was skipped for this release, and official verification lists app version 2026.8.2. The Android items below describe changes in the tagged source.

> Full Mac chat windows now use the web chat interface by default on compatible Gateways, including for existing Native users. Rich replies and conversation controls sit alongside the Mac sidebar, menus and Cmd-K search. Quick Chat and iOS keep their native interface. The Mac window also keeps it while native drafts or queued messages need attention, or if web chat cannot load.

> Dashboards opened inside the Android or Mac app can use the app's existing device approval, avoiding a second approval prompt. The Linux/Tauri companion supports this for its remote Primary Gateway dashboard. Update both the app and the Gateway-hosted Control UI to use it. On Mac, the Primary dashboard also keeps that approval through refreshes and reconnects.

> On iOS, typing and your first sent message stay visible while the app finishes finding your agent. On iPad, resizing the window or opening the sidebar keeps your chat and unsent draft in place.

> If iOS setup reports a storage problem when switching Gateways, it keeps your setup code and existing connection. Fix the storage problem before retrying.

> Android model search supports multiple words and small spelling mistakes in longer words. The Effort gauge follows your adjustments even with Fast mode on, shown by a separate bolt. To check token use and costs, open Chat actions → Context ; the usage ring has moved out of the writing area.

> Linux fixes a Quick Chat widget crash on X11 and shows clearer update instructions. On opt-in Windows desktop-test builds, the updater keeps the app and downloaded update available if the installer fails to launch, so you can retry.

> Terminals on Bun have separate requirements. Node-free terminals on macOS and Linux need a compatible Bun build; stock Bun 1.4.2 still needs Node. This update does not change the apps' Bun versions. Some Bun builds can also take about 30 seconds to close a desktop command that launched an app.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-30 · Google Antigravity · [[Changes/Google Antigravity/2026-09-30-on-windows-and-linux-a-left-click-on-the-tray-icon-now-reopens-or-focuses-the-an|On Windows and Linux, a left-click on the tray icon now reopens or focuses…]]
- Later: 2026-09-30 · OpenCode · [[Changes/OpenCode/2026-09-30-2-mobile-and-desktop-changes-in-v1-18-34|2 Mobile and Desktop changes in v1.18.34]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-a634d1&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-a634d1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->