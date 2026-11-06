---
card_id: codex-cli-2026-04-20-e2ddce
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Other changes: 100 changes in 0.122.0 — Sandboxed
  `apply_patch` writes work correctly with split filesystem policies, and file…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4f47391edadfb0c81c7204c4772d6457fa524d92bbef462ed9731db20a7d3963
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-e2ddce
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 100 other changes'
  evidence:
  - quote: 'Sandboxed `apply_patch` writes work correctly with split filesystem policies,
      and file watchers now notice files created after watching begins (#18296, #18492).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: Added a short guide for the responses API proxy (#18604).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: 'Stabilized Bazel and CI with flake fixes, native Rust test sharding, scoped
      repository caches, stronger Windows clippy coverage, and updated `rules_rs`/LLVM
      pins (#17791, #18082, #18366, #18350, #18397).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: 'Added core CODEOWNERS and a smaller development build profile (#18362,
      #18612).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17990 Auto install start-codex-exec.sh dependencies @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17892 Migrate archive/unarchive to local ThreadStore @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17989 [codex] Restore remote exec-server filesystem tests @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#15134 Dismiss stale app-server requests after remote resolution @ebrevdo'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18002 Re-enable it @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17885 feat: Support alternate marketplace manifests and local string
      @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18003 [docs] Revert extra changes from PR 17848 @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17022 Significantly improve standalone installer @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17742 removing network proxy for yolo @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18033 feat: introduce codex-pr-body skill @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17877 Display YOLO mode permissions if set when launching TUI @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18022 Async config loading @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17854 Update ToolSearch to be enabled by default @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17151 [codex] Route Fed ChatGPT auth through Fed edge @jackz-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18006 fix: more flake @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18127 fix: windows flake @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18138 chore: more pollution filtering @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18144 nit: get rid of an expect @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17791 Stabilize Bazel tests (timeout tweaks and flake fixes) @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18117 fix: auth preflight @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18146 chore: use `justfile_directory` in just file @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18057 Prefill rename prompt with current thread name @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18059 Fix invalid TUI resume hints @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18042 Make yolo skip managed-network tool enforcement @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17826 [codex] Add remote thread store implementation @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18086 [2/8] Support piped stdin in exec process API @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18061 Avoid fatal TUI errors on skills list failure @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#15979 feat(permissions): add glob deny-read policy support @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17425 Auto-upgrade configured marketplaces @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18178 fix: drop lock earlier; was held across send_event().await unnecessarily
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18000 Make thread unsubscribe test deterministic @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17996 Add codex_hook_run analytics event @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18184 fix: fix clippy issue in examples/ folder @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18023 fix(app-server): replay token usage after resume and fork @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18192 Throttle Windows Bazel test concurrency @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18200 [codex] Split codex op handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18026 Add OTEL metrics for hook runs @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18092 [codex] Update realtime V2 VAD silence delay and 1.5 prompt @bxie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18206 [codex] Split codex turn logic @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17971 fix: deprecate use_legacy_landlock feature flag @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18209 Refactor config loading to use filesystem abstraction @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17862 Stream apply_patch changes @akshaynathan'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18244 Split codex session modules @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17713 feat: add opt-in provider runtime abstraction @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18219 Move Computer Use tool suggestion to core @leoshimo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18231 codex: split thread/read view loading @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18126 fix(exec-policy) rules parsing @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18304 Fix Windows exec policy test flake @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17947 fix: reduce writable root @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18097 defer all tools behind feature flag @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18338 nit: phase 2 ephemeral @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17740 feat(config): support managed deny-read requirements @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18249 Move codex module under session @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18351 Fix config-loader tests after filesystem abstraction race @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18140 feat: config aliases @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17232 Make app tool hint defaults pessimistic for app policies @colby-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18352 codex: route thread/read persistence through thread store @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18263 enable tool search over dynamic tools @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18350 ci: make Windows Bazel clippy catch core test imports @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18362 Add core CODEOWNERS @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18366 ci: scope Bazel repository cache by job @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17305 Add sorting/backwardsCursor to thread/list and new thread/turns/list
      api @ddr-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18020 [3/6] Add pushed exec process events @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18379 Attribute automated PR Babysitter review replies @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18370 perf(tui): defer startup skills refresh @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18222 /plugins: Add v2 tabbed marketplace menu @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18227 [codex] Propagate rate limit reached type @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18380 exec-server: preserve fs helper runtime env @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18211 refactor: narrow async lock guard lifetimes @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18397 [codex] Upgrade rules_rs and llvm to latest BCR versions @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18082 bazel: use native rust test sharding @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18384 Update image resizing to fit 2048 square bounds @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17891 [TUI] add external config migration prompt when start TUI @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18298 feat: Budget skill metadata and surface trimming as a warning @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18220 [codex] Add owner nudge app-server API @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18325 Revert "[codex] drain mailbox only at request boundaries" @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18386 Update image outputs to default to high detail @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18524 Add fallback source for external official marketplace @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18571 Log realtime session id @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18190 Add `/side` conversations @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18604 Add tldr docs for responses-api-proxy @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18601 Soften Fast mode plan usage copy @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18596 chore(multiagent) skills instructions toggle @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18599 fix(guardian) disable skills message in guardian thread @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18612 Create dev-small build profile @andmis'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18440 Use thread IDs in TUI resume hints @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18605 TUI: remove simple legacy_core re-exports @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18221 [codex] Add workspace owner usage nudge UI @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17751 [codex] Add marketplace/remove app-server RPC @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18353 chore: morpheus to path @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18649 fix: main 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17721 Stabilize marketplace/remove installedRoot test @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18492 fix: FS watcher when file does not exist yet @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18646 feat: add `--ignore-user-config` and `--ignore-rules` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18652 nit: telepathy to chronicle in tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18651 feat: chronicle alias @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 100-other-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: uncategorized
  title: 100 other changes in rust-v0.122.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: uncategorized
title: 100 other changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 100 other changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sandboxed `apply_patch` writes work correctly with split filesystem policies, and file watchers now notice files created after watching begins (#18296, #18492).

> Added a short guide for the responses API proxy (#18604).

> Stabilized Bazel and CI with flake fixes, native Rust test sharding, scoped repository caches, stronger Windows clippy coverage, and updated `rules_rs`/LLVM pins (#17791, #18082, #18366, #18350, #18397).

> Added core CODEOWNERS and a smaller development build profile (#18362, #18612).

> #17990 Auto install start-codex-exec.sh dependencies @pakrym-oai

> #17892 Migrate archive/unarchive to local ThreadStore @wiltzius-openai

> #17989 [codex] Restore remote exec-server filesystem tests @starr-openai

> #15134 Dismiss stale app-server requests after remote resolution @ebrevdo

> #18002 Re-enable it @jif-oai

> #17885 feat: Support alternate marketplace manifests and local string @xl-openai

> #18003 [docs] Revert extra changes from PR 17848 @evawong-oai

> #17022 Significantly improve standalone installer @efrazer-oai

> #17742 removing network proxy for yolo @won-openai

> #18033 feat: introduce codex-pr-body skill @bolinfest

> #17877 Display YOLO mode permissions if set when launching TUI @canvrno-oai

> #18022 Async config loading @pakrym-oai

> #17854 Update ToolSearch to be enabled by default @mzeng-openai

> #17151 [codex] Route Fed ChatGPT auth through Fed edge @jackz-oai

> #18006 fix: more flake @jif-oai

> #18127 fix: windows flake @jif-oai

> #18138 chore: more pollution filtering @jif-oai

> #18144 nit: get rid of an expect @jif-oai

> #17791 Stabilize Bazel tests (timeout tweaks and flake fixes) @ddr-oai

> #18117 fix: auth preflight @jif-oai

> #18146 chore: use `justfile_directory` in just file @jif-oai

> #18057 Prefill rename prompt with current thread name @etraut-openai

> #18059 Fix invalid TUI resume hints @etraut-openai

> #18042 Make yolo skip managed-network tool enforcement @won-openai

> #17826 [codex] Add remote thread store implementation @wiltzius-openai

> #18086 [2/8] Support piped stdin in exec process API @aibrahim-oai

> #18061 Avoid fatal TUI errors on skills list failure @etraut-openai

> #15979 feat(permissions): add glob deny-read policy support @viyatb-oai

> #17425 Auto-upgrade configured marketplaces @xli-oai

> #18178 fix: drop lock earlier; was held across send_event().await unnecessarily @bolinfest

> #18000 Make thread unsubscribe test deterministic @starr-openai

> #17996 Add codex_hook_run analytics event @abhinav-oai

> #18184 fix: fix clippy issue in examples/ folder @bolinfest

> #18023 fix(app-server): replay token usage after resume and fork @fcoury-oai

> #18192 Throttle Windows Bazel test concurrency @starr-openai

> #18200 [codex] Split codex op handlers @pakrym-oai

> #18026 Add OTEL metrics for hook runs @abhinav-oai

> #18092 [codex] Update realtime V2 VAD silence delay and 1.5 prompt @bxie-openai

> #18206 [codex] Split codex turn logic @pakrym-oai

> #17971 fix: deprecate use_legacy_landlock feature flag @viyatb-oai

> #18209 Refactor config loading to use filesystem abstraction @pakrym-oai

> #17862 Stream apply_patch changes @akshaynathan

> #18244 Split codex session modules @pakrym-oai

> #17713 feat: add opt-in provider runtime abstraction @celia-oai

> #18219 Move Computer Use tool suggestion to core @leoshimo-oai

> #18231 codex: split thread/read view loading @wiltzius-openai

> #18126 fix(exec-policy) rules parsing @dylan-hurd-oai

> #18304 Fix Windows exec policy test flake @etraut-openai

> #17947 fix: reduce writable root @jif-oai

> #18097 defer all tools behind feature flag @sayan-oai

> #18338 nit: phase 2 ephemeral @jif-oai

> #17740 feat(config): support managed deny-read requirements @viyatb-oai

> #18249 Move codex module under session @pakrym-oai

> #18351 Fix config-loader tests after filesystem abstraction race @bolinfest

> #18140 feat: config aliases @jif-oai

> #17232 Make app tool hint defaults pessimistic for app policies @colby-oai

> #18352 codex: route thread/read persistence through thread store @wiltzius-openai

> #18263 enable tool search over dynamic tools @sayan-oai

> #18350 ci: make Windows Bazel clippy catch core test imports @bolinfest

> #18362 Add core CODEOWNERS @aibrahim-oai

> #18366 ci: scope Bazel repository cache by job @bolinfest

> #17305 Add sorting/backwardsCursor to thread/list and new thread/turns/list api @ddr-oai

> #18020 [3/6] Add pushed exec process events @aibrahim-oai

> #18379 Attribute automated PR Babysitter review replies @etraut-openai

> #18370 perf(tui): defer startup skills refresh @fcoury-oai

> #18222 /plugins: Add v2 tabbed marketplace menu @canvrno-oai

> #18227 [codex] Propagate rate limit reached type @richardopenai

> #18380 exec-server: preserve fs helper runtime env @starr-openai

> #18211 refactor: narrow async lock guard lifetimes @bolinfest

> #18397 [codex] Upgrade rules_rs and llvm to latest BCR versions @zbarsky-openai

> #18082 bazel: use native rust test sharding @bolinfest

> #18384 Update image resizing to fit 2048 square bounds @pakrym-oai

> #17891 [TUI] add external config migration prompt when start TUI @alexsong-oai

> #18298 feat: Budget skill metadata and surface trimming as a warning @xl-openai

> #18220 [codex] Add owner nudge app-server API @richardopenai

> #18325 Revert "[codex] drain mailbox only at request boundaries" @jif-oai

> #18386 Update image outputs to default to high detail @pakrym-oai

> #18524 Add fallback source for external official marketplace @alexsong-oai

> #18571 Log realtime session id @aibrahim-oai

> #18190 Add `/side` conversations @etraut-openai

> #18604 Add tldr docs for responses-api-proxy @andmis

> #18601 Soften Fast mode plan usage copy @pash-openai

> #18596 chore(multiagent) skills instructions toggle @dylan-hurd-oai

> #18599 fix(guardian) disable skills message in guardian thread @dylan-hurd-oai

> #18612 Create dev-small build profile @andmis

> #18440 Use thread IDs in TUI resume hints @etraut-openai

> #18605 TUI: remove simple legacy_core re-exports @etraut-openai

> #18221 [codex] Add workspace owner usage nudge UI @richardopenai

> #17751 [codex] Add marketplace/remove app-server RPC @xli-oai

> #18353 chore: morpheus to path @jif-oai

> #18649 fix: main 2 @jif-oai

> #17721 Stabilize marketplace/remove installedRoot test @xli-oai

> #18492 fix: FS watcher when file does not exist yet @jif-oai

> #18646 feat: add `--ignore-user-config` and `--ignore-rules` @jif-oai

> #18652 nit: telepathy to chronicle in tests @jif-oai

> #18651 feat: chronicle alias @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6 Developer Workflow changes in rust-v0.122.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Model Support
- [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]] · Context Window
- [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-20-18398-refactor-use-cloneable-async-channels-for-shared-receivers-bolinfest|♯18398 refactor: use cloneable async channels for shared receivers @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28 Apps and Integrations changes in rust-v0.122.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2 Interface Experience changes in rust-v0.122.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-20-2-mobile-and-desktop-changes-in-rust-v0-122-0|2 Mobile and Desktop changes in rust-v0.122.0]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-e2ddce&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-100-other-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-e2ddce%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->