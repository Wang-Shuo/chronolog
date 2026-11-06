---
card_id: codex-cli-2026-08-07-a60750
date: '2026-08-07'
description: 'Codex CLI · 2026-08-07 · Other changes: 196 changes in 0.147.0 — Enable
  automatically reviewed approvals with the new `--approve-for-me` CLI flag. (#36373)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bad66816dbe1c8688dfcf3711bbe2922e03720c75dd41f4cd64bfaa217d4aafe
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-07-a60750
  comparison: ''
  date: '2026-08-07'
  description: 'Codex CLI — 0.147.0: 196 other changes'
  evidence:
  - quote: Enable automatically reviewed approvals with the new `--approve-for-me`
      CLI flag. (#36373)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: 'Import Cursor-managed skills and synchronize changes to imported Claude
      and Cursor conversations without creating duplicates. (#36361, #36356, #35623)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: 'Properly interrupt Windows background processes and handle Windows filesystem
      paths consistently. (#35655, #35851, #37129)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: Stop publishing redundant Linux bundle archives; use the standard `codex-package-<target>`
      release archives. (#36342)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35595 Allow alpha hotfix versions in R2 releases @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35597 Add metrics for extension-rendered skill catalogs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35607 Record metrics for empty skill catalogs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35621 Skip restored token usage replay for exec resumes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35623 Parse Claude and Cursor session records separately @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35642 Make OpenTelemetry provider shutdown idempotent @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35644 Preserve thread metadata when rollout files are missing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35652 Enable network policy callbacks for remote exec @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35655 Terminate Windows non-TTY processes on interrupt @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35663 Evaluate character matching over skill routing metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35668 Expose the network proxy spec constructor @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35670 Raise the Windows exec yield floor to 10 seconds @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35678 Preserve paginated thread metadata across resumes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35688 Point crossterm patch to the OpenAI OSS fork @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35689 Preserve item timestamps in thread history projections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35691 Include empty-preview threads in relationship listings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35695 Honor the configured SQLite home in the logs client @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35715 Support streaming bodies in route-aware HTTP requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35717 Reuse route-aware clients for OpenAI file uploads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35720 Upgrade rmcp to 3.0.0-beta.3 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35721 Honor disabled code mode fallback without a process host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35722 Add persisted sections for organizing threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35738 Add bounded metadata for executed tool calls @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35766 Emit host skill budget warnings from world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35779 Load thread titles concurrently during session startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35785 Support self-serve Business ProLite accounts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35787 Gate paginated thread history on the state database @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35818 Advance latest-alpha-cli after release publishing completes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35828 Enforce centralized SQLite connection creation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35830 Route WebRTC sideband joins to the Realtime API @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35831 Update rusty_v8 to 150.4.0 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35835 Track parent turns for nested Codex requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35843 Tie remote exec servers to their parent stdin @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35851 Normalize Windows namespace paths in path URIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35854 Box app-server event payloads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35857 Add Bazel unit test targets for Rust binaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35875 Allow environment readiness updates in place @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35886 Show blocked goals as stalled in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35887 Clean up side conversations in the background @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35942 Update tests for current tool call and app-server event types @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35959 Upgrade Ratatui to 0.30.2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35962 Fix TUI layout for halfwidth Japanese sound marks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35982 Avoid cloning rollout history when truncating forks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35990 Test exec-server compatibility across Codex versions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#35997 Remove obsolete rusty_v8 146.4.0 Bazel targets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36001 Upgrade rmcp to 3.0.0 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36006 Reduce response serialization and rollout scan overhead @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36007 Add persisted manual ordering for thread sections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36014 Refine OpenAI docs skill source routing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36020 Avoid cloning ignored analytics notifications @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36030 Increase the app-server tracing test stack size @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36035 Exit the stdio app-server when its connection closes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36036 Allow naming forked chats from the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36037 Deny network access when an allow amendment fails @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36049 Keep tool-call metrics out of Statsig exports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36051 Avoid overwriting symlinked migration targets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36054 Remove legacy `--full-auto` handling from `codex exec` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36076 Remove codex-core''s direct reqwest dependency @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36083 Handle fractional rate limits in thread history projection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36092 Correlate image requests and explicit interrupts with turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36119 Unify tool runtime assembly before router construction @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36120 Delegate readiness waits to tool runtimes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36124 Respect filesystem permissions during capability discovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36127 Centralize tool registration and protect host tools @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36129 Resolve normalized tool name collisions in code mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36133 Preserve executor workspace permissions for apply_patch @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36139 Bound the code mode output termination test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36146 Stabilize approval scenario tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36149 Strengthen session file change approval coverage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36165 Stabilize file approval replay test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36166 Make pending realtime sideband test deterministic @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36168 Make tool telemetry tag collection synchronous @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36171 Test workspace-root patch protection for metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36177 Test remote Guardian network approval scoping @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36181 Record attempted tool calls in response metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36184 Coalesce concurrent remote metadata requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36187 Refresh environment dates from the configured clock @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36188 Make thread history projection resilient to malformed rollouts
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36191 Label explicit skill injection metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36194 Avoid shifting bytes in streaming output buffers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36212 Precompute app-server protocol exports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36217 Run code mode exclusively through the standalone host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36221 Ignore passthrough metadata when reconciling rollout items @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36239 Refresh precomputed app-server protocol exports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36264 Prefer the bundled resource for the code mode host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36271 Derive report prompt hashes from persisted rollouts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36309 Use the host skill provider catalog in world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36327 Preserve discovery order for host skill path aliases @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36342 Stop publishing legacy Linux bundle archives @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36354 Pass sessions directly to session tasks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36357 Use the step-scoped router for tool execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36361 Migrate Cursor-managed skills into Codex @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36367 Keep effective tool exposure in the registry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36372 Run native Windows Bazel tests with MSVC @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36373 Add an `--approve-for-me` CLI flag @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36374 Enable sandboxed V8 for code mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36378 Load local session pickers from the state DB first @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36380 Add thread section management APIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36384 Load turn summaries with paginated queries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36385 Add acknowledged user message submission to core @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36388 Track image preparation details in turn analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36389 Enforce single-writer ownership for all thread histories @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36393 Avoid redundant filesystem probes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36408 Allow custom Codex instructions for realtime transitions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36410 Make user input blocking behavior explicit @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36413 Add a realtime delegation acknowledgement control @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36440 Extract exec-server request dispatching @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36507 Retain attempted tool metadata across prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36511 Support two-stroke TUI key chords @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36632 Preserve SQLite thread metadata during goal mutations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36641 Capture rollout budget units from response usage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36715 Use provider-reported rollout budget units @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36727 Simplify turn metadata state ownership @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36740 Store turn skill state in extension data @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36742 Simplify contextual user fragment registration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36744 Store the extension registry directly in its builder @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36745 Consolidate apply_patch runtime execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36759 Harden the TUI focus palette regression test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36764 Avoid building code-mode definitions during registration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36770 Stabilize deferred goal fork testing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36771 Harden Linux managed proxy helper lifecycles @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36773 Derive the active user config layer from the layer stack @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36774 Clarify config layer iteration APIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36779 Stabilize network policy event capture in concurrent tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36782 Add Guardian session reuse and interruption tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36797 Normalize rusty_v8 checksum manifest line endings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36808 Prefer SQLite names for local session archive commands @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36809 Prefer the state database for `exec resume --last` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36812 Add a dual-WebSocket transport for code mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36822 Fix typo in approval resolver name @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36830 Time out stalled code-mode host requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36834 Avoid requesting key-release events in Ghostty @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36840 Keep API request metrics out of Statsig exports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36856 Support deferred loading for freeform tools @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36857 Support custom tools in namespaces @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36862 Consolidate thread spawning behind a request object @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36871 Parallelize R2 asset publishing with DotSlash @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36877 Move executor skill bundle loading into the skills extension @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36880 Move direct executor skill discovery into the skills extension
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36884 Add host skill root loading @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36898 Avoid redundant filesystem metadata probes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36901 Propagate updated permissions to review threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36903 Load skill interface metadata in the host loader @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36904 Limit RMCP logs persisted to SQLite @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36908 Improve bearer token secret redaction @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36912 Read approval policy from the current turn configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36913 Move skill policy resolution into `codex-skills` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36916 Centralize app enabled-state evaluation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36921 Move the host skills service into the skills extension @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36930 Read turn permissions from the current configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36935 Trust undecided local projects automatically @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36939 Include policy approval reasons in Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36941 Use current session settings for review threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36943 Move host skill root resolution into the skills extension @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36945 Grant the blob size policy job read access to contents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36947 Accept user input when starting idle turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36948 Paginate transcript history in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36949 Improve paginated TUI history loading @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36950 Paginate TUI transcript history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36951 Harden paginated history handling in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36952 Add durable per-thread user submission queues @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36954 Add tool registry collision policy configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36960 Prompt before trusting local project directories @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36964 Preserve working directories when importing external sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36966 Allow disabling the built-in image viewer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36976 Honor explicit-only orchestrator skills @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36979 Add Fence auditing to the blob size workflow @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36984 Support configured ChatGPT cookies in HTTP clients @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36986 Add process-scoped PSP routing for ChatGPT requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36987 Add opt-in concurrent exec-server request dispatch @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36993 Support `includeTurns` reads for paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#36998 Support deferred custom tools in tool search @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37020 Enforce strict tool name collision errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37022 Canonicalize default tools under the `functions` namespace @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37035 Align registry tests with canonical tool names @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37038 Use turn environment permissions for tool execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37053 Reject conflicting namespace descriptions in strict tool mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37083 Consolidate unified exec output state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37103 Use Luna for API-key Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37109 Bound interactive telemetry shutdown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37114 Add per-session code-mode execution limits @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37128 Centralize tool approval handling in `Session` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37129 Make Windows path URI comparisons ASCII-case-insensitive @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37144 Preserve discovery paths for symlinked skills @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37147 Track provisioned environment state across registration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37149 Project orchestrator skills through world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37157 Harden named session lookup in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37162 Load host skill roots through the skills extension @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37174 Centralize skill invocation helpers in `codex-skills` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37175 Add legacy rollout migration to paginated history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37178 Preserve image transparency metadata in app-server items @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  - quote: '#37188 Reserve the `tool_search` namespace for the search tool @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.147.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 196-other-changes-in-rust-v0-147-0
  source_release: codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2
  source_type: github_releases
  theme: uncategorized
  title: 196 other changes in rust-v0.147.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2]]'
source_type: github_releases
theme: uncategorized
title: 196 other changes in rust-v0.147.0
type: change
---

<!-- chronolog:begin region="header" -->
# 196 other changes in rust-v0.147.0

**Codex CLI** · 2026-08-07 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.147.0) · from [[Releases/Codex CLI/codex-cli-2026-08-07-rust-v0-147-0-github-366471016-f6cfdee2|0.147.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Enable automatically reviewed approvals with the new `--approve-for-me` CLI flag. (#36373)

> Import Cursor-managed skills and synchronize changes to imported Claude and Cursor conversations without creating duplicates. (#36361, #36356, #35623)

> Properly interrupt Windows background processes and handle Windows filesystem paths consistently. (#35655, #35851, #37129)

> Stop publishing redundant Linux bundle archives; use the standard `codex-package-<target>` release archives. (#36342)

> #35595 Allow alpha hotfix versions in R2 releases @copyberry

> #35597 Add metrics for extension-rendered skill catalogs @copyberry

> #35607 Record metrics for empty skill catalogs @copyberry

> #35621 Skip restored token usage replay for exec resumes @copyberry

> #35623 Parse Claude and Cursor session records separately @copyberry

> #35642 Make OpenTelemetry provider shutdown idempotent @copyberry

> #35644 Preserve thread metadata when rollout files are missing @copyberry

> #35652 Enable network policy callbacks for remote exec @copyberry

> #35655 Terminate Windows non-TTY processes on interrupt @copyberry

> #35663 Evaluate character matching over skill routing metadata @copyberry

> #35668 Expose the network proxy spec constructor @copyberry

> #35670 Raise the Windows exec yield floor to 10 seconds @copyberry

> #35678 Preserve paginated thread metadata across resumes @copyberry

> #35688 Point crossterm patch to the OpenAI OSS fork @copyberry

> #35689 Preserve item timestamps in thread history projections @copyberry

> #35691 Include empty-preview threads in relationship listings @copyberry

> #35695 Honor the configured SQLite home in the logs client @copyberry

> #35715 Support streaming bodies in route-aware HTTP requests @copyberry

> #35717 Reuse route-aware clients for OpenAI file uploads @copyberry

> #35720 Upgrade rmcp to 3.0.0-beta.3 @copyberry

> #35721 Honor disabled code mode fallback without a process host @copyberry

> #35722 Add persisted sections for organizing threads @copyberry

> #35738 Add bounded metadata for executed tool calls @copyberry

> #35766 Emit host skill budget warnings from world state @copyberry

> #35779 Load thread titles concurrently during session startup @copyberry

> #35785 Support self-serve Business ProLite accounts @copyberry

> #35787 Gate paginated thread history on the state database @copyberry

> #35818 Advance latest-alpha-cli after release publishing completes @copyberry

> #35828 Enforce centralized SQLite connection creation @copyberry

> #35830 Route WebRTC sideband joins to the Realtime API @copyberry

> #35831 Update rusty_v8 to 150.4.0 @copyberry

> #35835 Track parent turns for nested Codex requests @copyberry

> #35843 Tie remote exec servers to their parent stdin @copyberry

> #35851 Normalize Windows namespace paths in path URIs @copyberry

> #35854 Box app-server event payloads @copyberry

> #35857 Add Bazel unit test targets for Rust binaries @copyberry

> #35875 Allow environment readiness updates in place @copyberry

> #35886 Show blocked goals as stalled in the TUI @copyberry

> #35887 Clean up side conversations in the background @copyberry

> #35942 Update tests for current tool call and app-server event types @copyberry

> #35959 Upgrade Ratatui to 0.30.2 @copyberry

> #35962 Fix TUI layout for halfwidth Japanese sound marks @copyberry

> #35982 Avoid cloning rollout history when truncating forks @copyberry

> #35990 Test exec-server compatibility across Codex versions @copyberry

> #35997 Remove obsolete rusty_v8 146.4.0 Bazel targets @copyberry

> #36001 Upgrade rmcp to 3.0.0 @copyberry

> #36006 Reduce response serialization and rollout scan overhead @copyberry

> #36007 Add persisted manual ordering for thread sections @copyberry

> #36014 Refine OpenAI docs skill source routing @copyberry

> #36020 Avoid cloning ignored analytics notifications @copyberry

> #36030 Increase the app-server tracing test stack size @copyberry

> #36035 Exit the stdio app-server when its connection closes @copyberry

> #36036 Allow naming forked chats from the TUI @copyberry

> #36037 Deny network access when an allow amendment fails @copyberry

> #36049 Keep tool-call metrics out of Statsig exports @copyberry

> #36051 Avoid overwriting symlinked migration targets @copyberry

> #36054 Remove legacy `--full-auto` handling from `codex exec` @copyberry

> #36076 Remove codex-core's direct reqwest dependency @copyberry

> #36083 Handle fractional rate limits in thread history projection @copyberry

> #36092 Correlate image requests and explicit interrupts with turns @copyberry

> #36119 Unify tool runtime assembly before router construction @copyberry

> #36120 Delegate readiness waits to tool runtimes @copyberry

> #36124 Respect filesystem permissions during capability discovery @copyberry

> #36127 Centralize tool registration and protect host tools @copyberry

> #36129 Resolve normalized tool name collisions in code mode @copyberry

> #36133 Preserve executor workspace permissions for apply_patch @copyberry

> #36139 Bound the code mode output termination test @copyberry

> #36146 Stabilize approval scenario tests @copyberry

> #36149 Strengthen session file change approval coverage @copyberry

> #36165 Stabilize file approval replay test @copyberry

> #36166 Make pending realtime sideband test deterministic @copyberry

> #36168 Make tool telemetry tag collection synchronous @copyberry

> #36171 Test workspace-root patch protection for metadata @copyberry

> #36177 Test remote Guardian network approval scoping @copyberry

> #36181 Record attempted tool calls in response metadata @copyberry

> #36184 Coalesce concurrent remote metadata requests @copyberry

> #36187 Refresh environment dates from the configured clock @copyberry

> #36188 Make thread history projection resilient to malformed rollouts @copyberry

> #36191 Label explicit skill injection metrics @copyberry

> #36194 Avoid shifting bytes in streaming output buffers @copyberry

> #36212 Precompute app-server protocol exports @copyberry

> #36217 Run code mode exclusively through the standalone host @copyberry

> #36221 Ignore passthrough metadata when reconciling rollout items @copyberry

> #36239 Refresh precomputed app-server protocol exports @copyberry

> #36264 Prefer the bundled resource for the code mode host @copyberry

> #36271 Derive report prompt hashes from persisted rollouts @copyberry

> #36309 Use the host skill provider catalog in world state @copyberry

> #36327 Preserve discovery order for host skill path aliases @copyberry

> #36342 Stop publishing legacy Linux bundle archives @copyberry

> #36354 Pass sessions directly to session tasks @copyberry

> #36357 Use the step-scoped router for tool execution @copyberry

> #36361 Migrate Cursor-managed skills into Codex @copyberry

> #36367 Keep effective tool exposure in the registry @copyberry

> #36372 Run native Windows Bazel tests with MSVC @copyberry

> #36373 Add an `--approve-for-me` CLI flag @copyberry

> #36374 Enable sandboxed V8 for code mode @copyberry

> #36378 Load local session pickers from the state DB first @copyberry

> #36380 Add thread section management APIs @copyberry

> #36384 Load turn summaries with paginated queries @copyberry

> #36385 Add acknowledged user message submission to core @copyberry

> #36388 Track image preparation details in turn analytics @copyberry

> #36389 Enforce single-writer ownership for all thread histories @copyberry

> #36393 Avoid redundant filesystem probes @copyberry

> #36408 Allow custom Codex instructions for realtime transitions @copyberry

> #36410 Make user input blocking behavior explicit @copyberry

> #36413 Add a realtime delegation acknowledgement control @copyberry

> #36440 Extract exec-server request dispatching @copyberry

> #36507 Retain attempted tool metadata across prompts @copyberry

> #36511 Support two-stroke TUI key chords @copyberry

> #36632 Preserve SQLite thread metadata during goal mutations @copyberry

> #36641 Capture rollout budget units from response usage @copyberry

> #36715 Use provider-reported rollout budget units @copyberry

> #36727 Simplify turn metadata state ownership @copyberry

> #36740 Store turn skill state in extension data @copyberry

> #36742 Simplify contextual user fragment registration @copyberry

> #36744 Store the extension registry directly in its builder @copyberry

> #36745 Consolidate apply_patch runtime execution @copyberry

> #36759 Harden the TUI focus palette regression test @copyberry

> #36764 Avoid building code-mode definitions during registration @copyberry

> #36770 Stabilize deferred goal fork testing @copyberry

> #36771 Harden Linux managed proxy helper lifecycles @copyberry

> #36773 Derive the active user config layer from the layer stack @copyberry

> #36774 Clarify config layer iteration APIs @copyberry

> #36779 Stabilize network policy event capture in concurrent tests @copyberry

> #36782 Add Guardian session reuse and interruption tests @copyberry

> #36797 Normalize rusty_v8 checksum manifest line endings @copyberry

> #36808 Prefer SQLite names for local session archive commands @copyberry

> #36809 Prefer the state database for `exec resume --last` @copyberry

> #36812 Add a dual-WebSocket transport for code mode @copyberry

> #36822 Fix typo in approval resolver name @copyberry

> #36830 Time out stalled code-mode host requests @copyberry

> #36834 Avoid requesting key-release events in Ghostty @copyberry

> #36840 Keep API request metrics out of Statsig exports @copyberry

> #36856 Support deferred loading for freeform tools @copyberry

> #36857 Support custom tools in namespaces @copyberry

> #36862 Consolidate thread spawning behind a request object @copyberry

> #36871 Parallelize R2 asset publishing with DotSlash @copyberry

> #36877 Move executor skill bundle loading into the skills extension @copyberry

> #36880 Move direct executor skill discovery into the skills extension @copyberry

> #36884 Add host skill root loading @copyberry

> #36898 Avoid redundant filesystem metadata probes @copyberry

> #36901 Propagate updated permissions to review threads @copyberry

> #36903 Load skill interface metadata in the host loader @copyberry

> #36904 Limit RMCP logs persisted to SQLite @copyberry

> #36908 Improve bearer token secret redaction @copyberry

> #36912 Read approval policy from the current turn configuration @copyberry

> #36913 Move skill policy resolution into `codex-skills` @copyberry

> #36916 Centralize app enabled-state evaluation @copyberry

> #36921 Move the host skills service into the skills extension @copyberry

> #36930 Read turn permissions from the current configuration @copyberry

> #36935 Trust undecided local projects automatically @copyberry

> #36939 Include policy approval reasons in Guardian reviews @copyberry

> #36941 Use current session settings for review threads @copyberry

> #36943 Move host skill root resolution into the skills extension @copyberry

> #36945 Grant the blob size policy job read access to contents @copyberry

> #36947 Accept user input when starting idle turns @copyberry

> #36948 Paginate transcript history in the TUI @copyberry

> #36949 Improve paginated TUI history loading @copyberry

> #36950 Paginate TUI transcript history @copyberry

> #36951 Harden paginated history handling in the TUI @copyberry

> #36952 Add durable per-thread user submission queues @copyberry

> #36954 Add tool registry collision policy configuration @copyberry

> #36960 Prompt before trusting local project directories @copyberry

> #36964 Preserve working directories when importing external sessions @copyberry

> #36966 Allow disabling the built-in image viewer @copyberry

> #36976 Honor explicit-only orchestrator skills @copyberry

> #36979 Add Fence auditing to the blob size workflow @copyberry

> #36984 Support configured ChatGPT cookies in HTTP clients @copyberry

> #36986 Add process-scoped PSP routing for ChatGPT requests @copyberry

> #36987 Add opt-in concurrent exec-server request dispatch @copyberry

> #36993 Support `includeTurns` reads for paginated threads @copyberry

> #36998 Support deferred custom tools in tool search @copyberry

> #37020 Enforce strict tool name collision errors @copyberry

> #37022 Canonicalize default tools under the `functions` namespace @copyberry

> #37035 Align registry tests with canonical tool names @copyberry

> #37038 Use turn environment permissions for tool execution @copyberry

> #37053 Reject conflicting namespace descriptions in strict tool mode @copyberry

> #37083 Consolidate unified exec output state @copyberry

> #37103 Use Luna for API-key Guardian reviews @copyberry

> #37109 Bound interactive telemetry shutdown @copyberry

> #37114 Add per-session code-mode execution limits @copyberry

> #37128 Centralize tool approval handling in `Session` @copyberry

> #37129 Make Windows path URI comparisons ASCII-case-insensitive @copyberry

> #37144 Preserve discovery paths for symlinked skills @copyberry

> #37147 Track provisioned environment state across registration @copyberry

> #37149 Project orchestrator skills through world state @copyberry

> #37157 Harden named session lookup in the TUI @copyberry

> #37162 Load host skill roots through the skills extension @copyberry

> #37174 Centralize skill invocation helpers in `codex-skills` @copyberry

> #37175 Add legacy rollout migration to paginated history @copyberry

> #37178 Preserve image transparency metadata in app-server items @copyberry

> #37188 Reserve the `tool_search` namespace for the search tool @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.147.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-07-10-collaboration-changes-in-rust-v0-147-0|10 Collaboration changes in rust-v0.147.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-07-8-account-and-access-changes-in-rust-v0-147-0|8 Account and Access changes in rust-v0.147.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-07-36140-wait-for-memory-consolidation-shutdown-before-finishing-jobs-copyberry|♯36140 Wait for memory consolidation shutdown before finishing jobs @copyberry]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-07-65-apps-and-integrations-changes-in-rust-v0-147-0|65 Apps and Integrations changes in rust-v0.147.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-07-15-developer-workflow-changes-in-rust-v0-147-0|15 Developer Workflow changes in rust-v0.147.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-07-36043-document-the-responses-api-proxy-reqwest-exception-copyberry|♯36043 Document the Responses API proxy reqwest exception @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-07-36228-support-enterprise-automation-account-plans-copyberry|♯36228 Support Enterprise automation account plans @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-08-07-3-search-and-browsing-changes-in-rust-v0-147-0|3 Search and Browsing changes in rust-v0.147.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-08-07-17-agent-mode-changes-in-rust-v0-147-0|17 Agent Mode changes in rust-v0.147.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-07-13-model-support-changes-in-rust-v0-147-0|13 Model Support changes in rust-v0.147.0]] · Model Support
- [[Changes/Codex CLI/2026-08-07-36807-extract-audio-preparation-into-a-utility-crate-copyberry|♯36807 Extract audio preparation into a utility crate @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-07-4-mobile-and-desktop-changes-in-rust-v0-147-0|4 Mobile and Desktop changes in rust-v0.147.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-07-9-safety-and-privacy-changes-in-rust-v0-147-0|9 Safety and Privacy changes in rust-v0.147.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-07-10-context-window-changes-in-rust-v0-147-0|10 Context Window changes in rust-v0.147.0]] · Context Window
- [[Changes/Codex CLI/2026-08-07-6-interface-experience-changes-in-rust-v0-147-0|6 Interface Experience changes in rust-v0.147.0]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-07-a60750&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-07-196-other-changes-in-rust-v0-147-0.md%0ACard%20ID%3A%20codex-cli-2026-08-07-a60750%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.147.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->