---
card_id: codex-cli-2026-06-15-0c14d3
date: '2026-06-15'
description: 'Codex CLI · 2026-06-15 · Other changes: 121 changes in 0.140.0 — `/goal`
  now preserves oversized text, large pasted blocks, and image attachments, including
  in…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9d4581f21bbef3ef1fd042472301b9863ff933d12672c6c1b9fadf54ac1f63ab
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-15-0c14d3
  comparison: ''
  date: '2026-06-15'
  description: 'Codex CLI — 0.140.0: 121 other changes'
  evidence:
  - quote: '`/goal` now preserves oversized text, large pasted blocks, and image attachments,
      including in remote app-server sessions. (#27508, #27509, #27510)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: Typing `@` now opens the unified mentions menu for files, plugins, and
      skills by default. (#27499)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: 'Corrupted SQLite state databases are now backed up and rebuilt automatically
      from rollout data, including malformed database-directory cases. (#26859, #27719)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: Prevented `/review` from crashing when `Esc` is pressed with queued guidance,
      while preserving that guidance when the review is canceled. (#22879)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: 'Persisted “Don’t remind me” update dismissals reliably and cleared stale
      running-hook indicators after completed turns. (#27619, #27783)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: Non-TTY background commands can now be interrupted with Ctrl-C while preserving
      their final output and exit status. (#26734)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26420 Avoid no-op backfill state writes @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27031 Avoid rereading rollout history during cold resume @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#22879 fix: Prevent /review crash when entering Esc on steer message @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26835 [codex] Test extension API contracts @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27063 [codex-analytics] add extensible feature thread sources @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#22685 Add SOCKS5 TCP MITM coverage @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26711 Reduce TUI legacy core dependencies @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27110 [1/6] Add Python goal routing foundation @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26830 [codex] Characterize global instruction lifecycle @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26734 [codex] Handle Ctrl-C for non-TTY unified exec @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27116 Stop mirroring Codex user input into realtime @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27111 [2/6] Add private Python goal operations @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#25147 [codex] Retry streamable HTTP initialize failures @ssetty-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27094 Add spans to build_tool_router @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27078 [codex-analytics] emit goal lifecycle analytics @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27107 Add spans to run_turn @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27383 Remove async-trait from extension contributors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27264 [codex] Store compact window id in rollout @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27280 [codex] add io PathUri native conversion APIs @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27315 [codex] link Windows releases with LLD @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27276 Reduce archive rollout lookup CPU @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27299 [codex] Outline ToolExecutor handler bodies @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27391 Index visible thread list ordering @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27407 Fix compressed rollout search path matching @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27304 [codex] Remove async_trait from ToolExecutor @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#25018 Add app-server `thread/delete` API @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26859 fix: Auto-recover from corrupted sqlite databases @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27421 [codex] Raise app-server recursion limit @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27062 [codex] Retry transient Guardian review failures @kbazzi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27439 feat: make ThreadStore available on ThreadExtensionDependencies
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27343 Guard core test subprocess cleanup @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27321 [codex] Move release platform rules into bazel package @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27312 [codex] reuse release artifacts for npm staging @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27319 Forward standalone assistant output to realtime @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27057 [codex] Add reusable OTEL gauge instruments @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27392 [codex-analytics] emit internally started turn events @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27322 [codex] Preserve build-script dependencies in rules_rs annotations
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27484 Remove TUI legacy core test_support dependencies @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27476 Add session delete commands in CLI and TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27247 core: resize all history images behind a feature flag @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27487 Trim TUI legacy telemetry and migration dependencies @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27526 tools: simplify default tool search text @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27443 feat: add Bedrock API key as a managed auth mode @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27246 core: strip image detail from Responses Lite requests @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27520 [codex] Compact when comp_hash changes @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27266 image: preserve metadata when resizing prompt images @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27356 Use generic search metadata for dynamic tools @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#26513 [codex] Tune cloud config cache intervals @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27403 skills: cache remote catalog failures per thread @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27388 skills: expose remote skill resource tools @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27585 nit: cap error @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27404 test: cover referenced backend skill reads without an executor
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27591 skills: render catalog locators by authority @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27413 skills: decouple the skills extension from core @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27527 [codex] publish npm packages concurrently @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27528 [codex] publish DotSlash alongside npm @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27529 [codex] download only release artifacts @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27417 Print TUI session info on fatal exits @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27507 lint: allow self-documenting builder arguments @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27454 [codex] add cross-platform filesystem adapter coverage @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27415 [codex] Surface runtime warnings in codex exec @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27639 [codex] revert concurrent npm publishing @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27646 feat: disable orchestrator skills for now @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27323 [codex] Provide ARM64 MinGW powl compatibility support @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27433 [codex] remove EnvironmentPathRef @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27424 [codex] migrate ExecutorFileSystem paths to PathUri @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27101 [codex] Load user instructions through an injected provider @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27122 core: Consolidate Responses API Codex metadata @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27450 [codex-rs] enforce PAT workspace restrictions @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27653 [codex] migrate exec-server filesystem protocol to PathUri @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27700 Remove fs/join and fs/parent from exec-server protocol @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27318 [codex] Move persistence policy application into ThreadStore @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27498 Route image extension reads through turn environments v2 @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27623 Add spans to turn lifecycle gaps @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27711 Fix image extension PathUri conversion @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27475 [codex] Remove async_trait from first-party code @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27719 fix: Recover from sqlite directory being a file @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27715 ci(v8): gate Windows source builds on relevant changes @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27702 [codex] parallelize release code generation @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27508 [1 of 3] Support long raw TUI goal objectives @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27256 Add request_user_input auto-resolution window contract @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27724 code-mode standalone: extract protocol and add host crate @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27778 Translate non-English issues @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27732 [code-mode] Reject remote image URLs from output helpers @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27703 [codex] restore source-specific import copy @stefanstokic-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27879 fix: serialize auth environment tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27791 Reject transcript backtrack in side conversations @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27075 [ez][codex-rs] Support approvals reviewer in app defaults @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27783 Persist update dismissal without cache @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27720 realtime: add AVAS architecture override @bakks'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27919 chore: prompt MAv2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27816 sandboxing: migrate cwd inputs to PathUri @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27913 [codex] unify apply patch parsing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27927 [codex] Add size to internal filesystem metadata @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27504 feat: add secret auth storage configuration @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27535 feat: add auth-specific encrypted secret namespaces @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27939 [codex] Add crate API surface review rule @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27926 [codex] Align implicit skill reads with parser @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27539 feat: use encrypted local secrets for CLI auth @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27076 Warn for structured feature toggles @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27936 [codex] add roles to realtime append text @agamble-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27509 [2 of 3] Support long pasted text in TUI goals @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27109 Add Guardian catalog diagnostics metadata @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27855 [codex] parallelize Windows compression @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27499 Promote TUI unified mentions in composer to default mentions feature
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27972 [codex] Let generic test turns inherit their environment @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27856 [codex] package Windows symbols in parallel @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27976 [codex] make PathUri::from_abs_path infallible @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27854 [codex] parallelize Windows package archives @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27853 [codex] stage npm packages concurrently @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27510 [3 of 3] Support images in TUI goals @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27964 [codex] Add hermetic Wine test support @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27937 [codex] Add hermetic Wine exec-server test @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#27996 [codex] Send request-scoped turn state over WebSocket @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  - quote: '#28002 [codex] Send turn state through compact requests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.140.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 121-other-changes-in-rust-v0-140-0
  source_release: codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb
  source_type: github_releases
  theme: uncategorized
  title: 121 other changes in rust-v0.140.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb]]'
source_type: github_releases
theme: uncategorized
title: 121 other changes in rust-v0.140.0
type: change
---

<!-- chronolog:begin region="header" -->
# 121 other changes in rust-v0.140.0

**Codex CLI** · 2026-06-15 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.140.0) · from [[Releases/Codex CLI/codex-cli-2026-06-15-rust-v0-140-0-github-339797498-eb64f8cb|0.140.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/goal` now preserves oversized text, large pasted blocks, and image attachments, including in remote app-server sessions. (#27508, #27509, #27510)

> Typing `@` now opens the unified mentions menu for files, plugins, and skills by default. (#27499)

> Corrupted SQLite state databases are now backed up and rebuilt automatically from rollout data, including malformed database-directory cases. (#26859, #27719)

> Prevented `/review` from crashing when `Esc` is pressed with queued guidance, while preserving that guidance when the review is canceled. (#22879)

> Persisted “Don’t remind me” update dismissals reliably and cleared stale running-hook indicators after completed turns. (#27619, #27783)

> Non-TTY background commands can now be interrupted with Ctrl-C while preserving their final output and exit status. (#26734)

> #26420 Avoid no-op backfill state writes @zanie-oai

> #27031 Avoid rereading rollout history during cold resume @zanie-oai

> #22879 fix: Prevent /review crash when entering Esc on steer message @canvrno-oai

> #26835 [codex] Test extension API contracts @anp-oai

> #27063 [codex-analytics] add extensible feature thread sources @marksteinbrick-oai

> #22685 Add SOCKS5 TCP MITM coverage @winston-openai

> #26711 Reduce TUI legacy core dependencies @etraut-openai

> #27110 [1/6] Add Python goal routing foundation @aibrahim-oai

> #26830 [codex] Characterize global instruction lifecycle @anp-oai

> #26734 [codex] Handle Ctrl-C for non-TTY unified exec @pakrym-oai

> #27116 Stop mirroring Codex user input into realtime @guinness-oai

> #27111 [2/6] Add private Python goal operations @aibrahim-oai

> #25147 [codex] Retry streamable HTTP initialize failures @ssetty-oai

> #27094 Add spans to build_tool_router @mchen-oai

> #27078 [codex-analytics] emit goal lifecycle analytics @marksteinbrick-oai

> #27107 Add spans to run_turn @mchen-oai

> #27383 Remove async-trait from extension contributors @jif-oai

> #27264 [codex] Store compact window id in rollout @pakrym-oai

> #27280 [codex] add io PathUri native conversion APIs @anp-oai

> #27315 [codex] link Windows releases with LLD @tamird

> #27276 Reduce archive rollout lookup CPU @etraut-openai

> #27299 [codex] Outline ToolExecutor handler bodies @anp-oai

> #27391 Index visible thread list ordering @zanie-oai

> #27407 Fix compressed rollout search path matching @jif-oai

> #27304 [codex] Remove async_trait from ToolExecutor @anp-oai

> #25018 Add app-server `thread/delete` API @etraut-openai

> #26859 fix: Auto-recover from corrupted sqlite databases @ddr-oai

> #27421 [codex] Raise app-server recursion limit @anp-oai

> #27062 [codex] Retry transient Guardian review failures @kbazzi

> #27439 feat: make ThreadStore available on ThreadExtensionDependencies @bolinfest

> #27343 Guard core test subprocess cleanup @etraut-openai

> #27321 [codex] Move release platform rules into bazel package @anp-oai

> #27312 [codex] reuse release artifacts for npm staging @tamird

> #27319 Forward standalone assistant output to realtime @guinness-oai

> #27057 [codex] Add reusable OTEL gauge instruments @richardopenai

> #27392 [codex-analytics] emit internally started turn events @marksteinbrick-oai

> #27322 [codex] Preserve build-script dependencies in rules_rs annotations @anp-oai

> #27484 Remove TUI legacy core test_support dependencies @etraut-openai

> #27476 Add session delete commands in CLI and TUI @etraut-openai

> #27247 core: resize all history images behind a feature flag @fjord-oai

> #27487 Trim TUI legacy telemetry and migration dependencies @etraut-openai

> #27526 tools: simplify default tool search text @sayan-oai

> #27443 feat: add Bedrock API key as a managed auth mode @celia-oai

> #27246 core: strip image detail from Responses Lite requests @fjord-oai

> #27520 [codex] Compact when comp_hash changes @aibrahim-oai

> #27266 image: preserve metadata when resizing prompt images @fjord-oai

> #27356 Use generic search metadata for dynamic tools @sayan-oai

> #26513 [codex] Tune cloud config cache intervals @alexsong-oai

> #27403 skills: cache remote catalog failures per thread @jif-oai

> #27388 skills: expose remote skill resource tools @jif-oai

> #27585 nit: cap error @jif-oai

> #27404 test: cover referenced backend skill reads without an executor @jif-oai

> #27591 skills: render catalog locators by authority @jif-oai

> #27413 skills: decouple the skills extension from core @jif-oai

> #27527 [codex] publish npm packages concurrently @tamird

> #27528 [codex] publish DotSlash alongside npm @tamird

> #27529 [codex] download only release artifacts @tamird

> #27417 Print TUI session info on fatal exits @etraut-openai

> #27507 lint: allow self-documenting builder arguments @anp-oai

> #27454 [codex] add cross-platform filesystem adapter coverage @anp-oai

> #27415 [codex] Surface runtime warnings in codex exec @anp-oai

> #27639 [codex] revert concurrent npm publishing @tamird

> #27646 feat: disable orchestrator skills for now @jif-oai

> #27323 [codex] Provide ARM64 MinGW powl compatibility support @anp-oai

> #27433 [codex] remove EnvironmentPathRef @anp-oai

> #27424 [codex] migrate ExecutorFileSystem paths to PathUri @anp-oai

> #27101 [codex] Load user instructions through an injected provider @anp-oai

> #27122 core: Consolidate Responses API Codex metadata @owenlin0

> #27450 [codex-rs] enforce PAT workspace restrictions @cooper-oai

> #27653 [codex] migrate exec-server filesystem protocol to PathUri @anp-oai

> #27700 Remove fs/join and fs/parent from exec-server protocol @anp-oai

> #27318 [codex] Move persistence policy application into ThreadStore @wiltzius-openai

> #27498 Route image extension reads through turn environments v2 @won-openai

> #27623 Add spans to turn lifecycle gaps @mchen-oai

> #27711 Fix image extension PathUri conversion @anp-oai

> #27475 [codex] Remove async_trait from first-party code @anp-oai

> #27719 fix: Recover from sqlite directory being a file @ddr-oai

> #27715 ci(v8): gate Windows source builds on relevant changes @cconger

> #27702 [codex] parallelize release code generation @tamird

> #27508 [1 of 3] Support long raw TUI goal objectives @etraut-openai

> #27256 Add request_user_input auto-resolution window contract @shijie-oai

> #27724 code-mode standalone: extract protocol and add host crate @cconger

> #27778 Translate non-English issues @etraut-openai

> #27732 [code-mode] Reject remote image URLs from output helpers @rka-oai

> #27703 [codex] restore source-specific import copy @stefanstokic-oai

> #27879 fix: serialize auth environment tests @jif-oai

> #27791 Reject transcript backtrack in side conversations @etraut-openai

> #27075 [ez][codex-rs] Support approvals reviewer in app defaults @zamoshchin-openai

> #27783 Persist update dismissal without cache @etraut-openai

> #27720 realtime: add AVAS architecture override @bakks

> #27919 chore: prompt MAv2 @jif-oai

> #27816 sandboxing: migrate cwd inputs to PathUri @anp-oai

> #27913 [codex] unify apply patch parsing @pakrym-oai

> #27927 [codex] Add size to internal filesystem metadata @pakrym-oai

> #27504 feat: add secret auth storage configuration @celia-oai

> #27535 feat: add auth-specific encrypted secret namespaces @celia-oai

> #27939 [codex] Add crate API surface review rule @pakrym-oai

> #27926 [codex] Align implicit skill reads with parser @alexsong-oai

> #27539 feat: use encrypted local secrets for CLI auth @celia-oai

> #27076 Warn for structured feature toggles @canvrno-oai

> #27936 [codex] add roles to realtime append text @agamble-oai

> #27509 [2 of 3] Support long pasted text in TUI goals @etraut-openai

> #27109 Add Guardian catalog diagnostics metadata @won-openai

> #27855 [codex] parallelize Windows compression @tamird

> #27499 Promote TUI unified mentions in composer to default mentions feature @canvrno-oai

> #27972 [codex] Let generic test turns inherit their environment @pakrym-oai

> #27856 [codex] package Windows symbols in parallel @tamird

> #27976 [codex] make PathUri::from_abs_path infallible @anp-oai

> #27854 [codex] parallelize Windows package archives @tamird

> #27853 [codex] stage npm packages concurrently @tamird

> #27510 [3 of 3] Support images in TUI goals @etraut-openai

> #27964 [codex] Add hermetic Wine test support @anp-oai

> #27937 [codex] Add hermetic Wine exec-server test @anp-oai

> #27996 [codex] Send request-scoped turn state over WebSocket @aibrahim-oai

> #28002 [codex] Send turn state through compact requests @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.140.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-15-27245-image-add-shared-data-url-preparation-utilities-fjord-oai|♯27245 image: add shared data URL preparation utilities @fjord-oai]] · Collaboration
- [[Changes/Codex CLI/2026-06-15-27501-codex-expand-hosted-web-search-citation-guidance-yuning-oai|♯27501 codex Expand hosted web search citation guidance @yuning-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-15-3-reliability-and-performance-changes-in-rust-v0-140-0|3 Reliability and Performance changes in rust-v0.140.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-15-2-editor-experience-changes-in-rust-v0-140-0|2 Editor Experience changes in rust-v0.140.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-15-7-context-window-changes-in-rust-v0-140-0|7 Context Window changes in rust-v0.140.0]] · Context Window
- [[Changes/Codex CLI/2026-06-15-added-import-for-selectively-importing-setup-project-configuration-and-recent-ch|Added /import for selectively importing setup, project configuration, and recent…]] · Interface Experience
- [[Changes/Codex CLI/2026-06-15-27920-handle-standalone-image-generation-failures-as-terminal-items-won-openai|♯27920 Handle standalone image generation failures as terminal items @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-06-15-27129-feat-use-provider-defaults-for-memory-models-celia-oai|♯27129 feat: use provider defaults for memory models @celia-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-15-11-agent-mode-changes-in-rust-v0-140-0|11 Agent Mode changes in rust-v0.140.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-15-3-interface-experience-changes-in-rust-v0-140-0|3 Interface Experience changes in rust-v0.140.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-15-35-apps-and-integrations-changes-in-rust-v0-140-0|35 Apps and Integrations changes in rust-v0.140.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-15-5-account-and-access-changes-in-rust-v0-140-0|5 Account and Access changes in rust-v0.140.0]] · Account and Access
- [[Changes/Codex CLI/2026-06-15-4-model-support-changes-in-rust-v0-140-0|4 Model Support changes in rust-v0.140.0]] · Model Support
- [[Changes/Codex CLI/2026-06-15-clarified-contributor-guidance-around-keeping-crate-apis-narrow-and-supporting-l|Clarified contributor guidance around keeping crate APIs narrow and supporting…]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-15-27490-remove-tui-legacy-windows-sandbox-dependency-etraut-openai|♯27490 Remove TUI legacy Windows sandbox dependency @etraut-openai]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-15-6-developer-workflow-changes-in-rust-v0-140-0|6 Developer Workflow changes in rust-v0.140.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-15-2-voice-and-audio-changes-in-rust-v0-140-0|2 Voice and Audio changes in rust-v0.140.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-06-15-added-usage-views-for-daily-weekly-and-cumulative-account-token-activity-27925|Added /usage views for daily, weekly, and cumulative account token activity]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-15-0c14d3&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-15-121-other-changes-in-rust-v0-140-0.md%0ACard%20ID%3A%20codex-cli-2026-06-15-0c14d3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.140.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->