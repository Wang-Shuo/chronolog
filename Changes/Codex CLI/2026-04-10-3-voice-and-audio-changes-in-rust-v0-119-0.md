---
card_id: codex-cli-2026-04-10-6d16f1
date: '2026-04-10'
description: 'Codex CLI · 2026-04-10 · Voice and Audio: 3 changes in 0.119.0 — Realtime
  voice sessions now default to the v2 WebRTC path, with configurable transport, voice…'
diffusion:
  first_in_tracked: '[[Changes/Aider/2023-08-11-voice-to-code-https-aider-chat-docs-voice-html-support-which-allows-you-to-code|Voice-to-code((source
    link) support, which allows you…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 973
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 841904161f22d8a183f3b5cf854b917d20b7d55178e44839d0f937972ce88595
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-10-6d16f1
  comparison: ''
  date: '2026-04-10'
  description: 'Codex CLI — 0.119.0: 3 Voice and Audio changes'
  evidence:
  - quote: 'Realtime voice sessions now default to the v2 WebRTC path, with configurable
      transport, voice selection, native TUI media support, and app-server coverage
      for the new flow (#16960, #17057, #17058, #17093, #17097, #17145, #17165, #17176,
      #17183, #17188).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16467 tui: remove the voice-input crate feature @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17176 Add realtime voice selection @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-voice-and-audio-changes-in-rust-v0-119-0
  source_release: codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1
  source_type: github_releases
  theme: voice
  title: 3 Voice and Audio changes in rust-v0.119.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-26-slash-commands-unavailable-for-the-current-auth-setup-voice-mobile-chrome-upgrad|Slash
  commands unavailable for the current auth setup…]]'
- '[[Changes/Codex CLI/2026-03-26-15579-increase-voice-space-hold-timeout-to-1s-aibrahim-oai|♯15579
  Increase voice space hold timeout to 1s @aibrahim-oai]]'
- '[[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114
  Remove TUI voice transcription feature @etraut-openai]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1]]'
source_type: github_releases
theme: voice
title: 3 Voice and Audio changes in rust-v0.119.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Voice and Audio changes in rust-v0.119.0

**Codex CLI** · 2026-04-10 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.119.0) · from [[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Realtime voice sessions now default to the v2 WebRTC path, with configurable transport, voice selection, native TUI media support, and app-server coverage for the new flow (#16960, #17057, #17058, #17093, #17097, #17145, #17165, #17176, #17183, #17188).

> #16467 tui: remove the voice-input crate feature @bolinfest

> #17176 Add realtime voice selection @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.119.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Context Window
- [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-10-28-developer-workflow-changes-in-rust-v0-119-0|28 Developer Workflow changes in rust-v0.119.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-10-the-readme-now-uses-the-current-chatgpt-business-plan-name-16348|The README now uses the current ChatGPT Business plan name (♯16348)]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-10-17256-app-server-use-shared-receivers-for-app-server-message-processors-euroeles|♯17256 app-server: Use shared receivers for app-server message processors @euroelessar]] · Collaboration
- [[Changes/Codex CLI/2026-04-10-10-interface-experience-changes-in-rust-v0-119-0|10 Interface Experience changes in rust-v0.119.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-10-16202-fix-paste-driven-bottom-pane-completion-teardown-etraut-openai|♯16202 Fix paste-driven bottom pane completion teardown @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-10-2-reliability-and-performance-changes-in-rust-v0-119-0|2 Reliability and Performance changes in rust-v0.119.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Model Support
- [[Changes/Codex CLI/2026-04-10-6-mobile-and-desktop-changes-in-rust-v0-119-0|6 Mobile and Desktop changes in rust-v0.119.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-10-187-other-changes-in-rust-v0-119-0|187 other changes in rust-v0.119.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-03-31 · Codex CLI · [[Changes/Codex CLI/2026-03-31-16114-remove-tui-voice-transcription-feature-etraut-openai|♯16114 Remove TUI voice transcription feature @etraut-openai]]
- Later: 2026-04-13 · Cursor · [[Changes/Cursor/2026-04-13-prompt-buttons-now-stay-in-place-while-voice-input-is-processing|Prompt buttons now stay in place while voice input is processing]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-08-11 · Aider · [[Changes/Aider/2023-08-11-voice-to-code-https-aider-chat-docs-voice-html-support-which-allows-you-to-code|Voice-to-code((source link) support, which allows you…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-10-6d16f1&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-10-3-voice-and-audio-changes-in-rust-v0-119-0.md%0ACard%20ID%3A%20codex-cli-2026-04-10-6d16f1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.119.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->