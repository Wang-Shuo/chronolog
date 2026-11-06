---
card_id: codex-cli-2026-07-09-f01e5c
date: '2026-07-09'
description: 'Codex CLI · 2026-07-09 · Other changes: 43 changes in 0.144.0 — Added
  a `writes` app-approval mode that allows declared read-only actions while prompting
  for…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d9841747c5bedbe6e146f8413476d6291deecdfef397ea03ec59863c4515af72
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-09-f01e5c
  comparison: ''
  date: '2026-07-09'
  description: 'Codex CLI — 0.144.0: 43 other changes'
  evidence:
  - quote: Added a `writes` app-approval mode that allows declared read-only actions
      while prompting for writes. (#30482)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: Global pnunen installs are now detected so diagnostics and updates use
      the correct package manager. (#31503)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: Improved automatic review behavior with clearer instructions and a focused
      tool set. (#31480)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31298 feat(core): emit canonical dynamic tool call items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#30953 fix(release): add missing Intel V8 signing entitlement @malsamiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31355 refactor: make ExternalAuth return CodexAuth @lt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31352 ci: increase Windows Bazel local test jobs @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#30482 [codex-rs] Add writes app approval mode @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31439 Handle bio policy errors in Codex @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31422 test: generalize exec-server fixture @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#28772 [codex] Enable auth elicitation by default @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31285 [1/5] [codex] sync managed-layer bundle schema @hefuc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31300 feat(core): emit canonical collab tool call items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31301 feat(core): emit canonical collab wait items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31425 test: add TestAppServer builder @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31342 http-client: expose WebSocket proxy prerequisites @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31289 Use canonical indexed web access field @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31332 ci: parameterize Cargo target paths @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31421 refactor: unify external auth resolution @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31451 test: migrate TestAppServer callers to builder @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31274 [codex] Add externally provided Codex auth @lt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31283 core: support extension-owned turn items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31570 fs: support pruning hidden directories during walks @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31465 Align empty branch list message with search @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31586 Stabilize encrypted MAv2 spawn request test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31503 Detect Codex installs managed by pnpm @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31473 feat(core): emit canonical review mode items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31452 test: remove TestAppServer constructors @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31500 code-mode: move to hosted mode by default @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31524 chore(protocol): use UUIDv7 for generated item IDs @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31578 Bound exec-server pending RPCs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#29875 [codex] Sanitize imported session fallback titles @stefanstokic-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31630 feat(core): emit canonical hook prompt items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31441 core: preserve Responses WebSockets with system proxy @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31357 ci: route build IO through Dev Drives @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31461 chore: remove inert cargo audit workflow @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31614 test: migrate app-server v2 starts to auto env @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31650 code-mode: make all approvals trigger elicitation pause @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31648 Clarify device-code phishing warning @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31663 test(app-server): use native rollout fixture paths @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31427 test: add delayed exec-server transport @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#30278 [codex] Preserve reviewer when resuming threads @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#30188 feat(rollout): persist TurnItems for paginated thread rollouts
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 43-other-changes-in-rust-v0-144-0
  source_release: codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96
  source_type: github_releases
  theme: uncategorized
  title: 43 other changes in rust-v0.144.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96]]'
source_type: github_releases
theme: uncategorized
title: 43 other changes in rust-v0.144.0
type: change
---

<!-- chronolog:begin region="header" -->
# 43 other changes in rust-v0.144.0

**Codex CLI** · 2026-07-09 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.144.0) · from [[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `writes` app-approval mode that allows declared read-only actions while prompting for writes. (#30482)

> Global pnunen installs are now detected so diagnostics and updates use the correct package manager. (#31503)

> Improved automatic review behavior with clearer instructions and a focused tool set. (#31480)

> #31298 feat(core): emit canonical dynamic tool call items @owenlin0

> #30953 fix(release): add missing Intel V8 signing entitlement @malsamiri-oai

> #31355 refactor: make ExternalAuth return CodexAuth @lt-oai

> #31352 ci: increase Windows Bazel local test jobs @anp-oai

> #30482 [codex-rs] Add writes app approval mode @zamoshchin-openai

> #31439 Handle bio policy errors in Codex @fc-oai

> #31422 test: generalize exec-server fixture @anp-oai

> #28772 [codex] Enable auth elicitation by default @mzeng-openai

> #31285 [1/5] [codex] sync managed-layer bundle schema @hefuc-oai

> #31300 feat(core): emit canonical collab tool call items @owenlin0

> #31301 feat(core): emit canonical collab wait items @owenlin0

> #31425 test: add TestAppServer builder @anp-oai

> #31342 http-client: expose WebSocket proxy prerequisites @bolinfest

> #31289 Use canonical indexed web access field @winston-openai

> #31332 ci: parameterize Cargo target paths @anp-oai

> #31421 refactor: unify external auth resolution @pakrym-oai

> #31451 test: migrate TestAppServer callers to builder @anp-oai

> #31274 [codex] Add externally provided Codex auth @lt-oai

> #31283 core: support extension-owned turn items @owenlin0

> #31570 fs: support pruning hidden directories during walks @jif-oai

> #31465 Align empty branch list message with search @charliemarsh-oai

> #31586 Stabilize encrypted MAv2 spawn request test @jif-oai

> #31503 Detect Codex installs managed by pnpm @charliemarsh-oai

> #31473 feat(core): emit canonical review mode items @owenlin0

> #31452 test: remove TestAppServer constructors @anp-oai

> #31500 code-mode: move to hosted mode by default @cconger

> #31524 chore(protocol): use UUIDv7 for generated item IDs @owenlin0

> #31578 Bound exec-server pending RPCs @jif-oai

> #29875 [codex] Sanitize imported session fallback titles @stefanstokic-oai

> #31630 feat(core): emit canonical hook prompt items @owenlin0

> #31441 core: preserve Responses WebSockets with system proxy @bolinfest

> #31357 ci: route build IO through Dev Drives @anp-oai

> #31461 chore: remove inert cargo audit workflow @anp-oai

> #31614 test: migrate app-server v2 starts to auto env @anp-oai

> #31650 code-mode: make all approvals trigger elicitation pause @cconger

> #31648 Clarify device-code phishing warning @etraut-openai

> #31663 test(app-server): use native rollout fixture paths @fcoury-oai

> #31427 test: add delayed exec-server transport @anp-oai

> #30278 [codex] Preserve reviewer when resuming threads @viyatb-oai

> #30188 feat(rollout): persist TurnItems for paginated thread rollouts @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.144.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-09-31191-handle-completion-separators-and-popup-dismissal-charliemarsh-oai|♯31191 Handle completion separators and popup dismissal @charliemarsh-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-07-09-31596-use-the-image-generation-extension-by-default-won-openai|♯31596 Use the image generation extension by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-07-09-responses-websockets-continue-using-the-low-latency-transport-while-respecting-s|Responses WebSockets continue using the low-latency transport while respecting…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-09-31356-ci-run-v8-source-builds-on-windows-2025-anp-oai|♯31356 ci: run V8 source builds on Windows 2025 @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-09-11-apps-and-integrations-changes-in-rust-v0-144-0|11 Apps and Integrations changes in rust-v0.144.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587 Stabilize shared rollout budget test @jif-oai]] · Collaboration
- [[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525 core: migrate standalone web search to extension-owned turn items @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-09-5-account-and-access-changes-in-rust-v0-144-0|5 Account and Access changes in rust-v0.144.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-09-8-model-support-changes-in-rust-v0-144-0|8 Model Support changes in rust-v0.144.0]] · Model Support
- [[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit reset credits now show their type and expiration, and let you choose…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]] · Context Window
- [[Changes/Codex CLI/2026-07-09-3-interface-experience-changes-in-rust-v0-144-0|3 Interface Experience changes in rust-v0.144.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-09-6-developer-workflow-changes-in-rust-v0-144-0|6 Developer Workflow changes in rust-v0.144.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4 Safety and Privacy changes in rust-v0.144.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-09-f01e5c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-09-43-other-changes-in-rust-v0-144-0.md%0ACard%20ID%3A%20codex-cli-2026-07-09-f01e5c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.144.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->