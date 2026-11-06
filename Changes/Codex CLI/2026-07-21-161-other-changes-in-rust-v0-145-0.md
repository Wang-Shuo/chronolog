---
card_id: codex-cli-2026-07-21-7600e6
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Other changes: 161 changes in 0.145.0 — Updated
  the packaged ripgrep binary to 15.2.0. (#34384)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 44e03dd00b7f85ab168f88c56afbdb32ee0b4e2b5b5d84713ece995ce6a91944
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-7600e6
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 161 other changes'
  evidence:
  - quote: Updated the packaged ripgrep binary to 15.2.0. (#34384)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31667 fix: parse compact release metadata in installer @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31566 perf(skills): reuse walk inventory for host loading @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31576 Bound exec-server process event reordering @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31756 test(skills): assert symlinked metadata loading @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31581 Resolve selected capability roots without starting executors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31789 Stop persisting RMCP service traces @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31792 Summarize streamed response item logs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31791 Filter routine Hyper logs from SQLite @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31767 Remove the network proxy config wrapper @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31363 codex-api: route file uploads through HTTP client factory @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31830 fix(sandboxing): initialize network proxy config inline @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31431 build: ratchet direct reqwest dependencies @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31876 code-mode: fix installation on darwin @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31899 code-mode: fall back to using in process v8 if we fail to resolve
      external process @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31892 exec-server: materialize filesystem workspace roots @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31295 bench: add codex help e2e macrobenchmark @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31428 bench: add e2e benchmark entrypoints @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32093 Remove the legacy exec policy engine @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32112 Bound streamed exec-server HTTP response bodies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32123 Bound exec-server stdio JSON-RPC messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32126 Test bounded concurrency in ancestor discovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32134 Test stdio JSON-RPC size limits with LF and CRLF @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32135 Propagate tracing subscribers to exec start tasks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32150 Keep unified exec output collection bounded @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32200 Add a skill invocation extension contributor @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32213 Generate unique IDs for review rollout messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32214 Propagate workspace roots to exec-server sandboxes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32231 Support pending remote environment registration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32234 Add dedicated storage for paginated thread history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32246 Extract reverse JSONL scanning from session indexing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32256 Improve Responses WebSocket timing telemetry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32261 Preserve local path conventions in automatic approvals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32276 Repair unterminated rollout files before appending @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32289 Persist paginated items in the local thread store @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32305 Improve file blob upload diagnostics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32312 Require prefixes for outbound response item IDs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32326 Use canonical links in the moved config notice @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32332 Add ordinals to paginated rollout records @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32460 Emit thread-idle lifecycle after guardian interrupts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32485 Use available width for skill names in the toggle view @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32747 Align Guardian reviews with session configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32838 Reap exited PID-managed app-server children @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32844 Expand millisecond duration histogram boundaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32849 Hide Windows filesystem helper console windows @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32897 Route blocked network requests to their owning calls @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32899 Add exec-server environment status checks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32903 Include session IDs in tool item analytics events @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32905 Timestamp app-server notifications at emission @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32920 Expose environment status through app-server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32923 Materialize paginated thread history in SQLite @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32928 Resume thread history projection from its SQLite checkpoint @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32945 Restrict Guardian reviewer tools @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32952 Scope runtime workspace roots to execution environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32985 Expose exact per-response usage in raw app-server events @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32989 Always confirm before enabling full access @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33013 Bound exec-server JSON-RPC decoding complexity @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33026 Include raw response completions in TypeScript envelopes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33031 Preserve JSON number precision in exec-server RPC messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33093 Preserve streamed output during capped history replay @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33105 Fix TUI status visibility around streamed output @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33107 Preserve special filesystem subpaths as wire strings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33109 Reject forks of paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33152 Support paginated thread history in app-server list APIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33155 Trace startup prewarm tasks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33159 Move sleep items to the extension-owned lifecycle path @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33166 Defer Noise environment connections until registration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33175 Handle Amazon Bedrock credentials during logout @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33185 Keep approval test targets in the temporary home @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33187 Honor workspace spend controls in rate-limit handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33198 Keep interrupted prompts in conversation history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33203 Preserve in-flight state when restoring thread input @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33209 Separate session state from session I/O @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33239 Render TUI composer tabs as single-column spaces @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33251 Report selected environment connection transitions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33261 Add Frameless Bidi support for realtime conversations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33364 Enable paginated thread history in app-server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33369 Scan skill roots concurrently @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33373 Render TUI prompts before submitting user turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33425 Refresh host skill catalogs through world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33426 Add Cursor support to setup import @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33435 Warn on conflicting capability root locations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33441 Shut down Codex threads after approval scenarios @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33446 Remove the unused network proxy loader @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33457 Use final answers in turn history summaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33632 Remove generated-default filesystem path variants @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33633 Clarify when to wait for starting environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33636 Clarify when to wait for starting environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33639 Remove the unused realtime WebRTC crate @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33640 Avoid duplicate cached app list update notifications @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33651 Add an app-server API for reading app metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33658 Keep active-turn environments stable across settings updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33659 Require data URLs for code-mode image output @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33665 Refresh step world state for all sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33680 Reword the apply_patch tool description @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33684 Extract TUI approval request payloads into structs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33687 Avoid unnecessary writes during migration repair @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33695 Support custom transports for Amazon Bedrock @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33842 Give the zsh fork decline test more execution time @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33843 Add an API for reading installed app runtime state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33845 Confirm usage-limit resets before redemption @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33848 Fix the managed Bedrock logout test assertion @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33852 Add batched executor capability discovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33855 Tag realtime transcript tail flush delegations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33856 Stream realtime V3 Codex handoff output @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33861 Test workspace write isolation across exec servers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33863 Report detailed session import error types @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33864 Keep feature tests focused on behavior @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33866 Remove the redundant tool dispatch wrapper @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33867 Add grace period to code-mode yield timeouts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33868 Remove stale ignored core tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33870 Remove the redundant borrowed line wrapping helper @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33892 Limit rollout metadata reads to headers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33893 Track realtime conversation state in world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33902 Add bounded batch lookups for message history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33903 Route realtime V3 handoffs by response channel @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33905 Batch persistent history reads during reverse search @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33906 Launch managed network proxies on remote executors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33907 Add occurrence search for paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33925 Render inline visualization links in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33930 Track inherited paginated rollout prefixes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33938 Centralize SQLite connection configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33950 Let users remember the working directory for resumed sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34038 Handle compressed rollouts in doctor thread inventory @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34045 Render streamed Markdown incrementally @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34049 Avoid redundant TUI redraws while streaming @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34067 Seed realtime V3 sessions with initial text items @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34085 Support legacy views for paginated thread history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34197 Use the Markdown collector as the streaming source of truth @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34198 Start side conversations without replaying inherited turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34199 Avoid liveness races when starting side conversations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34204 Avoid cloning buffered TUI history lines @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34222 Avoid buffering replay-irrelevant thread notifications @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34229 Persist names for paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34232 Remeasure dynamic cells in the transcript overlay @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34271 Migrate legacy exec policy allow rules @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34344 Reject unsupported history modes when loading rollouts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34345 Remove unused Rust helpers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34346 Track inline visualization directives during streaming @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34347 Avoid cloning deferred TUI lifecycle payloads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34348 Cache TUI flex heights across frame passes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34355 Parallelize TUI bootstrap requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34361 Avoid cloning thread history for token usage replay @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34368 Use app-server skill metadata directly in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34371 Clear stale Guardian reviews when turns end @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34380 Stop retrying turns with invalid tool images @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34381 Avoid cloning Responses WebSocket payloads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34384 Update packaged ripgrep to 15.2.0 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34390 Use copy-on-write storage for history snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34392 Ignore inherited ACEs when refreshing Windows write roots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34400 Propagate approval rejection reasons @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34403 Update tests for history and hook API changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34407 Resolve paginated rollout lineages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34409 Limit the Linux `/proc` preflight filesystem view @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34411 Require absolute paths for test SQLite configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34416 Show completed hook warnings in TUI headers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34423 Support Windows sandboxing in the exec server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34434 Support catalog messages for non-request approval policies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34435 Resolve outbound proxy routes explicitly @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34438 Increase the patch approval test timeout @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34441 Add buffered code-mode exec yields @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 161-other-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: uncategorized
  title: 161 other changes in rust-v0.145.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: uncategorized
title: 161 other changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 161 other changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Updated the packaged ripgrep binary to 15.2.0. (#34384)

> #31667 fix: parse compact release metadata in installer @efrazer-oai

> #31566 perf(skills): reuse walk inventory for host loading @jif-oai

> #31576 Bound exec-server process event reordering @jif-oai

> #31756 test(skills): assert symlinked metadata loading @jif-oai

> #31581 Resolve selected capability roots without starting executors @jif-oai

> #31789 Stop persisting RMCP service traces @jif-oai

> #31792 Summarize streamed response item logs @jif-oai

> #31791 Filter routine Hyper logs from SQLite @jif-oai

> #31767 Remove the network proxy config wrapper @jif-oai

> #31363 codex-api: route file uploads through HTTP client factory @bolinfest

> #31830 fix(sandboxing): initialize network proxy config inline @fcoury-oai

> #31431 build: ratchet direct reqwest dependencies @bolinfest

> #31876 code-mode: fix installation on darwin @cconger

> #31899 code-mode: fall back to using in process v8 if we fail to resolve external process @cconger

> #31892 exec-server: materialize filesystem workspace roots @pakrym-oai

> #31295 bench: add codex help e2e macrobenchmark @anp-oai

> #31428 bench: add e2e benchmark entrypoints @anp-oai

> #32093 Remove the legacy exec policy engine @copyberry

> #32112 Bound streamed exec-server HTTP response bodies @copyberry

> #32123 Bound exec-server stdio JSON-RPC messages @copyberry

> #32126 Test bounded concurrency in ancestor discovery @copyberry

> #32134 Test stdio JSON-RPC size limits with LF and CRLF @copyberry

> #32135 Propagate tracing subscribers to exec start tasks @copyberry

> #32150 Keep unified exec output collection bounded @copyberry

> #32200 Add a skill invocation extension contributor @copyberry

> #32213 Generate unique IDs for review rollout messages @copyberry

> #32214 Propagate workspace roots to exec-server sandboxes @copyberry

> #32231 Support pending remote environment registration @copyberry

> #32234 Add dedicated storage for paginated thread history @copyberry

> #32246 Extract reverse JSONL scanning from session indexing @copyberry

> #32256 Improve Responses WebSocket timing telemetry @copyberry

> #32261 Preserve local path conventions in automatic approvals @copyberry

> #32276 Repair unterminated rollout files before appending @copyberry

> #32289 Persist paginated items in the local thread store @copyberry

> #32305 Improve file blob upload diagnostics @copyberry

> #32312 Require prefixes for outbound response item IDs @copyberry

> #32326 Use canonical links in the moved config notice @copyberry

> #32332 Add ordinals to paginated rollout records @copyberry

> #32460 Emit thread-idle lifecycle after guardian interrupts @copyberry

> #32485 Use available width for skill names in the toggle view @copyberry

> #32747 Align Guardian reviews with session configuration @copyberry

> #32838 Reap exited PID-managed app-server children @copyberry

> #32844 Expand millisecond duration histogram boundaries @copyberry

> #32849 Hide Windows filesystem helper console windows @copyberry

> #32897 Route blocked network requests to their owning calls @copyberry

> #32899 Add exec-server environment status checks @copyberry

> #32903 Include session IDs in tool item analytics events @copyberry

> #32905 Timestamp app-server notifications at emission @copyberry

> #32920 Expose environment status through app-server @copyberry

> #32923 Materialize paginated thread history in SQLite @copyberry

> #32928 Resume thread history projection from its SQLite checkpoint @copyberry

> #32945 Restrict Guardian reviewer tools @copyberry

> #32952 Scope runtime workspace roots to execution environments @copyberry

> #32985 Expose exact per-response usage in raw app-server events @copyberry

> #32989 Always confirm before enabling full access @copyberry

> #33013 Bound exec-server JSON-RPC decoding complexity @copyberry

> #33026 Include raw response completions in TypeScript envelopes @copyberry

> #33031 Preserve JSON number precision in exec-server RPC messages @copyberry

> #33093 Preserve streamed output during capped history replay @copyberry

> #33105 Fix TUI status visibility around streamed output @copyberry

> #33107 Preserve special filesystem subpaths as wire strings @copyberry

> #33109 Reject forks of paginated threads @copyberry

> #33152 Support paginated thread history in app-server list APIs @copyberry

> #33155 Trace startup prewarm tasks @copyberry

> #33159 Move sleep items to the extension-owned lifecycle path @copyberry

> #33166 Defer Noise environment connections until registration @copyberry

> #33175 Handle Amazon Bedrock credentials during logout @copyberry

> #33185 Keep approval test targets in the temporary home @copyberry

> #33187 Honor workspace spend controls in rate-limit handling @copyberry

> #33198 Keep interrupted prompts in conversation history @copyberry

> #33203 Preserve in-flight state when restoring thread input @copyberry

> #33209 Separate session state from session I/O @copyberry

> #33239 Render TUI composer tabs as single-column spaces @copyberry

> #33251 Report selected environment connection transitions @copyberry

> #33261 Add Frameless Bidi support for realtime conversations @copyberry

> #33364 Enable paginated thread history in app-server @copyberry

> #33369 Scan skill roots concurrently @copyberry

> #33373 Render TUI prompts before submitting user turns @copyberry

> #33425 Refresh host skill catalogs through world state @copyberry

> #33426 Add Cursor support to setup import @copyberry

> #33435 Warn on conflicting capability root locations @copyberry

> #33441 Shut down Codex threads after approval scenarios @copyberry

> #33446 Remove the unused network proxy loader @copyberry

> #33457 Use final answers in turn history summaries @copyberry

> #33632 Remove generated-default filesystem path variants @copyberry

> #33633 Clarify when to wait for starting environments @copyberry

> #33636 Clarify when to wait for starting environments @copyberry

> #33639 Remove the unused realtime WebRTC crate @copyberry

> #33640 Avoid duplicate cached app list update notifications @copyberry

> #33651 Add an app-server API for reading app metadata @copyberry

> #33658 Keep active-turn environments stable across settings updates @copyberry

> #33659 Require data URLs for code-mode image output @copyberry

> #33665 Refresh step world state for all sessions @copyberry

> #33680 Reword the apply_patch tool description @copyberry

> #33684 Extract TUI approval request payloads into structs @copyberry

> #33687 Avoid unnecessary writes during migration repair @copyberry

> #33695 Support custom transports for Amazon Bedrock @copyberry

> #33842 Give the zsh fork decline test more execution time @copyberry

> #33843 Add an API for reading installed app runtime state @copyberry

> #33845 Confirm usage-limit resets before redemption @copyberry

> #33848 Fix the managed Bedrock logout test assertion @copyberry

> #33852 Add batched executor capability discovery @copyberry

> #33855 Tag realtime transcript tail flush delegations @copyberry

> #33856 Stream realtime V3 Codex handoff output @copyberry

> #33861 Test workspace write isolation across exec servers @copyberry

> #33863 Report detailed session import error types @copyberry

> #33864 Keep feature tests focused on behavior @copyberry

> #33866 Remove the redundant tool dispatch wrapper @copyberry

> #33867 Add grace period to code-mode yield timeouts @copyberry

> #33868 Remove stale ignored core tests @copyberry

> #33870 Remove the redundant borrowed line wrapping helper @copyberry

> #33892 Limit rollout metadata reads to headers @copyberry

> #33893 Track realtime conversation state in world state @copyberry

> #33902 Add bounded batch lookups for message history @copyberry

> #33903 Route realtime V3 handoffs by response channel @copyberry

> #33905 Batch persistent history reads during reverse search @copyberry

> #33906 Launch managed network proxies on remote executors @copyberry

> #33907 Add occurrence search for paginated threads @copyberry

> #33925 Render inline visualization links in the TUI @copyberry

> #33930 Track inherited paginated rollout prefixes @copyberry

> #33938 Centralize SQLite connection configuration @copyberry

> #33950 Let users remember the working directory for resumed sessions @copyberry

> #34038 Handle compressed rollouts in doctor thread inventory @copyberry

> #34045 Render streamed Markdown incrementally @copyberry

> #34049 Avoid redundant TUI redraws while streaming @copyberry

> #34067 Seed realtime V3 sessions with initial text items @copyberry

> #34085 Support legacy views for paginated thread history @copyberry

> #34197 Use the Markdown collector as the streaming source of truth @copyberry

> #34198 Start side conversations without replaying inherited turns @copyberry

> #34199 Avoid liveness races when starting side conversations @copyberry

> #34204 Avoid cloning buffered TUI history lines @copyberry

> #34222 Avoid buffering replay-irrelevant thread notifications @copyberry

> #34229 Persist names for paginated threads @copyberry

> #34232 Remeasure dynamic cells in the transcript overlay @copyberry

> #34271 Migrate legacy exec policy allow rules @copyberry

> #34344 Reject unsupported history modes when loading rollouts @copyberry

> #34345 Remove unused Rust helpers @copyberry

> #34346 Track inline visualization directives during streaming @copyberry

> #34347 Avoid cloning deferred TUI lifecycle payloads @copyberry

> #34348 Cache TUI flex heights across frame passes @copyberry

> #34355 Parallelize TUI bootstrap requests @copyberry

> #34361 Avoid cloning thread history for token usage replay @copyberry

> #34368 Use app-server skill metadata directly in the TUI @copyberry

> #34371 Clear stale Guardian reviews when turns end @copyberry

> #34380 Stop retrying turns with invalid tool images @copyberry

> #34381 Avoid cloning Responses WebSocket payloads @copyberry

> #34384 Update packaged ripgrep to 15.2.0 @copyberry

> #34390 Use copy-on-write storage for history snapshots @copyberry

> #34392 Ignore inherited ACEs when refreshing Windows write roots @copyberry

> #34400 Propagate approval rejection reasons @copyberry

> #34403 Update tests for history and hook API changes @copyberry

> #34407 Resolve paginated rollout lineages @copyberry

> #34409 Limit the Linux `/proc` preflight filesystem view @copyberry

> #34411 Require absolute paths for test SQLite configuration @copyberry

> #34416 Show completed hook warnings in TUI headers @copyberry

> #34423 Support Windows sandboxing in the exec server @copyberry

> #34434 Support catalog messages for non-request approval policies @copyberry

> #34435 Resolve outbound proxy routes explicitly @copyberry

> #34438 Increase the patch approval test timeout @copyberry

> #34441 Add buffered code-mode exec yields @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.145.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-21-12-developer-workflow-changes-in-rust-v0-145-0|12 Developer Workflow changes in rust-v0.145.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-07-21-12-context-window-changes-in-rust-v0-145-0|12 Context Window changes in rust-v0.145.0]] · Context Window
- [[Changes/Codex CLI/2026-07-21-4-editor-experience-changes-in-rust-v0-145-0|4 Editor Experience changes in rust-v0.145.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0|17 Safety and Privacy changes in rust-v0.145.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-21-3-mobile-and-desktop-changes-in-rust-v0-145-0|3 Mobile and Desktop changes in rust-v0.145.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-21-3-image-generation-changes-in-rust-v0-145-0|3 Image Generation changes in rust-v0.145.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-21-22-model-support-changes-in-rust-v0-145-0|22 Model Support changes in rust-v0.145.0]] · Model Support
- [[Changes/Codex CLI/2026-07-21-33201-branch-conversations-when-editing-earlier-tui-prompts-copyberry|♯33201 Branch conversations when editing earlier TUI prompts @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0|3 Reliability and Performance changes in rust-v0.145.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167 Document the Windows exec yield time range @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-7600e6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-161-other-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-7600e6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->