---
card_id: codex-cli-2026-05-26-165ab0
date: '2026-05-26'
description: 'Codex CLI · 2026-05-26 · Other changes: 47 changes in 0.134.0 — Added
  search across local conversation history, including case-insensitive content matches
  with…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2b4f440456b31cd699a603d7a97621d9824e481da82adec11b6b3f5486167890
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-26-165ab0
  comparison: ''
  date: '2026-05-26'
  description: 'Codex CLI — 0.134.0: 47 other changes'
  evidence:
  - quote: 'Added search across local conversation history, including case-insensitive
      content matches with result previews. (#23519, #23921)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Displayed workspace-specific usage-limit messages for credit and spend-cap
      failures. (#24114)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Ensured Node-based tools honor Codex’s managed network proxy environment.
      (#23905)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Documented the curl and PowerShell installer paths in the README. (#24106)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Updated developer docs to prefer `just test` over direct `cargo test` for
      repo-local test runs. (#23910)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Added profile migration documentation links to relevant config errors.
      (#23879)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: Added release-build support for Codex-produced V8 artifacts. (#23934)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23581 Trace logical websocket request after untraced warmup @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23718 [codex] Steer budget-limited goal extension turns @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23861 fix: cargo lock @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23870 Make tool executor specs mandatory @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23876 refactor: centralize tool exposure planning @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23879 chore: link doc in profile error messages @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23883 cli: rename profile v2 flag to --profile @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23835 docs: add description to codex-cli/package.json @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23886 cli: remove legacy profile v1 plumbing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23833 packaging: move rg manifest out of npm bin @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23796 Improve `/goal` error messages for ephemeral sessions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23867 Reconnect disconnected exec-server websocket clients with fresh
      sessions @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23792 TUI: skip goal replace prompt for completed goals @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23519 [codex] Add rollout-backed thread content search @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23836 npm: remove legacy package artifact synthesis @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23921 [codex] Make thread search case-insensitive @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23860 Add Bedrock Mantle GovCloud region @CHARLESPALEN-OAI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23357 feat: support local refs and defs in tool input schemas @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23963 Expose conversation history to extension tools @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23904 feat: best-effort compact large tool schemas @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23905 [codex] Enable Node env proxy for managed network proxy @rreichel3-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24051 config: remove legacy profile v1 resolution @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24055 config: remove legacy profile write paths @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24061 otel: drop legacy profile usage telemetry @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24059 fix: reject legacy profile selectors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23934 ci: Use codex produced v8 artifacts for release builds @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24099 fix(app-server): fix optional bool annotations @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23910 Prefer `just test` over `cargo test` in docs @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24081 tui: make `codex-tui.log` opt-in @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24067 app-server: drop legacy profile config surface @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24106 docs: update README.md to mention curl-based installer @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24082 fix(tui): restore Windows VT before TUI renders @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23980 Add trace_id to TurnStartedEvent @mchen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23989 Add typed Images client to codex-api @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24129 package: factor DotSlash executable fetching @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24151 [codex] Use TurnInput for session task input @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#23935 [codex] Add image re-encoding benchmarks @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24152 chore: add JSON schema policy fixture coverage @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24157 [codex] Remove external client session reset plumbing @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  - quote: '#24114 Display workspace usage limit error copy from response header @dhruvgupta-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.134.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 47-other-changes-in-rust-v0-134-0
  source_release: codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e
  source_type: github_releases
  theme: uncategorized
  title: 47 other changes in rust-v0.134.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e|codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e]]'
source_type: github_releases
theme: uncategorized
title: 47 other changes in rust-v0.134.0
type: change
---

<!-- chronolog:begin region="header" -->
# 47 other changes in rust-v0.134.0

**Codex CLI** · 2026-05-26 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.134.0) · from [[Releases/Codex CLI/codex-cli-2026-05-26-rust-v0-134-0-github-329640454-7be6059e|0.134.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added search across local conversation history, including case-insensitive content matches with result previews. (#23519, #23921)

> Displayed workspace-specific usage-limit messages for credit and spend-cap failures. (#24114)

> Ensured Node-based tools honor Codex’s managed network proxy environment. (#23905)

> Documented the curl and PowerShell installer paths in the README. (#24106)

> Updated developer docs to prefer `just test` over direct `cargo test` for repo-local test runs. (#23910)

> Added profile migration documentation links to relevant config errors. (#23879)

> Added release-build support for Codex-produced V8 artifacts. (#23934)

> #23581 Trace logical websocket request after untraced warmup @jif-oai

> #23718 [codex] Steer budget-limited goal extension turns @jif-oai

> #23861 fix: cargo lock @jif-oai

> #23870 Make tool executor specs mandatory @jif-oai

> #23876 refactor: centralize tool exposure planning @jif-oai

> #23879 chore: link doc in profile error messages @jif-oai

> #23883 cli: rename profile v2 flag to --profile @jif-oai

> #23835 docs: add description to codex-cli/package.json @bolinfest

> #23886 cli: remove legacy profile v1 plumbing @jif-oai

> #23833 packaging: move rg manifest out of npm bin @bolinfest

> #23796 Improve `/goal` error messages for ephemeral sessions @etraut-openai

> #23867 Reconnect disconnected exec-server websocket clients with fresh sessions @starr-openai

> #23792 TUI: skip goal replace prompt for completed goals @etraut-openai

> #23519 [codex] Add rollout-backed thread content search @fc-oai

> #23836 npm: remove legacy package artifact synthesis @bolinfest

> #23921 [codex] Make thread search case-insensitive @fc-oai

> #23860 Add Bedrock Mantle GovCloud region @CHARLESPALEN-OAI

> #23357 feat: support local refs and defs in tool input schemas @celia-oai

> #23963 Expose conversation history to extension tools @sayan-oai

> #23904 feat: best-effort compact large tool schemas @celia-oai

> #23905 [codex] Enable Node env proxy for managed network proxy @rreichel3-oai

> #24051 config: remove legacy profile v1 resolution @jif-oai

> #24055 config: remove legacy profile write paths @jif-oai

> #24061 otel: drop legacy profile usage telemetry @jif-oai

> #24059 fix: reject legacy profile selectors @jif-oai

> #23934 ci: Use codex produced v8 artifacts for release builds @cconger

> #24099 fix(app-server): fix optional bool annotations @owenlin0

> #23910 Prefer `just test` over `cargo test` in docs @anp-oai

> #24081 tui: make `codex-tui.log` opt-in @jif-oai

> #24067 app-server: drop legacy profile config surface @jif-oai

> #24106 docs: update README.md to mention curl-based installer @bolinfest

> #24082 fix(tui): restore Windows VT before TUI renders @fcoury-oai

> #23980 Add trace_id to TurnStartedEvent @mchen-oai

> #23989 Add typed Images client to codex-api @won-openai

> #24129 package: factor DotSlash executable fetching @bolinfest

> #24151 [codex] Use TurnInput for session task input @pakrym-oai

> #23935 [codex] Add image re-encoding benchmarks @anp-oai

> #24152 chore: add JSON schema policy fixture coverage @celia-oai

> #24157 [codex] Remove external client session reset plumbing @pakrym-oai

> #24114 Display workspace usage limit error copy from response header @dhruvgupta-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.134.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-26-3-agent-mode-changes-in-rust-v0-134-0|3 Agent Mode changes in rust-v0.134.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-26-11-apps-and-integrations-changes-in-rust-v0-134-0|11 Apps and Integrations changes in rust-v0.134.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-26-22915-3-of-4-tui-route-feature-and-memory-toggles-through-app-server-etraut-open|♯22915 3 of 4 tui: route feature and memory toggles through app server @etraut-openai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-26-23736-add-new-enterprise-requirement-gate-adams-oai|♯23736 Add new enterprise requirement gate @adams-oai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-05-26-5-context-window-changes-in-rust-v0-134-0|5 Context Window changes in rust-v0.134.0]] · Context Window
- [[Changes/Codex CLI/2026-05-26-2-account-and-access-changes-in-rust-v0-134-0|2 Account and Access changes in rust-v0.134.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-26-7-safety-and-privacy-changes-in-rust-v0-134-0|7 Safety and Privacy changes in rust-v0.134.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-26-2-mobile-and-desktop-changes-in-rust-v0-134-0|2 Mobile and Desktop changes in rust-v0.134.0]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-26-165ab0&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-26-47-other-changes-in-rust-v0-134-0.md%0ACard%20ID%3A%20codex-cli-2026-05-26-165ab0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.134.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->