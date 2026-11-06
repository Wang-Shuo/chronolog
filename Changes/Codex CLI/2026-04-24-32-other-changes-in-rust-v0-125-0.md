---
card_id: codex-cli-2026-04-24-a4477b
date: '2026-04-24'
description: 'Codex CLI · 2026-04-24 · Other changes: 32 changes in 0.125.0 — Interrupting
  `/review` and exiting the TUI no longer leaves the interface wedged on delegate…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1f2a6654455a8c9fb5fca491b6d29cc149a55ba6214b3f10bb30db05c034eaf2
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-24-a4477b
  comparison: ''
  date: '2026-04-24'
  description: 'Codex CLI — 0.125.0: 32 other changes'
  evidence:
  - quote: Interrupting `/review` and exiting the TUI no longer leaves the interface
      wedged on delegate startup or unsubscribe. (#18921)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: 'Exec-server no longer drops buffered output after process exit and now
      waits correctly for stream closure. (#18946, #19130)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: App-server now respects explicitly untrusted project config instead of
      auto-persisting trust. (#18626)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: WebSocket app-server clients are less likely to disconnect during bursts
      of turn and tool-output notifications. (#19246)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19130 exec-server: wait for close after observed exit @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18892 Add remote thread config loader protos @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19014 Add excludeTurns parameter to thread/resume and thread/fork @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18882 [codex] Route live thread writes through ThreadStore @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19008 [codex] Implement remote thread store methods @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18626 Respect explicit untrusted project config @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18255 app-server: add Unix socket transport @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19099 Move marketplace add/remove and startup sync out of core. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18908 Add remote thread config endpoint @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18878 [rollout_trace] Trace tool and code-mode boundaries @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18946 fix(exec-server): retain output until streams close @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19074 Add app-server marketplace upgrade RPC @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19178 Stabilize approvals popup disabled-row test @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18921 Fix /review interrupt and TUI exit wedges @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18288 tests: isolate approval fixtures from host rules @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19044 guide Windows to use -WindowStyle Hidden for Start-Process calls
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19214 do not attempt ACLs on installed codex dir @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19161 ci: derive cache-stable Windows Bazel PATH @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18811 refactor: route Codex auth through AuthProvider @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19246 Increase app-server WebSocket outbound buffer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19048 feat: expose AWS account state from account/read @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18897 Add sticky environment API and thread state @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19206 app-server: persist device key bindings in sqlite @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19231 permissions: make profiles represent enforcement @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19232 ci: reuse Bazel CI startup for target-discovery queries @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19292 Reject unsupported js_repl image MIME types @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19247 chore: apply truncation policy to unified_exec @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19350 fix alpha build @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 32-other-changes-in-rust-v0-125-0
  source_release: codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c
  source_type: github_releases
  theme: uncategorized
  title: 32 other changes in rust-v0.125.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c]]'
source_type: github_releases
theme: uncategorized
title: 32 other changes in rust-v0.125.0
type: change
---

<!-- chronolog:begin region="header" -->
# 32 other changes in rust-v0.125.0

**Codex CLI** · 2026-04-24 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.125.0) · from [[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|0.125.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Interrupting `/review` and exiting the TUI no longer leaves the interface wedged on delegate startup or unsubscribe. (#18921)

> Exec-server no longer drops buffered output after process exit and now waits correctly for stream closure. (#18946, #19130)

> App-server now respects explicitly untrusted project config instead of auto-persisting trust. (#18626)

> WebSocket app-server clients are less likely to disconnect during bursts of turn and tool-output notifications. (#19246)

> #19130 exec-server: wait for close after observed exit @jif-oai

> #18892 Add remote thread config loader protos @rasmusrygaard

> #19014 Add excludeTurns parameter to thread/resume and thread/fork @ddr-oai

> #18882 [codex] Route live thread writes through ThreadStore @wiltzius-openai

> #19008 [codex] Implement remote thread store methods @wiltzius-openai

> #18626 Respect explicit untrusted project config @etraut-openai

> #18255 app-server: add Unix socket transport @euroelessar

> #19099 Move marketplace add/remove and startup sync out of core. @xl-openai

> #18908 Add remote thread config endpoint @rasmusrygaard

> #18878 [rollout_trace] Trace tool and code-mode boundaries @cassirer-openai

> #18946 fix(exec-server): retain output until streams close @bolinfest

> #19074 Add app-server marketplace upgrade RPC @xli-oai

> #19178 Stabilize approvals popup disabled-row test @etraut-openai

> #18921 Fix /review interrupt and TUI exit wedges @etraut-openai

> #18288 tests: isolate approval fixtures from host rules @bolinfest

> #19044 guide Windows to use -WindowStyle Hidden for Start-Process calls @iceweasel-oai

> #19214 do not attempt ACLs on installed codex dir @iceweasel-oai

> #19161 ci: derive cache-stable Windows Bazel PATH @bolinfest

> #18811 refactor: route Codex auth through AuthProvider @efrazer-oai

> #19246 Increase app-server WebSocket outbound buffer @etraut-openai

> #19048 feat: expose AWS account state from account/read @celia-oai

> #18897 Add sticky environment API and thread state @starr-openai

> #19206 app-server: persist device key bindings in sqlite @euroelessar

> #19231 permissions: make profiles represent enforcement @bolinfest

> #19232 ci: reuse Bazel CI startup for target-discovery queries @bolinfest

> #19292 Reject unsupported js_repl image MIME types @etraut-openai

> #19247 chore: apply truncation policy to unified_exec @sayan-oai

> #19350 fix alpha build @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.125.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-24-5-agent-mode-changes-in-rust-v0-125-0|5 Agent Mode changes in rust-v0.125.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-24-9-safety-and-privacy-changes-in-rust-v0-125-0|9 Safety and Privacy changes in rust-v0.125.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-24-2-context-window-changes-in-rust-v0-125-0|2 Context Window changes in rust-v0.125.0]] · Context Window
- [[Changes/Codex CLI/2026-04-24-19167-ci-add-macos-keychain-entitlements-euroelessar|♯19167 ci: add macOS keychain entitlements @euroelessar]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-24-windows-bazel-ci-now-uses-a-stable-path-and-shared-query-startup-path-for-better|Windows Bazel CI now uses a stable PATH and shared query startup path for better…]] · Collaboration
- [[Changes/Codex CLI/2026-04-24-2-developer-workflow-changes-in-rust-v0-125-0|2 Developer Workflow changes in rust-v0.125.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-24-5-model-support-changes-in-rust-v0-125-0|5 Model Support changes in rust-v0.125.0]] · Model Support
- [[Changes/Codex CLI/2026-04-24-11-apps-and-integrations-changes-in-rust-v0-125-0|11 Apps and Integrations changes in rust-v0.125.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-24-a4477b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-24-32-other-changes-in-rust-v0-125-0.md%0ACard%20ID%3A%20codex-cli-2026-04-24-a4477b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.125.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->