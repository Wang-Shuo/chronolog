---
card_id: codex-cli-2025-12-21-3841ed
date: '2025-12-21'
description: 'Codex CLI · 2025-12-21 · Other changes: 13 changes in 0.77.0 — TUI2:
  Normalize mouse wheel + trackpad scrolling across terminals; add `tui.scroll_*`
  config…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f3cbe1bb34126f3e1b30515439e80a2d39f69d217bb9d64c2383ddd6698216fb
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-21-3841ed
  comparison: ''
  date: '2025-12-21'
  description: 'Codex CLI — 0.77.0: 13 other changes'
  evidence:
  - quote: 'TUI2: Normalize mouse wheel + trackpad scrolling across terminals; add
      `tui.scroll_*` config settings (PR #8357)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: 'Improve fuzzy file search display/consistency by centralizing file-name
      derivation in `codex-file-search` (PR #8334)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: 'TUI2: Reduce redundant redraws while scrolling transcripts (PR #8295)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: Changelog (PRs merged in this tag range)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8374 Remove plan from system skills: https://github.com/openai/codex/pull/8374'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8357 TUI2 scroll normalization + config knobs: https://github.com/openai/codex/pull/8357'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8353 Thread config loading now receives cwd (internal plumbing): https://github.com/openai/codex/pull/8353'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8345 Bump cargo-deny-action version (CI): https://github.com/openai/codex/pull/8345'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8334 Move file-name derivation into codex-file-search: https://github.com/openai/codex/pull/8334'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8333 Enable resume_warning suite module (test coverage / wiring fix):
      https://github.com/openai/codex/pull/8333'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8330 Make ConstraintError an enum (more structured errors): https://github.com/openai/codex/pull/8330'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8303 Fix /undo staging interaction: https://github.com/openai/codex/pull/8303'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  - quote: '#8311 Fix docs link in experimental.md: https://github.com/openai/codex/pull/8311'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.77.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-other-changes-in-rust-v0-77-0
  source_release: codex-cli-2025-12-21-rust-v0-77-0-github-271997317-8c159931
  source_type: github_releases
  theme: uncategorized
  title: 13 other changes in rust-v0.77.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-21-rust-v0-77-0-github-271997317-8c159931|codex-cli-2025-12-21-rust-v0-77-0-github-271997317-8c159931]]'
source_type: github_releases
theme: uncategorized
title: 13 other changes in rust-v0.77.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 other changes in rust-v0.77.0

**Codex CLI** · 2025-12-21 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.77.0) · from [[Releases/Codex CLI/codex-cli-2025-12-21-rust-v0-77-0-github-271997317-8c159931|0.77.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> TUI2: Normalize mouse wheel + trackpad scrolling across terminals; add `tui.scroll_*` config settings (PR #8357)

> Improve fuzzy file search display/consistency by centralizing file-name derivation in `codex-file-search` (PR #8334)

> TUI2: Reduce redundant redraws while scrolling transcripts (PR #8295)

> Changelog (PRs merged in this tag range)

> #8374 Remove plan from system skills: https://github.com/openai/codex/pull/8374

> #8357 TUI2 scroll normalization + config knobs: https://github.com/openai/codex/pull/8357

> #8353 Thread config loading now receives cwd (internal plumbing): https://github.com/openai/codex/pull/8353

> #8345 Bump cargo-deny-action version (CI): https://github.com/openai/codex/pull/8345

> #8334 Move file-name derivation into codex-file-search: https://github.com/openai/codex/pull/8334

> #8333 Enable resume_warning suite module (test coverage / wiring fix): https://github.com/openai/codex/pull/8333

> #8330 Make ConstraintError an enum (more structured errors): https://github.com/openai/codex/pull/8330

> #8303 Fix /undo staging interaction: https://github.com/openai/codex/pull/8303

> #8311 Fix docs link in experimental.md: https://github.com/openai/codex/pull/8311

Source: https://github.com/openai/codex/releases/tag/rust-v0.77.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-21-8295-coalesce-transcript-scroll-redraws-tui2-performance-https-github-com-openai|♯8295 Coalesce transcript scroll redraws (TUI2 performance)]] · Reliability and Performance
- [[Changes/Codex CLI/2025-12-21-3-model-support-changes-in-rust-v0-77-0|3 Model Support changes in rust-v0.77.0]] · Model Support
- [[Changes/Codex CLI/2025-12-21-2-account-and-access-changes-in-rust-v0-77-0|2 Account and Access changes in rust-v0.77.0]] · Account and Access
- [[Changes/Codex CLI/2025-12-21-2-safety-and-privacy-changes-in-rust-v0-77-0|2 Safety and Privacy changes in rust-v0.77.0]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-21-3841ed&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-21-13-other-changes-in-rust-v0-77-0.md%0ACard%20ID%3A%20codex-cli-2025-12-21-3841ed%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.77.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->