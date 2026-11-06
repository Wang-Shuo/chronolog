---
card_id: codex-cli-2026-03-10-dbfed2
date: '2026-03-10'
description: 'Codex CLI · 2026-03-10 · Other changes: 70 changes in 0.113.0 — Hardened
  network proxy policy parsing by rejecting global wildcard (`*`) domains while…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 728b123dfd2f76710b3ee931d2b1946a694507255bf90e76a119bf53a433b57e
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-10-dbfed2
  comparison: ''
  date: '2026-03-10'
  description: 'Codex CLI — 0.113.0: 70 other changes'
  evidence:
  - quote: Hardened network proxy policy parsing by rejecting global wildcard (`*`)
      domains while preserving scoped wildcard support. (#13789)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: Clarified `js_repl` guidance for persistent bindings and redeclaration
      recovery to reduce avoidable REPL errors. (#13803)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: 'Reduced log/storage overhead by moving logs to a dedicated SQLite DB,
      adding timestamps to feedback logs, pruning old data, and tightening retention/row
      limits. (#13645, #13688, #13734, #13763, #13772, #13781)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13626 feat(otel): safe tracing @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13615 Replay thread rollback from rollout history @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13642 fix(tui): clean up pending steer preview wrapping @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13645 Add timestamped SQLite /feedback logs without schema changes @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13687 refactor: remove proxy admin endpoint @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#11874 fix(tui) remove config check for trusted setting @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13697 change sound @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13607 Enabling CWD Saving for Image-Gen @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13688 Add timestamps to feedback log lines @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13742 fix: windows normalization @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13514 [rmcp-client] Recover from streamable HTTP 404 sessions @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13750 feat: drop sqlite db feature flag @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13753 feat: drop discrepency metrics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13763 feat: limit number of rows per log @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13630 feat(otel, core): record turn TTFT and TTFM metrics in codex-core
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13674 app-server: Emit `thread/name/updated` event globally @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13772 Move sqlite logs to a dedicated database @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13620 chore: improve DB flushing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13781 Reduce SQLite log retention to 10 days @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13780 fix: move unit tests in codex-rs/core/src/config/mod.rs into their
      own file @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13783 fix: move unit tests in codex-rs/core/src/codex.rs into their own
      file @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13787 fix bazel build @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13789 fix: reject global wildcard network proxy domains @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#12943 Codex/winget auto update @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13800 chore(otel): reorganize codex-otel crate @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13803 Clarify js_repl binding reuse guidance @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13814 fix: include libcap-dev dependency when creating a devcontainer
      for building Codex @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13808 chore(otel): rename OtelManager to SessionTelemetry @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13791 fix(core): skip exec approval for permissionless skill scripts
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13819 feat(app-server-protocol): address naming conflicts in json schema
      exporter @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#12752 fix: support managed network allowlist controls @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13440 protocol: derive effective file access from filesystem policies
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13816 fix(core): respect reject policy by approval source for skill scripts
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13833 app-server: require absolute cwd for windowsSandbox/setupStart
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13771 feat: simplify DB further @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13692 Add guardian approval MVP @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13851 tmp: drop artifact skills @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13910 fix(core) rm guardian snapshot test @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13911 fix(ci) fix guardian ci @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13451 sandboxing: preserve denied paths when widening permissions @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13452 protocol: keep root carveouts sandboxed @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13874 Stabilize abort task follow-up handling @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13989 Fix inverted Windows PTY `TerminateProcess` handling @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13912 fix(ci): restore guardian coverage and bazel unit tests @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13839 [app-server] Support hot-reload user config when batch writing
      config. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14005 Add in-process app server and wire up exec to use it @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13929 app-server: include experimental skill metadata in exec approval
      requests @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14014 fix(core) patch otel test @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13841 tui: clarify pending steer follow-ups @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13092 Add request permissions tool @mousseau-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14027 fix(bazel) add missing app-server-client BUILD.bazel @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14004 feat(tui) render request_permissions calls @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14052 Stabilize app list update ordering test @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13897 guardian initial feedback / tweaks @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13884 Reduce app-server test timeout pressure @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13872 Stabilize zsh fork app-server tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13881 Stabilize RMCP pid file cleanup test @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13883 Stabilize PTY Python REPL test @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14058 Stabilize plan item app-server tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13943 Order websocket initialize after handshake @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13885 Stabilize thread resume replay tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14049 fix: properly handle 401 error in clound requirement fetch. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14102 Stabilize interrupted task approval cleanup @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14103 Stabilize guardian approval coverage @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#14060 Stabilize resumed rollout messages @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13880 Stabilize RMCP streamable HTTP readiness tests @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  - quote: '#13886 Stabilize protocol schema fixture generation @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.113.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 70-other-changes-in-rust-v0-113-0
  source_release: codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6
  source_type: github_releases
  theme: uncategorized
  title: 70 other changes in rust-v0.113.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6|codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6]]'
source_type: github_releases
theme: uncategorized
title: 70 other changes in rust-v0.113.0
type: change
---

<!-- chronolog:begin region="header" -->
# 70 other changes in rust-v0.113.0

**Codex CLI** · 2026-03-10 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.113.0) · from [[Releases/Codex CLI/codex-cli-2026-03-10-rust-v0-113-0-github-294999501-e594ccb6|0.113.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hardened network proxy policy parsing by rejecting global wildcard (`*`) domains while preserving scoped wildcard support. (#13789)

> Clarified `js_repl` guidance for persistent bindings and redeclaration recovery to reduce avoidable REPL errors. (#13803)

> Reduced log/storage overhead by moving logs to a dedicated SQLite DB, adding timestamps to feedback logs, pruning old data, and tightening retention/row limits. (#13645, #13688, #13734, #13763, #13772, #13781)

> #13626 feat(otel): safe tracing @owenlin0

> #13615 Replay thread rollback from rollout history @aibrahim-oai

> #13642 fix(tui): clean up pending steer preview wrapping @charley-oai

> #13645 Add timestamped SQLite /feedback logs without schema changes @charley-oai

> #13687 refactor: remove proxy admin endpoint @viyatb-oai

> #11874 fix(tui) remove config check for trusted setting @dylan-hurd-oai

> #13697 change sound @aibrahim-oai

> #13607 Enabling CWD Saving for Image-Gen @won-openai

> #13688 Add timestamps to feedback log lines @etraut-openai

> #13742 fix: windows normalization @jif-oai

> #13514 [rmcp-client] Recover from streamable HTTP 404 sessions @caseychow-oai

> #13750 feat: drop sqlite db feature flag @jif-oai

> #13753 feat: drop discrepency metrics @jif-oai

> #13763 feat: limit number of rows per log @jif-oai

> #13630 feat(otel, core): record turn TTFT and TTFM metrics in codex-core @owenlin0

> #13674 app-server: Emit `thread/name/updated` event globally @euroelessar

> #13772 Move sqlite logs to a dedicated database @charley-oai

> #13620 chore: improve DB flushing @jif-oai

> #13781 Reduce SQLite log retention to 10 days @charley-oai

> #13780 fix: move unit tests in codex-rs/core/src/config/mod.rs into their own file @bolinfest

> #13783 fix: move unit tests in codex-rs/core/src/codex.rs into their own file @bolinfest

> #13787 fix bazel build @bolinfest

> #13789 fix: reject global wildcard network proxy domains @viyatb-oai

> #12943 Codex/winget auto update @iceweasel-oai

> #13800 chore(otel): reorganize codex-otel crate @owenlin0

> #13803 Clarify js_repl binding reuse guidance @fjord-oai

> #13814 fix: include libcap-dev dependency when creating a devcontainer for building Codex @bolinfest

> #13808 chore(otel): rename OtelManager to SessionTelemetry @owenlin0

> #13791 fix(core): skip exec approval for permissionless skill scripts @celia-oai

> #13819 feat(app-server-protocol): address naming conflicts in json schema exporter @owenlin0

> #12752 fix: support managed network allowlist controls @viyatb-oai

> #13440 protocol: derive effective file access from filesystem policies @bolinfest

> #13816 fix(core): respect reject policy by approval source for skill scripts @celia-oai

> #13833 app-server: require absolute cwd for windowsSandbox/setupStart @iceweasel-oai

> #13771 feat: simplify DB further @jif-oai

> #13692 Add guardian approval MVP @charley-oai

> #13851 tmp: drop artifact skills @jif-oai

> #13910 fix(core) rm guardian snapshot test @dylan-hurd-oai

> #13911 fix(ci) fix guardian ci @dylan-hurd-oai

> #13451 sandboxing: preserve denied paths when widening permissions @bolinfest

> #13452 protocol: keep root carveouts sandboxed @bolinfest

> #13874 Stabilize abort task follow-up handling @aibrahim-oai

> #13989 Fix inverted Windows PTY `TerminateProcess` handling @etraut-openai

> #13912 fix(ci): restore guardian coverage and bazel unit tests @charley-oai

> #13839 [app-server] Support hot-reload user config when batch writing config. @mzeng-openai

> #14005 Add in-process app server and wire up exec to use it @etraut-openai

> #13929 app-server: include experimental skill metadata in exec approval requests @celia-oai

> #14014 fix(core) patch otel test @dylan-hurd-oai

> #13841 tui: clarify pending steer follow-ups @charley-oai

> #13092 Add request permissions tool @mousseau-oai

> #14027 fix(bazel) add missing app-server-client BUILD.bazel @dylan-hurd-oai

> #14004 feat(tui) render request_permissions calls @dylan-hurd-oai

> #14052 Stabilize app list update ordering test @aibrahim-oai

> #13897 guardian initial feedback / tweaks @charley-oai

> #13884 Reduce app-server test timeout pressure @aibrahim-oai

> #13872 Stabilize zsh fork app-server tests @aibrahim-oai

> #13881 Stabilize RMCP pid file cleanup test @aibrahim-oai

> #13883 Stabilize PTY Python REPL test @aibrahim-oai

> #14058 Stabilize plan item app-server tests @aibrahim-oai

> #13943 Order websocket initialize after handshake @aibrahim-oai

> #13885 Stabilize thread resume replay tests @aibrahim-oai

> #14049 fix: properly handle 401 error in clound requirement fetch. @xl-openai

> #14102 Stabilize interrupted task approval cleanup @aibrahim-oai

> #14103 Stabilize guardian approval coverage @aibrahim-oai

> #14060 Stabilize resumed rollout messages @aibrahim-oai

> #13880 Stabilize RMCP streamable HTTP readiness tests @aibrahim-oai

> #13886 Stabilize protocol schema fixture generation @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.113.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-10-10-safety-and-privacy-changes-in-rust-v0-113-0|10 Safety and Privacy changes in rust-v0.113.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-10-2-automation-and-scheduling-changes-in-rust-v0-113-0|2 Automation and Scheduling changes in rust-v0.113.0]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-03-10-13734-feat-prune-old-memories-in-db-jif-oai|♯13734 feat: prune old memories in DB @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-10-4-interface-experience-changes-in-rust-v0-113-0|4 Interface Experience changes in rust-v0.113.0]] · Interface Experience
- [[Changes/Codex CLI/2026-03-10-11-apps-and-integrations-changes-in-rust-v0-113-0|11 Apps and Integrations changes in rust-v0.113.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-10-8-developer-workflow-changes-in-rust-v0-113-0|8 Developer Workflow changes in rust-v0.113.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-10-14117-feat-otel-centralize-otel-metric-names-and-shared-tag-builders-owenlin0|♯14117 feat(otel): Centralize OTEL metric names and shared tag builders @owenlin0]] · Collaboration
- [[Changes/Codex CLI/2026-03-10-image-generation-now-saves-output-files-into-the-current-working-directory-13607|Image generation now saves output files into the current working directory]] · Image Generation
- [[Changes/Codex CLI/2026-03-10-14123-pass-on-save-info-to-model-ui-tweaks-won-openai|♯14123 pass on save info to model + ui tweaks @won-openai]] · Model Support
- [[Changes/Codex CLI/2026-03-10-2-search-and-browsing-changes-in-rust-v0-113-0|2 Search and Browsing changes in rust-v0.113.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-03-10-2-account-and-access-changes-in-rust-v0-113-0|2 Account and Access changes in rust-v0.113.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-10-4-context-window-changes-in-rust-v0-113-0|4 Context Window changes in rust-v0.113.0]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-10-dbfed2&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-10-70-other-changes-in-rust-v0-113-0.md%0ACard%20ID%3A%20codex-cli-2026-03-10-dbfed2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.113.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->