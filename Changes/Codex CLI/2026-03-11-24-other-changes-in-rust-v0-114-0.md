---
card_id: codex-cli-2026-03-11-b9c66b
date: '2026-03-11'
description: 'Codex CLI · 2026-03-11 · Other changes: 24 changes in 0.114.0 — Added
  an experimental code mode for more isolated coding workflows. (#13418)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e211efcbae278d58813d1637da28ff878fda2a04310fee09833ed1ba2f9b6574
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-11-b9c66b
  comparison: ''
  date: '2026-03-11'
  description: 'Codex CLI — 0.114.0: 24 other changes'
  evidence:
  - quote: Added an experimental code mode for more isolated coding workflows. (#13418)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: WebSocket app-server deployments now expose `GET /readyz` and `GET /healthz`
      on the same listener for easier health checks. (#13782)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: Added a config switch to disable bundled system skills entirely. (#13792)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13782 codex-rs/app-server: add health endpoints for --listen websocket
      server @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14055 fix(core) RequestPermissions + ApplyPatch @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14118 feat(approvals) RejectConfig for request_permissions @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13957 fix(protocol): preserve legacy workspace-write semantics @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14107 fix: keep permissions profiles forward compatible @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14152 Refactor tool output into trait implementations @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14163 sort plugins first in menu @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13418 Add code_mode experimental feature @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14157 Enforce single tool output type in codex handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14165 fix(core) default RejectConfig.request_permissions @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14167 Export tools module into code mode runner @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13792 feat: support disabling bundled system skills @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14000 Delay pending cleanup until task aborts @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#12296 Implemented thread-level atomic elicitation counter for stopwatch
      pausing @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13879 Stabilize incomplete SSE retry test @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14184 Fix unified exec test output assertion @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14002 Stabilize websocket test server binding @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13939 Stabilize app-server notify initialize test @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#13901 Log ChatGPT user ID for feedback tags @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14229 Reuse McpToolOutput in McpHandler @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  - quote: '#14125 Mark incomplete resumed turns interrupted when idle @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.114.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 24-other-changes-in-rust-v0-114-0
  source_release: codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8
  source_type: github_releases
  theme: uncategorized
  title: 24 other changes in rust-v0.114.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8|codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8]]'
source_type: github_releases
theme: uncategorized
title: 24 other changes in rust-v0.114.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 other changes in rust-v0.114.0

**Codex CLI** · 2026-03-11 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.114.0) · from [[Releases/Codex CLI/codex-cli-2026-03-11-rust-v0-114-0-github-295424880-aad043c8|0.114.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an experimental code mode for more isolated coding workflows. (#13418)

> WebSocket app-server deployments now expose `GET /readyz` and `GET /healthz` on the same listener for easier health checks. (#13782)

> Added a config switch to disable bundled system skills entirely. (#13792)

> #13782 codex-rs/app-server: add health endpoints for --listen websocket server @maxj-oai

> #14055 fix(core) RequestPermissions + ApplyPatch @dylan-hurd-oai

> #14118 feat(approvals) RejectConfig for request_permissions @dylan-hurd-oai

> #13957 fix(protocol): preserve legacy workspace-write semantics @viyatb-oai

> #14107 fix: keep permissions profiles forward compatible @viyatb-oai

> #14152 Refactor tool output into trait implementations @pakrym-oai

> #14163 sort plugins first in menu @sayan-oai

> #13418 Add code_mode experimental feature @pakrym-oai

> #14157 Enforce single tool output type in codex handlers @pakrym-oai

> #14165 fix(core) default RejectConfig.request_permissions @dylan-hurd-oai

> #14167 Export tools module into code mode runner @pakrym-oai

> #13792 feat: support disabling bundled system skills @xl-openai

> #14000 Delay pending cleanup until task aborts @aibrahim-oai

> #12296 Implemented thread-level atomic elicitation counter for stopwatch pausing @cconger

> #13879 Stabilize incomplete SSE retry test @aibrahim-oai

> #14184 Fix unified exec test output assertion @aibrahim-oai

> #14002 Stabilize websocket test server binding @aibrahim-oai

> #13939 Stabilize app-server notify initialize test @aibrahim-oai

> #13901 Log ChatGPT user ID for feedback tags @etraut-openai

> #14229 Reuse McpToolOutput in McpHandler @pakrym-oai

> #14125 Mark incomplete resumed turns interrupted when idle @guinness-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.114.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-11-14003-stabilize-split-pty-output-on-windows-aibrahim-oai|♯14003 Stabilize split PTY output on Windows @aibrahim-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-11-3-developer-workflow-changes-in-rust-v0-114-0|3 Developer Workflow changes in rust-v0.114.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-11-2-safety-and-privacy-changes-in-rust-v0-114-0|2 Safety and Privacy changes in rust-v0.114.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-11-14136-fix-core-use-dedicated-types-for-responsesapi-web-search-tool-config-owenl|♯14136 fix(core): use dedicated types for responsesapi web search tool config @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-11-14135-tui-only-show-fast-status-for-gpt-5-4-pash-openai|♯14135 tui: only show fast status for gpt-5.4 @pash-openai]] · Model Support
- [[Changes/Codex CLI/2026-03-11-2-context-window-changes-in-rust-v0-114-0|2 Context Window changes in rust-v0.114.0]] · Context Window
- [[Changes/Codex CLI/2026-03-11-8-apps-and-integrations-changes-in-rust-v0-114-0|8 Apps and Integrations changes in rust-v0.114.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-11-b9c66b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-11-24-other-changes-in-rust-v0-114-0.md%0ACard%20ID%3A%20codex-cli-2026-03-11-b9c66b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.114.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->