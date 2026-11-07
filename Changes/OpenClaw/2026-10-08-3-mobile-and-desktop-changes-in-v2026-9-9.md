---
card_id: openclaw-2026-10-08-8caecd
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Mobile and Desktop: 3 changes in v2026.9.9 —
  Windows workspaces. Creating an empty workspace on Windows no longer fails because
  of the…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2888
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b7d849b125fff403f95823a697ba171fd8ace2844234682906ff31613a63d7e4
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-8caecd
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 3 Mobile and Desktop changes'
  evidence:
  - quote: 'Windows workspaces. Creating an empty workspace on Windows no longer fails
      because of the way OpenClaw calls Git. You can choose New workspace and start
      a conversation without changing your global Git settings. First install Git
      for Windows using the native Windows setup guidance . Folders nested too deeply
      can still hit a separate Git limit. #164202 by @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Failed-update recovery. Supported updaters can recover a compatible OpenClaw
      installation after a failed update while preserving data written during the
      attempt. Returning to 2026.9.8 also keeps later updates possible. An older updater
      already running cannot gain these safeguards. On macOS and Linux, restart stays
      blocked until Doctor processes are confirmed stopped. Follow the repair steps
      and rollback guidance . #164497 , #164724 by @RomneyDa , with original recovery
      work by @steipete and reports from @DasX and @jarvisnextgeneration20-lang .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Commands that would not exit. Fixed a Node problem that could leave commands
      running after they had printed all their output. The workaround also covers
      the Gateway service, hook relays and macOS node worker. Some commands may take
      longer, and advanced overrides can bypass the fix; see the Node compatibility
      guide . #163788 by @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-mobile-and-desktop-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 3 Mobile and Desktop changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/Ollama/2026-10-07-manifest-avoid-symlinks-on-windows-by-dhiltgen-in-https-github-com-ollama-ollama|manifest:
  avoid symlinks on Windows]]'
- '[[Changes/Claude Code/2026-10-08-changed-the-claude-apps-gateway-to-start-with-a-warning-and-serve-a-desktop-poli|Changed
  the Claude apps gateway to start with a warning and serve a desktop policy…]]'
- '[[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384
  Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 3 Mobile and Desktop changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Mobile and Desktop changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows workspaces. Creating an empty workspace on Windows no longer fails because of the way OpenClaw calls Git. You can choose New workspace and start a conversation without changing your global Git settings. First install Git for Windows using the native Windows setup guidance . Folders nested too deeply can still hit a separate Git limit. #164202 by @steipete .

> Failed-update recovery. Supported updaters can recover a compatible OpenClaw installation after a failed update while preserving data written during the attempt. Returning to 2026.9.8 also keeps later updates possible. An older updater already running cannot gain these safeguards. On macOS and Linux, restart stays blocked until Doctor processes are confirmed stopped. Follow the repair steps and rollback guidance . #164497 , #164724 by @RomneyDa , with original recovery work by @steipete and reports from @DasX and @jarvisnextgeneration20-lang .

> Commands that would not exit. Fixed a Node problem that could leave commands running after they had printed all their output. The workaround also covers the Gateway service, hook relays and macOS node worker. Some commands may take longer, and advanced overrides can bypass the fix; see the Node compatibility guide . #163788 by @steipete .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the|Model retries and context]] · Context Window
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-10-08 · Codex CLI · [[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384 Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]]
- Later: 2026-10-09 · Raycast · [[Changes/Raycast/2026-10-09-clipboard-history-added-an-option-to-save-universal-clipboard-items-from-your-ip|Clipboard History : Added an option to save Universal Clipboard items…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-8caecd&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-8caecd%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->