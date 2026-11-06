---
card_id: codex-cli-2026-03-26-b67af2
date: '2026-03-26'
description: 'Codex CLI · 2026-03-26 · Other changes: 117 changes in 0.117.0 — Prompt
  history recall now works in the app-server TUI, including across sessions. (#14945)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7ce11639802f89c950cdaea826fa4623f2f3496db2464125078e5993f6e95618
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-26-b67af2
  comparison: ''
  date: '2026-03-26'
  description: 'Codex CLI — 0.117.0: 117 other changes'
  evidence:
  - quote: Prompt history recall now works in the app-server TUI, including across
      sessions. (#14945)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: 'Linux sandboxed tool calls are more reliable on older distributions with
      older `bubblewrap`, and Windows restricted-token sandboxing now supports more
      split-policy carveout layouts. (#15693, #14172)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: 'Expanded the app-server and exec-server docs/schema fixtures to cover
      exec-server setup, filesystem watch RPCs, realtime transcript notifications,
      and the new Python `thread.run(...)` quickstart flow. (#15089, #14533, #15344,
      #15088)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: 'Removed the legacy artifact tool and retired the old `read_file` and `grep_files`
      handlers as part of ongoing tool-surface cleanup. (#15851, #15864, #15773, #15775)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15092 fix: try to fix "Stage npm package" step in ci.yml @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15075 Propagate tool errors to code mode @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15072 Return image URL from view_image tool @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15076 Add a startup deprecation warning for custom prompts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15077 Add final message prefix to realtime handoff output @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#13494 Align SQLite feedback logs with feedback formatter @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15111 don''t add transcript for v2 realtime @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15103 Add update_plan code mode result @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15100 Add apply_patch code mode result @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15089 Add exec-server stub server and protocol docs @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15119 Remove stdio transport from exec server @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14632 feat(core, tracing): create turn spans over websockets @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14970 Simple directory mentions @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14988 Add thread/shellCommand to app server API surface @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15125 Move environment abstraction into exec server @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15180 chore: add metrics for profile @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15196 Add experimental exec server URL handling @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15198 Publish runnable DotSlash package for argument-comment lint @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15090 Add exec-server process and filesystem RPCs @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15201 Log automated reviewer approval sources distinctly @gabec-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15206 feat(tracing): tag app-server turn spans with turn_id @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15154 adding full imagepath to tui @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15220 feat(app-server): add mcpServer/startupStatus/updated notification
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15222 changed save directory to codex_home @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15232 Refactor ExecServer filesystem split between local and remote @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15021 V8 Bazel Build @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15254 core: add a full-buffer exec capture policy @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15253 Split features into codex-features crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15233 Split exec process into local and remote implementations @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15199 Use released DotSlash package for argument-comment lint @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15215 Initial plugins TUI menu - list and read only. tui + tui_app_server
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15262 Add guardian follow-up reminder @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15218 Add temporary app-server originator fallback for codex-tui @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15328 try to fix bazel @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15324 Add remote test skill @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15337 Bump aws-lc-rs @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15203 Add v8-poc consumer of our new built v8 @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15128 chore(core) Remove Feature::PowershellUtf8 @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15344 Add realtime transcript notification in v2 @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15285 Gate tui /plugins menu behind flag @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15114 fix: allow restricted filesystem profiles to read helper executables
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15231 chore(core) update prefix_rule guidance @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15276 Code mode on v8 @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15390 Remove legacy app-server notification handling from tui_app_server
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15409 Add JIT entitlement for macosx @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15414 Remove legacy auth and notification handling from tui_app_server
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15415 chore(exec_policy) ExecPolicyRequirementScenario tests @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15464 Remove smart_approvals alias migration @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15317 nit: guard -> registry @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15338 fix: fall back to vendored bubblewrap when system bwrap lacks --argv0
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15520 fix: cargo deny @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15259 tui: queue follow-ups during manual /compact @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15516 Thread guardian Responses API errors into denial rationale @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15378 feat: support disable skills by name. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15529 Unify realtime stop handling in TUI @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15557 fix: main tui @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15426 chore(core) Add approvals reviewer to UserTurn @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15360 fix: build PATH env var using OsString instead of String @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15239 Add fork snapshot modes @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15592 Extract landlock helpers into codex-sandboxing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15478 [codex-cli][app-server] Update self-serve business usage limit
      copy in error returned @dhruvgupta-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15600 move imagegen skill into system skills @dkundel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15613 nit: split v2 wait @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15614 fix: flaky test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15549 Allow global network allowlist wildcard @rreichel3-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15424 Finish moving codex exec to app-server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15484 chore(deps): bump pnpm/action-setup from 4 to 5 @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14777 Bump vedantmgoyal9/winget-releaser from 19e706d4c9121098010096f9c495a70a7518b30f
      to 7bd472be23763def6e16bd06cc8b1cdfab0e2fd5 @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15558 [Codex TUI] - Sort /plugins TUI menu by installed status first,
      alpha second @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15605 [codex] Stabilize compact resume and fork snapshot flaky tests
      @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15093 core: Make FileWatcher reusable @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15647 feat: communication pattern v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15530 chore: stop app-server auth refresh storms after permanent token
      failure @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15660 Hide numeric prefixes on disabled TUI list rows @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15670 tui_app_server: tolerate missing rate limits while logged out @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15572 Move string truncation helpers into codex-utils-string @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14533 app-server: add filesystem watch support @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15689 app-server: Return codex home in initialize response @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15363 fix: keep rmcp-client env vars as OsString @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15351 Expand ~ in MDM workspace write roots @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15548 Extract rollout into its own crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15601 [app-server] Add a method to override feature flags. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15714 Fix stale turn steering fallback in tui_app_server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15766 chore: tty metric @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15775 chore: remove grep_files handler @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15710 Use AbsolutePathBuf for cwd state @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15773 chore: remove read_file handler @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15776 feat: add multi-thread log query @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15744 Extract codex-instructions crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15339 Add non-interactive resume filter option @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15748 Extract codex-analytics crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15707 Clarify codex_home base for MDM path resolution @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14847 feat: add websocket auth for app-server @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15759 fix(tui_app_server): preserve transcript events under backpressure
      @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15749 Extract codex-core-skills crate @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15798 Avoid duplicate auth refreshes in `getAuthStatus` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15785 Add cached environment manager for exec server URL @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15806 Add ReloadUserConfig to tui_app_server @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15810 app-server: Organize app-server to allow more transports @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#14853 Wire remote app-server auth through the client @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15693 fix: fix old system bubblewrap compatibility without falling back
      to vendored bwrap @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15784 feat: replace askama by custom lib @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15851 feat: drop artifact tool and feature @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15861 feat: clean spawn v1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15691 feat: exec-server prep for unified exec @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15864 chore: drop artifacts lib @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15812 core: remove special execve handling for skill scripts @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15869 fix: flaky @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15866 feat: use `ProcessId` in `exec-server` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15839 Fix duplicate /review messages in app-server TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15661 Enable `tui_app_server` feature by default @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15835 fix: box apply_patch test harness futures @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  - quote: '#15813 Add wildcard in the middle test coverage @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.117.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 117-other-changes-in-rust-v0-117-0
  source_release: codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6
  source_type: github_releases
  theme: uncategorized
  title: 117 other changes in rust-v0.117.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6]]'
source_type: github_releases
theme: uncategorized
title: 117 other changes in rust-v0.117.0
type: change
---

<!-- chronolog:begin region="header" -->
# 117 other changes in rust-v0.117.0

**Codex CLI** · 2026-03-26 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.117.0) · from [[Releases/Codex CLI/codex-cli-2026-03-26-rust-v0-117-0-github-302123790-7cb322b6|0.117.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Prompt history recall now works in the app-server TUI, including across sessions. (#14945)

> Linux sandboxed tool calls are more reliable on older distributions with older `bubblewrap`, and Windows restricted-token sandboxing now supports more split-policy carveout layouts. (#15693, #14172)

> Expanded the app-server and exec-server docs/schema fixtures to cover exec-server setup, filesystem watch RPCs, realtime transcript notifications, and the new Python `thread.run(...)` quickstart flow. (#15089, #14533, #15344, #15088)

> Removed the legacy artifact tool and retired the old `read_file` and `grep_files` handlers as part of ongoing tool-surface cleanup. (#15851, #15864, #15773, #15775)

> #15092 fix: try to fix "Stage npm package" step in ci.yml @bolinfest

> #15075 Propagate tool errors to code mode @pakrym-oai

> #15072 Return image URL from view_image tool @pakrym-oai

> #15076 Add a startup deprecation warning for custom prompts @etraut-openai

> #15077 Add final message prefix to realtime handoff output @aibrahim-oai

> #13494 Align SQLite feedback logs with feedback formatter @charley-oai

> #15111 don't add transcript for v2 realtime @aibrahim-oai

> #15103 Add update_plan code mode result @pakrym-oai

> #15100 Add apply_patch code mode result @pakrym-oai

> #15089 Add exec-server stub server and protocol docs @starr-openai

> #15119 Remove stdio transport from exec server @pakrym-oai

> #14632 feat(core, tracing): create turn spans over websockets @owenlin0

> #14970 Simple directory mentions @canvrno-oai

> #14988 Add thread/shellCommand to app server API surface @etraut-openai

> #15125 Move environment abstraction into exec server @pakrym-oai

> #15180 chore: add metrics for profile @jif-oai

> #15196 Add experimental exec server URL handling @pakrym-oai

> #15198 Publish runnable DotSlash package for argument-comment lint @bolinfest

> #15090 Add exec-server process and filesystem RPCs @starr-openai

> #15201 Log automated reviewer approval sources distinctly @gabec-openai

> #15206 feat(tracing): tag app-server turn spans with turn_id @owenlin0

> #15154 adding full imagepath to tui @won-openai

> #15220 feat(app-server): add mcpServer/startupStatus/updated notification @owenlin0

> #15222 changed save directory to codex_home @won-openai

> #15232 Refactor ExecServer filesystem split between local and remote @pakrym-oai

> #15021 V8 Bazel Build @cconger

> #15254 core: add a full-buffer exec capture policy @bolinfest

> #15253 Split features into codex-features crate @aibrahim-oai

> #15233 Split exec process into local and remote implementations @starr-openai

> #15199 Use released DotSlash package for argument-comment lint @bolinfest

> #15215 Initial plugins TUI menu - list and read only. tui + tui_app_server @canvrno-oai

> #15262 Add guardian follow-up reminder @charley-oai

> #15218 Add temporary app-server originator fallback for codex-tui @etraut-openai

> #15328 try to fix bazel @jif-oai

> #15324 Add remote test skill @pakrym-oai

> #15337 Bump aws-lc-rs @cconger

> #15203 Add v8-poc consumer of our new built v8 @cconger

> #15128 chore(core) Remove Feature::PowershellUtf8 @dylan-hurd-oai

> #15344 Add realtime transcript notification in v2 @aibrahim-oai

> #15285 Gate tui /plugins menu behind flag @canvrno-oai

> #15114 fix: allow restricted filesystem profiles to read helper executables @celia-oai

> #15231 chore(core) update prefix_rule guidance @dylan-hurd-oai

> #15276 Code mode on v8 @cconger

> #15390 Remove legacy app-server notification handling from tui_app_server @etraut-openai

> #15409 Add JIT entitlement for macosx @cconger

> #15414 Remove legacy auth and notification handling from tui_app_server @etraut-openai

> #15415 chore(exec_policy) ExecPolicyRequirementScenario tests @dylan-hurd-oai

> #15464 Remove smart_approvals alias migration @charley-oai

> #15317 nit: guard -> registry @jif-oai

> #15338 fix: fall back to vendored bubblewrap when system bwrap lacks --argv0 @bolinfest

> #15520 fix: cargo deny @jif-oai

> #15259 tui: queue follow-ups during manual /compact @charley-oai

> #15516 Thread guardian Responses API errors into denial rationale @charley-oai

> #15378 feat: support disable skills by name. @xl-openai

> #15529 Unify realtime stop handling in TUI @aibrahim-oai

> #15557 fix: main tui @jif-oai

> #15426 chore(core) Add approvals reviewer to UserTurn @dylan-hurd-oai

> #15360 fix: build PATH env var using OsString instead of String @bolinfest

> #15239 Add fork snapshot modes @charley-oai

> #15592 Extract landlock helpers into codex-sandboxing @pakrym-oai

> #15478 [codex-cli][app-server] Update self-serve business usage limit copy in error returned @dhruvgupta-oai

> #15600 move imagegen skill into system skills @dkundel-openai

> #15613 nit: split v2 wait @jif-oai

> #15614 fix: flaky test @jif-oai

> #15549 Allow global network allowlist wildcard @rreichel3-oai

> #15424 Finish moving codex exec to app-server @etraut-openai

> #15484 chore(deps): bump pnpm/action-setup from 4 to 5 @dependabot

> #14777 Bump vedantmgoyal9/winget-releaser from 19e706d4c9121098010096f9c495a70a7518b30f to 7bd472be23763def6e16bd06cc8b1cdfab0e2fd5 @dependabot

> #15558 [Codex TUI] - Sort /plugins TUI menu by installed status first, alpha second @canvrno-oai

> #15605 [codex] Stabilize compact resume and fork snapshot flaky tests @charley-oai

> #15093 core: Make FileWatcher reusable @euroelessar

> #15647 feat: communication pattern v2 @jif-oai

> #15530 chore: stop app-server auth refresh storms after permanent token failure @celia-oai

> #15660 Hide numeric prefixes on disabled TUI list rows @canvrno-oai

> #15670 tui_app_server: tolerate missing rate limits while logged out @etraut-openai

> #15572 Move string truncation helpers into codex-utils-string @aibrahim-oai

> #14533 app-server: add filesystem watch support @euroelessar

> #15689 app-server: Return codex home in initialize response @euroelessar

> #15363 fix: keep rmcp-client env vars as OsString @bolinfest

> #15351 Expand ~ in MDM workspace write roots @evawong-oai

> #15548 Extract rollout into its own crate @aibrahim-oai

> #15601 [app-server] Add a method to override feature flags. @mzeng-openai

> #15714 Fix stale turn steering fallback in tui_app_server @etraut-openai

> #15766 chore: tty metric @jif-oai

> #15775 chore: remove grep_files handler @jif-oai

> #15710 Use AbsolutePathBuf for cwd state @pakrym-oai

> #15773 chore: remove read_file handler @jif-oai

> #15776 feat: add multi-thread log query @jif-oai

> #15744 Extract codex-instructions crate @aibrahim-oai

> #15339 Add non-interactive resume filter option @nornagon-openai

> #15748 Extract codex-analytics crate @aibrahim-oai

> #15707 Clarify codex_home base for MDM path resolution @evawong-oai

> #14847 feat: add websocket auth for app-server @viyatb-oai

> #15759 fix(tui_app_server): preserve transcript events under backpressure @fcoury

> #15749 Extract codex-core-skills crate @aibrahim-oai

> #15798 Avoid duplicate auth refreshes in `getAuthStatus` @etraut-openai

> #15785 Add cached environment manager for exec server URL @pakrym-oai

> #15806 Add ReloadUserConfig to tui_app_server @canvrno-oai

> #15810 app-server: Organize app-server to allow more transports @euroelessar

> #14853 Wire remote app-server auth through the client @etraut-openai

> #15693 fix: fix old system bubblewrap compatibility without falling back to vendored bwrap @viyatb-oai

> #15784 feat: replace askama by custom lib @jif-oai

> #15851 feat: drop artifact tool and feature @jif-oai

> #15861 feat: clean spawn v1 @jif-oai

> #15691 feat: exec-server prep for unified exec @jif-oai

> #15864 chore: drop artifacts lib @jif-oai

> #15812 core: remove special execve handling for skill scripts @bolinfest

> #15869 fix: flaky @jif-oai

> #15866 feat: use `ProcessId` in `exec-server` @jif-oai

> #15839 Fix duplicate /review messages in app-server TUI @etraut-openai

> #15661 Enable `tui_app_server` feature by default @etraut-openai

> #15835 fix: box apply_patch test harness futures @bolinfest

> #15813 Add wildcard in the middle test coverage @evawong-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.117.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-26-19-developer-workflow-changes-in-rust-v0-117-0|19 Developer Workflow changes in rust-v0.117.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-26-15789-treat-chatgpt-hc-plan-as-enterprise-arnavdugar-openai|♯15789 Treat ChatGPT hc plan as Enterprise @arnavdugar-openai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-26-the-app-server-backed-tui-is-now-enabled-by-default-and-the-plugin-app-rollout-f|The app-server-backed TUI is now enabled by default, and the plugin/app rollout…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-plugins-are-now-a-first-class-workflow-codex-can-sync-product-scoped-plugins-at|Plugins are now a first-class workflow]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-26-2-image-generation-changes-in-rust-v0-117-0|2 Image Generation changes in rust-v0.117.0]] · Image Generation
- [[Changes/Codex CLI/2026-03-26-15579-increase-voice-space-hold-timeout-to-1s-aibrahim-oai|♯15579 Increase voice space hold timeout to 1s @aibrahim-oai]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-26-2-automation-and-scheduling-changes-in-rust-v0-117-0|2 Automation and Scheduling changes in rust-v0.117.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-26-5-context-window-changes-in-rust-v0-117-0|5 Context Window changes in rust-v0.117.0]] · Context Window
- [[Changes/Codex CLI/2026-03-26-14945-feat-tui-restore-composer-history-in-app-server-tui-fcoury|♯14945 feat(tui): restore composer history in app-server tui @fcoury]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-03-26-15480-use-shift-left-to-edit-queued-messages-in-tmux-charley-oai|♯15480 Use Shift+Left to edit queued messages in tmux @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-03-26-3-interface-experience-changes-in-rust-v0-117-0|3 Interface Experience changes in rust-v0.117.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-26-4-account-and-access-changes-in-rust-v0-117-0|4 Account and Access changes in rust-v0.117.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-26-19-agent-mode-changes-in-rust-v0-117-0|19 Agent Mode changes in rust-v0.117.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-26-57-apps-and-integrations-changes-in-rust-v0-117-0|57 Apps and Integrations changes in rust-v0.117.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-26-3-mobile-and-desktop-changes-in-rust-v0-117-0|3 Mobile and Desktop changes in rust-v0.117.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-26-3-model-support-changes-in-rust-v0-117-0|3 Model Support changes in rust-v0.117.0]] · Model Support
- [[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175 chore: morpheus does not generate memories @jif-oai]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-26-b67af2&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-26-117-other-changes-in-rust-v0-117-0.md%0ACard%20ID%3A%20codex-cli-2026-03-26-b67af2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.117.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->