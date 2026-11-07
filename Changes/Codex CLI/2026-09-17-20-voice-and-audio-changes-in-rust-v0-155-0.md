---
card_id: codex-cli-2026-09-17-bebf4c
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Voice and Audio: 20 changes in 0.155.0 — Added
  experimental `/voice` conversations with live transcripts and microphone controls
  on…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2992
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d424693a1ee2c80cb67d0a9d36f477ae086704cdaea3118d2f558e9829f9a53
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-bebf4c
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 20 Voice and Audio changes'
  evidence:
  - quote: 'Added experimental `/voice` conversations with live transcripts and microphone
      controls on supported builds, enabled through `/experimental`. (#43581, #43651,
      #44331)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43581 Add live WebRTC voice conversations to the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43645 Expand TUI regression coverage for realtime voice conversations
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43651 Add voice mute shortcut and recording activity indicators @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43656 Animate live voice transcripts with split-flap tiles @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43676 Style spoken prompts and link workspace files in voice transcripts
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43683 Move voice controls into a dedicated composer strip @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43690 Make the voice mute shortcut configurable in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43695 Stabilize realtime voice meter sampling across redraws @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43699 Preserve split-flap animation state when voice transcripts scroll
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43704 Disable clock synchronization in the voice audio sink @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43934 Track voice session lifecycle metrics in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43983 Bundle signed voice resources in macOS releases @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44025 Refresh workspace lockfile before building macOS voice releases
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44062 Fix voice runtime release builds and packaging @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44070 Reject empty audio payloads in data URLs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44080 Make staged macOS voice runtimes writable before packaging @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44101 Handle empty voice arguments in macOS release packaging @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44198 Preserve voice indicator styles during composer sparkle effects
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44331 Expose voice conversations in experimental features @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 20-voice-and-audio-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: voice
  title: 20 Voice and Audio changes in rust-v0.155.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-09-14-elevenagents-bdb11f|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-09-14-elevenagents-dab1d0|ElevenAgents]]'
- '[[Changes/Synthesia/2026-09-16-create-up-to-20-seconds-of-b-roll-with-natively-synced-audio-and-drop-polished-c|Generate
  B-roll with Flux 3 from Black Forest Labs]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: voice
title: 20 Voice and Audio changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Voice and Audio changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added experimental `/voice` conversations with live transcripts and microphone controls on supported builds, enabled through `/experimental`. (#43581, #43651, #44331)

> #43581 Add live WebRTC voice conversations to the TUI @copyberry

> #43645 Expand TUI regression coverage for realtime voice conversations @copyberry

> #43651 Add voice mute shortcut and recording activity indicators @copyberry

> #43656 Animate live voice transcripts with split-flap tiles @copyberry

> #43676 Style spoken prompts and link workspace files in voice transcripts @copyberry

> #43683 Move voice controls into a dedicated composer strip @copyberry

> #43690 Make the voice mute shortcut configurable in the TUI @copyberry

> #43695 Stabilize realtime voice meter sampling across redraws @copyberry

> #43699 Preserve split-flap animation state when voice transcripts scroll @copyberry

> #43704 Disable clock synchronization in the voice audio sink @copyberry

> #43934 Track voice session lifecycle metrics in the TUI @copyberry

> #43983 Bundle signed voice resources in macOS releases @copyberry

> #44025 Refresh workspace lockfile before building macOS voice releases @copyberry

> #44062 Fix voice runtime release builds and packaging @copyberry

> #44070 Reject empty audio payloads in data URLs @copyberry

> #44080 Make staged macOS voice runtimes writable before packaging @copyberry

> #44101 Handle empty voice arguments in macOS release packaging @copyberry

> #44198 Preserve voice indicator styles during composer sparkle effects @copyberry

> #44331 Expose voice conversations in experimental features @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.155.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953 Preserve per-image generation IDs in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-17-43846-include-completed-commentary-in-the-copy-picker-copyberry|♯43846 Include completed commentary in the /copy picker @copyberry]] · Interface Experience
- [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]] · Model Support
- [[Changes/Codex CLI/2026-09-17-2-editor-experience-changes-in-rust-v0-155-0|2 Editor Experience changes in rust-v0.155.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-17-15-developer-workflow-changes-in-rust-v0-155-0|15 Developer Workflow changes in rust-v0.155.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-17-2-mobile-and-desktop-changes-in-rust-v0-155-0|2 Mobile and Desktop changes in rust-v0.155.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]] · Context Window
- [[Changes/Codex CLI/2026-09-17-44354-extract-shared-footer-hint-wrapping-in-the-tui-copyberry|♯44354 Extract shared footer hint wrapping in the TUI @copyberry]] · Collaboration
- [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-17-6-account-and-access-changes-in-rust-v0-155-0|6 Account and Access changes in rust-v0.155.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0|24 Apps and Integrations changes in rust-v0.155.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-17-96-other-changes-in-rust-v0-155-0|96 other changes in rust-v0.155.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-16 · Synthesia · [[Changes/Synthesia/2026-09-16-create-up-to-20-seconds-of-b-roll-with-natively-synced-audio-and-drop-polished-c|Generate B-roll with Flux 3 from Black Forest Labs]]
- Later: 2026-09-17 · Descript · [[Changes/Descript/2026-09-17-how-to-find-it|How to find it]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-bebf4c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-20-voice-and-audio-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-bebf4c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->