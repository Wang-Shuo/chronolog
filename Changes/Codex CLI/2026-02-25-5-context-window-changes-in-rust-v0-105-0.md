---
card_id: codex-cli-2026-02-25-9b5ae6
date: '2026-02-25'
description: 'Codex CLI · 2026-02-25 · Context Window: 5 changes in 0.105.0 — The
  TUI picked up new convenience commands: `/copy` copies the latest complete assistant
  reply…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1028
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 74df2744a4bdb92f3f2c6c8f7aee5e26ecf85668cc557136af8c036f4c940022
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-25-9b5ae6
  comparison: ''
  date: '2026-02-25'
  description: 'Codex CLI — 0.105.0: 5 Context Window changes'
  evidence:
  - quote: 'The TUI picked up new convenience commands: `/copy` copies the latest
      complete assistant reply, while `/clear` and `Ctrl-L` clear the screen without
      losing thread context, with `/clear` also able to start a fresh chat. (#12444,
      #12520, #12613, #12628)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12073 Add model-visible context layout snapshot tests @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12179 Move previous turn context tracking into ContextManager history
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12252 Fix compaction context reinjection and model baselines @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12717 Raise image byte estimate for compaction token accounting @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-context-window-changes-in-rust-v0-105-0
  source_release: codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed
  source_type: github_releases
  theme: context-window
  title: 5 Context Window changes in rust-v0.105.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-24-tool-results-larger-than-50k-characters-are-now-persisted-to-disk-previously-100|Tool
  results larger than 50K characters are now persisted to disk (previously 100K)]]'
- '[[Changes/ChatGPT/2026-02-25-ad-hoc-text-sources-paste-notes-briefs-or-reference-material-directly-to-capture|Ad-hoc
  text sources]]'
- '[[Changes/ChatGPT/2026-02-25-projects-now-make-it-easy-to-build-a-living-knowledge-base-by-adding-sources-whe|Projects
  now make it easy to build a living knowledge base by adding sources…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed]]'
source_type: github_releases
theme: context-window
title: 5 Context Window changes in rust-v0.105.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Context Window changes in rust-v0.105.0

**Codex CLI** · 2026-02-25 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.105.0) · from [[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|0.105.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The TUI picked up new convenience commands: `/copy` copies the latest complete assistant reply, while `/clear` and `Ctrl-L` clear the screen without losing thread context, with `/clear` also able to start a fresh chat. (#12444, #12520, #12613, #12628)

> #12073 Add model-visible context layout snapshot tests @charley-oai

> #12179 Move previous turn context tracking into ContextManager history @charley-oai

> #12252 Fix compaction context reinjection and model baselines @charley-oai

> #12717 Raise image byte estimate for compaction token accounting @etraut-openai

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
- [[Changes/Codex CLI/2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0|9 Safety and Privacy changes in rust-v0.105.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model Support changes in rust-v0.105.0]] · Model Support
- [[Changes/Codex CLI/2026-02-25-2-mobile-and-desktop-changes-in-rust-v0-105-0|2 Mobile and Desktop changes in rust-v0.105.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-25-2-voice-and-audio-changes-in-rust-v0-105-0|2 Voice and Audio changes in rust-v0.105.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-156-other-changes-in-rust-v0-105-0|156 other changes in rust-v0.105.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-02-25 · ChatGPT · [[Changes/ChatGPT/2026-02-25-projects-now-make-it-easy-to-build-a-living-knowledge-base-by-adding-sources-whe|Projects now make it easy to build a living knowledge base by adding sources…]]
- Later: 2026-02-25 · Gemini CLI · [[Changes/Gemini CLI/2026-02-25-2-context-window-changes-in-v0-30-0|2 Context Window changes in v0.30.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-25-9b5ae6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-25-5-context-window-changes-in-rust-v0-105-0.md%0ACard%20ID%3A%20codex-cli-2026-02-25-9b5ae6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.105.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->