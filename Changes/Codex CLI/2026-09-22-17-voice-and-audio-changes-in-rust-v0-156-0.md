---
card_id: codex-cli-2026-09-22-c0f337
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Voice and Audio: 17 changes in 0.156.0 — Voice
  conversations are enabled by default, with an F8 toggle, a `/voice settings` picker…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support
    for Inline Notes]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2997
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: voice
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7c6f657aa0bab13ddc36213fe202e0b38c42d253692d7dfd14ffe00be2520beb
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-c0f337
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 17 Voice and Audio changes'
  evidence:
  - quote: 'Voice conversations are enabled by default, with an F8 toggle, a `/voice
      settings` picker, and bundled audio runtimes for Linux and Windows. (#44921,
      #46071, #44622, #44714, #44922)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: Prevent speech from being dropped during playback pauses or bursts of incoming
      audio. (#46880)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44622 Add `/voice settings` to choose a voice for future conversations
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44671 Keep voice sessions alive through mute and audio backlog @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44714 Bundle Linux voice runtimes and improve audio reliability @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44749 Preserve voice caption order when replaying TUI history @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44921 Enable TUI voice conversations by default @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44922 Bundle native voice runtimes in Windows releases @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44924 Refresh the speaker format when restarting voice output @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44925 Accept voice response audio before captions on quiet turns @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44928 Preserve voice meter history through quiet samples @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44942 Clarify the Windows Visual C++ runtime notice for voice packages
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44952 Keep voice captions visible across speaker updates and history
      handoff @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46058 Attribute analytics events to realtime voice sessions @chrisdong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46071 Add a configurable F8 shortcut for voice conversations @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46835 Respect reduced motion in the voice UI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46880 Preserve voice playback across pauses and packet bursts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-voice-and-audio-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: voice
  title: 17 Voice and Audio changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice
  and Audio changes in v2026.9.5]]'
- '[[Changes/ElevenLabs/2026-09-21-text-to-speech|Text to Speech]]'
- '[[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and
  Audio changes in v0.11.4]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: voice
title: 17 Voice and Audio changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Voice and Audio changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/voice|Voice and Audio]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Voice conversations are enabled by default, with an F8 toggle, a `/voice settings` picker, and bundled audio runtimes for Linux and Windows. (#44921, #46071, #44622, #44714, #44922)

> Prevent speech from being dropped during playback pauses or bursts of incoming audio. (#46880)

> #44622 Add `/voice settings` to choose a voice for future conversations @bc-openai

> #44671 Keep voice sessions alive through mute and audio backlog @bc-openai

> #44714 Bundle Linux voice runtimes and improve audio reliability @bc-openai

> #44749 Preserve voice caption order when replaying TUI history @bc-openai

> #44921 Enable TUI voice conversations by default @bc-openai

> #44922 Bundle native voice runtimes in Windows releases @bc-openai

> #44924 Refresh the speaker format when restarting voice output @bc-openai

> #44925 Accept voice response audio before captions on quiet turns @bc-openai

> #44928 Preserve voice meter history through quiet samples @bc-openai

> #44942 Clarify the Windows Visual C++ runtime notice for voice packages @bc-openai

> #44952 Keep voice captions visible across speaker updates and history handoff @bc-openai

> #46058 Attribute analytics events to realtime voice sessions @chrisdong-oai

> #46071 Add a configurable F8 shortcut for voice conversations @etraut-openai

> #46835 Respect reduced motion in the voice UI @etraut-openai

> #46880 Preserve voice playback across pauses and packet bursts @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.156.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13 Account and Access changes in rust-v0.156.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-22-32-interface-experience-changes-in-rust-v0-156-0|32 Interface Experience changes in rust-v0.156.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-22-2-search-and-browsing-changes-in-rust-v0-156-0|2 Search and Browsing changes in rust-v0.156.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-22-46027-document-and-test-wildcards-in-network-proxy-domain-patterns-viyatb-oai|♯46027 Document and test ? wildcards in network proxy domain patterns @viyatb-oai]] · Files and Data
- [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544 Discourage logging full image generation results @Gan-Tu]] · Image Generation
- [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]] · Context Window
- [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11 Mobile and Desktop changes in rust-v0.156.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Voice and Audio

- Earlier: 2026-09-21 · Open WebUI · [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]]
- Later: 2026-09-22 · Google Antigravity · [[Changes/Google Antigravity/2026-09-22-right-clicking-an-image-caption-or-an-enlarged-image-no-longer-pops-open-the-thu|Right-clicking an image caption or an enlarged image no longer pops open…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-09 · Descript · [[Changes/Descript/2018-07-09-type-in-parentheses-to-add-notes-to-your-script-that-don-t-affect-the-audio-text|Support for Inline Notes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-c0f337&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-c0f337%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->