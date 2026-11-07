---
card_id: openclaw-2026-09-01-5208c3
date: '2026-09-01'
description: 'OpenClaw · 2026-09-01 · Mobile and Desktop: 3 changes in v2026.8.2 —
  Installation and first-run setup now do a better job of preserving the system and
  model…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2851
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d3977c5ea0d125143353cb5ce9b802dc0418f1fee80c990da52fc8c015937a90
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-01-5208c3
  comparison: ''
  date: '2026-09-01'
  description: 'OpenClaw — v2026.8.2: 3 Mobile and Desktop changes'
  evidence:
  - quote: Installation and first-run setup now do a better job of preserving the
      system and model choices people already made. Linux and macOS recovery paths
      fail more clearly, guided setup keeps the selected agent and model through reconnects,
      and required runtime plugins can be reviewed, installed, and verified without
      sending people to Terminal.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: Installation now follows the path each system actually began with. Fedora
      and other affected RPM-based Linux systems can keep their distro-owned Node
      packages while OpenClaw selects a managed runtime that meets its SQLite requirements,
      and the shell installer once again exposes the npm errors it needs to recover
      from supported stale launchers and install directories. On macOS, Install and
      Relaunch stops after one failed relocation retry and points to the Applications
      copy instead of looping. Linux Gateway installation also refuses an unsafe sudo-to-root
      setup before it writes root-owned configuration or credentials, without changing
      genuine root installs or ordinary sudo lifecycle commands.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  - quote: On supported macOS and Linux extension builds, a paired Chrome extension
      can wake an authenticated local relay even when the Gateway is not running,
      and the Gateway can join that relay later without taking the browser session
      away from other authenticated clients. This is not yet established for Chrome
      Web Store v2.2.0, Windows still requires manual relay setup, and commands through
      the browser CLI still need a running Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-mobile-and-desktop-changes-in-v2026-8-2
  source_release: openclaw-2026-09-01-v2026-8-2-cca64187
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 3 Mobile and Desktop changes in v2026.8.2
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-08-31-installation-and-onboarding-a-clearer-path-from-download-to-a-first-useful-conve|Installation
  and Onboarding - A clearer path from download to a first useful…]]'
- '[[Changes/Qoder/2026-08-31-improved-the-reliability-of-installation-and-updates-on-windows|Improved
  the reliability of installation and updates on Windows]]'
- '[[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed
  --add-dir, /add-dir, and additionalDirectories to refuse network paths…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|openclaw-2026-09-01-v2026-8-2-cca64187]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 3 Mobile and Desktop changes in v2026.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Mobile and Desktop changes in v2026.8.2

**OpenClaw** · 2026-09-01 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.8.2) · from [[Releases/OpenClaw/openclaw-2026-09-01-v2026-8-2-cca64187|v2026.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Installation and first-run setup now do a better job of preserving the system and model choices people already made. Linux and macOS recovery paths fail more clearly, guided setup keeps the selected agent and model through reconnects, and required runtime plugins can be reviewed, installed, and verified without sending people to Terminal.

> Installation now follows the path each system actually began with. Fedora and other affected RPM-based Linux systems can keep their distro-owned Node packages while OpenClaw selects a managed runtime that meets its SQLite requirements, and the shell installer once again exposes the npm errors it needs to recover from supported stale launchers and install directories. On macOS, Install and Relaunch stops after one failed relocation retry and points to the Applications copy instead of looping. Linux Gateway installation also refuses an unsafe sudo-to-root setup before it writes root-owned configuration or credentials, without changing genuine root installs or ordinary sudo lifecycle commands.

> On supported macOS and Linux extension builds, a paired Chrome extension can wake an authenticated local relay even when the Gateway is not running, and the Gateway can join that relay later without taking the browser session away from other authenticated clients. This is not yet established for Chrome Web Store v2.2.0, Windows still requires manual relay setup, and commands through the browser CLI still need a running Gateway.

Source: https://docs.openclaw.ai/releases/2026.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-01-4-model-support-changes-in-v2026-8-2|4 Model Support changes in v2026.8.2]] · Model Support
- [[Changes/OpenClaw/2026-09-01-11-agent-mode-changes-in-v2026-8-2|11 Agent Mode changes in v2026.8.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-01-9-voice-and-audio-changes-in-v2026-8-2|9 Voice and Audio changes in v2026.8.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-01-3-context-window-changes-in-v2026-8-2|3 Context Window changes in v2026.8.2]] · Context Window
- [[Changes/OpenClaw/2026-09-01-4-collaboration-changes-in-v2026-8-2|4 Collaboration changes in v2026.8.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-01-5-editor-experience-changes-in-v2026-8-2|5 Editor Experience changes in v2026.8.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-01-another-382-changes-in-v2026-8-2-primarily-affect-the-people-who-build-test-docu|Another 382 changes in v2026.8.2 primarily affect the people who build, test…]] · Files and Data
- [[Changes/OpenClaw/2026-09-01-usage-and-status-views-now-carry-cumulative-output-token-totals-through-tool-cal|Usage and status views now carry cumulative output-token totals through tool calls…]] · Pricing Model
- [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-01-9-apps-and-integrations-changes-in-v2026-8-2|9 Apps and Integrations changes in v2026.8.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-01-3-interface-experience-changes-in-v2026-8-2|3 Interface Experience changes in v2026.8.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account and Access changes in v2026.8.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-01-importing-or-returning-to-a-large-retained-history-also-requires-less-local-work|Importing or returning to a large retained history also requires less local work…]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-01-20-other-changes-in-v2026-8-2|20 other changes in v2026.8.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh|Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…]]
- Later: 2026-09-02 · Lovable · [[Changes/Lovable/2026-09-02-download-the-mobile-app-from-your-settings|Download the mobile app from your settings]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-01-5208c3&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-01-3-mobile-and-desktop-changes-in-v2026-8-2.md%0ACard%20ID%3A%20openclaw-2026-09-01-5208c3%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->