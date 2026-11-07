---
card_id: openclaw-2026-09-23-35d035
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Mobile and Desktop: 16 changes in v2026.9.6
  — Production npm installs on macOS, Windows and Linux carry about 18 MiB less unused
  Bash…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1289
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 04dc32ae61bc2755220c0ffce7d1d3733a348526294e335cec3ab3d2dbe52475
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-35d035
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 16 Mobile and Desktop changes'
  evidence:
  - quote: Production npm installs on macOS, Windows and Linux carry about 18 MiB
      less unused Bash parser material while keeping the same command-parsing behavior.
      This is a reduction in installed files, with no configuration change needed.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: On mobile, progress stays collapsed by default across new messages and
      completion unless you open it. Completed work durations include the final model
      request when matching timing is available, and omit missing or mismatched timing
      instead of guessing.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Restart, update and diagnostic checks distinguish a Gateway that is still
      making startup progress from one that has failed, and local health checks recognize
      serving wildcard listeners on macOS. At the restart wait limit, exit code 2
      means still starting, not healthy; health and channels JSON may likewise exit
      0 with status=starting . Check openclaw gateway status --deep and inspect again
      before treating the service as ready. Existing wait budgets remain, and an older
      updater already running cannot inherit the new checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: On supported Node installations on macOS and Linux, SIGUSR1 now opens the
      debugger without restarting the Gateway. Change scripts that used it for restarts
      to SIGUSR2 , or use openclaw gateway restart , which retains handling for verified
      older running Gateways. The restart and supervision guide explains the signal
      change.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Normal logs now report when Slack fails to clear an accepted working status
      at the end of a turn, making that failure easier to diagnose. This exposes the
      cleanup problem without adding retries or repairing Slack Desktop's separate
      stale-indicator behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Android connection forms keep their labels visible after you type and put
      setup errors beside the relevant fields. Overview gives Chat a clearer entry
      point and makes connection states and destination rows easier to read, while
      saved credentials remain masked and replacing them still requires confirmation.
      Nearby Gateway lists also retain current addresses and availability when a service
      disappears or is rediscovered, without changing pairing or connection checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Sending a photo in native iOS chat no longer triggers the reported composer
      freeze, so you can send the attachment and continue typing without restarting
      the app. This repairs the send-time focus problem; keeping sent photos visible
      after history refresh remains separate work.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The Tauri app on macOS can reopen saved local or remote Gateways without
      the reported startup crash. If the launch environment prevents keychain access,
      its warning now gives appropriate recovery guidance, including reopening from
      Finder when relevant.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The bundled Mac worker can start with saved desktop-sharing preferences,
      including named profiles, and honors whether sharing is enabled or disabled.
      Signing in from an open embedded Dashboard can also restore protected images
      and files while keeping the same-account conversation. Update both the Mac app
      and Dashboard for that renewal; signing in through an ordinary browser tab does
      not renew the embedded session.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Hosted workers track unfinished commands through cancellation and node
      restarts, freeing occupied slots after cleanup is confirmed. Update the Gateway
      and the node hosts or Mac app together, and restart the updated hosts; older
      nodes may show Update required. Linux and macOS gain stronger cleanup, while
      Windows keeps a slot reserved when cleanup is uncertain. Let active workers
      finish before downgrading to an older version.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Claude CLI keeps follow-up tools and the final answer in the original turn
      when a foreground Bash command takes long enough to be moved into the background
      automatically. Commands intentionally started in the background still end the
      turn promptly and do not gain independent later delivery. Supported npm-installed
      wrappers now launch on Windows, long reasoning streams require less repeated
      parsing, and recovery timing stays within its existing budget when the system
      clock changes.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Persistent paired Mac, Windows, and Linux computers now offer desktop sharing
      by default, with native Mac and Tauri switches and connection status. Pairing
      approval and an authenticated local Screen Sharing or VNC service are still
      required, and the switch does not turn on that operating-system service. Explicit
      disables and Gateway denials remain respected. Some existing computers need
      approval again in Devices after updating. Tauri requires a local OpenClaw CLI,
      and closing it to the tray leaves sharing active.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Upgrade the host, inspect with openclaw doctor , then use openclaw doctor
      --fix during maintenance with no other OpenClaw producer running. On Linux and
      macOS, Doctor can reclaim eligible legacy captures only after a complete, fresh
      process check. Windows, recognized containers, and incomplete or ambiguous checks
      remain report-only. Live, changed, managed, foreign, and symlink-target content
      stays protected; age alone is not a reason to delete files, and reported sizes
      can overcount hardlinks.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Swift and Android tests reuse preparation and wait for observable readiness,
      while Apple catalog checks follow the current app text. Windows lifecycle fixtures
      retain their compiled files until cleanup completes.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Shared native clients gain interfaces and cross-language contract checks
      for continued development, alongside consolidated Apple Watch status formatting.
      The shared-client groundwork does not activate a new macOS sidecar.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Crabbox reports classified fetch failures without exposing raw private
      Git output and waits for cancellation cleanup. It can inspect and recover verified
      abandoned local staging, while keeping copies whose ownership or cleanup remains
      uncertain. Testbox validation stays in the selected checkout, restores targeted
      source uploads and accepts verified Microsoft OpenSSH installation locations
      on Windows. Stop and rewarm existing Testbox leases after preparation updates;
      support for live staging on filesystems without flushing does not permit recovery
      of unverified abandoned copies.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 16-mobile-and-desktop-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 16 Mobile and Desktop changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Cline/2026-09-22-rules-are-found-and-shown-consistently-the-rules-panel-listed-only-clinerules-an|Rules
  are found and shown consistently]]'
