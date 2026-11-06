---
card_id: codex-cli-2026-04-30-312d98
date: '2026-04-30'
description: 'Codex CLI · 2026-04-30 · Other changes: 145 changes in 0.128.0 — Clarified
  contributor-facing docs, including the PR template, Rust async trait guidance, and…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f24d703ae3b11c0157b5d2814a47ac1402fdab82c8e6396d05395ca80491c95a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-30-312d98
  comparison: ''
  date: '2026-04-30'
  description: 'Codex CLI — 0.128.0: 145 other changes'
  evidence:
  - quote: 'Clarified contributor-facing docs, including the PR template, Rust async
      trait guidance, and README wording. (#19912, #20242, #19514)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: 'Added a checked-in `codex-core` public API listing and a ThreadManager
      sample crate. (#20243, #20141)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: 'Published `codex-app-server` release artifacts, stopped publishing GNU
      Linux binaries, and increased release workflow timeouts. (#19447, #19445, #20271,
      #20343)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: 'Stabilized CI and release plumbing with Bazel setup migration, release
      smoke-test pinning, and updated workflow pins/timeouts. (#19851, #19854, #19472,
      #19609)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19124 Make MultiAgentV2 interruption markers assistant-authored @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19354 chore: alias max_concurrent_threads_per_session @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18392 Fix hang on turn/interrupt @danwang-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19283 check PID of named pipe consumer @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19163 Harden package-manager install policy @mcgrew-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19093 [codex] Omit fork turns from thread started notifications @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19244 Update unix socket transport to use WebSocket upgrade @willwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19414 permissions: make legacy profile conversion cwd-free @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18900 Migrate fork and resume reads to thread store @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19445 ci: stop publishing GNU Linux release artifacts @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19447 ci: publish codex-app-server release artifacts @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19422 Clarify bundled OpenAI Docs upgrade guide wording @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19266 [codex] add non-local thread store regression harness @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19098 feat: Compress skill paths with root aliases @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19234 Refactor log DB into LogWriter interface @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19449 permissions: remove legacy read-only access modes @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19472 ci: pin codex-action v1.7 @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19468 Fix Bazel cargo_bin runfiles paths @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19410 Remove js_repl feature @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18073 Add goal persistence foundation (1 / 5) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18074 Add goal app-server API (2 / 5) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18076 Add goal core runtime (4 / 5) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18077 Add goal TUI UX (5 / 5) @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19454 Split approval matrix test groups @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19514 Fix codex-rs README grammar @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19459 Enable unavailable dummy tools by default @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19578 fix: increase Bazel timeout to 45 minutes @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19595 [codex] Bypass managed network for escalated exec @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19609 fix: restore 30-minute timeout for Bazel builds @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19389 Guard npm update readiness @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19610 Support end_turn in response.completed @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19606 permissions: make runtime config profile-backed @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19392 permissions: derive compatibility policies from profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19484 Lift app-server JSON-RPC error handling to request boundary @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19487 [codex] Move config loading into codex-config @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19726 Fix codex-core config test type paths @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19727 test: increase core-all-test shard count to 16 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19605 Delete unused ResponseItem::Message.end_turn @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19394 permissions: remove core legacy policy round trips @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19395 permissions: finish profile-backed app surfaces @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19736 permissions: constrain requirements as profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19737 permissions: derive legacy exec policies at boundaries @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19779 Add Codex issue digest skill @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19813 nit: one more fix @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19510 Hide rewind preview when no user message exists @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19709 Render delegated patch approval details @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19762 refactor: make auth loading async @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19854 ci: pin npm staging smoke test to a recent rust-release run @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19851 ci: migrate Bazel setup away from archived setup-bazelisk @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19863 [codex-analytics] remove ga flag @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19865 Cap original-detail image token estimates @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19591 Fix filtered thread-list resume regression in TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19513 Delay approval prompts while typing @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19706 Preserve TUI markdown list spacing after code blocks @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19841 permissions: remove cwd special path @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19492 Streamline thread start handler @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19493 Streamline thread mutation handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19494 Streamline thread read handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19839 [codex] Trace cancelled inference streams @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19495 Streamline thread resume and fork handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19497 Streamline turn and realtime handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19498 Streamline review and feedback handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19772 permissions: derive config defaults as profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19836 disallow fileparams metadata for custom mcps @colby-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19892 Refactor exec-server filesystem API into codex-file-system @miz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19481 Remove ghost snapshots @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19773 permissions: require profiles in TUI thread state @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19917 Allow /statusline and /title slash commands during active turns
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19912 Clarify PR template invitation requirement @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19630 Avoid persisting ShutdownComplete after thread shutdown @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19774 permissions: make SessionConfigured profile-only @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19920 Allow large remote app-server resume responses @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19776 permissions: store thread sessions as profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19961 feat: fix hinting 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19963 feat: fix hinting 3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19904 fix: configure AgentIdentity AuthAPI base URL @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19832 Preserve assistant phase for replayed messages @friel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19625 Reset TUI keyboard reporting on exit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#18593 feat(tui): add configurable keymap support @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19929 TUI: use cumulative turn duration for worked-for separator @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19473 Add turn start timestamp to turn metadata @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19847 Enforce workspace metadata protections in Seatbelt @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19901 feat(tui): suggest plan mode from composer drafts @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19931 Move local /resume cwd filtering into thread/list @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20002 fix(network-proxy): tighten network proxy bypass defaults @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19900 permissions: add built-in default profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19432 [codex] Add token usage to turn tracing spans @charley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20001 fix(network-proxy): harden linux proxy bridge helpers @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19959 Fix log db batch flush flake @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#17373 app-server: run initialized rpcs with keyed serialization @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19999 fix(network-proxy): recheck network proxy connect targets @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20052 Make MultiAgentV2 wait minimum configurable @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20066 [rollout-trace] Include x-request-id in rollout trace. @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19995 fix(network-proxy): normalize network proxy host matching @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20092 Return None when auth refresh fails @gpeal'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20097 Refine Codex issue digest summaries @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20015 core tests: configure profiles directly @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20021 core tests: migrate view image turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20026 core tests: migrate plan item turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20028 core tests: migrate permissions message tests to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20030 core tests: migrate exec policy turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20032 core tests: migrate prompt caching turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20033 core tests: migrate request permissions tool turns to profiles
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20034 core tests: migrate zsh-fork permissions to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20035 core tests: migrate compact turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20037 core tests: migrate rmcp turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20040 core tests: migrate apply patch turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20041 core tests: migrate hook turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20072 Support disabling tool suggest for specific tools. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20108 fix: restore live event submit path for apply patch tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19939 Restore TUI working status after steer message is set @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20049 feat: expose provider capability bounds to app server clients @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20112 Soften skill description budget warnings @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20058 Add environment provider snapshot @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20133 chore(cli) deprecate --full-auto @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20144 Fix migrated hook path rewriting @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20042 Fix Windows pseudoconsole attribute handling for sandboxed PTY
      sessions @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20082 Use /goal resume for paused goals @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20172 TUI: Remove core protocol dependency [1/7] @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19211 Improve Windows process management edge cases @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20123 [rollout-tracer] Match analysis messages on encrypted id. @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20173 TUI: Remove core protocol dependency [2/7] @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20174 TUI: Remove core protocol dependency [3/7] @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20141 Add ThreadManager sample crate @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19184 fix: handle deferred network proxy denials @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#17088 [codex-analytics] ingest server requests and responses @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20091 [tool_suggest] Improve tool_suggest triggering conditions. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20258 app-server: fix outgoing sender test setup @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20050 [app-server] type client response payloads @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20059 [app-server] centralize client response analytics @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20242 docs: discourage `#[async_trait]` and `#[allow(async_fn_in_trait)]`
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19620 Escape turn metadata headers as ASCII JSON @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20243 Add codex-core public API listing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20271 chore: increase release build timeout from 60 min to 90 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20261 Consume ai-title from external sessions and add end marker @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20282 tui: return from side chat on Ctrl-D @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20080 [codex-analytics] prevent stale guardian events from satisfying
      reused reviews @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20291 app-server: remove dead api version handling from bespoke events
      @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20095 permissions: expose active profile metadata @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19840 Add persisted hook enablement state @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20343 ci: increase Windows release workflow timeouts @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 145-other-changes-in-rust-v0-128-0
  source_release: codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89
  source_type: github_releases
  theme: uncategorized
  title: 145 other changes in rust-v0.128.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89]]'
source_type: github_releases
theme: uncategorized
title: 145 other changes in rust-v0.128.0
type: change
---

<!-- chronolog:begin region="header" -->
# 145 other changes in rust-v0.128.0

**Codex CLI** · 2026-04-30 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.128.0) · from [[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Clarified contributor-facing docs, including the PR template, Rust async trait guidance, and README wording. (#19912, #20242, #19514)

> Added a checked-in `codex-core` public API listing and a ThreadManager sample crate. (#20243, #20141)

> Published `codex-app-server` release artifacts, stopped publishing GNU Linux binaries, and increased release workflow timeouts. (#19447, #19445, #20271, #20343)

> Stabilized CI and release plumbing with Bazel setup migration, release smoke-test pinning, and updated workflow pins/timeouts. (#19851, #19854, #19472, #19609)

> #19124 Make MultiAgentV2 interruption markers assistant-authored @jif-oai

> #19354 chore: alias max_concurrent_threads_per_session @jif-oai

> #18392 Fix hang on turn/interrupt @danwang-oai

> #19283 check PID of named pipe consumer @iceweasel-oai

> #19163 Harden package-manager install policy @mcgrew-oai

> #19093 [codex] Omit fork turns from thread started notifications @euroelessar

> #19244 Update unix socket transport to use WebSocket upgrade @willwang-openai

> #19414 permissions: make legacy profile conversion cwd-free @bolinfest

> #18900 Migrate fork and resume reads to thread store @wiltzius-openai

> #19445 ci: stop publishing GNU Linux release artifacts @bolinfest

> #19447 ci: publish codex-app-server release artifacts @bolinfest

> #19422 Clarify bundled OpenAI Docs upgrade guide wording @kkahadze-oai

> #19266 [codex] add non-local thread store regression harness @wiltzius-openai

> #19098 feat: Compress skill paths with root aliases @xl-openai

> #19234 Refactor log DB into LogWriter interface @rasmusrygaard

> #19449 permissions: remove legacy read-only access modes @bolinfest

> #19472 ci: pin codex-action v1.7 @viyatb-oai

> #19468 Fix Bazel cargo_bin runfiles paths @fjord-oai

> #19410 Remove js_repl feature @fjord-oai

> #18073 Add goal persistence foundation (1 / 5) @etraut-openai

> #18074 Add goal app-server API (2 / 5) @etraut-openai

> #18076 Add goal core runtime (4 / 5) @etraut-openai

> #18077 Add goal TUI UX (5 / 5) @etraut-openai

> #19454 Split approval matrix test groups @dylan-hurd-oai

> #19514 Fix codex-rs README grammar @etraut-openai

> #19459 Enable unavailable dummy tools by default @mzeng-openai

> #19578 fix: increase Bazel timeout to 45 minutes @bolinfest

> #19595 [codex] Bypass managed network for escalated exec @viyatb-oai

> #19609 fix: restore 30-minute timeout for Bazel builds @bolinfest

> #19389 Guard npm update readiness @shijie-oai

> #19610 Support end_turn in response.completed @andmis

> #19606 permissions: make runtime config profile-backed @bolinfest

> #19392 permissions: derive compatibility policies from profiles @bolinfest

> #19484 Lift app-server JSON-RPC error handling to request boundary @pakrym-oai

> #19487 [codex] Move config loading into codex-config @pakrym-oai

> #19726 Fix codex-core config test type paths @pakrym-oai

> #19727 test: increase core-all-test shard count to 16 @bolinfest

> #19605 Delete unused ResponseItem::Message.end_turn @andmis

> #19394 permissions: remove core legacy policy round trips @bolinfest

> #19395 permissions: finish profile-backed app surfaces @bolinfest

> #19736 permissions: constrain requirements as profiles @bolinfest

> #19737 permissions: derive legacy exec policies at boundaries @bolinfest

> #19779 Add Codex issue digest skill @etraut-openai

> #19813 nit: one more fix @jif-oai

> #19510 Hide rewind preview when no user message exists @etraut-openai

> #19709 Render delegated patch approval details @etraut-openai

> #19762 refactor: make auth loading async @efrazer-oai

> #19854 ci: pin npm staging smoke test to a recent rust-release run @bolinfest

> #19851 ci: migrate Bazel setup away from archived setup-bazelisk @bolinfest

> #19863 [codex-analytics] remove ga flag @rhan-oai

> #19865 Cap original-detail image token estimates @fjord-oai

> #19591 Fix filtered thread-list resume regression in TUI @etraut-openai

> #19513 Delay approval prompts while typing @etraut-openai

> #19706 Preserve TUI markdown list spacing after code blocks @etraut-openai

> #19841 permissions: remove cwd special path @bolinfest

> #19492 Streamline thread start handler @pakrym-oai

> #19493 Streamline thread mutation handlers @pakrym-oai

> #19494 Streamline thread read handlers @pakrym-oai

> #19839 [codex] Trace cancelled inference streams @cassirer-openai

> #19495 Streamline thread resume and fork handlers @pakrym-oai

> #19497 Streamline turn and realtime handlers @pakrym-oai

> #19498 Streamline review and feedback handlers @pakrym-oai

> #19772 permissions: derive config defaults as profiles @bolinfest

> #19836 disallow fileparams metadata for custom mcps @colby-oai

> #19892 Refactor exec-server filesystem API into codex-file-system @miz-openai

> #19481 Remove ghost snapshots @pakrym-oai

> #19773 permissions: require profiles in TUI thread state @bolinfest

> #19917 Allow /statusline and /title slash commands during active turns @canvrno-oai

> #19912 Clarify PR template invitation requirement @etraut-openai

> #19630 Avoid persisting ShutdownComplete after thread shutdown @etraut-openai

> #19774 permissions: make SessionConfigured profile-only @bolinfest

> #19920 Allow large remote app-server resume responses @etraut-openai

> #19776 permissions: store thread sessions as profiles @bolinfest

> #19961 feat: fix hinting 2 @jif-oai

> #19963 feat: fix hinting 3 @jif-oai

> #19904 fix: configure AgentIdentity AuthAPI base URL @efrazer-oai

> #19832 Preserve assistant phase for replayed messages @friel-openai

> #19625 Reset TUI keyboard reporting on exit @etraut-openai

> #18593 feat(tui): add configurable keymap support @fcoury-oai

> #19929 TUI: use cumulative turn duration for worked-for separator @etraut-openai

> #19473 Add turn start timestamp to turn metadata @mchen-oai

> #19847 Enforce workspace metadata protections in Seatbelt @evawong-oai

> #19901 feat(tui): suggest plan mode from composer drafts @fcoury-oai

> #19931 Move local /resume cwd filtering into thread/list @canvrno-oai

> #20002 fix(network-proxy): tighten network proxy bypass defaults @viyatb-oai

> #19900 permissions: add built-in default profiles @bolinfest

> #19432 [codex] Add token usage to turn tracing spans @charley-openai

> #20001 fix(network-proxy): harden linux proxy bridge helpers @viyatb-oai

> #19959 Fix log db batch flush flake @dylan-hurd-oai

> #17373 app-server: run initialized rpcs with keyed serialization @euroelessar

> #19999 fix(network-proxy): recheck network proxy connect targets @viyatb-oai

> #20052 Make MultiAgentV2 wait minimum configurable @jif-oai

> #20066 [rollout-trace] Include x-request-id in rollout trace. @cassirer-openai

> #19995 fix(network-proxy): normalize network proxy host matching @viyatb-oai

> #20092 Return None when auth refresh fails @gpeal

> #20097 Refine Codex issue digest summaries @etraut-openai

> #20015 core tests: configure profiles directly @bolinfest

> #20021 core tests: migrate view image turns to profiles @bolinfest

> #20026 core tests: migrate plan item turns to profiles @bolinfest

> #20028 core tests: migrate permissions message tests to profiles @bolinfest

> #20030 core tests: migrate exec policy turns to profiles @bolinfest

> #20032 core tests: migrate prompt caching turns to profiles @bolinfest

> #20033 core tests: migrate request permissions tool turns to profiles @bolinfest

> #20034 core tests: migrate zsh-fork permissions to profiles @bolinfest

> #20035 core tests: migrate compact turns to profiles @bolinfest

> #20037 core tests: migrate rmcp turns to profiles @bolinfest

> #20040 core tests: migrate apply patch turns to profiles @bolinfest

> #20041 core tests: migrate hook turns to profiles @bolinfest

> #20072 Support disabling tool suggest for specific tools. @mzeng-openai

> #20108 fix: restore live event submit path for apply patch tests @bolinfest

> #19939 Restore TUI working status after steer message is set @canvrno-oai

> #20049 feat: expose provider capability bounds to app server clients @celia-oai

> #20112 Soften skill description budget warnings @xl-openai

> #20058 Add environment provider snapshot @starr-openai

> #20133 chore(cli) deprecate --full-auto @dylan-hurd-oai

> #20144 Fix migrated hook path rewriting @alexsong-oai

> #20042 Fix Windows pseudoconsole attribute handling for sandboxed PTY sessions @iceweasel-oai

> #20082 Use /goal resume for paused goals @etraut-openai

> #20172 TUI: Remove core protocol dependency [1/7] @etraut-openai

> #19211 Improve Windows process management edge cases @iceweasel-oai

> #20123 [rollout-tracer] Match analysis messages on encrypted id. @cassirer-openai

> #20173 TUI: Remove core protocol dependency [2/7] @etraut-openai

> #20174 TUI: Remove core protocol dependency [3/7] @etraut-openai

> #20141 Add ThreadManager sample crate @pakrym-oai

> #19184 fix: handle deferred network proxy denials @viyatb-oai

> #17088 [codex-analytics] ingest server requests and responses @rhan-oai

> #20091 [tool_suggest] Improve tool_suggest triggering conditions. @mzeng-openai

> #20258 app-server: fix outgoing sender test setup @sayan-oai

> #20050 [app-server] type client response payloads @rhan-oai

> #20059 [app-server] centralize client response analytics @rhan-oai

> #20242 docs: discourage `#[async_trait]` and `#[allow(async_fn_in_trait)]` @bolinfest

> #19620 Escape turn metadata headers as ASCII JSON @etraut-openai

> #20243 Add codex-core public API listing @pakrym-oai

> #20271 chore: increase release build timeout from 60 min to 90 @bolinfest

> #20261 Consume ai-title from external sessions and add end marker @alexsong-oai

> #20282 tui: return from side chat on Ctrl-D @etraut-openai

> #20080 [codex-analytics] prevent stale guardian events from satisfying reused reviews @rhan-oai

> #20291 app-server: remove dead api version handling from bespoke events @pakrym-oai

> #20095 permissions: expose active profile metadata @bolinfest

> #19840 Add persisted hook enablement state @abhinav-oai

> #20343 ci: increase Windows release workflow timeouts @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.128.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-30-2-interface-experience-changes-in-rust-v0-128-0|2 Interface Experience changes in rust-v0.128.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-30-19805-add-multiagentv2-root-and-subagent-context-hints-jif-oai|♯19805 Add MultiAgentV2 root and subagent context hints @jif-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-30-3-mobile-and-desktop-changes-in-rust-v0-128-0|3 Mobile and Desktop changes in rust-v0.128.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0|12 Memory and Personalization changes in rust-v0.128.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-30-19-agent-mode-changes-in-rust-v0-128-0|19 Agent Mode changes in rust-v0.128.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-30-20149-reduce-the-surface-of-collaboration-modes-pakrym-oai|♯20149 Reduce the surface of collaboration modes @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-30-14-developer-workflow-changes-in-rust-v0-128-0|14 Developer Workflow changes in rust-v0.128.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]] · Image Generation
- [[Changes/Codex CLI/2026-04-30-3-account-and-access-changes-in-rust-v0-128-0|3 Account and Access changes in rust-v0.128.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045 Fix plan mode nudge test after task completion signature change @canvrno-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-30-10-model-support-changes-in-rust-v0-128-0|10 Model Support changes in rust-v0.128.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-30-312d98&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-30-145-other-changes-in-rust-v0-128-0.md%0ACard%20ID%3A%20codex-cli-2026-04-30-312d98%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.128.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->