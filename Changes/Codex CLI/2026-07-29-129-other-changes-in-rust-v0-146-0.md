---
card_id: codex-cli-2026-07-29-37a09d
date: '2026-07-29'
description: 'Codex CLI · 2026-07-29 · Other changes: 129 changes in 0.146.0 — Name
  new sessions with `/new` or `/clear`, pin important threads, and switch between
  side…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 775d4c33d1d9c794d2536226649edb0e8b18a130012e7e66071352c96aff8243
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-29-37a09d
  comparison: ''
  date: '2026-07-29'
  description: 'Codex CLI — 0.146.0: 129 other changes'
  evidence:
  - quote: 'Name new sessions with `/new` or `/clear`, pin important threads, and
      switch between side conversations without closing them. (#34605, #34840, #35011)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Fork threads with paginated history, including temporary forks that do
      not appear in thread listings. (#35220, #35251)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Connect app-server to remote Code Mode hosts over WebSocket. (#35078,
      #35098)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Discover executor-provided skills and securely read their associated resources,
      including explicitly selected skills. (#35184, #35198)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Preserve submitted messages, final responses, failed-turn errors, imported
      timestamps, and approval settings across interruptions, replay, imports, and
      forks. (#34839, #34777, #35524, #34989, #34664)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: Clarify Windows drive-letter canonicalization for `PathUri` values. (#34667)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Publish release artifacts, channel metadata, and installer aliases through
      OpenAI-hosted release infrastructure, with GitHub fallback. (#34505, #34508,
      #34729, #34910)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: 'Reduce app-server serialization overhead and unnecessary request-building
      allocations. (#34761, #34766, #34825)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34447 Add a route-aware HTTP client pool @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34449 Make external session detection limits configurable @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34463 Support alpha hotfix release versions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34469 Preserve thread settings for goal-first and forked threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34476 Separate HTTP execution from request logging @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34478 Honor `CARGO_HTTP_CAINFO` in managed proxy environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34479 Re-resolve system proxy routes across redirects @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34481 Add route-aware redirect test coverage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34483 Expand route-aware proxy redirect coverage @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34490 Route backend requests through the HTTP client factory @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34495 Honor system proxy settings in the daemon updater @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34497 Preserve custom arg0 for sandboxed exec-server processes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34505 Mirror Rust release artifacts to Cloudflare R2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34508 Publish release metadata to R2 channels @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34514 Add an optional releases.openai.com installer source @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34516 Allow `numer` in codespell checks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34517 Pass empty inherited FDs in the Wine PTY test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34525 Add step-scoped data to extension contributors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34533 Centralize compacted rollout item construction @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34544 Size Noise handshake buffers to their messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34552 Remove unused RtOptions setters @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34558 Remove obsolete ignored tests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34559 Add backend client support for Codex user settings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34562 Record rollout boundaries for materialized turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34563 Page through inherited thread history @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34566 Protect fork history references during rollout cleanup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34570 Highlight CUDA files as C++ in the TUI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34578 Gate the TUI suspend restore helper on Unix @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34597 Enforce exact values from managed config requirements @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34601 Sanitize skill names in injection metrics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34603 Allow explicitly permitted loopback proxy targets @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34605 Allow naming sessions with `/new` and `/clear` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34612 Detach non-interactive subprocesses from stdin @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34620 Add exec-server network policy callback types @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34624 Terminate Windows process trees with job objects @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34630 Add a policy-aware HTTP client builder @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34636 Keep the TUI open when starting a turn fails @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34637 Attribute review findings to repository rules @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34640 Update Windows process-tree tests for inherited FDs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34641 Harden managed proxy setup for sandboxed executions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34645 Always assign response item IDs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34649 Propagate resolved proxy policy through auth routing @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34650 Require auth managers to receive routing configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34654 Render turn diffs for foreign environment paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34655 Honor configured proxy routes for auth refreshes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34664 Preserve approvals reviewer when forking threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34669 Expand codex-http-client usage guidance @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34681 Add session headers to realtime conversation starts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34713 Order unified exec lifecycle events reliably @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34729 Publish stable installer aliases to R2 @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34732 Preserve skill catalog entries under metadata pressure @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34734 Remove step-scoped data from extension contributors @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34738 Drop skill descriptions before omitting catalog entries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34744 Update skills budget tests for extension API changes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34746 Match core skill ordering in extension catalogs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34761 Reduce app-server JSON serialization overhead @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34763 Retry websocket requests when the previous response is missing
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34766 Reduce typed app-server request serialization overhead @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34770 Enable exec-server network policy callbacks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34771 Size unified mention popups to visible results @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34781 Upgrade Bazel Rust and LLVM dependencies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34784 Reject dynamic environments named `local` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34789 Avoid unnecessary post-sampling token estimates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34796 Skip syntax highlighting for lines over 4 KiB @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34797 Suppress omission notices in core-compatible skill catalogs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34808 Centralize SQLite connection configuration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34814 Consolidate thread startup around `StartThreadOptions` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34816 Support configurable realtime BEM channel prefixes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34823 Run code-mode tests in non-Windows Bazel CI @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34824 Normalize Guardian review cwd reuse keys @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34825 Reduce cloning when building Responses requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34827 Remove Windows Bazel lint toolchain overrides @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34831 Flush analytics before in-process app server shutdown @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34840 Add persisted thread pinning to the app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34844 Remove first-party type from app metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34910 Prefer releases.openai.com in standalone installers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34940 Keep session defaults static during config batch writes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34959 Handle @ in local marketplace paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34969 Keep the sleep tool outside code mode @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34978 Honor disabled redirects in route-aware HTTP clients @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34986 Enforce single-writer ownership for paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34994 Honor the configured SQLite home across state consumers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34995 Initialize execution environments with the final HTTP policy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34996 Separate Codex error details from retry metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35000 Make TUI turn interrupts nonblocking @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35011 Keep side conversations open when switching threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35012 Expose remote skill icon URLs through app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35013 Support incremental replay of updated thread items @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35015 Align installed app duration metrics with the legacy baseline @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35023 Route exec-server HTTP through configured proxy policy @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35031 Enforce writer ownership for thread archive and deletion @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35033 Expose Browser Use requirements through the app server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35048 Track app/read request duration @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35049 Register the Guardian V2 feature flag @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35054 Allow disabling the update_plan tool @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35056 Route exec-server WebSockets through configured proxies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35059 Decouple exec-server HTTP from reqwest types @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35063 Track deferred tool namespaces in world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35065 Avoid duplicating deferred sources in tool search @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35067 Fix Bazel test configuration for platform-specific data @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35078 Add WebSocket transport to the code-mode host @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35098 Support remote code-mode hosts in app-server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35106 Allow hosts to customize `wait_for_environment` descriptions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35168 Route extension warnings to app-server threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35172 Compact host skill paths under metadata pressure @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35184 Expose executor skills through skill tools @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35198 Enable resource reads for explicit executor skills @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35220 Support paginated thread forks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35221 Avoid persisting non-local threads for hook transcripts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35251 Support ephemeral forks of paginated threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35266 Allow disabling the in-process code-mode host fallback @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35267 Harden network approval cancellation and concurrency @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35271 Include code-mode tool names in Responses Lite metadata @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35275 Trace remote exec-server connection setup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35359 Handle exec-server network policy requests in the client @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35364 Bound Code Mode metadata compatibility headers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35365 Keep unified mention results fresh @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35408 Ignore generated system skills in the skills watcher @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35523 Shut down the in-process outbound router explicitly @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35525 Skip inactive TUI threads without pending user interaction @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35537 Add managed policy for in-app updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 129-other-changes-in-rust-v0-146-0
  source_release: codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983
  source_type: github_releases
  theme: uncategorized
  title: 129 other changes in rust-v0.146.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983|codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983]]'
source_type: github_releases
theme: uncategorized
title: 129 other changes in rust-v0.146.0
type: change
---

<!-- chronolog:begin region="header" -->
# 129 other changes in rust-v0.146.0

**Codex CLI** · 2026-07-29 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.146.0) · from [[Releases/Codex CLI/codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983|0.146.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Name new sessions with `/new` or `/clear`, pin important threads, and switch between side conversations without closing them. (#34605, #34840, #35011)

> Fork threads with paginated history, including temporary forks that do not appear in thread listings. (#35220, #35251)

> Connect app-server to remote Code Mode hosts over WebSocket. (#35078, #35098)

> Discover executor-provided skills and securely read their associated resources, including explicitly selected skills. (#35184, #35198)

> Preserve submitted messages, final responses, failed-turn errors, imported timestamps, and approval settings across interruptions, replay, imports, and forks. (#34839, #34777, #35524, #34989, #34664)

> Clarify Windows drive-letter canonicalization for `PathUri` values. (#34667)

> Publish release artifacts, channel metadata, and installer aliases through OpenAI-hosted release infrastructure, with GitHub fallback. (#34505, #34508, #34729, #34910)

> Reduce app-server serialization overhead and unnecessary request-building allocations. (#34761, #34766, #34825)

> #34447 Add a route-aware HTTP client pool @copyberry

> #34449 Make external session detection limits configurable @copyberry

> #34463 Support alpha hotfix release versions @copyberry

> #34469 Preserve thread settings for goal-first and forked threads @copyberry

> #34476 Separate HTTP execution from request logging @copyberry

> #34478 Honor `CARGO_HTTP_CAINFO` in managed proxy environments @copyberry

> #34479 Re-resolve system proxy routes across redirects @copyberry

> #34481 Add route-aware redirect test coverage @copyberry

> #34483 Expand route-aware proxy redirect coverage @copyberry

> #34490 Route backend requests through the HTTP client factory @copyberry

> #34495 Honor system proxy settings in the daemon updater @copyberry

> #34497 Preserve custom arg0 for sandboxed exec-server processes @copyberry

> #34505 Mirror Rust release artifacts to Cloudflare R2 @copyberry

> #34508 Publish release metadata to R2 channels @copyberry

> #34514 Add an optional releases.openai.com installer source @copyberry

> #34516 Allow `numer` in codespell checks @copyberry

> #34517 Pass empty inherited FDs in the Wine PTY test @copyberry

> #34525 Add step-scoped data to extension contributors @copyberry

> #34533 Centralize compacted rollout item construction @copyberry

> #34544 Size Noise handshake buffers to their messages @copyberry

> #34552 Remove unused RtOptions setters @copyberry

> #34558 Remove obsolete ignored tests @copyberry

> #34559 Add backend client support for Codex user settings @copyberry

> #34562 Record rollout boundaries for materialized turns @copyberry

> #34563 Page through inherited thread history @copyberry

> #34566 Protect fork history references during rollout cleanup @copyberry

> #34570 Highlight CUDA files as C++ in the TUI @copyberry

> #34578 Gate the TUI suspend restore helper on Unix @copyberry

> #34597 Enforce exact values from managed config requirements @copyberry

> #34601 Sanitize skill names in injection metrics @copyberry

> #34603 Allow explicitly permitted loopback proxy targets @copyberry

> #34605 Allow naming sessions with `/new` and `/clear` @copyberry

> #34612 Detach non-interactive subprocesses from stdin @copyberry

> #34620 Add exec-server network policy callback types @copyberry

> #34624 Terminate Windows process trees with job objects @copyberry

> #34630 Add a policy-aware HTTP client builder @copyberry

> #34636 Keep the TUI open when starting a turn fails @copyberry

> #34637 Attribute review findings to repository rules @copyberry

> #34640 Update Windows process-tree tests for inherited FDs @copyberry

> #34641 Harden managed proxy setup for sandboxed executions @copyberry

> #34645 Always assign response item IDs @copyberry

> #34649 Propagate resolved proxy policy through auth routing @copyberry

> #34650 Require auth managers to receive routing configuration @copyberry

> #34654 Render turn diffs for foreign environment paths @copyberry

> #34655 Honor configured proxy routes for auth refreshes @copyberry

> #34664 Preserve approvals reviewer when forking threads @copyberry

> #34669 Expand codex-http-client usage guidance @copyberry

> #34681 Add session headers to realtime conversation starts @copyberry

> #34713 Order unified exec lifecycle events reliably @copyberry

> #34729 Publish stable installer aliases to R2 @copyberry

> #34732 Preserve skill catalog entries under metadata pressure @copyberry

> #34734 Remove step-scoped data from extension contributors @copyberry

> #34738 Drop skill descriptions before omitting catalog entries @copyberry

> #34744 Update skills budget tests for extension API changes @copyberry

> #34746 Match core skill ordering in extension catalogs @copyberry

> #34761 Reduce app-server JSON serialization overhead @copyberry

> #34763 Retry websocket requests when the previous response is missing @copyberry

> #34766 Reduce typed app-server request serialization overhead @copyberry

> #34770 Enable exec-server network policy callbacks @copyberry

> #34771 Size unified mention popups to visible results @copyberry

> #34781 Upgrade Bazel Rust and LLVM dependencies @copyberry

> #34784 Reject dynamic environments named `local` @copyberry

> #34789 Avoid unnecessary post-sampling token estimates @copyberry

> #34796 Skip syntax highlighting for lines over 4 KiB @copyberry

> #34797 Suppress omission notices in core-compatible skill catalogs @copyberry

> #34808 Centralize SQLite connection configuration @copyberry

> #34814 Consolidate thread startup around `StartThreadOptions` @copyberry

> #34816 Support configurable realtime BEM channel prefixes @copyberry

> #34823 Run code-mode tests in non-Windows Bazel CI @copyberry

> #34824 Normalize Guardian review cwd reuse keys @copyberry

> #34825 Reduce cloning when building Responses requests @copyberry

> #34827 Remove Windows Bazel lint toolchain overrides @copyberry

> #34831 Flush analytics before in-process app server shutdown @copyberry

> #34840 Add persisted thread pinning to the app server @copyberry

> #34844 Remove first-party type from app metadata @copyberry

> #34910 Prefer releases.openai.com in standalone installers @copyberry

> #34940 Keep session defaults static during config batch writes @copyberry

> #34959 Handle @ in local marketplace paths @copyberry

> #34969 Keep the sleep tool outside code mode @copyberry

> #34978 Honor disabled redirects in route-aware HTTP clients @copyberry

> #34986 Enforce single-writer ownership for paginated threads @copyberry

> #34994 Honor the configured SQLite home across state consumers @copyberry

> #34995 Initialize execution environments with the final HTTP policy @copyberry

> #34996 Separate Codex error details from retry metadata @copyberry

> #35000 Make TUI turn interrupts nonblocking @copyberry

> #35011 Keep side conversations open when switching threads @copyberry

> #35012 Expose remote skill icon URLs through app server @copyberry

> #35013 Support incremental replay of updated thread items @copyberry

> #35015 Align installed app duration metrics with the legacy baseline @copyberry

> #35023 Route exec-server HTTP through configured proxy policy @copyberry

> #35031 Enforce writer ownership for thread archive and deletion @copyberry

> #35033 Expose Browser Use requirements through the app server @copyberry

> #35048 Track app/read request duration @copyberry

> #35049 Register the Guardian V2 feature flag @copyberry

> #35054 Allow disabling the update_plan tool @copyberry

> #35056 Route exec-server WebSockets through configured proxies @copyberry

> #35059 Decouple exec-server HTTP from reqwest types @copyberry

> #35063 Track deferred tool namespaces in world state @copyberry

> #35065 Avoid duplicating deferred sources in tool search @copyberry

> #35067 Fix Bazel test configuration for platform-specific data @copyberry

> #35078 Add WebSocket transport to the code-mode host @copyberry

> #35098 Support remote code-mode hosts in app-server @copyberry

> #35106 Allow hosts to customize `wait_for_environment` descriptions @copyberry

> #35168 Route extension warnings to app-server threads @copyberry

> #35172 Compact host skill paths under metadata pressure @copyberry

> #35184 Expose executor skills through skill tools @copyberry

> #35198 Enable resource reads for explicit executor skills @copyberry

> #35220 Support paginated thread forks @copyberry

> #35221 Avoid persisting non-local threads for hook transcripts @copyberry

> #35251 Support ephemeral forks of paginated threads @copyberry

> #35266 Allow disabling the in-process code-mode host fallback @copyberry

> #35267 Harden network approval cancellation and concurrency @copyberry

> #35271 Include code-mode tool names in Responses Lite metadata @copyberry

> #35275 Trace remote exec-server connection setup @copyberry

> #35359 Handle exec-server network policy requests in the client @copyberry

> #35364 Bound Code Mode metadata compatibility headers @copyberry

> #35365 Keep unified mention results fresh @copyberry

> #35408 Ignore generated system skills in the skills watcher @copyberry

> #35523 Shut down the in-process outbound router explicitly @copyberry

> #35525 Skip inactive TUI threads without pending user interaction @copyberry

> #35537 Add managed policy for in-app updates @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.146.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-29-47-apps-and-integrations-changes-in-rust-v0-146-0|47 Apps and Integrations changes in rust-v0.146.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-29-2-search-and-browsing-changes-in-rust-v0-146-0|2 Search and Browsing changes in rust-v0.146.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-29-2-mobile-and-desktop-changes-in-rust-v0-146-0|2 Mobile and Desktop changes in rust-v0.146.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-29-34850-disable-image-generation-for-free-plan-accounts-copyberry|♯34850 Disable image generation for Free-plan accounts @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-07-29-3-collaboration-changes-in-rust-v0-146-0|3 Collaboration changes in rust-v0.146.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-29-3-model-support-changes-in-rust-v0-146-0|3 Model Support changes in rust-v0.146.0]] · Model Support
- [[Changes/Codex CLI/2026-07-29-5-context-window-changes-in-rust-v0-146-0|5 Context Window changes in rust-v0.146.0]] · Context Window
- [[Changes/Codex CLI/2026-07-29-35530-track-model-and-personality-in-world-state-copyberry|♯35530 Track model and personality in world state @copyberry]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-29-34643-migrate-login-http-construction-to-httpclient-copyberry|♯34643 Migrate login HTTP construction to HttpClient @copyberry]] · Account and Access
- [[Changes/Codex CLI/2026-07-29-8-interface-experience-changes-in-rust-v0-146-0|8 Interface Experience changes in rust-v0.146.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-29-12-developer-workflow-changes-in-rust-v0-146-0|12 Developer Workflow changes in rust-v0.146.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-29-11-agent-mode-changes-in-rust-v0-146-0|11 Agent Mode changes in rust-v0.146.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-29-3-editor-experience-changes-in-rust-v0-146-0|3 Editor Experience changes in rust-v0.146.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-29-6-safety-and-privacy-changes-in-rust-v0-146-0|6 Safety and Privacy changes in rust-v0.146.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-29-2-enterprise-and-administration-changes-in-rust-v0-146-0|2 Enterprise and Administration changes in rust-v0.146.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-07-29-2-files-and-data-changes-in-rust-v0-146-0|2 Files and Data changes in rust-v0.146.0]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-29-37a09d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-29-129-other-changes-in-rust-v0-146-0.md%0ACard%20ID%3A%20codex-cli-2026-07-29-37a09d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.146.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->