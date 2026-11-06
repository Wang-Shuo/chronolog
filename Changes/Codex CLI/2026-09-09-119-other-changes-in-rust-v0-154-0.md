---
card_id: codex-cli-2026-09-09-54a0f9
date: '2026-09-09'
description: 'Codex CLI · 2026-09-09 · Other changes: 119 changes in 0.154.0 — Answer
  questions inline while Codex continues working, using suggested choices or custom
  text…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a1150e0e983874d4cdcaf7b9456bf2fde8c2c84cb6d03caa8592eab936469298
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-09-54a0f9
  comparison: ''
  date: '2026-09-09'
  description: 'Codex CLI — 0.154.0: 119 other changes'
  evidence:
  - quote: 'Answer questions inline while Codex continues working, using suggested
      choices or custom text without losing your main draft. (#42891, #42894, #42897)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: 'Vim editing gains `R` replace mode with undo and dot-repeat, plus more
      reliable Escape handling in legacy terminals. (#42194, #42584)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: Resuming a conversation open in another app now shows a read-only transcript
      with a retry option while preserving your draft. (#43253)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42188 Fix punctuation in npm packaging documentation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42194 Add Vim replace mode to the TUI composer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42202 Separate TUI preferences from server configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42207 Retry TUI reconnects while threads are closing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42247 Track history notes thread hint outcomes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42256 Skip Guardian scoring in User approval mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42270 Report the exec-server release version in environment info @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42288 Fetch rules_rs zlib packages from Ubuntu snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42290 Expand Guardian history coverage across resume and rollback @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42298 Preserve retained answers across steer rollbacks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42316 Refactor exec-server startup futures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42318 Support packaged managed Codex binary paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42320 Make the app-server thread unload delay configurable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42325 Render completed assistant messages directly during replay @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42326 Harden Windows control socket rendezvous @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42354 Add free-form asynchronous user messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42356 Initialize questions in buffered replay test messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42358 Extend rate limit reads with usage capabilities @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42366 List managed worktrees for a repository @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42369 Keep SQLite history projection moving past invalid records @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42372 Add Luna Reserve usage fallback to the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42373 Add attributed exec process lifecycle telemetry @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42374 Extract PID startup into a dedicated module @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42377 Make app-server realtime sessions always available @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42378 Route rollout reads through the canonical JSON decoder @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42383 Update rmcp to 3.2.0 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42386 Expose loaded thread environments in app-server responses @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42388 Recover deferred environments after provisioning failure @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42395 Expose the Codex version to commands and turn metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42397 Extract focused TUI logic into submodules @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42399 Preserve restored input after resolved misalignment errors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42403 Expose the last accepted environment ready report @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42408 Harden embedded composer input handling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42410 Allow reviewing and continuing misalignment-paused chats @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42417 Expose managed application network requirements @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42425 Discover TUI experimental features from the server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42451 Acknowledge pending TUI steers by submission ID @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42458 Expose thread originators through the app-server API @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42584 Recover Vim escape input in legacy terminals @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42602 Deprecate detached review delivery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42603 Expose global metrics installation in `codex-otel` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42606 Support trusted headers for remote exec WebSockets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42609 Condense TUI startup warnings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42623 Bound Noise handshakes by the exec server initialization timeout
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42624 Centralize prompt image detail modes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42634 Add an injectable attachment store to ThreadManager @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42640 Harden TUI parsing of assistant markup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42650 Render assistant file citations as local links @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42652 Add managed worktrees to `codex exec` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42654 Update the stable exec-server test to Codex 0.153.1 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42667 Tailor TUI cyber refusal notices to Daybreak eligibility @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42671 Preserve TUI sessions while starting replacement threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42674 Persist server-advertised experimental features from the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42677 Narrow async user message guidance @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42682 Fix the worktrees experimental feature test fixture @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42718 Gate unified exec TTY support behind a feature flag @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42741 Make the TUI symlink startup test Bazel-compatible @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42749 Improve automatic thread naming in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42758 Propagate response tickets to Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42767 Avoid port races in streamable HTTP tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42773 Avoid holding metadata permit during cold resume config load @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42781 Add direct SigV4 transport to exec-server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42791 Keep TUI prompt history tied to local settings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42792 Extract the note input view into its own module @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42798 Add data-use disclosures to the user report dialog @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42807 Add request-scoped Guardian approval decisions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42814 Support custom report event titles @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42819 Route Guardian approvals independently of async scoring @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42821 Report managed filesystem policy in `codex doctor` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42823 Expose managed WebMCP policy through the app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42838 Preserve executor paths in Guardian approval reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42842 Add Astra sparkle effects to the TUI composer @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42847 Preserve Markdown formatting when copying TUI responses @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42850 Use jemalloc for Linux musl binaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42854 Persist Daybreak preferences in thread metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42863 Preserve precedence across feature requirement aliases @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42883 Add client-side exec-server RPC attempt metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42889 Add TUI building blocks for inline async question editing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42891 Integrate asynchronous questions into the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42894 Support selectable answers for asynchronous TUI questions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42897 Add inline Other answers to async question choices @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#42933 Wait for turn analytics before shutting down the Guardian v2 test
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43002 Replace Guardian tickets with parent response IDs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43005 Add Guardian V2 failure reasons and connection timing metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43039 Refresh live thread tools through `app/installed` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43055 Allow `/copy` to copy status output and individual fields @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43069 Support managed worktrees for interactive sessions and forks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43070 Clarify comments in CI setup and the Rust workflow @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43097 Add a helper-backed realtime WebRTC session API @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43126 Expose native Windows build tools through Bazel targets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43178 Allow guarded legacy resume with background migration enabled @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43253 Show read-only conversations when resume encounters an active writer
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43261 Use server defaults when starting TUI background tasks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43265 Add experimental user verification API contracts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43279 Include linked worktrees in TUI session discovery @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43281 Move npm package staging into a separate release workflow job @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43282 Make Bazel binary stamping opt-in @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43315 Resolve session labels uniquely before acting on them @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43325 Sort JSON schema object keys for consistent Cargo and Bazel output
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43330 Preserve saved permissions when resuming or forking remote tasks
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43360 Use app-server metadata for TUI session restoration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43408 Avoid WebSocket connection waits in Guardian v2 classification
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43419 Initialize `cwd` in TUI resume and fork test fixtures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43421 Remove the app-server README and its contributor guidance references
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43426 Handle Luna HTTP requests in guardian history tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43432 Route approvals through the extension decision API @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43442 Keep Guardian review evidence consistent and reject stale approvals
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43444 Pin V8 release manifests and prevent published release replacement
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43462 Remove legacy Guardian approval review paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43472 Recover missing Guardian root instructions in acceptance order
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43478 Retain inherited Guardian instructions in standalone forks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43494 Limit archive rollout reads to requested threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43495 Allow internal sessions to fork from selected history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43504 Treat zombie processes as inactive in the Unix PID backend @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43513 Expose a stable executor build identity in environment metadata
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  - quote: '#43519 Set `recursion_limit` to 256 for app-server, exec, and TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.154.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 119-other-changes-in-rust-v0-154-0
  source_release: codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1
  source_type: github_releases
  theme: uncategorized
  title: 119 other changes in rust-v0.154.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1]]'
source_type: github_releases
theme: uncategorized
title: 119 other changes in rust-v0.154.0
type: change
---

<!-- chronolog:begin region="header" -->
# 119 other changes in rust-v0.154.0

**Codex CLI** · 2026-09-09 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.154.0) · from [[Releases/Codex CLI/codex-cli-2026-09-09-rust-v0-154-0-github-385887902-ee241ff1|0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Answer questions inline while Codex continues working, using suggested choices or custom text without losing your main draft. (#42891, #42894, #42897)

> Vim editing gains `R` replace mode with undo and dot-repeat, plus more reliable Escape handling in legacy terminals. (#42194, #42584)

> Resuming a conversation open in another app now shows a read-only transcript with a retry option while preserving your draft. (#43253)

> #42188 Fix punctuation in npm packaging documentation @copyberry

> #42194 Add Vim replace mode to the TUI composer @copyberry

> #42202 Separate TUI preferences from server configuration @copyberry

> #42207 Retry TUI reconnects while threads are closing @copyberry

> #42247 Track history notes thread hint outcomes @copyberry

> #42256 Skip Guardian scoring in User approval mode @copyberry

> #42270 Report the exec-server release version in environment info @copyberry

> #42288 Fetch rules_rs zlib packages from Ubuntu snapshots @copyberry

> #42290 Expand Guardian history coverage across resume and rollback @copyberry

> #42298 Preserve retained answers across steer rollbacks @copyberry

> #42316 Refactor exec-server startup futures @copyberry

> #42318 Support packaged managed Codex binary paths @copyberry

> #42320 Make the app-server thread unload delay configurable @copyberry

> #42325 Render completed assistant messages directly during replay @copyberry

> #42326 Harden Windows control socket rendezvous @copyberry

> #42354 Add free-form asynchronous user messages @copyberry

> #42356 Initialize questions in buffered replay test messages @copyberry

> #42358 Extend rate limit reads with usage capabilities @copyberry

> #42366 List managed worktrees for a repository @copyberry

> #42369 Keep SQLite history projection moving past invalid records @copyberry

> #42372 Add Luna Reserve usage fallback to the TUI @copyberry

> #42373 Add attributed exec process lifecycle telemetry @copyberry

> #42374 Extract PID startup into a dedicated module @copyberry

> #42377 Make app-server realtime sessions always available @copyberry

> #42378 Route rollout reads through the canonical JSON decoder @copyberry

> #42383 Update rmcp to 3.2.0 @copyberry

> #42386 Expose loaded thread environments in app-server responses @copyberry

> #42388 Recover deferred environments after provisioning failure @copyberry

> #42395 Expose the Codex version to commands and turn metadata @copyberry

> #42397 Extract focused TUI logic into submodules @copyberry

> #42399 Preserve restored input after resolved misalignment errors @copyberry

> #42403 Expose the last accepted environment ready report @copyberry

> #42408 Harden embedded composer input handling @copyberry

> #42410 Allow reviewing and continuing misalignment-paused chats @copyberry

> #42417 Expose managed application network requirements @copyberry

> #42425 Discover TUI experimental features from the server @copyberry

> #42451 Acknowledge pending TUI steers by submission ID @copyberry

> #42458 Expose thread originators through the app-server API @copyberry

> #42584 Recover Vim escape input in legacy terminals @copyberry

> #42602 Deprecate detached review delivery @copyberry

> #42603 Expose global metrics installation in `codex-otel` @copyberry

> #42606 Support trusted headers for remote exec WebSockets @copyberry

> #42609 Condense TUI startup warnings @copyberry

> #42623 Bound Noise handshakes by the exec server initialization timeout @copyberry

> #42624 Centralize prompt image detail modes @copyberry

> #42634 Add an injectable attachment store to ThreadManager @copyberry

> #42640 Harden TUI parsing of assistant markup @copyberry

> #42650 Render assistant file citations as local links @copyberry

> #42652 Add managed worktrees to `codex exec` @copyberry

> #42654 Update the stable exec-server test to Codex 0.153.1 @copyberry

> #42667 Tailor TUI cyber refusal notices to Daybreak eligibility @copyberry

> #42671 Preserve TUI sessions while starting replacement threads @copyberry

> #42674 Persist server-advertised experimental features from the TUI @copyberry

> #42677 Narrow async user message guidance @copyberry

> #42682 Fix the worktrees experimental feature test fixture @copyberry

> #42718 Gate unified exec TTY support behind a feature flag @copyberry

> #42741 Make the TUI symlink startup test Bazel-compatible @copyberry

> #42749 Improve automatic thread naming in the TUI @copyberry

> #42758 Propagate response tickets to Guardian reviews @copyberry

> #42767 Avoid port races in streamable HTTP tests @copyberry

> #42773 Avoid holding metadata permit during cold resume config load @copyberry

> #42781 Add direct SigV4 transport to exec-server @copyberry

> #42791 Keep TUI prompt history tied to local settings @copyberry

> #42792 Extract the note input view into its own module @copyberry

> #42798 Add data-use disclosures to the user report dialog @copyberry

> #42807 Add request-scoped Guardian approval decisions @copyberry

> #42814 Support custom report event titles @copyberry

> #42819 Route Guardian approvals independently of async scoring @copyberry

> #42821 Report managed filesystem policy in `codex doctor` @copyberry

> #42823 Expose managed WebMCP policy through the app server @copyberry

> #42838 Preserve executor paths in Guardian approval reviews @copyberry

> #42842 Add Astra sparkle effects to the TUI composer @copyberry

> #42847 Preserve Markdown formatting when copying TUI responses @copyberry

> #42850 Use jemalloc for Linux musl binaries @copyberry

> #42854 Persist Daybreak preferences in thread metadata @copyberry

> #42863 Preserve precedence across feature requirement aliases @copyberry

> #42883 Add client-side exec-server RPC attempt metrics @copyberry

> #42889 Add TUI building blocks for inline async question editing @copyberry

> #42891 Integrate asynchronous questions into the TUI @copyberry

> #42894 Support selectable answers for asynchronous TUI questions @copyberry

> #42897 Add inline Other answers to async question choices @copyberry

> #42933 Wait for turn analytics before shutting down the Guardian v2 test @copyberry

> #43002 Replace Guardian tickets with parent response IDs @copyberry

> #43005 Add Guardian V2 failure reasons and connection timing metrics @copyberry

> #43039 Refresh live thread tools through `app/installed` @copyberry

> #43055 Allow `/copy` to copy status output and individual fields @copyberry

> #43069 Support managed worktrees for interactive sessions and forks @copyberry

> #43070 Clarify comments in CI setup and the Rust workflow @copyberry

> #43097 Add a helper-backed realtime WebRTC session API @copyberry

> #43126 Expose native Windows build tools through Bazel targets @copyberry

> #43178 Allow guarded legacy resume with background migration enabled @copyberry

> #43253 Show read-only conversations when resume encounters an active writer @copyberry

> #43261 Use server defaults when starting TUI background tasks @copyberry

> #43265 Add experimental user verification API contracts @copyberry

> #43279 Include linked worktrees in TUI session discovery @copyberry

> #43281 Move npm package staging into a separate release workflow job @copyberry

> #43282 Make Bazel binary stamping opt-in @copyberry

> #43315 Resolve session labels uniquely before acting on them @copyberry

> #43325 Sort JSON schema object keys for consistent Cargo and Bazel output @copyberry

> #43330 Preserve saved permissions when resuming or forking remote tasks @copyberry

> #43360 Use app-server metadata for TUI session restoration @copyberry

> #43408 Avoid WebSocket connection waits in Guardian v2 classification @copyberry

> #43419 Initialize `cwd` in TUI resume and fork test fixtures @copyberry

> #43421 Remove the app-server README and its contributor guidance references @copyberry

> #43426 Handle Luna HTTP requests in guardian history tests @copyberry

> #43432 Route approvals through the extension decision API @copyberry

> #43442 Keep Guardian review evidence consistent and reject stale approvals @copyberry

> #43444 Pin V8 release manifests and prevent published release replacement @copyberry

> #43462 Remove legacy Guardian approval review paths @copyberry

> #43472 Recover missing Guardian root instructions in acceptance order @copyberry

> #43478 Retain inherited Guardian instructions in standalone forks @copyberry

> #43494 Limit archive rollout reads to requested threads @copyberry

> #43495 Allow internal sessions to fork from selected history @copyberry

> #43504 Treat zombie processes as inactive in the Unix PID backend @copyberry

> #43513 Expose a stable executor build identity in environment metadata @copyberry

> #43519 Set `recursion_limit` to 256 for app-server, exec, and TUI @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.154.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-09-21-model-support-changes-in-rust-v0-154-0|21 Model Support changes in rust-v0.154.0]] · Model Support
- [[Changes/Codex CLI/2026-09-09-5-account-and-access-changes-in-rust-v0-154-0|5 Account and Access changes in rust-v0.154.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-09-19-apps-and-integrations-changes-in-rust-v0-154-0|19 Apps and Integrations changes in rust-v0.154.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-09-4-interface-experience-changes-in-rust-v0-154-0|4 Interface Experience changes in rust-v0.154.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-09-17-context-window-changes-in-rust-v0-154-0|17 Context Window changes in rust-v0.154.0]] · Context Window
- [[Changes/Codex CLI/2026-09-09-6-mobile-and-desktop-changes-in-rust-v0-154-0|6 Mobile and Desktop changes in rust-v0.154.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-09-25-safety-and-privacy-changes-in-rust-v0-154-0|25 Safety and Privacy changes in rust-v0.154.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-09-gpt-6-astra-is-now-available-in-the-model-picker-and-amazon-bedrock-catalogs-428|GPT-6-Astra is now available in the model picker and Amazon Bedrock catalogs]] · Model Support
- [[Changes/Codex CLI/2026-09-09-20-voice-and-audio-changes-in-rust-v0-154-0|20 Voice and Audio changes in rust-v0.154.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2 Memory and Personalization changes in rust-v0.154.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-09-experimental-worktree-support-lets-you-create-isolated-checkouts-for-new-or-fork|Experimental worktree support lets you create isolated checkouts for new or forked…]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-09-42746-handle-pending-network-reviews-after-process-completion-copyberry|♯42746 Handle pending network reviews after process completion @copyberry]] · Editor Experience
- [[Changes/Codex CLI/2026-09-09-6-agent-mode-changes-in-rust-v0-154-0|6 Agent Mode changes in rust-v0.154.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-09-42306-stabilize-the-detached-exec-server-session-resume-test-copyberry|♯42306 Stabilize the detached exec-server session resume test @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-09-09-6-collaboration-changes-in-rust-v0-154-0|6 Collaboration changes in rust-v0.154.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-09-7-developer-workflow-changes-in-rust-v0-154-0|7 Developer Workflow changes in rust-v0.154.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-09-54a0f9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-09-119-other-changes-in-rust-v0-154-0.md%0ACard%20ID%3A%20codex-cli-2026-09-09-54a0f9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.154.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->