---
card_id: codex-cli-2026-02-12-e031bf
date: '2026-02-12'
description: 'Codex CLI · 2026-02-12 · Other changes: 59 changes in 0.100.0 — Added
  an experimental, feature-gated JavaScript REPL runtime (`js_repl`) that can persist
  state…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bbff2a4c7bbf1273b35e2c30d9bc3b475c432d97b600a154e8824dd055e428e0
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-12-e031bf
  comparison: ''
  date: '2026-02-12'
  description: 'Codex CLI — 0.100.0: 59 other changes'
  evidence:
  - quote: Added an experimental, feature-gated JavaScript REPL runtime (`js_repl`)
      that can persist state across tool calls, with optional runtime path overrides.
      (#10674)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: Added support for multiple simultaneous rate limits across the protocol,
      backend client, and TUI status surfaces. (#11260)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: 'Reintroduced app-server websocket transport with a split inbound/outbound
      architecture, plus connection-aware thread resume subscriptions. (#11370, #11474)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: Added JS REPL documentation and config/schema guidance for enabling and
      configuring the feature. (#10674)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: Updated app-server websocket transport documentation in the app-server
      README. (#11370)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: Split `codex-common` into focused `codex-utils-*` crates to simplify dependency
      boundaries across Rust workspace components. (#11422)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: Prevented GitHub release asset upload collisions by excluding duplicate
      `cargo-timing.html` artifacts. (#11564)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11383 Do not resend output items in incremental websockets connections
      @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11246 chore: persist turn_id in rollout session and make turn_id uuid
      based @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11260 feat: support multiple rate limits @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11405 Remove `test-support` feature from `codex-core` and replace it
      with explicit test toggles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11428 fix: flaky test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11429 feat: improve thread listing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11422 feat: split codex-common into smaller utils crates @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11305 Cache cloud requirements @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11420 chore: rename disable_websockets -> websockets_disabled @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11402 Do not attempt to append after response.completed @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11389 Extract `codex-config` from `codex-core` @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11370 Reapply "Add app-server transport layer with websocket support"
      @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11470 feat: panic if Constrained<WebSearchMode> does not support Disabled
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11475 feat: remove "cargo check individual crates" from CI @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11414 Linkify feedback link @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11480 chore: update mem prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11485 fix: Constrained import @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#10674 Add feature-gated freeform js_repl core runtime @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11419 refactor: codex app-server ThreadState @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11413 Pump pings @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11488 feat: use more powerful machines for building Windows releases
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11494 Increased file watcher debounce duration from 1s to 10s @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11335 Add AfterToolUse hook @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11290 chore(tui) Simplify /status Permissions @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11474 app-server: thread resume subscriptions @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11277 Added seatbelt policy rule to allow os.cpus @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11506 chore: inject originator/residency headers to ws client @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11513 feat: try to fix bugs I saw in the wild in the resource parsing
      logic @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11519 Use slug in tui @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11522 fix: add --test_verbose_timeout_warnings to bazel.yml @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11526 fix: remove errant Cargo.lock files @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11532 fix compilation @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11531 Teach codex to test itself @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11540 ci: remove actions/cache from rust release workflows @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11542 ci(windows): use DotSlash for zstd in rust-release-windows @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11545 fix: make project_doc skill-render tests deterministic @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11543 ci: capture cargo timings in Rust CI and release workflows @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11539 Bump rmcp to 0.15 @gpeal'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11548 Hide the first websocket retry @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11556 Fix rust-release failures in musl linking and release asset upload
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11558 Handle response.incomplete @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11557 fix: stop inheriting rate-limit limit_name @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11564 rust-release: exclude cargo-timing.html from release assets @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11448 Fix test flake @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11569 feat: mem slash commands @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11573 Fix flaky pre_sampling_compact switch test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11571 feat: mem drop cot @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11572 Ensure list_threads drops stale rollout files @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11575 fix: db stuff mem @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11581 nit: upgrade DB version @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11590 chore: clean consts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  - quote: '#11600 feat: add sanitizer to redact secrets @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.100.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 59-other-changes-in-rust-v0-100-0
  source_release: codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6
  source_type: github_releases
  theme: uncategorized
  title: 59 other changes in rust-v0.100.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6|codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6]]'
source_type: github_releases
theme: uncategorized
title: 59 other changes in rust-v0.100.0
type: change
---

<!-- chronolog:begin region="header" -->
# 59 other changes in rust-v0.100.0

**Codex CLI** · 2026-02-12 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.100.0) · from [[Releases/Codex CLI/codex-cli-2026-02-12-rust-v0-100-0-github-285810603-4852bda6|0.100.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added an experimental, feature-gated JavaScript REPL runtime (`js_repl`) that can persist state across tool calls, with optional runtime path overrides. (#10674)

> Added support for multiple simultaneous rate limits across the protocol, backend client, and TUI status surfaces. (#11260)

> Reintroduced app-server websocket transport with a split inbound/outbound architecture, plus connection-aware thread resume subscriptions. (#11370, #11474)

> Added JS REPL documentation and config/schema guidance for enabling and configuring the feature. (#10674)

> Updated app-server websocket transport documentation in the app-server README. (#11370)

> Split `codex-common` into focused `codex-utils-*` crates to simplify dependency boundaries across Rust workspace components. (#11422)

> Prevented GitHub release asset upload collisions by excluding duplicate `cargo-timing.html` artifacts. (#11564)

> #11383 Do not resend output items in incremental websockets connections @pakrym-oai

> #11246 chore: persist turn_id in rollout session and make turn_id uuid based @celia-oai

> #11260 feat: support multiple rate limits @xl-openai

> #11405 Remove `test-support` feature from `codex-core` and replace it with explicit test toggles @bolinfest

> #11428 fix: flaky test @jif-oai

> #11429 feat: improve thread listing @jif-oai

> #11422 feat: split codex-common into smaller utils crates @bolinfest

> #11305 Cache cloud requirements @gt-oai

> #11420 chore: rename disable_websockets -> websockets_disabled @sayan-oai

> #11402 Do not attempt to append after response.completed @pakrym-oai

> #11389 Extract `codex-config` from `codex-core` @bolinfest

> #11370 Reapply "Add app-server transport layer with websocket support" @maxj-oai

> #11470 feat: panic if Constrained\<WebSearchMode> does not support Disabled @bolinfest

> #11475 feat: remove "cargo check individual crates" from CI @bolinfest

> #11414 Linkify feedback link @pakrym-oai

> #11480 chore: update mem prompt @jif-oai

> #11485 fix: Constrained import @owenlin0

> #10674 Add feature-gated freeform js_repl core runtime @fjord-oai

> #11419 refactor: codex app-server ThreadState @maxj-oai

> #11413 Pump pings @pakrym-oai

> #11488 feat: use more powerful machines for building Windows releases @bolinfest

> #11494 Increased file watcher debounce duration from 1s to 10s @etraut-openai

> #11335 Add AfterToolUse hook @gt-oai

> #11290 chore(tui) Simplify /status Permissions @dylan-hurd-oai

> #11474 app-server: thread resume subscriptions @maxj-oai

> #11277 Added seatbelt policy rule to allow os.cpus @etraut-openai

> #11506 chore: inject originator/residency headers to ws client @apanasenko-oai

> #11513 feat: try to fix bugs I saw in the wild in the resource parsing logic @bolinfest

> #11519 Use slug in tui @pakrym-oai

> #11522 fix: add --test_verbose_timeout_warnings to bazel.yml @bolinfest

> #11526 fix: remove errant Cargo.lock files @bolinfest

> #11532 fix compilation @sayan-oai

> #11531 Teach codex to test itself @pakrym-oai

> #11540 ci: remove actions/cache from rust release workflows @bolinfest

> #11542 ci(windows): use DotSlash for zstd in rust-release-windows @bolinfest

> #11545 fix: make project_doc skill-render tests deterministic @bolinfest

> #11543 ci: capture cargo timings in Rust CI and release workflows @bolinfest

> #11539 Bump rmcp to 0.15 @gpeal

> #11548 Hide the first websocket retry @pakrym-oai

> #11556 Fix rust-release failures in musl linking and release asset upload @bolinfest

> #11558 Handle response.incomplete @pakrym-oai

> #11557 fix: stop inheriting rate-limit limit_name @xl-openai

> #11564 rust-release: exclude cargo-timing.html from release assets @bolinfest

> #11448 Fix test flake @gt-oai

> #11569 feat: mem slash commands @jif-oai

> #11573 Fix flaky pre_sampling_compact switch test @jif-oai

> #11571 feat: mem drop cot @jif-oai

> #11572 Ensure list_threads drops stale rollout files @jif-oai

> #11575 fix: db stuff mem @jif-oai

> #11581 nit: upgrade DB version @jif-oai

> #11590 chore: clean consts @jif-oai

> #11600 feat: add sanitizer to redact secrets @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.100.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-12-11-memory-and-personalization-changes-in-rust-v0-100-0|11 Memory and Personalization changes in rust-v0.100.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-12-11412-tui-show-non-file-layer-content-in-debug-config-bolinfest|♯11412 tui: show non-file layer content in /debug-config @bolinfest]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-12-11521-test-app-server-stabilize-app-list-thread-feature-flag-test-by-using-file|♯11521 test(app-server): stabilize app/list thread feature-flag test by using…]] · Account and Access
- [[Changes/Codex CLI/2026-02-12-3-context-window-changes-in-rust-v0-100-0|3 Context Window changes in rust-v0.100.0]] · Context Window
- [[Changes/Codex CLI/2026-02-12-improved-websocket-session-stability-by-continuing-ping-handling-when-idle-and-s|Improved websocket session stability by continuing ping handling when idle…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-12-2-agent-mode-changes-in-rust-v0-100-0|2 Agent Mode changes in rust-v0.100.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-12-4-mobile-and-desktop-changes-in-rust-v0-100-0|4 Mobile and Desktop changes in rust-v0.100.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-12-5-safety-and-privacy-changes-in-rust-v0-100-0|5 Safety and Privacy changes in rust-v0.100.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-12-4-model-support-changes-in-rust-v0-100-0|4 Model Support changes in rust-v0.100.0]] · Model Support
- [[Changes/Codex CLI/2026-02-12-reduced-repeated-skill-parse-error-spam-during-active-edits-by-increasing-file-w|Reduced repeated skill parse-error spam during active edits by increasing…]] · Editor Experience
- [[Changes/Codex CLI/2026-02-12-5-apps-and-integrations-changes-in-rust-v0-100-0|5 Apps and Integrations changes in rust-v0.100.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-12-e031bf&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-12-59-other-changes-in-rust-v0-100-0.md%0ACard%20ID%3A%20codex-cli-2026-02-12-e031bf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.100.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->