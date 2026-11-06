---
card_id: codex-cli-2026-05-07-7764b9
date: '2026-05-07'
description: 'Codex CLI · 2026-05-07 · Other changes: 137 changes in 0.129.0 — The
  TUI now supports modal Vim editing in the composer, including `/vim`, default-mode
  config…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d5c56f04e0f84ea79fbd4a66657f556e7a0cd301afd34485455d9c22f7c6fb91
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-07-7764b9
  comparison: ''
  date: '2026-05-07'
  description: 'Codex CLI — 0.129.0: 137 other changes'
  evidence:
  - quote: The TUI now supports modal Vim editing in the composer, including `/vim`,
      default-mode config, and Vim-specific keymap contexts. (#18595)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: 'Experimental goals are now discoverable, stay paused across resume unless
      the user opts back in, and show clearer validation and multi-day duration output.
      (#20083, #20790, #20746, #20558)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: Updated the embedded OpenAI Docs sample skill so API-key setup guidance
      stays aligned with other docs variants. (#21263)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: Removed local-only planning/spec docs and redirected config docs toward
      the maintained external documentation surface. (#20896)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: 'Linux releases now build, publish, bundle, and verify a standalone `bwrap`
      fallback for npm and DotSlash installs. (#21255, #21256, #21257, #21312, #21285)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: 'App-server and protocol internals were split and slimmed down, including
      transport extraction, protocol module decomposition, thread/message history
      moves, and tool-handler cleanup. (#20324, #20325, #20348, #20545, #21251, #21278,
      #21395)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20334 Make missing config clears no-ops @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20361 realtime: rename provider session ids @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20083 Mark goals feature as experimental @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20458 [Extension] Allowlist Chrome Extension in the tool_suggest tool
      @teddywyly-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20324 Remove core protocol dependency [1/2] @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20299 Move item event mapping into app-server-protocol @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20325 Remove core protocol dependency [2/2] @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20471 Stop emitting item/fileChange/outputDelta output delta notifications
      @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20245 [Codex] Add browser use external feature flag @khoi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20275 fix: show correct Bedrock runtime endpoint in /status @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20463 feat(rollouts): store EventMsg::ApplyPatchEnd in limited history
      mode @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19280 [codex] Migrate thread turns list to thread store @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19160 Make apply_patch streaming parser stateful @akshaynathan'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20504 fix flaky test falls_back_to_registered_fallback_port_when_default_po…
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20098 fix: ignore dangerous project-level config keys @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20502 fix(tui): set persist_extended_history: false @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#18595 feat(tui): add vim composer mode @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20499 fix(app-server): mark thread/turns/list and exclude_turns as experime…
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20113 fix(exec_policy) heredoc parsing file_redirect @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20300 [codex-analytics] centralize thread analytics state @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20484 [codex] Improve PR babysitter CI diagnostics and guardrails @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20511 [codex] Remove unused event messages @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19474 Make thread store process-scoped @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20558 Format multi-day goal durations in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19631 Color TUI statusline from active theme @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20602 feat: ad-hoc instructions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20610 chore: improve remember prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20405 feat: export and replay effective config locks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20540 Move apply-patch file changes into turn items @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20564 Enforce `animations = false` for screen readers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20523 Remove no-tool goal continuation suppression @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20627 fix: cargo deny @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20545 app-server: move transport into dedicated crate @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20630 [codex] Add Codex environment config @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20524 deprecate legacy notify @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20486 [codex] Migrate loaded thread/read history to ThreadStore @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20535 fix(tui): restore alt-enter newline alias @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20650 fix: reduce ConfigBuilder::build stack usage @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20512 [codex] Emit image view as core item @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20562 Use the 2025-06-18 elicitation capability shape @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20674 Clear live hook rows when turns finalize @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20542 Prune unused code-mode globals @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20585 ci: cross-compile Windows Bazel tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20701 ci: cross-compile Windows Bazel clippy @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20566 [tool_suggest] More prompt polishes. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20751 Bound websocket request sends with idle timeout @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20893 [codex] Add issue labeler area labels @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20896 Remove local docs and specs @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20897 [codex] Refactor app-server dispatch result flow @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20998 nit: renaming @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21006 nit: legacy @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20790 Keep paused goals paused on thread resume @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20940 [codex] Split app-server request processors @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21023 typo @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20750 Unify skip-review handling for approval_mode = "approve" @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20682 feat(app-server): always return limited thread history @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21034 tui: retire /approvals and rename /autoreview to /approve @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20669 Prepare selected environment plumbing @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20685 Fix Windows PTY teardown by preserving ConPTY ownership @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20663 Add stdio exec-server listener @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20561 state: pass state db handles through consumers @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20892 feat(tui): add PR summary statusline items @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20798 feat(tui): improve TUI keymap coverage @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21060 core: fix apply_patch request permissions test @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21058 fix(tui): support modified backspace/delete keys @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20715 Make realtime sideband startup async @kmeelu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20514 [codex-analytics] add item lifecycle timing @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19040 [codex] Add unsandboxed process exec API @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21105 [network-proxy] Cover DNS timeout blocking @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20576 codex: route metadata updates through ThreadStore @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21122 Add turn_id to Codex skill invocation analytics @edwardysun3'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20575 codex: migrate (more) app-server thread history reads to ThreadStore
      @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21170 tools: remove unused experimental `list_dir` tool @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20207 fix(tui): make /copy work inside tmux without passthrough @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20799 Add goal lifecycle metrics @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20746 Validate /goal objective length in TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20692 Support PreToolUse additionalContext @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21091 [codex] Fix TUI large paste placeholder numbering after Ctrl+C
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21089 [codex] Fix fork --last cwd filtering @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21152 revert legacy notify deprecation @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20111 fix(sandboxing): Bound advisory system bwrap startup probe @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21220 chore: add minimal proxy egress diagnostics @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20819 feat(tui): add raw scrollback mode @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21225 app-server: ignore persist_extended_history param @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#17089 [codex-analytics] add tool item event schemas @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20647 Route process tools to selected environments @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20321 hook trust metadata and enforcement @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21063 add turn items view to app-server turns @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20687 [codex] Split tool handlers by tool name @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21243 [codex] fix TUI turn items view fixtures @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21146 Enable V8 sandboxing for source-built builds @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#19575 Add cloud executor registration to exec-server @miz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20577 codex: use ThreadStore history for core review forks @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21261 fix build @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21251 chore(app-server-protocol): split v2 API definitions into modules
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21259 ci: trigger rusty-v8 releases from tags @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21256 release: publish standalone bwrap artifacts @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21260 [codex] Move thread naming to app server @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21257 release/npm: bundle standalone bwrap on Linux @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21276 [codex] Remove unused ListModels op @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21282 [codex] Remove legacy ListSkills op @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20949 [codex-analytics] rework thread_source for thread analytics @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20724 app-server: align dynamic tool identifiers with Responses API @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21285 fix(bwrap): emit libcap after standalone archive @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21312 release: bundle bwrap with Linux codex DotSlash artifact @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20437 feat: add `session_id` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21328 test: isolate app-server-client in-process test state @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21332 feat: return session ID from thread/fork @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21249 Propagate cache key and service tiers in compact @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21182 Move installation ID resolution out of core startup @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21336 feat(app-server): move v2 `sessionId` onto `Thread` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#20971 2- Use string service tiers in session protocol @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21278 Move message history out of core @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21284 [codex] Add response.processed websocket request @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21367 rollout: coalesce thread updated_at touches @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21378 feat: move auto vaccum @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21263 [codex] Coordinate OpenAI docs sample with API key setup @mifan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21351 fix(tui): keep Ctrl-C stashed drafts after /clear @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21389 vendor: update bubblewrap to 0.11.2 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21397 fix(tui): persist ctrl-c draft via app event @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21107 Avoid noisy OTEL diagnostics in codex exec @cpaasch-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21395 [codex] Split tool handlers into separate files @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21401 [codex-tui] pass thread source for tui threads @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#17090 [codex-analytics] emit tool item events from item lifecycle @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21287 Move skills watcher to app-server @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21416 [codex] Move tool specs into core handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21460 Revert "Move skills watcher to app-server" @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21450 fix(tui): clear first inline viewport render @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21427 [codex] Delete tool handler plan indirection @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21423 [codex] Add OpenAI Developers to tool suggest allowlist @mifan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  - quote: '#21441 [codex] Parallelize skills list cwd loading @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.129.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 137-other-changes-in-rust-v0-129-0
  source_release: codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e
  source_type: github_releases
  theme: uncategorized
  title: 137 other changes in rust-v0.129.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e]]'
source_type: github_releases
theme: uncategorized
title: 137 other changes in rust-v0.129.0
type: change
---

<!-- chronolog:begin region="header" -->
# 137 other changes in rust-v0.129.0

**Codex CLI** · 2026-05-07 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.129.0) · from [[Releases/Codex CLI/codex-cli-2026-05-07-rust-v0-129-0-github-319066904-0c2c638e|0.129.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The TUI now supports modal Vim editing in the composer, including `/vim`, default-mode config, and Vim-specific keymap contexts. (#18595)

> Experimental goals are now discoverable, stay paused across resume unless the user opts back in, and show clearer validation and multi-day duration output. (#20083, #20790, #20746, #20558)

> Updated the embedded OpenAI Docs sample skill so API-key setup guidance stays aligned with other docs variants. (#21263)

> Removed local-only planning/spec docs and redirected config docs toward the maintained external documentation surface. (#20896)

> Linux releases now build, publish, bundle, and verify a standalone `bwrap` fallback for npm and DotSlash installs. (#21255, #21256, #21257, #21312, #21285)

> App-server and protocol internals were split and slimmed down, including transport extraction, protocol module decomposition, thread/message history moves, and tool-handler cleanup. (#20324, #20325, #20348, #20545, #21251, #21278, #21395)

> #20334 Make missing config clears no-ops @etraut-openai

> #20361 realtime: rename provider session ids @aibrahim-oai

> #20083 Mark goals feature as experimental @etraut-openai

> #20458 [Extension] Allowlist Chrome Extension in the tool_suggest tool @teddywyly-oai

> #20324 Remove core protocol dependency [1/2] @etraut-openai

> #20299 Move item event mapping into app-server-protocol @pakrym-oai

> #20325 Remove core protocol dependency [2/2] @etraut-openai

> #20471 Stop emitting item/fileChange/outputDelta output delta notifications @pakrym-oai

> #20245 [Codex] Add browser use external feature flag @khoi-oai

> #20275 fix: show correct Bedrock runtime endpoint in /status @celia-oai

> #20463 feat(rollouts): store EventMsg::ApplyPatchEnd in limited history mode @owenlin0

> #19280 [codex] Migrate thread turns list to thread store @wiltzius-openai

> #19160 Make apply_patch streaming parser stateful @akshaynathan

> #20504 fix flaky test falls_back_to_registered_fallback_port_when_default_po… @owenlin0

> #20098 fix: ignore dangerous project-level config keys @owenlin0

> #20502 fix(tui): set persist_extended_history: false @owenlin0

> #18595 feat(tui): add vim composer mode @fcoury-oai

> #20499 fix(app-server): mark thread/turns/list and exclude_turns as experime… @owenlin0

> #20113 fix(exec_policy) heredoc parsing file_redirect @dylan-hurd-oai

> #20300 [codex-analytics] centralize thread analytics state @rhan-oai

> #20484 [codex] Improve PR babysitter CI diagnostics and guardrails @wiltzius-openai

> #20511 [codex] Remove unused event messages @pakrym-oai

> #19474 Make thread store process-scoped @wiltzius-openai

> #20558 Format multi-day goal durations in the TUI @etraut-openai

> #19631 Color TUI statusline from active theme @etraut-openai

> #20602 feat: ad-hoc instructions @jif-oai

> #20610 chore: improve remember prompt @jif-oai

> #20405 feat: export and replay effective config locks @jif-oai

> #20540 Move apply-patch file changes into turn items @pakrym-oai

> #20564 Enforce `animations = false` for screen readers @etraut-openai

> #20523 Remove no-tool goal continuation suppression @etraut-openai

> #20627 fix: cargo deny @jif-oai

> #20545 app-server: move transport into dedicated crate @euroelessar

> #20630 [codex] Add Codex environment config @pakrym-oai

> #20524 deprecate legacy notify @abhinav-oai

> #20486 [codex] Migrate loaded thread/read history to ThreadStore @wiltzius-openai

> #20535 fix(tui): restore alt-enter newline alias @fcoury-oai

> #20650 fix: reduce ConfigBuilder::build stack usage @jif-oai

> #20512 [codex] Emit image view as core item @pakrym-oai

> #20562 Use the 2025-06-18 elicitation capability shape @abhinav-oai

> #20674 Clear live hook rows when turns finalize @abhinav-oai

> #20542 Prune unused code-mode globals @cconger

> #20585 ci: cross-compile Windows Bazel tests @bolinfest

> #20701 ci: cross-compile Windows Bazel clippy @bolinfest

> #20566 [tool_suggest] More prompt polishes. @mzeng-openai

> #20751 Bound websocket request sends with idle timeout @pakrym-oai

> #20893 [codex] Add issue labeler area labels @etraut-openai

> #20896 Remove local docs and specs @etraut-openai

> #20897 [codex] Refactor app-server dispatch result flow @pakrym-oai

> #20998 nit: renaming @jif-oai

> #21006 nit: legacy @jif-oai

> #20790 Keep paused goals paused on thread resume @etraut-openai

> #20940 [codex] Split app-server request processors @pakrym-oai

> #21023 typo @jif-oai

> #20750 Unify skip-review handling for approval_mode = "approve" @mzeng-openai

> #20682 feat(app-server): always return limited thread history @owenlin0

> #21034 tui: retire /approvals and rename /autoreview to /approve @won-openai

> #20669 Prepare selected environment plumbing @starr-openai

> #20685 Fix Windows PTY teardown by preserving ConPTY ownership @iceweasel-oai

> #20663 Add stdio exec-server listener @starr-openai

> #20561 state: pass state db handles through consumers @euroelessar

> #20892 feat(tui): add PR summary statusline items @fcoury-oai

> #20798 feat(tui): improve TUI keymap coverage @fcoury-oai

> #21060 core: fix apply_patch request permissions test @bolinfest

> #21058 fix(tui): support modified backspace/delete keys @fcoury-oai

> #20715 Make realtime sideband startup async @kmeelu-oai

> #20514 [codex-analytics] add item lifecycle timing @rhan-oai

> #19040 [codex] Add unsandboxed process exec API @euroelessar

> #21105 [network-proxy] Cover DNS timeout blocking @evawong-oai

> #20576 codex: route metadata updates through ThreadStore @wiltzius-openai

> #21122 Add turn_id to Codex skill invocation analytics @edwardysun3

> #20575 codex: migrate (more) app-server thread history reads to ThreadStore @wiltzius-openai

> #21170 tools: remove unused experimental `list_dir` tool @jif-oai

> #20207 fix(tui): make /copy work inside tmux without passthrough @fcoury-oai

> #20799 Add goal lifecycle metrics @etraut-openai

> #20746 Validate /goal objective length in TUI @etraut-openai

> #20692 Support PreToolUse additionalContext @abhinav-oai

> #21091 [codex] Fix TUI large paste placeholder numbering after Ctrl+C @canvrno-oai

> #21089 [codex] Fix fork --last cwd filtering @canvrno-oai

> #21152 revert legacy notify deprecation @abhinav-oai

> #20111 fix(sandboxing): Bound advisory system bwrap startup probe @viyatb-oai

> #21220 chore: add minimal proxy egress diagnostics @viyatb-oai

> #20819 feat(tui): add raw scrollback mode @fcoury-oai

> #21225 app-server: ignore persist_extended_history param @owenlin0

> #17089 [codex-analytics] add tool item event schemas @rhan-oai

> #20647 Route process tools to selected environments @starr-openai

> #20321 hook trust metadata and enforcement @abhinav-oai

> #21063 add turn items view to app-server turns @rhan-oai

> #20687 [codex] Split tool handlers by tool name @pakrym-oai

> #21243 [codex] fix TUI turn items view fixtures @fcoury-oai

> #21146 Enable V8 sandboxing for source-built builds @cconger

> #19575 Add cloud executor registration to exec-server @miz-openai

> #20577 codex: use ThreadStore history for core review forks @wiltzius-openai

> #21261 fix build @bolinfest

> #21251 chore(app-server-protocol): split v2 API definitions into modules @owenlin0

> #21259 ci: trigger rusty-v8 releases from tags @cconger

> #21256 release: publish standalone bwrap artifacts @bolinfest

> #21260 [codex] Move thread naming to app server @pakrym-oai

> #21257 release/npm: bundle standalone bwrap on Linux @bolinfest

> #21276 [codex] Remove unused ListModels op @pakrym-oai

> #21282 [codex] Remove legacy ListSkills op @pakrym-oai

> #20949 [codex-analytics] rework thread_source for thread analytics @rhan-oai

> #20724 app-server: align dynamic tool identifiers with Responses API @eternal-openai

> #21285 fix(bwrap): emit libcap after standalone archive @viyatb-oai

> #21312 release: bundle bwrap with Linux codex DotSlash artifact @bolinfest

> #20437 feat: add `session_id` @jif-oai

> #21328 test: isolate app-server-client in-process test state @jif-oai

> #21332 feat: return session ID from thread/fork @jif-oai

> #21249 Propagate cache key and service tiers in compact @aibrahim-oai

> #21182 Move installation ID resolution out of core startup @jif-oai

> #21336 feat(app-server): move v2 `sessionId` onto `Thread` @jif-oai

> #20971 2- Use string service tiers in session protocol @aibrahim-oai

> #21278 Move message history out of core @pakrym-oai

> #21284 [codex] Add response.processed websocket request @pakrym-oai

> #21367 rollout: coalesce thread updated_at touches @jif-oai

> #21378 feat: move auto vaccum @jif-oai

> #21263 [codex] Coordinate OpenAI docs sample with API key setup @mifan-oai

> #21351 fix(tui): keep Ctrl-C stashed drafts after /clear @fcoury-oai

> #21389 vendor: update bubblewrap to 0.11.2 @bolinfest

> #21397 fix(tui): persist ctrl-c draft via app event @fcoury-oai

> #21107 Avoid noisy OTEL diagnostics in codex exec @cpaasch-oai

> #21395 [codex] Split tool handlers into separate files @pakrym-oai

> #21401 [codex-tui] pass thread source for tui threads @rhan-oai

> #17090 [codex-analytics] emit tool item events from item lifecycle @rhan-oai

> #21287 Move skills watcher to app-server @pakrym-oai

> #21416 [codex] Move tool specs into core handlers @pakrym-oai

> #21460 Revert "Move skills watcher to app-server" @pakrym-oai

> #21450 fix(tui): clear first inline viewport render @fcoury-oai

> #21427 [codex] Delete tool handler plan indirection @pakrym-oai

> #21423 [codex] Add OpenAI Developers to tool suggest allowlist @mifan-oai

> #21441 [codex] Parallelize skills list cwd loading @xli-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.129.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-07-5-agent-mode-changes-in-rust-v0-129-0|5 Agent Mode changes in rust-v0.129.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-07-39-apps-and-integrations-changes-in-rust-v0-129-0|39 Apps and Integrations changes in rust-v0.129.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-07-3-mobile-and-desktop-changes-in-rust-v0-129-0|3 Mobile and Desktop changes in rust-v0.129.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-07-3-collaboration-changes-in-rust-v0-129-0|3 Collaboration changes in rust-v0.129.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-07-20065-feat-tui-redesign-session-picker-fcoury-oai|♯20065 feat(tui): redesign session picker @fcoury-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-05-07-4-model-support-changes-in-rust-v0-129-0|4 Model Support changes in rust-v0.129.0]] · Model Support
- [[Changes/Codex CLI/2026-05-07-4-editor-experience-changes-in-rust-v0-129-0|4 Editor Experience changes in rust-v0.129.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-07-5-developer-workflow-changes-in-rust-v0-129-0|5 Developer Workflow changes in rust-v0.129.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-07-2-account-and-access-changes-in-rust-v0-129-0|2 Account and Access changes in rust-v0.129.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-07-7-context-window-changes-in-rust-v0-129-0|7 Context Window changes in rust-v0.129.0]] · Context Window
- [[Changes/Codex CLI/2026-05-07-tui-startup-and-accessibility-were-tightened-by-bounding-terminal-probes-clearin|TUI startup and accessibility were tightened by bounding terminal probes, clearing…]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-05-07-21379-document-codex-git-commit-attribution-config-henzelmann-oai|♯21379 Document Codex git commit attribution config @henzelmann-oai]] · Files and Data
- [[Changes/Codex CLI/2026-05-07-21054-rollout-store-web-search-and-mcp-tool-calls-owenlin0|♯21054 rollout: store web search and mcp tool calls @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-05-07-16-memory-and-personalization-changes-in-rust-v0-129-0|16 Memory and Personalization changes in rust-v0.129.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-07-2-reliability-and-performance-changes-in-rust-v0-129-0|2 Reliability and Performance changes in rust-v0.129.0]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-07-7764b9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-07-137-other-changes-in-rust-v0-129-0.md%0ACard%20ID%3A%20codex-cli-2026-05-07-7764b9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.129.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->