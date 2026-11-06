---
card_id: codex-cli-2026-03-05-e32337
date: '2026-03-05'
description: 'Codex CLI · 2026-03-05 · Other changes: 71 changes in 0.110.0 — Added
  a persisted `/fast` toggle in the TUI and app-server support for `fast` and `flex`…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b01715a1544abfb7c3414a68172ca2a8fb7d0bf5ce78ef80fd72db1367718b69
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-05-e32337
  comparison: ''
  date: '2026-03-05'
  description: 'Codex CLI — 0.110.0: 71 other changes'
  evidence:
  - quote: 'Added a persisted `/fast` toggle in the TUI and app-server support for
      `fast` and `flex` service tiers. (#13212, #13334, #13391)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: Added a direct Windows installer script to published release artifacts.
      (#12741)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: 'Removed the remaining legacy app-server v1 websocket/RPC surfaces in favor
      of the current protocol. (#13364, #13375, #13397)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13086 Fix CLI feedback link @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13063 Make cloud_requirements fail close @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13027 feat: skill disable respect config layer @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13125 chore: change mem default @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13065 core: resolve host_executable() rules during preflight @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#12989 fix: MacOSAutomationPermission::BundleIDs should allow communicating
      … @leoshimo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13181 [codex] include plan type in account updates @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13058 Record realtime close marker on replacement @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13215 Fix issue deduplication workflow for Codex issues @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13090 Fix project trust config parsing so CLI overrides work @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13202 tui: restore draft footer hints @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#11814 test(app-server): increase flow test timeout to reduce flake @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13282 app-server: Update `thread/name/set` to support not-loaded threads
      @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13285 feat(app-server): add tracing to all app-server APIs @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13265 Update realtime websocket API @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13261 fix(app-server): emit turn/started only when turn actually starts
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13079 app-server: Silence thread status changes caused by thread being
      created @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13284 Adjusting plan prompt for clarity and verbosity @bfioca-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13286 feat(app-server-test-client): support tracing @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13212 add fast mode toggle @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13336 fix: db windows path @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13334 app-server service tier plumbing (plus some cleanup) @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13341 feat: presentation artifact p1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13344 feat: pres artifact 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13346 feat: pres artifact 3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13348 feat: presentation part 4 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13355 feat: pres artifact part 5 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13357 feat: add multi-actions to presentation tool @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13360 feat: artifact presentation part 7 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#12741 Add Windows direct install script @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13376 realtime prompt changes @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13324 app-server-protocol: export flat v2 schema bundle @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13364 Remove Responses V1 websocket implementation @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#12969 app-server: source /feedback logs from sqlite at trace level @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13381 chore: rm --all-features flag from rust-analyzer @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13385 Revert "realtime prompt changes" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13389 fix @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13375 chore(app-server): delete v1 RPC methods and notifications @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13397 chore(app-server): restore EventMsg TS types @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13395 Build delegated realtime handoff text from all messages @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13399 Require deduplicator success before commenting @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13398 Revert "Revert "realtime prompt changes"" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13275 fix(network-proxy): reject mismatched host headers @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#12868 tui: align pending steers with core acceptance @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13280 Add thread metadata update endpoint to app server @joeytrasatti-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13050 Add under-development original-resolution view_image support @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13331 Make js_repl image output controllable @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13292 [feedback] diagnostics @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13414 feat(app-server): add a skills/changed v2 notification @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13366 [bazel] Bump rules_rs and llvm @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13427 chore: Nest skill and protocol network permissions under `network.enabled`
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13429 core: box wrapper futures to reduce stack pressure @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13391 support ''flex'' tier in app-server in addition to ''fast'' @kharvd'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13290 image-gen-core @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13412 feat: ordinal nick name @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13454 add metric for per-turn token usage @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13461 fix: bad merge @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13456 feat: add metric for per-turn tool count and add tmp_mem flag @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13468 nit: citation prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13424 feat(core, tracing): add a span representing a turn @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13489 remove serviceTier from app-server examples @kharvd'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13382 fix(tui): decode ANSI alpha-channel encoding in syntax themes @fcoury'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13485 feat: external artifacts builder @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13493 feat(app-server-test-client): OTEL setup for tracing @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13501 add metrics for external config import @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13495 Notify TUI about plan mode prompts and user input requests @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13506 [release] temporarily use thin LTO for releases @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13505 Prefix handoff messages with role @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 71-other-changes-in-rust-v0-110-0
  source_release: codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302
  source_type: github_releases
  theme: uncategorized
  title: 71 other changes in rust-v0.110.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302]]'
source_type: github_releases
theme: uncategorized
title: 71 other changes in rust-v0.110.0
type: change
---

<!-- chronolog:begin region="header" -->
# 71 other changes in rust-v0.110.0

**Codex CLI** · 2026-03-05 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.110.0) · from [[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|0.110.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a persisted `/fast` toggle in the TUI and app-server support for `fast` and `flex` service tiers. (#13212, #13334, #13391)

> Added a direct Windows installer script to published release artifacts. (#12741)

> Removed the remaining legacy app-server v1 websocket/RPC surfaces in favor of the current protocol. (#13364, #13375, #13397)

> #13086 Fix CLI feedback link @etraut-openai

> #13063 Make cloud_requirements fail close @alexsong-oai

> #13027 feat: skill disable respect config layer @jif-oai

> #13125 chore: change mem default @jif-oai

> #13065 core: resolve host_executable() rules during preflight @bolinfest

> #12989 fix: MacOSAutomationPermission::BundleIDs should allow communicating … @leoshimo-oai

> #13181 [codex] include plan type in account updates @tibo-openai

> #13058 Record realtime close marker on replacement @aibrahim-oai

> #13215 Fix issue deduplication workflow for Codex issues @etraut-openai

> #13090 Fix project trust config parsing so CLI overrides work @etraut-openai

> #13202 tui: restore draft footer hints @charley-oai

> #11814 test(app-server): increase flow test timeout to reduce flake @joshka-oai

> #13282 app-server: Update `thread/name/set` to support not-loaded threads @euroelessar

> #13285 feat(app-server): add tracing to all app-server APIs @owenlin0

> #13265 Update realtime websocket API @aibrahim-oai

> #13261 fix(app-server): emit turn/started only when turn actually starts @owenlin0

> #13079 app-server: Silence thread status changes caused by thread being created @euroelessar

> #13284 Adjusting plan prompt for clarity and verbosity @bfioca-openai

> #13286 feat(app-server-test-client): support tracing @owenlin0

> #13212 add fast mode toggle @pash-openai

> #13336 fix: db windows path @jif-oai

> #13334 app-server service tier plumbing (plus some cleanup) @pash-openai

> #13341 feat: presentation artifact p1 @jif-oai

> #13344 feat: pres artifact 2 @jif-oai

> #13346 feat: pres artifact 3 @jif-oai

> #13348 feat: presentation part 4 @jif-oai

> #13355 feat: pres artifact part 5 @jif-oai

> #13357 feat: add multi-actions to presentation tool @jif-oai

> #13360 feat: artifact presentation part 7 @jif-oai

> #12741 Add Windows direct install script @efrazer-oai

> #13376 realtime prompt changes @aibrahim-oai

> #13324 app-server-protocol: export flat v2 schema bundle @apanasenko-oai

> #13364 Remove Responses V1 websocket implementation @pakrym-oai

> #12969 app-server: source /feedback logs from sqlite at trace level @charley-oai

> #13381 chore: rm --all-features flag from rust-analyzer @sayan-oai

> #13385 Revert "realtime prompt changes" @aibrahim-oai

> #13389 fix @aibrahim-oai

> #13375 chore(app-server): delete v1 RPC methods and notifications @owenlin0

> #13397 chore(app-server): restore EventMsg TS types @owenlin0

> #13395 Build delegated realtime handoff text from all messages @aibrahim-oai

> #13399 Require deduplicator success before commenting @etraut-openai

> #13398 Revert "Revert "realtime prompt changes"" @aibrahim-oai

> #13275 fix(network-proxy): reject mismatched host headers @viyatb-oai

> #12868 tui: align pending steers with core acceptance @charley-oai

> #13280 Add thread metadata update endpoint to app server @joeytrasatti-openai

> #13050 Add under-development original-resolution view_image support @fjord-oai

> #13331 Make js_repl image output controllable @fjord-oai

> #13292 [feedback] diagnostics @rhan-oai

> #13414 feat(app-server): add a skills/changed v2 notification @owenlin0

> #13366 [bazel] Bump rules_rs and llvm @zbarsky-openai

> #13427 chore: Nest skill and protocol network permissions under `network.enabled` @celia-oai

> #13429 core: box wrapper futures to reduce stack pressure @bolinfest

> #13391 support 'flex' tier in app-server in addition to 'fast' @kharvd

> #13290 image-gen-core @won-openai

> #13412 feat: ordinal nick name @jif-oai

> #13454 add metric for per-turn token usage @jif-oai

> #13461 fix: bad merge @jif-oai

> #13456 feat: add metric for per-turn tool count and add tmp_mem flag @jif-oai

> #13468 nit: citation prompt @jif-oai

> #13424 feat(core, tracing): add a span representing a turn @owenlin0

> #13489 remove serviceTier from app-server examples @kharvd

> #13382 fix(tui): decode ANSI alpha-channel encoding in syntax themes @fcoury

> #13485 feat: external artifacts builder @jif-oai

> #13493 feat(app-server-test-client): OTEL setup for tracing @owenlin0

> #13501 add metrics for external config import @alexsong-oai

> #13495 Notify TUI about plan mode prompts and user input requests @etraut-openai

> #13506 [release] temporarily use thin LTO for releases @bolinfest

> #13505 Prefix handoff messages with role @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.110.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-05-12935-speed-up-subagent-startup-daveaitel-openai|♯12935 Speed up subagent startup @daveaitel-openai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-03-05-2-model-support-changes-in-rust-v0-110-0|2 Model Support changes in rust-v0.110.0]] · Model Support
- [[Changes/Codex CLI/2026-03-05-13127-nit-disable-on-windows-jif-oai|♯13127 nit: disable on windows @jif-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-05-13-agent-mode-changes-in-rust-v0-110-0|13 Agent Mode changes in rust-v0.110.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-05-13313-renaming-team-to-business-plan-during-tui-onboarding-bwanner-oai|♯13313 Renaming Team to Business plan during TUI onboarding @bwanner-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-05-12383-add-new-scopes-to-login-adaley-openai|♯12383 add new scopes to login @adaley-openai]] · Account and Access
- [[Changes/Codex CLI/2026-03-05-4-files-and-data-changes-in-rust-v0-110-0|4 Files and Data changes in rust-v0.110.0]] · Files and Data
- [[Changes/Codex CLI/2026-03-05-13388-config-enforce-enterprise-feature-requirements-bolinfest|♯13388 config: enforce enterprise feature requirements @bolinfest]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7 Apps and Integrations changes in rust-v0.110.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-05-7-developer-workflow-changes-in-rust-v0-110-0|7 Developer Workflow changes in rust-v0.110.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0|5 Memory and Personalization changes in rust-v0.110.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4 Safety and Privacy changes in rust-v0.110.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-05-3-context-window-changes-in-rust-v0-110-0|3 Context Window changes in rust-v0.110.0]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-05-e32337&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-05-71-other-changes-in-rust-v0-110-0.md%0ACard%20ID%3A%20codex-cli-2026-03-05-e32337%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.110.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->