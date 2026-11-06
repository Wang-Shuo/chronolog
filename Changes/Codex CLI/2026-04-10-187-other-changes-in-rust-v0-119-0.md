---
card_id: codex-cli-2026-04-10-b98528
date: '2026-04-10'
description: 'Codex CLI · 2026-04-10 · Other changes: 187 changes in 0.119.0 — `/resume`
  can now jump directly to a session by ID or name from the TUI (#17222).'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4bb5088f08dff3b44bfb92151880421c976922473f50b782badaf005f92c50f6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-10-b98528
  comparison: ''
  date: '2026-04-10'
  description: 'Codex CLI — 0.119.0: 187 other changes'
  evidence:
  - quote: '`/resume` can now jump directly to a session by ID or name from the TUI
      (#17222).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: Fast Mode no longer stays stuck on after `/fast off` in app-server-backed
      TUI sessions (#16833).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: Developer guidance for `argument_comment_lint` was updated to favor getting
      CI started instead of blocking on slow local lint runs (#16375).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: Obsolete `codex-cli` README content was removed to avoid stale setup guidance
      (#17096).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '`codex exec --help` now shows clearer usage and approval-mode wording
      (#16881, #16888).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: 'Rust CI and workspace guardrails were simplified by blocking new crate
      features and dropping routine `--all-features` runs (#16455, #16473).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: 'Core compile times were reduced by removing expensive async-trait expansion
      from hot tool/task abstractions (#16630, #16631).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: 'Bazel diagnostics and dependency wiring improved with compact execution
      logs, repository-cache persistence, remote downloader support, and several platform-specific
      build fixes (#16577, #16926, #16928, #16634, #16744).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16308 fix: one shot end of turn @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16238 fix: ma2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16317 chore: clean wait v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16318 nit: update aborted line @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15771 feat: fork pattern v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16322 fix: update fork boundaries computation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16324 chore: drop interrupt from send_message @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16345 fix: fix clippy issue caught by cargo but not bazel @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16184 Route TUI `/feedback` submission through the app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16330 feat: log db better maintenance @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15690 [codex-analytics] thread events @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16363 Fix PR babysitter review comment monitoring @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16356 Refactor external auth to use a single trait @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16366 Fix Windows external bearer refresh test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16353 ci: verify codex-rs Cargo manifests inherit workspace settings
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16361 Refactor chatwidget tests into topical modules @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16201 Fix stale /status rate limits in active TUI sessions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16351 ci: sync Bazel clippy lints and fix uncovered violations @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16378 fix: suppress status card expect_used warnings after #16351 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16409 Use message string in v2 send_message @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16419 Use message string in v2 assign_task @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16425 nit: update wait v2 desc @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16426 chore: interrupted as state @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16427 nit: deny field v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16433 chore: drop log DB @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16434 feat: auto vaccum state DB @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16449 fix: remove unused import @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15772 Make fuzzy file search case insensitive @meyers-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16455 ci: block new workspace crate features @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16456 cloud-tasks: split the mock client out of cloud-tasks-client @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16379 Extract tool config into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16469 otel: remove the last workspace crate feature @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16471 Extract tool spec helpers into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16473 ci: stop running rust CI with --all-features @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16477 Extract tool discovery helpers into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16448 fix(guardian): make GuardianAssessmentEvent.action strongly typed
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16481 Extract update_plan tool spec into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16482 Remove client_common tool re-exports @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16495 fix: remove unused import @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16493 Extract built-in tool spec constructors into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16273 Fix regression: "not available in TUI" error message @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16497 Extract tool-search output helpers into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16499 Extract tool-suggest wire helpers into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16504 core: use codex-tools config types directly @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16503 Extract request_user_input normalization into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16509 Extract code-mode nested tool collection into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16512 core: remove cross-crate re-exports from lib.rs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16516 fix: add update to Cargo.lock that was missed in #16512 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16513 Extract tool registry planning into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16521 Move tool registry plan tests into codex-tools @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16523 [codex] Move config types into codex-config @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16524 fix: move some test utilities out of codex-rs/core/src/tools/spec.rs
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16529 [codex] Remove codex-core config type shim @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16561 fix: race pending @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16564 nit: lint @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16566 fix: races in end of turn @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16567 chore: rework state machine further @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16569 nit: state machine desc @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16571 chore: rename assign_task for followup_task @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16577 ci: upload compact Bazel execution logs for bazel.yml @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16581 chore: move codex-exec unit tests into sibling files @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16606 fix: add more detail to test assertion @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16608 fix: increase timeout to account for slow PowerShell startup @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16613 fix: increase another startup timeout for PowerShell @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16616 Fixed some existing labels and added a few new ones @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16588 Fix stale turn steering during TUI review follow-ups @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16596 Fix fork source display in /status (expose forked_from_id in app
      server) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16630 core: cut codex-core compile time 63% with native async ToolHandler
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16631 core: cut codex-core compile time 48% with native async SessionTask
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16492 Auto-trust cwd on thread start @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16634 build: fix Bazel lzma-sys wiring @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16626 remove temporary ownership re-exports @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16648 Fix stale /copy output after commentary-only turns @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16667 Suppress bwrap warning when sandboxing is bypassed @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16700 Add remote --cd forwarding for app-server sessions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16715 fix: address clippy violations that sneaked in @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16722 fix windows-only clippy lint violation @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16710 fix(tui): sort skill mentions by display name first @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16709 Sanitize forked child history @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16711 Fix Windows Bazel app-server trust tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16720 Remove OPENAI_BASE_URL config fallback @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16528 Codex/windows bazel rust test coverage no rs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16450 bazel: lint rust_test targets in clippy workflow @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16735 [codex] allow disabling prompt instruction blocks @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16755 Use Node 24 for npm publish @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16753 [codex] add responses proxy JSON dumps @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16757 Back out "bazel: lint rust_test targets in clippy workflow (#16450)"
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16737 test: avoid PowerShell startup in Windows auth fixture @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16740 ci: align Bazel repo cache and Windows clippy target handling @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16763 Add CODEX_SKIP_VENDORED_BWRAP @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16823 Fix flaky test relating to metadata remote URL @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16881 Fix misleading codex exec help usage @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16888 Clarify `codex exec` approval help @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16833 Fix TUI fast mode toggle regression @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16795 [regression] Fix ephemeral turn backfill in exec @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16813 Annotate skill doc reads with skill names @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16810 (tui): Decode percent-escaped bare local file links @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16877 [codex-backend] Make thread metadata updates tolerate pending backfill
      @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16701 feat(requirements): support allowed_approval_reviewers @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16925 fix(bazel): fix simdutf @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16926 bazel: Always save bazel repository cache @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16928 bazel: Enable `--experimental_remote_downloader` @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16462 fix(guardian): fix ordering of guardian events @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16924 fix(sqlite): don''t hard fail migrator if DB is newer @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16744 build: restore lzma-sys Bazel wiring for devbox codex run @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16764 app-server: centralize AuthManager initialization @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16939 Fix clippy warning @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16923 Revert "[codex-backend] Make thread metadata updates tolerate pending
      backfill" @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15951 app-server: Add egress websocket transport @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16945 [codex] Allow PyTorch libomp shm in Seatbelt @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16827 tui: route device-code auth through app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16638 [codex-analytics] add protocol-native turn timestamps @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16349 Disable env-bound tools when exec server is none @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16957 Promote image_detail_original to experimental @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16962 Refactor config types into a separate crate @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16153 Add setTimeout support to code mode @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16961 app-server: Unify config changes handling a bit @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16890 Validate exec input before starting app-server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#15893 fix: warn when bwrap cannot create user namespaces @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16946 [codex] Add danger-full-access denylist-only network mode @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16964 Honor null thread instructions @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16988 collapse dev message into one @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16724 [codex] ez - rename env=>request in codex-rs/core/src/unified_exec/process_manager.rs
      @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16999 feat: empty role ok @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17008 chore: send_message and followup_task do not return anything @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16442 feat: /feedback cascade @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16978 [codex] reduce module visibility @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16885 Fix read-only apply_patch rejection message @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16882 Fix nested exec thread ID restore @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16976 Preserve null developer instructions @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16987 Fix missing resume hint on zero-token exits @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16912 feat(analytics): generate an installation_id and pass it in responsesapi
      client_metadata @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16956 fix(guardian): don''t throw away transcript when over budget @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16981 [codex] Make AbsolutePathBuf joins infallible @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16348 Update README @romainhuet'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16977 [codex] Make unified exec tests remote aware @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17026 app-server: Move watch_id to request of fs/watch @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16980 Add full-ci branch trigger @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17032 [codex] Fix unified exec test build @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17027 [codex] Migrate apply_patch to executor filesystem @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17044 [app-server-protocol] introduce generic ServerResponse for app-server-protocol
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17047 fix(app-server) revert null instructions changes @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16960 Add WebRTC transport to realtime start @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17053 Fix remote address format to work with Windows Firewall rules.
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17048 [codex] Apply patches through executor filesystem @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17052 Add regression tests for JsonSchema @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17059 Add remote exec start script @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17064 Add project-local codex bug triage skill @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17096 Remove obsolete codex-cli README @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16875 Support anyOf and enum in JsonSchema @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16880 Render function attribute descriptions @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16879 Render namespace description for tools @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16582 feat: single app-server bootstrap in TUI @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17086 Fix TUI crash when resuming the current thread @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17097 Add realtime transport config @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17058 Add WebRTC media transport to realtime TUI @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17063 Use AbsolutePathBuf for exec cwd plumbing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17046 release ready, enabling only for siwc users @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17142 [codex] Support remote exec cwd in TUI startup @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17149 Fix missing fields @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17154 Fix ToolsConfigParams initializer in tool registry test @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17145 Wire realtime WebRTC native media into Bazel @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17057 Attach WebRTC realtime starts to sideband websocket @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17162 Add top-level exec-server subcommand @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17061 Update guardian output schema @maja-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17093 Add WebRTC realtime app-server e2e tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17174 Support Warp for OSC 9 notifications @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16646 Fix stale thread-name resume lookups @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17165 Move default realtime prompt into core @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17175 Add TUI notification condition config @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17186 Skip update prompts for source builds @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17188 make webrtc the default experience @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17222 feat: /resume per ID/name @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17226 feat: advanced announcements per OS and plans @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17116 chore: merge name and title @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17076 [codex] Show ctrl + t hint on truncated exec output in TUI @mom-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#16009 Forward app-server turn clientMetadata to Responses @neil-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17262 app-server: Fix clippy by removing extra `mut` @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  - quote: '#17258 Omit empty app-server instruction overrides @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.119.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 187-other-changes-in-rust-v0-119-0
  source_release: codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1
  source_type: github_releases
  theme: uncategorized
  title: 187 other changes in rust-v0.119.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1]]'
source_type: github_releases
theme: uncategorized
title: 187 other changes in rust-v0.119.0
type: change
---

<!-- chronolog:begin region="header" -->
# 187 other changes in rust-v0.119.0

**Codex CLI** · 2026-04-10 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.119.0) · from [[Releases/Codex CLI/codex-cli-2026-04-10-rust-v0-119-0-github-307754801-19f169d1|0.119.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/resume` can now jump directly to a session by ID or name from the TUI (#17222).

> Fast Mode no longer stays stuck on after `/fast off` in app-server-backed TUI sessions (#16833).

> Developer guidance for `argument_comment_lint` was updated to favor getting CI started instead of blocking on slow local lint runs (#16375).

> Obsolete `codex-cli` README content was removed to avoid stale setup guidance (#17096).

> `codex exec --help` now shows clearer usage and approval-mode wording (#16881, #16888).

> Rust CI and workspace guardrails were simplified by blocking new crate features and dropping routine `--all-features` runs (#16455, #16473).

> Core compile times were reduced by removing expensive async-trait expansion from hot tool/task abstractions (#16630, #16631).

> Bazel diagnostics and dependency wiring improved with compact execution logs, repository-cache persistence, remote downloader support, and several platform-specific build fixes (#16577, #16926, #16928, #16634, #16744).

> #16308 fix: one shot end of turn @jif-oai

> #16238 fix: ma2 @jif-oai

> #16317 chore: clean wait v2 @jif-oai

> #16318 nit: update aborted line @jif-oai

> #15771 feat: fork pattern v2 @jif-oai

> #16322 fix: update fork boundaries computation @jif-oai

> #16324 chore: drop interrupt from send_message @jif-oai

> #16345 fix: fix clippy issue caught by cargo but not bazel @bolinfest

> #16184 Route TUI `/feedback` submission through the app server @etraut-openai

> #16330 feat: log db better maintenance @jif-oai

> #15690 [codex-analytics] thread events @rhan-oai

> #16363 Fix PR babysitter review comment monitoring @etraut-openai

> #16356 Refactor external auth to use a single trait @etraut-openai

> #16366 Fix Windows external bearer refresh test @bolinfest

> #16353 ci: verify codex-rs Cargo manifests inherit workspace settings @bolinfest

> #16361 Refactor chatwidget tests into topical modules @etraut-openai

> #16201 Fix stale /status rate limits in active TUI sessions @etraut-openai

> #16351 ci: sync Bazel clippy lints and fix uncovered violations @bolinfest

> #16378 fix: suppress status card expect_used warnings after #16351 @bolinfest

> #16409 Use message string in v2 send_message @jif-oai

> #16419 Use message string in v2 assign_task @jif-oai

> #16425 nit: update wait v2 desc @jif-oai

> #16426 chore: interrupted as state @jif-oai

> #16427 nit: deny field v2 @jif-oai

> #16433 chore: drop log DB @jif-oai

> #16434 feat: auto vaccum state DB @jif-oai

> #16449 fix: remove unused import @bolinfest

> #15772 Make fuzzy file search case insensitive @meyers-oai

> #16455 ci: block new workspace crate features @bolinfest

> #16456 cloud-tasks: split the mock client out of cloud-tasks-client @bolinfest

> #16379 Extract tool config into codex-tools @bolinfest

> #16469 otel: remove the last workspace crate feature @bolinfest

> #16471 Extract tool spec helpers into codex-tools @bolinfest

> #16473 ci: stop running rust CI with --all-features @bolinfest

> #16477 Extract tool discovery helpers into codex-tools @bolinfest

> #16448 fix(guardian): make GuardianAssessmentEvent.action strongly typed @owenlin0

> #16481 Extract update_plan tool spec into codex-tools @bolinfest

> #16482 Remove client_common tool re-exports @bolinfest

> #16495 fix: remove unused import @bolinfest

> #16493 Extract built-in tool spec constructors into codex-tools @bolinfest

> #16273 Fix regression: "not available in TUI" error message @etraut-openai

> #16497 Extract tool-search output helpers into codex-tools @bolinfest

> #16499 Extract tool-suggest wire helpers into codex-tools @bolinfest

> #16504 core: use codex-tools config types directly @bolinfest

> #16503 Extract request_user_input normalization into codex-tools @bolinfest

> #16509 Extract code-mode nested tool collection into codex-tools @bolinfest

> #16512 core: remove cross-crate re-exports from lib.rs @bolinfest

> #16516 fix: add update to Cargo.lock that was missed in #16512 @bolinfest

> #16513 Extract tool registry planning into codex-tools @bolinfest

> #16521 Move tool registry plan tests into codex-tools @bolinfest

> #16523 [codex] Move config types into codex-config @bolinfest

> #16524 fix: move some test utilities out of codex-rs/core/src/tools/spec.rs @bolinfest

> #16529 [codex] Remove codex-core config type shim @bolinfest

> #16561 fix: race pending @jif-oai

> #16564 nit: lint @jif-oai

> #16566 fix: races in end of turn @jif-oai

> #16567 chore: rework state machine further @jif-oai

> #16569 nit: state machine desc @jif-oai

> #16571 chore: rename assign_task for followup_task @jif-oai

> #16577 ci: upload compact Bazel execution logs for bazel.yml @bolinfest

> #16581 chore: move codex-exec unit tests into sibling files @bolinfest

> #16606 fix: add more detail to test assertion @bolinfest

> #16608 fix: increase timeout to account for slow PowerShell startup @bolinfest

> #16613 fix: increase another startup timeout for PowerShell @bolinfest

> #16616 Fixed some existing labels and added a few new ones @etraut-openai

> #16588 Fix stale turn steering during TUI review follow-ups @etraut-openai

> #16596 Fix fork source display in /status (expose forked_from_id in app server) @etraut-openai

> #16630 core: cut codex-core compile time 63% with native async ToolHandler @bolinfest

> #16631 core: cut codex-core compile time 48% with native async SessionTask @bolinfest

> #16492 Auto-trust cwd on thread start @aibrahim-oai

> #16634 build: fix Bazel lzma-sys wiring @starr-openai

> #16626 remove temporary ownership re-exports @aibrahim-oai

> #16648 Fix stale /copy output after commentary-only turns @etraut-openai

> #16667 Suppress bwrap warning when sandboxing is bypassed @etraut-openai

> #16700 Add remote --cd forwarding for app-server sessions @etraut-openai

> #16715 fix: address clippy violations that sneaked in @bolinfest

> #16722 fix windows-only clippy lint violation @bolinfest

> #16710 fix(tui): sort skill mentions by display name first @fcoury-oai

> #16709 Sanitize forked child history @aibrahim-oai

> #16711 Fix Windows Bazel app-server trust tests @bolinfest

> #16720 Remove OPENAI_BASE_URL config fallback @etraut-openai

> #16528 Codex/windows bazel rust test coverage no rs @bolinfest

> #16450 bazel: lint rust_test targets in clippy workflow @bolinfest

> #16735 [codex] allow disabling prompt instruction blocks @tibo-openai

> #16755 Use Node 24 for npm publish @aibrahim-oai

> #16753 [codex] add responses proxy JSON dumps @tibo-openai

> #16757 Back out "bazel: lint rust_test targets in clippy workflow (#16450)" @bolinfest

> #16737 test: avoid PowerShell startup in Windows auth fixture @bolinfest

> #16740 ci: align Bazel repo cache and Windows clippy target handling @bolinfest

> #16763 Add CODEX_SKIP_VENDORED_BWRAP @andmis

> #16823 Fix flaky test relating to metadata remote URL @etraut-openai

> #16881 Fix misleading codex exec help usage @etraut-openai

> #16888 Clarify `codex exec` approval help @etraut-openai

> #16833 Fix TUI fast mode toggle regression @etraut-openai

> #16795 [regression] Fix ephemeral turn backfill in exec @etraut-openai

> #16813 Annotate skill doc reads with skill names @etraut-openai

> #16810 (tui): Decode percent-escaped bare local file links @etraut-openai

> #16877 [codex-backend] Make thread metadata updates tolerate pending backfill @joeytrasatti-openai

> #16701 feat(requirements): support allowed_approval_reviewers @owenlin0

> #16925 fix(bazel): fix simdutf @owenlin0

> #16926 bazel: Always save bazel repository cache @euroelessar

> #16928 bazel: Enable `--experimental_remote_downloader` @euroelessar

> #16462 fix(guardian): fix ordering of guardian events @owenlin0

> #16924 fix(sqlite): don't hard fail migrator if DB is newer @owenlin0

> #16744 build: restore lzma-sys Bazel wiring for devbox codex run @starr-openai

> #16764 app-server: centralize AuthManager initialization @euroelessar

> #16939 Fix clippy warning @mzeng-openai

> #16923 Revert "[codex-backend] Make thread metadata updates tolerate pending backfill" @joeytrasatti-openai

> #15951 app-server: Add egress websocket transport @euroelessar

> #16945 [codex] Allow PyTorch libomp shm in Seatbelt @viyatb-oai

> #16827 tui: route device-code auth through app server @etraut-openai

> #16638 [codex-analytics] add protocol-native turn timestamps @rhan-oai

> #16349 Disable env-bound tools when exec server is none @starr-openai

> #16957 Promote image_detail_original to experimental @fjord-oai

> #16962 Refactor config types into a separate crate @pakrym-oai

> #16153 Add setTimeout support to code mode @pakrym-oai

> #16961 app-server: Unify config changes handling a bit @euroelessar

> #16890 Validate exec input before starting app-server @etraut-openai

> #15893 fix: warn when bwrap cannot create user namespaces @viyatb-oai

> #16946 [codex] Add danger-full-access denylist-only network mode @viyatb-oai

> #16964 Honor null thread instructions @aibrahim-oai

> #16988 collapse dev message into one @won-openai

> #16724 [codex] ez - rename env=>request in codex-rs/core/src/unified_exec/process_manager.rs @starr-openai

> #16999 feat: empty role ok @jif-oai

> #17008 chore: send_message and followup_task do not return anything @jif-oai

> #16442 feat: /feedback cascade @jif-oai

> #16978 [codex] reduce module visibility @pakrym-oai

> #16885 Fix read-only apply_patch rejection message @etraut-openai

> #16882 Fix nested exec thread ID restore @etraut-openai

> #16976 Preserve null developer instructions @aibrahim-oai

> #16987 Fix missing resume hint on zero-token exits @etraut-openai

> #16912 feat(analytics): generate an installation_id and pass it in responsesapi client_metadata @owenlin0

> #16956 fix(guardian): don't throw away transcript when over budget @owenlin0

> #16981 [codex] Make AbsolutePathBuf joins infallible @pakrym-oai

> #16348 Update README @romainhuet

> #16977 [codex] Make unified exec tests remote aware @pakrym-oai

> #17026 app-server: Move watch_id to request of fs/watch @euroelessar

> #16980 Add full-ci branch trigger @pakrym-oai

> #17032 [codex] Fix unified exec test build @pakrym-oai

> #17027 [codex] Migrate apply_patch to executor filesystem @pakrym-oai

> #17044 [app-server-protocol] introduce generic ServerResponse for app-server-protocol @rhan-oai

> #17047 fix(app-server) revert null instructions changes @dylan-hurd-oai

> #16960 Add WebRTC transport to realtime start @aibrahim-oai

> #17053 Fix remote address format to work with Windows Firewall rules. @iceweasel-oai

> #17048 [codex] Apply patches through executor filesystem @pakrym-oai

> #17052 Add regression tests for JsonSchema @vivi

> #17059 Add remote exec start script @pakrym-oai

> #17064 Add project-local codex bug triage skill @etraut-openai

> #17096 Remove obsolete codex-cli README @etraut-openai

> #16875 Support anyOf and enum in JsonSchema @vivi

> #16880 Render function attribute descriptions @vivi

> #16879 Render namespace description for tools @vivi

> #16582 feat: single app-server bootstrap in TUI @jif-oai

> #17086 Fix TUI crash when resuming the current thread @etraut-openai

> #17097 Add realtime transport config @aibrahim-oai

> #17058 Add WebRTC media transport to realtime TUI @aibrahim-oai

> #17063 Use AbsolutePathBuf for exec cwd plumbing @pakrym-oai

> #17046 release ready, enabling only for siwc users @won-openai

> #17142 [codex] Support remote exec cwd in TUI startup @pakrym-oai

> #17149 Fix missing fields @canvrno-oai

> #17154 Fix ToolsConfigParams initializer in tool registry test @won-openai

> #17145 Wire realtime WebRTC native media into Bazel @aibrahim-oai

> #17057 Attach WebRTC realtime starts to sideband websocket @aibrahim-oai

> #17162 Add top-level exec-server subcommand @starr-openai

> #17061 Update guardian output schema @maja-openai

> #17093 Add WebRTC realtime app-server e2e tests @aibrahim-oai

> #17174 Support Warp for OSC 9 notifications @etraut-openai

> #16646 Fix stale thread-name resume lookups @etraut-openai

> #17165 Move default realtime prompt into core @aibrahim-oai

> #17175 Add TUI notification condition config @etraut-openai

> #17186 Skip update prompts for source builds @etraut-openai

> #17188 make webrtc the default experience @aibrahim-oai

> #17222 feat: /resume per ID/name @jif-oai

> #17226 feat: advanced announcements per OS and plans @jif-oai

> #17116 chore: merge name and title @jif-oai

> #17076 [codex] Show ctrl + t hint on truncated exec output in TUI @mom-oai

> #16009 Forward app-server turn clientMetadata to Responses @neil-oai

> #17262 app-server: Fix clippy by removing extra `mut` @euroelessar

> #17258 Omit empty app-server instruction overrides @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.119.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-10-4-context-window-changes-in-rust-v0-119-0|4 Context Window changes in rust-v0.119.0]] · Context Window
- [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-10-28-developer-workflow-changes-in-rust-v0-119-0|28 Developer Workflow changes in rust-v0.119.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-10-13-agent-mode-changes-in-rust-v0-119-0|13 Agent Mode changes in rust-v0.119.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-10-2-memory-and-personalization-changes-in-rust-v0-119-0|2 Memory and Personalization changes in rust-v0.119.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-10-the-readme-now-uses-the-current-chatgpt-business-plan-name-16348|The README now uses the current ChatGPT Business plan name (♯16348)]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-04-10-3-voice-and-audio-changes-in-rust-v0-119-0|3 Voice and Audio changes in rust-v0.119.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-04-10-19-apps-and-integrations-changes-in-rust-v0-119-0|19 Apps and Integrations changes in rust-v0.119.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-10-2-account-and-access-changes-in-rust-v0-119-0|2 Account and Access changes in rust-v0.119.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-10-17256-app-server-use-shared-receivers-for-app-server-message-processors-euroeles|♯17256 app-server: Use shared receivers for app-server message processors @euroelessar]] · Collaboration
- [[Changes/Codex CLI/2026-04-10-10-interface-experience-changes-in-rust-v0-119-0|10 Interface Experience changes in rust-v0.119.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-10-16202-fix-paste-driven-bottom-pane-completion-teardown-etraut-openai|♯16202 Fix paste-driven bottom pane completion teardown @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-10-2-reliability-and-performance-changes-in-rust-v0-119-0|2 Reliability and Performance changes in rust-v0.119.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-10-5-model-support-changes-in-rust-v0-119-0|5 Model Support changes in rust-v0.119.0]] · Model Support
- [[Changes/Codex CLI/2026-04-10-6-mobile-and-desktop-changes-in-rust-v0-119-0|6 Mobile and Desktop changes in rust-v0.119.0]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-10-b98528&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-10-187-other-changes-in-rust-v0-119-0.md%0ACard%20ID%3A%20codex-cli-2026-04-10-b98528%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.119.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->