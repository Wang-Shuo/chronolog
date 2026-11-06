---
card_id: codex-cli-2026-10-15-36cdbf
date: '2026-10-15'
description: 'Codex CLI · 2026-10-15 · Other changes: 134 changes in 0.163.0 — Open
  `/config` to search preferences across categories, change supported settings immediately…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d3b6ad0dcd85a6042eacca7c3d10b57b391cb6906de2a9eb2098ce62d97bd4b5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-15-36cdbf
  comparison: ''
  date: '2026-10-15'
  description: 'Codex CLI — 0.163.0: 134 other changes'
  evidence:
  - quote: 'Open `/config` to search preferences across categories, change supported
      settings immediately, and see which changes require a restart. (#52990, #53429)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: 'Send a follow-up while Codex is responding to steer it immediately. Interrupting
      a turn also stops active Code Mode cells and their nested tool calls. (#51812,
      #51835)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: Restart a managed background server from `/daemon`. Codex warns about work
      the restart could interrupt, then reconnects automatically. (#53173)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: 'Daybreak is enabled by default for eligible accounts. `codex exec` can
      also select it with an OpenAI API key when the server offers access. (#53701,
      #53717)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: 'Resuming a saved thread restores its permissions and network approvals,
      while respecting explicit overrides and current managed policy. (#53150, #53419,
      #53424)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: 'Return to an existing side conversation with `/side` after switching threads.
      Answers to pending prompts also go back to the thread that asked. (#52184, #53436)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: 'Local commands finish promptly when a child keeps an output pipe open.
      Remote commands preserve late-arriving output so the final poll can still collect
      it. (#52652, #53331, #53622)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51556 Complete dynamic tool lifecycles on cancellation @mikelam-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51575 Expose package assembly helpers and support gzip DotSlash artifacts
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51595 Add thread ID exclusions to `thread/list` @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51602 Distinguish thread listing failures from exhausted history @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51650 Require hostname authorization before proxy DNS lookups @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51651 Persist Guardian review failures for reports across restarts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51683 Roll back stale Guardian reviews before reusing reviewer history
      @olliem-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51690 Add a feature flag for Code Mode tool description ordering @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51704 Honor tool-description-first ordering in Code Mode @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51710 Fix a discovery race in the external auth refresh test @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51761 Reduce tool metadata cloning in the code-mode runtime @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51775 Prevent recursive Tokio tracing in telemetry and SQLite logs @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51800 Remove duplicate field initializers in extension registry tests
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51812 Enable instant interrupts by default @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51828 Add policy-based file contents integrity checks @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51835 Enable code mode interruption by default @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51847 Preserve Cargo package names in Bazel Rust builds @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51848 Align Bazel release builds with Cargo and fix platform compatibility
      @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51850 Add Bazel release staging archives @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51855 Add Bazel support to the Codex package build action @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51856 Build Bazel release artifacts alongside Cargo artifacts @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51857 Add an app-server prompt prefix compatibility test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51866 Preserve line breaks and links in multiline async questions @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51868 Record tool registration metrics for each sampling request @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51872 Keep global app-server config independent of the launch directory
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51892 Preserve tool call completeness when recorded arguments are truncated
      @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51893 Record metrics for incremental tool updates @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51895 Report specific reasons for WebSocket continuation failures @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51897 Use a dedicated matcher for network domain policies @rafael-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51908 Honor the user input setting for asynchronous questions @mandal-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52048 Cover instant interruption in steered-input persistence tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52061 Run Guardian conversation classifiers concurrently and preserve
      action order @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52065 Require assessment text in the Guardian parser @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52176 Show AWS GovCloud guidance at startup and remember acknowledgment
      @jackz100'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52178 Strip symbols from source-built release package binaries @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52203 Expose Codex lifecycle status in iTerm2 sessions @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52213 Stop bundling patched zsh in Codex packages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52223 Enforce application network policy for daemon updates @jackz100'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52225 Fix config rebuild call in the Windows MXC preference test @virajrai-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52226 Include foreground activity in iTerm2 session status @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52234 Support request IDs in exec-server WebSocket handshakes @mattj-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52235 Recover gRPC code-mode sessions after missing-session errors @surajs-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52245 Enable parallel execution for read-only tools @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52256 Normalize formatting in docs, web assets, and sample scripts @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52268 Preserve large arguments in executed tool call metadata @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52273 Add configurable persistent leader shortcuts to the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52274 Add structured tracing for Guardian reviews and background scoring
      @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52277 Preserve UTF-8 byte semantics in network domain matching @rafael-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52278 Honor custom OTLP metrics exporters when analytics is disabled
      @jackz100'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52288 Remove duplicate field initializers from extension registry tests
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52295 Emit one developer notice per incremental namespace update batch
      @akira-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52299 Make Bazel release jobs advisory @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52302 Add opt-in credential masking for proxied sandboxed sessions @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52325 Track history initialization in Responses turn metadata @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52329 Remove per-content source attribution metadata @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52337 Add durable thread read state with revision-checked updates @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52350 Expose experimental durable thread read state in the app server
      @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52381 Preserve per-session routing for gRPC code mode @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52384 Notify subscribers when thread read state changes @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52395 Add experimental app-server thread read-state updates @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52418 Avoid an extra blank quote line when pasting text with a trailing
      newline @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52568 Expose message board permissions and structured denials @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52591 Fix races in remote environment and session replacement tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52608 Upgrade `hyper` to 1.11.1 and test connection closure @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52629 Consolidate local message board storage helpers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52635 Skip background workspace routing reads without ChatGPT auth @joesavona'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52637 Add experimental thread item lookup by ID @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52640 Count interrupted goal continuations toward the no-activity limit
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52648 Limit daemon feature compatibility checks to explicit CLI overrides
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52652 Bound local exec-server output draining after process exit @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52671 Add retention annotations to submitted tool outputs @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52676 Refresh persisted capability roots from owner-provided configuration
      @teddywyly-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52679 Add timeout-aware exec-server configuration reads @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52681 Reject reserved Serde JSON keys in code mode @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52685 Preserve code mode cancellation during output serialization @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52686 Add opt-in retention for turn tool outputs @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52689 Forward per-turn Cyber access programs to Guardian @daneschneider-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52700 Update the exec-server stable compatibility baseline to Codex 0.162.1
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52702 Retry bootstrap GETs through the system proxy after request failures
      @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52721 Explain session creation failures during server shutdown @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52723 Add opt-in gRPC over stdio for the code-mode host @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52724 Add observers for initial exec-server connection attempts @aaronl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52742 Add opt-in output token replay for OpenAI requests @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52748 Make code-mode `exit()` stop the entire cell @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52778 Make pinned transcript prompts clickable @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52825 Report exec runtime resets before accepting further requests @JenZhao'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52923 Stabilize the realtime steering timeline test @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52952 Verify reset notification during code-mode host recovery @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52959 Reduce stack usage in async TUI tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52964 Defer owned transcript redraws during raw paste bursts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52972 Upgrade `rmcp` to `3.5.1` and harden lifecycle tests @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52990 Add a searchable `/config` preferences panel to the TUI @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53049 Add connection-bound reply handles for app-server requests @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53148 Fix startup draft recovery for pending Vim Replace keys @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53150 Restore thread-owned permissions on cold resume @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53152 Allow selecting and copying TUI turn tips @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53155 Keep remote app-server events deliverable during shutdown @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53173 Allow restarting managed background servers from the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53224 Support Windows clipboard text paste shortcuts in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53331 Finish remote exec cleanup when output streams remain open @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53339 Test final polling of remote processes with open output streams
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53382 Ignore the unsafe-libyaml advisory in dependency audits @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53400 Add explicit local board connections with fixed runtime access
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53412 Isolate arg0 helper directories by operating system @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53419 Restore saved thread permissions during configuration loading @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53424 Add regression coverage for network grants on cold thread resume
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53426 Preserve Windows runtime registration failure diagnostics @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53436 Route TUI request replies to their originating connection and thread
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53443 Use local MSVC toolchains for native Windows Bazel tests @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53444 Suppress repeated turn diffs in `codex exec` human output @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53452 Close input admission while a turn finishes recording @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53485 Update `quinn-proto` to 0.11.18 @smurching-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53496 Preserve pending Effects toggles across save refreshes @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53506 Reject duplicate Host headers in the network proxy @jfoo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53622 Preserve remote exec output until it is collected @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53628 Record truncation metrics for accepted Guardian review inputs @ioanbudea-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53631 Materialize the thread before testing a discovered daemon restart
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53633 Add an environment API key fallback for Guardian Decisions @swastik-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53654 Keep spawned children provisional until the spawn result returns
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53668 Improve remote exec-server test startup diagnostics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53670 Account for token usage from incomplete responses @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53673 Publish Rust releases with the GitHub CLI @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53698 Interrupt and drain canceled classifier responses before socket
      reuse @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53699 Cancel Guardian V2 classifications that exceed the tool-call lag
      window @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53701 Enable CLI Daybreak by default and enforce background-turn eligibility
      @julee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53717 Enable Cyber access programs for API-key sessions by default @julee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53723 Wire V2 capability discovery through exec-server RPC @TAFOYA-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 134-other-changes-in-rust-v0-163-0
  source_release: codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6
  source_type: github_releases
  theme: uncategorized
  title: 134 other changes in rust-v0.163.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6]]'
source_type: github_releases
theme: uncategorized
title: 134 other changes in rust-v0.163.0
type: change
---

<!-- chronolog:begin region="header" -->
# 134 other changes in rust-v0.163.0

**Codex CLI** · 2026-10-15 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.163.0) · from [[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|0.163.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Open `/config` to search preferences across categories, change supported settings immediately, and see which changes require a restart. (#52990, #53429)

> Send a follow-up while Codex is responding to steer it immediately. Interrupting a turn also stops active Code Mode cells and their nested tool calls. (#51812, #51835)

> Restart a managed background server from `/daemon`. Codex warns about work the restart could interrupt, then reconnects automatically. (#53173)

> Daybreak is enabled by default for eligible accounts. `codex exec` can also select it with an OpenAI API key when the server offers access. (#53701, #53717)

> Resuming a saved thread restores its permissions and network approvals, while respecting explicit overrides and current managed policy. (#53150, #53419, #53424)

> Return to an existing side conversation with `/side` after switching threads. Answers to pending prompts also go back to the thread that asked. (#52184, #53436)

> Local commands finish promptly when a child keeps an output pipe open. Remote commands preserve late-arriving output so the final poll can still collect it. (#52652, #53331, #53622)

> #51556 Complete dynamic tool lifecycles on cancellation @mikelam-oai

> #51575 Expose package assembly helpers and support gzip DotSlash artifacts @bolinfest

> #51595 Add thread ID exclusions to `thread/list` @btraut-openai

> #51602 Distinguish thread listing failures from exhausted history @btraut-openai

> #51650 Require hostname authorization before proxy DNS lookups @jif-oai

> #51651 Persist Guardian review failures for reports across restarts @jif-oai

> #51683 Roll back stale Guardian reviews before reusing reviewer history @olliem-oai

> #51690 Add a feature flag for Code Mode tool description ordering @swastik-oai

> #51704 Honor tool-description-first ordering in Code Mode @swastik-oai

> #51710 Fix a discovery race in the external auth refresh test @jgershen-oai

> #51761 Reduce tool metadata cloning in the code-mode runtime @akira-oai

> #51775 Prevent recursive Tokio tracing in telemetry and SQLite logs @zbarsky-openai

> #51800 Remove duplicate field initializers in extension registry tests @anp-oai

> #51812 Enable instant interrupts by default @pakrym-oai

> #51828 Add policy-based file contents integrity checks @iceweasel-oai

> #51835 Enable code mode interruption by default @won-openai

> #51847 Preserve Cargo package names in Bazel Rust builds @dkovalenko-oai

> #51848 Align Bazel release builds with Cargo and fix platform compatibility @dkovalenko-oai

> #51850 Add Bazel release staging archives @dkovalenko-oai

> #51855 Add Bazel support to the Codex package build action @dkovalenko-oai

> #51856 Build Bazel release artifacts alongside Cargo artifacts @dkovalenko-oai

> #51857 Add an app-server prompt prefix compatibility test @jif-oai

> #51866 Preserve line breaks and links in multiline async questions @pash-openai

> #51868 Record tool registration metrics for each sampling request @akira-oai

> #51872 Keep global app-server config independent of the launch directory @etraut-openai

> #51892 Preserve tool call completeness when recorded arguments are truncated @ningyi-oai

> #51893 Record metrics for incremental tool updates @akira-oai

> #51895 Report specific reasons for WebSocket continuation failures @pakrym-oai

> #51897 Use a dedicated matcher for network domain policies @rafael-oai

> #51908 Honor the user input setting for asynchronous questions @mandal-OAI

> #52048 Cover instant interruption in steered-input persistence tests @jif-oai

> #52061 Run Guardian conversation classifiers concurrently and preserve action order @felixxia-oai

> #52065 Require assessment text in the Guardian parser @ioanbudea-OAI

> #52176 Show AWS GovCloud guidance at startup and remember acknowledgment @jackz100

> #52178 Strip symbols from source-built release package binaries @bolinfest

> #52203 Expose Codex lifecycle status in iTerm2 sessions @fcoury-oai

> #52213 Stop bundling patched zsh in Codex packages @jif-oai

> #52223 Enforce application network policy for daemon updates @jackz100

> #52225 Fix config rebuild call in the Windows MXC preference test @virajrai-oai

> #52226 Include foreground activity in iTerm2 session status @fcoury-oai

> #52234 Support request IDs in exec-server WebSocket handshakes @mattj-openai

> #52235 Recover gRPC code-mode sessions after missing-session errors @surajs-oai

> #52245 Enable parallel execution for read-only tools @zamoshchin-openai

> #52256 Normalize formatting in docs, web assets, and sample scripts @anp-oai

> #52268 Preserve large arguments in executed tool call metadata @ningyi-oai

> #52273 Add configurable persistent leader shortcuts to the TUI @fcoury-oai

> #52274 Add structured tracing for Guardian reviews and background scoring @ioanbudea-OAI

> #52277 Preserve UTF-8 byte semantics in network domain matching @rafael-oai

> #52278 Honor custom OTLP metrics exporters when analytics is disabled @jackz100

> #52288 Remove duplicate field initializers from extension registry tests @anp-oai

> #52295 Emit one developer notice per incremental namespace update batch @akira-oai

> #52299 Make Bazel release jobs advisory @anp-oai

> #52302 Add opt-in credential masking for proxied sandboxed sessions @winston-openai

> #52325 Track history initialization in Responses turn metadata @anp-oai

> #52329 Remove per-content source attribution metadata @anp-oai

> #52337 Add durable thread read state with revision-checked updates @btraut-openai

> #52350 Expose experimental durable thread read state in the app server @btraut-openai

> #52381 Preserve per-session routing for gRPC code mode @cassirer-openai

> #52384 Notify subscribers when thread read state changes @btraut-openai

> #52395 Add experimental app-server thread read-state updates @btraut-openai

> #52418 Avoid an extra blank quote line when pasting text with a trailing newline @bc-openai

> #52568 Expose message board permissions and structured denials @jif-oai

> #52591 Fix races in remote environment and session replacement tests @jif-oai

> #52608 Upgrade `hyper` to 1.11.1 and test connection closure @jif-oai

> #52629 Consolidate local message board storage helpers @jif-oai

> #52635 Skip background workspace routing reads without ChatGPT auth @joesavona

> #52637 Add experimental thread item lookup by ID @btraut-openai

> #52640 Count interrupted goal continuations toward the no-activity limit @etraut-openai

> #52648 Limit daemon feature compatibility checks to explicit CLI overrides @etraut-openai

> #52652 Bound local exec-server output draining after process exit @jif-oai

> #52671 Add retention annotations to submitted tool outputs @won-openai

> #52676 Refresh persisted capability roots from owner-provided configuration @teddywyly-oai

> #52679 Add timeout-aware exec-server configuration reads @hlevy-openai

> #52681 Reject reserved Serde JSON keys in code mode @cassirer-openai

> #52685 Preserve code mode cancellation during output serialization @cassirer-openai

> #52686 Add opt-in retention for turn tool outputs @won-openai

> #52689 Forward per-turn Cyber access programs to Guardian @daneschneider-oai

> #52700 Update the exec-server stable compatibility baseline to Codex 0.162.1 @iceweasel-oai

> #52702 Retry bootstrap GETs through the system proxy after request failures @abhinav-oai

> #52721 Explain session creation failures during server shutdown @etraut-openai

> #52723 Add opt-in gRPC over stdio for the code-mode host @cconger

> #52724 Add observers for initial exec-server connection attempts @aaronl-openai

> #52742 Add opt-in output token replay for OpenAI requests @pakrym-oai

> #52748 Make code-mode `exit()` stop the entire cell @cconger

> #52778 Make pinned transcript prompts clickable @fcoury-oai

> #52825 Report exec runtime resets before accepting further requests @JenZhao

> #52923 Stabilize the realtime steering timeline test @anp-oai

> #52952 Verify reset notification during code-mode host recovery @etraut-openai

> #52959 Reduce stack usage in async TUI tests @jif-oai

> #52964 Defer owned transcript redraws during raw paste bursts @etraut-openai

> #52972 Upgrade `rmcp` to `3.5.1` and harden lifecycle tests @alishobeiri-oai

> #52990 Add a searchable `/config` preferences panel to the TUI @fcoury-oai

> #53049 Add connection-bound reply handles for app-server requests @bc-openai

> #53148 Fix startup draft recovery for pending Vim Replace keys @etraut-openai

> #53150 Restore thread-owned permissions on cold resume @etraut-openai

> #53152 Allow selecting and copying TUI turn tips @etraut-openai

> #53155 Keep remote app-server events deliverable during shutdown @etraut-openai

> #53173 Allow restarting managed background servers from the TUI @etraut-openai

> #53224 Support Windows clipboard text paste shortcuts in the TUI @etraut-openai

> #53331 Finish remote exec cleanup when output streams remain open @jif-oai

> #53339 Test final polling of remote processes with open output streams @jif-oai

> #53382 Ignore the unsafe-libyaml advisory in dependency audits @swastik-oai

> #53400 Add explicit local board connections with fixed runtime access @jif-oai

> #53412 Isolate arg0 helper directories by operating system @jif-oai

> #53419 Restore saved thread permissions during configuration loading @jif-oai

> #53424 Add regression coverage for network grants on cold thread resume @jif-oai

> #53426 Preserve Windows runtime registration failure diagnostics @zm-oai

> #53436 Route TUI request replies to their originating connection and thread @bc-openai

> #53443 Use local MSVC toolchains for native Windows Bazel tests @etraut-openai

> #53444 Suppress repeated turn diffs in `codex exec` human output @fcoury-oai

> #53452 Close input admission while a turn finishes recording @etraut-openai

> #53485 Update `quinn-proto` to 0.11.18 @smurching-oai

> #53496 Preserve pending Effects toggles across save refreshes @fcoury-oai

> #53506 Reject duplicate Host headers in the network proxy @jfoo-oai

> #53622 Preserve remote exec output until it is collected @jif-oai

> #53628 Record truncation metrics for accepted Guardian review inputs @ioanbudea-OAI

> #53631 Materialize the thread before testing a discovered daemon restart @jif-oai

> #53633 Add an environment API key fallback for Guardian Decisions @swastik-oai

> #53654 Keep spawned children provisional until the spawn result returns @jif-oai

> #53668 Improve remote exec-server test startup diagnostics @jif-oai

> #53670 Account for token usage from incomplete responses @jif-oai

> #53673 Publish Rust releases with the GitHub CLI @jif-oai

> #53698 Interrupt and drain canceled classifier responses before socket reuse @felixxia-oai

> #53699 Cancel Guardian V2 classifications that exceed the tool-call lag window @felixxia-oai

> #53701 Enable CLI Daybreak by default and enforce background-turn eligibility @julee-oai

> #53717 Enable Cyber access programs for API-key sessions by default @julee-oai

> #53723 Wire V2 capability discovery through exec-server RPC @TAFOYA-OAI

Source: https://github.com/openai/codex/releases/tag/rust-v0.163.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-15-3-mobile-and-desktop-changes-in-rust-v0-163-0|3 Mobile and Desktop changes in rust-v0.163.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-15-6-model-support-changes-in-rust-v0-163-0|6 Model Support changes in rust-v0.163.0]] · Model Support
- [[Changes/Codex CLI/2026-10-15-15-apps-and-integrations-changes-in-rust-v0-163-0|15 Apps and Integrations changes in rust-v0.163.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-15-18-safety-and-privacy-changes-in-rust-v0-163-0|18 Safety and Privacy changes in rust-v0.163.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-15-4-collaboration-changes-in-rust-v0-163-0|4 Collaboration changes in rust-v0.163.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-15-codex-can-run-independent-read-only-tools-in-parallel-including-skill-memory-and|Codex can run independent read-only tools in parallel, including skill, memory…]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-15-15-developer-workflow-changes-in-rust-v0-163-0|15 Developer Workflow changes in rust-v0.163.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-15-4-voice-and-audio-changes-in-rust-v0-163-0|4 Voice and Audio changes in rust-v0.163.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-15-4-editor-experience-changes-in-rust-v0-163-0|4 Editor Experience changes in rust-v0.163.0]] · Editor Experience
- [[Changes/Codex CLI/2026-10-15-16-context-window-changes-in-rust-v0-163-0|16 Context Window changes in rust-v0.163.0]] · Context Window
- [[Changes/Codex CLI/2026-10-15-8-interface-experience-changes-in-rust-v0-163-0|8 Interface Experience changes in rust-v0.163.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-15-14-agent-mode-changes-in-rust-v0-163-0|14 Agent Mode changes in rust-v0.163.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-15-53389-use-cached-login-credentials-for-guardian-decisions-swastik-oai|♯53389 Use cached login credentials for Guardian decisions @swastik-oai]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-15-36cdbf&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-15-134-other-changes-in-rust-v0-163-0.md%0ACard%20ID%3A%20codex-cli-2026-10-15-36cdbf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.163.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->