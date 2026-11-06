---
card_id: codex-cli-2026-08-20-46845e
date: '2026-08-20'
description: 'Codex CLI · 2026-08-20 · Other changes: 125 changes in 0.149.0 — Added
  `/cd`, `/pwd`, and `/cwd` commands for managing the working directory in TUI sessions…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c771ebde69acc1287095d1739a0625c2e59eaf2f5ec2e3d98183c0d6c7622ae6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-20-46845e
  comparison: ''
  date: '2026-08-20'
  description: 'Codex CLI — 0.149.0: 125 other changes'
  evidence:
  - quote: Added `/cd`, `/pwd`, and `/cwd` commands for managing the working directory
      in TUI sessions. (#38894)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: Added `codex queue` for sending messages to existing local or remote sessions.
      (#39092)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: Expanded Vim editing with character replacement and more change motions
      such as `cw`, `c$`, and `cc`. (#39661)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: Realtime WebRTC sideband connections now reconnect after unexpected transport
      loss without dropping pending output. (#39257)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: Inactive TUI thread replay buffers are now bounded to prevent excessive
      retained streamed output. (#39081)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: Documented DNS exfiltration risks and trust limitations for secure devcontainers.
      (#39283)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38819 Support metadata staging for reserved thread IDs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38822 Avoid cloning TUI history span content @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38823 Avoid allocating per character when decorating hyperlinks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38827 Add endpoint protection checks to `codex doctor` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38893 Restore thread timestamp maxima independently @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38894 Add working-directory commands to the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38899 Move requirements policy ownership to execpolicy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38918 Improve `codex doctor` network diagnostics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38940 Add experimental app-server project APIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38978 Add a configurable skill catalog token budget @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38987 Include images in Guardian v2 transcripts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38997 Retry transient Guardian sampling failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39001 Ignore stale Guardian tool risk scores @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39005 Disable Guardian V2 for managed automatic reviewers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39007 Wait for Guardian score progress in approval tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39022 Hang soft-break whitespace in the TUI composer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39026 Use simulated time in the long typing test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39028 Cache the test pet spritesheet encoding @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39032 Encapsulate TUI shimmer under the motion module @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39033 Bound legacy resume preview scans @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39034 Dispatch queued messages written by other processes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39035 Add app-server coverage for Guardian V2 approval routing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39036 Allow config reads to join active app-server read batches @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39038 Restore Guardian risk scores across thread lifecycles @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39040 Preserve foreign paths in managed network approvals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39050 Prepare the telemetry shutdown worker during initialization @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39055 Add network policy metadata to environment configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39056 Verify the pinned zsh manifest in release builds @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39057 Rate-limit TUI frames from their actual emission time @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39061 Avoid rerendering streamed code fences @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39063 Render only visible rows in the transcript pager @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39064 Restrict queued-message editing to its dedicated binding @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39073 Propagate caller metadata to rendezvous connections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39077 Build filesystem JSON params only for remote TUI sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39081 Bound TUI thread replay buffers by delta size @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39082 Prompt for project trust in remote TUI workspaces @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39089 Clarify the external contribution policy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39101 Update rmcp to 3.1.2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39113 Surface interactive requests in realtime conversations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39115 Remove the experimental thread config endpoint @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39147 Centralize persisted resume settings lookup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39152 Update PyPI publish action to v1.14.2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39154 Box the TUI future to bound CLI stack usage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39157 Notify clients when Guardian requires strict review @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39165 Prevent marketplace identity spoofing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39174 Skip empty user messages for automatic idle turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39200 Add a symlink-safe reader for sensitive files @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39213 Add a fail-closed Tree-sitter PowerShell lowerer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39214 Prevent custom providers from inheriting ambient auth @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39220 Reconnect Guardian sampling WebSockets after auth changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39224 Add Guardian v2 approval review metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39227 Include node_repl screenshots in Guardian v2 reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39235 Decouple Noise relay streams from JSON-RPC processing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39241 Record Guardian v2 classification metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39246 Give Guardian classifier connections distinct thread identities
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39249 Add exec-server forwarding mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39256 Deduplicate rollout moves when archiving threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39257 Reconnect WebRTC Realtime sideband transports @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39259 Simplify unified exec output snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39261 Stop TUI chats on misalignment policy violations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39262 Prevent ConPTY DLL loading from the current directory @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39264 Improve Guardian v2 risk classification @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39267 Inject Node REPL policy into Guardian review sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39273 Preserve thread names during rollout migration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39277 Declare experimental Amazon Bedrock setup APIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39278 Preserve owner-provided environment configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39284 Report network disconnects during approval @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39285 Show file destinations in TUI change approvals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39287 Report diagnostic upload failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39288 Register the async message feature flag @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39293 Remove app-server''s direct reqwest dependency @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39294 Increase SQLite log sink batching @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39298 Allow overriding Codex package versions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39303 Record Guardian v2 classification token usage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39306 Honor managed config during project discovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39307 Fail closed on Guardian V2 risk scoring errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39315 Evict guardian transcript entries in cacheable chunks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39316 Support Edu Plus and Edu Pro account plans @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39319 Add the async user message tool @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39372 Scope TUI approval requests to their threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39385 Prefer the most recent session when queueing by name @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39402 Remove npm package staging from repo checks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39404 Support FD mounts with older system Bubblewrap versions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39410 Refresh expired AWS credentials for Bedrock @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39452 Remove the feature gate for async user messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39493 Make head-tail buffer capacity const generic @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39494 Test panoramic Guardian transcript image resizing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39496 Use default timeouts in cyber exec policy tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39497 Correct normalized dynamic tool coverage across response modes
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39501 Use a narrow fixture for the unified image resize test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39505 Test text stringify errors in the code mode runtime @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39506 Test code mode notifications without a sync tool call @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39509 Test disabled enhanced Node REPL transcript images separately @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39510 Track built-in control tool calls in analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39514 Use stored item types when materializing turn summaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39515 Use `mem::take` to drain unified exec output buffers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39523 Persist thread section moves before the first turn @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39584 Add a just recipe for assembling Codex packages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39586 Isolate IPC in Bubblewrap sandboxes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39592 Prevent SQLx warnings from feeding back into SQLite logs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39595 Keep marketplace upgrade state out of config @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39597 Separate thread settings from environment configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39601 Keep async user messages on the direct tool surface @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39604 Preserve queued TUI input semantics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39605 Hide approved automatic review warnings in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39608 Harden skill installation against unsafe symlinks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39614 Prevent `apply_patch` from widening write permissions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39616 Validate linked worktrees before inheriting project trust @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39618 Apply composer editing preferences to TUI text prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39620 Stream executor capability and skill file reads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39630 Retire the untrusted approval policy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39635 Show strict review warnings in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39637 Treat `invalid_grant` refresh failures as permanent @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39640 Prompt to unarchive sessions before resuming or forking @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39646 Exercise restricted-token sandboxing in cyber policy tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39649 Resolve bundled Windows helpers through bin junctions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39659 Harden unsandboxed patch filesystem access @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39661 Expand Vim change commands and add character replacement @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39666 Improve no-follow filesystem behavior across platforms @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 125-other-changes-in-rust-v0-149-0
  source_release: codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944
  source_type: github_releases
  theme: uncategorized
  title: 125 other changes in rust-v0.149.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944]]'
source_type: github_releases
theme: uncategorized
title: 125 other changes in rust-v0.149.0
type: change
---

<!-- chronolog:begin region="header" -->
# 125 other changes in rust-v0.149.0

**Codex CLI** · 2026-08-20 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.149.0) · from [[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|0.149.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `/cd`, `/pwd`, and `/cwd` commands for managing the working directory in TUI sessions. (#38894)

> Added `codex queue` for sending messages to existing local or remote sessions. (#39092)

> Expanded Vim editing with character replacement and more change motions such as `cw`, `c$`, and `cc`. (#39661)

> Realtime WebRTC sideband connections now reconnect after unexpected transport loss without dropping pending output. (#39257)

> Inactive TUI thread replay buffers are now bounded to prevent excessive retained streamed output. (#39081)

> Documented DNS exfiltration risks and trust limitations for secure devcontainers. (#39283)

> #38819 Support metadata staging for reserved thread IDs @copyberry

> #38822 Avoid cloning TUI history span content @copyberry

> #38823 Avoid allocating per character when decorating hyperlinks @copyberry

> #38827 Add endpoint protection checks to `codex doctor` @copyberry

> #38893 Restore thread timestamp maxima independently @copyberry

> #38894 Add working-directory commands to the TUI @copyberry

> #38899 Move requirements policy ownership to execpolicy @copyberry

> #38918 Improve `codex doctor` network diagnostics @copyberry

> #38940 Add experimental app-server project APIs @copyberry

> #38978 Add a configurable skill catalog token budget @copyberry

> #38987 Include images in Guardian v2 transcripts @copyberry

> #38997 Retry transient Guardian sampling failures @copyberry

> #39001 Ignore stale Guardian tool risk scores @copyberry

> #39005 Disable Guardian V2 for managed automatic reviewers @copyberry

> #39007 Wait for Guardian score progress in approval tests @copyberry

> #39022 Hang soft-break whitespace in the TUI composer @copyberry

> #39026 Use simulated time in the long typing test @copyberry

> #39028 Cache the test pet spritesheet encoding @copyberry

> #39032 Encapsulate TUI shimmer under the motion module @copyberry

> #39033 Bound legacy resume preview scans @copyberry

> #39034 Dispatch queued messages written by other processes @copyberry

> #39035 Add app-server coverage for Guardian V2 approval routing @copyberry

> #39036 Allow config reads to join active app-server read batches @copyberry

> #39038 Restore Guardian risk scores across thread lifecycles @copyberry

> #39040 Preserve foreign paths in managed network approvals @copyberry

> #39050 Prepare the telemetry shutdown worker during initialization @copyberry

> #39055 Add network policy metadata to environment configuration @copyberry

> #39056 Verify the pinned zsh manifest in release builds @copyberry

> #39057 Rate-limit TUI frames from their actual emission time @copyberry

> #39061 Avoid rerendering streamed code fences @copyberry

> #39063 Render only visible rows in the transcript pager @copyberry

> #39064 Restrict queued-message editing to its dedicated binding @copyberry

> #39073 Propagate caller metadata to rendezvous connections @copyberry

> #39077 Build filesystem JSON params only for remote TUI sessions @copyberry

> #39081 Bound TUI thread replay buffers by delta size @copyberry

> #39082 Prompt for project trust in remote TUI workspaces @copyberry

> #39089 Clarify the external contribution policy @copyberry

> #39101 Update rmcp to 3.1.2 @copyberry

> #39113 Surface interactive requests in realtime conversations @copyberry

> #39115 Remove the experimental thread config endpoint @copyberry

> #39147 Centralize persisted resume settings lookup @copyberry

> #39152 Update PyPI publish action to v1.14.2 @copyberry

> #39154 Box the TUI future to bound CLI stack usage @copyberry

> #39157 Notify clients when Guardian requires strict review @copyberry

> #39165 Prevent marketplace identity spoofing @copyberry

> #39174 Skip empty user messages for automatic idle turns @copyberry

> #39200 Add a symlink-safe reader for sensitive files @copyberry

> #39213 Add a fail-closed Tree-sitter PowerShell lowerer @copyberry

> #39214 Prevent custom providers from inheriting ambient auth @copyberry

> #39220 Reconnect Guardian sampling WebSockets after auth changes @copyberry

> #39224 Add Guardian v2 approval review metrics @copyberry

> #39227 Include node_repl screenshots in Guardian v2 reviews @copyberry

> #39235 Decouple Noise relay streams from JSON-RPC processing @copyberry

> #39241 Record Guardian v2 classification metrics @copyberry

> #39246 Give Guardian classifier connections distinct thread identities @copyberry

> #39249 Add exec-server forwarding mode @copyberry

> #39256 Deduplicate rollout moves when archiving threads @copyberry

> #39257 Reconnect WebRTC Realtime sideband transports @copyberry

> #39259 Simplify unified exec output snapshots @copyberry

> #39261 Stop TUI chats on misalignment policy violations @copyberry

> #39262 Prevent ConPTY DLL loading from the current directory @copyberry

> #39264 Improve Guardian v2 risk classification @copyberry

> #39267 Inject Node REPL policy into Guardian review sessions @copyberry

> #39273 Preserve thread names during rollout migration @copyberry

> #39277 Declare experimental Amazon Bedrock setup APIs @copyberry

> #39278 Preserve owner-provided environment configuration @copyberry

> #39284 Report network disconnects during approval @copyberry

> #39285 Show file destinations in TUI change approvals @copyberry

> #39287 Report diagnostic upload failures @copyberry

> #39288 Register the async message feature flag @copyberry

> #39293 Remove app-server's direct reqwest dependency @copyberry

> #39294 Increase SQLite log sink batching @copyberry

> #39298 Allow overriding Codex package versions @copyberry

> #39303 Record Guardian v2 classification token usage @copyberry

> #39306 Honor managed config during project discovery @copyberry

> #39307 Fail closed on Guardian V2 risk scoring errors @copyberry

> #39315 Evict guardian transcript entries in cacheable chunks @copyberry

> #39316 Support Edu Plus and Edu Pro account plans @copyberry

> #39319 Add the async user message tool @copyberry

> #39372 Scope TUI approval requests to their threads @copyberry

> #39385 Prefer the most recent session when queueing by name @copyberry

> #39402 Remove npm package staging from repo checks @copyberry

> #39404 Support FD mounts with older system Bubblewrap versions @copyberry

> #39410 Refresh expired AWS credentials for Bedrock @copyberry

> #39452 Remove the feature gate for async user messages @copyberry

> #39493 Make head-tail buffer capacity const generic @copyberry

> #39494 Test panoramic Guardian transcript image resizing @copyberry

> #39496 Use default timeouts in cyber exec policy tests @copyberry

> #39497 Correct normalized dynamic tool coverage across response modes @copyberry

> #39501 Use a narrow fixture for the unified image resize test @copyberry

> #39505 Test text stringify errors in the code mode runtime @copyberry

> #39506 Test code mode notifications without a sync tool call @copyberry

> #39509 Test disabled enhanced Node REPL transcript images separately @copyberry

> #39510 Track built-in control tool calls in analytics @copyberry

> #39514 Use stored item types when materializing turn summaries @copyberry

> #39515 Use `mem::take` to drain unified exec output buffers @copyberry

> #39523 Persist thread section moves before the first turn @copyberry

> #39584 Add a just recipe for assembling Codex packages @copyberry

> #39586 Isolate IPC in Bubblewrap sandboxes @copyberry

> #39592 Prevent SQLx warnings from feeding back into SQLite logs @copyberry

> #39595 Keep marketplace upgrade state out of config @copyberry

> #39597 Separate thread settings from environment configuration @copyberry

> #39601 Keep async user messages on the direct tool surface @copyberry

> #39604 Preserve queued TUI input semantics @copyberry

> #39605 Hide approved automatic review warnings in the TUI @copyberry

> #39608 Harden skill installation against unsafe symlinks @copyberry

> #39614 Prevent `apply_patch` from widening write permissions @copyberry

> #39616 Validate linked worktrees before inheriting project trust @copyberry

> #39618 Apply composer editing preferences to TUI text prompts @copyberry

> #39620 Stream executor capability and skill file reads @copyberry

> #39630 Retire the untrusted approval policy @copyberry

> #39635 Show strict review warnings in the TUI @copyberry

> #39637 Treat `invalid_grant` refresh failures as permanent @copyberry

> #39640 Prompt to unarchive sessions before resuming or forking @copyberry

> #39646 Exercise restricted-token sandboxing in cyber policy tests @copyberry

> #39649 Resolve bundled Windows helpers through bin junctions @copyberry

> #39659 Harden unsandboxed patch filesystem access @copyberry

> #39661 Expand Vim change commands and add character replacement @copyberry

> #39666 Improve no-follow filesystem behavior across platforms @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.149.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-20-2-reliability-and-performance-changes-in-rust-v0-149-0|2 Reliability and Performance changes in rust-v0.149.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model Support changes in rust-v0.149.0]] · Model Support
- [[Changes/Codex CLI/2026-08-20-18-developer-workflow-changes-in-rust-v0-149-0|18 Developer Workflow changes in rust-v0.149.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2 Memory and Personalization changes in rust-v0.149.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-20-39045-add-managed-gates-for-in-app-chat-and-dictation-copyberry|♯39045 Add managed gates for in-app chat and dictation @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0|18 Safety and Privacy changes in rust-v0.149.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context Window changes in rust-v0.149.0]] · Context Window
- [[Changes/Codex CLI/2026-08-20-2-collaboration-changes-in-rust-v0-149-0|2 Collaboration changes in rust-v0.149.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-20-5-editor-experience-changes-in-rust-v0-149-0|5 Editor Experience changes in rust-v0.149.0]] · Editor Experience
- [[Changes/Codex CLI/2026-08-20-7-mobile-and-desktop-changes-in-rust-v0-149-0|7 Mobile and Desktop changes in rust-v0.149.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-20-3-interface-experience-changes-in-rust-v0-149-0|3 Interface Experience changes in rust-v0.149.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-20-33-apps-and-integrations-changes-in-rust-v0-149-0|33 Apps and Integrations changes in rust-v0.149.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-20-8-account-and-access-changes-in-rust-v0-149-0|8 Account and Access changes in rust-v0.149.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-20-39072-persist-generated-images-through-turn-executors-copyberry|♯39072 Persist generated images through turn executors @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-20-39283-document-secure-devcontainer-dns-exfiltration-risk-copyberry|♯39283 Document secure devcontainer DNS exfiltration risk @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-20-39006-emit-api-key-turn-cost-telemetry-from-app-server-copyberry|♯39006 Emit API-key turn cost telemetry from app-server @copyberry]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-20-46845e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-20-125-other-changes-in-rust-v0-149-0.md%0ACard%20ID%3A%20codex-cli-2026-08-20-46845e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.149.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->