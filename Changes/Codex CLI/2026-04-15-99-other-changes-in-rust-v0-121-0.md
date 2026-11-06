---
card_id: codex-cli-2026-04-15-a087c6
date: '2026-04-15'
description: 'Codex CLI · 2026-04-15 · Other changes: 99 changes in 0.121.0 — Added
  TUI prompt history improvements, including `Ctrl+R` reverse search and local recall
  for…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e760671e2f4f20801faadc534f7df69938daa4b0e97d079bb90d463296efe15f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-15-a087c6
  comparison: ''
  date: '2026-04-15'
  description: 'Codex CLI — 0.121.0: 99 other changes'
  evidence:
  - quote: 'Added TUI prompt history improvements, including `Ctrl+R` reverse search
      and local recall for accepted slash commands (#17550, #17336).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Made Guardian timeouts distinct from policy denials, with timeout-specific
      guidance and visible TUI history entries (#17381, #17486, #17521, #17557).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Stabilized app-server behavior by avoiding premature thread unloads, tolerating
      failed trust persistence on startup, and skipping broken symlinks in `fs/readDirectory`
      (#17398, #17595, #17907).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Documented the secure devcontainer profile and its bubblewrap requirements
      (#10431, #17547).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: Added TUI composer documentation for history search behavior (#17550).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: Documented WSL1 bubblewrap limitations and WSL2 behavior (#17559).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Added Bazel release-build verification so release-only Rust code is compiled
      in PR CI (#17704, #17705).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Introduced the `codex-thread-store` crate/interface and moved local thread
      listing behind it (#17659, #17824).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: Required reviewed pnpm dependency build scripts for workspace installs
      (#17558).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: 'Reduced Rust maintenance surface with broader absolute-path types and
      removal of unused helper APIs (#17407, #17792, #17146).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17409 Fix Windows exec-server output test flake @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17381 representing guardian review timeouts in protocol types @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17399 TUI: enforce core boundary @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17396 update cloud requirements parse failure msg @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17424 Stabilize marketplace add local source test @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#10431 feat(devcontainer): add separate secure customer profile @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17314 Pass turn id with feedback uploads @ningyi-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17336 fix(tui): recall accepted slash commands locally @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17430 Handle closed TUI input stream as shutdown @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17493 fix @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17419 Support prolite plan type @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17416 Clear /ps after /stop @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17415 Restore codex-tui resume hint on exit @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17402 chore: refactor name and namespace to single type @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17486 changing decision semantics after guardian timeout @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17521 Clarify guardian timeout guidance @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17547 [codex] Support bubblewrap in secure Docker devcontainer @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17558 build(pnpm): require reviewed dependency build scripts @mcgrew-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17559 fix(sandboxing): reject WSL1 bubblewrap sandboxing @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17520 Mirror user text into realtime @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17550 feat(tui): add reverse history search to composer @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17605 Stabilize exec-server process tests @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17221 feat: ignore keyring on 0.0.0 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17216 Build remote exec env from exec-server policy @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17643 fix: dedup compact @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17470 Fix custom tool output cleanup on stream failure @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17417 Emit plan-mode prompt notifications for questionnaires @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17481 Wrap status reset timestamps in narrow layouts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17595 Do not fail thread start when trust persistence fails @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17407 Use AbsolutePathBuf in skill loading and codex_home @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17638 feat: Avoid reloading curated marketplaces for tool-suggest discovera…
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17398 app-server: Only unload threads which were unused for some time
      @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17669 only specify remote ports when the rule needs them @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17691 Fix tui compilation @davidhao3300'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17395 Remove unnecessary tests @kliu128'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17685 Cap realtime mirrored user turns @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17699 change realtime tool description @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17667 Add `supports_parallel_tool_calls` flag to included mcps @josiah-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17703 Add turn item injection API @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17671 Stabilize exec-server filesystem tests in CI @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17557 guardian timeout fix pr 3 - ux touch for timeouts @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17719 [codex] Add symlink flag to fs metadata @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17146 [codex] Remove unused Rust helpers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17471 fix: pin inputs @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17709 [codex] Initialize ICU data for code mode V8 @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17749 [codex] drain mailbox only at request boundaries @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#16640 [codex-analytics] feature plumbing and emittance @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17761 Tighten realtime handoff finalization @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17701 Add realtime output modality and transcript events @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17777 nit: feature flag @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17374 [codex-analytics] add session source to client metadata @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17489 Moving updated-at timestamps to unique millisecond times @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17784 feat: codex sampler @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17732 fix: Revert danger-full-access denylist-only mode @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17803 Keep image_detail_original as a removed feature flag @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17372 app-server: prepare to run initialized rpcs concurrently @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17704 Refactor Bazel CI job setup @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17674 Route apply_patch through the environment filesystem @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17702 Fix remote skill popup loading @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17830 [codex] Fix app-server initialized request analytics build @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17389 [codex-analytics] enable general analytics by default @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17659 thread store interface @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17792 Spread AbsolutePathBuf @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17808 fix: apply patch bin refresh @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17838 Add realtime wire trace logs @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17705 Add Bazel verify-release-build job @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17720 Make skill loading filesystem-aware @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17756 [codex] Support local marketplace sources @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17846 Fix for Guardian CI Tests stack overflow, applying Box to reduce
      stack pressure @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17868 Wrap delegated input text @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17837 Reuse remote exec-server in core tests @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17870 fix: cleanup the contract of the general-purpose exec() function
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17871 fix: add websocket capability token hash support @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17915 fix: cargo deny @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17921 chore: exp flag @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17917 [codex] Fix current main CI blockers @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17924 nit: stable test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17941 nit: doc @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17938 feat: sanitize rollouts before phase 1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17907 Fix fs/readDirectory to skip broken symlinks @willwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17960 chore(features) codex dependencies feat @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17965 fix: rename is_azure_responses_wire_base_url to is_azure_responses_provider
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17946 Fix empty tool descriptions @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17824 [codex] Add local thread store listing @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17942 Add CLI update announcement @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17866 Refactor auth providers to mutate request headers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17953 fix: propagate log db @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17920 chore(tui) cleanup @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17981 chore: tmp disable @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 99-other-changes-in-rust-v0-121-0
  source_release: codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03
  source_type: github_releases
  theme: uncategorized
  title: 99 other changes in rust-v0.121.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03]]'
source_type: github_releases
theme: uncategorized
title: 99 other changes in rust-v0.121.0
type: change
---

<!-- chronolog:begin region="header" -->
# 99 other changes in rust-v0.121.0

**Codex CLI** · 2026-04-15 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.121.0) · from [[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|0.121.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added TUI prompt history improvements, including `Ctrl+R` reverse search and local recall for accepted slash commands (#17550, #17336).

> Made Guardian timeouts distinct from policy denials, with timeout-specific guidance and visible TUI history entries (#17381, #17486, #17521, #17557).

> Stabilized app-server behavior by avoiding premature thread unloads, tolerating failed trust persistence on startup, and skipping broken symlinks in `fs/readDirectory` (#17398, #17595, #17907).

> Documented the secure devcontainer profile and its bubblewrap requirements (#10431, #17547).

> Added TUI composer documentation for history search behavior (#17550).

> Documented WSL1 bubblewrap limitations and WSL2 behavior (#17559).

> Added Bazel release-build verification so release-only Rust code is compiled in PR CI (#17704, #17705).

> Introduced the `codex-thread-store` crate/interface and moved local thread listing behind it (#17659, #17824).

> Required reviewed pnpm dependency build scripts for workspace installs (#17558).

> Reduced Rust maintenance surface with broader absolute-path types and removal of unused helper APIs (#17407, #17792, #17146).

> #17409 Fix Windows exec-server output test flake @etraut-openai

> #17381 representing guardian review timeouts in protocol types @won-openai

> #17399 TUI: enforce core boundary @etraut-openai

> #17396 update cloud requirements parse failure msg @alexsong-oai

> #17424 Stabilize marketplace add local source test @ningyi-oai

> #10431 feat(devcontainer): add separate secure customer profile @viyatb-oai

> #17314 Pass turn id with feedback uploads @ningyi-oai

> #17336 fix(tui): recall accepted slash commands locally @fcoury-oai

> #17430 Handle closed TUI input stream as shutdown @etraut-openai

> #17493 fix @aibrahim-oai

> #17419 Support prolite plan type @etraut-openai

> #17416 Clear /ps after /stop @etraut-openai

> #17415 Restore codex-tui resume hint on exit @etraut-openai

> #17402 chore: refactor name and namespace to single type @sayan-oai

> #17486 changing decision semantics after guardian timeout @won-openai

> #17521 Clarify guardian timeout guidance @won-openai

> #17547 [codex] Support bubblewrap in secure Docker devcontainer @viyatb-oai

> #17558 build(pnpm): require reviewed dependency build scripts @mcgrew-oai

> #17559 fix(sandboxing): reject WSL1 bubblewrap sandboxing @viyatb-oai

> #17520 Mirror user text into realtime @aibrahim-oai

> #17550 feat(tui): add reverse history search to composer @fcoury-oai

> #17605 Stabilize exec-server process tests @etraut-openai

> #17221 feat: ignore keyring on 0.0.0 @jif-oai

> #17216 Build remote exec env from exec-server policy @jif-oai

> #17643 fix: dedup compact @jif-oai

> #17470 Fix custom tool output cleanup on stream failure @etraut-openai

> #17417 Emit plan-mode prompt notifications for questionnaires @etraut-openai

> #17481 Wrap status reset timestamps in narrow layouts @etraut-openai

> #17595 Do not fail thread start when trust persistence fails @etraut-openai

> #17407 Use AbsolutePathBuf in skill loading and codex_home @pakrym-oai

> #17638 feat: Avoid reloading curated marketplaces for tool-suggest discovera… @jif-oai

> #17398 app-server: Only unload threads which were unused for some time @euroelessar

> #17669 only specify remote ports when the rule needs them @iceweasel-oai

> #17691 Fix tui compilation @davidhao3300

> #17395 Remove unnecessary tests @kliu128

> #17685 Cap realtime mirrored user turns @aibrahim-oai

> #17699 change realtime tool description @aibrahim-oai

> #17667 Add `supports_parallel_tool_calls` flag to included mcps @josiah-openai

> #17703 Add turn item injection API @pakrym-oai

> #17671 Stabilize exec-server filesystem tests in CI @starr-openai

> #17557 guardian timeout fix pr 3 - ux touch for timeouts @won-openai

> #17719 [codex] Add symlink flag to fs metadata @pakrym-oai

> #17146 [codex] Remove unused Rust helpers @pakrym-oai

> #17471 fix: pin inputs @viyatb-oai

> #17709 [codex] Initialize ICU data for code mode V8 @pakrym-oai

> #17749 [codex] drain mailbox only at request boundaries @tibo-openai

> #16640 [codex-analytics] feature plumbing and emittance @rhan-oai

> #17761 Tighten realtime handoff finalization @aibrahim-oai

> #17701 Add realtime output modality and transcript events @aibrahim-oai

> #17777 nit: feature flag @jif-oai

> #17374 [codex-analytics] add session source to client metadata @marksteinbrick-oai

> #17489 Moving updated-at timestamps to unique millisecond times @ddr-oai

> #17784 feat: codex sampler @jif-oai

> #17732 fix: Revert danger-full-access denylist-only mode @viyatb-oai

> #17803 Keep image_detail_original as a removed feature flag @fjord-oai

> #17372 app-server: prepare to run initialized rpcs concurrently @euroelessar

> #17704 Refactor Bazel CI job setup @bolinfest

> #17674 Route apply_patch through the environment filesystem @starr-openai

> #17702 Fix remote skill popup loading @starr-openai

> #17830 [codex] Fix app-server initialized request analytics build @etraut-openai

> #17389 [codex-analytics] enable general analytics by default @rhan-oai

> #17659 thread store interface @wiltzius-openai

> #17792 Spread AbsolutePathBuf @pakrym-oai

> #17808 fix: apply patch bin refresh @jif-oai

> #17838 Add realtime wire trace logs @aibrahim-oai

> #17705 Add Bazel verify-release-build job @bolinfest

> #17720 Make skill loading filesystem-aware @pakrym-oai

> #17756 [codex] Support local marketplace sources @xli-oai

> #17846 Fix for Guardian CI Tests stack overflow, applying Box to reduce stack pressure @won-openai

> #17868 Wrap delegated input text @guinness-oai

> #17837 Reuse remote exec-server in core tests @starr-openai

> #17870 fix: cleanup the contract of the general-purpose exec() function @bolinfest

> #17871 fix: add websocket capability token hash support @viyatb-oai

> #17915 fix: cargo deny @jif-oai

> #17921 chore: exp flag @jif-oai

> #17917 [codex] Fix current main CI blockers @sayan-oai

> #17924 nit: stable test @jif-oai

> #17941 nit: doc @jif-oai

> #17938 feat: sanitize rollouts before phase 1 @jif-oai

> #17907 Fix fs/readDirectory to skip broken symlinks @willwang-openai

> #17960 chore(features) codex dependencies feat @dylan-hurd-oai

> #17965 fix: rename is_azure_responses_wire_base_url to is_azure_responses_provider @bolinfest

> #17946 Fix empty tool descriptions @shijie-oai

> #17824 [codex] Add local thread store listing @wiltzius-openai

> #17942 Add CLI update announcement @shijie-oai

> #17866 Refactor auth providers to mutate request headers @pakrym-oai

> #17953 fix: propagate log db @jif-oai

> #17920 chore(tui) cleanup @dylan-hurd-oai

> #17981 chore: tmp disable @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.121.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-15-3-model-support-changes-in-rust-v0-121-0|3 Model Support changes in rust-v0.121.0]] · Model Support
- [[Changes/Codex CLI/2026-04-15-17684-adjust-default-tool-search-result-caps-malone-oai|♯17684 Adjust default tool search result caps @malone-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-15-9-memory-and-personalization-changes-in-rust-v0-121-0|9 Memory and Personalization changes in rust-v0.121.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-15-9-apps-and-integrations-changes-in-rust-v0-121-0|9 Apps and Integrations changes in rust-v0.121.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-15-4-context-window-changes-in-rust-v0-121-0|4 Context Window changes in rust-v0.121.0]] · Context Window
- [[Changes/Codex CLI/2026-04-15-7-agent-mode-changes-in-rust-v0-121-0|7 Agent Mode changes in rust-v0.121.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-15-4-developer-workflow-changes-in-rust-v0-121-0|4 Developer Workflow changes in rust-v0.121.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-15-17640-fix-stability-exec-server-jif-oai|♯17640 fix: stability exec server @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-15-added-realtime-and-app-server-apis-for-output-modality-transcript-completion-eve|Added realtime and app-server APIs for output modality, transcript completion…]] · Editor Experience
- [[Changes/Codex CLI/2026-04-15-17414-fix-thread-list-cwd-filtering-for-windows-verbatim-paths-etraut-openai|♯17414 Fix thread/list cwd filtering for Windows verbatim paths @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-15-10-safety-and-privacy-changes-in-rust-v0-121-0|10 Safety and Privacy changes in rust-v0.121.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-15-17717-codex-refactor-marketplace-add-into-shared-core-flow-xli-oai|♯17717 codex Refactor marketplace add into shared core flow @xli-oai]] · Collaboration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-15-a087c6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-15-99-other-changes-in-rust-v0-121-0.md%0ACard%20ID%3A%20codex-cli-2026-04-15-a087c6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.121.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->