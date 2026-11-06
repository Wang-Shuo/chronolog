---
card_id: codex-cli-2026-09-28-98cc27
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Other changes: 96 changes in 0.158.0 — Approval
  reviews now retry when new user input arrives, so a status question does not…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2a27ebec61da23db8b36f773ec81c82a06ab3900113023a2b89cb13ef0bc2758
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-98cc27
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 96 other changes'
  evidence:
  - quote: Approval reviews now retry when new user input arrives, so a status question
      does not automatically abort a pending action. (#47819)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: 'Mermaid flowcharts now render quoted labels and ampersands; unsupported
      diagrams explain why they fall back to source. (#47572, #47678)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47441 Use secondary text styling for the transcript footer shortcut hint
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47458 Parallelize instruction refresh and tool preparation @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47565 Classify rollout read failures by reason and progress @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47589 Keep unfinished link destinations out of rich streaming previews
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47591 Stream daemon executable hashing off the async runtime @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47597 Guard prerelease channel and canary updates against older versions
      @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47603 Add a reap-only drop policy for child processes @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47604 Extend child commands with session and descriptor controls @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47612 Launch Linux pipe processes through a fresh setup helper @freeqaz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47613 Expand Linux spawn-helper lifecycle test coverage @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47617 Route Linux PTY launches through the process setup helper @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47618 Prefer Shift-arrow hints for queued messages and questions @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47619 Add bounded buffering for global operation metrics @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47620 Add portable project trust lookup APIs @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47623 Fix read-only metadata mount ordering for nested writable roots
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47629 Route V2 child loading through `AgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47630 Bind Guardian reviews to the action''s target environment @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47635 Overlap startup WebSocket preconnect with tool discovery @bromano-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47638 Classify retryable exec-server preparation errors by type @mtsui-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47639 Add configurable copy-on-select for transcript selections @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47641 Honor Retry-After and preserve server retry deadlines @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47653 Attach inherited rollout history to diagnostic reports @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47654 Make Linux descriptor cleanup fork-safe @yuzhu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47655 Bump the exec-server stable compatibility test to Codex 0.156.1
      @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47663 Preserve managed network policy in route-aware transports @jackz100'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47678 Support quoted labels and ampersands in Mermaid flowcharts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47680 Add exec-server RPC timing and process startup tracing @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47683 Add executor capability discovery V2 infrastructure @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47688 Remove legacy Guardian authorization evidence paths @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47693 Configure curl retries for DotSlash installation in CI @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47696 Avoid the shutdown timeout in the lagged-event test @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47698 Allow WebSocket test server shutdown while waiting for requests
      @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47701 Allow idle threads to prewarm and repair WebSocket connections
      @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47703 Preserve account network policy for ChatGPT backend requests @jackz100'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47704 Fix spawn flag typing and isolate project configuration tests @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47709 Route resume prewarm through the cached WebSocket session @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47712 Update unified exec output buffers atomically @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47714 Preserve tool result metadata more selectively under size limits
      @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47741 Attribute tool telemetry to the invoking turn''s product SKU @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47745 Skip startup prewarm preparation when the WebSocket is ready @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47755 Centralize typed app-server response decoding @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47757 Refactor tool telemetry product SKU matching to use an allowlist
      @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47758 Preserve more tool metadata within outgoing message budgets @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47773 Honor catalog schemas for asynchronous user input @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47797 Support close-on-exec attachments without changing PTY semantics
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47811 Preserve explicit user goal updates in Guardian authorization @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47813 Fix sleep interruption test event handling and fixture lifetime
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47814 Fix a lost wakeup in the unified exec termination test @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47819 Retry Guardian reviews when authorization changes @teddywyly-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47830 Bind Guardian async scores to target environment permissions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47832 Stabilize Rosetta test timing and retry delay telemetry @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47847 Keep the TUI responsive during clipboard copies @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47851 Preserve human overrides across repeated heartbeat instructions
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47852 Avoid blocking async proxy resolution on the system proxy cache
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47856 Initialize media estimates outside the global cache lock @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47870 Add opt-in OTLP logging for Guardian assessments @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47871 Fix PID reservation test race and update guardian heartbeat snapshot
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47873 Measure deferred tool namespace fragments before and after truncation
      @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47881 Use Tokio''s clock for TUI paste timing @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47886 Preserve diagnostic logs when SQLite logging fails @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47887 Warn users when SQLite diagnostic log writes fail @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47889 Include TUI client logs in diagnostic uploads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47894 Clean up temporary Codex homes after TUI tests @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47896 Preserve Markdown formatting when copying transcript selections
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47898 Preserve local-binding inheritance in environment network policies
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47900 Default local threads to paginated history @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47901 Add bounded credential-storage telemetry helpers @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47902 Avoid repeated table clones during config merging @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47903 Move config key alias normalization ahead of merging @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47904 Support nested canonical paths in config key aliases @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47908 Alias `tui.whimsy` to `tui.effects.starfield` @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47912 Fix attestation routing during thread startup @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47913 Add an opt-in flag to defer mailbox preemption @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47915 Reuse verified V8 checksum manifests from the artifact cache @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47918 Parameterize the turn-start originator header test @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47920 Allow directory moves under global Seatbelt basename denies @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47922 Allow full-access Windows setup to provision through registered
      Core @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47924 Make project trust lookup paths explicit and defer root resolution
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47926 Retry file blob uploads on HTTP 502 and 504 @mtsui-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47937 Add direct replies for thread settings updates @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47943 Remove unused Windows world-writable audit code @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47945 Parameterize the thread initialization analytics test by originator
      @eddie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47957 Bound tool-call observations to the outgoing Responses message
      budget @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47962 Request transparent huge pages for Cargo and eligible Bazel rustc
      jobs @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47968 Handle Btrfs device mismatches when masking daemon sockets @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47970 Expose current environment selections for a running turn @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47971 Add Pro Max plan support and update Pro display names @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47989 Add startup-only PID namespace inheritance to exec-server @open-matt'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48015 Validate tool suggestion install URLs before showing the app link
      @aionescu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48060 Deduplicate retained instructions across Guardian reviews @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48072 Skip message-board notification previews when there are no recipients
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48109 Deduplicate retained instructions against Guardian transcripts
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48123 Add early yielding for code-mode observations @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48130 Use request notifications in the cloud config loader lifetime test
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 96-other-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: uncategorized
  title: 96 other changes in rust-v0.158.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: uncategorized
title: 96 other changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 96 other changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Approval reviews now retry when new user input arrives, so a status question does not automatically abort a pending action. (#47819)

> Mermaid flowcharts now render quoted labels and ampersands; unsupported diagrams explain why they fall back to source. (#47572, #47678)

> #47441 Use secondary text styling for the transcript footer shortcut hint @etraut-openai

> #47458 Parallelize instruction refresh and tool preparation @hlevy-openai

> #47565 Classify rollout read failures by reason and progress @jif-oai

> #47589 Keep unfinished link destinations out of rich streaming previews @etraut-openai

> #47591 Stream daemon executable hashing off the async runtime @etraut-openai

> #47597 Guard prerelease channel and canary updates against older versions @imac-oai

> #47603 Add a reap-only drop policy for child processes @charliemarsh-oai

> #47604 Extend child commands with session and descriptor controls @charliemarsh-oai

> #47612 Launch Linux pipe processes through a fresh setup helper @freeqaz-openai

> #47613 Expand Linux spawn-helper lifecycle test coverage @charliemarsh-oai

> #47617 Route Linux PTY launches through the process setup helper @charliemarsh-oai

> #47618 Prefer Shift-arrow hints for queued messages and questions @imac-oai

> #47619 Add bounded buffering for global operation metrics @celia-oai

> #47620 Add portable project trust lookup APIs @seanh-oai

> #47623 Fix read-only metadata mount ordering for nested writable roots @jif-oai

> #47629 Route V2 child loading through `AgentControl` @jif-oai

> #47630 Bind Guardian reviews to the action's target environment @jif-oai

> #47635 Overlap startup WebSocket preconnect with tool discovery @bromano-oai

> #47638 Classify retryable exec-server preparation errors by type @mtsui-oai

> #47639 Add configurable copy-on-select for transcript selections @fcoury-oai

> #47641 Honor Retry-After and preserve server retry deadlines @anp-oai

> #47653 Attach inherited rollout history to diagnostic reports @dkovalenko-oai

> #47654 Make Linux descriptor cleanup fork-safe @yuzhu-oai

> #47655 Bump the exec-server stable compatibility test to Codex 0.156.1 @imac-oai

> #47663 Preserve managed network policy in route-aware transports @jackz100

> #47678 Support quoted labels and ampersands in Mermaid flowcharts @etraut-openai

> #47680 Add exec-server RPC timing and process startup tracing @anp-oai

> #47683 Add executor capability discovery V2 infrastructure @TAFOYA-OAI

> #47688 Remove legacy Guardian authorization evidence paths @felixxia-oai

> #47693 Configure curl retries for DotSlash installation in CI @anp-oai

> #47696 Avoid the shutdown timeout in the lagged-event test @jgershen-oai

> #47698 Allow WebSocket test server shutdown while waiting for requests @jgershen-oai

> #47701 Allow idle threads to prewarm and repair WebSocket connections @vkg-oai

> #47703 Preserve account network policy for ChatGPT backend requests @jackz100

> #47704 Fix spawn flag typing and isolate project configuration tests @seanh-oai

> #47709 Route resume prewarm through the cached WebSocket session @vkg-oai

> #47712 Update unified exec output buffers atomically @sdcoffey

> #47714 Preserve tool result metadata more selectively under size limits @ningyi-oai

> #47741 Attribute tool telemetry to the invoking turn's product SKU @rennie-openai

> #47745 Skip startup prewarm preparation when the WebSocket is ready @vkg-oai

> #47755 Centralize typed app-server response decoding @aibrahim-oai

> #47757 Refactor tool telemetry product SKU matching to use an allowlist @rennie-openai

> #47758 Preserve more tool metadata within outgoing message budgets @ningyi-oai

> #47773 Honor catalog schemas for asynchronous user input @rhan-oai

> #47797 Support close-on-exec attachments without changing PTY semantics @jif-oai

> #47811 Preserve explicit user goal updates in Guardian authorization @felixxia-oai

> #47813 Fix sleep interruption test event handling and fixture lifetime @felixxia-oai

> #47814 Fix a lost wakeup in the unified exec termination test @felixxia-oai

> #47819 Retry Guardian reviews when authorization changes @teddywyly-oai

> #47830 Bind Guardian async scores to target environment permissions @jif-oai

> #47832 Stabilize Rosetta test timing and retry delay telemetry @jif-oai

> #47847 Keep the TUI responsive during clipboard copies @fcoury-oai

> #47851 Preserve human overrides across repeated heartbeat instructions @felixxia-oai

> #47852 Avoid blocking async proxy resolution on the system proxy cache @jif-oai

> #47856 Initialize media estimates outside the global cache lock @jif-oai

> #47870 Add opt-in OTLP logging for Guardian assessments @jif-oai

> #47871 Fix PID reservation test race and update guardian heartbeat snapshot @jif-oai

> #47873 Measure deferred tool namespace fragments before and after truncation @mzeng-openai

> #47881 Use Tokio's clock for TUI paste timing @charliemarsh-oai

> #47886 Preserve diagnostic logs when SQLite logging fails @dkovalenko-oai

> #47887 Warn users when SQLite diagnostic log writes fail @dkovalenko-oai

> #47889 Include TUI client logs in diagnostic uploads @etraut-openai

> #47894 Clean up temporary Codex homes after TUI tests @fcoury-oai

> #47896 Preserve Markdown formatting when copying transcript selections @fcoury-oai

> #47898 Preserve local-binding inheritance in environment network policies @seanh-oai

> #47900 Default local threads to paginated history @owenlin0

> #47901 Add bounded credential-storage telemetry helpers @celia-oai

> #47902 Avoid repeated table clones during config merging @imac-oai

> #47903 Move config key alias normalization ahead of merging @imac-oai

> #47904 Support nested canonical paths in config key aliases @imac-oai

> #47908 Alias `tui.whimsy` to `tui.effects.starfield` @imac-oai

> #47912 Fix attestation routing during thread startup @charliemarsh-oai

> #47913 Add an opt-in flag to defer mailbox preemption @jif-oai

> #47915 Reuse verified V8 checksum manifests from the artifact cache @aibrahim-oai

> #47918 Parameterize the turn-start originator header test @aibrahim-oai

> #47920 Allow directory moves under global Seatbelt basename denies @chess-oai

> #47922 Allow full-access Windows setup to provision through registered Core @zm-oai

> #47924 Make project trust lookup paths explicit and defer root resolution @seanh-oai

> #47926 Retry file blob uploads on HTTP 502 and 504 @mtsui-oai

> #47937 Add direct replies for thread settings updates @sayan-oai

> #47943 Remove unused Windows world-writable audit code @iceweasel-oai

> #47945 Parameterize the thread initialization analytics test by originator @eddie-openai

> #47957 Bound tool-call observations to the outgoing Responses message budget @ningyi-oai

> #47962 Request transparent huge pages for Cargo and eligible Bazel rustc jobs @aibrahim-oai

> #47968 Handle Btrfs device mismatches when masking daemon sockets @etraut-openai

> #47970 Expose current environment selections for a running turn @sayan-oai

> #47971 Add Pro Max plan support and update Pro display names @etraut-openai

> #47989 Add startup-only PID namespace inheritance to exec-server @open-matt

> #48015 Validate tool suggestion install URLs before showing the app link @aionescu-oai

> #48060 Deduplicate retained instructions across Guardian reviews @felixxia-oai

> #48072 Skip message-board notification previews when there are no recipients @jif-oai

> #48109 Deduplicate retained instructions against Guardian transcripts @felixxia-oai

> #48123 Add early yielding for code-mode observations @pakrym-oai

> #48130 Use request notifications in the cloud config loader lifetime test @felixxia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-28-8-account-and-access-changes-in-rust-v0-158-0|8 Account and Access changes in rust-v0.158.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0|3 Mobile and Desktop changes in rust-v0.158.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-98cc27&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-96-other-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-98cc27%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->