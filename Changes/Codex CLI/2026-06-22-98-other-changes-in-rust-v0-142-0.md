---
card_id: codex-cli-2026-06-22-3f6b69
date: '2026-06-22'
description: 'Codex CLI · 2026-06-22 · Other changes: 98 changes in 0.142.0 — Codex
  can now receive scheduled UTC time reminders and query the current time directly…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8117917a20a9a862c2b4240167f9010c03086d64f86f6d6c8a0a0d2a7a247765
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-22-3f6b69
  comparison: ''
  date: '2026-06-22'
  description: 'Codex CLI — 0.142.0: 98 other changes'
  evidence:
  - quote: 'Codex can now receive scheduled UTC time reminders and query the current
      time directly, including through client-provided app-server clocks. (#28822,
      #28824, #28835, #29011)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: Goal-first threads are once again persisted and returned by `thread/list`
      and `thread/search`. (#28808)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: 'Reduced persistent-log churn by removing per-event WebSocket payload logging
      and filtering duplicated telemetry records. (#29432, #29457)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27751 [codex] expose Bedrock credential source in account/read @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28338 [codex] Compress cold active rollouts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28473 path-uri: clarify invalid host path errors @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28342 fix(tui): restore TUI after suspend @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28354 [codex] exec-server: stream files in chunks @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28553 chore: side prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28554 fix(tui): highlight C++ module files @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28467 [codex] Warn clearly when code mode output is truncated @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27750 [codex] Add incremental thread history changes @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28154 feat(tui): add rate-limit reset redemption to /usage @jayp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28562 ci: run code-mode unit tests on all bazel targets @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28468 code-mode: extend test coverage to lock in cell lifecycle @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28587 [codex] test exec relative additional permissions @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28589 Record invariants for path migration. @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28146 app-server: preserve target-native environment cwd @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28595 Tell codex about PathUri serde compat. @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28152 core: render remote environment cwd natively @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#26706 PAC 1 - Add system proxy feature config surface @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28627 Revert "Tell codex about PathUri serde compat. (#28595)" @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28642 thread-store: fix response fixture compilation @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28599 code-mode: move cell state into library actor @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28471 [codex] Test code-mode variable truncation @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28638 core: remove redundant TurnContext and Prompt fields @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28656 [codex] Persist built-in image results reported as generating @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28512 Resume exec-server sessions after disconnect @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28546 Back off registry retries during exec recovery @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28705 Replace SkillsManager with SkillsService @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28628 [codex] Repair invalid skill frontmatter scalars @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28632 Tell codex to avoid changing rollout format. @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#19047 feat: add run task identity primitives @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28671 [codex] Restore thread recency with compatible migration history
      @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28389 [codex] Use compact OpenAI docs search queries @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28681 unified-exec: preserve PathUri through exec-server @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28651 exec-server: expose environment registry payloads @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28778 path-uri: decouple native path parsing @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28774 feat(exec-server): add Noise rendezvous environment @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28812 [codex] Add optional IDs to response items @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28784 fix(install): support older awk checksum parsing @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28826 [codex] Use unique IDs for realtime-routed turns @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27986 [codex] control automatic realtime handoff delivery @jiayuhuang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28836 [codex] Support assistant realtime append text @guinness-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28374 Refresh signed exec-server URLs on reconnect @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28851 Record more path migration guidance for codex. @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28746 [codex] add rollout token budget configuration (1/N) @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28766 Add network environment ID plumbing @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28813 Pause active goals before TUI interrupts @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28895 Recover exec process stdin writes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28940 Pin Windows argument lint to Windows 2022 @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28808 Fix goal-first live threads missing from thread/list @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#25019 [codex] Initialize exec-server OpenTelemetry at startup @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28946 Synchronize realtime notification test requests @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28822 Add Config for Time Reminders (1/n) @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28494 [codex] rollout budget implementation (2/N) @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27500 Support `openai/form` extended form elicitations @gpeal'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28949 [codex] Make thread store turn filter optional @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28824 current time reminders impl for system clock (2/n) @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28854 apply-patch: carry paths as PathUri @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28835 Add app-server current-time impl (3/n) @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28947 [codex] Remove hardcoded app ID filters @ericning-o'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28856 Always use AVAS for realtime WebRTC calls @bakks'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28814 [codex] Assign response item IDs when recording history @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29011 [codex] add clock current-time tool @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29012 core: assign item IDs to compacted replacement history @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28674 [1/3] core: add remote environment connection lifecycle @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28683 [2/3] core: track starting environments in snapshots @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29025 [3/3] app-server: configure environment connection timeout @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28707 [codex] abort turns when rollout budgets expire (token budget 3/3)
      @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28899 Scope network approvals by environment @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29099 Keep remote exec commands native to the executor @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29095 Use cached and live web access terminology @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29132 chore(deps): advance tokio-tungstenite @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29325 Test pipelined scalar exec-server requests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29326 Parallelize skill metadata stats @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29329 Use controlled time for remote initialization timeout test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29170 code-mode: define transport-neutral runtime types @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29285 code-mode: move session ownership into runtime @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29287 code-mode: make session shutdown authoritative @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29301 [prompting] updated plan mode prompt @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29288 code-mode: preserve dropped observation output @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29327 Persist session IDs across thread resume @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29001 Add workspace messages app-server API @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29432 Stop logging every Responses WebSocket event @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29455 fix(core): restore thread_source in x-codex-turn-metadata @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29457 Filter noisy targets from persistent logs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29429 remove flag for image preparation @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29143 ci: restore custom Windows runner with hermetic LLVM 0.7.9 @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28968 core: rename metadata -> internal_chat_message_metadata_passthrough
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28793 [codex] Fix usage-limit reset copy and state @jayp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27982 [codex] Start the guardian child session when parent session is
      started @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29468 core: remove unused permissions cwd plumbing @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28991 Allow ChatGPT accounts without email @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29423 [codex] configure rollout budget reminder thresholds @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29476 [codex] handle request_user_input in app-server test client @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29014 Honor startup custom CA bundles with managed MITM @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29480 chore: advance tungstenite fork pins @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 98-other-changes-in-rust-v0-142-0
  source_release: codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e
  source_type: github_releases
  theme: uncategorized
  title: 98 other changes in rust-v0.142.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e]]'
source_type: github_releases
theme: uncategorized
title: 98 other changes in rust-v0.142.0
type: change
---

<!-- chronolog:begin region="header" -->
# 98 other changes in rust-v0.142.0

**Codex CLI** · 2026-06-22 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.0) · from [[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|0.142.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Codex can now receive scheduled UTC time reminders and query the current time directly, including through client-provided app-server clocks. (#28822, #28824, #28835, #29011)

> Goal-first threads are once again persisted and returned by `thread/list` and `thread/search`. (#28808)

> Reduced persistent-log churn by removing per-event WebSocket payload logging and filtering duplicated telemetry records. (#29432, #29457)

> #27751 [codex] expose Bedrock credential source in account/read @celia-oai

> #28338 [codex] Compress cold active rollouts @jif-oai

> #28473 path-uri: clarify invalid host path errors @anp-oai

> #28342 fix(tui): restore TUI after suspend @fcoury-oai

> #28354 [codex] exec-server: stream files in chunks @pakrym-oai

> #28553 chore: side prompt @jif-oai

> #28554 fix(tui): highlight C++ module files @fcoury-oai

> #28467 [codex] Warn clearly when code mode output is truncated @aibrahim-oai

> #27750 [codex] Add incremental thread history changes @wiltzius-openai

> #28154 feat(tui): add rate-limit reset redemption to /usage @jayp-oai

> #28562 ci: run code-mode unit tests on all bazel targets @cconger

> #28468 code-mode: extend test coverage to lock in cell lifecycle @cconger

> #28587 [codex] test exec relative additional permissions @anp-oai

> #28589 Record invariants for path migration. @anp-oai

> #28146 app-server: preserve target-native environment cwd @anp-oai

> #28595 Tell codex about PathUri serde compat. @anp-oai

> #28152 core: render remote environment cwd natively @anp-oai

> #26706 PAC 1 - Add system proxy feature config surface @canvrno-oai

> #28627 Revert "Tell codex about PathUri serde compat. (#28595)" @anp-oai

> #28642 thread-store: fix response fixture compilation @pakrym-oai

> #28599 code-mode: move cell state into library actor @cconger

> #28471 [codex] Test code-mode variable truncation @aibrahim-oai

> #28638 core: remove redundant TurnContext and Prompt fields @pakrym-oai

> #28656 [codex] Persist built-in image results reported as generating @won-openai

> #28512 Resume exec-server sessions after disconnect @jif-oai

> #28546 Back off registry retries during exec recovery @jif-oai

> #28705 Replace SkillsManager with SkillsService @jif-oai

> #28628 [codex] Repair invalid skill frontmatter scalars @charlesgong-openai

> #28632 Tell codex to avoid changing rollout format. @anp-oai

> #19047 feat: add run task identity primitives @adrian-openai

> #28671 [codex] Restore thread recency with compatible migration history @nornagon-openai

> #28389 [codex] Use compact OpenAI docs search queries @kkahadze-oai

> #28681 unified-exec: preserve PathUri through exec-server @anp-oai

> #28651 exec-server: expose environment registry payloads @viyatb-oai

> #28778 path-uri: decouple native path parsing @anp-oai

> #28774 feat(exec-server): add Noise rendezvous environment @apanasenko-oai

> #28812 [codex] Add optional IDs to response items @pakrym-oai

> #28784 fix(install): support older awk checksum parsing @fcoury-oai

> #28826 [codex] Use unique IDs for realtime-routed turns @guinness-oai

> #27986 [codex] control automatic realtime handoff delivery @jiayuhuang-openai

> #28836 [codex] Support assistant realtime append text @guinness-oai

> #28374 Refresh signed exec-server URLs on reconnect @apanasenko-oai

> #28851 Record more path migration guidance for codex. @anp-oai

> #28746 [codex] add rollout token budget configuration (1/N) @rka-oai

> #28766 Add network environment ID plumbing @jif-oai

> #28813 Pause active goals before TUI interrupts @etraut-openai

> #28895 Recover exec process stdin writes @jif-oai

> #28940 Pin Windows argument lint to Windows 2022 @rka-oai

> #28808 Fix goal-first live threads missing from thread/list @etraut-openai

> #25019 [codex] Initialize exec-server OpenTelemetry at startup @starr-openai

> #28946 Synchronize realtime notification test requests @rka-oai

> #28822 Add Config for Time Reminders (1/n) @rka-oai

> #28494 [codex] rollout budget implementation (2/N) @rka-oai

> #27500 Support `openai/form` extended form elicitations @gpeal

> #28949 [codex] Make thread store turn filter optional @wiltzius-openai

> #28824 current time reminders impl for system clock (2/n) @rka-oai

> #28854 apply-patch: carry paths as PathUri @anp-oai

> #28835 Add app-server current-time impl (3/n) @rka-oai

> #28947 [codex] Remove hardcoded app ID filters @ericning-o

> #28856 Always use AVAS for realtime WebRTC calls @bakks

> #28814 [codex] Assign response item IDs when recording history @pakrym-oai

> #29011 [codex] add clock current-time tool @rka-oai

> #29012 core: assign item IDs to compacted replacement history @pakrym-oai

> #28674 [1/3] core: add remote environment connection lifecycle @sayan-oai

> #28683 [2/3] core: track starting environments in snapshots @sayan-oai

> #29025 [3/3] app-server: configure environment connection timeout @sayan-oai

> #28707 [codex] abort turns when rollout budgets expire (token budget 3/3) @rka-oai

> #28899 Scope network approvals by environment @jif-oai

> #29099 Keep remote exec commands native to the executor @jif-oai

> #29095 Use cached and live web access terminology @winston-openai

> #29132 chore(deps): advance tokio-tungstenite @apanasenko-oai

> #29325 Test pipelined scalar exec-server requests @jif-oai

> #29326 Parallelize skill metadata stats @jif-oai

> #29329 Use controlled time for remote initialization timeout test @jif-oai

> #29170 code-mode: define transport-neutral runtime types @cconger

> #29285 code-mode: move session ownership into runtime @cconger

> #29287 code-mode: make session shutdown authoritative @cconger

> #29301 [prompting] updated plan mode prompt @rhan-oai

> #29288 code-mode: preserve dropped observation output @cconger

> #29327 Persist session IDs across thread resume @jif-oai

> #29001 Add workspace messages app-server API @xli-oai

> #29432 Stop logging every Responses WebSocket event @jif-oai

> #29455 fix(core): restore thread_source in x-codex-turn-metadata @owenlin0

> #29457 Filter noisy targets from persistent logs @jif-oai

> #29429 remove flag for image preparation @rka-oai

> #29143 ci: restore custom Windows runner with hermetic LLVM 0.7.9 @anp-oai

> #28968 core: rename metadata -> internal_chat_message_metadata_passthrough @owenlin0

> #28793 [codex] Fix usage-limit reset copy and state @jayp-oai

> #27982 [codex] Start the guardian child session when parent session is started @jgershen-oai

> #29468 core: remove unused permissions cwd plumbing @bolinfest

> #28991 Allow ChatGPT accounts without email @efrazer-oai

> #29423 [codex] configure rollout budget reminder thresholds @rka-oai

> #29476 [codex] handle request_user_input in app-server test client @celia-oai

> #29014 Honor startup custom CA bundles with managed MITM @winston-openai

> #29480 chore: advance tungstenite fork pins @apanasenko-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-22-12-safety-and-privacy-changes-in-rust-v0-142-0|12 Safety and Privacy changes in rust-v0.142.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-22-4-interface-experience-changes-in-rust-v0-142-0|4 Interface Experience changes in rust-v0.142.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-22-26496-make-auto-review-on-request-prompt-more-proactive-maja-openai|♯26496 Make auto-review on-request prompt more proactive @maja-openai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-22-usage-can-now-show-and-redeem-earned-usage-limit-reset-credits-with-confirmation|/usage can now show and redeem earned usage-limit reset credits…]] · Pricing Model
- [[Changes/Codex CLI/2026-06-22-28791-bazel-refresh-expired-macos-sdk-pin-anp-oai|♯28791 bazel: refresh expired macOS SDK pin @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent Mode changes in rust-v0.142.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-22-26707-pac-2-add-shared-auth-system-proxy-contract-canvrno-oai|♯26707 PAC 2 - Add shared auth system proxy contract @canvrno-oai]] · Collaboration
- [[Changes/Codex CLI/2026-06-22-4-developer-workflow-changes-in-rust-v0-142-0|4 Developer Workflow changes in rust-v0.142.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-22-10-context-window-changes-in-rust-v0-142-0|10 Context Window changes in rust-v0.142.0]] · Context Window
- [[Changes/Codex CLI/2026-06-22-29289-code-mode-preserve-initial-yield-at-completion-cconger|♯29289 code-mode: preserve initial yield at completion @cconger]] · Editor Experience
- [[Changes/Codex CLI/2026-06-22-2-reliability-and-performance-changes-in-rust-v0-142-0|2 Reliability and Performance changes in rust-v0.142.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-22-37-apps-and-integrations-changes-in-rust-v0-142-0|37 Apps and Integrations changes in rust-v0.142.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-22-29022-codex-support-protected-resource-oauth-discovery-xl-openai|♯29022 codex Support protected resource OAuth discovery @xl-openai]] · Account and Access
- [[Changes/Codex CLI/2026-06-22-28770-connectors-ignore-synthetic-links-for-app-accessibility-adaley-openai|♯28770 connectors Ignore synthetic links for app accessibility @adaley-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-06-22-29086-document-raw-response-item-compatibility-jif-oai|♯29086 Document raw response item compatibility @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-22-3-model-support-changes-in-rust-v0-142-0|3 Model Support changes in rust-v0.142.0]] · Model Support
- [[Changes/Codex CLI/2026-06-22-2-search-and-browsing-changes-in-rust-v0-142-0|2 Search and Browsing changes in rust-v0.142.0]] · Search and Browsing
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-22-3f6b69&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-22-98-other-changes-in-rust-v0-142-0.md%0ACard%20ID%3A%20codex-cli-2026-06-22-3f6b69%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->