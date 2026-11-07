---
card_id: codex-cli-2026-09-09-6d6ee1
date: '2026-09-09'
description: 'Codex CLI · 2026-09-09 · Voice and Audio: 20 changes in 0.154.0 — #42204
  Add macOS voice runtime projection @copyberry'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2984
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 16e8a0926bb5449d9c42ae88d929a2f00b8a45e870ee5176dedb50ab9657396d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-09-6d6ee1
  comparison: ''
  date: '2026-09-09'
  description: 'Codex CLI — 0.154.0: 20 Voice and Audio changes'
  evidence:
  - quote: '#42204 Add macOS voice runtime projection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42208 Add GNU Linux voice runtime preparation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42209 Add Windows voice runtime preparation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42332 Package prepared runtimes with the voice host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42404 Read voice helper frames independently of pipe chunks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42631 Initialize the packaged GStreamer runtime in the voice host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42676 Add WebRTC negotiation to the voice host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43079 Add opt-in local audio devices to the voice helper @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43090 Send processed microphone audio over RTP in voice-host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43099 Add receipt-verified native voice SDK export @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43102 Include GIO in voice SDKs and native runtimes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43109 Add explicit toolchain inputs for native voice builds @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43111 Add a Bazel target for native voice dependencies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43114 Add Bazel preparation for native voice runtimes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43117 Link Unix Bazel bindings against the prepared voice runtime @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43121 Require a prepared runtime when assembling voice helper packages
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43125 Add explicit Windows tool selection for native voice builds @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43144 Add Windows MSVC Bazel targets for native voice libraries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43244 Add bounded GStreamer playback components to the voice host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43248 Connect voice-host RTP audio to speaker playback @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 20-voice-and-audio-changes-in-rust-v0-154-0
  source_release: codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1
  source_type: github_releases
  theme: voice
  title: 20 Voice and Audio changes in rust-v0.154.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice
  and Audio changes in v2026.9.2]]'
- '[[Changes/ElevenLabs/2026-09-07-workspaces|Workspaces]]'
- '[[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and
  Audio changes in v2026.9.3]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1]]'
source_type: github_releases
theme: voice
title: 20 Voice and Audio changes in rust-v0.154.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Voice and Audio changes in rust-v0.154.0

**Codex CLI** · 2026-09-09 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.154.0) · from [[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #42204 Add macOS voice runtime projection @copyberry

> #42208 Add GNU Linux voice runtime preparation @copyberry

> #42209 Add Windows voice runtime preparation @copyberry

> #42332 Package prepared runtimes with the voice host @copyberry

> #42404 Read voice helper frames independently of pipe chunks @copyberry

> #42631 Initialize the packaged GStreamer runtime in the voice host @copyberry

> #42676 Add WebRTC negotiation to the voice host @copyberry

> #43079 Add opt-in local audio devices to the voice helper @copyberry

> #43090 Send processed microphone audio over RTP in voice-host @copyberry

> #43099 Add receipt-verified native voice SDK export @copyberry

> #43102 Include GIO in voice SDKs and native runtimes @copyberry

> #43109 Add explicit toolchain inputs for native voice builds @copyberry

> #43111 Add a Bazel target for native voice dependencies @copyberry

> #43114 Add Bazel preparation for native voice runtimes @copyberry

> #43117 Link Unix Bazel bindings against the prepared voice runtime @copyberry

> #43121 Require a prepared runtime when assembling voice helper packages @copyberry

> #43125 Add explicit Windows tool selection for native voice builds @copyberry

> #43144 Add Windows MSVC Bazel targets for native voice libraries @copyberry

> #43244 Add bounded GStreamer playback components to the voice host @copyberry

> #43248 Connect voice-host RTP audio to speaker playback @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.154.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-09-21-model-support-changes-in-rust-v0-154-0|21 Model Support changes in rust-v0.154.0]] · Model Support
- [[Changes/Codex CLI/2026-09-09-5-account-and-access-changes-in-rust-v0-154-0|5 Account and Access changes in rust-v0.154.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-09-19-apps-and-integrations-changes-in-rust-v0-154-0|19 Apps and Integrations changes in rust-v0.154.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-09-4-interface-experience-changes-in-rust-v0-154-0|4 Interface Experience changes in rust-v0.154.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-09-17-context-window-changes-in-rust-v0-154-0|17 Context Window changes in rust-v0.154.0]] · Context Window
- [[Changes/Codex CLI/2026-09-09-6-mobile-and-desktop-changes-in-rust-v0-154-0|6 Mobile and Desktop changes in rust-v0.154.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-09-25-safety-and-privacy-changes-in-rust-v0-154-0|25 Safety and Privacy changes in rust-v0.154.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-09-gpt-6-astra-is-now-available-in-the-model-picker-and-amazon-bedrock-catalogs-428|GPT-6-Astra is now available in the model picker and Amazon Bedrock catalogs]] · Model Support
- [[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2 Memory and Personalization changes in rust-v0.154.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-09-experimental-worktree-support-lets-you-create-isolated-checkouts-for-new-or-fork|Experimental worktree support lets you create isolated checkouts for new or forked…]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-09-42746-handle-pending-network-reviews-after-process-completion-copyberry|♯42746 Handle pending network reviews after process completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-09-09-6-agent-mode-changes-in-rust-v0-154-0|6 Agent Mode changes in rust-v0.154.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-09-42306-stabilize-the-detached-exec-server-session-resume-test-copyberry|♯42306 Stabilize the detached exec-server session resume test @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-09-09-6-collaboration-changes-in-rust-v0-154-0|6 Collaboration changes in rust-v0.154.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-09-7-developer-workflow-changes-in-rust-v0-154-0|7 Developer Workflow changes in rust-v0.154.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-09-119-other-changes-in-rust-v0-154-0|119 other changes in rust-v0.154.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-08 · OpenClaw · [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]]
- Later: 2026-09-10 · Raycast · [[Changes/Raycast/2026-09-10-dictation-improved-reliability-when-the-active-audio-device-changes|Dictation: Improved reliability when the active audio device changes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-09-6d6ee1&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-09-20-voice-and-audio-changes-in-rust-v0-154-0.md%0ACard%20ID%3A%20codex-cli-2026-09-09-6d6ee1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.154.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->