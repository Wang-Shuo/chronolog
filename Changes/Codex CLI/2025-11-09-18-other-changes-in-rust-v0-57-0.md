---
card_id: codex-cli-2025-11-09-44a628
date: '2025-11-09'
description: 'Codex CLI · 2025-11-09 · Other changes: 18 changes in 0.57.0 — Improve
  timeout on long running commasnds'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 09c60d0ddb6b27595195d9b2c1d5d69749e67f441be875b5b8bf91f0c5d4f06e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-11-09-44a628
  comparison: ''
  date: '2025-11-09'
  description: 'Codex CLI — 0.57.0: 18 other changes'
  evidence:
  - quote: Improve timeout on long running commasnds
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6233 – Freeform unified exec output formatting'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6342 – Make `generate_ts` prettier output warn-only'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6335 – TUI: fix backtracking past `/status`'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#1994 – Enable CTRL-n/CTRL-p for navigating slash commands, files, history'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6340 – Skip retries on `insufficient_quota` errors'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6347 – Refresh AI labeler rules to match issue tracker labels'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6346 – Prefer `wait_for_event` over `wait_for_event_with_timeout` (initial
      update)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#5486 – Fix `apply_patch` rename/move path resolution'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6349 – Prefer `wait_for_event` over `wait_for_event_with_timeout` (follow-up)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6336 – App-server: implement `account/read` endpoint'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6338 – App-server: expose additional fields on `Thread`'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6368 – App-server: README updates for threads and turns'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6369 – TUI: add inline comments to `tui.rs`'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6370 – Add `--promote-alpha` option to `create_github_release` script'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6377 – App-server docs: add initialization section'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6252 – Core: replace Cloudflare 403 HTML with friendly message'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  - quote: '#6380 – Unified exec: allow safe commands without approval'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.57.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-other-changes-in-rust-v0-57-0
  source_release: codex-cli-2025-11-09-rust-v0-57-0-github-260963239-baa7573b
  source_type: github_releases
  theme: uncategorized
  title: 18 other changes in rust-v0.57.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-11-09-rust-v0-57-0-github-260963239-baa7573b|codex-cli-2025-11-09-rust-v0-57-0-github-260963239-baa7573b]]'
source_type: github_releases
theme: uncategorized
title: 18 other changes in rust-v0.57.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 other changes in rust-v0.57.0

**Codex CLI** · 2025-11-09 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.57.0) · from [[Releases/Codex CLI/codex-cli-2025-11-09-rust-v0-57-0-github-260963239-baa7573b|0.57.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improve timeout on long running commasnds

> #6233 – Freeform unified exec output formatting

> #6342 – Make `generate_ts` prettier output warn-only

> #6335 – TUI: fix backtracking past `/status`

> #1994 – Enable CTRL-n/CTRL-p for navigating slash commands, files, history

> #6340 – Skip retries on `insufficient_quota` errors

> #6347 – Refresh AI labeler rules to match issue tracker labels

> #6346 – Prefer `wait_for_event` over `wait_for_event_with_timeout` (initial update)

> #5486 – Fix `apply_patch` rename/move path resolution

> #6349 – Prefer `wait_for_event` over `wait_for_event_with_timeout` (follow-up)

> #6336 – App-server: implement `account/read` endpoint

> #6338 – App-server: expose additional fields on `Thread`

> #6368 – App-server: README updates for threads and turns

> #6369 – TUI: add inline comments to `tui.rs`

> #6370 – Add `--promote-alpha` option to `create_github_release` script

> #6377 – App-server docs: add initialization section

> #6252 – Core: replace Cloudflare 403 HTML with friendly message

> #6380 – Unified exec: allow safe commands without approval

Source: https://github.com/openai/codex/releases/tag/rust-v0.57.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-11-09-tui-quality-of-life-ctrl-n-p-navigation-for-slash-command-lists-and-backtracking|TUI quality-of-life: ctrl-n/p navigation for slash command lists and backtracking…]] · Interface Experience
- [[Changes/Codex CLI/2025-11-09-6351-promote-shell-config-tool-to-model-family-config|♯6351 – Promote shell config tool to model family config]] · Model Support
- [[Changes/Codex CLI/2025-11-09-6367-sdk-add-network-access-and-web-search-options-to-typescript-sdk|♯6367 – SDK: add network_access and web_search options to TypeScript SDK]] · Search and Browsing
- [[Changes/Codex CLI/2025-11-09-6353-app-server-add-auth-v2-doc-update-codex-mcp-interface-section|♯6353 – App-server: add auth v2 doc & update Codex MCP interface section]] · Apps and Integrations
- [[Changes/Codex CLI/2025-11-09-4-developer-workflow-changes-in-rust-v0-57-0|4 Developer Workflow changes in rust-v0.57.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-11-09-44a628&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-11-09-18-other-changes-in-rust-v0-57-0.md%0ACard%20ID%3A%20codex-cli-2025-11-09-44a628%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.57.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->