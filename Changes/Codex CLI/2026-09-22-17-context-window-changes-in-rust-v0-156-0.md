---
card_id: codex-cli-2026-09-22-542e3b
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Context Window: 17 changes in 0.156.0 — #44669
  Resolve filesystem denials with explicit path context @seanh-oai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1237
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0fccd4b1ab597f12f5f1ad3b3e2a558dd97eb4b5de3347ef60248b0609ec5848
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-542e3b
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 17 Context Window changes'
  evidence:
  - quote: '#44669 Resolve filesystem denials with explicit path context @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44866 Preserve originating context for yielded code-mode tool calls @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44932 Unify context snapshots and group requests into windows @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44934 Add scenario snapshots for remote compaction and Code Mode tools
      @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44976 Make context snapshot text rendering consistent @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45090 Preserve conversation context and separate next actions in recaps
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45094 Estimate history tokens from content instead of serialized envelopes
      @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45417 Extract guardian transcript selection into `guardian-context` @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45683 Consolidate guardian transcript tests in `guardian-context` @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46009 Centralize compaction checkpoint selection and validation @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46044 Include Code Mode tool metadata in compaction prompts @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46064 Consolidate Guardian tests at shared policy and context boundaries
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46072 Account for file images in context budgets and Guardian reviews
      @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46512 Capture Guardian review checkpoints from live context @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46522 Enable Guardian parent-compaction reuse by default @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46541 Add opt-in compaction after final responses @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47030 Preserve ordered assistant context in Guardian reviews @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-context-window-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: context-window
  title: 17 Context Window changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long
  tasks now compact when they actually need to rather than running out of room]]'
- '[[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context
  Window changes in rust-v0.155.0]]'
- '[[Changes/Cline/2026-09-22-2-context-window-changes-in-v4-1-20|2 Context Window
  changes in v4.1.20]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: context-window
title: 17 Context Window changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Context Window changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #44669 Resolve filesystem denials with explicit path context @seanh-oai

> #44866 Preserve originating context for yielded code-mode tool calls @abhinav-oai

> #44932 Unify context snapshots and group requests into windows @pakrym-oai

> #44934 Add scenario snapshots for remote compaction and Code Mode tools @pakrym-oai

> #44976 Make context snapshot text rendering consistent @pakrym-oai

> #45090 Preserve conversation context and separate next actions in recaps @fcoury-oai

> #45094 Estimate history tokens from content instead of serialized envelopes @won-openai

> #45417 Extract guardian transcript selection into `guardian-context` @felixxia-oai

> #45683 Consolidate guardian transcript tests in `guardian-context` @felixxia-oai

> #46009 Centralize compaction checkpoint selection and validation @felixxia-oai

> #46044 Include Code Mode tool metadata in compaction prompts @ningyi-oai

> #46064 Consolidate Guardian tests at shared policy and context boundaries @felixxia-oai

> #46072 Account for file images in context budgets and Guardian reviews @kchainani-oai

> #46512 Capture Guardian review checkpoints from live context @jif-oai

> #46522 Enable Guardian parent-compaction reuse by default @felixxia-oai

> #46541 Add opt-in compaction after final responses @hlevy-openai

> #47030 Preserve ordered assistant context in Guardian reviews @felixxia-oai

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
- [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11 Mobile and Desktop changes in rust-v0.156.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-22 · Cline · [[Changes/Cline/2026-09-22-2-context-window-changes-in-v4-1-20|2 Context Window changes in v4.1.20]]
- Later: 2026-09-24 · Cline · [[Changes/Cline/2026-09-24-long-replies-on-local-models-llama-cpp-ollama-lm-studio-that-hit-the-output-toke|Long replies on local models (llama.cpp, Ollama, LM Studio) that hit…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-542e3b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-17-context-window-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-542e3b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->