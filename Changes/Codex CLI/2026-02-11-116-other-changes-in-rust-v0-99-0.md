---
card_id: codex-cli-2026-02-11-b1fa1e
date: '2026-02-11'
description: 'Codex CLI · 2026-02-11 · Other changes: 116 changes in 0.99.0 — Image
  attachments now accept GIF and WebP inputs in addition to existing formats. (#11237)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 10c85c5448b52e173785f3f5198b321d86b5889bbfcfad9a030c4c58d093da1f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-11-b1fa1e
  comparison: ''
  date: '2026-02-11'
  description: 'Codex CLI — 0.99.0: 116 other changes'
  evidence:
  - quote: Image attachments now accept GIF and WebP inputs in addition to existing
      formats. (#11237)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: 'Reworked npm release packaging so platform-specific binaries are distributed
      via `@openai/codex` dist-tags, reducing package-size pressure while preserving
      platform-specific installs (including `@alpha`). (#11318, #11339)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10689 fix: flaky landlock @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10738 nit: backfill stronger @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10246 adding fork information (UI) when forking @pap-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10425 Include real OS info in metrics. @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10745 feat: resumable backfill @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10758 feat: wire ephemeral in `codex exec` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10756 chore: handle shutdown correctly in tui @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10751 feat: repair DB in case of missing lines @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10762 nit: add DB version in discrepancy recording @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10621 Leverage state DB metadata for thread summaries @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10423 fix(auth): isolate chatgptAuthTokens concept to auth manager and
      app-server @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10783 fix: announcement in prio @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10721 [app-server] Add a method to list experimental features. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10787 chore: limit update to 0.98.0 NUX to < 0.98.0 ver @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10655 Add analytics for /rename and /fork @pap-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10790 feat: wait for backfill to be ready @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10693 Add app-server transport layer with websocket support @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10818 other announcement @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10815 Sync app-server requirements API with refreshed cloud loader @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10727 Send beta header with websocket connects @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10809 updates: use brew api for version check @magus'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10793 Add stage field for experimental flags. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10821 feat(app-server): turn/steer API @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10792 Print warning when config does not meet requirements @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10699 feat: expose detailed metrics to runtime metrics @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10843 Log an event (info only) when we receive a file watcher event @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10892 nit: test an @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10894 feat: backfill async again @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10851 Removed "exec_policy" feature flag @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10457 Queue nudges while plan generating @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10822 Add app configs to config.toml @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10420 feat(network-proxy): add structured policy decision to blocked
      errors @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10698 core: preconnect Responses websocket for first turn @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10928 chore(app-server): add experimental annotation to relevant fields
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10861 Support alternative websocket API @by-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10826 add originator to otel @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10943 app-server: print help message to console when starting websockets
      server @JaviSoto'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10965 refactor(network-proxy): flatten network config under [network]
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10970 Fixed a flaky test @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10977 fix: use expected line ending in codex-rs/core/config.schema.json
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10973 Do not poll for usage when using API Key auth @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10921 Show left/right arrows to navigate in tui request_user_input @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10993 Fix flaky windows CI test @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10987 Fixed a flaky Windows test that is consistently causing a CI failure
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10958 feat(core): add network constraints schema to requirements.toml
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10983 app-server: treat null mode developer instructions as built-in
      defaults @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11040 Simplify pre-connect @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10966 feat: enable premessage-deflate for websockets @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#9040 fix(tui): rehydrate drafts and restore image placeholders @Chriss4123'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10824 Fallback to HTTP on UPGRADE_REQUIRED @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11028 Defer persistence of rollout file @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10980 fix: remove config.schema.json from tag check @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11109 [bazel] Upgrade some rulesets in preparation for enabling windows
      @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11114 chore: refactor network-proxy so that ConfigReloader is injectable
      behavior @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10718 Upgrade rmcp to 0.14 @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11121 chore: reverse the codex-network-proxy -> codex-core dependency
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11105 feat: include NetworkConfig through ExecParams @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10799 feat: do not close unified exec processes across turns @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11193 Deflake mixed parallel tools timing test @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10937 Translate websocket errors @rasmusrygaard'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11217 Fixed bug in file watcher that results in spurious skills update
      events and large log files @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11216 Move warmup to the task level @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11203 Try to stop small helper methods @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11197 [bazel] Upgrade some rulesets in preparation for enabling windows,
      part 2 @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11158 chore: remove network-proxy-cli crate @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11123 TUI: fix request_user_input wrapping for long option labels @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10657 feat: search_tool @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10835 feat: extend skills/list to support additional roots. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10960 skill-creator: Remove invalid reference. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11219 feat: use a notify instead of grace to close ue process @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10962 fix(tui): keep unified exec summary on working line @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11232 Add originator to otel metadata tags @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11237 adding image support for gif and webp @natea-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11242 fix(feature) UnderDevelopment feature must be off @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11185 fix: nix build by adding missing dependencies and fix outputHashes
      @Philipp-M'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11262 chore: change ConfigState so it no longer depends on a single config.toml
      file for reloading @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11240 fix(app-server): for external auth, replace id_token with chatgpt_acc…
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11140 chore(deps): bump insta from 1.46.2 to 1.46.3 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11139 chore(deps): bump anyhow from 1.0.100 to 1.0.101 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11138 chore(deps): bump regex from 1.12.2 to 1.12.3 in /codex-rs @dependabot'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11269 feat: reserve loopback ephemeral listeners for managed proxy @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11244 feat: add SkillPolicy to skill metadata and support allow_implicit_invocation
      @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10215 chore(tui) cleanup /approvals @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10940 feat: support configurable metric_exporter @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11207 feat: retain NetworkProxy, when appropriate @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11306 feat: phase 2 consolidation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11318 chore: split NPM packages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11322 Fix pending input test waiting logic @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11265 Remove ApiPrompt @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11295 tui: keep history recall cursor at line end @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11288 fix(protocol): approval policy never prompt @fouad-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11323 Revert "Add app-server transport layer with websocket support (#10693)"
      @maxj-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11162 Fix: update parallel tool call exec approval to approve on request
      id @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11319 feat: opt-out of events in the app-server @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11241 Treat first rollout session_meta as canonical thread identity @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11339 # Use `@openai/codex` dist-tags for platform binaries instead of
      separate package names @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11345 core: remove stale apply_patch SandboxPolicy TODO in seatbelt @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11343 Compare full request for websockets incrementality @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11344 fix: reduce usage of `open_if_present` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11337 Extract tool building @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10941 fix(core): canonicalize wrapper approvals and support heredoc prefix
      … @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11348 Use thin LTO for alpha Rust release builds @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11364 feat: mem v2 - PR1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11365 feat: mem v2 - PR2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11366 feat: mem v2 - PR3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11369 feat: mem v2 - PR4 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11362 Enable SOCKS defaults for common local network proxy use cases
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11359 ci: fall back to local Bazel on forks without BuildBuddy key @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11372 feat: mem v2 - PR5 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11374 feat: mem v2 - PR6 (consolidation) @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11377 feat: prevent double backfill @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11394 Disable very flaky tests @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11373 tui: queue non-pending rollback trims in app-event order @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11393 Remove `deterministic_process_ids` feature to avoid duplicate `codex-core`
      builds @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 116-other-changes-in-rust-v0-99-0
  source_release: codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016
  source_type: github_releases
  theme: uncategorized
  title: 116 other changes in rust-v0.99.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016]]'
source_type: github_releases
theme: uncategorized
title: 116 other changes in rust-v0.99.0
type: change
---

<!-- chronolog:begin region="header" -->
# 116 other changes in rust-v0.99.0

**Codex CLI** · 2026-02-11 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.99.0) · from [[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|0.99.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Image attachments now accept GIF and WebP inputs in addition to existing formats. (#11237)

> Reworked npm release packaging so platform-specific binaries are distributed via `@openai/codex` dist-tags, reducing package-size pressure while preserving platform-specific installs (including `@alpha`). (#11318, #11339)

> #10689 fix: flaky landlock @jif-oai

> #10738 nit: backfill stronger @jif-oai

> #10246 adding fork information (UI) when forking @pap-openai

> #10425 Include real OS info in metrics. @iceweasel-oai

> #10745 feat: resumable backfill @jif-oai

> #10758 feat: wire ephemeral in `codex exec` @jif-oai

> #10756 chore: handle shutdown correctly in tui @jif-oai

> #10751 feat: repair DB in case of missing lines @jif-oai

> #10762 nit: add DB version in discrepancy recording @jif-oai

> #10621 Leverage state DB metadata for thread summaries @jif-oai

> #10423 fix(auth): isolate chatgptAuthTokens concept to auth manager and app-server @owenlin0

> #10783 fix: announcement in prio @jif-oai

> #10721 [app-server] Add a method to list experimental features. @mzeng-openai

> #10787 chore: limit update to 0.98.0 NUX to < 0.98.0 ver @sayan-oai

> #10655 Add analytics for /rename and /fork @pap-openai

> #10790 feat: wait for backfill to be ready @jif-oai

> #10693 Add app-server transport layer with websocket support @maxj-oai

> #10818 other announcement @jif-oai

> #10815 Sync app-server requirements API with refreshed cloud loader @xl-openai

> #10727 Send beta header with websocket connects @pakrym-oai

> #10809 updates: use brew api for version check @magus

> #10793 Add stage field for experimental flags. @mzeng-openai

> #10821 feat(app-server): turn/steer API @owenlin0

> #10792 Print warning when config does not meet requirements @gt-oai

> #10699 feat: expose detailed metrics to runtime metrics @apanasenko-oai

> #10843 Log an event (info only) when we receive a file watcher event @etraut-openai

> #10892 nit: test an @jif-oai

> #10894 feat: backfill async again @jif-oai

> #10851 Removed "exec_policy" feature flag @etraut-openai

> #10457 Queue nudges while plan generating @charley-oai

> #10822 Add app configs to config.toml @canvrno-oai

> #10420 feat(network-proxy): add structured policy decision to blocked errors @viyatb-oai

> #10698 core: preconnect Responses websocket for first turn @joshka-oai

> #10928 chore(app-server): add experimental annotation to relevant fields @owenlin0

> #10861 Support alternative websocket API @by-openai

> #10826 add originator to otel @alexsong-oai

> #10943 app-server: print help message to console when starting websockets server @JaviSoto

> #10965 refactor(network-proxy): flatten network config under [network] @viyatb-oai

> #10970 Fixed a flaky test @etraut-openai

> #10977 fix: use expected line ending in codex-rs/core/config.schema.json @bolinfest

> #10973 Do not poll for usage when using API Key auth @etraut-openai

> #10921 Show left/right arrows to navigate in tui request_user_input @charley-oai

> #10993 Fix flaky windows CI test @etraut-openai

> #10987 Fixed a flaky Windows test that is consistently causing a CI failure @etraut-openai

> #10958 feat(core): add network constraints schema to requirements.toml @viyatb-oai

> #10983 app-server: treat null mode developer instructions as built-in defaults @charley-oai

> #11040 Simplify pre-connect @pakrym-oai

> #10966 feat: enable premessage-deflate for websockets @apanasenko-oai

> #9040 fix(tui): rehydrate drafts and restore image placeholders @Chriss4123

> #10824 Fallback to HTTP on UPGRADE_REQUIRED @pakrym-oai

> #11028 Defer persistence of rollout file @etraut-openai

> #10980 fix: remove config.schema.json from tag check @bolinfest

> #11109 [bazel] Upgrade some rulesets in preparation for enabling windows @zbarsky-openai

> #11114 chore: refactor network-proxy so that ConfigReloader is injectable behavior @bolinfest

> #10718 Upgrade rmcp to 0.14 @mzeng-openai

> #11121 chore: reverse the codex-network-proxy -> codex-core dependency @bolinfest

> #11105 feat: include NetworkConfig through ExecParams @bolinfest

> #10799 feat: do not close unified exec processes across turns @jif-oai

> #11193 Deflake mixed parallel tools timing test @gt-oai

> #10937 Translate websocket errors @rasmusrygaard

> #11217 Fixed bug in file watcher that results in spurious skills update events and large log files @etraut-openai

> #11216 Move warmup to the task level @pakrym-oai

> #11203 Try to stop small helper methods @pakrym-oai

> #11197 [bazel] Upgrade some rulesets in preparation for enabling windows, part 2 @zbarsky-openai

> #11158 chore: remove network-proxy-cli crate @viyatb-oai

> #11123 TUI: fix request_user_input wrapping for long option labels @charley-oai

> #10657 feat: search_tool @apanasenko-oai

> #10835 feat: extend skills/list to support additional roots. @xl-openai

> #10960 skill-creator: Remove invalid reference. @xl-openai

> #11219 feat: use a notify instead of grace to close ue process @jif-oai

> #10962 fix(tui): keep unified exec summary on working line @joshka-oai

> #11232 Add originator to otel metadata tags @alexsong-oai

> #11237 adding image support for gif and webp @natea-oai

> #11242 fix(feature) UnderDevelopment feature must be off @dylan-hurd-oai

> #11185 fix: nix build by adding missing dependencies and fix outputHashes @Philipp-M

> #11262 chore: change ConfigState so it no longer depends on a single config.toml file for reloading @bolinfest

> #11240 fix(app-server): for external auth, replace id_token with chatgpt_acc… @owenlin0

> #11140 chore(deps): bump insta from 1.46.2 to 1.46.3 in /codex-rs @dependabot

> #11139 chore(deps): bump anyhow from 1.0.100 to 1.0.101 in /codex-rs @dependabot

> #11138 chore(deps): bump regex from 1.12.2 to 1.12.3 in /codex-rs @dependabot

> #11269 feat: reserve loopback ephemeral listeners for managed proxy @bolinfest

> #11244 feat: add SkillPolicy to skill metadata and support allow_implicit_invocation @alexsong-oai

> #10215 chore(tui) cleanup /approvals @dylan-hurd-oai

> #10940 feat: support configurable metric_exporter @alexsong-oai

> #11207 feat: retain NetworkProxy, when appropriate @bolinfest

> #11306 feat: phase 2 consolidation @jif-oai

> #11318 chore: split NPM packages @jif-oai

> #11322 Fix pending input test waiting logic @jif-oai

> #11265 Remove ApiPrompt @pakrym-oai

> #11295 tui: keep history recall cursor at line end @joshka-oai

> #11288 fix(protocol): approval policy never prompt @fouad-openai

> #11323 Revert "Add app-server transport layer with websocket support (#10693)" @maxj-oai

> #11162 Fix: update parallel tool call exec approval to approve on request id @shijie-oai

> #11319 feat: opt-out of events in the app-server @jif-oai

> #11241 Treat first rollout session_meta as canonical thread identity @guinness-oai

> #11339 # Use `@openai/codex` dist-tags for platform binaries instead of separate package names @bolinfest

> #11345 core: remove stale apply_patch SandboxPolicy TODO in seatbelt @bolinfest

> #11343 Compare full request for websockets incrementality @pakrym-oai

> #11344 fix: reduce usage of `open_if_present` @jif-oai

> #11337 Extract tool building @pakrym-oai

> #10941 fix(core): canonicalize wrapper approvals and support heredoc prefix … @viyatb-oai

> #11348 Use thin LTO for alpha Rust release builds @bolinfest

> #11364 feat: mem v2 - PR1 @jif-oai

> #11365 feat: mem v2 - PR2 @jif-oai

> #11366 feat: mem v2 - PR3 @jif-oai

> #11369 feat: mem v2 - PR4 @jif-oai

> #11362 Enable SOCKS defaults for common local network proxy use cases @viyatb-oai

> #11359 ci: fall back to local Bazel on forks without BuildBuddy key @joshka-oai

> #11372 feat: mem v2 - PR5 @jif-oai

> #11374 feat: mem v2 - PR6 (consolidation) @jif-oai

> #11377 feat: prevent double backfill @jif-oai

> #11394 Disable very flaky tests @pakrym-oai

> #11373 tui: queue non-pending rollback trims in app-event order @charley-oai

> #11393 Remove `deterministic_process_ids` feature to avoid duplicate `codex-core` builds @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.99.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3 Search and Browsing changes in rust-v0.99.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-11-9-developer-workflow-changes-in-rust-v0-99-0|9 Developer Workflow changes in rust-v0.99.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-11-6-context-window-changes-in-rust-v0-99-0|6 Context Window changes in rust-v0.99.0]] · Context Window
- [[Changes/Codex CLI/2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0|13 Apps and Integrations changes in rust-v0.99.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety and Privacy changes in rust-v0.99.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-11-7-memory-and-personalization-changes-in-rust-v0-99-0|7 Memory and Personalization changes in rust-v0.99.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-11-enterprise-admin-requirements-can-now-restrict-web-search-modes-and-define-netwo|Enterprise/admin requirements can now restrict web search modes and define network…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-02-11-2-editor-experience-changes-in-rust-v0-99-0|2 Editor Experience changes in rust-v0.99.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-11-11294-chore-put-crypto-provider-logic-in-a-shared-crate-bolinfest|♯11294 chore: put crypto provider logic in a shared crate @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-02-11-11336-always-expose-view-image-and-return-unsupported-image-input-error-aibrahim|♯11336 Always expose view_image and return unsupported image-input error @aibrahim-oai]] · Multimodal Input
- [[Changes/Codex CLI/2026-02-11-15-model-support-changes-in-rust-v0-99-0|15 Model Support changes in rust-v0.99.0]] · Model Support
- [[Changes/Codex CLI/2026-02-11-10-agent-mode-changes-in-rust-v0-99-0|10 Agent Mode changes in rust-v0.99.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-11-4-mobile-and-desktop-changes-in-rust-v0-99-0|4 Mobile and Desktop changes in rust-v0.99.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-11-8-interface-experience-changes-in-rust-v0-99-0|8 Interface Experience changes in rust-v0.99.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-11-added-statusline-to-configure-which-metadata-appears-in-the-tui-footer-interacti|Added /statusline to configure which metadata appears in the TUI footer interactively]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-11-b1fa1e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-11-116-other-changes-in-rust-v0-99-0.md%0ACard%20ID%3A%20codex-cli-2026-02-11-b1fa1e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.99.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->