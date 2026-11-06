---
card_id: codex-cli-2026-10-29-a83cfe
date: '2026-10-29'
description: 'Codex CLI · 2026-10-29 · Other changes: 173 changes in 0.166.0 — Rendered
  Markdown consistently in async questions, choices, answers, and transcript replies…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8a52d8632110a8d99c4a74ba05b4d0c50b709d92cdb5e92bcd421d6b77e9058d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-29-a83cfe
  comparison: ''
  date: '2026-10-29'
  description: 'Codex CLI — 0.166.0: 173 other changes'
  evidence:
  - quote: 'Rendered Markdown consistently in async questions, choices, answers, and
      transcript replies. (#57259, #57292)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: Added `codex queue --resume` to resume unloaded threads after queueing
      a message. (#57232)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: Added `codex doctor --network-only` for focused configuration, connectivity,
      and WebSocket diagnostics. (#57606)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: Preserved local image attachments when restoring killed composer text.
      (#57502)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: Restored spawned descendant threads when unarchiving their parent. (#57635)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: Improved TUI reconnection recovery, including offline `/quit` and `/exit`
      handling. (#57820)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: 'Switched Bazel to source-built V8 with target-matched Rust bindings and
      native Windows MSVC archive support. (#57164, #57269, #57644, #57832)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: Shipped the standalone executor in canonical CLI and app-server release
      packages. (#57837)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: 'Standardized development and release builds on Node.js 24.22.1 and Rust
      1.95.0. (#57168, #57373)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56494 Add channel upserts to message boards @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56505 Defer synchronous Guardian tool-call truncation to preparation
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56515 Add trace instrumentation for turn startup and response streaming
      @bkotsopoulos'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56516 Respect server approval policy defaults during TUI startup @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56524 Add turn, tool, and skill attribution to traces @bkotsopoulos'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56533 Defer sync Guardian tool-output truncation to transcript preparation
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56535 Extract the head-tail buffer into a utility crate @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56552 Initialize SQLite databases with DELETE journaling on NFS @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56554 Enable masked AWS credentials for local proxy signing @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56555 Apply sync Guardian message limits during transcript preparation
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56556 Use conversations for all Guardian v2 async classification @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56557 Exercise retained sampling in Guardian transport tests @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#56560 Allow configuring GCP project and location in provider settings
      @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57164 Move the V8 Bazel build graph into Codex @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57165 Enforce V8 artifact profiles at Bazel target boundaries @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57166 Surface automatic marketplace update failures as startup warnings
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57167 Track CUA tool call starts and deduplicate lifecycle events @trpcic-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57170 Update prebuilt argument-comment-lint to `rust-v0.164.0` @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57172 Expose lifecycle timestamps on app-server thread items @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57176 Defer Guardian Node REPL output truncation until prompt preparation
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57178 Route FedRAMP API keys to government endpoints by default @lsingh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57180 Add constraint-aware standalone network proxy configuration @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57186 Fail closed on unreadable glob search root metadata errors @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57187 Allow advisory rollout budgets with optional limit enforcement
      @nvogt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57191 Read unified exec output directly from stdout and stderr @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57192 Gate capability discovery V2 on executor version @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57193 Preserve failed `write_stdin` calls in rollout trace replay @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57194 Classify rollout tool calls by their runtime handler @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57197 Clarify skill toggle summaries in the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57199 Truncate rollout JSON summaries at UTF-8 character boundaries @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57201 Capture direct-tool critical paths behind a feature flag @taohong339'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57202 Preserve the tool dispatch span across runtime futures @trpcic-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57204 Register the `untrusted_as_tool_output` feature flag @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57206 Ignore the crypto-bigint timing advisory in dependency checks @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57207 Attribute approval waits to tool critical-path timing @taohong339'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57208 Propagate installer download failures in standalone Unix updates
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57209 Report turn critical-path timing in analytics @taohong339'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57212 Enable zstd compression for code-mode gRPC responses @cayoub-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57218 Support negotiated WebSocket compression in the remote app-server
      client @thorvald-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57220 Log app-server WebSocket compression statistics @thorvald-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57225 Add managed enforcement of DELETE journaling on NFS @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57227 Preserve acknowledged permissions when resuming and forking threads
      @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57232 Add optional thread resumption to `codex queue` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57233 Stop dotenv loading on persistent I/O errors @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57234 Prevent credential collisions in registry auth test fixtures @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57241 Honor configured message limits for encrypted guardian transcripts
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57242 Reduce the default thread unload delay to one minute @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57243 Pause Tokio time in startup draft handoff tests @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57245 Stabilize the rejected queue message test @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57247 Release the rollout maintenance lock when its guard is dropped
      @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57251 Show native dollar thread usage for ENT26 plans @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57253 Allow slow daemon startup while detecting early process exits @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57256 Keep parent history out of attached thread views @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57259 Render Markdown in TUI async question choices @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57261 Separate `apply_patch` request preparation from execution @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57262 Add incremental skill catalogs behind `skill_catalog_deltas` @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57265 Show effective processing tiers in TUI status surfaces @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57267 Keep cloud conversation settings server-owned in the TUI @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57268 Record reasons for embedded TUI starts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57269 Add native Windows MSVC V8 source archive builds @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57272 Add code-mode output truncation protocol contracts @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57273 Reject unsupported options for `codex queue` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57276 Support window prefixes for extension world-state sections @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57277 Use the crates.io release of `i18n-config` @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57282 Promote rounded token counts to the next compact unit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57284 Express TUI mouse capture as an explicit policy @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57286 Support `network_proxy` in managed requirements @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57287 Preserve parent tool declarations in prediction forks @keyz'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57291 Represent user message presentation with an enum @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57292 Render async questions and replies with Markdown in the TUI @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57295 Defer synchronous Guardian evidence limits to preparation @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57304 Surface refresh-token rejection errors during workspace routing
      @smurching-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57307 Bump `openai/fence` to `v0.12.2` in the blob size policy @joesavona'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57311 Preserve tool output versions and history order in rollout traces
      @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57314 Format all Rust sources and clean up repository checks @joesavona'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57352 Preserve child signal failures in the npm wrapper @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57353 Avoid object-identity preflight for MXC path grants @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57357 Report when NFS database migration finds no databases @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57358 Serialize session index mutations across processes @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57360 Bound waits for the thread writer coordination lock @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57366 Show the selected ChatGPT workspace in `/status` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57373 Pin the Rust toolchain to 1.95.0 @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57393 Render integral limits and parenthesized matrices in TUI math @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57394 Add experimental GCP account setup to the app server @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57420 Make thread item timestamps optional in TypeScript exports @keyz'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57430 Test goal provenance in existing workers'' Guardian reviews @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57433 Add opt-in synchronous Guardian review for native tool calls @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57438 Carry prepared commands through unified execution @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57439 Preserve Guardian request metadata with custom OpenAI base URLs
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57452 Distinguish policy-restricted capacity failures from server overloads
      @toml-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57458 Move Guardian token usage calculation into the reviewer crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57462 Always put Code Mode tool descriptions before namespace descriptions
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57468 Fix guardian handoff mocks for native history tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57474 Test encrypted native call history across Guardian reviews @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57476 Move Guardian session helpers into the reviewer crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57478 Move Guardian approval request types into the reviewer crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57483 Skip unrelated indexed rollouts during selected thread migration
      @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57488 Move guardian prompt composition into the reviewer crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57493 Move Guardian action JSON formatting into the reviewer crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57500 Add an option to omit descriptions from skill catalogs @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57501 Render escaped percent signs in TUI math @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57502 Preserve local image attachments when restoring killed text @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57506 Move Guardian request mappings into the reviewer crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57509 Extract Guardian planned-action assembly into the reviewer crate
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57512 Explicitly unlock daemon PID reservation probes on Unix @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57513 Replace the npm wrapper with the native binary using `execve` @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57514 Add experimental ChatGPT workspace switching to app-server @dhruvgupta-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57515 Limit MXC volume expansion probes to symbolic links @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57519 Defer synchronous Guardian heartbeat compression to preparation
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57522 Add isolated reviews to the guardian reviewer pool @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57533 Release empty PID probe locks explicitly on Unix @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57538 Preserve host-assigned user input IDs in Responses messages @zbrunson-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57563 Avoid retaining unneeded output items in HTTP response streams
      @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57564 Preserve rich composer content in Vim registers @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57567 Allow catalog URL overrides for the built-in OpenAI provider @jamy-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57569 Preserve process output and control replies under backpressure
      @ztanner-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57573 Add filesystem-free classification of intercepted patch commands
      @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57575 Refactor HTTP client construction and request execution @bz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57584 Preserve output boundaries through token truncation @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57586 Add host-reserved V2 child creation APIs @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57589 Add a standalone `codex-exec-server` executable @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57590 Ship `codex-exec-server` in CLI and app-server packages @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57593 Remove empty local staging routing files @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57597 Preserve WebSocket probe evidence and redact diagnostic details
      @dob-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57598 Cache empty remote skill discovery with filesystem watches @adams-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57606 Add `codex doctor --network-only` for focused network diagnostics
      @dob-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57618 Release sampling prompts after stream setup @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57626 Show Bedrock setup for explicitly configured OpenAI providers @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57628 Stop shipping `codex-exec-server` in release artifacts @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57635 Restore spawned descendants when unarchiving a thread @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57638 Add OpenTelemetry requirement types to the app-server protocol
      @arnavpatidar-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57644 Generate Rust bindings that match Bazel-built V8 archives @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57649 Support managed OpenTelemetry configuration requirements @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57654 Redact OTEL exporter headers in app-server config responses @arnavpatidar-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57657 Fix trace exporter activation after account switches @arnavpatidar-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57658 Support managed OpenTelemetry metadata and PEM client identities
      @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57667 Remove detached delivery from `review/start` @yansenzhou-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57692 Wait for turn profiles before asserting sampling counts in trace
      tests @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57697 Move Guardian review state into the reviewer extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57702 Move Guardian review evidence into the reviewer extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57710 Preserve parent routing affinity for Guardian reviews @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57720 Move `ReviewAction` into the Guardian reviewer crate @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57723 Disable optimization for the on-demand Bazel schema generator @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57729 Remove `free_guardian` configuration from Guardian tests @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57741 Separate test-only Rust sources from Bazel library and binary inputs
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57757 Expose Guardian assessments in response streams @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57774 Skip non-regular files when detecting pasted image paths @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57782 Restrict code-mode host replacement to session admission @aakash-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57783 Exclude unrelated network shares from MXC default reads @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57787 Fix app-server thread listener startup and shutdown races @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57788 Release app-server thread runtimes after shutdown @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57790 Centralize synchronous Guardian prompt preparation @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57796 Extend GitHub release read retries and add jitter @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57817 Detach realtime sideband observers without ending the session @jiahao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57818 Reduce unnecessary work in configuration processing @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57820 Improve TUI reconnect recovery and offline exit handling @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57824 Include directly attached threads in diagnostic uploads @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57825 Update CI setup to use `meta/install-dotslash` @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57832 Build V8 from source by default in Bazel @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57834 Add isolated Guardian assessments for prepared actions @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57835 Limit concurrent image availability checks to eight @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57837 Ship the standalone executor in release packages @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57840 Validate thread providers before resume and input @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  - quote: '#57841 Add optional process metrics sampling for code-mode hosts @aakash-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.166.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 173-other-changes-in-rust-v0-166-0
  source_release: codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a
  source_type: github_releases
  theme: uncategorized
  title: 173 other changes in rust-v0.166.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a]]'
source_type: github_releases
theme: uncategorized
title: 173 other changes in rust-v0.166.0
type: change
---

<!-- chronolog:begin region="header" -->
# 173 other changes in rust-v0.166.0

**Codex CLI** · 2026-10-29 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.166.0) · from [[Releases/Codex CLI/codex-cli-2026-10-29-rust-v0-166-0-github-428320524-44f8c24a|0.166.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Rendered Markdown consistently in async questions, choices, answers, and transcript replies. (#57259, #57292)

> Added `codex queue --resume` to resume unloaded threads after queueing a message. (#57232)

> Added `codex doctor --network-only` for focused configuration, connectivity, and WebSocket diagnostics. (#57606)

> Preserved local image attachments when restoring killed composer text. (#57502)

> Restored spawned descendant threads when unarchiving their parent. (#57635)

> Improved TUI reconnection recovery, including offline `/quit` and `/exit` handling. (#57820)

> Switched Bazel to source-built V8 with target-matched Rust bindings and native Windows MSVC archive support. (#57164, #57269, #57644, #57832)

> Shipped the standalone executor in canonical CLI and app-server release packages. (#57837)

> Standardized development and release builds on Node.js 24.22.1 and Rust 1.95.0. (#57168, #57373)

> #56494 Add channel upserts to message boards @felixxia-oai

> #56505 Defer synchronous Guardian tool-call truncation to preparation @ioanbudea-OAI

> #56515 Add trace instrumentation for turn startup and response streaming @bkotsopoulos

> #56516 Respect server approval policy defaults during TUI startup @etraut-openai

> #56524 Add turn, tool, and skill attribution to traces @bkotsopoulos

> #56533 Defer sync Guardian tool-output truncation to transcript preparation @ioanbudea-OAI

> #56535 Extract the head-tail buffer into a utility crate @seanh-oai

> #56552 Initialize SQLite databases with DELETE journaling on NFS @dkovalenko-oai

> #56554 Enable masked AWS credentials for local proxy signing @viyatb-oai

> #56555 Apply sync Guardian message limits during transcript preparation @ioanbudea-OAI

> #56556 Use conversations for all Guardian v2 async classification @felixxia-oai

> #56557 Exercise retained sampling in Guardian transport tests @felixxia-oai

> #56560 Allow configuring GCP project and location in provider settings @alexsong-oai

> #57164 Move the V8 Bazel build graph into Codex @seanh-oai

> #57165 Enforce V8 artifact profiles at Bazel target boundaries @seanh-oai

> #57166 Surface automatic marketplace update failures as startup warnings @dkovalenko-oai

> #57167 Track CUA tool call starts and deduplicate lifecycle events @trpcic-openai

> #57170 Update prebuilt argument-comment-lint to `rust-v0.164.0` @tamird

> #57172 Expose lifecycle timestamps on app-server thread items @charliemarsh-oai

> #57176 Defer Guardian Node REPL output truncation until prompt preparation @ioanbudea-OAI

> #57178 Route FedRAMP API keys to government endpoints by default @lsingh-oai

> #57180 Add constraint-aware standalone network proxy configuration @viyatb-oai

> #57186 Fail closed on unreadable glob search root metadata errors @viyatb-oai

> #57187 Allow advisory rollout budgets with optional limit enforcement @nvogt-oai

> #57191 Read unified exec output directly from stdout and stderr @anp-oai

> #57192 Gate capability discovery V2 on executor version @TAFOYA-OAI

> #57193 Preserve failed `write_stdin` calls in rollout trace replay @cassirer-openai

> #57194 Classify rollout tool calls by their runtime handler @cassirer-openai

> #57197 Clarify skill toggle summaries in the TUI @fcoury-oai

> #57199 Truncate rollout JSON summaries at UTF-8 character boundaries @cassirer-openai

> #57201 Capture direct-tool critical paths behind a feature flag @taohong339

> #57202 Preserve the tool dispatch span across runtime futures @trpcic-openai

> #57204 Register the `untrusted_as_tool_output` feature flag @akira-oai

> #57206 Ignore the crypto-bigint timing advisory in dependency checks @etraut-openai

> #57207 Attribute approval waits to tool critical-path timing @taohong339

> #57208 Propagate installer download failures in standalone Unix updates @etraut-openai

> #57209 Report turn critical-path timing in analytics @taohong339

> #57212 Enable zstd compression for code-mode gRPC responses @cayoub-oai

> #57218 Support negotiated WebSocket compression in the remote app-server client @thorvald-oai

> #57220 Log app-server WebSocket compression statistics @thorvald-oai

> #57225 Add managed enforcement of DELETE journaling on NFS @dkovalenko-oai

> #57227 Preserve acknowledged permissions when resuming and forking threads @charliemarsh-oai

> #57232 Add optional thread resumption to `codex queue` @etraut-openai

> #57233 Stop dotenv loading on persistent I/O errors @etraut-openai

> #57234 Prevent credential collisions in registry auth test fixtures @jif-oai

> #57241 Honor configured message limits for encrypted guardian transcripts @ioanbudea-OAI

> #57242 Reduce the default thread unload delay to one minute @jif-oai

> #57243 Pause Tokio time in startup draft handoff tests @goodman-oai

> #57245 Stabilize the rejected queue message test @goodman-oai

> #57247 Release the rollout maintenance lock when its guard is dropped @goodman-oai

> #57251 Show native dollar thread usage for ENT26 plans @jif-oai

> #57253 Allow slow daemon startup while detecting early process exits @etraut-openai

> #57256 Keep parent history out of attached thread views @btraut-openai

> #57259 Render Markdown in TUI async question choices @imac-oai

> #57261 Separate `apply_patch` request preparation from execution @swastik-oai

> #57262 Add incremental skill catalogs behind `skill_catalog_deltas` @adaley-openai

> #57265 Show effective processing tiers in TUI status surfaces @etraut-openai

> #57267 Keep cloud conversation settings server-owned in the TUI @bc-openai

> #57268 Record reasons for embedded TUI starts @etraut-openai

> #57269 Add native Windows MSVC V8 source archive builds @seanh-oai

> #57272 Add code-mode output truncation protocol contracts @seanh-oai

> #57273 Reject unsupported options for `codex queue` @etraut-openai

> #57276 Support window prefixes for extension world-state sections @fc-oai

> #57277 Use the crates.io release of `i18n-config` @goodman-oai

> #57282 Promote rounded token counts to the next compact unit @etraut-openai

> #57284 Express TUI mouse capture as an explicit policy @imac-oai

> #57286 Support `network_proxy` in managed requirements @viyatb-oai

> #57287 Preserve parent tool declarations in prediction forks @keyz

> #57291 Represent user message presentation with an enum @imac-oai

> #57292 Render async questions and replies with Markdown in the TUI @imac-oai

> #57295 Defer synchronous Guardian evidence limits to preparation @ioanbudea-OAI

> #57304 Surface refresh-token rejection errors during workspace routing @smurching-oai

> #57307 Bump `openai/fence` to `v0.12.2` in the blob size policy @joesavona

> #57311 Preserve tool output versions and history order in rollout traces @cassirer-openai

> #57314 Format all Rust sources and clean up repository checks @joesavona

> #57352 Preserve child signal failures in the npm wrapper @dkovalenko-oai

> #57353 Avoid object-identity preflight for MXC path grants @iceweasel-oai

> #57357 Report when NFS database migration finds no databases @dkovalenko-oai

> #57358 Serialize session index mutations across processes @dkovalenko-oai

> #57360 Bound waits for the thread writer coordination lock @dkovalenko-oai

> #57366 Show the selected ChatGPT workspace in `/status` @etraut-openai

> #57373 Pin the Rust toolchain to 1.95.0 @TAFOYA-OAI

> #57393 Render integral limits and parenthesized matrices in TUI math @etraut-openai

> #57394 Add experimental GCP account setup to the app server @alexsong-oai

> #57420 Make thread item timestamps optional in TypeScript exports @keyz

> #57430 Test goal provenance in existing workers' Guardian reviews @jif-oai

> #57433 Add opt-in synchronous Guardian review for native tool calls @jif-oai

> #57438 Carry prepared commands through unified execution @swastik-oai

> #57439 Preserve Guardian request metadata with custom OpenAI base URLs @jif-oai

> #57452 Distinguish policy-restricted capacity failures from server overloads @toml-openai

> #57458 Move Guardian token usage calculation into the reviewer crate @jif-oai

> #57462 Always put Code Mode tool descriptions before namespace descriptions @swastik-oai

> #57468 Fix guardian handoff mocks for native history tests @jif-oai

> #57474 Test encrypted native call history across Guardian reviews @jif-oai

> #57476 Move Guardian session helpers into the reviewer crate @jif-oai

> #57478 Move Guardian approval request types into the reviewer crate @jif-oai

> #57483 Skip unrelated indexed rollouts during selected thread migration @charliemarsh-oai

> #57488 Move guardian prompt composition into the reviewer crate @jif-oai

> #57493 Move Guardian action JSON formatting into the reviewer crate @jif-oai

> #57500 Add an option to omit descriptions from skill catalogs @adaley-openai

> #57501 Render escaped percent signs in TUI math @etraut-openai

> #57502 Preserve local image attachments when restoring killed text @etraut-openai

> #57506 Move Guardian request mappings into the reviewer crate @jif-oai

> #57509 Extract Guardian planned-action assembly into the reviewer crate @jif-oai

> #57512 Explicitly unlock daemon PID reservation probes on Unix @jif-oai

> #57513 Replace the npm wrapper with the native binary using `execve` @bolinfest

> #57514 Add experimental ChatGPT workspace switching to app-server @dhruvgupta-oai

> #57515 Limit MXC volume expansion probes to symbolic links @iceweasel-oai

> #57519 Defer synchronous Guardian heartbeat compression to preparation @ioanbudea-OAI

> #57522 Add isolated reviews to the guardian reviewer pool @swastik-oai

> #57533 Release empty PID probe locks explicitly on Unix @jif-oai

> #57538 Preserve host-assigned user input IDs in Responses messages @zbrunson-openai

> #57563 Avoid retaining unneeded output items in HTTP response streams @btraut-openai

> #57564 Preserve rich composer content in Vim registers @bc-openai

> #57567 Allow catalog URL overrides for the built-in OpenAI provider @jamy-OAI

> #57569 Preserve process output and control replies under backpressure @ztanner-oai

> #57573 Add filesystem-free classification of intercepted patch commands @swastik-oai

> #57575 Refactor HTTP client construction and request execution @bz-openai

> #57584 Preserve output boundaries through token truncation @seanh-oai

> #57586 Add host-reserved V2 child creation APIs @rhan-oai

> #57589 Add a standalone `codex-exec-server` executable @dkovalenko-oai

> #57590 Ship `codex-exec-server` in CLI and app-server packages @dkovalenko-oai

> #57593 Remove empty local staging routing files @fcoury-oai

> #57597 Preserve WebSocket probe evidence and redact diagnostic details @dob-oai

> #57598 Cache empty remote skill discovery with filesystem watches @adams-oai

> #57606 Add `codex doctor --network-only` for focused network diagnostics @dob-oai

> #57618 Release sampling prompts after stream setup @btraut-openai

> #57626 Show Bedrock setup for explicitly configured OpenAI providers @alexsong-oai

> #57628 Stop shipping `codex-exec-server` in release artifacts @fcoury-oai

> #57635 Restore spawned descendants when unarchiving a thread @etraut-openai

> #57638 Add OpenTelemetry requirement types to the app-server protocol @arnavpatidar-OAI

> #57644 Generate Rust bindings that match Bazel-built V8 archives @seanh-oai

> #57649 Support managed OpenTelemetry configuration requirements @abhinav-oai

> #57654 Redact OTEL exporter headers in app-server config responses @arnavpatidar-OAI

> #57657 Fix trace exporter activation after account switches @arnavpatidar-OAI

> #57658 Support managed OpenTelemetry metadata and PEM client identities @abhinav-oai

> #57667 Remove detached delivery from `review/start` @yansenzhou-oai

> #57692 Wait for turn profiles before asserting sampling counts in trace tests @ioanbudea-OAI

> #57697 Move Guardian review state into the reviewer extension @jif-oai

> #57702 Move Guardian review evidence into the reviewer extension @jif-oai

> #57710 Preserve parent routing affinity for Guardian reviews @jif-oai

> #57720 Move `ReviewAction` into the Guardian reviewer crate @jif-oai

> #57723 Disable optimization for the on-demand Bazel schema generator @jif-oai

> #57729 Remove `free_guardian` configuration from Guardian tests @ioanbudea-OAI

> #57741 Separate test-only Rust sources from Bazel library and binary inputs @jif-oai

> #57757 Expose Guardian assessments in response streams @jif-oai

> #57774 Skip non-regular files when detecting pasted image paths @etraut-openai

> #57782 Restrict code-mode host replacement to session admission @aakash-oai

> #57783 Exclude unrelated network shares from MXC default reads @iceweasel-oai

> #57787 Fix app-server thread listener startup and shutdown races @charliemarsh-oai

> #57788 Release app-server thread runtimes after shutdown @charliemarsh-oai

> #57790 Centralize synchronous Guardian prompt preparation @ioanbudea-OAI

> #57796 Extend GitHub release read retries and add jitter @imac-oai

> #57817 Detach realtime sideband observers without ending the session @jiahao-oai

> #57818 Reduce unnecessary work in configuration processing @bc-openai

> #57820 Improve TUI reconnect recovery and offline exit handling @etraut-openai

> #57824 Include directly attached threads in diagnostic uploads @btraut-openai

> #57825 Update CI setup to use `meta/install-dotslash` @seanh-oai

> #57832 Build V8 from source by default in Bazel @seanh-oai

> #57834 Add isolated Guardian assessments for prepared actions @swastik-oai

> #57835 Limit concurrent image availability checks to eight @kchainani-oai

> #57837 Ship the standalone executor in release packages @dkovalenko-oai

> #57840 Validate thread providers before resume and input @abhinav-oai

> #57841 Add optional process metrics sampling for code-mode hosts @aakash-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.166.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-29-57503-fix-macos-standalone-release-pruning-etraut-openai|♯57503 Fix macOS standalone release pruning @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-29-3-image-generation-changes-in-rust-v0-166-0|3 Image Generation changes in rust-v0.166.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-29-10-developer-workflow-changes-in-rust-v0-166-0|10 Developer Workflow changes in rust-v0.166.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-29-22-apps-and-integrations-changes-in-rust-v0-166-0|22 Apps and Integrations changes in rust-v0.166.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-29-57342-separate-tui-session-resume-preparation-from-activation-bc-openai|♯57342 Separate TUI session resume preparation from activation @bc-openai]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-10-29-12-interface-experience-changes-in-rust-v0-166-0|12 Interface Experience changes in rust-v0.166.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-29-3-editor-experience-changes-in-rust-v0-166-0|3 Editor Experience changes in rust-v0.166.0]] · Editor Experience
- [[Changes/Codex CLI/2026-10-29-10-model-support-changes-in-rust-v0-166-0|10 Model Support changes in rust-v0.166.0]] · Model Support
- [[Changes/Codex CLI/2026-10-29-57542-add-model-gated-literature-search-to-standalone-web-search-rhan-oai|♯57542 Add model-gated literature search to standalone web search @rhan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-29-10-safety-and-privacy-changes-in-rust-v0-166-0|10 Safety and Privacy changes in rust-v0.166.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-29-57226-allow-nfs-database-migration-with-shared-file-permissions-dkovalenko-oai|♯57226 Allow NFS database migration with shared file permissions @dkovalenko-oai]] · Collaboration
- [[Changes/Codex CLI/2026-10-29-8-account-and-access-changes-in-rust-v0-166-0|8 Account and Access changes in rust-v0.166.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-29-2-memory-and-personalization-changes-in-rust-v0-166-0|2 Memory and Personalization changes in rust-v0.166.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-29-56495-add-paginated-channel-subscription-queries-to-the-local-message-board-feli|♯56495 Add paginated channel subscription queries to the local message board @felixxia-oai]] · Pricing Model
- [[Changes/Codex CLI/2026-10-29-7-agent-mode-changes-in-rust-v0-166-0|7 Agent Mode changes in rust-v0.166.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-29-13-context-window-changes-in-rust-v0-166-0|13 Context Window changes in rust-v0.166.0]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-29-a83cfe&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-29-173-other-changes-in-rust-v0-166-0.md%0ACard%20ID%3A%20codex-cli-2026-10-29-a83cfe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.166.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->