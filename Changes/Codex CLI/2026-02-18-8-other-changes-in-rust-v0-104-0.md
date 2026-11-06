---
card_id: codex-cli-2026-02-18-9e5715
date: '2026-02-18'
description: 'Codex CLI · 2026-02-18 · Other changes: 8 changes in 0.104.0 — Added
  `WS_PROXY`/`WSS_PROXY` environment support (including lowercase variants) for websocket…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6629540412339381c8789e90a9477bf73a8c5b36a9d5d8e0caf3599a16db5479
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-18-9e5715
  comparison: ''
  date: '2026-02-18'
  description: 'Codex CLI — 0.104.0: 8 other changes'
  evidence:
  - quote: Added `WS_PROXY`/`WSS_PROXY` environment support (including lowercase variants)
      for websocket proxying in the network proxy. (#11784)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: App-server v2 now emits notifications when threads are archived or unarchived,
      enabling clients to react without polling. (#12030)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: '`Ctrl+C`/`Ctrl+D` now cleanly exits the cwd-change prompt during resume/fork
      flows instead of implicitly selecting an option. (#12040)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: Made the Rust release workflow resilient to `npm publish` attempts for
      an already-published version. (#12044)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: '#11784 feat(network-proxy): add websocket proxy env support @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: '#12044 don''t fail if an npm publish attempt is for an existing version.
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: '#12040 tui: exit session on Ctrl+C in cwd change prompt @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  - quote: '#12030 app-server: Emit thread archive/unarchive notifications @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.104.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-other-changes-in-rust-v0-104-0
  source_release: codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in rust-v0.104.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34|codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34]]'
source_type: github_releases
theme: uncategorized
title: 8 other changes in rust-v0.104.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in rust-v0.104.0

**Codex CLI** · 2026-02-18 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.104.0) · from [[Releases/Codex CLI/codex-cli-2026-02-18-rust-v0-104-0-github-287549221-f2e69b34|0.104.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `WS_PROXY`/`WSS_PROXY` environment support (including lowercase variants) for websocket proxying in the network proxy. (#11784)

> App-server v2 now emits notifications when threads are archived or unarchived, enabling clients to react without polling. (#12030)

> `Ctrl+C`/`Ctrl+D` now cleanly exits the cwd-change prompt during resume/fork flows instead of implicitly selecting an option. (#12040)

> Made the Rust release workflow resilient to `npm publish` attempts for an already-published version. (#12044)

> #11784 feat(network-proxy): add websocket proxy env support @viyatb-oai

> #12044 don't fail if an npm publish attempt is for an existing version. @iceweasel-oai

> #12040 tui: exit session on Ctrl+C in cwd change prompt @charley-oai

> #12030 app-server: Emit thread archive/unarchive notifications @euroelessar

Source: https://github.com/openai/codex/releases/tag/rust-v0.104.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-18-2-model-support-changes-in-rust-v0-104-0|2 Model Support changes in rust-v0.104.0]] · Model Support
- [[Changes/Codex CLI/2026-02-18-protocol-core-now-carry-distinct-approval-ids-for-command-approvals-to-support-m|Protocol/core now carry distinct approval IDs for command approvals to support…]] · Agent Mode
- [[Changes/Codex CLI/2026-02-18-2-context-window-changes-in-rust-v0-104-0|2 Context Window changes in rust-v0.104.0]] · Context Window
- [[Changes/Codex CLI/2026-02-18-2-developer-workflow-changes-in-rust-v0-104-0|2 Developer Workflow changes in rust-v0.104.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-18-9e5715&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-18-8-other-changes-in-rust-v0-104-0.md%0ACard%20ID%3A%20codex-cli-2026-02-18-9e5715%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.104.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->