- '[[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11
  Mobile and Desktop changes in rust-v0.156.0]]'
- '[[Changes/Claude Code/2026-09-23-2-mobile-and-desktop-changes-in-v2-1-281|2 Mobile
  and Desktop changes in v2.1.281]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 16 Mobile and Desktop changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Mobile and Desktop changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Production npm installs on macOS, Windows and Linux carry about 18 MiB less unused Bash parser material while keeping the same command-parsing behavior. This is a reduction in installed files, with no configuration change needed.

> On mobile, progress stays collapsed by default across new messages and completion unless you open it. Completed work durations include the final model request when matching timing is available, and omit missing or mismatched timing instead of guessing.

> Restart, update and diagnostic checks distinguish a Gateway that is still making startup progress from one that has failed, and local health checks recognize serving wildcard listeners on macOS. At the restart wait limit, exit code 2 means still starting, not healthy; health and channels JSON may likewise exit 0 with status=starting . Check openclaw gateway status --deep and inspect again before treating the service as ready. Existing wait budgets remain, and an older updater already running cannot inherit the new checks.

> On supported Node installations on macOS and Linux, SIGUSR1 now opens the debugger without restarting the Gateway. Change scripts that used it for restarts to SIGUSR2 , or use openclaw gateway restart , which retains handling for verified older running Gateways. The restart and supervision guide explains the signal change.

> Normal logs now report when Slack fails to clear an accepted working status at the end of a turn, making that failure easier to diagnose. This exposes the cleanup problem without adding retries or repairing Slack Desktop's separate stale-indicator behavior.

> Android connection forms keep their labels visible after you type and put setup errors beside the relevant fields. Overview gives Chat a clearer entry point and makes connection states and destination rows easier to read, while saved credentials remain masked and replacing them still requires confirmation. Nearby Gateway lists also retain current addresses and availability when a service disappears or is rediscovered, without changing pairing or connection checks.

> Sending a photo in native iOS chat no longer triggers the reported composer freeze, so you can send the attachment and continue typing without restarting the app. This repairs the send-time focus problem; keeping sent photos visible after history refresh remains separate work.

> The Tauri app on macOS can reopen saved local or remote Gateways without the reported startup crash. If the launch environment prevents keychain access, its warning now gives appropriate recovery guidance, including reopening from Finder when relevant.

> The bundled Mac worker can start with saved desktop-sharing preferences, including named profiles, and honors whether sharing is enabled or disabled. Signing in from an open embedded Dashboard can also restore protected images and files while keeping the same-account conversation. Update both the Mac app and Dashboard for that renewal; signing in through an ordinary browser tab does not renew the embedded session.

> Hosted workers track unfinished commands through cancellation and node restarts, freeing occupied slots after cleanup is confirmed. Update the Gateway and the node hosts or Mac app together, and restart the updated hosts; older nodes may show Update required. Linux and macOS gain stronger cleanup, while Windows keeps a slot reserved when cleanup is uncertain. Let active workers finish before downgrading to an older version.

> Claude CLI keeps follow-up tools and the final answer in the original turn when a foreground Bash command takes long enough to be moved into the background automatically. Commands intentionally started in the background still end the turn promptly and do not gain independent later delivery. Supported npm-installed wrappers now launch on Windows, long reasoning streams require less repeated parsing, and recovery timing stays within its existing budget when the system clock changes.

> Persistent paired Mac, Windows, and Linux computers now offer desktop sharing by default, with native Mac and Tauri switches and connection status. Pairing approval and an authenticated local Screen Sharing or VNC service are still required, and the switch does not turn on that operating-system service. Explicit disables and Gateway denials remain respected. Some existing computers need approval again in Devices after updating. Tauri requires a local OpenClaw CLI, and closing it to the tray leaves sharing active.

> Upgrade the host, inspect with openclaw doctor , then use openclaw doctor --fix during maintenance with no other OpenClaw producer running. On Linux and macOS, Doctor can reclaim eligible legacy captures only after a complete, fresh process check. Windows, recognized containers, and incomplete or ambiguous checks remain report-only. Live, changed, managed, foreign, and symlink-target content stays protected; age alone is not a reason to delete files, and reported sizes can overcount hardlinks.

> Swift and Android tests reuse preparation and wait for observable readiness, while Apple catalog checks follow the current app text. Windows lifecycle fixtures retain their compiled files until cleanup completes.

> Shared native clients gain interfaces and cross-language contract checks for continued development, alongside consolidated Apple Watch status formatting. The shared-client groundwork does not activate a new macOS sidecar.

> Crabbox reports classified fetch failures without exposing raw private Git output and waits for cancellation cleanup. It can inspect and recover verified abandoned local staging, while keeping copies whose ownership or cleanup remains uncertain. Testbox validation stays in the selected checkout, restores targeted source uploads and accepts verified Microsoft OpenSSH installation locations on Windows. Stop and rewarm existing Testbox leases after preparation updates; support for live staging on filesystems without flushing does not permit recovery of unverified abandoned copies.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-23 · Claude Code · [[Changes/Claude Code/2026-09-23-2-mobile-and-desktop-changes-in-v2-1-281|2 Mobile and Desktop changes in v2.1.281]]
- Later: 2026-09-23 · OpenHands · [[Changes/OpenHands/2026-09-23-feat-desktop-universal-macos-dmg-with-per-arch-bundled-runtimes-by-harsh-batheja|feat(desktop): universal macOS DMG with per-arch bundled runtimes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-35d035&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-35d035%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->