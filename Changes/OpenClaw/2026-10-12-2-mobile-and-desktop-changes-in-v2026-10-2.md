---
card_id: openclaw-2026-10-12-e77c3d
date: '2026-10-12'
description: 'OpenClaw · 2026-10-12 · Mobile and Desktop: 2 changes in v2026.10.2
  — HTTPS commands through the secret proxy. HTTPS commands using the secret egress
  proxy no…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2892
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3c7ef1f3b12694ed7e8090866a5821f3d2826e0ee378ed304cf70c2dd51e463c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-12-e77c3d
  comparison: ''
  date: '2026-10-12'
  description: 'OpenClaw — v2026.10.2: 2 Mobile and Desktop changes'
  evidence:
  - quote: HTTPS commands through the secret proxy. HTTPS commands using the secret
      egress proxy no longer fail strict certificate checks with newly generated certificates,
      including affected Python commands on macOS. After updating, restart the Gateway
      and start a new command. Keep certificate verification enabled. Retained older
      debug-proxy certificates are unchanged and can still fail strict checks. f1cd78c
      , thanks to @steipete , @vortexopenclaw and @A1fred-AI .
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Quoted Windows commands. Commands on Windows nodes preserve multiword
      arguments, URLs and executable paths with spaces through the supported command
      wrapper. #158160 , thanks to @Dimitri-lcht , @igs-rogenlo , @steipete and @kassol
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 2-mobile-and-desktop-changes-in-v2026-10-2
  source_release: openclaw-2026-10-12-v2026-10-2-9abf70fc
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 2 Mobile and Desktop changes in v2026.10.2
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile
  and Desktop changes in v0.12.0]]'
- '[[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile
  and Desktop changes in v2026.10.1]]'
- '[[Changes/Google Antigravity/2026-10-12-2-mobile-and-desktop-changes-in-hub-v2-23-0-permissions-picker|2
  Mobile and Desktop changes in HUB v2.23.0 — Permissions picker…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|openclaw-2026-10-12-v2026-10-2-9abf70fc]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 2 Mobile and Desktop changes in v2026.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Mobile and Desktop changes in v2026.10.2

**OpenClaw** · 2026-10-12 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.2) · from [[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|v2026.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> HTTPS commands through the secret proxy. HTTPS commands using the secret egress proxy no longer fail strict certificate checks with newly generated certificates, including affected Python commands on macOS. After updating, restart the Gateway and start a new command. Keep certificate verification enabled. Retained older debug-proxy certificates are unchanged and can still fail strict checks. f1cd78c , thanks to @steipete , @vortexopenclaw and @A1fred-AI .

> Quoted Windows commands. Commands on Windows nodes preserve multiword arguments, URLs and executable paths with spaces through the supported command wrapper. #158160 , thanks to @Dimitri-lcht , @igs-rogenlo , @steipete and @kassol .

Source: https://docs.openclaw.ai/releases/2026.10.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-12-5-apps-and-integrations-changes-in-v2026-10-2|5 Apps and Integrations changes in v2026.10.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-12-4-memory-and-personalization-changes-in-v2026-10-2|4 Memory and Personalization changes in v2026.10.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-12-older-session-history-doctor-can-continue-repairing-leftover-session-files-while|Older session history]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-12-2-pricing-model-changes-in-v2026-10-2|2 Pricing Model changes in v2026.10.2]] · Pricing Model
- [[Changes/OpenClaw/2026-10-12-9-model-support-changes-in-v2026-10-2|9 Model Support changes in v2026.10.2]] · Model Support
- [[Changes/OpenClaw/2026-10-12-4-context-window-changes-in-v2026-10-2|4 Context Window changes in v2026.10.2]] · Context Window
- [[Changes/OpenClaw/2026-10-12-dictation-holding-the-microphone-and-releasing-it-no-longer-stops-recording-prem|Dictation. Holding the microphone and releasing it no longer stops recording prematurely]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-12-managed-browser-tabs-at-the-shared-tab-limit-locally-managed-browser-cleanup-fav|Managed browser tabs]] · Editor Experience
- [[Changes/OpenClaw/2026-10-12-2-developer-workflow-changes-in-v2026-10-2|2 Developer Workflow changes in v2026.10.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-12-home-notifications-creating-many-chats-no-longer-fills-home-s-notification-queue|Home notifications]] · Collaboration
- [[Changes/OpenClaw/2026-10-12-manually-started-jobs-an-accepted-automation-can-keep-using-its-allowed-tools-af|Manually started jobs]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-12-5-agent-mode-changes-in-v2026-10-2|5 Agent Mode changes in v2026.10.2]] · Agent Mode
- [[Changes/OpenClaw/2026-10-12-plugin-approval-waits-affected-plugin-tools-can-wait-for-your-approval-for-the-e|Plugin approval waits]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-12-summaries-before-completion-replies-when-a-long-conversation-needs-a-summary-ope|Summaries before completion replies]] · Interface Experience
- [[Changes/OpenClaw/2026-10-12-23-other-changes-in-v2026-10-2|23 other changes in v2026.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-10-12 · Google Antigravity · [[Changes/Google Antigravity/2026-10-12-2-mobile-and-desktop-changes-in-hub-v2-23-0-permissions-picker|2 Mobile and Desktop changes in HUB v2.23.0 — Permissions picker…]]
- Later: 2026-10-12 · Windsurf · [[Changes/Windsurf/2026-10-12-devin-desktop|Devin Desktop]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-12-e77c3d&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-12-2-mobile-and-desktop-changes-in-v2026-10-2.md%0ACard%20ID%3A%20openclaw-2026-10-12-e77c3d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->