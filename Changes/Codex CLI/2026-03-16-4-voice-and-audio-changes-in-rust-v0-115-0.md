---
card_id: codex-cli-2026-03-16-446e69
date: '2026-03-16'
description: 'Codex CLI · 2026-03-16 · Voice and Audio: 4 changes in 0.115.0 — Realtime
  websocket sessions gained a dedicated transcription mode, plus v2 handoff support…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2
    Voice and Audio changes in 0.3.7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 980
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e493a084a0146d8f5cbbc1278fe79328dd7ae65cf655fc772ceaa651420754b9
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-16-446e69
  comparison: ''
  date: '2026-03-16'
  description: 'Codex CLI — 0.115.0: 4 Voice and Audio changes'
  evidence:
  - quote: 'Realtime websocket sessions gained a dedicated transcription mode, plus
      v2 handoff support through the `codex` tool, with a unified `[realtime]` session
      config. (#14554, #14556, #14606)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14556 Add realtime transcription mode for websocket sessions @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14635 Fix realtime transcription session.update tools payload @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14636 Use parser-specific realtime voice enum @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-voice-and-audio-changes-in-rust-v0-115-0
  source_release: codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db
  source_type: github_releases
  theme: voice
  title: 4 Voice and Audio changes in rust-v0.115.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-10-improved-voice-input-transcription-accuracy-for-repo-names-and-common-dev-terms|Improved
  voice input transcription accuracy for repo names and common dev terms…]]'
- '[[Changes/Claude Code/2026-03-11-improved-voice-mode-to-automatically-retry-transient-connection-failures-during|Improved
  voice mode to automatically retry transient connection failures during…]]'
- '[[Changes/Claude Code/2026-03-14-improved-voice-to-show-your-dictation-language-on-enable-and-warn-when-your-lang|Improved
  /voice to show your dictation language on enable and warn…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db]]'
source_type: github_releases
theme: voice
title: 4 Voice and Audio changes in rust-v0.115.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Voice and Audio changes in rust-v0.115.0

**Codex CLI** · 2026-03-16 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.115.0) · from [[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|0.115.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Realtime websocket sessions gained a dedicated transcription mode, plus v2 handoff support through the `codex` tool, with a unified `[realtime]` session config. (#14554, #14556, #14606)

> #14556 Add realtime transcription mode for websocket sessions @aibrahim-oai

> #14635 Fix realtime transcription session.update tools payload @aibrahim-oai

> #14636 Use parser-specific realtime voice enum @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.115.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0|17 Apps and Integrations changes in rust-v0.115.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]] · Context Window
- [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-16-2-mobile-and-desktop-changes-in-rust-v0-115-0|2 Mobile and Desktop changes in rust-v0.115.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-16-14493-memories-focus-write-prompts-on-user-preferences-andi-oai|♯14493 memories: focus write prompts on user preferences @andi-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0|9 Safety and Privacy changes in rust-v0.115.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-16-5-model-support-changes-in-rust-v0-115-0|5 Model Support changes in rust-v0.115.0]] · Model Support
- [[Changes/Codex CLI/2026-03-16-2-account-and-access-changes-in-rust-v0-115-0|2 Account and Access changes in rust-v0.115.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-16-2-developer-workflow-changes-in-rust-v0-115-0|2 Developer Workflow changes in rust-v0.115.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-16-14410-make-collab-model-metadata-accurate-on-completion-aibrahim-oai|♯14410 Make collab model metadata accurate on completion @aibrahim-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-16-70-other-changes-in-rust-v0-115-0|70 other changes in rust-v0.115.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-improved-voice-to-show-your-dictation-language-on-enable-and-warn-when-your-lang|Improved /voice to show your dictation language on enable and warn…]]
- Later: 2026-03-16 · ElevenLabs · [[Changes/ElevenLabs/2026-03-16-packages|Packages]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-10 · Dify · [[Changes/Dify/2023-07-10-2-voice-and-audio-changes-in-0-3-7|2 Voice and Audio changes in 0.3.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-16-446e69&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-16-4-voice-and-audio-changes-in-rust-v0-115-0.md%0ACard%20ID%3A%20codex-cli-2026-03-16-446e69%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.115.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->