---
card_id: codex-cli-2026-08-18-215fc3
date: '2026-08-18'
description: 'Codex CLI · 2026-08-18 · Other changes: 231 changes in 0.148.0 — Export
  complete TUI conversations to Markdown with `/export`, either to the clipboard or
  a new…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5135dc8f8abbc0d8af07db3433e4380f32f7304b566daa06b19aaec8733d7159
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-18-215fc3
  comparison: ''
  date: '2026-08-18'
  description: 'Codex CLI — 0.148.0: 231 other changes'
  evidence:
  - quote: Export complete TUI conversations to Markdown with `/export`, either to
      the clipboard or a new file. (#37358)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: 'Draft prompts while the TUI initializes, with resume and fork progress
      shown during startup. (#38642, #38788)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: 'Resumed sessions now restore their persisted working directory and approval
      policy, with more accurate transcript previews. (#37198, #37368, #38605)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: The bundled skill-creator guide is more focused, and validation now rejects
      unfinished TODO placeholders. (#38384)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37191 Preserve legacy semantics during rollout migration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37198 Prefer persisted cwd when reading local threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37199 Track thread archive analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37204 Add durable user-message queue dispatch @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37206 Add a unified image budget @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37211 Harden network proxy MITM authorization @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37279 Avoid cloning immutable metadata on tool search cache hits @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37335 Fully repaint inline viewports after history overlap @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37336 Use step environments for extension turn input @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37339 Reload app-server telemetry after account changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37340 Consolidate deferred environment provisioning APIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37341 Support content references for inline visualizations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37342 Preserve foreign cwd URIs for turn-input contributors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37343 Stage Bazel app-server test binaries in `TEST_TMPDIR` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37348 Add rollout migration tooling and background migration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37349 Mount a minimal `/dev` in full-filesystem Bubblewrap sandboxes
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37350 Allow `ThreadManager` to customize thread ID generation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37352 Configure the default code-mode exec yield timeout @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37354 Retry busy app-server test executable spawns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37358 Add Markdown conversation export to the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37360 Use consistent TUI input placeholders @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37367 Add session forking to `codex exec` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37368 Restore approval policy when resuming threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37389 Add tool namespace metadata configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37400 Rename the tool registry metadata setting @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37406 Add a loader for executor-local config layers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37408 Add executor-local config reads to the exec server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37424 Cap project instructions across environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37434 Add process diagnostics snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37446 Preserve base instruction provenance across sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37457 Remove the legacy core skill loader @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37461 Remove the unused remote skills client @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37466 Move skill config rule resolution into `codex-config` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37470 Expose app-server diagnostics through the experimental API @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37478 Shard state unit tests under Bazel @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37479 Report temporary directories in exec-server environment info @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37480 Delegate remote process sandboxing to the executor @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37483 Interrupt active code-mode cells with their turn @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37485 Keep response streams alive through connection failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37486 Expose runtime activity in server diagnostics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37488 Generalize skill locator aliases across providers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37492 Include tool namespace inventory in turn metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37497 Limit payload traces in diagnostic logs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37498 Preserve child waiters during process termination @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37500 Remove the legacy code-mode tool metadata inventory @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37503 Move host skill prompt injection into the skills extension @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37504 Disable Nagle''s algorithm for code-mode WebSockets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37505 Remove the codex-core-skills crate @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37510 Define the code-mode host gRPC protocol @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37513 Reuse parent compactions in Guardian review sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37527 Terminate timed-out hook process trees @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37530 Implement the gRPC code-mode host service @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37538 Expose execution mode in hook listings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37610 Add workload identity token exchange support @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37618 Use step environments for Guardian approval reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37622 Include buffered turns when editing prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37644 Generalize hook handler execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37654 Advertise environment config read support @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37709 Keep wrapped composer whitespace with following text @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37723 Report I/O subtypes for session config import failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37745 Add gRPC TCP transport to the code-mode host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37747 Bound Cursor project path resolution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37757 Add a line-ending preservation mode to `apply_patch` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37758 Add a feature flag to preserve apply_patch line endings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37788 Use native transparency in the imagegen skill @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37808 Simplify package-based skill reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37810 Support packaged defaults in config layering @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37812 Keep multi-workspace skill listings consistent @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37838 Tighten the skills extension API surface @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37862 Rename environment config for turn scope @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37867 Reject duplicate resolved paths in apply_patch @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37871 Extract persisted history types into a dedicated crate @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37874 Keep runtime summary metrics out of Statsig exports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37878 Add configurable goal token budget limits @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37886 Extend bundled package discovery and expose its version @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37891 Use thread configuration for `app/read` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37892 Validate images before returning `view_image` output @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37895 Add configurable Responses API request metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37898 Add appearance metadata to thread sections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37901 Make submission operations move-only @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37902 Defer `view_image` processing to history insertion @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37906 Make gRPC code-mode notifications fire-and-forget @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37908 Apply refreshed cloud config bundles to later sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37922 Extract reusable code-mode host test support @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37926 Distinguish turn-start thread persistence @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37939 Validate images before returning `view_image` output @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37979 Honor per-directory bundled skill settings in `skills/list` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#37984 Stop re-exporting skill APIs from `codex-core` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38011 Remove config lockfile support @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38020 Retry transient exec-server startup failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38026 Fail closed on unsafe Linux unreadable globs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38032 Hide approved Guardian assessments from TUI history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38033 Use session metadata to validate thread history paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38034 Filter live rollout items in place @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38036 Limit TUI streaming traces in SQLite logs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38041 Add gRPC-backed code-mode sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38044 Compact code mode tool calls in TUI history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38047 Add turn-aware response item injection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38049 Harden network proxy credential brokerage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38056 Configure PSP routing through the feature system @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38058 Preserve harness metadata across conversation history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38060 Disable storage for Azure Responses requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38066 Track resource-backed skill invocations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38067 Scope environment readiness config to thread attachments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38072 Forward gRPC code-mode callbacks to session delegates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38074 Track implicit executor skill invocations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38075 Respect rendered width when adding TUI history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38078 Reduce cloning in world-state patch handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38083 Remove standard form input from app-server docs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38084 Allow empty input to start a turn @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38092 Simplify queued user message admission @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38127 Distinguish rollout IDs from thread IDs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38167 Read executor skill packages directly @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38170 Notify running turn watchers only on count changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38172 Update `lru` and `webbrowser` dependencies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38179 Embed defaults in the packaged config layer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38183 Add conservative restriction helpers for tool policies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38186 Stop overriding environments in the skills user-turn test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38205 Enforce non-interactive approval policy for Codex delegates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38214 Avoid allocations when sanitizing TUI user text @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38227 Add a flag to retain client developer messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38228 Detect implicit skill invocations from PowerShell reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38232 Track root turns across delegated Codex requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38241 Include Node REPL policy in turn metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38242 Cache stable active-cell layout measurements @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38243 Track client-authored developer messages in rollout history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38244 Resolve paginated thread history by rollout ID @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38256 Report the latest rejection from multiple network reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38257 Reconnect gRPC code-mode sessions after host restarts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38261 Resolve skill package aliases in `skills.read` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38268 Expose executor skill roots from `skills.read` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38270 Add per-thread usage queries to the backend client @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38272 Stamp conversation history items with creation times @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38274 Represent persisted world state as JSON objects @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38275 Unify turn input submission and routing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38280 Use protobuf''s built-in Bazel proto rule @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38281 Show estimated thread usage in `/status` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38282 Add thread usage to TUI status surfaces @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38285 Move `codex-execpolicy` to protocol dev dependencies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38288 Support gRPC code-mode hosts in app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38291 Remove unused apply_patch prompt fallback @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38292 Add durable reverts for paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38303 Add interrupted turn recovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38321 Make gRPC code-mode yield tests deterministic @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38336 Add Guardian V2 extension scaffold @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38356 Support sandboxed file streaming in exec-server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38358 Optimize orphan output normalization @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38361 Test hook rejection for explicitly started queue items @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38362 Stabilize exec-server byte-budget tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38368 Add the Guardian V2 Luna sampler @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38377 Constrain Guardian reviews to parent filesystem permissions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38380 Preserve user message styling when wrapping long URLs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38381 Prevent unread events from blocking in-process requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38383 Return Luna samples when streamed JSON completes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38384 Refine skill creation guidance and validation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38390 Use effective permissions when trusting app-server projects @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38396 Reap orphaned processes in Linux sandboxes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38397 Include Node REPL results in Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38399 Preserve floating-point values when decoding rollout lines @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38400 Refresh tracing interest in the token estimate test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38406 Pool Guardian sampling WebSocket connections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38409 Classify tool calls in the Guardian V2 extension @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38413 Allow metadata updates without materializing threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38415 Recognize PowerShell `Get-Content` file reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38416 Honor filesystem permissions for app file uploads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38419 Apply Codex attribution to app-created commits @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38420 Recover capability discovery after executor disconnects @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38424 Fail closed when workload identity initialization fails @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38426 Protect workload identity auth in app-server account RPCs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38427 Add Guardian guidance for Node REPL tool calls @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38440 Add app-server support for reverting paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38447 Add running-task exit choices to local daemon sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38452 Add structured telemetry for response retries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38454 Include node_repl images in Guardian review evidence @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38456 Add experimental thread queue APIs to app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38460 Add an `AbsolutePathBuf` conversion for `FileSystemPath` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38463 Preserve thread subscriptions across revert reloads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38470 Add an Amazon Bedrock Runtime provider @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38494 Verify bundled bwrap in Bazel builds @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38521 Carry environment config in turn selections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38527 Configure Guardian sampling for responses lite @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38540 Record Guardian V2 risk scores on threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38553 Initialize Guardian V2 samplers per thread @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38555 Preserve Guardian transcript boundaries in sampling input @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38564 Reuse compatible parent compactions in Guardian V2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38569 Require automatic review for high-risk Guardian v2 actions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38579 Report thread storage changes after rollout migration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38580 Keep the latest Guardian risk score during concurrent sampling
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38581 Honor cloud-managed requirements in feature listings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38586 Bound Guardian V2 tool actions before risk classification @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38596 Prioritize new Guardian classifications under load @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38597 Install Guardian V2 in the app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38601 Make unbounded connection retries configurable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38604 Avoid paginated resume requests for verified legacy rollouts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38606 Allow larger gRPC code mode tool descriptions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38610 Support workload identity in remote exec-server auth @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38612 Skip stale Guardian risk score persistence @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38615 Remove the gRPC code-mode enabled tool limit @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38616 Route escalated approval retries through Guardian @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38618 Apply Guardian policies to v2 risk classification @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38621 Preserve large gRPC code-mode tool errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38624 Open notes when accepting the request input Other option @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38628 Make Guardian v2 risk classification configurable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38630 Remove the gRPC code-mode open session limit @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38635 Remove repository-local Codex skills @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38639 Render the initial TUI session header before input @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38641 Harden TUI startup input handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38642 Keep the composer editable during TUI startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38645 Deliver gRPC code-mode notifications without truncation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38646 Read Apple notarization issuer ID from Key Vault @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38647 Add an override to skip project configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38649 Reuse the TUI startup account response during bootstrap @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38662 Delete Thai combining marks one at a time in the composer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38664 Resolve local JSON Schema refs in Code Mode types @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38670 Forward executor network policy decisions for auditing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38675 Exclude shortcut-modified input from TUI paste bursts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38678 Preserve environment configuration ownership @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38681 Preserve HTTP fallback for delegated sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38682 Surface misalignment policy violations as typed errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38684 Support pending environment attachment configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38704 Normalize CRLF line endings in pasted text @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38746 Remove the TUI test dependency on `codex-cli` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38774 Use paginated history for persistent exec threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38788 Show resume and fork status during TUI startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38795 Add storage diagnostics to `codex doctor` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38800 Route executor policy audits through log-only telemetry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  - quote: '#38806 Add a health endpoint to the code-mode gRPC listener @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.148.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 231-other-changes-in-rust-v0-148-0
  source_release: codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae
  source_type: github_releases
  theme: uncategorized
  title: 231 other changes in rust-v0.148.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae]]'
source_type: github_releases
theme: uncategorized
title: 231 other changes in rust-v0.148.0
type: change
---

<!-- chronolog:begin region="header" -->
# 231 other changes in rust-v0.148.0

**Codex CLI** · 2026-08-18 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.148.0) · from [[Releases/Codex CLI/codex-cli-2026-08-18-rust-v0-148-0-github-372686337-4265c0ae|0.148.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Export complete TUI conversations to Markdown with `/export`, either to the clipboard or a new file. (#37358)

> Draft prompts while the TUI initializes, with resume and fork progress shown during startup. (#38642, #38788)

> Resumed sessions now restore their persisted working directory and approval policy, with more accurate transcript previews. (#37198, #37368, #38605)

> The bundled skill-creator guide is more focused, and validation now rejects unfinished TODO placeholders. (#38384)

> #37191 Preserve legacy semantics during rollout migration @copyberry

> #37198 Prefer persisted cwd when reading local threads @copyberry

> #37199 Track thread archive analytics @copyberry

> #37204 Add durable user-message queue dispatch @copyberry

> #37206 Add a unified image budget @copyberry

> #37211 Harden network proxy MITM authorization @copyberry

> #37279 Avoid cloning immutable metadata on tool search cache hits @copyberry

> #37335 Fully repaint inline viewports after history overlap @copyberry

> #37336 Use step environments for extension turn input @copyberry

> #37339 Reload app-server telemetry after account changes @copyberry

> #37340 Consolidate deferred environment provisioning APIs @copyberry

> #37341 Support content references for inline visualizations @copyberry

> #37342 Preserve foreign cwd URIs for turn-input contributors @copyberry

> #37343 Stage Bazel app-server test binaries in `TEST_TMPDIR` @copyberry

> #37348 Add rollout migration tooling and background migration @copyberry

> #37349 Mount a minimal `/dev` in full-filesystem Bubblewrap sandboxes @copyberry

> #37350 Allow `ThreadManager` to customize thread ID generation @copyberry

> #37352 Configure the default code-mode exec yield timeout @copyberry

> #37354 Retry busy app-server test executable spawns @copyberry

> #37358 Add Markdown conversation export to the TUI @copyberry

> #37360 Use consistent TUI input placeholders @copyberry

> #37367 Add session forking to `codex exec` @copyberry

> #37368 Restore approval policy when resuming threads @copyberry

> #37389 Add tool namespace metadata configuration @copyberry

> #37400 Rename the tool registry metadata setting @copyberry

> #37406 Add a loader for executor-local config layers @copyberry

> #37408 Add executor-local config reads to the exec server @copyberry

> #37424 Cap project instructions across environments @copyberry

> #37434 Add process diagnostics snapshots @copyberry

> #37446 Preserve base instruction provenance across sessions @copyberry

> #37457 Remove the legacy core skill loader @copyberry

> #37461 Remove the unused remote skills client @copyberry

> #37466 Move skill config rule resolution into `codex-config` @copyberry

> #37470 Expose app-server diagnostics through the experimental API @copyberry

> #37478 Shard state unit tests under Bazel @copyberry

> #37479 Report temporary directories in exec-server environment info @copyberry

> #37480 Delegate remote process sandboxing to the executor @copyberry

> #37483 Interrupt active code-mode cells with their turn @copyberry

> #37485 Keep response streams alive through connection failures @copyberry

> #37486 Expose runtime activity in server diagnostics @copyberry

> #37488 Generalize skill locator aliases across providers @copyberry

> #37492 Include tool namespace inventory in turn metadata @copyberry

> #37497 Limit payload traces in diagnostic logs @copyberry

> #37498 Preserve child waiters during process termination @copyberry

> #37500 Remove the legacy code-mode tool metadata inventory @copyberry

> #37503 Move host skill prompt injection into the skills extension @copyberry

> #37504 Disable Nagle's algorithm for code-mode WebSockets @copyberry

> #37505 Remove the codex-core-skills crate @copyberry

> #37510 Define the code-mode host gRPC protocol @copyberry

> #37513 Reuse parent compactions in Guardian review sessions @copyberry

> #37527 Terminate timed-out hook process trees @copyberry

> #37530 Implement the gRPC code-mode host service @copyberry

> #37538 Expose execution mode in hook listings @copyberry

> #37610 Add workload identity token exchange support @copyberry

> #37618 Use step environments for Guardian approval reviews @copyberry

> #37622 Include buffered turns when editing prompts @copyberry

> #37644 Generalize hook handler execution @copyberry

> #37654 Advertise environment config read support @copyberry

> #37709 Keep wrapped composer whitespace with following text @copyberry

> #37723 Report I/O subtypes for session config import failures @copyberry

> #37745 Add gRPC TCP transport to the code-mode host @copyberry

> #37747 Bound Cursor project path resolution @copyberry

> #37757 Add a line-ending preservation mode to `apply_patch` @copyberry

> #37758 Add a feature flag to preserve apply_patch line endings @copyberry

> #37788 Use native transparency in the imagegen skill @copyberry

> #37808 Simplify package-based skill reads @copyberry

> #37810 Support packaged defaults in config layering @copyberry

> #37812 Keep multi-workspace skill listings consistent @copyberry

> #37838 Tighten the skills extension API surface @copyberry

> #37862 Rename environment config for turn scope @copyberry

> #37867 Reject duplicate resolved paths in apply_patch @copyberry

> #37871 Extract persisted history types into a dedicated crate @copyberry

> #37874 Keep runtime summary metrics out of Statsig exports @copyberry

> #37878 Add configurable goal token budget limits @copyberry

> #37886 Extend bundled package discovery and expose its version @copyberry

> #37891 Use thread configuration for `app/read` @copyberry

> #37892 Validate images before returning `view_image` output @copyberry

> #37895 Add configurable Responses API request metadata @copyberry

> #37898 Add appearance metadata to thread sections @copyberry

> #37901 Make submission operations move-only @copyberry

> #37902 Defer `view_image` processing to history insertion @copyberry

> #37906 Make gRPC code-mode notifications fire-and-forget @copyberry

> #37908 Apply refreshed cloud config bundles to later sessions @copyberry

> #37922 Extract reusable code-mode host test support @copyberry

> #37926 Distinguish turn-start thread persistence @copyberry

> #37939 Validate images before returning `view_image` output @copyberry

> #37979 Honor per-directory bundled skill settings in `skills/list` @copyberry

> #37984 Stop re-exporting skill APIs from `codex-core` @copyberry

> #38011 Remove config lockfile support @copyberry

> #38020 Retry transient exec-server startup failures @copyberry

> #38026 Fail closed on unsafe Linux unreadable globs @copyberry

> #38032 Hide approved Guardian assessments from TUI history @copyberry

> #38033 Use session metadata to validate thread history paths @copyberry

> #38034 Filter live rollout items in place @copyberry

> #38036 Limit TUI streaming traces in SQLite logs @copyberry

> #38041 Add gRPC-backed code-mode sessions @copyberry

> #38044 Compact code mode tool calls in TUI history @copyberry

> #38047 Add turn-aware response item injection @copyberry

> #38049 Harden network proxy credential brokerage @copyberry

> #38056 Configure PSP routing through the feature system @copyberry

> #38058 Preserve harness metadata across conversation history @copyberry

> #38060 Disable storage for Azure Responses requests @copyberry

> #38066 Track resource-backed skill invocations @copyberry

> #38067 Scope environment readiness config to thread attachments @copyberry

> #38072 Forward gRPC code-mode callbacks to session delegates @copyberry

> #38074 Track implicit executor skill invocations @copyberry

> #38075 Respect rendered width when adding TUI history @copyberry

> #38078 Reduce cloning in world-state patch handling @copyberry

> #38083 Remove standard form input from app-server docs @copyberry

> #38084 Allow empty input to start a turn @copyberry

> #38092 Simplify queued user message admission @copyberry

> #38127 Distinguish rollout IDs from thread IDs @copyberry

> #38167 Read executor skill packages directly @copyberry

> #38170 Notify running turn watchers only on count changes @copyberry

> #38172 Update `lru` and `webbrowser` dependencies @copyberry

> #38179 Embed defaults in the packaged config layer @copyberry

> #38183 Add conservative restriction helpers for tool policies @copyberry

> #38186 Stop overriding environments in the skills user-turn test @copyberry

> #38205 Enforce non-interactive approval policy for Codex delegates @copyberry

> #38214 Avoid allocations when sanitizing TUI user text @copyberry

> #38227 Add a flag to retain client developer messages @copyberry

> #38228 Detect implicit skill invocations from PowerShell reads @copyberry

> #38232 Track root turns across delegated Codex requests @copyberry

> #38241 Include Node REPL policy in turn metadata @copyberry

> #38242 Cache stable active-cell layout measurements @copyberry

> #38243 Track client-authored developer messages in rollout history @copyberry

> #38244 Resolve paginated thread history by rollout ID @copyberry

> #38256 Report the latest rejection from multiple network reviews @copyberry

> #38257 Reconnect gRPC code-mode sessions after host restarts @copyberry

> #38261 Resolve skill package aliases in `skills.read` @copyberry

> #38268 Expose executor skill roots from `skills.read` @copyberry

> #38270 Add per-thread usage queries to the backend client @copyberry

> #38272 Stamp conversation history items with creation times @copyberry

> #38274 Represent persisted world state as JSON objects @copyberry

> #38275 Unify turn input submission and routing @copyberry

> #38280 Use protobuf's built-in Bazel proto rule @copyberry

> #38281 Show estimated thread usage in `/status` @copyberry

> #38282 Add thread usage to TUI status surfaces @copyberry

> #38285 Move `codex-execpolicy` to protocol dev dependencies @copyberry

> #38288 Support gRPC code-mode hosts in app server @copyberry

> #38291 Remove unused apply_patch prompt fallback @copyberry

> #38292 Add durable reverts for paginated threads @copyberry

> #38303 Add interrupted turn recovery @copyberry

> #38321 Make gRPC code-mode yield tests deterministic @copyberry

> #38336 Add Guardian V2 extension scaffold @copyberry

> #38356 Support sandboxed file streaming in exec-server @copyberry

> #38358 Optimize orphan output normalization @copyberry

> #38361 Test hook rejection for explicitly started queue items @copyberry

> #38362 Stabilize exec-server byte-budget tests @copyberry

> #38368 Add the Guardian V2 Luna sampler @copyberry

> #38377 Constrain Guardian reviews to parent filesystem permissions @copyberry

> #38380 Preserve user message styling when wrapping long URLs @copyberry

> #38381 Prevent unread events from blocking in-process requests @copyberry

> #38383 Return Luna samples when streamed JSON completes @copyberry

> #38384 Refine skill creation guidance and validation @copyberry

> #38390 Use effective permissions when trusting app-server projects @copyberry

> #38396 Reap orphaned processes in Linux sandboxes @copyberry

> #38397 Include Node REPL results in Guardian reviews @copyberry

> #38399 Preserve floating-point values when decoding rollout lines @copyberry

> #38400 Refresh tracing interest in the token estimate test @copyberry

> #38406 Pool Guardian sampling WebSocket connections @copyberry

> #38409 Classify tool calls in the Guardian V2 extension @copyberry

> #38413 Allow metadata updates without materializing threads @copyberry

> #38415 Recognize PowerShell `Get-Content` file reads @copyberry

> #38416 Honor filesystem permissions for app file uploads @copyberry

> #38419 Apply Codex attribution to app-created commits @copyberry

> #38420 Recover capability discovery after executor disconnects @copyberry

> #38424 Fail closed when workload identity initialization fails @copyberry

> #38426 Protect workload identity auth in app-server account RPCs @copyberry

> #38427 Add Guardian guidance for Node REPL tool calls @copyberry

> #38440 Add app-server support for reverting paginated threads @copyberry

> #38447 Add running-task exit choices to local daemon sessions @copyberry

> #38452 Add structured telemetry for response retries @copyberry

> #38454 Include node_repl images in Guardian review evidence @copyberry

> #38456 Add experimental thread queue APIs to app server @copyberry

> #38460 Add an `AbsolutePathBuf` conversion for `FileSystemPath` @copyberry

> #38463 Preserve thread subscriptions across revert reloads @copyberry

> #38470 Add an Amazon Bedrock Runtime provider @copyberry

> #38494 Verify bundled bwrap in Bazel builds @copyberry

> #38521 Carry environment config in turn selections @copyberry

> #38527 Configure Guardian sampling for responses lite @copyberry

> #38540 Record Guardian V2 risk scores on threads @copyberry

> #38553 Initialize Guardian V2 samplers per thread @copyberry

> #38555 Preserve Guardian transcript boundaries in sampling input @copyberry

> #38564 Reuse compatible parent compactions in Guardian V2 @copyberry

> #38569 Require automatic review for high-risk Guardian v2 actions @copyberry

> #38579 Report thread storage changes after rollout migration @copyberry

> #38580 Keep the latest Guardian risk score during concurrent sampling @copyberry

> #38581 Honor cloud-managed requirements in feature listings @copyberry

> #38586 Bound Guardian V2 tool actions before risk classification @copyberry

> #38596 Prioritize new Guardian classifications under load @copyberry

> #38597 Install Guardian V2 in the app server @copyberry

> #38601 Make unbounded connection retries configurable @copyberry

> #38604 Avoid paginated resume requests for verified legacy rollouts @copyberry

> #38606 Allow larger gRPC code mode tool descriptions @copyberry

> #38610 Support workload identity in remote exec-server auth @copyberry

> #38612 Skip stale Guardian risk score persistence @copyberry

> #38615 Remove the gRPC code-mode enabled tool limit @copyberry

> #38616 Route escalated approval retries through Guardian @copyberry

> #38618 Apply Guardian policies to v2 risk classification @copyberry

> #38621 Preserve large gRPC code-mode tool errors @copyberry

> #38624 Open notes when accepting the request input Other option @copyberry

> #38628 Make Guardian v2 risk classification configurable @copyberry

> #38630 Remove the gRPC code-mode open session limit @copyberry

> #38635 Remove repository-local Codex skills @copyberry

> #38639 Render the initial TUI session header before input @copyberry

> #38641 Harden TUI startup input handling @copyberry

> #38642 Keep the composer editable during TUI startup @copyberry

> #38645 Deliver gRPC code-mode notifications without truncation @copyberry

> #38646 Read Apple notarization issuer ID from Key Vault @copyberry

> #38647 Add an override to skip project configuration @copyberry

> #38649 Reuse the TUI startup account response during bootstrap @copyberry

> #38662 Delete Thai combining marks one at a time in the composer @copyberry

> #38664 Resolve local JSON Schema refs in Code Mode types @copyberry

> #38670 Forward executor network policy decisions for auditing @copyberry

> #38675 Exclude shortcut-modified input from TUI paste bursts @copyberry

> #38678 Preserve environment configuration ownership @copyberry

> #38681 Preserve HTTP fallback for delegated sessions @copyberry

> #38682 Surface misalignment policy violations as typed errors @copyberry

> #38684 Support pending environment attachment configuration @copyberry

> #38704 Normalize CRLF line endings in pasted text @copyberry

> #38746 Remove the TUI test dependency on `codex-cli` @copyberry

> #38774 Use paginated history for persistent exec threads @copyberry

> #38788 Show resume and fork status during TUI startup @copyberry

> #38795 Add storage diagnostics to `codex doctor` @copyberry

> #38800 Route executor policy audits through log-only telemetry @copyberry

> #38806 Add a health endpoint to the code-mode gRPC listener @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.148.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-18-57-apps-and-integrations-changes-in-rust-v0-148-0|57 Apps and Integrations changes in rust-v0.148.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-18-13-interface-experience-changes-in-rust-v0-148-0|13 Interface Experience changes in rust-v0.148.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-18-18-model-support-changes-in-rust-v0-148-0|18 Model Support changes in rust-v0.148.0]] · Model Support
- [[Changes/Codex CLI/2026-08-18-3-mobile-and-desktop-changes-in-rust-v0-148-0|3 Mobile and Desktop changes in rust-v0.148.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-18-5-developer-workflow-changes-in-rust-v0-148-0|5 Developer Workflow changes in rust-v0.148.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-18-38650-canonicalize-default-namespaces-in-grpc-subscription-filters-copyberry|♯38650 Canonicalize default namespaces in gRPC subscription filters @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-18-37828-track-running-unified-exec-processes-at-turn-completion-copyberry|♯37828 Track running unified exec processes at turn completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0|17 Safety and Privacy changes in rust-v0.148.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-18-16-account-and-access-changes-in-rust-v0-148-0|16 Account and Access changes in rust-v0.148.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-18-13-context-window-changes-in-rust-v0-148-0|13 Context Window changes in rust-v0.148.0]] · Context Window
- [[Changes/Codex CLI/2026-08-18-12-agent-mode-changes-in-rust-v0-148-0|12 Agent Mode changes in rust-v0.148.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-18-38024-expose-image-generation-usage-limit-failures-copyberry|♯38024 Expose image generation usage-limit failures @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-18-5-collaboration-changes-in-rust-v0-148-0|5 Collaboration changes in rust-v0.148.0]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-18-215fc3&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-18-231-other-changes-in-rust-v0-148-0.md%0ACard%20ID%3A%20codex-cli-2026-08-18-215fc3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.148.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->