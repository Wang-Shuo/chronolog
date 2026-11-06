---
card_id: codex-cli-2026-09-22-ada1a9
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Memory and Personalization: 6 changes in 0.156.0
  — Clarify that deprecated `friendly` and `pragmatic` personality settings no longer…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1160
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a4c03baeed7734517095a9d115f7895a86c8d503c5ab4a4147a718ccb9f13628
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-ada1a9
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 6 Memory and Personalization changes'
  evidence:
  - quote: Clarify that deprecated `friendly` and `pragmatic` personality settings
      no longer select response styles. (#45809)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44935 Remove personality selection from the TUI @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44946 Retire Friendly and Pragmatic personality selection @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45809 Retire the personality feature flag and document deprecated settings
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45956 Record memory storage size after successful consolidation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46531 Preserve request-level reasoning effort for memory and title workers
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-memory-and-personalization-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: memory
  title: 6 Memory and Personalization changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-vscode-added-memory-and-instructions-entries-to-the-customize-menu-memory-shows|VSCode
  Added Memory and Instructions entries to the Customize menu]]'
- '[[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7
  Memory and Personalization changes in rust-v0.155.0]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear
  down the processes an internal git command started when it times out, so a slow…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: memory
title: 6 Memory and Personalization changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Memory and Personalization changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Clarify that deprecated `friendly` and `pragmatic` personality settings no longer select response styles. (#45809)

> #44935 Remove personality selection from the TUI @rhan-oai

> #44946 Retire Friendly and Pragmatic personality selection @rhan-oai

> #45809 Retire the personality feature flag and document deprecated settings @rhan-oai

> #45956 Record memory storage size after successful consolidation @jif-oai

> #46531 Preserve request-level reasoning effort for memory and title workers @felixxia-oai

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
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear down the processes an internal git command started when it times out, so a slow…]]
- Later: 2026-09-22 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-22-resuming-large-local-sessions-keeps-transcript-memory-bounded-for-smoother-cli-p|Resuming large local sessions keeps transcript memory bounded for smoother CLI performance]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-ada1a9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-ada1a9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->