---
card_id: codex-cli-2026-05-18-07548a
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Other changes: 155 changes in 0.131.0 — The
  TUI now offers richer session controls and display: data-driven service-tier commands…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9423ff6cce1e01b79779329c19d0a1fee4c1ccc935ea631f3536da348b410b16
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-07548a
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: 155 other changes'
  evidence:
  - quote: 'The TUI now offers richer session controls and display: data-driven service-tier
      commands, blended token usage, permissions/approval mode, effective workspace
      roots, and responsive Markdown tables. (#21745, #21906, #21991, #21669, #21677,
      #22052, #22612)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Made app-server and local state startup safer by preserving SQLite data,
      failing closed when state cannot open, adding recovery paths, and softening
      optional metadata sync failures. (#21831, #21847, #22580, #22734, #22899)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: Clarified that general Codex product docs should not be added to this repo,
      while app-server API docs remain in scope. (#21772)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Split large TUI ChatWidget, history, and composer code into focused modules
      without intended behavior changes. (#21866, #22269, #22407, #22433, #22518,
      #22537, #22704, #22581, #22656)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21550 [codex] make shutdown pending-touch test deterministic @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21697 Allow string service tiers in config TOML @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21687 [codex] Enable apply_patch freeform by default @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21757 api: send hyphenated session and thread headers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21763 nit: comment @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21749 codex-otel: validate provider span attributes consistently @bbrown-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21767 chore: thread tui @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21443 [sandboxing] Remove Darwin user cache write from Seatbelt network
      policy @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21604 Fix `rust-ci-full` failures due to missing `bwrap` @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21745 [codex] Generalize service tier slash commands @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21622 [codex] Address some more GHA hygiene issues @ww-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21662 feat: Use installation ID in remote enrollments @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20667 Load configured environments from CODEX_HOME @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21787 Support resource binaries in Python runtime staging @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21784 Publish Python runtime wheels on release @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21601 Emit accepted line fingerprint analytics @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21465 Remove ToolName display helper @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21810 Revert "Publish Python runtime wheels on release" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21651 [codex] Delete function-style apply_patch @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21616 Enable `--deny-warnings` for `cargo shear` @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21835 ci: check out PR head commits in workflows @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21794 Make environment provider snapshots path-free @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21831 app-server: support daemon-safe restart handling @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20293 Support openai library tool @lt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21323 [codex] support executor registry remote environments @miz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21825 Increase exec-server environment transport timeouts @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20718 [daemon] Add app-server daemon lifecycle management @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21847 sqlite: no more destructive version bumps @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21652 Reapply "Move skills watcher to app-server" @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21290 Move file watcher out of core @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21906 [codex] Lowercase TUI service tier commands @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21760 fix(tui): preserve wrapped prose beside URLs @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21866 Split ChatWidget state into focused modules @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21991 Persist ''priority'' service tier as fast in config @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21943 fix(tui): preserve Shift+Enter in tmux csi-u panes @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22039 Deduplicate issue digest interactions by user @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22052 feat(tui): render responsive Markdown tables in TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21736 extension: add initial typed extension API @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21737 extension: wire extension registries into sessions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22138 refactor: extract executable tool contracts into codex-tool-api
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22140 feat: drop `CodexExtension` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22143 [codex] default unknown contributed tools to mutating @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22147 feat: wire extension tool bundles into core @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22113 Add x-codex-ws-stream-request-start-ms @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21860 Persist /goal commands in history @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22106 Fix side conversation config inheritance @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22045 Improve goal continuation based on feedback @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21981 Use goal preview metadata for goal-first threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21843 app-server: remove TCP websocket listener @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22173 chore: drop built-in MCPs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21431 [codex-analytics] add turn tool counts to turn events @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22154 Add process-scoped SQLite telemetry @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#19068 Unified mentions in TUI @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22058 fix(exec-server): suppress Windows taskkill output @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22178 fix(app-server): thread history redaction for remote clients @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#15977 fix(permissions): preserve managed deny-read during escalation
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22188 [elicitation] Advertise new url elicitation capability when auth_elicitation
      is enabled. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22192 config: accept `minus` in TUI keymap config @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21853 daemon: refresh updater after validated binary rollout @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20147 feat: add network proxy feature flag @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22180 Stop uploading accepted line fingerprints @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22198 Add production startup and TTFT telemetry @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21963 [exec-server] serve websocket listener via HTTP upgrade @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20527 Support PreToolUse updatedInput rewrites @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22254 [codex] Make handlers own parallel tool support @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22216 feat: guardian as an extension (contributors part) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22311 [rollout-trace] Add x-codex-inference-call-id header to inference
      calls. @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22323 fix: uv lock @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22382 tools: remove is_mutating dispatch gating @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22377 code-mode: carry nested tool kind through runtime @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22392 test(tui): relax configured pet load timeout @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22343 feat(exec-server): use protobuf relay frames @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20509 [codex] Remove workspace owner usage nudge gate @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22256 Refactor namespaced tool spec registration @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22280 code-mode: Add pending-aware code mode execution @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22398 [codex] Add search term coverage for tool_search @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22236 Unify thread metadata updates above store @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22269 Refactor chatwidget state into modules @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22381 [codex] Remove tool search bucket limit override @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22386 mark Feature::RemoteControl as removed @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22404 Restore app-server websocket listener with auth guard @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22413 Remove CODEX_RS_SSE_FIXTURE test hook @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22406 tools: infer code-mode namespace descriptions from specs @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22261 Encapsulate tool search entries in handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22414 Add support for UDS in `codex --remote` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22407 Refactor chatwidget input flow into modules @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21768 add --dangerously-bypass-hook-trust CLI flag @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22344 extension-api: add approval review contributor flow @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22479 nit: codeowners @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22480 feat: add turn lifecycle contributors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22482 fix: emit thread stop lifecycle on implicit shutdown @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22485 feat: add token usage contributor hook @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22490 feat: move extension scope ids into ExtensionData @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22214 feat(tui): remove Zellij TUI workarounds @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22488 feat: add config-change extension contributor @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22503 fix: main @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22433 Refactor chatwidget protocol flows into modules (phase 3) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20559 config: add strict config parsing @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22489 Introduce tool exposure for deferred registration @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22193 fix: drop underscored id headers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22520 revert: mark Feature::RemoteControl as removed @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22366 Pass Codex product SKU to ChatGPT backend @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22519 Deprecate TurnContext cwd and resolve_path @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22518 Refactor chatwidget settings surfaces into modules (phase 4) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22412 chore(config) rm Feature::CodexGitCommit @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22501 chore(config) rm tools.view_image @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22533 fix: prevent codex-backend from stealing originator @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22408 Shard Bazel Windows tests across jobs @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22542 Use selected environment cwd for filesystem helpers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21235 [codex] Fix TUI wrapping for external borrowed slices @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22336 feat(cli): add codex doctor diagnostics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22543 clean up instructions @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22529 Spill oversized PreToolUse additionalContext @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22556 feat: namespace in ext @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22537 Refactor chatwidget orchestration into modules (phase 5) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22574 Deprecate issue labeler @maxb-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22580 fix: Block appserver startup if state db can''t be opened @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22565 chore(config) rm experimental_use_freeform_apply_patch @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22573 Simplify TUI startup test coverage @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22587 Defer startup NUX impressions until startup succeeds @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22560 feat: make ToolExecutor an async trait @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22494 Wire turn item contributors into stream output @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#17141 feat: add layered --profile-v2 config files @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22643 [codex] treat PowerShell stop-parsing forms as unsupported @bookholt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22646 Fix abort-path turn extension data plumbing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22624 permissions: canonicalize workspace_roots and danger-full-access
      names @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22649 Chore: better published unsigned artifacts @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22581 tui: split composer attachment and popup state @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22229 fix(tui): render network approval history by target @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22512 test: isolate exec review policy config test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22572 Fix remote environment test fixtures @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22563 tests: isolate codex home for live cli @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#18161 [codex] Support multiple forced ChatGPT workspaces @rreichel3-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22702 make rust-release-prepare use env secret @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22711 chore(features) rm Feature::ApplyPatchFreeform @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22695 Trim TUI legacy core helper usage @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22684 Remove SSE fixture loaders @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22730 [codex] Group removed feature flags @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22724 [codex] Remove experimental instructions file config @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22303 Stabilize compact rollback follow-up test @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22683 permissions: resolve profile identity with constraints @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22734 tui: recover local state db startup failures @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22710 Prevent Esc from dismissing or rewinding `/side` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22704 TUI: split history cells into focused modules @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22612 tui/exec: show effective workspace roots in summaries @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22647 Reject legacy [profiles] when using profile-v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22636 Simplify tool executor and registry plumbing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22820 Remove zombie tools spec module @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22656 tui: split remaining composer draft and footer state @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22582 Workflow updates @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22899 [codex] Soften SQLite metadata sync failures @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 155-other-changes-in-rust-v0-131-0
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: uncategorized
  title: 155 other changes in rust-v0.131.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: uncategorized
title: 155 other changes in rust-v0.131.0
type: change
---

<!-- chronolog:begin region="header" -->
# 155 other changes in rust-v0.131.0

**Codex CLI** · 2026-05-18 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The TUI now offers richer session controls and display: data-driven service-tier commands, blended token usage, permissions/approval mode, effective workspace roots, and responsive Markdown tables. (#21745, #21906, #21991, #21669, #21677, #22052, #22612)

> Made app-server and local state startup safer by preserving SQLite data, failing closed when state cannot open, adding recovery paths, and softening optional metadata sync failures. (#21831, #21847, #22580, #22734, #22899)

> Clarified that general Codex product docs should not be added to this repo, while app-server API docs remain in scope. (#21772)

> Split large TUI ChatWidget, history, and composer code into focused modules without intended behavior changes. (#21866, #22269, #22407, #22433, #22518, #22537, #22704, #22581, #22656)

> #21550 [codex] make shutdown pending-touch test deterministic @jif-oai

> #21697 Allow string service tiers in config TOML @aibrahim-oai

> #21687 [codex] Enable apply_patch freeform by default @aibrahim-oai

> #21757 api: send hyphenated session and thread headers @jif-oai

> #21763 nit: comment @jif-oai

> #21749 codex-otel: validate provider span attributes consistently @bbrown-oai

> #21767 chore: thread tui @jif-oai

> #21443 [sandboxing] Remove Darwin user cache write from Seatbelt network policy @evawong-oai

> #21604 Fix `rust-ci-full` failures due to missing `bwrap` @zanie-oai

> #21745 [codex] Generalize service tier slash commands @aibrahim-oai

> #21622 [codex] Address some more GHA hygiene issues @ww-oai

> #21662 feat: Use installation ID in remote enrollments @ddr-oai

> #20667 Load configured environments from CODEX_HOME @starr-openai

> #21787 Support resource binaries in Python runtime staging @aibrahim-oai

> #21784 Publish Python runtime wheels on release @aibrahim-oai

> #21601 Emit accepted line fingerprint analytics @alexsong-oai

> #21465 Remove ToolName display helper @pakrym-oai

> #21810 Revert "Publish Python runtime wheels on release" @aibrahim-oai

> #21651 [codex] Delete function-style apply_patch @pakrym-oai

> #21616 Enable `--deny-warnings` for `cargo shear` @charliemarsh-oai

> #21835 ci: check out PR head commits in workflows @bolinfest

> #21794 Make environment provider snapshots path-free @starr-openai

> #21831 app-server: support daemon-safe restart handling @euroelessar

> #20293 Support openai library tool @lt-oai

> #21323 [codex] support executor registry remote environments @miz-openai

> #21825 Increase exec-server environment transport timeouts @starr-openai

> #20718 [daemon] Add app-server daemon lifecycle management @euroelessar

> #21847 sqlite: no more destructive version bumps @owenlin0

> #21652 Reapply "Move skills watcher to app-server" @pakrym-oai

> #21290 Move file watcher out of core @pakrym-oai

> #21906 [codex] Lowercase TUI service tier commands @aibrahim-oai

> #21760 fix(tui): preserve wrapped prose beside URLs @fcoury-oai

> #21866 Split ChatWidget state into focused modules @etraut-openai

> #21991 Persist 'priority' service tier as fast in config @aibrahim-oai

> #21943 fix(tui): preserve Shift+Enter in tmux csi-u panes @fcoury-oai

> #22039 Deduplicate issue digest interactions by user @etraut-openai

> #22052 feat(tui): render responsive Markdown tables in TUI @fcoury-oai

> #21736 extension: add initial typed extension API @jif-oai

> #21737 extension: wire extension registries into sessions @jif-oai

> #22138 refactor: extract executable tool contracts into codex-tool-api @jif-oai

> #22140 feat: drop `CodexExtension` @jif-oai

> #22143 [codex] default unknown contributed tools to mutating @jif-oai

> #22147 feat: wire extension tool bundles into core @jif-oai

> #22113 Add x-codex-ws-stream-request-start-ms @andmis

> #21860 Persist /goal commands in history @etraut-openai

> #22106 Fix side conversation config inheritance @etraut-openai

> #22045 Improve goal continuation based on feedback @etraut-openai

> #21981 Use goal preview metadata for goal-first threads @etraut-openai

> #21843 app-server: remove TCP websocket listener @euroelessar

> #22173 chore: drop built-in MCPs @jif-oai

> #21431 [codex-analytics] add turn tool counts to turn events @rhan-oai

> #22154 Add process-scoped SQLite telemetry @jif-oai

> #19068 Unified mentions in TUI @canvrno-oai

> #22058 fix(exec-server): suppress Windows taskkill output @fcoury-oai

> #22178 fix(app-server): thread history redaction for remote clients @owenlin0

> #15977 fix(permissions): preserve managed deny-read during escalation @viyatb-oai

> #22188 [elicitation] Advertise new url elicitation capability when auth_elicitation is enabled. @mzeng-openai

> #22192 config: accept `minus` in TUI keymap config @fcoury-oai

> #21853 daemon: refresh updater after validated binary rollout @euroelessar

> #20147 feat: add network proxy feature flag @viyatb-oai

> #22180 Stop uploading accepted line fingerprints @alexsong-oai

> #22198 Add production startup and TTFT telemetry @mzeng-openai

> #21963 [exec-server] serve websocket listener via HTTP upgrade @euroelessar

> #20527 Support PreToolUse updatedInput rewrites @abhinav-oai

> #22254 [codex] Make handlers own parallel tool support @pakrym-oai

> #22216 feat: guardian as an extension (contributors part) @jif-oai

> #22311 [rollout-trace] Add x-codex-inference-call-id header to inference calls. @cassirer-openai

> #22323 fix: uv lock @jif-oai

> #22382 tools: remove is_mutating dispatch gating @pakrym-oai

> #22377 code-mode: carry nested tool kind through runtime @pakrym-oai

> #22392 test(tui): relax configured pet load timeout @fcoury-oai

> #22343 feat(exec-server): use protobuf relay frames @apanasenko-oai

> #20509 [codex] Remove workspace owner usage nudge gate @richardopenai

> #22256 Refactor namespaced tool spec registration @pakrym-oai

> #22280 code-mode: Add pending-aware code mode execution @cconger

> #22398 [codex] Add search term coverage for tool_search @pakrym-oai

> #22236 Unify thread metadata updates above store @wiltzius-openai

> #22269 Refactor chatwidget state into modules @etraut-openai

> #22381 [codex] Remove tool search bucket limit override @sayan-oai

> #22386 mark Feature::RemoteControl as removed @owenlin0

> #22404 Restore app-server websocket listener with auth guard @etraut-openai

> #22413 Remove CODEX_RS_SSE_FIXTURE test hook @pakrym-oai

> #22406 tools: infer code-mode namespace descriptions from specs @pakrym-oai

> #22261 Encapsulate tool search entries in handlers @pakrym-oai

> #22414 Add support for UDS in `codex --remote` @etraut-openai

> #22407 Refactor chatwidget input flow into modules @etraut-openai

> #21768 add --dangerously-bypass-hook-trust CLI flag @abhinav-oai

> #22344 extension-api: add approval review contributor flow @jif-oai

> #22479 nit: codeowners @jif-oai

> #22480 feat: add turn lifecycle contributors @jif-oai

> #22482 fix: emit thread stop lifecycle on implicit shutdown @jif-oai

> #22485 feat: add token usage contributor hook @jif-oai

> #22490 feat: move extension scope ids into ExtensionData @jif-oai

> #22214 feat(tui): remove Zellij TUI workarounds @fcoury-oai

> #22488 feat: add config-change extension contributor @jif-oai

> #22503 fix: main @jif-oai

> #22433 Refactor chatwidget protocol flows into modules (phase 3) @etraut-openai

> #20559 config: add strict config parsing @bolinfest

> #22489 Introduce tool exposure for deferred registration @jif-oai

> #22193 fix: drop underscored id headers @jif-oai

> #22520 revert: mark Feature::RemoteControl as removed @owenlin0

> #22366 Pass Codex product SKU to ChatGPT backend @ericning-o

> #22519 Deprecate TurnContext cwd and resolve_path @pakrym-oai

> #22518 Refactor chatwidget settings surfaces into modules (phase 4) @etraut-openai

> #22412 chore(config) rm Feature::CodexGitCommit @dylan-hurd-oai

> #22501 chore(config) rm tools.view_image @dylan-hurd-oai

> #22533 fix: prevent codex-backend from stealing originator @owenlin0

> #22408 Shard Bazel Windows tests across jobs @starr-openai

> #22542 Use selected environment cwd for filesystem helpers @pakrym-oai

> #21235 [codex] Fix TUI wrapping for external borrowed slices @canvrno-oai

> #22336 feat(cli): add codex doctor diagnostics @fcoury-oai

> #22543 clean up instructions @sayan-oai

> #22529 Spill oversized PreToolUse additionalContext @abhinav-oai

> #22556 feat: namespace in ext @jif-oai

> #22537 Refactor chatwidget orchestration into modules (phase 5) @etraut-openai

> #22574 Deprecate issue labeler @maxb-openai

> #22580 fix: Block appserver startup if state db can't be opened @ddr-oai

> #22565 chore(config) rm experimental_use_freeform_apply_patch @dylan-hurd-oai

> #22573 Simplify TUI startup test coverage @etraut-openai

> #22587 Defer startup NUX impressions until startup succeeds @etraut-openai

> #22560 feat: make ToolExecutor an async trait @jif-oai

> #22494 Wire turn item contributors into stream output @jif-oai

> #17141 feat: add layered --profile-v2 config files @jif-oai

> #22643 [codex] treat PowerShell stop-parsing forms as unsupported @bookholt-oai

> #22646 Fix abort-path turn extension data plumbing @jif-oai

> #22624 permissions: canonicalize workspace_roots and danger-full-access names @bolinfest

> #22649 Chore: better published unsigned artifacts @shijie-oai

> #22581 tui: split composer attachment and popup state @etraut-openai

> #22229 fix(tui): render network approval history by target @fcoury-oai

> #22512 test: isolate exec review policy config test @bolinfest

> #22572 Fix remote environment test fixtures @starr-openai

> #22563 tests: isolate codex home for live cli @starr-openai

> #18161 [codex] Support multiple forced ChatGPT workspaces @rreichel3-oai

> #22702 make rust-release-prepare use env secret @sayan-oai

> #22711 chore(features) rm Feature::ApplyPatchFreeform @dylan-hurd-oai

> #22695 Trim TUI legacy core helper usage @etraut-openai

> #22684 Remove SSE fixture loaders @pakrym-oai

> #22730 [codex] Group removed feature flags @dylan-hurd-oai

> #22724 [codex] Remove experimental instructions file config @dylan-hurd-oai

> #22303 Stabilize compact rollback follow-up test @dylan-hurd-oai

> #22683 permissions: resolve profile identity with constraints @bolinfest

> #22734 tui: recover local state db startup failures @etraut-openai

> #22710 Prevent Esc from dismissing or rewinding `/side` @etraut-openai

> #22704 TUI: split history cells into focused modules @etraut-openai

> #22612 tui/exec: show effective workspace roots in summaries @bolinfest

> #22647 Reject legacy [profiles] when using profile-v2 @jif-oai

> #22636 Simplify tool executor and registry plumbing @jif-oai

> #22820 Remove zombie tools spec module @jif-oai

> #22656 tui: split remaining composer draft and footer state @etraut-openai

> #22582 Workflow updates @viyatb-oai

> #22899 [codex] Soften SQLite metadata sync failures @wiltzius-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-5-account-and-access-changes-in-rust-v0-131-0|5 Account and Access changes in rust-v0.131.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0|12 Developer Workflow changes in rust-v0.131.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0|10 Mobile and Desktop changes in rust-v0.131.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-07548a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-155-other-changes-in-rust-v0-131-0.md%0ACard%20ID%3A%20codex-cli-2026-05-18-07548a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->