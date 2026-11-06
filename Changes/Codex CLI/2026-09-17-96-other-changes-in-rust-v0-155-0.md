---
card_id: codex-cli-2026-09-17-545a49
date: '2026-09-17'
description: 'Codex CLI · 2026-09-17 · Other changes: 96 changes in 0.155.0 — Added
  configurable daemon update schedules and `codex app-server daemon update`; saved
  threads…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 300cb1c183afaf65a920622848479831f69bf6a093ea173134b469813c42c2e9
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-17-545a49
  comparison: ''
  date: '2026-09-17'
  description: 'Codex CLI — 0.155.0: 96 other changes'
  evidence:
  - quote: 'Added configurable daemon update schedules and `codex app-server daemon
      update`; saved threads and active goals can recover after daemon restarts. (#43542,
      #43562, #44314)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: 'Automatic approval reviews now preserve complete actions and authorization
      evidence more reliably, retry transient failures, and distinguish review failures
      from unsafe-action findings. (#44482, #44569, #44570)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43521 Preserve standalone release pins during daemon updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43527 Discount an approval''s own code-mode wrapper from Guardian score
      lag @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43529 Ensure the standalone updater runs on managed daemon starts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43533 Fix jemalloc tools and compiler flags for Bazel musl builds @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43542 Make app-server daemon automatic updates configurable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43547 Add user-verification provider abstractions and RPC adapters @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43552 Record the launched app-server executable identity in PID files
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43568 Wire app-server user verification RPCs to the native provider @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43570 Manage synchronous Guardian reviewers through the thread manager
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43572 Make the managed app-server shutdown grace period configurable
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43576 Group adjacent computer actions in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43584 Remove a stale transcript field assignment from the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43603 Recover missed tmux resize notifications in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43619 Add a stable TUI/app-server version comparison helper @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43622 Warn when the connected Codex service is older than the CLI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43698 Make older app-server notices configurable in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43702 Add a TUI user verification prompt component @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43708 Add TUI request bookkeeping for user verification @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43715 Enable user verification for the bundled TUI on supported devices
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43790 Limit app-server storage metrics to session directories @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43798 Batch non-user history eviction to preserve Guardian transcript
      deltas @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43842 Wait for parent idle before rollback in guardian fork tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43848 Preserve runtime workspace roots across thread resume @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43873 Handle undefined values before JSON serialization in code mode
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43884 Close active network proxy connections on teardown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43889 Fix transcript viewer restoration and half-page scrolling @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43894 Preserve thread identity in code-mode tool dispatch traces @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43895 Preserve `__oailb` routing cookies in ChatGPT HTTP clients @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43903 Extract Windows deny-read glob scan planning into protocol @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43915 Remove the repository devcontainer configurations @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43918 Expose the queued event count on `CodexThread` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43925 Add cancellation for native user-verification RPCs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43927 Rename thread artifacts to attachments in the state database @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43943 Gate new turn submissions on host shutdown admission @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43948 Show configured app-server updater settings in doctor @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43949 Add transactional thread attachment mutations to the state runtime
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43950 Keep app-server thread RPCs active until delegated work completes
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43956 Increase the TUI thread capability test stack to 12 MiB @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43959 Gate new app-server work during graceful shutdown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43961 Use curly apostrophes in protocol error messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43966 Heap-allocate the resume future in the legacy history test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#43994 Clear stale transcript history when switching threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44002 Encapsulate executed tool call metadata recording @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44028 Add AWS credential export commands for Amazon Bedrock @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44043 Use `StartThreadOptions` across thread fork APIs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44049 Extract credential broker environment and registry helpers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44056 Add configurable credential providers to the network proxy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44060 Raise Guardian''s action review limit to 200,000 bytes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44066 Extend configured credential brokerage to embedded aliases @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44067 Publish Python packages after stable CLI releases @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44068 Preserve credential broker destinations across environment filtering
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44077 Refactor credential-broker tunnel protocol detection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44089 Support credential brokering in plaintext HTTP tunnels @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44138 Coordinate rollout compression with active thread writers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44175 Attach compressed rollouts to diagnostic reports as JSONL @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44176 Reduce TUI stack usage during session transitions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44183 Release persistent writers when session startup is cancelled @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44207 Measure total exec-server request duration including queueing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44226 Continue rollout searches when a compressed rollout cannot be searched
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44227 Extract Guardian review policy into a dedicated crate @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44241 Handle credential provider source remapping across config layers
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44242 Use captured step settings for tool planning and execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44248 Preserve tool output truncation budgets across resume and fork
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44252 Move synchronous Guardian orchestration into the reviewer extension
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44281 Enforce complete request budgets for Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44283 Persist loaded threads before managed daemon shutdown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44284 Add telemetry for the Windows system config namespace @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44289 Expand MXC volume grants and resolve deny globs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44290 Allow user-requested goal pauses through `update_goal` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44293 Enforce the async Guardian classifier''s complete input budget
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44299 Record thread recovery candidates on managed daemon shutdown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44314 Restore saved threads when the managed daemon restarts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44320 Block goals after three empty automatic continuation turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44325 Return the prompt hash in upload responses @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44328 Clear pending TUI questions when accepting a new prompt @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44330 Add paginated thread attachment listing to the state runtime @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44336 Add bounded tool-result metadata support to executed tool calls
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44350 Add thread attachment operations with coordinated deletion @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44352 Remove path-bearing fields from Guardian review analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44377 Update the forked-thread hook test to use `StartThreadOptions`
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44472 Harden Code Mode tool-call completeness tracking @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44482 Improve Guardian retries and review failure reporting @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44489 Reset cached WebSocket state when auth ownership changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44492 Distinguish HTTP quota errors from rate limits @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44523 Bound app-server stdio shutdown and handle Unix SIGTERM gracefully
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44536 Move Guardian reviewer settings and execution into the reviewer
      crate @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44544 Move Guardian reporting and denial accounting into the extension
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44564 Add app-server APIs for stored thread attachments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44569 Preserve complete actions in Guardian approval reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44570 Preserve Guardian authorization evidence until request budgeting
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44574 Use captured action settings for Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44575 Tie network approval reviews to their originating execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44580 Support symbolic `:root` filesystem policies in MXC @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  - quote: '#44586 Remove `repo_url` from skill invocation analytics events @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.155.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 96-other-changes-in-rust-v0-155-0
  source_release: codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512
  source_type: github_releases
  theme: uncategorized
  title: 96 other changes in rust-v0.155.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512]]'
source_type: github_releases
theme: uncategorized
title: 96 other changes in rust-v0.155.0
type: change
---

<!-- chronolog:begin region="header" -->
# 96 other changes in rust-v0.155.0

**Codex CLI** · 2026-09-17 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.155.0) · from [[Releases/Codex CLI/codex-cli-2026-09-17-rust-v0-155-0-github-391114314-ca085512|0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added configurable daemon update schedules and `codex app-server daemon update`; saved threads and active goals can recover after daemon restarts. (#43542, #43562, #44314)

> Automatic approval reviews now preserve complete actions and authorization evidence more reliably, retry transient failures, and distinguish review failures from unsafe-action findings. (#44482, #44569, #44570)

> #43521 Preserve standalone release pins during daemon updates @copyberry

> #43527 Discount an approval's own code-mode wrapper from Guardian score lag @copyberry

> #43529 Ensure the standalone updater runs on managed daemon starts @copyberry

> #43533 Fix jemalloc tools and compiler flags for Bazel musl builds @copyberry

> #43542 Make app-server daemon automatic updates configurable @copyberry

> #43547 Add user-verification provider abstractions and RPC adapters @copyberry

> #43552 Record the launched app-server executable identity in PID files @copyberry

> #43568 Wire app-server user verification RPCs to the native provider @copyberry

> #43570 Manage synchronous Guardian reviewers through the thread manager @copyberry

> #43572 Make the managed app-server shutdown grace period configurable @copyberry

> #43576 Group adjacent computer actions in the TUI @copyberry

> #43584 Remove a stale transcript field assignment from the TUI @copyberry

> #43603 Recover missed tmux resize notifications in the TUI @copyberry

> #43619 Add a stable TUI/app-server version comparison helper @copyberry

> #43622 Warn when the connected Codex service is older than the CLI @copyberry

> #43698 Make older app-server notices configurable in the TUI @copyberry

> #43702 Add a TUI user verification prompt component @copyberry

> #43708 Add TUI request bookkeeping for user verification @copyberry

> #43715 Enable user verification for the bundled TUI on supported devices @copyberry

> #43790 Limit app-server storage metrics to session directories @copyberry

> #43798 Batch non-user history eviction to preserve Guardian transcript deltas @copyberry

> #43842 Wait for parent idle before rollback in guardian fork tests @copyberry

> #43848 Preserve runtime workspace roots across thread resume @copyberry

> #43873 Handle undefined values before JSON serialization in code mode @copyberry

> #43884 Close active network proxy connections on teardown @copyberry

> #43889 Fix transcript viewer restoration and half-page scrolling @copyberry

> #43894 Preserve thread identity in code-mode tool dispatch traces @copyberry

> #43895 Preserve `__oailb` routing cookies in ChatGPT HTTP clients @copyberry

> #43903 Extract Windows deny-read glob scan planning into protocol @copyberry

> #43915 Remove the repository devcontainer configurations @copyberry

> #43918 Expose the queued event count on `CodexThread` @copyberry

> #43925 Add cancellation for native user-verification RPCs @copyberry

> #43927 Rename thread artifacts to attachments in the state database @copyberry

> #43943 Gate new turn submissions on host shutdown admission @copyberry

> #43948 Show configured app-server updater settings in doctor @copyberry

> #43949 Add transactional thread attachment mutations to the state runtime @copyberry

> #43950 Keep app-server thread RPCs active until delegated work completes @copyberry

> #43956 Increase the TUI thread capability test stack to 12 MiB @copyberry

> #43959 Gate new app-server work during graceful shutdown @copyberry

> #43961 Use curly apostrophes in protocol error messages @copyberry

> #43966 Heap-allocate the resume future in the legacy history test @copyberry

> #43994 Clear stale transcript history when switching threads @copyberry

> #44002 Encapsulate executed tool call metadata recording @copyberry

> #44028 Add AWS credential export commands for Amazon Bedrock @copyberry

> #44043 Use `StartThreadOptions` across thread fork APIs @copyberry

> #44049 Extract credential broker environment and registry helpers @copyberry

> #44056 Add configurable credential providers to the network proxy @copyberry

> #44060 Raise Guardian's action review limit to 200,000 bytes @copyberry

> #44066 Extend configured credential brokerage to embedded aliases @copyberry

> #44067 Publish Python packages after stable CLI releases @copyberry

> #44068 Preserve credential broker destinations across environment filtering @copyberry

> #44077 Refactor credential-broker tunnel protocol detection @copyberry

> #44089 Support credential brokering in plaintext HTTP tunnels @copyberry

> #44138 Coordinate rollout compression with active thread writers @copyberry

> #44175 Attach compressed rollouts to diagnostic reports as JSONL @copyberry

> #44176 Reduce TUI stack usage during session transitions @copyberry

> #44183 Release persistent writers when session startup is cancelled @copyberry

> #44207 Measure total exec-server request duration including queueing @copyberry

> #44226 Continue rollout searches when a compressed rollout cannot be searched @copyberry

> #44227 Extract Guardian review policy into a dedicated crate @copyberry

> #44241 Handle credential provider source remapping across config layers @copyberry

> #44242 Use captured step settings for tool planning and execution @copyberry

> #44248 Preserve tool output truncation budgets across resume and fork @copyberry

> #44252 Move synchronous Guardian orchestration into the reviewer extension @copyberry

> #44281 Enforce complete request budgets for Guardian reviews @copyberry

> #44283 Persist loaded threads before managed daemon shutdown @copyberry

> #44284 Add telemetry for the Windows system config namespace @copyberry

> #44289 Expand MXC volume grants and resolve deny globs @copyberry

> #44290 Allow user-requested goal pauses through `update_goal` @copyberry

> #44293 Enforce the async Guardian classifier's complete input budget @copyberry

> #44299 Record thread recovery candidates on managed daemon shutdown @copyberry

> #44314 Restore saved threads when the managed daemon restarts @copyberry

> #44320 Block goals after three empty automatic continuation turns @copyberry

> #44325 Return the prompt hash in upload responses @copyberry

> #44328 Clear pending TUI questions when accepting a new prompt @copyberry

> #44330 Add paginated thread attachment listing to the state runtime @copyberry

> #44336 Add bounded tool-result metadata support to executed tool calls @copyberry

> #44350 Add thread attachment operations with coordinated deletion @copyberry

> #44352 Remove path-bearing fields from Guardian review analytics @copyberry

> #44377 Update the forked-thread hook test to use `StartThreadOptions` @copyberry

> #44472 Harden Code Mode tool-call completeness tracking @copyberry

> #44482 Improve Guardian retries and review failure reporting @copyberry

> #44489 Reset cached WebSocket state when auth ownership changes @copyberry

> #44492 Distinguish HTTP quota errors from rate limits @copyberry

> #44523 Bound app-server stdio shutdown and handle Unix SIGTERM gracefully @copyberry

> #44536 Move Guardian reviewer settings and execution into the reviewer crate @copyberry

> #44544 Move Guardian reporting and denial accounting into the extension @copyberry

> #44564 Add app-server APIs for stored thread attachments @copyberry

> #44569 Preserve complete actions in Guardian approval reviews @copyberry

> #44570 Preserve Guardian authorization evidence until request budgeting @copyberry

> #44574 Use captured action settings for Guardian reviews @copyberry

> #44575 Tie network approval reviews to their originating execution @copyberry

> #44580 Support symbolic `:root` filesystem policies in MXC @copyberry

> #44586 Remove `repo_url` from skill invocation analytics events @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.155.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-17-43953-preserve-per-image-generation-ids-in-image-generation-analytics-copyberry|♯43953 Preserve per-image generation IDs in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7 Memory and Personalization changes in rust-v0.155.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-17-43846-include-completed-commentary-in-the-copy-picker-copyberry|♯43846 Include completed commentary in the /copy picker @copyberry]] · Interface Experience
- [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]] · Model Support
- [[Changes/Codex CLI/2026-09-17-2-editor-experience-changes-in-rust-v0-155-0|2 Editor Experience changes in rust-v0.155.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-17-15-developer-workflow-changes-in-rust-v0-155-0|15 Developer Workflow changes in rust-v0.155.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-17-20-voice-and-audio-changes-in-rust-v0-155-0|20 Voice and Audio changes in rust-v0.155.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-17-2-mobile-and-desktop-changes-in-rust-v0-155-0|2 Mobile and Desktop changes in rust-v0.155.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]] · Context Window
- [[Changes/Codex CLI/2026-09-17-44354-extract-shared-footer-hint-wrapping-in-the-tui-copyberry|♯44354 Extract shared footer hint wrapping in the TUI @copyberry]] · Collaboration
- [[Changes/Codex CLI/2026-09-17-9-agent-mode-changes-in-rust-v0-155-0|9 Agent Mode changes in rust-v0.155.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-17-6-account-and-access-changes-in-rust-v0-155-0|6 Account and Access changes in rust-v0.155.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-17-24-apps-and-integrations-changes-in-rust-v0-155-0|24 Apps and Integrations changes in rust-v0.155.0]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-17-545a49&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-17-96-other-changes-in-rust-v0-155-0.md%0ACard%20ID%3A%20codex-cli-2026-09-17-545a49%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.155.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->