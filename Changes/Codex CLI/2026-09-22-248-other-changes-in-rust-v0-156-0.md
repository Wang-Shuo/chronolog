---
card_id: codex-cli-2026-09-22-4a0377
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Other changes: 248 changes in 0.156.0 — Update
  the local background server through `/daemon`, or bypass it with `--no-daemon`…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d1805adb03f16779ec7b7731fe6bee70c45a4ae95d7ae0b2654620d957065268
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-4a0377
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 248 other changes'
  evidence:
  - quote: 'Update the local background server through `/daemon`, or bypass it with
      `--no-daemon`. (#45854, #46088)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: 'Restore Plan mode when resuming sessions and preserve thread identity
      and settings when editing earlier prompts. (#45519, #45845)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: Explain how `?` matches a single character in network proxy allow and deny
      patterns. (#46027)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: 'Update bundled TLS dependencies, including OpenSSL 3.6.4 for Linux musl
      builds. (#45149, #45489)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44606 Preserve whole diagnostic attachments and report incomplete uploads
      @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44611 Preserve root turn attribution in turn-start events @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44615 Treat non-interactive dumb terminals as warnings in `codex doctor`
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44619 Allow discarded code mode tool responses to be garbage collected
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44620 Support temporary and minimal filesystem grants in MXC @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44626 Add bounded environment transport for MXC launch requests @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44628 Expose session analytics state in Responses turn metadata @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44654 Preserve missing environment variable diagnostics in Codex Doctor
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44661 Trace tool call receipt, result readiness, and code-mode dispatch
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44666 Honor system reduced-motion preferences in the TUI @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44691 Warn about ignored configuration settings @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44693 Preserve selected profile settings over managed new-thread defaults
      @alexr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44701 Add a provider for thread-scoped instructions @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44732 Clarify folder trust prompts and add restricted widget support
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44744 Make archive confirmation number shortcuts act immediately @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44746 Check folder trust after resolving the startup destination @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44857 Add consistent theme-based thread colors across the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44862 Preserve parent cache affinity for ephemeral forks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44865 Scope code mode callback delegates to individual executions @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44867 Preserve originating budgets for code mode notifications @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44870 Enable worktrees by default and clarify local daemon errors @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44877 Return public key metadata from user verification enrollment @riley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44879 Fade Astra composer stars and stabilize cursor redraws @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44903 Wire up the native Windows MXC helper entry point @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44915 Remove the deprecated `thread/rollback` API @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44931 Stop setting `YARN_NO_PROXY` in the managed proxy environment @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44933 Remove Windows world-writable scans and warnings from the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44944 Enforce managed provider requirements on existing app-server threads
      @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45035 Run DotSlash publishing directly on Ubuntu runners @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45039 Use gzip compression level 6 for Codex package archives @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45051 Consolidate Rust release artifact downloads @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45089 Delay automatic recaps and compact their TUI layout @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45108 Cancel pending thread title generation after manual renames @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45116 Prevent multiline report notes from submitting early @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45124 Add a feature flag for asynchronous user messages @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45135 Preview streaming prose before a newline arrives in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45137 Remove Astra sparkle animation from the TUI composer @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45149 Use OpenSSL 3.6.4 for musl builds @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45185 Bind direct tool-call metadata to invocation outputs @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45262 Route pastes into the active history search query @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45399 Cancel code mode timer tasks when cleared or the cell finishes
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45413 Invalidate Guardian review sessions after parent history resets
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45418 Extract Guardian conversation bookkeeping into the reviewer crate
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45420 Extract Guardian sampler execution into a dedicated module @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45441 Preserve Guardian parent response IDs across sampling requests
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45454 Preserve tabs in non-bracketed paste bursts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45457 Fix clipboard routing for tmux and SSH sessions @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45461 Label rollout compression failures by stage and I/O error kind
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45463 Allow dedicated listeners for managed network proxies @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45475 Fix fuzzy match scoring within Unicode lowercase expansions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45487 Retain thread persistence acquisition through session cancellation
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45489 Update `rustls` and AWS-LC dependencies in Cargo and Bazel lockfiles
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45492 Split Guardian V2 async scoring into focused modules @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45493 Make the Guardian deadline cancellation helper crate-private @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45496 Trace global user instruction loading @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45499 Send local TUI images as portable attachments to remote app servers
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45501 Render inline TeX math as Unicode in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45502 Add managed thread lifetimes with cancellation-safe startup @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45503 Add revocable network policy primitives to the HTTP client @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45504 Allow ConPTY output to close after the last console client exits
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45505 Add lifecycle tracing for unified exec @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45506 Allow background persistence for steered user input @bryanashley'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45513 Allow setting `daybreakEnabled` when starting a thread @faizan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45516 Allow configuring the Guardian prompt template @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45517 Use a dedicated mock server in the provider enforcement test @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45518 Route Guardian reviewers through ThreadManager for inline parents
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45521 Move Guardian reviewer startup into the pool @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45524 Enable MXC TTY launches and managed networking in the exec server
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45526 Stage Python runtime wheels directly from package directories @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45528 Compress larger Windows release artifacts first @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45529 Expose selected workspace routing in app-server account reads @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45535 Classify tool analytics events by call origin @eddie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45537 Move Guardian reviewer lifecycle into the extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45546 Move daemon packages out of the standalone CLI installation @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45548 Honor prepared Unix socket permissions in Seatbelt @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45549 Preserve streamed answers and plans when turns terminate @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45556 Add attachment upload and resolution APIs and pass stores into
      sessions @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45558 Seed missing daemon installs from complete local CLI packages @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45579 Copy current thread attachments into non-ephemeral forks @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45580 Add explicit daemon package replacement from the CLI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45602 Fix retry classification for throttling and quota errors @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45612 Render standalone display math in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45672 Consolidate Guardian reviewer lifecycle ownership @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45677 Move Guardian review reporting and denial accounting into the extension
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45679 Retire the unused Guardian extension prototype API @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45680 Restrict guardian assessment parsing and circuit breaker visibility
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45684 Pass `ReviewModel` through guardian review sessions @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45693 Move Guardian approval routing into the reviewer extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45711 Add startup tool allowlists for threads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45729 Move Guardian reviewer configuration into the extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45736 Route Guardian requests through `/responses` with identifying headers
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45739 Add typed account analytics reports to the backend client @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45740 Add account analytics data normalization to the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45741 Add token history and credit formatting helpers for analytics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45746 Explicitly gate DotSlash publishing on release success @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45760 Disable V8 optimization paths affected by array sort bugs @kliu128'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45762 Load analytics reports with server plans and account identity checks
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45763 Add stacked chart primitives for account analytics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45764 Add an account analytics dashboard to `/usage` @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45765 Add Top chats to usage analytics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45766 Add gated plan usage history to TUI analytics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45768 Add consumer Top chats usage analytics @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45779 Use native process identities for PID-managed daemons @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45780 Allow daemon updates to restore pinned packages to latest stable
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45781 Normalize bullet glyphs in the image preparation disconnect snapshot
      @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45782 Preserve Guardian authorization evidence across checkpoint migration
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45789 Preserve Guardian evidence during checkpoint migration @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45794 Support image references by file ID in inputs and tool outputs
      @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45807 Record interrupted turns in managed daemon recovery snapshots @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45812 Add workspace routing support for Responses requests @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45817 Add a bounded Mermaid text renderer @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45820 Continue interrupted work after managed daemon restarts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45822 Add opt-in response body limits to the HTTP transport @sergio-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45823 Run R2 publishing when release dependencies succeed @dkumar-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45825 Add opt-in nonfatal handling for clock read failures @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45837 Hide WSLg''s duplicate root in restricted Linux sandboxes @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45845 Revert the current thread when editing an earlier TUI prompt @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45865 Reject paths in project documentation fallback filenames @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45957 Centralize Guardian policy resolution in config and protocol @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45966 Measure rollout read and materialization durations @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45980 Fall back to summary history for read-only conversations @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45984 Isolate app-server Unix sockets from filesystem-restricted commands
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45985 Replace guardian review result tuples with named structs @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45987 Centralize Guardian action preparation for review @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46002 Extract route-aware HTTP request execution into a separate module
      @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46004 Preserve attachment Unix socket grants when controller policy is
      omitted @open-matt'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46006 Report clock failures again after recovery @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46010 Enable app tool result metadata with analytics controls @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46011 Enforce managed residency when constructing API providers @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46015 Allow callers to disable executor skills per environment @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46020 Add an experimental rollout compression endpoint @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46031 Keep Noise relay streams alive after repeated handshake failures
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46035 Add per-app tool exposure configuration @ptiet-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46036 Preserve config error causes when saving the approvals reviewer
      @darius-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46041 Tighten request handling in Guardian approval tests @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46047 Tag rollout compression metrics by trigger @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46051 Track WebSocket continuation modes and full-input send reasons
      @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46054 Render Mermaid code blocks as diagrams in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46063 Trim Guardian tests and tighten request layout assertions @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46065 Route prepared images through the attachment store @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46069 Use syntax theme colors for inline code and file paths @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46070 Suppress warnings when skill descriptions are shortened @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46073 Bound code-mode output previews across result blocks @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46081 Mark finished empty Code Mode tool inventories as complete @nf-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46096 Add a one-time composer starfield for new Astra tasks @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46107 Box app-server request handler futures to reduce stack usage @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46108 Replace Sites migration state with a runtime compatibility guard
      @jiwon-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46116 Make TUI web and image activity summaries compact and descriptive
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46117 Add opt-in automatic background server startup @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46125 Fix daemon socket isolation checks for private tmp mounts @open-matt'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46179 Include sender user messages in Guardian delegation reviews @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46230 Preserve configured Flex tiers without catalog or fast-mode support
      @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46245 Publish Guardian cached scores and coverage atomically @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46258 Preserve uploaded image file IDs in user message display history
      @kchainani-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46268 Add filesystem accessors bound to environment permissions @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46278 Reduce R2 release upload concurrency and enable standard retries
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46279 Preserve Guardian''s reusable history prefix across approval requests
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46288 Add opt-in overhead timing to code-mode responses @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46293 Route skill discovery and loading through `EnvironmentAccess` @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46294 Separate thread startup metadata from replay history @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46302 Validate network socket policies using the executor OS @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46303 Serialize release asset uploads to avoid secondary rate limits
      @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46305 Avoid cloning turn items for app-server active turn lookups @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46306 Preserve bio policy errors as a distinct non-retryable error @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46328 Avoid persisting project trust for projectless directories @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46330 Move retry backoff into `codex-async-utils` @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46331 Defer environment network policy validation until after composition
      @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46332 Dim conversation recaps in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46488 Split analytics tests into focused suites @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46492 Unify TUI tool output previews with a three-row limit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46494 Keep remote workspace roots under server control @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46499 Allow approved escalation with environment-owned network policies
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46501 Add configuration and feature diagnostics to report metadata @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46504 Add six bundled TUI themes and theme-aware accents @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46509 Flush completed Guardian reviews before delivering decisions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46510 Avoid cloning active turn items for metadata-only thread resumes
      @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46511 Avoid cloning excluded turn items during thread resume @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46513 Rename `AgentControl` to `LocalAgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46514 Replay guardian checkpoints into a fresh session in tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46517 Stabilize the TUI exit interruption test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46518 Handle delayed process startup in the Guardian network approval
      test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46523 Default local binding to true for MXC managed networking @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46524 Retry busy executable launches in packaged daemon tests @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46527 Pin WinGet publishing dependencies in the release workflow @imac-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46532 Remove `com.apple.runningboard` from Seatbelt platform defaults
      @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46534 Support `env_inherit` in `workspace_root_test` @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46540 Centralize retry decisions and delays in `CodexErr` @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46543 Add bounded filesystem path diagnostics to `codex doctor` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46546 Skip skill discovery when injecting items into initialized threads
      @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46548 Advertise the control socket''s WebSocket message size limit @konsti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46551 Add a composite action to build and smoke-test Codex packages @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46554 Always use private desktops for legacy Windows sandboxes @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46555 Track executor registrations across connection refresh and recovery
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46556 Keep step settings and approval environments consistent @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46559 Encapsulate rollout budget accounting in `LocalAgentControl` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46560 Fix stale environment config in the network approval test @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46566 Allow recovery commands when the current thread is unavailable
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46568 Use captured environment state for permissions and daemon recovery
      @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46569 Set explicit turn triggers for exec and TUI requests @eddie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46573 Add a standalone network proxy binary with JSON configuration @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46574 Notify users when asynchronous questions arrive in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46575 Preserve Windows package identity for sandboxed descendants @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46578 Fix standalone network proxy policy initialization @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46580 Keep Guardian reviews on the applied instruction snapshot @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46659 Move local child-process spawning into `codex-utils-pty` @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46660 Make local child process launch settings explicit @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46673 Extend server version notices to prerelease and local clients @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46708 Preserve logical source text and styles across TUI wrapping @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46710 Restore rich tool details in persisted TUI transcripts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46712 Recover executed tool call metadata under recorder capacity pressure
      @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46714 Skip polling delays in the external queue lifecycle test @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46719 Extract the TUI transcript overlay into its own module @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46731 Render dynamic tool activity and preserve TUI history ordering
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46733 Integrate the interactive transcript into the alternate-screen
      TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46734 Add transcript search and per-activity detail controls @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46749 Stabilize transcript and composer interactions in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46750 Preserve startup drafts and submit them when the session is ready
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46751 Add a warning footer and dedicated warnings viewer to the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46832 Add independent controls for TUI visual effects @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46844 Select read-only permissions for temporary structured threads @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46861 Remove analytics TUI snapshots @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46862 Refresh analytics on identity changes and compact usage menus @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46864 Improve usage report layouts and preserve reading positions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46884 Enable plain clicks on transcript links and style bare URLs @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46895 Add right-click copying for transcript and composer selections
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46899 Make transcript list spacing uniform after streaming @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46902 Hide Back to bottom when the current transcript tail is visible
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46905 Identify local background servers in `/status` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46910 Preserve transcript position when opening settings pickers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46912 Keep quota warnings visible in the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46922 Fix realtime V3 transcript reconciliation for handoffs @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46929 Remove the `Error` prefix from TUI `config.toml` load errors @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46952 Preserve metadata in native user verification requests @teddywyly-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46962 Avoid exposing config values in `codex doctor` errors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46979 Index channel posts by timestamp for latest-message lookups @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46993 Clarify Bazel lockfile verification failures @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46999 Decouple tool restrictions from session identity with `ToolPolicy`
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47026 Add diagnostics for rollout compression metadata failures @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47029 Delete persisted message boards with their root threads @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47035 Defer extension tool history materialization until first access
      @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47039 Preserve delivered messages through post-tool hook failures @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47042 Recover corrupt message-board storage during thread deletion @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47050 Batch message-board subscriber reads into one SQLite result @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#47055 Fetch local message board thread summaries in one query @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 248-other-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: uncategorized
  title: 248 other changes in rust-v0.156.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: uncategorized
title: 248 other changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 248 other changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Update the local background server through `/daemon`, or bypass it with `--no-daemon`. (#45854, #46088)

> Restore Plan mode when resuming sessions and preserve thread identity and settings when editing earlier prompts. (#45519, #45845)

> Explain how `?` matches a single character in network proxy allow and deny patterns. (#46027)

> Update bundled TLS dependencies, including OpenSSL 3.6.4 for Linux musl builds. (#45149, #45489)

> #44606 Preserve whole diagnostic attachments and report incomplete uploads @chess-oai

> #44611 Preserve root turn attribution in turn-start events @owenlin0

> #44615 Treat non-interactive dumb terminals as warnings in `codex doctor` @etraut-openai

> #44619 Allow discarded code mode tool responses to be garbage collected @jif-oai

> #44620 Support temporary and minimal filesystem grants in MXC @iceweasel-oai

> #44626 Add bounded environment transport for MXC launch requests @iceweasel-oai

> #44628 Expose session analytics state in Responses turn metadata @marksteinbrick-oai

> #44654 Preserve missing environment variable diagnostics in Codex Doctor @etraut-openai

> #44661 Trace tool call receipt, result readiness, and code-mode dispatch @anp-oai

> #44666 Honor system reduced-motion preferences in the TUI @imac-oai

> #44691 Warn about ignored configuration settings @andrewgu-oai

> #44693 Preserve selected profile settings over managed new-thread defaults @alexr-oai

> #44701 Add a provider for thread-scoped instructions @vkg-oai

> #44732 Clarify folder trust prompts and add restricted widget support @etraut-openai

> #44744 Make archive confirmation number shortcuts act immediately @etraut-openai

> #44746 Check folder trust after resolving the startup destination @etraut-openai

> #44857 Add consistent theme-based thread colors across the TUI @etraut-openai

> #44862 Preserve parent cache affinity for ephemeral forks @jif-oai

> #44865 Scope code mode callback delegates to individual executions @abhinav-oai

> #44867 Preserve originating budgets for code mode notifications @abhinav-oai

> #44870 Enable worktrees by default and clarify local daemon errors @bc-openai

> #44877 Return public key metadata from user verification enrollment @riley-oai

> #44879 Fade Astra composer stars and stabilize cursor redraws @imac-oai

> #44903 Wire up the native Windows MXC helper entry point @iceweasel-oai

> #44915 Remove the deprecated `thread/rollback` API @owenlin0

> #44931 Stop setting `YARN_NO_PROXY` in the managed proxy environment @viyatb-oai

> #44933 Remove Windows world-writable scans and warnings from the TUI @etraut-openai

> #44944 Enforce managed provider requirements on existing app-server threads @alexsong-oai

> #45035 Run DotSlash publishing directly on Ubuntu runners @charliemarsh-oai

> #45039 Use gzip compression level 6 for Codex package archives @charliemarsh-oai

> #45051 Consolidate Rust release artifact downloads @charliemarsh-oai

> #45089 Delay automatic recaps and compact their TUI layout @fcoury-oai

> #45108 Cancel pending thread title generation after manual renames @fcoury-oai

> #45116 Prevent multiline report notes from submitting early @etraut-openai

> #45124 Add a feature flag for asynchronous user messages @alishobeiri-oai

> #45135 Preview streaming prose before a newline arrives in the TUI @etraut-openai

> #45137 Remove Astra sparkle animation from the TUI composer @fcoury-oai

> #45149 Use OpenSSL 3.6.4 for musl builds @zm-oai

> #45185 Bind direct tool-call metadata to invocation outputs @ningyi-oai

> #45262 Route pastes into the active history search query @charliemarsh-oai

> #45399 Cancel code mode timer tasks when cleared or the cell finishes @jif-oai

> #45413 Invalidate Guardian review sessions after parent history resets @jif-oai

> #45418 Extract Guardian conversation bookkeeping into the reviewer crate @felixxia-oai

> #45420 Extract Guardian sampler execution into a dedicated module @felixxia-oai

> #45441 Preserve Guardian parent response IDs across sampling requests @jif-oai

> #45454 Preserve tabs in non-bracketed paste bursts @etraut-openai

> #45457 Fix clipboard routing for tmux and SSH sessions @fcoury-oai

> #45461 Label rollout compression failures by stage and I/O error kind @jif-oai

> #45463 Allow dedicated listeners for managed network proxies @iceweasel-oai

> #45475 Fix fuzzy match scoring within Unicode lowercase expansions @etraut-openai

> #45487 Retain thread persistence acquisition through session cancellation @jif-oai

> #45489 Update `rustls` and AWS-LC dependencies in Cargo and Bazel lockfiles @zm-oai

> #45492 Split Guardian V2 async scoring into focused modules @felixxia-oai

> #45493 Make the Guardian deadline cancellation helper crate-private @felixxia-oai

> #45496 Trace global user instruction loading @vkg-oai

> #45499 Send local TUI images as portable attachments to remote app servers @etraut-openai

> #45501 Render inline TeX math as Unicode in the TUI @etraut-openai

> #45502 Add managed thread lifetimes with cancellation-safe startup @jif-oai

> #45503 Add revocable network policy primitives to the HTTP client @acrognale-oai

> #45504 Allow ConPTY output to close after the last console client exits @iceweasel-oai

> #45505 Add lifecycle tracing for unified exec @anp-oai

> #45506 Allow background persistence for steered user input @bryanashley

> #45513 Allow setting `daybreakEnabled` when starting a thread @faizan-oai

> #45516 Allow configuring the Guardian prompt template @won-openai

> #45517 Use a dedicated mock server in the provider enforcement test @zm-oai

> #45518 Route Guardian reviewers through ThreadManager for inline parents @jif-oai

> #45521 Move Guardian reviewer startup into the pool @jif-oai

> #45524 Enable MXC TTY launches and managed networking in the exec server @iceweasel-oai

> #45526 Stage Python runtime wheels directly from package directories @charliemarsh-oai

> #45528 Compress larger Windows release artifacts first @charliemarsh-oai

> #45529 Expose selected workspace routing in app-server account reads @acrognale-oai

> #45535 Classify tool analytics events by call origin @eddie-openai

> #45537 Move Guardian reviewer lifecycle into the extension @jif-oai

> #45546 Move daemon packages out of the standalone CLI installation @etraut-openai

> #45548 Honor prepared Unix socket permissions in Seatbelt @viyatb-oai

> #45549 Preserve streamed answers and plans when turns terminate @etraut-openai

> #45556 Add attachment upload and resolution APIs and pass stores into sessions @kchainani-oai

> #45558 Seed missing daemon installs from complete local CLI packages @etraut-openai

> #45579 Copy current thread attachments into non-ephemeral forks @joeytrasatti-openai

> #45580 Add explicit daemon package replacement from the CLI @etraut-openai

> #45602 Fix retry classification for throttling and quota errors @sdcoffey

> #45612 Render standalone display math in the TUI @etraut-openai

> #45672 Consolidate Guardian reviewer lifecycle ownership @jif-oai

> #45677 Move Guardian review reporting and denial accounting into the extension @jif-oai

> #45679 Retire the unused Guardian extension prototype API @felixxia-oai

> #45680 Restrict guardian assessment parsing and circuit breaker visibility @felixxia-oai

> #45684 Pass `ReviewModel` through guardian review sessions @felixxia-oai

> #45693 Move Guardian approval routing into the reviewer extension @jif-oai

> #45711 Add startup tool allowlists for threads @jif-oai

> #45729 Move Guardian reviewer configuration into the extension @jif-oai

> #45736 Route Guardian requests through `/responses` with identifying headers @jif-oai

> #45739 Add typed account analytics reports to the backend client @fcoury-oai

> #45740 Add account analytics data normalization to the TUI @fcoury-oai

> #45741 Add token history and credit formatting helpers for analytics @fcoury-oai

> #45746 Explicitly gate DotSlash publishing on release success @chess-oai

> #45760 Disable V8 optimization paths affected by array sort bugs @kliu128

> #45762 Load analytics reports with server plans and account identity checks @fcoury-oai

> #45763 Add stacked chart primitives for account analytics @fcoury-oai

> #45764 Add an account analytics dashboard to `/usage` @fcoury-oai

> #45765 Add Top chats to usage analytics @fcoury-oai

> #45766 Add gated plan usage history to TUI analytics @fcoury-oai

> #45768 Add consumer Top chats usage analytics @fcoury-oai

> #45779 Use native process identities for PID-managed daemons @etraut-openai

> #45780 Allow daemon updates to restore pinned packages to latest stable @etraut-openai

> #45781 Normalize bullet glyphs in the image preparation disconnect snapshot @jgershen-oai

> #45782 Preserve Guardian authorization evidence across checkpoint migration @felixxia-oai

> #45789 Preserve Guardian evidence during checkpoint migration @felixxia-oai

> #45794 Support image references by file ID in inputs and tool outputs @kchainani-oai

> #45807 Record interrupted turns in managed daemon recovery snapshots @etraut-openai

> #45812 Add workspace routing support for Responses requests @acrognale-oai

> #45817 Add a bounded Mermaid text renderer @etraut-openai

> #45820 Continue interrupted work after managed daemon restarts @etraut-openai

> #45822 Add opt-in response body limits to the HTTP transport @sergio-oai

> #45823 Run R2 publishing when release dependencies succeed @dkumar-oai

> #45825 Add opt-in nonfatal handling for clock read failures @vivi

> #45837 Hide WSLg's duplicate root in restricted Linux sandboxes @etraut-openai

> #45845 Revert the current thread when editing an earlier TUI prompt @etraut-openai

> #45865 Reject paths in project documentation fallback filenames @etraut-openai

> #45957 Centralize Guardian policy resolution in config and protocol @jif-oai

> #45966 Measure rollout read and materialization durations @jif-oai

> #45980 Fall back to summary history for read-only conversations @etraut-openai

> #45984 Isolate app-server Unix sockets from filesystem-restricted commands @etraut-openai

> #45985 Replace guardian review result tuples with named structs @felixxia-oai

> #45987 Centralize Guardian action preparation for review @felixxia-oai

> #46002 Extract route-aware HTTP request execution into a separate module @acrognale-oai

> #46004 Preserve attachment Unix socket grants when controller policy is omitted @open-matt

> #46006 Report clock failures again after recovery @anp-oai

> #46010 Enable app tool result metadata with analytics controls @ningyi-oai

> #46011 Enforce managed residency when constructing API providers @andrewgu-oai

> #46015 Allow callers to disable executor skills per environment @vkg-oai

> #46020 Add an experimental rollout compression endpoint @jif-oai

> #46031 Keep Noise relay streams alive after repeated handshake failures @viyatb-oai

> #46035 Add per-app tool exposure configuration @ptiet-oai

> #46036 Preserve config error causes when saving the approvals reviewer @darius-oai

> #46041 Tighten request handling in Guardian approval tests @jgershen-oai

> #46047 Tag rollout compression metrics by trigger @jif-oai

> #46051 Track WebSocket continuation modes and full-input send reasons @vkg-oai

> #46054 Render Mermaid code blocks as diagrams in the TUI @etraut-openai

> #46063 Trim Guardian tests and tighten request layout assertions @felixxia-oai

> #46065 Route prepared images through the attachment store @kchainani-oai

> #46069 Use syntax theme colors for inline code and file paths @etraut-openai

> #46070 Suppress warnings when skill descriptions are shortened @etraut-openai

> #46073 Bound code-mode output previews across result blocks @etraut-openai

> #46081 Mark finished empty Code Mode tool inventories as complete @nf-openai

> #46096 Add a one-time composer starfield for new Astra tasks @imac-oai

> #46107 Box app-server request handler futures to reduce stack usage @etraut-openai

> #46108 Replace Sites migration state with a runtime compatibility guard @jiwon-oai

> #46116 Make TUI web and image activity summaries compact and descriptive @etraut-openai

> #46117 Add opt-in automatic background server startup @etraut-openai

> #46125 Fix daemon socket isolation checks for private tmp mounts @open-matt

> #46179 Include sender user messages in Guardian delegation reviews @jif-oai

> #46230 Preserve configured Flex tiers without catalog or fast-mode support @sdcoffey

> #46245 Publish Guardian cached scores and coverage atomically @felixxia-oai

> #46258 Preserve uploaded image file IDs in user message display history @kchainani-oai

> #46268 Add filesystem accessors bound to environment permissions @anp-oai

> #46278 Reduce R2 release upload concurrency and enable standard retries @anp-oai

> #46279 Preserve Guardian's reusable history prefix across approval requests @jif-oai

> #46288 Add opt-in overhead timing to code-mode responses @cassirer-openai

> #46293 Route skill discovery and loading through `EnvironmentAccess` @anp-oai

> #46294 Separate thread startup metadata from replay history @charliemarsh-oai

> #46302 Validate network socket policies using the executor OS @seanh-oai

> #46303 Serialize release asset uploads to avoid secondary rate limits @imac-oai

> #46305 Avoid cloning turn items for app-server active turn lookups @charliemarsh-oai

> #46306 Preserve bio policy errors as a distinct non-retryable error @rennie-openai

> #46328 Avoid persisting project trust for projectless directories @viyatb-oai

> #46330 Move retry backoff into `codex-async-utils` @bolinfest

> #46331 Defer environment network policy validation until after composition @seanh-oai

> #46332 Dim conversation recaps in the TUI @etraut-openai

> #46488 Split analytics tests into focused suites @rhan-oai

> #46492 Unify TUI tool output previews with a three-row limit @etraut-openai

> #46494 Keep remote workspace roots under server control @etraut-openai

> #46499 Allow approved escalation with environment-owned network policies @sayan-oai

> #46501 Add configuration and feature diagnostics to report metadata @pakrym-oai

> #46504 Add six bundled TUI themes and theme-aware accents @etraut-openai

> #46509 Flush completed Guardian reviews before delivering decisions @jif-oai

> #46510 Avoid cloning active turn items for metadata-only thread resumes @charliemarsh-oai

> #46511 Avoid cloning excluded turn items during thread resume @charliemarsh-oai

> #46513 Rename `AgentControl` to `LocalAgentControl` @jif-oai

> #46514 Replay guardian checkpoints into a fresh session in tests @jif-oai

> #46517 Stabilize the TUI exit interruption test @jif-oai

> #46518 Handle delayed process startup in the Guardian network approval test @jif-oai

> #46523 Default local binding to true for MXC managed networking @iceweasel-oai

> #46524 Retry busy executable launches in packaged daemon tests @felixxia-oai

> #46527 Pin WinGet publishing dependencies in the release workflow @imac-oai

> #46532 Remove `com.apple.runningboard` from Seatbelt platform defaults @nornagon-openai

> #46534 Support `env_inherit` in `workspace_root_test` @bolinfest

> #46540 Centralize retry decisions and delays in `CodexErr` @anp-oai

> #46543 Add bounded filesystem path diagnostics to `codex doctor` @etraut-openai

> #46546 Skip skill discovery when injecting items into initialized threads @hlevy-openai

> #46548 Advertise the control socket's WebSocket message size limit @konsti-openai

> #46551 Add a composite action to build and smoke-test Codex packages @anp-oai

> #46554 Always use private desktops for legacy Windows sandboxes @iceweasel-oai

> #46555 Track executor registrations across connection refresh and recovery @viyatb-oai

> #46556 Keep step settings and approval environments consistent @sayan-oai

> #46559 Encapsulate rollout budget accounting in `LocalAgentControl` @jif-oai

> #46560 Fix stale environment config in the network approval test @sayan-oai

> #46566 Allow recovery commands when the current thread is unavailable @etraut-openai

> #46568 Use captured environment state for permissions and daemon recovery @sayan-oai

> #46569 Set explicit turn triggers for exec and TUI requests @eddie-openai

> #46573 Add a standalone network proxy binary with JSON configuration @viyatb-oai

> #46574 Notify users when asynchronous questions arrive in the TUI @etraut-openai

> #46575 Preserve Windows package identity for sandboxed descendants @zm-oai

> #46578 Fix standalone network proxy policy initialization @etraut-openai

> #46580 Keep Guardian reviews on the applied instruction snapshot @jif-oai

> #46659 Move local child-process spawning into `codex-utils-pty` @charliemarsh-oai

> #46660 Make local child process launch settings explicit @charliemarsh-oai

> #46673 Extend server version notices to prerelease and local clients @etraut-openai

> #46708 Preserve logical source text and styles across TUI wrapping @etraut-openai

> #46710 Restore rich tool details in persisted TUI transcripts @etraut-openai

> #46712 Recover executed tool call metadata under recorder capacity pressure @ningyi-oai

> #46714 Skip polling delays in the external queue lifecycle test @charliemarsh-oai

> #46719 Extract the TUI transcript overlay into its own module @etraut-openai

> #46731 Render dynamic tool activity and preserve TUI history ordering @etraut-openai

> #46733 Integrate the interactive transcript into the alternate-screen TUI @etraut-openai

> #46734 Add transcript search and per-activity detail controls @etraut-openai

> #46749 Stabilize transcript and composer interactions in the TUI @etraut-openai

> #46750 Preserve startup drafts and submit them when the session is ready @etraut-openai

> #46751 Add a warning footer and dedicated warnings viewer to the TUI @etraut-openai

> #46832 Add independent controls for TUI visual effects @etraut-openai

> #46844 Select read-only permissions for temporary structured threads @etraut-openai

> #46861 Remove analytics TUI snapshots @etraut-openai

> #46862 Refresh analytics on identity changes and compact usage menus @etraut-openai

> #46864 Improve usage report layouts and preserve reading positions @etraut-openai

> #46884 Enable plain clicks on transcript links and style bare URLs @etraut-openai

> #46895 Add right-click copying for transcript and composer selections @fcoury-oai

> #46899 Make transcript list spacing uniform after streaming @fcoury-oai

> #46902 Hide Back to bottom when the current transcript tail is visible @fcoury-oai

> #46905 Identify local background servers in `/status` @etraut-openai

> #46910 Preserve transcript position when opening settings pickers @etraut-openai

> #46912 Keep quota warnings visible in the TUI @fcoury-oai

> #46922 Fix realtime V3 transcript reconciliation for handoffs @etraut-openai

> #46929 Remove the `Error` prefix from TUI `config.toml` load errors @etraut-openai

> #46952 Preserve metadata in native user verification requests @teddywyly-oai

> #46962 Avoid exposing config values in `codex doctor` errors @jif-oai

> #46979 Index channel posts by timestamp for latest-message lookups @jif-oai

> #46993 Clarify Bazel lockfile verification failures @jif-oai

> #46999 Decouple tool restrictions from session identity with `ToolPolicy` @felixxia-oai

> #47026 Add diagnostics for rollout compression metadata failures @jif-oai

> #47029 Delete persisted message boards with their root threads @jif-oai

> #47035 Defer extension tool history materialization until first access @charliemarsh-oai

> #47039 Preserve delivered messages through post-tool hook failures @felixxia-oai

> #47042 Recover corrupt message-board storage during thread deletion @jif-oai

> #47050 Batch message-board subscriber reads into one SQLite result @jif-oai

> #47055 Fetch local message board thread summaries in one query @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.156.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13 Account and Access changes in rust-v0.156.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-22-32-interface-experience-changes-in-rust-v0-156-0|32 Interface Experience changes in rust-v0.156.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-22-2-search-and-browsing-changes-in-rust-v0-156-0|2 Search and Browsing changes in rust-v0.156.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-22-46027-document-and-test-wildcards-in-network-proxy-domain-patterns-viyatb-oai|♯46027 Document and test ? wildcards in network proxy domain patterns @viyatb-oai]] · Files and Data
- [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544 Discourage logging full image generation results @Gan-Tu]] · Image Generation
- [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]] · Context Window
- [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11 Mobile and Desktop changes in rust-v0.156.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]] · Model Support
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-4a0377&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-248-other-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-4a0377%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->