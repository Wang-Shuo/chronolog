---
card_id: codex-cli-2026-02-25-902b43
date: '2026-02-25'
description: 'Codex CLI · 2026-02-25 · Safety and Privacy: 9 changes in 0.105.0 —
  Approval controls are more flexible: Codex can now ask for extra sandbox permissions
  for a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1046
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9b79ba8b7539e1a14d07c03f52f71f08597f98c057c7f660ffa09d7e7aeb1741
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-25-902b43
  comparison: ''
  date: '2026-02-25'
  description: 'Codex CLI — 0.105.0: 9 Safety and Privacy changes'
  evidence:
  - quote: 'Approval controls are more flexible: Codex can now ask for extra sandbox
      permissions for a command, and you can auto-reject specific approval prompt
      types without turning approvals off entirely. (#11871, #12087)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: Added a public security policy with Bugcrowd reporting guidance. (#12193)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12096 Updated issue labeler script to include safety-check label @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12025 app-server support for Windows sandbox setup. @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12081 fix(linux-sandbox): mount /dev in bwrap sandbox @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12193 docs: add codex security policy @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11293 feat(linux-sandbox): implement proxy-only egress via TCP-UDS-TCP
      bridge @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12473 core: preserve constrained approval/sandbox policies in TurnContext
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12753 Surface skill permission profiles in zsh-fork exec approvals @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-105-0
  source_release: codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.105.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety
  and Privacy changes in v0.8.4]]'
- '[[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety
  and Privacy changes in v2.1.51]]'
- '[[Changes/OpenCode/2026-02-24-core-normalize-paths-at-permission-boundaries-on-windows|Core
  Normalize paths at permission boundaries on Windows]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.105.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.105.0

**Codex CLI** · 2026-02-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.105.0) · from [[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|0.105.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Approval controls are more flexible: Codex can now ask for extra sandbox permissions for a command, and you can auto-reject specific approval prompt types without turning approvals off entirely. (#11871, #12087)

> Added a public security policy with Bugcrowd reporting guidance. (#12193)

> #12096 Updated issue labeler script to include safety-check label @etraut-openai

> #12025 app-server support for Windows sandbox setup. @iceweasel-oai

> #12081 fix(linux-sandbox): mount /dev in bwrap sandbox @viyatb-oai

> #12193 docs: add codex security policy @viyatb-oai

> #11293 feat(linux-sandbox): implement proxy-only egress via TCP-UDS-TCP bridge @viyatb-oai

> #12473 core: preserve constrained approval/sandbox policies in TurnContext @bolinfest

> #12753 Surface skill permission profiles in zsh-fork exec approvals @celia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.105.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-25-13-apps-and-integrations-changes-in-rust-v0-105-0|13 Apps and Integrations changes in rust-v0.105.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-25-18-agent-mode-changes-in-rust-v0-105-0|18 Agent Mode changes in rust-v0.105.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-25-15-developer-workflow-changes-in-rust-v0-105-0|15 Developer Workflow changes in rust-v0.105.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-25-12028-remove-feature-flag-collaboration-modes-aibrahim-oai|♯12028 remove feature flag collaboration modes @aibrahim-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-25-9-memory-and-personalization-changes-in-rust-v0-105-0|9 Memory and Personalization changes in rust-v0.105.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-25-3-reliability-and-performance-changes-in-rust-v0-105-0|3 Reliability and Performance changes in rust-v0.105.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-25-you-can-now-dictate-prompts-by-holding-the-spacebar-to-record-and-transcribe-voi|Dictate prompts by holding the spacebar to record and transcribe voice input…]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-3-account-and-access-changes-in-rust-v0-105-0|3 Account and Access changes in rust-v0.105.0]] · Account and Access
- [[Changes/Codex CLI/2026-02-25-8-interface-experience-changes-in-rust-v0-105-0|8 Interface Experience changes in rust-v0.105.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-25-2-editor-experience-changes-in-rust-v0-105-0|2 Editor Experience changes in rust-v0.105.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-25-5-context-window-changes-in-rust-v0-105-0|5 Context Window changes in rust-v0.105.0]] · Context Window
- [[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model Support changes in rust-v0.105.0]] · Model Support
- [[Changes/Codex CLI/2026-02-25-2-mobile-and-desktop-changes-in-rust-v0-105-0|2 Mobile and Desktop changes in rust-v0.105.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-25-2-voice-and-audio-changes-in-rust-v0-105-0|2 Voice and Audio changes in rust-v0.105.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-156-other-changes-in-rust-v0-105-0|156 other changes in rust-v0.105.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-24 · OpenCode · [[Changes/OpenCode/2026-02-24-core-normalize-paths-at-permission-boundaries-on-windows|Core Normalize paths at permission boundaries on Windows]]
- Later: 2026-02-25 · Gemini CLI · [[Changes/Gemini CLI/2026-02-25-refactor-core-adopt-coretoolcallstatus-enum-for-type-safety-by-jerop-in-https-gi|refactor(core): adopt CoreToolCallStatus enum for type safety]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-25-902b43&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0.md%0ACard%20ID%3A%20codex-cli-2026-02-25-902b43%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.105.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->