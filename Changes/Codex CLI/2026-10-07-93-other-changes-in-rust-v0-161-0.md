---
card_id: codex-cli-2026-10-07-7ed11f
date: '2026-10-07'
description: 'Codex CLI · 2026-10-07 · Other changes: 93 changes in 0.161.0 — Approved
  filesystem escalation can now grant broader write access while preserving denied
  reads…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1c1f7f1aa50b9b9fe801e818b4ae42e005d35c6a69a535046632e83c24241f39
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-07-7ed11f
  comparison: ''
  date: '2026-10-07'
  description: 'Codex CLI — 0.161.0: 93 other changes'
  evidence:
  - quote: 'Approved filesystem escalation can now grant broader write access while
      preserving denied reads and network restrictions. Background tasks retain their
      originating turn’s permissions. (#49353, #49880)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: Enter correctly submits buffered input after paste detection expires, including
      in Vim insert mode. (#49810)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: 'Thread resume includes the latest committed history. Startup detects recoverable
      SQLite corruption earlier and preserves damaged databases as backups. (#49599,
      #49701)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: Responses retries and WebSocket-to-HTTP fallback honor server retry guidance,
      reducing premature failures during overload. (#49441)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: Publishing an older alpha or hotfix no longer moves npm alpha tags backward.
      (#49704)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49246 Use executable fixture copying in the bundled bwrap test @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49262 Trace turn phases and correlate accepted input with turns @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49269 Preserve thread overrides and cloud policy validity during config
      reloads @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49275 Isolate realtime conversation tests from Responses prewarm connections
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49280 Restrict capability roots to captured turn environments @miz-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49295 Simplify configuration fingerprint canonicalization @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49297 Scan the session index backwards for batch thread name lookups
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49300 Compact the inline hidden tag buffer once per chunk @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49305 Batch metadata reads when resolving thread names @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49316 Bump taiki-e/install-action to v2.87.21 in CI setup @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49332 Clean up canceled exec-server RPC requests immediately @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49353 Allow approved filesystem escalation while preserving denied reads
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49357 Continue Markdown blockquotes when pasting multiline text @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49379 Compile hook matchers during discovery @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49384 Track credential storage outcomes and redact sensitive errors @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49388 Fix Windows path inference for opaque URIs with slash prefixes
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49395 Remove randomized greetings from TUI session headers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49401 Preserve live tool-call metadata across request windows @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49406 Support explicit cyber access programs with OpenAI API keys @julee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49407 Recover exec-server sessions after environment info timeouts @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49408 Compare tool call metadata in the recorder refresh test @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49411 Bind the app-server time provider to a local variable @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49414 Filter graceful shutdown guard and trigger traces from SQLite logs
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49416 Omit payloads from multiline ANSI warnings @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49424 Infer Windows UNC paths with forward and mixed slashes @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49425 Prune diagnostic logs periodically by age and database size @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49426 Enable analytics by default for daemon-launched app servers @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49441 Honor server retry advice across Responses retries and fallback
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49444 Use `memrchr` to find newlines in reverse JSONL scans @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49472 Use server-authoritative permissions in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49480 Add experimental thread prediction protocol types @keyz'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49489 Add regression coverage for account switches between analytics
      batches @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49564 Copy selected file paths as plain text in the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49584 Skip host skill discovery for Guardian reviews @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49595 Make the strict network approval test independent of request order
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49599 Return authoritative replay history when resuming a thread @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49600 Reuse unchanged history snapshots when resuming threads @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49675 Serialize Responses routing fields before large inputs @jbeckwith-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49686 Deliver remote message board notifications to active turns @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49689 Export skill invocation events through OpenTelemetry @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49692 Keep compressed rollout snippet searches on one blocking worker
      @npancha-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49693 Move thread history projection into one blocking task @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49694 Batch rollout listing scans on cancellable blocking workers @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49696 Make exec-server file reads cancellable between chunks @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49701 Detect SQLite corruption during startup and preserve recovery backups
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49702 Rename exec-server file handle management identifiers @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49704 Prevent npm alpha dist-tags from moving backward @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49706 Upgrade the argument comment lint toolchain and Dylint @tamird'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49708 Move session index I/O off async runtime threads @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49710 Classify SQLite corruption using typed error codes @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49712 Avoid full-string scans in token-budget truncation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49713 Remove repository-local Codex guidance, skills, and environment
      config @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49778 Define exec-server protocol types for streamed file writes @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49783 Preserve background thread requests when forking in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49784 Add a requirements feature gate for the browser annotation API
      @tepman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49785 Persist empty paginated threads when naming them @rd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49792 Add retained conversation support to Guardian async sampling @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49793 Add conversation mode to Guardian v2 async classification @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49795 Avoid duplicate sync reviews in Guardian classifier continuations
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49800 Allow cleanup of replay-only side conversations with missing threads
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49801 Update the Rust toolchain action for argument-comment linting @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49804 Use platform-specific modifier labels in TUI shortcut hints @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49805 Add capability-gated writable file streams to the exec-server client
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49806 Accept unknown Codex error variants in the app-server protocol
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49809 Preserve local launch permissions across TUI sessions and reconnects
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49810 Flush expired paste bursts before handling Enter @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49811 Handle unsupported `fs/writeBlock` requests in exec-server @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49812 Move shadow skill ranking off the turn preparation path @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49813 Support AWS GovCloud regions for Amazon Bedrock Mantle @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49816 Remove browser-open success messages from the TUI @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49817 Add an advisory Bedrock GovCloud requirements check @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49818 Use dedicated parameters for sandboxed file opens @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49819 Recover daemon startup and updater re-exec after cwd deletion @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49835 Clarify service tier default save errors in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49843 Preserve daemon diagnostics and include updater logs in reports
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49846 Capture host-supplied extension data for each turn @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49850 Launch Windows daemon children in a dedicated working directory
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49852 Improve diagnostics for report attachment failures @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49855 Use embedded mode for elevated Windows TUI sessions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49858 Add a persistent `/daybreak` toggle to the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49859 Honor Daybreak settings in TUI continuations and background tasks
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49867 Update elevated-launch warning snapshot to use `⌃o` for copy @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49874 Point usage and credit links to ChatGPT settings @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49875 Decouple TUI startup presentation from execution configuration
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49898 Scope extension filesystem access to callback permissions @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49910 Preserve validation errors for invalid TUI keybindings @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49912 Respect approval policies in temporary structured threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49959 Test session index thread-name append and removal @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 93-other-changes-in-rust-v0-161-0
  source_release: codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55
  source_type: github_releases
  theme: uncategorized
  title: 93 other changes in rust-v0.161.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55]]'
source_type: github_releases
theme: uncategorized
title: 93 other changes in rust-v0.161.0
type: change
---

<!-- chronolog:begin region="header" -->
# 93 other changes in rust-v0.161.0

**Codex CLI** · 2026-10-07 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.161.0) · from [[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|0.161.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Approved filesystem escalation can now grant broader write access while preserving denied reads and network restrictions. Background tasks retain their originating turn’s permissions. (#49353, #49880)

> Enter correctly submits buffered input after paste detection expires, including in Vim insert mode. (#49810)

> Thread resume includes the latest committed history. Startup detects recoverable SQLite corruption earlier and preserves damaged databases as backups. (#49599, #49701)

> Responses retries and WebSocket-to-HTTP fallback honor server retry guidance, reducing premature failures during overload. (#49441)

> Publishing an older alpha or hotfix no longer moves npm alpha tags backward. (#49704)

> #49246 Use executable fixture copying in the bundled bwrap test @felixxia-oai

> #49262 Trace turn phases and correlate accepted input with turns @jif-oai

> #49269 Preserve thread overrides and cloud policy validity during config reloads @nicksteele-oai

> #49275 Isolate realtime conversation tests from Responses prewarm connections @felixxia-oai

> #49280 Restrict capability roots to captured turn environments @miz-openai

> #49295 Simplify configuration fingerprint canonicalization @jif-oai

> #49297 Scan the session index backwards for batch thread name lookups @jif-oai

> #49300 Compact the inline hidden tag buffer once per chunk @jif-oai

> #49305 Batch metadata reads when resolving thread names @jif-oai

> #49316 Bump taiki-e/install-action to v2.87.21 in CI setup @jgershen-oai

> #49332 Clean up canceled exec-server RPC requests immediately @jif-oai

> #49353 Allow approved filesystem escalation while preserving denied reads @viyatb-oai

> #49357 Continue Markdown blockquotes when pasting multiline text @bc-openai

> #49379 Compile hook matchers during discovery @jif-oai

> #49384 Track credential storage outcomes and redact sensitive errors @celia-oai

> #49388 Fix Windows path inference for opaque URIs with slash prefixes @dkovalenko-oai

> #49395 Remove randomized greetings from TUI session headers @etraut-openai

> #49401 Preserve live tool-call metadata across request windows @ningyi-oai

> #49406 Support explicit cyber access programs with OpenAI API keys @julee-oai

> #49407 Recover exec-server sessions after environment info timeouts @vivi

> #49408 Compare tool call metadata in the recorder refresh test @euroelessar

> #49411 Bind the app-server time provider to a local variable @euroelessar

> #49414 Filter graceful shutdown guard and trigger traces from SQLite logs @dkovalenko-oai

> #49416 Omit payloads from multiline ANSI warnings @dkovalenko-oai

> #49424 Infer Windows UNC paths with forward and mixed slashes @dkovalenko-oai

> #49425 Prune diagnostic logs periodically by age and database size @dkovalenko-oai

> #49426 Enable analytics by default for daemon-launched app servers @bc-openai

> #49441 Honor server retry advice across Responses retries and fallback @anp-oai

> #49444 Use `memrchr` to find newlines in reverse JSONL scans @btraut-openai

> #49472 Use server-authoritative permissions in the TUI @etraut-openai

> #49480 Add experimental thread prediction protocol types @keyz

> #49489 Add regression coverage for account switches between analytics batches @anp-oai

> #49564 Copy selected file paths as plain text in the TUI @fcoury-oai

> #49584 Skip host skill discovery for Guardian reviews @jif-oai

> #49595 Make the strict network approval test independent of request order @jif-oai

> #49599 Return authoritative replay history when resuming a thread @felixxia-oai

> #49600 Reuse unchanged history snapshots when resuming threads @felixxia-oai

> #49675 Serialize Responses routing fields before large inputs @jbeckwith-oai

> #49686 Deliver remote message board notifications to active turns @jif-oai

> #49689 Export skill invocation events through OpenTelemetry @jif-oai

> #49692 Keep compressed rollout snippet searches on one blocking worker @npancha-openai

> #49693 Move thread history projection into one blocking task @charliemarsh-oai

> #49694 Batch rollout listing scans on cancellable blocking workers @charliemarsh-oai

> #49696 Make exec-server file reads cancellable between chunks @charliemarsh-oai

> #49701 Detect SQLite corruption during startup and preserve recovery backups @dkovalenko-oai

> #49702 Rename exec-server file handle management identifiers @anp-oai

> #49704 Prevent npm alpha dist-tags from moving backward @imac-oai

> #49706 Upgrade the argument comment lint toolchain and Dylint @tamird

> #49708 Move session index I/O off async runtime threads @charliemarsh-oai

> #49710 Classify SQLite corruption using typed error codes @dkovalenko-oai

> #49712 Avoid full-string scans in token-budget truncation @jif-oai

> #49713 Remove repository-local Codex guidance, skills, and environment config @anp-oai

> #49778 Define exec-server protocol types for streamed file writes @anp-oai

> #49783 Preserve background thread requests when forking in the TUI @etraut-openai

> #49784 Add a requirements feature gate for the browser annotation API @tepman-oai

> #49785 Persist empty paginated threads when naming them @rd-oai

> #49792 Add retained conversation support to Guardian async sampling @felixxia-oai

> #49793 Add conversation mode to Guardian v2 async classification @felixxia-oai

> #49795 Avoid duplicate sync reviews in Guardian classifier continuations @felixxia-oai

> #49800 Allow cleanup of replay-only side conversations with missing threads @bc-openai

> #49801 Update the Rust toolchain action for argument-comment linting @andrewgu-oai

> #49804 Use platform-specific modifier labels in TUI shortcut hints @bc-openai

> #49805 Add capability-gated writable file streams to the exec-server client @anp-oai

> #49806 Accept unknown Codex error variants in the app-server protocol @anp-oai

> #49809 Preserve local launch permissions across TUI sessions and reconnects @etraut-openai

> #49810 Flush expired paste bursts before handling Enter @bc-openai

> #49811 Handle unsupported `fs/writeBlock` requests in exec-server @anp-oai

> #49812 Move shadow skill ranking off the turn preparation path @vkg-oai

> #49813 Support AWS GovCloud regions for Amazon Bedrock Mantle @alexsong-oai

> #49816 Remove browser-open success messages from the TUI @bc-openai

> #49817 Add an advisory Bedrock GovCloud requirements check @alexsong-oai

> #49818 Use dedicated parameters for sandboxed file opens @anp-oai

> #49819 Recover daemon startup and updater re-exec after cwd deletion @etraut-openai

> #49835 Clarify service tier default save errors in the TUI @etraut-openai

> #49843 Preserve daemon diagnostics and include updater logs in reports @etraut-openai

> #49846 Capture host-supplied extension data for each turn @sayan-oai

> #49850 Launch Windows daemon children in a dedicated working directory @etraut-openai

> #49852 Improve diagnostics for report attachment failures @dkovalenko-oai

> #49855 Use embedded mode for elevated Windows TUI sessions @etraut-openai

> #49858 Add a persistent `/daybreak` toggle to the TUI @etraut-openai

> #49859 Honor Daybreak settings in TUI continuations and background tasks @etraut-openai

> #49867 Update elevated-launch warning snapshot to use `⌃o` for copy @etraut-openai

> #49874 Point usage and credit links to ChatGPT settings @etraut-openai

> #49875 Decouple TUI startup presentation from execution configuration @etraut-openai

> #49898 Scope extension filesystem access to callback permissions @anp-oai

> #49910 Preserve validation errors for invalid TUI keybindings @etraut-openai

> #49912 Respect approval policies in temporary structured threads @etraut-openai

> #49959 Test session index thread-name append and removal @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.161.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-07-10-developer-workflow-changes-in-rust-v0-161-0|10 Developer Workflow changes in rust-v0.161.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-07-3-search-and-browsing-changes-in-rust-v0-161-0|3 Search and Browsing changes in rust-v0.161.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-07-9-safety-and-privacy-changes-in-rust-v0-161-0|9 Safety and Privacy changes in rust-v0.161.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-07-5-apps-and-integrations-changes-in-rust-v0-161-0|5 Apps and Integrations changes in rust-v0.161.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-07-49856-support-daybreak-selection-in-codex-exec-etraut-openai|♯49856 Support Daybreak selection in codex exec @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-10-07-9-model-support-changes-in-rust-v0-161-0|9 Model Support changes in rust-v0.161.0]] · Model Support
- [[Changes/Codex CLI/2026-10-07-49876-remove-personality-plumbing-from-the-tui-etraut-openai|♯49876 Remove personality plumbing from the TUI @etraut-openai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-07-49473-use-the-rmcp-sdk-for-enterprise-managed-token-exchanges-nicksteele-oai|♯49473 Use the rmcp SDK for enterprise-managed token exchanges @nicksteele-oai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-10-07-10-account-and-access-changes-in-rust-v0-161-0|10 Account and Access changes in rust-v0.161.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-07-9-agent-mode-changes-in-rust-v0-161-0|9 Agent Mode changes in rust-v0.161.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-07-4-voice-and-audio-changes-in-rust-v0-161-0|4 Voice and Audio changes in rust-v0.161.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-07-9-context-window-changes-in-rust-v0-161-0|9 Context Window changes in rust-v0.161.0]] · Context Window
- [[Changes/Codex CLI/2026-10-07-2-collaboration-changes-in-rust-v0-161-0|2 Collaboration changes in rust-v0.161.0]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-07-7ed11f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-07-93-other-changes-in-rust-v0-161-0.md%0ACard%20ID%3A%20codex-cli-2026-10-07-7ed11f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.161.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->