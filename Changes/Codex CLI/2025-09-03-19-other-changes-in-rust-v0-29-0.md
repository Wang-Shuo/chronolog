---
card_id: codex-cli-2025-09-03-619de5
date: '2025-09-03'
description: 'Codex CLI · 2025-09-03 · Other changes: 19 changes in 0.29.0 — **Stable,
  cross‑platform file locking** using std `fs` APIs.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 875c1bee6b5a91019cc0387c8f38a00c60560cfae6343bb04f91c7350261884b
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-03-619de5
  comparison: ''
  date: '2025-09-03'
  description: 'Codex CLI — 0.29.0: 19 other changes'
  evidence:
  - quote: '**Stable, cross‑platform file locking** using std `fs` APIs.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '**Auth consolidation**: `CodexAuth` and `AuthManager` moved into the `core`
      crate.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '**Rate‑limit handling restored** for API‑key usage.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '**Core rollout refactor**: extract `rollout` module, add listing API,
      return file heads.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '**Quality of life**: support `cd foo && ...` in `exec`/`apply_patch`,
      fix TUI flicker, prefer ratatui `Stylize`.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '**Distribution**: include Windows ARM64 executable in the npm package.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '**Switch to the latest search tool**.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#3086] Use the new search tool'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#1634] core(rollout): extract rollout module, add listing API, and return
      file heads'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#2894] Add stable file locking using std::fs APIs'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#3074] Move CodexAuth and AuthManager to the core crate'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#3070] Add back rate‑limit error handling when using API key'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#3083] Parse “cd foo && ...” for exec and apply_patch'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#3068] Prefer ratatui Stylize for constructing lines/spans'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#3067] Include arm64 Windows executable in npm module'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#2736] Unify history loading'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#2461] Improve gpt‑oss compatibility'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#2651] apply‑patch: fix lark grammar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  - quote: '[#2667] Bump thiserror from 2.0.12 to 2.0.16 in codex‑rs'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.29.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 19-other-changes-in-rust-v0-29-0
  source_release: codex-cli-2025-09-03-rust-v0-29-0-github-244361437-fe9adbc1
  source_type: github_releases
  theme: uncategorized
  title: 19 other changes in rust-v0.29.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-03-rust-v0-29-0-github-244361437-fe9adbc1|codex-cli-2025-09-03-rust-v0-29-0-github-244361437-fe9adbc1]]'
source_type: github_releases
theme: uncategorized
title: 19 other changes in rust-v0.29.0
type: change
---

<!-- chronolog:begin region="header" -->
# 19 other changes in rust-v0.29.0

**Codex CLI** · 2025-09-03 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.29.0) · from [[Releases/Codex CLI/codex-cli-2025-09-03-rust-v0-29-0-github-244361437-fe9adbc1|0.29.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Stable, cross‑platform file locking** using std `fs` APIs.

> **Auth consolidation**: `CodexAuth` and `AuthManager` moved into the `core` crate.

> **Rate‑limit handling restored** for API‑key usage.

> **Core rollout refactor**: extract `rollout` module, add listing API, return file heads.

> **Quality of life**: support `cd foo && ...` in `exec`/`apply_patch`, fix TUI flicker, prefer ratatui `Stylize`.

> **Distribution**: include Windows ARM64 executable in the npm package.

> **Switch to the latest search tool**.

> [#3086] Use the new search tool

> [#1634] core(rollout): extract rollout module, add listing API, and return file heads

> [#2894] Add stable file locking using std::fs APIs

> [#3074] Move CodexAuth and AuthManager to the core crate

> [#3070] Add back rate‑limit error handling when using API key

> [#3083] Parse “cd foo && ...” for exec and apply_patch

> [#3068] Prefer ratatui Stylize for constructing lines/spans

> [#3067] Include arm64 Windows executable in npm module

> [#2736] Unify history loading

> [#2461] Improve gpt‑oss compatibility

> [#2651] apply‑patch: fix lark grammar

> [#2667] Bump thiserror from 2.0.12 to 2.0.16 in codex‑rs

Source: https://github.com/openai/codex/releases/tag/rust-v0.29.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-03-3071-use-experimental-reasoning-summary|♯3071 Use experimental reasoning summary]] · Model Support
- [[Changes/Codex CLI/2025-09-03-3089-docs-update-link-to-https-agents-md|♯3089 Docs: update link to (source link)]] · Agent Mode
- [[Changes/Codex CLI/2025-09-03-3061-show-loading-state-when-search-results-are-pending|♯3061 Show loading state when @ search results are pending]] · Search and Browsing
- [[Changes/Codex CLI/2025-09-03-2-mobile-and-desktop-changes-in-rust-v0-29-0|2 Mobile and Desktop changes in rust-v0.29.0]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-03-619de5&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-03-19-other-changes-in-rust-v0-29-0.md%0ACard%20ID%3A%20codex-cli-2025-09-03-619de5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.29.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->