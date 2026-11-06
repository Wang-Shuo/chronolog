---
card_id: codex-cli-2026-08-20-98ea29
date: '2026-08-20'
description: 'Codex CLI · 2026-08-20 · Mobile and Desktop: 7 changes in 0.149.0 —
  `codex doctor` now diagnoses endpoint protection, network/proxy failures, desktop
  app…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1255
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e895753dc49e24db8c880f10b63cc92908f03bf46ac22bdb08848244527ea16a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-20-98ea29
  comparison: ''
  date: '2026-08-20'
  description: 'Codex CLI — 0.149.0: 7 Mobile and Desktop changes'
  evidence:
  - quote: '`codex doctor` now diagnoses endpoint protection, network/proxy failures,
      desktop app state, and update connectivity. (#38827, #38918, #39060, #39074)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38947 Stop loading legacy managed config on Windows @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39060 Add desktop app diagnostics to `codex doctor` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39074 Add desktop update diagnostics to `codex doctor` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39599 Protect macOS Seatbelt writable root anchors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39623 Prevent protected-path rename bypasses in macOS Seatbelt @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39656 Advertise the Desktop app in graphical Linux sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-mobile-and-desktop-changes-in-rust-v0-149-0
  source_release: codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944
  source_type: github_releases
  theme: mobile-desktop
  title: 7 Mobile and Desktop changes in rust-v0.149.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-19-added-notify-when-idle-to-cross-session-sendmessage-ask-another-claude-code-sess|Added
  notify_when_idle to cross-session SendMessage]]'
- '[[Changes/ChatGPT/2026-08-20-keep-pinned-chats-in-sync-pinned-chats-now-stay-in-sync-between-the-chatgpt-desk|Keep
  pinned chats in sync]]'
- '[[Changes/Claude Code/2026-08-20-improved-startup-bare-claude-starts-sooner-on-macos|Improved
  startup: bare claude starts sooner on macOS]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944]]'
source_type: github_releases
theme: mobile-desktop
title: 7 Mobile and Desktop changes in rust-v0.149.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Mobile and Desktop changes in rust-v0.149.0

**Codex CLI** · 2026-08-20 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.149.0) · from [[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|0.149.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `codex doctor` now diagnoses endpoint protection, network/proxy failures, desktop app state, and update connectivity. (#38827, #38918, #39060, #39074)

> #38947 Stop loading legacy managed config on Windows @copyberry

> #39060 Add desktop app diagnostics to `codex doctor` @copyberry

> #39074 Add desktop update diagnostics to `codex doctor` @copyberry

> #39599 Protect macOS Seatbelt writable root anchors @copyberry

> #39623 Prevent protected-path rename bypasses in macOS Seatbelt @copyberry

> #39656 Advertise the Desktop app in graphical Linux sessions @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.149.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-20-2-reliability-and-performance-changes-in-rust-v0-149-0|2 Reliability and Performance changes in rust-v0.149.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model Support changes in rust-v0.149.0]] · Model Support
- [[Changes/Codex CLI/2026-08-20-18-developer-workflow-changes-in-rust-v0-149-0|18 Developer Workflow changes in rust-v0.149.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2 Memory and Personalization changes in rust-v0.149.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-20-39045-add-managed-gates-for-in-app-chat-and-dictation-copyberry|♯39045 Add managed gates for in-app chat and dictation @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0|18 Safety and Privacy changes in rust-v0.149.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context Window changes in rust-v0.149.0]] · Context Window
- [[Changes/Codex CLI/2026-08-20-2-collaboration-changes-in-rust-v0-149-0|2 Collaboration changes in rust-v0.149.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-20-5-editor-experience-changes-in-rust-v0-149-0|5 Editor Experience changes in rust-v0.149.0]] · Editor Experience
- [[Changes/Codex CLI/2026-08-20-3-interface-experience-changes-in-rust-v0-149-0|3 Interface Experience changes in rust-v0.149.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-20-33-apps-and-integrations-changes-in-rust-v0-149-0|33 Apps and Integrations changes in rust-v0.149.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-20-8-account-and-access-changes-in-rust-v0-149-0|8 Account and Access changes in rust-v0.149.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-20-39072-persist-generated-images-through-turn-executors-copyberry|♯39072 Persist generated images through turn executors @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-20-39283-document-secure-devcontainer-dns-exfiltration-risk-copyberry|♯39283 Document secure devcontainer DNS exfiltration risk @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-20-39006-emit-api-key-turn-cost-telemetry-from-app-server-copyberry|♯39006 Emit API-key turn cost telemetry from app-server @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-20-125-other-changes-in-rust-v0-149-0|125 other changes in rust-v0.149.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-08-20 · Claude Code · [[Changes/Claude Code/2026-08-20-improved-startup-bare-claude-starts-sooner-on-macos|Improved startup: bare claude starts sooner on macOS]]
- Later: 2026-08-21 · Claude Code · [[Changes/Claude Code/2026-08-21-remote-sessions-images-uploaded-from-mobile-now-include-their-saved-file-path-so|Remote sessions: images uploaded from mobile now include their saved file path…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-20-98ea29&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-20-7-mobile-and-desktop-changes-in-rust-v0-149-0.md%0ACard%20ID%3A%20codex-cli-2026-08-20-98ea29%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.149.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->