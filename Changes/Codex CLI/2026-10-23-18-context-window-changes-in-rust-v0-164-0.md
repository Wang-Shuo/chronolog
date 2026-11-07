---
card_id: codex-cli-2026-10-23-abc3aa
date: '2026-10-23'
description: 'Codex CLI · 2026-10-23 · Context Window: 18 changes in 0.164.0 — Failed
  compaction no longer leaves partial summaries in conversation history, and background…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fcf081dd064f1af0b562a48959f9154a39ca01b7a70f69bffa1ddfc47e2e7990
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-23-abc3aa
  comparison: ''
  date: '2026-10-23'
  description: 'Codex CLI — 0.164.0: 18 Context Window changes'
  evidence:
  - quote: 'Failed compaction no longer leaves partial summaries in conversation history,
      and background compaction failures fall back without panicking. (#53932, #55581)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53797 Refresh Guardian reviews when review context changes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53800 Wire background compaction into the turn lifecycle @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53831 Track content provenance through prompt assembly and compaction
      @tz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53872 Refresh model instructions in incremental-tool context windows
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53932 Preserve conversation history when compaction fails @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54046 Track approval cancellation sources and Guardian context changes
      @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54281 Attribute compaction summaries to the assistant in Guardian transcripts
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54316 Centralize context fragment kind constants @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54590 Capture sender context for `codex_app.create_thread` deliveries
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55355 Remove the long-thread accuracy warning after compaction @asohrabi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55391 Deduplicate native agent messages in Guardian review context @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55581 Avoid panics after background compaction fails before a checkpoint
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55587 Allow callers to control prompt cache keys independently of session
      IDs @rm-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55597 Extract shared TUI user prompt helpers from IDE context @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55666 Omit reasoning and compaction from Decisions snapshot comparisons
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55733 Box session metadata and compaction payloads in `RolloutItem` @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55993 Preserve per-execution trace context in code-mode stdio callbacks
      @bschoepke-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-context-window-changes-in-rust-v0-164-0
  source_release: codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d
  source_type: github_releases
  theme: context-window
  title: 18 Context Window changes in rust-v0.164.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-22-updated-the-claude-api-skill-service-account-keys-and-workload-identity-federati|Updated
  the /claude-api skill]]'
- '[[Changes/Ollama/2026-10-22-ollama-launch-now-passes-cloud-models-context-lengths-and-capabilities-to-coding|ollama
  launch now passes cloud models'' context lengths and capabilities to coding…]]'
- '[[Changes/OpenClaw/2026-10-22-4-context-window-changes-in-v2026-10-6|4 Context
  Window changes in v2026.10.6]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d]]'
source_type: github_releases
theme: context-window
title: 18 Context Window changes in rust-v0.164.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Context Window changes in rust-v0.164.0

**Codex CLI** · 2026-10-23 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.164.0) · from [[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|0.164.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Failed compaction no longer leaves partial summaries in conversation history, and background compaction failures fall back without panicking. (#53932, #55581)

> #53797 Refresh Guardian reviews when review context changes @jif-oai

> #53800 Wire background compaction into the turn lifecycle @rka-oai

> #53831 Track content provenance through prompt assembly and compaction @tz-openai

> #53872 Refresh model instructions in incremental-tool context windows @rhan-oai

> #53932 Preserve conversation history when compaction fails @jif-oai

> #54046 Track approval cancellation sources and Guardian context changes @vkg-oai

> #54281 Attribute compaction summaries to the assistant in Guardian transcripts @jif-oai

> #54316 Centralize context fragment kind constants @ioanbudea-OAI

> #54590 Capture sender context for `codex_app.create_thread` deliveries @felixxia-oai

> #55355 Remove the long-thread accuracy warning after compaction @asohrabi-oai

> #55391 Deduplicate native agent messages in Guardian review context @jif-oai

> #55581 Avoid panics after background compaction fails before a checkpoint @jif-oai

> #55587 Allow callers to control prompt cache keys independently of session IDs @rm-openai

> #55597 Extract shared TUI user prompt helpers from IDE context @bc-openai

> #55666 Omit reasoning and compaction from Decisions snapshot comparisons @swastik-oai

> #55733 Box session metadata and compaction payloads in `RolloutItem` @charliemarsh-oai

> #55993 Preserve per-execution trace context in code-mode stdio callbacks @bschoepke-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-23-24-account-and-access-changes-in-rust-v0-164-0|24 Account and Access changes in rust-v0.164.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-23-8-mobile-and-desktop-changes-in-rust-v0-164-0|8 Mobile and Desktop changes in rust-v0.164.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0|30 Apps and Integrations changes in rust-v0.164.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-9-interface-experience-changes-in-rust-v0-164-0|9 Interface Experience changes in rust-v0.164.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-23-9-model-support-changes-in-rust-v0-164-0|9 Model Support changes in rust-v0.164.0]] · Model Support
- [[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14 Developer Workflow changes in rust-v0.164.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice and Audio changes in rust-v0.164.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-23-183-other-changes-in-rust-v0-164-0|183 other changes in rust-v0.164.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-22 · OpenClaw · [[Changes/OpenClaw/2026-10-22-4-context-window-changes-in-v2026-10-6|4 Context Window changes in v2026.10.6]]
- Later: 2026-10-23 · Dify · [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-23-abc3aa&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-23-18-context-window-changes-in-rust-v0-164-0.md%0ACard%20ID%3A%20codex-cli-2026-10-23-abc3aa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.164.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->