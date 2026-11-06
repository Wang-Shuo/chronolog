---
card_id: codex-cli-2026-05-21-b3da23
date: '2026-05-21'
description: 'Codex CLI · 2026-05-21 · Other changes: 79 changes in 0.133.0 — Improved
  release and CI reliability with package-builder tests, prebuilt resource packaging…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 146967175b6076a25674e2233077c4afe3227000b692eef49173ca727ab24425
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-21-b3da23
  comparison: ''
  date: '2026-05-21'
  description: 'Codex CLI — 0.133.0: 79 other changes'
  evidence:
  - quote: 'Improved release and CI reliability with package-builder tests, prebuilt
      resource packaging, DotSlash zstd handling, platform-sharded Rust tests, and
      Codex Linux release runners. (#23760, #23759, #23752, #23358, #23761)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22380 fix: default unknown tool schemas to empty schemas @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23309 Add tool lifecycle extension contributor @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23253 Reduce rust-ci-full Windows nextest timeout flakes @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#21812 Publish Linux runtime wheels with glibc-compatible tags @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22709 [codex] Trim unused TurnContextItem fields @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22728 [codex] Move pending input into input queue @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23371 fix(tui): warn on unsupported iTerm2 pet versions @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23376 [codex-analytics] preserve user thread source for exec threads
      @marksteinbrick-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23384 [codex] Remove external websocket session resets @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22721 cleanup: Remove skill env var dependency prompting @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23389 Remove ToolSearch feature toggle @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23080 [1 of 7] Add thread settings to UserInput @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23081 [2 of 7] Remove UserInputWithTurnContext @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23075 [3 of 7] Remove UserTurn @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22508 [5 of 7] Replace OverrideTurnContext with ThreadSettings @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22086 CI: Customize v8 building @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23300 feat: dedicated goal DB @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22835 Remove ToolsConfig from tool planning @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23409 [codex] Allow empty turn/start requests @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23388 [codex] Move hook request plumbing into hook runtime @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23405 [codex] Preserve steer input as user input @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22914 [2 of 4] tui: route app and skill enablement through app server
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23397 [codex] Make contextual user fragments dyn-renderable @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22929 Harden CLI rate limit window labels @ase-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22782 Add SubagentStart hook @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23513 build: add Codex package builder @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23369 Make local environment optional in EnvironmentManager @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23327 Refactor exec-server websocket pump @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23536 fix(tui): preserve modified enter in plan questions @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23400 Fix empty rollout path app-server handling @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23551 Route local-only app-server gating through processors @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23516 fix: serialize unix app-server startup @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22169 [codex] Honor role-defined spawn service tiers @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23555 Add CUA requirements subsection for locked computer use @adams-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23538 Fix: TUI starting in wrong CWD @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23526 build: fetch rg for Codex packages @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23573 Remove unused ARC monitor path @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23541 build: default Codex package target and output @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23358 Fan out rust-ci-full nextest by platform @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23593 feat: expose codex-app-server version flag @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23564 [codex] Preserve raw code-mode exec output by default @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23586 build: package prebuilt Codex entrypoints @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23582 ci: build Codex package archives in release workflow @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23596 runtime: detect Codex package layout @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23500 add encryptedcontent to functioncalloutput @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23633 Migrate exec-server remote registration to environments @richardopenai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23667 feat: rename 1 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23669 feat: rename 3 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23668 feat: rename 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23675 fix: main @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23685 feat: wire goal extension tools to the dedicated goal store @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23690 feat: async approval contrib @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23692 feat: async turn item process @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23605 [codex] Hide deferred tools from code mode prompt @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23635 release: publish Codex package archive checksums @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23696 feat: account active goal progress in the goal extension @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23176 [2 of 2] Start fresh TUI thread in background @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23502 Add thread/settings/update app-server API @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23507 Sync TUI thread settings through app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23666 feat: add turn_id and truncation_policy to extension tool calls
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23636 install: consume Codex package archives @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23717 [codex] Preserve failed goal accounting flushes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23655 add standalone websearch api client @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23724 Fix thread settings clippy failure @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23637 npm: ship platform packages in Codex package layout @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23729 fix(config): resolve cloud requirements deny-read globs @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23638 dotslash: publish Codex entrypoints from package archives @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23719 cli: add strict config to exec-server @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23752 release: use DotSlash zstd for package archives @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23761 chore: use Codex Linux runners for Rust releases @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23759 release: package prebuilt resource binaries @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22873 Add SubagentStop hook @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23732 Make goals feature on by default and no longer experimental @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23537 Honor client-resolved service tier defaults @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23771 [codex] Fix realtime v1 websocket compatibility @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23760 ci: run Codex package builder tests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#18240 Use named MITM permissions config @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23774 [codex] Reject read-only fallback with approvals disabled @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 79-other-changes-in-rust-v0-133-0
  source_release: codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc
  source_type: github_releases
  theme: uncategorized
  title: 79 other changes in rust-v0.133.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc]]'
