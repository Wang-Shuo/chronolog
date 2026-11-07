---
card_id: codex-cli-2026-09-17-d60e56
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Context Window: 20 changes in 0.155.0 — Accepted
  prompts are now saved even when compaction fails before a turn starts. (#44487)'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2556
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 97200612ac247cc3d07b3ce75012c8162ced93cc1eefff21e218a375a4108d80
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-d60e56
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 20 Context Window changes'
  evidence:
  - quote: Accepted prompts are now saved even when compaction fails before a turn
      starts. (#44487)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43534 Preserve Guardian context sections and share planned-action rendering
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43545 Preserve fork runtime versions without loading full model context
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43595 Centralize bounded Guardian review evidence in guardian-context
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43597 Move trusted tool metadata into shared Guardian context @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43599 Move trusted skill evidence into the Guardian context registry
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43601 Move Guardian image selection into shared context sections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43602 Move Guardian REPL evidence rendering into the shared context registry
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43796 Preserve reasoning effort through compaction and reset it on success
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43805 Centralize Guardian context composition @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43806 Centralize Guardian transcript policy in context profiles @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43912 Keep Guardian reviewers on summary-based compaction @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44164 Add Guardian context cost and request token telemetry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44166 Add aggregate budget enforcement for Guardian context @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44181 Use explicit histogram buckets for Guardian context metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44200 Use captured step settings when building model context @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44202 Use captured step model settings for extension context @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44255 Always use streamed remote compaction for supported providers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44273 Remove the unused legacy remote compaction implementation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44487 Preserve incoming prompts when pre-turn compaction fails @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 20-context-window-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: context-window
  title: 20 Context Window changes in rust-v0.155.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context
  Window changes in v1.0.85]]'
- '[[Changes/OpenHands/2026-09-16-test-cover-conversation-context-menu-by-aivong-openhands-in-https-github-com-ope|test:
  cover conversation context menu]]'
- '[[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long
  tasks now compact when they actually need to rather than running out of room]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: context-window
title: 20 Context Window changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Context Window changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Accepted prompts are now saved even when compaction fails before a turn starts. (#44487)

> #43534 Preserve Guardian context sections and share planned-action rendering @copyberry

> #43545 Preserve fork runtime versions without loading full model context @copyberry

> #43595 Centralize bounded Guardian review evidence in guardian-context @copyberry

> #43597 Move trusted tool metadata into shared Guardian context @copyberry

> #43599 Move trusted skill evidence into the Guardian context registry @copyberry

> #43601 Move Guardian image selection into shared context sections @copyberry

> #43602 Move Guardian REPL evidence rendering into the shared context registry @copyberry

> #43796 Preserve reasoning effort through compaction and reset it on success @copyberry

> #43805 Centralize Guardian context composition @copyberry

> #43806 Centralize Guardian transcript policy in context profiles @copyberry

> #43912 Keep Guardian reviewers on summary-based compaction @copyberry

> #44164 Add Guardian context cost and request token telemetry @copyberry

> #44166 Add aggregate budget enforcement for Guardian context @copyberry

> #44181 Use explicit histogram buckets for Guardian context metrics @copyberry

> #44200 Use captured step settings when building model context @copyberry

> #44202 Use captured step model settings for extension context @copyberry

> #44255 Always use streamed remote compaction for supported providers @copyberry

> #44273 Remove the unused legacy remote compaction implementation @copyberry

> #44487 Preserve incoming prompts when pre-turn compaction fails @copyberry

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
- [[Changes/Codex CLI/2026-09-17-20-voice-and-audio-changes-in-rust-v0-155-0|20 Voice and Audio changes in rust-v0.155.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-17-2-mobile-and-desktop-changes-in-rust-v0-155-0|2 Mobile and Desktop changes in rust-v0.155.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-17-44354-extract-shared-footer-hint-wrapping-in-the-tui-copyberry|♯44354 Extract shared footer hint wrapping in the TUI @copyberry]] · Collaboration
- [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-17-6-account-and-access-changes-in-rust-v0-155-0|6 Account and Access changes in rust-v0.155.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0|24 Apps and Integrations changes in rust-v0.155.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-17-96-other-changes-in-rust-v0-155-0|96 other changes in rust-v0.155.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-17 · Cline · [[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long tasks now compact when they actually need to rather than running out of room]]
- Later: 2026-09-18 · Lovable · [[Changes/Lovable/2026-09-18-type-or-to-add-context-and-skills-where-you-type|Type @ or / to add context and skills where you type]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-d60e56&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-20-context-window-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-d60e56%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->