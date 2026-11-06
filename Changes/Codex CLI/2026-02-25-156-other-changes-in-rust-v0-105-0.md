---
card_id: codex-cli-2026-02-25-bbd0a1
date: '2026-02-25'
description: 'Codex CLI · 2026-02-25 · Other changes: 156 changes in 0.105.0 — App-server
  clients can do more with threads: `thread/list` can search by title, thread status…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7bb4294bff719d9df88986289157ddfdf7750fd4aa6cf79cc2df49aff21769c7
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-25-bbd0a1
  comparison: ''
  date: '2026-02-25'
  description: 'Codex CLI — 0.105.0: 156 other changes'
  evidence:
  - quote: 'App-server clients can do more with threads: `thread/list` can search
      by title, thread status is exposed in read/list responses and notifications,
      and `thread/resume` returns the latest turn inline so reconnects are less lossy.
      (#11776, #11786, #12578)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: Long links in the TUI stay clickable when wrapped, which also fixes related
      clipping and layout issues in several views. (#12067)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: 'Several TUI interaction edge cases were fixed: queued-message editing
      now works in more terminals, follow-up prompts no longer get stuck if you press
      Enter while a final answer is still streaming, and approval dialogs now respond
      with the correct request id. (#12240, #12569, #12746)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: Linux sandboxed commands now get a minimal `/dev`, fixing failures in tools
      that need entropy or other standard device nodes. (#12081)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '`js_repl` now reports uncaught kernel failures more clearly, recovers
      cleanly afterward, and correctly attaches `view_image` results from nested tool
      calls. (#12636, #12725)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: 'Updated install and local workflow docs to use `cargo install --locked
      cargo-nextest` and to avoid routine `--all-features` builds unless you specifically
      need full feature coverage. (#12377, #12429)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12071 Use V2 websockets if feature enabled @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12052 feat(core): zsh exec bridge @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12077 got rid of experimental_mode for configtoml @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12036 codex-api: realtime websocket session.create + typed inbound events
      @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11944 [js_repl] paths for node module resolution can be specified for
      js_repl @aaronl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12124 feat: phase 1 and phase 2 e2e latencies @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12121 feat: phase 2 usage @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12135 feat: better slug for rollout summaries @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12157 Disable collab tools during review delegation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11802 Fixed a hole in token refresh logic for app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12105 fix: file watcher @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12177 js_repl: canonicalize paths for node_modules boundary checks @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12187 fix: Remove citation @zuxin-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11786 app-server: expose loaded thread status via read/list and notifications
      @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12038 state: enforce 10 MiB log caps for thread and threadless process
      logs @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12203 Stabilize app-server detached review and running-resume tests @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12164 Update docs links for feature flag notice @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12228 feat: add configurable write_stdin timeout @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12244 Restore phase when loading from history @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12101 client side modelinfo overrides @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12254 chore: increase stack size for everyone @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12250 feat: no timeout mode on ue @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12255 chore: consolidate new() and initialize() for McpConnectionManager
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12256 Revert "feat: no timeout mode on ue" @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12258 Undo stack size Bazel test hack @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12264 Fix flaky test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12087 feat: add Reject approval policy with granular prompt rejection
      controls @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12253 Skip removed features during metrics emission @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12265 Clarify cumulative proposed_plan behavior in Plan mode @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12266 app-server tests: reduce intermittent nextest LEAK via graceful
      child shutdown @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11953 ws turn metadata via client_metadata @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12274 [bazel] Fix proc_macro_dep libs @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12054 feat(config): add permissions.network proxy config wiring @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12269 tests(thread_resume): interrupt running turns in resume error-path
      tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12009 Update pnpm versions to fix cve-2026-24842 @mjr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12080 skill-creator: lazy-load PyYAML in frontmatter parsing @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12271 tests: centralize in-flight turn cleanup helper @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11776 app-server: improve thread resume rejoin flow @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12315 chore: nit explorer @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12326 disable collab for phase 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12344 feat: do not enqueue phase 2 if not necessary @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12347 fix: nick name at thread/read @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12294 Reuse connection between turns @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12287 app-server: add JSON tracing logs @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12140 Refactor network approvals to host/protocol/port scope @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12300 js_repl: block wrapped payload prefixes in grammar @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11368 fix(network-proxy): add unix socket allow-all and update seatbelt
      rules @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12275 js_repl: remove codex.state helper references @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12205 ci(bazel): install Node from node-version.txt in remote image @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12218 app-server: harden disconnect cleanup paths @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12291 core tests: use hermetic mock server in review suite @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12377 docs: use --locked when installing cargo-nextest @derekf-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12370 Add ability to attach extra files to feedback @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12306 Move sanitizer into codex-secrets @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12406 fix: explicitly list name collisions in JSON schema generation
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12301 Add field to Thread object for the latest rename set for a given
      thread @natea-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12268 Wire realtime api to core @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12415 fix(nix): include libcap dependency on linux builds @rgodha24'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12416 Add experimental realtime websocket URL override @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12418 Add experimental realtime websocket overrides and text mirroring
      @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12381 fix: address flakiness in thread_resume_rejoins_running_thread_even_with_override_mismatch
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12422 feat: use OAI Responses API MessagePhase type directly in App Server
      v2 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12376 test(app-server): wait for turn/completed in turn_start tests @yvolovich-cyber'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12408 ignore v1 in JSON schema codegen @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12314 fix(core) Filter non-matching prefix rules @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12429 feat: discourage the use of the --all-features flag @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12427 chore: move config diagnostics out of codex-core @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12430 Collapse waited message @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12434 fix: codex-arg0 no longer depends on codex-core @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12435 refactor(core): move embedded system skills into codex-skills crate
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12440 chore: delete empty codex-rs/code file @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12441 Delete AggregatedStream @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12420 Prevent replayed runtime events from forcing active status @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12428 Prefer v2 websockets if available @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12419 Improve token usage estimate for images @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12067 fix(tui): preserve URL clickability across all TUI views @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12469 Route inbound realtime text into turn start or steer @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12479 Revert "Route inbound realtime text into turn start or steer" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12475 fix: make realtime conversation flake test order-insensitive @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12373 app-server: retain thread listener across disconnects @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12444 feat(tui) /clear @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12485 fix(core) exec policy parsing 3 @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12423 Send events to realtime api @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12364 feat: monitor role @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12313 Handle orphan exec ends without clobbering active exploring cell
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12455 feat(tui): support Alt-d delete-forward-word @dougEfresh'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12480 Revert "Revert "Route inbound realtime text into turn start or
      steer"" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12511 Add C# syntax option to highlight selections @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12513 Add PR babysitting skill for this repo @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12518 test: vendor zsh fork via DotSlash and stabilize zsh-fork tests
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12553 Return image content from view_image @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12559 chore: nit name @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12562 chore: awaiter @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12568 chore: phase 2 name @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12571 fix: TUI constraint @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12500 feat: add uuid helper @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12141 feat: land sqlite @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12576 chore: better bazel test logs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12421 app-server: box request dispatch future to reduce stack pressure
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12528 chore(deps): bump libc from 0.2.180 to 0.2.182 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12529 chore(deps): bump syn from 2.0.114 to 2.0.117 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12583 Use Arc-based ToolCtx in tool runtimes @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12609 fix(tui): recover on owned wrap mapping mismatch @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12569 fix(tui): queue steer Enter while final answer is still streaming
      to prevent dead state @guidedways'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12530 chore(deps): bump owo-colors from 4.2.3 to 4.3.0 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12619 Handle realtime spawn_transcript delegation @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12357 feat(core): persist network approvals in execpolicy @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12648 fix(exec) Patch resume test race condition @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12049 Support implicit skill invocation analytics events @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12647 Avoid `AbsolutePathBuf::parent()` panic under `EMFILE` by skipping
      re-absolutization @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12633 Add skill approval event/response @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12650 chore: rm hardcoded PRESETS list @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12652 Simplify skill tracking @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11258 Send warmup request @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12688 feat: use process group to kill the PTY @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11871 feat(core) Introduce Feature::RequestPermissions @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#9859 feat(network-proxy): add MITM support and gate limited-mode CONNECT
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12643 Fix @mention token parsing in chat composer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12658 fix: also try matching namespaced prefix for modelinfo candidate
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#11766 feat(sleep-inhibitor): add Linux and Windows idle-sleep prevention
      @yvolovich-cyber'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12707 refactor: remove unused seatbelt unix socket arg @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12687 Add TUI realtime conversation mode @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12711 fix: temp remove citation @zuxin-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12613 feat(tui) - /copy @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12695 Add app-server event tracing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12517 codex-rs/app-server: graceful websocket restart on Ctrl-C @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12636 fix(js_repl): surface uncaught kernel errors and reset cleanly
      @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12729 fix: clarify the value of SkillMetadata.path @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12719 feat: pass helper executable paths via Arg0DispatchPaths @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12720 add AWS_LC_SYS_NO_JITTER_ENTROPY=1 to release musl build step to
      unblock releases @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12725 Fix js_repl view_image attachments in nested tool calls @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12656 chore: change catalog mode to enum @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12731 chore: migrate additional permissions to PermissionProfile @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12407 tests(js_repl): stabilize CI runtime test execution @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12372 feat: update Docker image digest to reflect #12205 @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12746 fix: chatwidget was not honoring approval_id for an ExecApprovalRequestEvent
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12185 tests(js_repl): remove node-related skip paths from js_repl tests
      @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12358 feat(ui): add network approval persistence plumbing @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12730 feat: zsh-fork forces scripts/**/* for skills to trigger a prompt
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12319 feat: add service name to app-server @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12692 fix: flaky test due to second-resolution for thread ordering @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12578 feat: add search term to thread list @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12756 feat: record whether a skill script is approved for the session
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12767 Display pending child-thread approvals in TUI @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12768 feat: add large stack test macro @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12666 feat: adding stream parser @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12772 nit: migration @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12352 otel: add host.name resource attribute to logs/traces via gethostname
      @mcgrew-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12770 chore: unify max depth parameter @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  - quote: '#12787 feat: fix sqlite home @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.105.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 156-other-changes-in-rust-v0-105-0
  source_release: codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed
  source_type: github_releases
  theme: uncategorized
  title: 156 other changes in rust-v0.105.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed]]'
source_type: github_releases
theme: uncategorized
title: 156 other changes in rust-v0.105.0
type: change
---

<!-- chronolog:begin region="header" -->
# 156 other changes in rust-v0.105.0

**Codex CLI** · 2026-02-25 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.105.0) · from [[Releases/Codex CLI/codex-cli-2026-02-25-rust-v0-105-0-github-290476287-0c72d1ed|0.105.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients can do more with threads: `thread/list` can search by title, thread status is exposed in read/list responses and notifications, and `thread/resume` returns the latest turn inline so reconnects are less lossy. (#11776, #11786, #12578)

> Long links in the TUI stay clickable when wrapped, which also fixes related clipping and layout issues in several views. (#12067)

> Several TUI interaction edge cases were fixed: queued-message editing now works in more terminals, follow-up prompts no longer get stuck if you press Enter while a final answer is still streaming, and approval dialogs now respond with the correct request id. (#12240, #12569, #12746)

> Linux sandboxed commands now get a minimal `/dev`, fixing failures in tools that need entropy or other standard device nodes. (#12081)

> `js_repl` now reports uncaught kernel failures more clearly, recovers cleanly afterward, and correctly attaches `view_image` results from nested tool calls. (#12636, #12725)

> Updated install and local workflow docs to use `cargo install --locked cargo-nextest` and to avoid routine `--all-features` builds unless you specifically need full feature coverage. (#12377, #12429)

> #12071 Use V2 websockets if feature enabled @pakrym-oai

> #12052 feat(core): zsh exec bridge @owenlin0

> #12077 got rid of experimental_mode for configtoml @won-openai

> #12036 codex-api: realtime websocket session.create + typed inbound events @aibrahim-oai

> #11944 [js_repl] paths for node module resolution can be specified for js_repl @aaronl-openai

> #12124 feat: phase 1 and phase 2 e2e latencies @jif-oai

> #12121 feat: phase 2 usage @jif-oai

> #12135 feat: better slug for rollout summaries @jif-oai

> #12157 Disable collab tools during review delegation @jif-oai

> #11802 Fixed a hole in token refresh logic for app server @etraut-openai

> #12105 fix: file watcher @jif-oai

> #12177 js_repl: canonicalize paths for node_modules boundary checks @fjord-oai

> #12187 fix: Remove citation @zuxin-oai

> #11786 app-server: expose loaded thread status via read/list and notifications @euroelessar

> #12038 state: enforce 10 MiB log caps for thread and threadless process logs @charley-oai

> #12203 Stabilize app-server detached review and running-resume tests @charley-oai

> #12164 Update docs links for feature flag notice @etraut-openai

> #12228 feat: add configurable write_stdin timeout @jif-oai

> #12244 Restore phase when loading from history @mousseau-oai

> #12101 client side modelinfo overrides @sayan-oai

> #12254 chore: increase stack size for everyone @jif-oai

> #12250 feat: no timeout mode on ue @jif-oai

> #12255 chore: consolidate new() and initialize() for McpConnectionManager @bolinfest

> #12256 Revert "feat: no timeout mode on ue" @jif-oai

> #12258 Undo stack size Bazel test hack @charley-oai

> #12264 Fix flaky test @jif-oai

> #12087 feat: add Reject approval policy with granular prompt rejection controls @bolinfest

> #12253 Skip removed features during metrics emission @jif-oai

> #12265 Clarify cumulative proposed_plan behavior in Plan mode @charley-oai

> #12266 app-server tests: reduce intermittent nextest LEAK via graceful child shutdown @bolinfest

> #11953 ws turn metadata via client_metadata @pash-openai

> #12274 [bazel] Fix proc_macro_dep libs @zbarsky-openai

> #12054 feat(config): add permissions.network proxy config wiring @viyatb-oai

> #12269 tests(thread_resume): interrupt running turns in resume error-path tests @bolinfest

> #12009 Update pnpm versions to fix cve-2026-24842 @mjr-openai

> #12080 skill-creator: lazy-load PyYAML in frontmatter parsing @xl-openai

> #12271 tests: centralize in-flight turn cleanup helper @bolinfest

> #11776 app-server: improve thread resume rejoin flow @maxj-oai

> #12315 chore: nit explorer @jif-oai

> #12326 disable collab for phase 2 @jif-oai

> #12344 feat: do not enqueue phase 2 if not necessary @jif-oai

> #12347 fix: nick name at thread/read @jif-oai

> #12294 Reuse connection between turns @pakrym-oai

> #12287 app-server: add JSON tracing logs @maxj-oai

> #12140 Refactor network approvals to host/protocol/port scope @viyatb-oai

> #12300 js_repl: block wrapped payload prefixes in grammar @fjord-oai

> #11368 fix(network-proxy): add unix socket allow-all and update seatbelt rules @viyatb-oai

> #12275 js_repl: remove codex.state helper references @fjord-oai

> #12205 ci(bazel): install Node from node-version.txt in remote image @fjord-oai

> #12218 app-server: harden disconnect cleanup paths @maxj-oai

> #12291 core tests: use hermetic mock server in review suite @viyatb-oai

> #12377 docs: use --locked when installing cargo-nextest @derekf-oai

> #12370 Add ability to attach extra files to feedback @pakrym-oai

> #12306 Move sanitizer into codex-secrets @viyatb-oai

> #12406 fix: explicitly list name collisions in JSON schema generation @bolinfest

> #12301 Add field to Thread object for the latest rename set for a given thread @natea-oai

> #12268 Wire realtime api to core @aibrahim-oai

> #12415 fix(nix): include libcap dependency on linux builds @rgodha24

> #12416 Add experimental realtime websocket URL override @aibrahim-oai

> #12418 Add experimental realtime websocket overrides and text mirroring @aibrahim-oai

> #12381 fix: address flakiness in thread_resume_rejoins_running_thread_even_with_override_mismatch @bolinfest

> #12422 feat: use OAI Responses API MessagePhase type directly in App Server v2 @bolinfest

> #12376 test(app-server): wait for turn/completed in turn_start tests @yvolovich-cyber

> #12408 ignore v1 in JSON schema codegen @bolinfest

> #12314 fix(core) Filter non-matching prefix rules @dylan-hurd-oai

> #12429 feat: discourage the use of the --all-features flag @bolinfest

> #12427 chore: move config diagnostics out of codex-core @bolinfest

> #12430 Collapse waited message @pakrym-oai

> #12434 fix: codex-arg0 no longer depends on codex-core @bolinfest

> #12435 refactor(core): move embedded system skills into codex-skills crate @bolinfest

> #12440 chore: delete empty codex-rs/code file @bolinfest

> #12441 Delete AggregatedStream @pakrym-oai

> #12420 Prevent replayed runtime events from forcing active status @etraut-openai

> #12428 Prefer v2 websockets if available @pakrym-oai

> #12419 Improve token usage estimate for images @etraut-openai

> #12067 fix(tui): preserve URL clickability across all TUI views @fcoury

> #12469 Route inbound realtime text into turn start or steer @aibrahim-oai

> #12479 Revert "Route inbound realtime text into turn start or steer" @aibrahim-oai

> #12475 fix: make realtime conversation flake test order-insensitive @bolinfest

> #12373 app-server: retain thread listener across disconnects @maxj-oai

> #12444 feat(tui) /clear @won-openai

> #12485 fix(core) exec policy parsing 3 @dylan-hurd-oai

> #12423 Send events to realtime api @aibrahim-oai

> #12364 feat: monitor role @jif-oai

> #12313 Handle orphan exec ends without clobbering active exploring cell @jif-oai

> #12455 feat(tui): support Alt-d delete-forward-word @dougEfresh

> #12480 Revert "Revert "Route inbound realtime text into turn start or steer"" @aibrahim-oai

> #12511 Add C# syntax option to highlight selections @etraut-openai

> #12513 Add PR babysitting skill for this repo @etraut-openai

> #12518 test: vendor zsh fork via DotSlash and stabilize zsh-fork tests @bolinfest

> #12553 Return image content from view_image @pakrym-oai

> #12559 chore: nit name @jif-oai

> #12562 chore: awaiter @jif-oai

> #12568 chore: phase 2 name @jif-oai

> #12571 fix: TUI constraint @jif-oai

> #12500 feat: add uuid helper @jif-oai

> #12141 feat: land sqlite @jif-oai

> #12576 chore: better bazel test logs @jif-oai

> #12421 app-server: box request dispatch future to reduce stack pressure @charley-oai

> #12528 chore(deps): bump libc from 0.2.180 to 0.2.182 in /codex-rs @dependabot

> #12529 chore(deps): bump syn from 2.0.114 to 2.0.117 in /codex-rs @dependabot

> #12583 Use Arc-based ToolCtx in tool runtimes @bolinfest

> #12609 fix(tui): recover on owned wrap mapping mismatch @fcoury

> #12569 fix(tui): queue steer Enter while final answer is still streaming to prevent dead state @guidedways

> #12530 chore(deps): bump owo-colors from 4.2.3 to 4.3.0 in /codex-rs @dependabot

> #12619 Handle realtime spawn_transcript delegation @aibrahim-oai

> #12357 feat(core): persist network approvals in execpolicy @viyatb-oai

> #12648 fix(exec) Patch resume test race condition @dylan-hurd-oai

> #12049 Support implicit skill invocation analytics events @alexsong-oai

> #12647 Avoid `AbsolutePathBuf::parent()` panic under `EMFILE` by skipping re-absolutization @etraut-openai

> #12633 Add skill approval event/response @pakrym-oai

> #12650 chore: rm hardcoded PRESETS list @sayan-oai

> #12652 Simplify skill tracking @pakrym-oai

> #11258 Send warmup request @pakrym-oai

> #12688 feat: use process group to kill the PTY @jif-oai

> #11871 feat(core) Introduce Feature::RequestPermissions @dylan-hurd-oai

> #9859 feat(network-proxy): add MITM support and gate limited-mode CONNECT @viyatb-oai

> #12643 Fix @mention token parsing in chat composer @etraut-openai

> #12658 fix: also try matching namespaced prefix for modelinfo candidate @sayan-oai

> #11766 feat(sleep-inhibitor): add Linux and Windows idle-sleep prevention @yvolovich-cyber

> #12707 refactor: remove unused seatbelt unix socket arg @bolinfest

> #12687 Add TUI realtime conversation mode @aibrahim-oai

> #12711 fix: temp remove citation @zuxin-oai

> #12613 feat(tui) - /copy @won-openai

> #12695 Add app-server event tracing @pakrym-oai

> #12517 codex-rs/app-server: graceful websocket restart on Ctrl-C @maxj-oai

> #12636 fix(js_repl): surface uncaught kernel errors and reset cleanly @fjord-oai

> #12729 fix: clarify the value of SkillMetadata.path @bolinfest

> #12719 feat: pass helper executable paths via Arg0DispatchPaths @bolinfest

> #12720 add AWS_LC_SYS_NO_JITTER_ENTROPY=1 to release musl build step to unblock releases @sayan-oai

> #12725 Fix js_repl view_image attachments in nested tool calls @fjord-oai

> #12656 chore: change catalog mode to enum @sayan-oai

> #12731 chore: migrate additional permissions to PermissionProfile @celia-oai

> #12407 tests(js_repl): stabilize CI runtime test execution @fjord-oai

> #12372 feat: update Docker image digest to reflect #12205 @fjord-oai

> #12746 fix: chatwidget was not honoring approval_id for an ExecApprovalRequestEvent @bolinfest

> #12185 tests(js_repl): remove node-related skip paths from js_repl tests @fjord-oai

> #12358 feat(ui): add network approval persistence plumbing @viyatb-oai

> #12730 feat: zsh-fork forces scripts/**/* for skills to trigger a prompt @bolinfest

> #12319 feat: add service name to app-server @jif-oai

> #12692 fix: flaky test due to second-resolution for thread ordering @jif-oai

> #12578 feat: add search term to thread list @jif-oai

> #12756 feat: record whether a skill script is approved for the session @bolinfest

> #12767 Display pending child-thread approvals in TUI @jif-oai

> #12768 feat: add large stack test macro @jif-oai

> #12666 feat: adding stream parser @jif-oai

> #12772 nit: migration @jif-oai

> #12352 otel: add host.name resource attribute to logs/traces via gethostname @mcgrew-oai

> #12770 chore: unify max depth parameter @jif-oai

> #12787 feat: fix sqlite home @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.105.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-25-13-apps-and-integrations-changes-in-rust-v0-105-0|13 Apps and Integrations changes in rust-v0.105.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-25-18-agent-mode-changes-in-rust-v0-105-0|18 Agent Mode changes in rust-v0.105.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-25-15-developer-workflow-changes-in-rust-v0-105-0|15 Developer Workflow changes in rust-v0.105.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-25-12028-remove-feature-flag-collaboration-modes-aibrahim-oai|♯12028 remove feature flag collaboration modes @aibrahim-oai]] · Collaboration
- [[Changes/Codex CLI/2026-02-25-9-memory-and-personalization-changes-in-rust-v0-105-0|9 Memory and Personalization changes in rust-v0.105.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-25-3-reliability-and-performance-changes-in-rust-v0-105-0|3 Reliability and Performance changes in rust-v0.105.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-25-you-can-now-dictate-prompts-by-holding-the-spacebar-to-record-and-transcribe-voi|Dictate prompts by holding the spacebar to record and transcribe voice input…]] · Voice and Audio
- [[Changes/Codex CLI/2026-02-25-3-account-and-access-changes-in-rust-v0-105-0|3 Account and Access changes in rust-v0.105.0]] · Account and Access
- [[Changes/Codex CLI/2026-02-25-8-interface-experience-changes-in-rust-v0-105-0|8 Interface Experience changes in rust-v0.105.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-25-2-editor-experience-changes-in-rust-v0-105-0|2 Editor Experience changes in rust-v0.105.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0|9 Safety and Privacy changes in rust-v0.105.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-25-5-context-window-changes-in-rust-v0-105-0|5 Context Window changes in rust-v0.105.0]] · Context Window
- [[Changes/Codex CLI/2026-02-25-6-model-support-changes-in-rust-v0-105-0|6 Model Support changes in rust-v0.105.0]] · Model Support
- [[Changes/Codex CLI/2026-02-25-2-mobile-and-desktop-changes-in-rust-v0-105-0|2 Mobile and Desktop changes in rust-v0.105.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-25-2-voice-and-audio-changes-in-rust-v0-105-0|2 Voice and Audio changes in rust-v0.105.0]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-25-bbd0a1&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-25-156-other-changes-in-rust-v0-105-0.md%0ACard%20ID%3A%20codex-cli-2026-02-25-bbd0a1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.105.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->