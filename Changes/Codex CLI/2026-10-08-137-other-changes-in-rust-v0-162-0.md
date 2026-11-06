---
card_id: codex-cli-2026-10-08-34377d
date: '2026-10-08'
description: 'Codex CLI · 2026-10-08 · Other changes: 137 changes in 0.162.0 — Add
  JavaScript helpers for streaming promise results as they settle, plus opt-in ranked
  tool…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eef2abf6a011c9c2e3d3a94471b820b5b585788690a526508c7594339eb51110
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-08-34377d
  comparison: ''
  date: '2026-10-08'
  description: 'Codex CLI — 0.162.0: 137 other changes'
  evidence:
  - quote: 'Add JavaScript helpers for streaming promise results as they settle, plus
      opt-in ranked tool search in Code Mode. (#51126, #51209)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: Preserve existing CRLF line endings in `apply_patch` updates without requiring
      an opt-in. (#51203)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: 'Honor server `Retry-After` advice for retryable Responses and WebSocket
      failures. (#50418, #51440)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: Publish a signed PowerShell installer with Windows releases. (#51158)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: 'Keep older stable releases and prereleases from replacing newer stable
      download targets or installer aliases. (#51186, #51425)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50018 Use descriptor-safe helpers for executable test fixtures @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50019 Protect the guardian decisions API key from environment forwarding
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50039 Keep transcript Find results readable after closing the query @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50045 Keep transcript Find expansion scoped to the current match @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50054 Check token estimate filtering directly on the tracing subscriber
      @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50058 Upgrade Windows bindings to `windows-sys` 0.61.2 @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50066 Add a bounded Decisions transport for Guardian comparison classification
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50083 Add paginated reverse lookup for thread attachments @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50094 Add attachment owner lookup to the app-server @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50099 Add opt-in Decisions comparison for Guardian V2 @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50105 Consolidate chat composer footer logic in `footer_state` @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50112 Centralize TUI loading glyphs and frame scheduling @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50113 Add a native gRPC client for cloud thread resume and attach @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50131 Add opt-in JSON diagnostics for TCP tunnels @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50162 Bound in-flight file opens in exec-server @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50166 Upgrade `age` to 0.12.1 and remove the obsolete advisory exception
      @michaelm-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50177 Enable writable file streaming in exec-server @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50183 Add `dots` to issue labeler guidance @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50199 Restore the account email in `/status` after account updates @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50200 Report the configured TUI mode in `codex doctor` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50207 Release stable Markdown tables into scrollback during streaming
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50215 Support Ctrl+Insert for copying TUI selections @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50219 Bound tmux option probes to one second @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50354 Skip unrelated subtrees during config alias normalization @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50359 Render ANSI styles in TUI hook system messages @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50360 Remove initial messages from session configuration events @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50396 Honor pager bindings for transcript page keys @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50418 Honor Retry-After headers in failed Responses events @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50433 Allow API-key accounts to use Daybreak in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50435 Persist additional tool definitions in rollout history @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50442 Preserve native USD amounts in thread usage responses @asohrabi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50443 Stabilize paused-time code-mode service tests @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50445 Assert that only direct tool calls emit timing events @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50446 Bundle rollout attachments into a gzip tar archive @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50447 Remove the provider capability gate for tool namespaces @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50454 Measure rollout persistence size reductions @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50462 Populate thread previews from delegated task inputs @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50464 Add the `incremental_tools` feature flag @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50467 Copy transcript selections as literal text while preserving rich
      HTML @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50477 Use the app-server default output cap for TUI workspace commands
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50499 Include installer stderr in daemon update failures @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50503 Use Enter to accept transcript Find results and Escape to cancel
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50504 Center TUI confirmations over their retained backdrop @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50510 Require GovCloud guidance acknowledgment after Bedrock setup @jackz100'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50525 Reject unknown TUI keys in strict config validation @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50531 Persist realtime transcript tails before closure without inference
      @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50540 Send incremental tool catalog updates in Responses Lite @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50558 Avoid reading the current directory when resolving absolute paths
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50559 Distinguish daemon release identity from executable contents @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50562 Keep Code Mode tool discovery guidance stable across catalog changes
      @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50687 Keep third-party tools deferred in strict Code Mode Only @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50695 Preserve local Markdown link labels in the TUI @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50741 Keep environment-backed tools exposed across readiness changes
      @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50756 Show unavailable slash commands when searched in side conversations
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50764 Allow `/archive` while a turn is running @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50782 Retry Windows daemon release publication on transient file locks
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50788 Open slash commands from empty drafts in Vim Normal mode @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50802 Fall back to mklink when Windows daemon junction updates are denied
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50804 Preserve review lifecycle ordering on failure @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50808 Prune TUI snapshots and consolidate behavior tests @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50940 Recover malformed Windows deny-read ACL state safely @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50962 Gate stable environment tool exposure behind a feature flag @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50964 Track inference tool changes in turn analytics @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#50977 Isolate tracing in the strict third-party tool deferral test @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51061 Gate Guardian continuation tests on classifier request capture
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51063 Honor prior cancellation before starting Codex delegates @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51065 Scope Guardian V2 response timing to snapshot sampling @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51119 Clarify incremental tool namespace updates in Responses Lite @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51126 Add promise settlement streaming helpers to code mode @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51133 Allow Guardian Decisions to fall back to `OPENAI_API_KEY` @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51137 Recover Guardian reviews from parent checkpoints @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51139 Force fresh Guardian sessions for parent-checkpoint recovery @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51140 Isolate Guardian checkpoint recovery flags per review attempt @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51156 Send base instructions as Responses input messages @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51158 Sign the PowerShell installer in Windows releases @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51185 Retry transient gRPC code-mode session admission failures @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51186 Prevent stable release pointers from moving backward @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51188 Record base instructions in incremental tool history @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51191 Clean up Unix app-server control-socket startup lock files @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51192 Wait for SIGCONT when resuming the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51193 Test thread archiving before the first turn @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51194 Add browser extension request headers to config requirements @jn-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51198 Allow concurrent release builds while serializing publication @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51200 Upgrade Bazel to 9.2.0 and refresh the module lockfile @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51202 Distinguish namespace removals in incremental tool updates @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51203 Make apply_patch preserve line endings unconditionally @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51209 Add ranked tool discovery to JavaScript code mode @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51217 Preserve review targets and scope misalignment continuation metadata
      @yunhan-wei'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51220 Honor the OTLP metrics temporality preference @daniel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51221 Separate environment requests from runtime selections @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51230 Make session lookup pagination stable and report listing failures
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51241 Add a partial answer message phase @rb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51253 Enforce Fast and Ultra Fast policies independently @dpatel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51257 Fix installer checksum verification under Windows PowerShell @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51260 Handle partial answers in realtime routing and thread search @rb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51330 Measure total Guardian approval decision duration @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51334 Count Guardian denial-limit interruptions in telemetry @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51378 Keep Guardian v2 WebSocket pools warm with concurrent replenishment
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51391 Make URLs in asynchronous question titles clickable @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51396 Let late low-risk scores complete pending Guardian reviews @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51400 Prevent later Guardian scores from releasing earlier pending reviews
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51411 Suppress repeated image paste presses in legacy terminals @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51415 Expose and persist turn lineage across the app server @eddie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51419 Preserve turn attribution when queued mail wakes durable sleep
      @eddie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51420 Finish idle thread unloads after slow shutdown @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51422 Accept environment requests at thread and turn settings boundaries
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51425 Skip stable installer alias publishing for prereleases @zsol-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51427 Prevent invalidated wakeups from starting a turn @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51439 Preserve clickable URLs in TUI approval headers @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51440 Honor Retry-After in WebSocket error events @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51449 Make URLs clickable in TUI user input questions @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51451 Make URLs in the TUI warnings viewer clickable @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51452 Make banner URLs clickable across wrapped lines @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51457 Preserve status usage hyperlinks when the URL wraps @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51458 Make URLs clickable in user verification prompts @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51460 Retry realtime sideband attachment while an existing call activates
      @bullman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51465 Add an optional JSON transcript format for Guardian @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51466 Keep Guardian transcript records structured through budget recovery
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51467 Keep submission logs useful without exposing payloads @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51470 Raise the managed app-server file descriptor limit on Unix @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51471 Preserve clickable URLs in pending input previews @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51473 Preserve URL destinations in wrapped hook details @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51482 Use PathUri for skill identity and path matching @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51483 Add correlated, credential-free rendezvous connection diagnostics
      @alexi-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51491 Classify executor capability root ownership independently of parsing
      @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51493 Bind capability roots to environment selections @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51499 Load rollout history on a single blocking worker @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51502 Bound relay connection attempts and handle pongs during blocked
      writes @alexi-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51510 Preserve live TUI settings when configuration reloads fail @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51511 Fix Windows 10 drive-letter opens for no-follow filesystem operations
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51517 Pass thread persistence intent to attachment uploads @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  - quote: '#51525 Preserve the CLI MXC preference in executor config reads @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.162.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 137-other-changes-in-rust-v0-162-0
  source_release: codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db
  source_type: github_releases
  theme: uncategorized
  title: 137 other changes in rust-v0.162.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db]]'
source_type: github_releases
theme: uncategorized
title: 137 other changes in rust-v0.162.0
type: change
---

<!-- chronolog:begin region="header" -->
# 137 other changes in rust-v0.162.0

**Codex CLI** · 2026-10-08 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.162.0) · from [[Releases/Codex CLI/codex-cli-2026-10-08-rust-v0-162-0-github-407151970-b80d60db|0.162.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add JavaScript helpers for streaming promise results as they settle, plus opt-in ranked tool search in Code Mode. (#51126, #51209)

> Preserve existing CRLF line endings in `apply_patch` updates without requiring an opt-in. (#51203)

> Honor server `Retry-After` advice for retryable Responses and WebSocket failures. (#50418, #51440)

> Publish a signed PowerShell installer with Windows releases. (#51158)

> Keep older stable releases and prereleases from replacing newer stable download targets or installer aliases. (#51186, #51425)

> #50018 Use descriptor-safe helpers for executable test fixtures @jif-oai

> #50019 Protect the guardian decisions API key from environment forwarding @swastik-oai

> #50039 Keep transcript Find results readable after closing the query @fcoury-oai

> #50045 Keep transcript Find expansion scoped to the current match @fcoury-oai

> #50054 Check token estimate filtering directly on the tracing subscriber @tamird

> #50058 Upgrade Windows bindings to `windows-sys` 0.61.2 @tamird

> #50066 Add a bounded Decisions transport for Guardian comparison classification @swastik-oai

> #50083 Add paginated reverse lookup for thread attachments @joeytrasatti-openai

> #50094 Add attachment owner lookup to the app-server @joeytrasatti-openai

> #50099 Add opt-in Decisions comparison for Guardian V2 @swastik-oai

> #50105 Consolidate chat composer footer logic in `footer_state` @imac-oai

> #50112 Centralize TUI loading glyphs and frame scheduling @imac-oai

> #50113 Add a native gRPC client for cloud thread resume and attach @bc-openai

> #50131 Add opt-in JSON diagnostics for TCP tunnels @richardopenai

> #50162 Bound in-flight file opens in exec-server @anp-oai

> #50166 Upgrade `age` to 0.12.1 and remove the obsolete advisory exception @michaelm-openai

> #50177 Enable writable file streaming in exec-server @anp-oai

> #50183 Add `dots` to issue labeler guidance @etraut-openai

> #50199 Restore the account email in `/status` after account updates @etraut-openai

> #50200 Report the configured TUI mode in `codex doctor` @etraut-openai

> #50207 Release stable Markdown tables into scrollback during streaming @etraut-openai

> #50215 Support Ctrl+Insert for copying TUI selections @etraut-openai

> #50219 Bound tmux option probes to one second @etraut-openai

> #50354 Skip unrelated subtrees during config alias normalization @btraut-openai

> #50359 Render ANSI styles in TUI hook system messages @etraut-openai

> #50360 Remove initial messages from session configuration events @owenlin0

> #50396 Honor pager bindings for transcript page keys @bc-openai

> #50418 Honor Retry-After headers in failed Responses events @anp-oai

> #50433 Allow API-key accounts to use Daybreak in the TUI @etraut-openai

> #50435 Persist additional tool definitions in rollout history @pakrym-oai

> #50442 Preserve native USD amounts in thread usage responses @asohrabi-oai

> #50443 Stabilize paused-time code-mode service tests @seanh-oai

> #50445 Assert that only direct tool calls emit timing events @seanh-oai

> #50446 Bundle rollout attachments into a gzip tar archive @dkovalenko-oai

> #50447 Remove the provider capability gate for tool namespaces @pakrym-oai

> #50454 Measure rollout persistence size reductions @owenlin0

> #50462 Populate thread previews from delegated task inputs @bc-openai

> #50464 Add the `incremental_tools` feature flag @pakrym-oai

> #50467 Copy transcript selections as literal text while preserving rich HTML @fcoury-oai

> #50477 Use the app-server default output cap for TUI workspace commands @etraut-openai

> #50499 Include installer stderr in daemon update failures @etraut-openai

> #50503 Use Enter to accept transcript Find results and Escape to cancel @fcoury-oai

> #50504 Center TUI confirmations over their retained backdrop @bc-openai

> #50510 Require GovCloud guidance acknowledgment after Bedrock setup @jackz100

> #50525 Reject unknown TUI keys in strict config validation @etraut-openai

> #50531 Persist realtime transcript tails before closure without inference @guinness-oai

> #50540 Send incremental tool catalog updates in Responses Lite @pakrym-oai

> #50558 Avoid reading the current directory when resolving absolute paths @etraut-openai

> #50559 Distinguish daemon release identity from executable contents @etraut-openai

> #50562 Keep Code Mode tool discovery guidance stable across catalog changes @aibrahim-oai

> #50687 Keep third-party tools deferred in strict Code Mode Only @aibrahim-oai

> #50695 Preserve local Markdown link labels in the TUI @bc-openai

> #50741 Keep environment-backed tools exposed across readiness changes @won-openai

> #50756 Show unavailable slash commands when searched in side conversations @bc-openai

> #50764 Allow `/archive` while a turn is running @bc-openai

> #50782 Retry Windows daemon release publication on transient file locks @etraut-openai

> #50788 Open slash commands from empty drafts in Vim Normal mode @bc-openai

> #50802 Fall back to mklink when Windows daemon junction updates are denied @etraut-openai

> #50804 Preserve review lifecycle ordering on failure @etraut-openai

> #50808 Prune TUI snapshots and consolidate behavior tests @etraut-openai

> #50940 Recover malformed Windows deny-read ACL state safely @zm-oai

> #50962 Gate stable environment tool exposure behind a feature flag @aibrahim-oai

> #50964 Track inference tool changes in turn analytics @aibrahim-oai

> #50977 Isolate tracing in the strict third-party tool deferral test @alishobeiri-oai

> #51061 Gate Guardian continuation tests on classifier request capture @jif-oai

> #51063 Honor prior cancellation before starting Codex delegates @jif-oai

> #51065 Scope Guardian V2 response timing to snapshot sampling @swastik-oai

> #51119 Clarify incremental tool namespace updates in Responses Lite @akira-oai

> #51126 Add promise settlement streaming helpers to code mode @cconger

> #51133 Allow Guardian Decisions to fall back to `OPENAI_API_KEY` @swastik-oai

> #51137 Recover Guardian reviews from parent checkpoints @felixxia-oai

> #51139 Force fresh Guardian sessions for parent-checkpoint recovery @felixxia-oai

> #51140 Isolate Guardian checkpoint recovery flags per review attempt @felixxia-oai

> #51156 Send base instructions as Responses input messages @pakrym-oai

> #51158 Sign the PowerShell installer in Windows releases @chess-oai

> #51185 Retry transient gRPC code-mode session admission failures @cassirer-openai

> #51186 Prevent stable release pointers from moving backward @andrewgu-oai

> #51188 Record base instructions in incremental tool history @pakrym-oai

> #51191 Clean up Unix app-server control-socket startup lock files @etraut-openai

> #51192 Wait for SIGCONT when resuming the TUI @etraut-openai

> #51193 Test thread archiving before the first turn @btraut-openai

> #51194 Add browser extension request headers to config requirements @jn-openai

> #51198 Allow concurrent release builds while serializing publication @andrewgu-oai

> #51200 Upgrade Bazel to 9.2.0 and refresh the module lockfile @anp-oai

> #51202 Distinguish namespace removals in incremental tool updates @akira-oai

> #51203 Make apply_patch preserve line endings unconditionally @charliemarsh-oai

> #51209 Add ranked tool discovery to JavaScript code mode @zamoshchin-openai

> #51217 Preserve review targets and scope misalignment continuation metadata @yunhan-wei

> #51220 Honor the OTLP metrics temporality preference @daniel-oai

> #51221 Separate environment requests from runtime selections @anp-oai

> #51230 Make session lookup pagination stable and report listing failures @etraut-openai

> #51241 Add a partial answer message phase @rb-oai

> #51253 Enforce Fast and Ultra Fast policies independently @dpatel-oai

> #51257 Fix installer checksum verification under Windows PowerShell @zm-oai

> #51260 Handle partial answers in realtime routing and thread search @rb-oai

> #51330 Measure total Guardian approval decision duration @jif-oai

> #51334 Count Guardian denial-limit interruptions in telemetry @jif-oai

> #51378 Keep Guardian v2 WebSocket pools warm with concurrent replenishment @jif-oai

> #51391 Make URLs in asynchronous question titles clickable @charliemarsh-oai

> #51396 Let late low-risk scores complete pending Guardian reviews @jif-oai

> #51400 Prevent later Guardian scores from releasing earlier pending reviews @jif-oai

> #51411 Suppress repeated image paste presses in legacy terminals @etraut-openai

> #51415 Expose and persist turn lineage across the app server @eddie-openai

> #51419 Preserve turn attribution when queued mail wakes durable sleep @eddie-openai

> #51420 Finish idle thread unloads after slow shutdown @jif-oai

> #51422 Accept environment requests at thread and turn settings boundaries @anp-oai

> #51425 Skip stable installer alias publishing for prereleases @zsol-openai

> #51427 Prevent invalidated wakeups from starting a turn @jif-oai

> #51439 Preserve clickable URLs in TUI approval headers @charliemarsh-oai

> #51440 Honor Retry-After in WebSocket error events @anp-oai

> #51449 Make URLs clickable in TUI user input questions @charliemarsh-oai

> #51451 Make URLs in the TUI warnings viewer clickable @charliemarsh-oai

> #51452 Make banner URLs clickable across wrapped lines @charliemarsh-oai

> #51457 Preserve status usage hyperlinks when the URL wraps @charliemarsh-oai

> #51458 Make URLs clickable in user verification prompts @charliemarsh-oai

> #51460 Retry realtime sideband attachment while an existing call activates @bullman-oai

> #51465 Add an optional JSON transcript format for Guardian @felixxia-oai

> #51466 Keep Guardian transcript records structured through budget recovery @felixxia-oai

> #51467 Keep submission logs useful without exposing payloads @chess-oai

> #51470 Raise the managed app-server file descriptor limit on Unix @etraut-openai

> #51471 Preserve clickable URLs in pending input previews @charliemarsh-oai

> #51473 Preserve URL destinations in wrapped hook details @charliemarsh-oai

> #51482 Use PathUri for skill identity and path matching @anp-oai

> #51483 Add correlated, credential-free rendezvous connection diagnostics @alexi-openai

> #51491 Classify executor capability root ownership independently of parsing @stevenlee-oai

> #51493 Bind capability roots to environment selections @anp-oai

> #51499 Load rollout history on a single blocking worker @charliemarsh-oai

> #51502 Bound relay connection attempts and handle pongs during blocked writes @alexi-openai

> #51510 Preserve live TUI settings when configuration reloads fail @imac-oai

> #51511 Fix Windows 10 drive-letter opens for no-follow filesystem operations @zm-oai

> #51517 Pass thread persistence intent to attachment uploads @kchainani-oai

> #51525 Preserve the CLI MXC preference in executor config reads @zm-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.162.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223 Remove legacy personality template metadata @rhan-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-08-3-reliability-and-performance-changes-in-rust-v0-162-0|3 Reliability and Performance changes in rust-v0.162.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-08-2-voice-and-audio-changes-in-rust-v0-162-0|2 Voice and Audio changes in rust-v0.162.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-08-10-context-window-changes-in-rust-v0-162-0|10 Context Window changes in rust-v0.162.0]] · Context Window
- [[Changes/Codex CLI/2026-10-08-50216-use-the-shared-text-editor-for-command-center-task-renaming-bc-openai|♯50216 Use the shared text editor for command-center task renaming @bc-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0|13 Safety and Privacy changes in rust-v0.162.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-08-20-apps-and-integrations-changes-in-rust-v0-162-0|20 Apps and Integrations changes in rust-v0.162.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-08-50384-allow-opting-into-16-kib-arm64-code-pages-for-macos-signing-chess-oai|♯50384 Allow opting into 16 KiB ARM64 code pages for macOS signing @chess-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-08-8-interface-experience-changes-in-rust-v0-162-0|8 Interface Experience changes in rust-v0.162.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0|12 Developer Workflow changes in rust-v0.162.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-08-14-agent-mode-changes-in-rust-v0-162-0|14 Agent Mode changes in rust-v0.162.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-08-11-model-support-changes-in-rust-v0-162-0|11 Model Support changes in rust-v0.162.0]] · Model Support
- [[Changes/Codex CLI/2026-10-08-2-account-and-access-changes-in-rust-v0-162-0|2 Account and Access changes in rust-v0.162.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-08-2-collaboration-changes-in-rust-v0-162-0|2 Collaboration changes in rust-v0.162.0]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-08-34377d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-08-137-other-changes-in-rust-v0-162-0.md%0ACard%20ID%3A%20codex-cli-2026-10-08-34377d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.162.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->