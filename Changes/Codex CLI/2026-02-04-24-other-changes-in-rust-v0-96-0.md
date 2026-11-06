---
card_id: codex-cli-2026-02-04-5d1c14
date: '2026-02-04'
description: 'Codex CLI · 2026-02-04 · Other changes: 24 changes in 0.96.0 — Enabled
  `unified_exec` on all non-Windows platforms. (#10641)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 15006be5b25246509b7fb131523cd98dd84e72ca4c14530c3ddf6e73749dc108
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-04-5d1c14
  comparison: ''
  date: '2026-02-04'
  description: 'Codex CLI — 0.96.0: 24 other changes'
  evidence:
  - quote: Enabled `unified_exec` on all non-Windows platforms. (#10641)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: Thread listing now queries the state DB first (including archived threads)
      and falls back to filesystem traversal only when needed, improving listing correctness
      and resilience. (#10544)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: Dynamic tool injection now runs in a single transaction to avoid partial
      state updates. (#10614)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: 'Refined `request_rule` guidance used in approval-policy prompting to correct
      rule behavior. (#10379, #10598)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: Updated app-server docs for `thread/compact` to clarify its asynchronous
      behavior and thread-busy lifecycle. (#10445)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: Updated TUI docs to match the mode-specific `Esc` behavior in `request_user_input`.
      (#10569)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: Migrated state DB helpers to a versioned SQLite filename scheme and cleaned
      up legacy state files during runtime initialization. (#10623)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: 'Expanded runtime telemetry with websocket timing metrics and simplified
      internal metadata flow in core client plumbing. (#10577, #10589)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10569 tui: make Esc clear request_user_input notes while notes are shown
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10577 feat: log webscocket timing into runtime metrics @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10445 Add thread/compact v2 @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10589 Move metadata calculation out of client @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10379 fix(core) updated request_rule guidance @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10598 fix(core) Request Rule guidance tweak @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10544 Prefer state DB thread listings before filesystem @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10614 fix: single transaction for dyn tools injection @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10568 Requirements: add source to constrained requirement values @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10611 chore: simplify user message detection @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10618 fix: make sure file exist in `find_thread_path_by_id_str_in_subdir`
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10619 nit: cleaning @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10324 Add a codex.rate_limits event for websockets @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10623 Migrate state DB path helpers to versioned filename @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10638 Update tests to stop using sse_completed fixture @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  - quote: '#10641 feat: land unified_exec @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.96.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 24-other-changes-in-rust-v0-96-0
  source_release: codex-cli-2026-02-04-rust-v0-96-0-github-283083942-f92045dd
  source_type: github_releases
  theme: uncategorized
  title: 24 other changes in rust-v0.96.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-96-0-github-283083942-f92045dd|codex-cli-2026-02-04-rust-v0-96-0-github-283083942-f92045dd]]'
source_type: github_releases
theme: uncategorized
title: 24 other changes in rust-v0.96.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 other changes in rust-v0.96.0

**Codex CLI** · 2026-02-04 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.96.0) · from [[Releases/Codex CLI/codex-cli-2026-02-04-rust-v0-96-0-github-283083942-f92045dd|0.96.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Enabled `unified_exec` on all non-Windows platforms. (#10641)

> Thread listing now queries the state DB first (including archived threads) and falls back to filesystem traversal only when needed, improving listing correctness and resilience. (#10544)

> Dynamic tool injection now runs in a single transaction to avoid partial state updates. (#10614)

> Refined `request_rule` guidance used in approval-policy prompting to correct rule behavior. (#10379, #10598)

> Updated app-server docs for `thread/compact` to clarify its asynchronous behavior and thread-busy lifecycle. (#10445)

> Updated TUI docs to match the mode-specific `Esc` behavior in `request_user_input`. (#10569)

> Migrated state DB helpers to a versioned SQLite filename scheme and cleaned up legacy state files during runtime initialization. (#10623)

> Expanded runtime telemetry with websocket timing metrics and simplified internal metadata flow in core client plumbing. (#10577, #10589)

> #10569 tui: make Esc clear request_user_input notes while notes are shown @charley-oai

> #10577 feat: log webscocket timing into runtime metrics @apanasenko-oai

> #10445 Add thread/compact v2 @aibrahim-oai

> #10589 Move metadata calculation out of client @pakrym-oai

> #10379 fix(core) updated request_rule guidance @dylan-hurd-oai

> #10598 fix(core) Request Rule guidance tweak @dylan-hurd-oai

> #10544 Prefer state DB thread listings before filesystem @jif-oai

> #10614 fix: single transaction for dyn tools injection @jif-oai

> #10568 Requirements: add source to constrained requirement values @gt-oai

> #10611 chore: simplify user message detection @jif-oai

> #10618 fix: make sure file exist in `find_thread_path_by_id_str_in_subdir` @jif-oai

> #10619 nit: cleaning @jif-oai

> #10324 Add a codex.rate_limits event for websockets @rasmusrygaard

> #10623 Migrate state DB path helpers to versioned filename @jif-oai

> #10638 Update tests to stop using sse_completed fixture @pakrym-oai

> #10641 feat: land unified_exec @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.96.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-04-added-websocket-side-rate-limit-signaling-via-a-new-codex-rate-limits-event-with|Added websocket-side rate limit signaling via a new codex.rate_limits event…]] · Model Support
- [[Changes/Codex CLI/2026-02-04-constrained-requirement-values-now-include-source-provenance-enabling-source-awa|Constrained requirement values now include source provenance, enabling source-aware…]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-04-added-thread-compact-to-the-v2-app-server-api-as-an-async-trigger-rpc-so-clients|Added thread/compact to the v2 app-server API as an async trigger RPC, so clients…]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-04-5d1c14&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-04-24-other-changes-in-rust-v0-96-0.md%0ACard%20ID%3A%20codex-cli-2026-02-04-5d1c14%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.96.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->