source_type: github_releases
theme: uncategorized
title: 79 other changes in rust-v0.133.0
type: change
---

<!-- chronolog:begin region="header" -->
# 79 other changes in rust-v0.133.0

**Codex CLI** · 2026-05-21 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.133.0) · from [[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|0.133.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved release and CI reliability with package-builder tests, prebuilt resource packaging, DotSlash zstd handling, platform-sharded Rust tests, and Codex Linux release runners. (#23760, #23759, #23752, #23358, #23761)

> #22380 fix: default unknown tool schemas to empty schemas @celia-oai

> #23309 Add tool lifecycle extension contributor @jif-oai

> #23253 Reduce rust-ci-full Windows nextest timeout flakes @starr-openai

> #21812 Publish Linux runtime wheels with glibc-compatible tags @aibrahim-oai

> #22709 [codex] Trim unused TurnContextItem fields @pakrym-oai

> #22728 [codex] Move pending input into input queue @pakrym-oai

> #23371 fix(tui): warn on unsupported iTerm2 pet versions @fcoury-oai

> #23376 [codex-analytics] preserve user thread source for exec threads @marksteinbrick-oai

> #23384 [codex] Remove external websocket session resets @pakrym-oai

> #22721 cleanup: Remove skill env var dependency prompting @xl-openai

> #23389 Remove ToolSearch feature toggle @sayan-oai

> #23080 [1 of 7] Add thread settings to UserInput @etraut-openai

> #23081 [2 of 7] Remove UserInputWithTurnContext @etraut-openai

> #23075 [3 of 7] Remove UserTurn @etraut-openai

> #22508 [5 of 7] Replace OverrideTurnContext with ThreadSettings @etraut-openai

> #22086 CI: Customize v8 building @cconger

> #23300 feat: dedicated goal DB @jif-oai

> #22835 Remove ToolsConfig from tool planning @jif-oai

> #23409 [codex] Allow empty turn/start requests @pakrym-oai

> #23388 [codex] Move hook request plumbing into hook runtime @pakrym-oai

> #23405 [codex] Preserve steer input as user input @pakrym-oai

> #22914 [2 of 4] tui: route app and skill enablement through app server @etraut-openai

> #23397 [codex] Make contextual user fragments dyn-renderable @pakrym-oai

> #22929 Harden CLI rate limit window labels @ase-openai

> #22782 Add SubagentStart hook @abhinav-oai

> #23513 build: add Codex package builder @bolinfest

> #23369 Make local environment optional in EnvironmentManager @starr-openai

> #23327 Refactor exec-server websocket pump @starr-openai

> #23536 fix(tui): preserve modified enter in plan questions @fcoury-oai

> #23400 Fix empty rollout path app-server handling @wiltzius-openai

> #23551 Route local-only app-server gating through processors @starr-openai

> #23516 fix: serialize unix app-server startup @efrazer-oai

> #22169 [codex] Honor role-defined spawn service tiers @aibrahim-oai

> #23555 Add CUA requirements subsection for locked computer use @adams-oai

> #23538 Fix: TUI starting in wrong CWD @canvrno-oai

> #23526 build: fetch rg for Codex packages @bolinfest

> #23573 Remove unused ARC monitor path @mzeng-openai

> #23541 build: default Codex package target and output @bolinfest

> #23358 Fan out rust-ci-full nextest by platform @starr-openai

> #23593 feat: expose codex-app-server version flag @bolinfest

> #23564 [codex] Preserve raw code-mode exec output by default @aibrahim-oai

> #23586 build: package prebuilt Codex entrypoints @bolinfest

> #23582 ci: build Codex package archives in release workflow @bolinfest

> #23596 runtime: detect Codex package layout @bolinfest

> #23500 add encryptedcontent to functioncalloutput @sayan-oai

> #23633 Migrate exec-server remote registration to environments @richardopenai

> #23667 feat: rename 1 @jif-oai

> #23669 feat: rename 3 @jif-oai

> #23668 feat: rename 2 @jif-oai

> #23675 fix: main @jif-oai

> #23685 feat: wire goal extension tools to the dedicated goal store @jif-oai

> #23690 feat: async approval contrib @jif-oai

> #23692 feat: async turn item process @jif-oai

> #23605 [codex] Hide deferred tools from code mode prompt @pakrym-oai

> #23635 release: publish Codex package archive checksums @bolinfest

> #23696 feat: account active goal progress in the goal extension @jif-oai

> #23176 [2 of 2] Start fresh TUI thread in background @etraut-openai

> #23502 Add thread/settings/update app-server API @etraut-openai

> #23507 Sync TUI thread settings through app server @etraut-openai

> #23666 feat: add turn_id and truncation_policy to extension tool calls @jif-oai

> #23636 install: consume Codex package archives @bolinfest

> #23717 [codex] Preserve failed goal accounting flushes @jif-oai

> #23655 add standalone websearch api client @sayan-oai

> #23724 Fix thread settings clippy failure @etraut-openai

> #23637 npm: ship platform packages in Codex package layout @bolinfest

> #23729 fix(config): resolve cloud requirements deny-read globs @viyatb-oai

> #23638 dotslash: publish Codex entrypoints from package archives @bolinfest

> #23719 cli: add strict config to exec-server @bolinfest

> #23752 release: use DotSlash zstd for package archives @bolinfest

> #23761 chore: use Codex Linux runners for Rust releases @bolinfest

> #23759 release: package prebuilt resource binaries @bolinfest

> #22873 Add SubagentStop hook @abhinav-oai

> #23732 Make goals feature on by default and no longer experimental @etraut-openai

> #23537 Honor client-resolved service tier defaults @shijie-oai

> #23771 [codex] Fix realtime v1 websocket compatibility @guinness-oai

> #23760 ci: run Codex package builder tests @bolinfest

> #18240 Use named MITM permissions config @evawong-oai

> #23774 [codex] Reject read-only fallback with approvals disabled @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.133.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-21-7-agent-mode-changes-in-rust-v0-133-0|7 Agent Mode changes in rust-v0.133.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-21-20-apps-and-integrations-changes-in-rust-v0-133-0|20 Apps and Integrations changes in rust-v0.133.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-21-5-context-window-changes-in-rust-v0-133-0|5 Context Window changes in rust-v0.133.0]] · Context Window
- [[Changes/Codex CLI/2026-05-21-3-developer-workflow-changes-in-rust-v0-133-0|3 Developer Workflow changes in rust-v0.133.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-21-18868-add-mitm-hook-config-model-evawong-oai|♯18868 Add MITM hook config model @evawong-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-21-23578-fix-app-server-speed-up-shutdown-fcoury-oai|♯23578 fix(app-server): speed up shutdown @fcoury-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17 Safety and Privacy changes in rust-v0.133.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-21-goals-are-now-enabled-by-default-backed-by-dedicated-storage-and-track-progress|Goals are now enabled by default, backed by dedicated storage, and track progress…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-21-b3da23&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-21-79-other-changes-in-rust-v0-133-0.md%0ACard%20ID%3A%20codex-cli-2026-05-21-b3da23%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.133.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->