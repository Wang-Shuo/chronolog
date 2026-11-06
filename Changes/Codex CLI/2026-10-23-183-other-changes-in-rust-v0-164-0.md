---
card_id: codex-cli-2026-10-23-2f4dd5
date: '2026-10-23'
description: 'Codex CLI · 2026-10-23 · Other changes: 183 changes in 0.164.0 — Resuming
  sessions now finds compressed histories and restores saved thread settings instead
  of…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a9efb6449d872dd26d6e42e9caea582a3b587ac810e0671fd9abb3b0d3735127
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-23-2f4dd5
  comparison: ''
  date: '2026-10-23'
  description: 'Codex CLI — 0.164.0: 183 other changes'
  evidence:
  - quote: 'Resuming sessions now finds compressed histories and restores saved thread
      settings instead of replacing them with global defaults. (#54008, #55923)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: CLI configuration overrides are preserved when `-c` or `--config` appears
      at multiple subcommand levels. (#56022)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: 'Reduced disk usage by pruning unused installations, cleaning abandoned
      marketplace checkouts, and bounding daemon logs. (#53827, #55149, #55689, #55690,
      #55856)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53725 Render Markdown web links as labels in Rex @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53732 Reuse compiled search patterns across compressed rollouts @ethernetdan-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53733 Default Guardian v2 async classification to conversation mode @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53736 Acquire and cache opt-in executor capability inventories via V2
      @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53751 Apply feature overrides when restarting the app-server daemon @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53753 Extend copy-on-select to composer text @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53780 Remove redundant Codex manual cache directory check @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53781 Remove the product-gating TODO from `SkillPolicy` @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53794 Retain rollout migration locks across worker cancellation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53805 Add safe diagnostics to workspace routing configuration errors
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53811 Support daemon installation from Windows WinGet packages @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53816 Reject Guardian review threads during interactive CLI resume @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53827 Prune unused app-server daemon releases safely @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53845 Fix daemon updater socket binding and bootstrap readiness on Unix
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53853 Reuse staged file digests when preparing daemon installs @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53879 Preserve running turn recovery across thread settings updates @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53897 Isolate daemon package tests to reduce disk contention @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53947 Stop rollout reads when the calling task is cancelled @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53969 Avoid reconnect races in the daemon restart test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53987 Skip service backoff for stale Guardian authorization retries @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53991 Report the reason for ChatGPT token refresh requests @tejsudha-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53996 Bump `rustls` to `0.23.46` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#53997 Filter rollout filenames before checking compressed siblings @bbrown-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54003 Include compressed rollouts in doctor storage statistics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54008 Fix session lookup and resume after rollout compression @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54027 Preserve Windows startup variables and MXC child environment defaults
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54039 Return async Guardian approvals before review cleanup finishes
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54044 Keep fork lineage ahead of paginated transcript history @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54047 Restore elapsed time for replayed in-progress turns @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54050 Scope TUI skill refreshes and workspace commands to explicit directories
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54053 Add Responses API client metadata patches for turn start and steer
      @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54056 Coalesce overlapping native TLS root certificate loads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54057 Distinguish unsupported evidence in Decisions comparison metrics
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54059 Support store-owned preparation when resuming threads @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54060 Limit unarchive scans to the requested thread''s archived rollouts
      @bz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54076 Avoid false URL-launch detections in literal PowerShell commands
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54078 Update `gix` to 0.89.0 and `gix-url` to 0.40.0 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54080 Extract TUI user-turn submission into a dedicated module @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54082 Stabilize the Guardian network review timeout test @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54087 Upgrade Bazel''s `rules_python` to 2.4.2 @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54097 Show Daybreak notices after the session header @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54098 Keep environment tools stable across readiness changes @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54099 Wait for readiness in the SIGTERM cancellation test @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54113 Embed generated app-server schema bundles in Bazel builds @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54133 Record per-tool incremental update and description size metrics
      @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54135 Allow large file writes over direct exec-server WebSockets @ostepanian'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54151 Generate keymap descriptors and binding accessors from one catalog
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54217 Apply syntax theme colors to Markdown prose in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54250 Add regression tests for case-variant metadata protection @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54257 Preserve recent speech when trimming realtime transcripts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54263 Require fresh Guardian approval for escalated tool retries @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54264 Track Guardian transcript admission across failed reviews @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54309 Enable credential masking for remote exec-server commands @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54315 Keep TUI Markdown colors readable against their backgrounds @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54346 Add scoped executor credential auth for remote exec-server @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54351 Use the turn index for turn-scoped item pagination @bz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54363 Filter uninspectable network roots from implicit MXC read grants
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54365 Prevent duplicate assistant messages around interleaved commands
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54369 Retry SQLite operations on transient writer contention @willwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54379 Add configuration support for TUI input presets @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54380 Add `/presets` for reusable prompts and slash commands @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54387 Add session-only arguments to `/title` and `/statusline` @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54389 Preserve existing SQLite journal modes on startup @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54398 Store generated image items as attachment references @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54414 Allow root turn suspension with live descendants @miz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54417 Skip SQLite page reclamation on Linux NFS mounts @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54419 Support line breaks in Mermaid flowchart node labels @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54421 Treat explicit connections to the verified default daemon as local
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54433 Use neutral labels for nonzero exits in compact TUI output @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54434 Add rotating stdin credentials for remote exec-server @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54475 Use a synchronous mutex for remote metadata request tracking @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54505 Add streaming file replacement to filesystem abstractions @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54589 Preserve evidence message structure in Guardian Decisions requests
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54623 Resolve stable releases dynamically for exec-server compatibility
      tests @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54637 Preserve disconnect reasons in Noise handshake errors @virajrai-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54639 Stream rollout records during thread history materialization @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54654 Allow dynamic tool calls to execute in parallel @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54664 Distinguish retryable thread-store errors from unknown write outcomes
      @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54674 Add an opt-in tool for copying files between environments @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54681 Keep TUI session selections bound to their backend @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54708 Honor home deletion preferences during Windows uninstall @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54710 Move V8''s ICU Bazel rules into the workspace @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54716 Keep prereleases in draft until release assets finish uploading
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54724 Preserve prereleased events when creating GitHub prereleases @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54739 Close arg0 lock files before removing temporary directories @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54741 Gate the file-copy extension behind `multi_env_copy_file` @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54776 Support typed content in contextual prompt fragments @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54930 Add negotiated zstd compression to app-server WebSockets @thorvald-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54949 Gate app-server WebSocket compression behind a feature flag @thorvald-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55149 Prune unused standalone releases after successful installation
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55226 Bucket admitted Guardian request metrics by input size @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55227 Allow plus signs in metric tags @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55234 Record Guardian sampling retries, attempts, and delivery outcomes
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55237 Add Guardian review routing and cached score metrics @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55244 Batch thread history materialization into SQLite @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55252 Preserve rollout access metadata across compression and restoration
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55255 Unload idle ephemeral composer prediction threads without delay
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55270 Honor per-thread unload delays in app-server @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55274 Stabilize daemon reconnect and Rosetta package startup tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55283 Avoid cloning events in the app-server thread listener @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55288 Recheck EMA request authority at HTTP boundaries @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55297 Add GitHub Actions OIDC token acquisition to the responses API
      proxy @ee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55298 Add renewable federated auth primitives to the Responses API proxy
      @ee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55299 Refresh rejected proxy credentials and back off failed renewals
      @ee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55300 Add one-shot app-server startup configuration discovery @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55302 Stop the closest remote SHA search at zero distance @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55303 Route skill reads by alias source @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55304 Reject TUI events from a different backend @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55322 Integrate discovery V2 with step-scoped skill catalogs @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55324 Remove thread title generation spinners from the TUI @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55330 Expose skill installations and stabilize package aliases @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55339 Add experimental `thread/sample` requests to the app server @liame-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55342 Consolidate cached and fetched Codex manual handling @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55347 Add Guardian retry metrics and preserve turn attribution @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55351 Reduce path storage in the file-search index @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55357 Prepare skill catalogs before building step tools @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55365 Import only the continuation of backgrounded Claude sessions @jgrodman-arch'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55368 Enable incremental tools by default for Responses Lite @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55379 Handle response body failures in OpenAI docs downloads @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55380 Preserve thread metadata before rollout files are materialized
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55381 Manage TUI backend sessions independently @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55387 Add support for Academic Researchers plans @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55388 Mark `transcript_v2` as removed @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55395 Roll back interrupted Guardian reviews to preserve evidence @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55396 Prefetch sibling rollout paths when reading history pages @bz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55401 Defer environment disconnect notifications until recovery fails
      @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55402 Add ephemeral runtime registration and signed assertions @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55406 Trace harness-side Noise handshake failures @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55409 Retry TUI startup after a server shutdown refusal @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55410 Track credential sources separately from auth owners @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55411 Render async question prompts as Markdown in the TUI @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55441 Add cancellation for experimental thread samples @liame-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55442 Check daemon feature overrides and prompt for mismatch recovery
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55456 Support Windows registry overrides for `requirements.toml` @johnl-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55498 Add correlated diagnostics for Noise relay handshakes @virajrai-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55524 Make the startup migration contention test deterministic @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55533 Separate Guardian conversation preparation from execution @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55545 Improve diagnostics for compressed rollout read failures @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55547 Ignore the basic-toml advisory in dependency audits @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55591 Measure Guardian approval blocking time per turn @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55616 Update `rustls-webpki` and `webpki-roots` lockfile versions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55623 Refactor Guardian v2 Decisions snapshot comparison @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55627 Reserve a sibling rollout candidate slot for the first ancestor
      @bz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55631 Add frozen cloud skill snapshots to the app server @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55635 Enable Decisions comparisons for Guardian V2 conversation mode
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55645 Fix in-process app-server shutdown with full queues @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55652 Search compressed rollouts concurrently @ethernetdan-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55653 Track code-mode cell lifecycle and result buffering time @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55677 Upgrade the Rust toolchain to 1.99.1 @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55685 Add account credential support to EMA token exchange helpers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55689 Clean up failed and abandoned marketplace staging directories @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55690 Reclaim aged legacy marketplace staging directories @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55692 Tag tool registration metrics with effective incremental tools
      mode @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55705 Centralize cloud skill cache state under the catalog lock @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55719 Allow unified exec to fall back when credential masking is unavailable
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55723 Avoid redundant clones when sending app-server notifications @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55725 Preserve code cell response metadata in rollout traces @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55804 Add a critical-path utility for exclusive duration attribution
      @taohong339'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55847 Bound retained turn analytics and clean up closed threads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55848 Pause relay test time while inspecting handshake diagnostics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55856 Bound managed app-server and updater stderr logging @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55913 Skip conversation scoring superseded by newer scores and history
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55940 Add local diagnostic ZIP exports to the app server @viktor-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55954 Separate retained instruction collection from budget policy @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55969 Drain WebSocket responses on mailbox preemption @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55971 Add storage namespaces for local message boards @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55973 Allow consumers to select message-board tools @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55978 Route SQLite logs to an explicitly configured `log_dir` @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55987 Refresh remote exec-server credentials after unauthorized responses
      @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56003 Scope MITM credential substitution to trusted origins and placeholders
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56007 Pause Tokio time in the reused Guardian session test @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56008 Add a critical-path timing recorder for direct tool calls @taohong339'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56020 Allow thread sampling after failed or interrupted turns @liame-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56022 Preserve config overrides across CLI subcommand boundaries @jmickey-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56024 Limit decoded HTTP/3 response headers in the TCP tunnel @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56031 Support client Responses API metadata in `thread/sample` @liame-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56033 Enable the Bedrock setup wizard by default @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56037 Add a channel-backed cloud app-server client @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56049 Support configured credential providers in remote execution @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#56055 Require managed configuration from the configured server @smurching-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 183-other-changes-in-rust-v0-164-0
  source_release: codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d
  source_type: github_releases
  theme: uncategorized
  title: 183 other changes in rust-v0.164.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d]]'
source_type: github_releases
theme: uncategorized
title: 183 other changes in rust-v0.164.0
type: change
---

<!-- chronolog:begin region="header" -->
# 183 other changes in rust-v0.164.0

**Codex CLI** · 2026-10-23 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.164.0) · from [[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|0.164.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Resuming sessions now finds compressed histories and restores saved thread settings instead of replacing them with global defaults. (#54008, #55923)

> CLI configuration overrides are preserved when `-c` or `--config` appears at multiple subcommand levels. (#56022)

> Reduced disk usage by pruning unused installations, cleaning abandoned marketplace checkouts, and bounding daemon logs. (#53827, #55149, #55689, #55690, #55856)

> #53725 Render Markdown web links as labels in Rex @bc-openai

> #53732 Reuse compiled search patterns across compressed rollouts @ethernetdan-openai

> #53733 Default Guardian v2 async classification to conversation mode @felixxia-oai

> #53736 Acquire and cache opt-in executor capability inventories via V2 @TAFOYA-OAI

> #53751 Apply feature overrides when restarting the app-server daemon @jif-oai

> #53753 Extend copy-on-select to composer text @fcoury-oai

> #53780 Remove redundant Codex manual cache directory check @kkahadze-oai

> #53781 Remove the product-gating TODO from `SkillPolicy` @kkahadze-oai

> #53794 Retain rollout migration locks across worker cancellation @jif-oai

> #53805 Add safe diagnostics to workspace routing configuration errors @etraut-openai

> #53811 Support daemon installation from Windows WinGet packages @etraut-openai

> #53816 Reject Guardian review threads during interactive CLI resume @dylan-hurd-oai

> #53827 Prune unused app-server daemon releases safely @etraut-openai

> #53845 Fix daemon updater socket binding and bootstrap readiness on Unix @etraut-openai

> #53853 Reuse staged file digests when preparing daemon installs @charliemarsh-oai

> #53879 Preserve running turn recovery across thread settings updates @bc-openai

> #53897 Isolate daemon package tests to reduce disk contention @etraut-openai

> #53947 Stop rollout reads when the calling task is cancelled @jif-oai

> #53969 Avoid reconnect races in the daemon restart test @jif-oai

> #53987 Skip service backoff for stale Guardian authorization retries @jif-oai

> #53991 Report the reason for ChatGPT token refresh requests @tejsudha-openai

> #53996 Bump `rustls` to `0.23.46` @jif-oai

> #53997 Filter rollout filenames before checking compressed siblings @bbrown-oai

> #54003 Include compressed rollouts in doctor storage statistics @jif-oai

> #54008 Fix session lookup and resume after rollout compression @jif-oai

> #54027 Preserve Windows startup variables and MXC child environment defaults @iceweasel-oai

> #54039 Return async Guardian approvals before review cleanup finishes @jif-oai

> #54044 Keep fork lineage ahead of paginated transcript history @fcoury-oai

> #54047 Restore elapsed time for replayed in-progress turns @etraut-openai

> #54050 Scope TUI skill refreshes and workspace commands to explicit directories @etraut-openai

> #54053 Add Responses API client metadata patches for turn start and steer @marksteinbrick-oai

> #54056 Coalesce overlapping native TLS root certificate loads @jif-oai

> #54057 Distinguish unsupported evidence in Decisions comparison metrics @swastik-oai

> #54059 Support store-owned preparation when resuming threads @owenlin0

> #54060 Limit unarchive scans to the requested thread's archived rollouts @bz-openai

> #54076 Avoid false URL-launch detections in literal PowerShell commands @jif-oai

> #54078 Update `gix` to 0.89.0 and `gix-url` to 0.40.0 @jif-oai

> #54080 Extract TUI user-turn submission into a dedicated module @bc-openai

> #54082 Stabilize the Guardian network review timeout test @felixxia-oai

> #54087 Upgrade Bazel's `rules_python` to 2.4.2 @dkovalenko-oai

> #54097 Show Daybreak notices after the session header @charliemarsh-oai

> #54098 Keep environment tools stable across readiness changes @aibrahim-oai

> #54099 Wait for readiness in the SIGTERM cancellation test @felixxia-oai

> #54113 Embed generated app-server schema bundles in Bazel builds @dkovalenko-oai

> #54133 Record per-tool incremental update and description size metrics @akira-oai

> #54135 Allow large file writes over direct exec-server WebSockets @ostepanian

> #54151 Generate keymap descriptors and binding accessors from one catalog @bc-openai

> #54217 Apply syntax theme colors to Markdown prose in the TUI @etraut-openai

> #54250 Add regression tests for case-variant metadata protection @jif-oai

> #54257 Preserve recent speech when trimming realtime transcripts @jif-oai

> #54263 Require fresh Guardian approval for escalated tool retries @jif-oai

> #54264 Track Guardian transcript admission across failed reviews @jif-oai

> #54309 Enable credential masking for remote exec-server commands @viyatb-oai

> #54315 Keep TUI Markdown colors readable against their backgrounds @fcoury-oai

> #54346 Add scoped executor credential auth for remote exec-server @viyatb-oai

> #54351 Use the turn index for turn-scoped item pagination @bz-openai

> #54363 Filter uninspectable network roots from implicit MXC read grants @iceweasel-oai

> #54365 Prevent duplicate assistant messages around interleaved commands @fcoury-oai

> #54369 Retry SQLite operations on transient writer contention @willwang-openai

> #54379 Add configuration support for TUI input presets @fcoury-oai

> #54380 Add `/presets` for reusable prompts and slash commands @fcoury-oai

> #54387 Add session-only arguments to `/title` and `/statusline` @fcoury-oai

> #54389 Preserve existing SQLite journal modes on startup @dkovalenko-oai

> #54398 Store generated image items as attachment references @kchainani-oai

> #54414 Allow root turn suspension with live descendants @miz-openai

> #54417 Skip SQLite page reclamation on Linux NFS mounts @dkovalenko-oai

> #54419 Support line breaks in Mermaid flowchart node labels @etraut-openai

> #54421 Treat explicit connections to the verified default daemon as local @etraut-openai

> #54433 Use neutral labels for nonzero exits in compact TUI output @bc-openai

> #54434 Add rotating stdin credentials for remote exec-server @viyatb-oai

> #54475 Use a synchronous mutex for remote metadata request tracking @anp-oai

> #54505 Add streaming file replacement to filesystem abstractions @anp-oai

> #54589 Preserve evidence message structure in Guardian Decisions requests @swastik-oai

> #54623 Resolve stable releases dynamically for exec-server compatibility tests @felixxia-oai

> #54637 Preserve disconnect reasons in Noise handshake errors @virajrai-oai

> #54639 Stream rollout records during thread history materialization @chess-oai

> #54654 Allow dynamic tool calls to execute in parallel @sdcoffey

> #54664 Distinguish retryable thread-store errors from unknown write outcomes @wiltzius-openai

> #54674 Add an opt-in tool for copying files between environments @anp-oai

> #54681 Keep TUI session selections bound to their backend @bc-openai

> #54708 Honor home deletion preferences during Windows uninstall @chess-oai

> #54710 Move V8's ICU Bazel rules into the workspace @seanh-oai

> #54716 Keep prereleases in draft until release assets finish uploading @ioanbudea-OAI

> #54724 Preserve prereleased events when creating GitHub prereleases @ioanbudea-OAI

> #54739 Close arg0 lock files before removing temporary directories @dkovalenko-oai

> #54741 Gate the file-copy extension behind `multi_env_copy_file` @anp-oai

> #54776 Support typed content in contextual prompt fragments @pakrym-oai

> #54930 Add negotiated zstd compression to app-server WebSockets @thorvald-oai

> #54949 Gate app-server WebSocket compression behind a feature flag @thorvald-oai

> #55149 Prune unused standalone releases after successful installation @etraut-openai

> #55226 Bucket admitted Guardian request metrics by input size @ioanbudea-OAI

> #55227 Allow plus signs in metric tags @swastik-oai

> #55234 Record Guardian sampling retries, attempts, and delivery outcomes @ioanbudea-OAI

> #55237 Add Guardian review routing and cached score metrics @ioanbudea-OAI

> #55244 Batch thread history materialization into SQLite @jif-oai

> #55252 Preserve rollout access metadata across compression and restoration @jif-oai

> #55255 Unload idle ephemeral composer prediction threads without delay @jif-oai

> #55270 Honor per-thread unload delays in app-server @jif-oai

> #55274 Stabilize daemon reconnect and Rosetta package startup tests @jif-oai

> #55283 Avoid cloning events in the app-server thread listener @charliemarsh-oai

> #55288 Recheck EMA request authority at HTTP boundaries @jif-oai

> #55297 Add GitHub Actions OIDC token acquisition to the responses API proxy @ee-oai

> #55298 Add renewable federated auth primitives to the Responses API proxy @ee-oai

> #55299 Refresh rejected proxy credentials and back off failed renewals @ee-oai

> #55300 Add one-shot app-server startup configuration discovery @acrognale-oai

> #55302 Stop the closest remote SHA search at zero distance @jif-oai

> #55303 Route skill reads by alias source @TAFOYA-OAI

> #55304 Reject TUI events from a different backend @bc-openai

> #55322 Integrate discovery V2 with step-scoped skill catalogs @TAFOYA-OAI

> #55324 Remove thread title generation spinners from the TUI @cconger

> #55330 Expose skill installations and stabilize package aliases @TAFOYA-OAI

> #55339 Add experimental `thread/sample` requests to the app server @liame-oai

> #55342 Consolidate cached and fetched Codex manual handling @kkahadze-oai

> #55347 Add Guardian retry metrics and preserve turn attribution @ioanbudea-OAI

> #55351 Reduce path storage in the file-search index @charliemarsh-oai

> #55357 Prepare skill catalogs before building step tools @TAFOYA-OAI

> #55365 Import only the continuation of backgrounded Claude sessions @jgrodman-arch

> #55368 Enable incremental tools by default for Responses Lite @akira-oai

> #55379 Handle response body failures in OpenAI docs downloads @kkahadze-oai

> #55380 Preserve thread metadata before rollout files are materialized @jif-oai

> #55381 Manage TUI backend sessions independently @bc-openai

> #55387 Add support for Academic Researchers plans @etraut-openai

> #55388 Mark `transcript_v2` as removed @etraut-openai

> #55395 Roll back interrupted Guardian reviews to preserve evidence @jif-oai

> #55396 Prefetch sibling rollout paths when reading history pages @bz-openai

> #55401 Defer environment disconnect notifications until recovery fails @richardopenai

> #55402 Add ephemeral runtime registration and signed assertions @cooper-oai

> #55406 Trace harness-side Noise handshake failures @alishobeiri-oai

> #55409 Retry TUI startup after a server shutdown refusal @fcoury-oai

> #55410 Track credential sources separately from auth owners @cooper-oai

> #55411 Render async question prompts as Markdown in the TUI @bc-openai

> #55441 Add cancellation for experimental thread samples @liame-oai

> #55442 Check daemon feature overrides and prompt for mismatch recovery @etraut-openai

> #55456 Support Windows registry overrides for `requirements.toml` @johnl-oai

> #55498 Add correlated diagnostics for Noise relay handshakes @virajrai-oai

> #55524 Make the startup migration contention test deterministic @jif-oai

> #55533 Separate Guardian conversation preparation from execution @swastik-oai

> #55545 Improve diagnostics for compressed rollout read failures @jif-oai

> #55547 Ignore the basic-toml advisory in dependency audits @jif-oai

> #55591 Measure Guardian approval blocking time per turn @ioanbudea-OAI

> #55616 Update `rustls-webpki` and `webpki-roots` lockfile versions @jif-oai

> #55623 Refactor Guardian v2 Decisions snapshot comparison @swastik-oai

> #55627 Reserve a sibling rollout candidate slot for the first ancestor @bz-openai

> #55631 Add frozen cloud skill snapshots to the app server @fc-oai

> #55635 Enable Decisions comparisons for Guardian V2 conversation mode @swastik-oai

> #55645 Fix in-process app-server shutdown with full queues @jif-oai

> #55652 Search compressed rollouts concurrently @ethernetdan-openai

> #55653 Track code-mode cell lifecycle and result buffering time @euroelessar

> #55677 Upgrade the Rust toolchain to 1.99.1 @dkovalenko-oai

> #55685 Add account credential support to EMA token exchange helpers @jif-oai

> #55689 Clean up failed and abandoned marketplace staging directories @dkovalenko-oai

> #55690 Reclaim aged legacy marketplace staging directories @dkovalenko-oai

> #55692 Tag tool registration metrics with effective incremental tools mode @akira-oai

> #55705 Centralize cloud skill cache state under the catalog lock @TAFOYA-OAI

> #55719 Allow unified exec to fall back when credential masking is unavailable @viyatb-oai

> #55723 Avoid redundant clones when sending app-server notifications @charliemarsh-oai

> #55725 Preserve code cell response metadata in rollout traces @cassirer-openai

> #55804 Add a critical-path utility for exclusive duration attribution @taohong339

> #55847 Bound retained turn analytics and clean up closed threads @jif-oai

> #55848 Pause relay test time while inspecting handshake diagnostics @jif-oai

> #55856 Bound managed app-server and updater stderr logging @jif-oai

> #55913 Skip conversation scoring superseded by newer scores and history @jif-oai

> #55940 Add local diagnostic ZIP exports to the app server @viktor-oai

> #55954 Separate retained instruction collection from budget policy @ioanbudea-OAI

> #55969 Drain WebSocket responses on mailbox preemption @jif-oai

> #55971 Add storage namespaces for local message boards @felixxia-oai

> #55973 Allow consumers to select message-board tools @felixxia-oai

> #55978 Route SQLite logs to an explicitly configured `log_dir` @dkovalenko-oai

> #55987 Refresh remote exec-server credentials after unauthorized responses @apanasenko-oai

> #56003 Scope MITM credential substitution to trusted origins and placeholders @viyatb-oai

> #56007 Pause Tokio time in the reused Guardian session test @goodman-oai

> #56008 Add a critical-path timing recorder for direct tool calls @taohong339

> #56020 Allow thread sampling after failed or interrupted turns @liame-oai

> #56022 Preserve config overrides across CLI subcommand boundaries @jmickey-oai

> #56024 Limit decoded HTTP/3 response headers in the TCP tunnel @richardopenai

> #56031 Support client Responses API metadata in `thread/sample` @liame-oai

> #56033 Enable the Bedrock setup wizard by default @alexsong-oai

> #56037 Add a channel-backed cloud app-server client @bc-openai

> #56049 Support configured credential providers in remote execution @viyatb-oai

> #56055 Require managed configuration from the configured server @smurching-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-23-24-account-and-access-changes-in-rust-v0-164-0|24 Account and Access changes in rust-v0.164.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-23-8-mobile-and-desktop-changes-in-rust-v0-164-0|8 Mobile and Desktop changes in rust-v0.164.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]] · Context Window
- [[Changes/Codex CLI/2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0|30 Apps and Integrations changes in rust-v0.164.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-9-interface-experience-changes-in-rust-v0-164-0|9 Interface Experience changes in rust-v0.164.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-23-9-model-support-changes-in-rust-v0-164-0|9 Model Support changes in rust-v0.164.0]] · Model Support
- [[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14 Developer Workflow changes in rust-v0.164.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice and Audio changes in rust-v0.164.0]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-23-2f4dd5&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-23-183-other-changes-in-rust-v0-164-0.md%0ACard%20ID%3A%20codex-cli-2026-10-23-2f4dd5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.164.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->