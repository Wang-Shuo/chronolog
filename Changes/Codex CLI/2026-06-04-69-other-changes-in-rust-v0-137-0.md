---
card_id: codex-cli-2026-06-04-946018
date: '2026-06-04'
description: 'Codex CLI · 2026-06-04 · Other changes: 69 changes in 0.137.0 — Hosted
  web and image tools are available in more code-mode flows, with standalone web searches…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 068771618265bfc9628f33c0850d7c578de587c87e2e84fde9aeb99e203eb94a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-04-946018
  comparison: ''
  date: '2026-06-04'
  description: 'Codex CLI — 0.137.0: 69 other changes'
  evidence:
  - quote: 'Hosted web and image tools are available in more code-mode flows, with
      standalone web searches able to run in parallel (#25176, #25702, #25890, #25923).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: 'Root formatting and Justfile workflows are more complete and Windows-aware
      (#24983, #25165, #25683).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: Bazel CI’s BuildBuddy wrapper was reintroduced with Windows-safe process
      handling and validation (#25915).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25329 feat(tui): allow function keys through f24 in keymaps @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24617 Add config bundle transport types @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25435 Add build_unsigned_archive release mode @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24619 Compose requirements layers @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24620 Add cloud-managed config layer support @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25462 Revert "Add build_unsigned_archive release mode" @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25113 store and expose parent_thread_id on Threads @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25060 Add goal extension idle continuation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25576 Use templates for goal steering prompts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25577 Remove Plan-mode gate from idle turn injection @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25096 Add goal extension GoalApi @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25087 Read compressed rollouts and materialize before append @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25628 [codex] fix compressed rollout fixture SessionMeta initialization
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25316 feat(tui): restore output-free cancelled prompts @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25624 Preserve renamed thread titles during reconciliation @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25089 Compress cold local rollouts @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25603 [codex] Inherit raw events for spawned child listeners @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25655 nit: drop todo @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25654 Parallelize cold rollout compression @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25121 exec-server: add environment path refs @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24983 [codex] Make justfile recipes Windows-aware @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25659 Throttle repeated rollout compression runs @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25165 Check root Python script formatting in CI @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25149 exec-server: canonicalize bound filesystem paths @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25669 fix: deflake zsh-fork approval test @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24979 feat: gate unified exec zsh fork composition @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25679 Add rollout compression counters @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25680 Add rollout compression histograms @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25689 [codex] Generalize deferred nested tool guidance @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25690 Add Python version compatibility guidance @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25701 fix: rename McpServer to TestAppServer @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25684 Move tool search metadata onto ToolExecutor @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25625 fix(tui): clarify footer shortcut overlay hints @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25649 [codex] Publish release symbol artifacts @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25661 Reject directory rollout paths for pathless side chats @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#22668 Wire managed MITM CA trust into child env @winston-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25712 app-server: remove experimental persist_extended_history bool flag
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24621 Move cloud requirements crate to cloud config @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25683 [codex] Add comprehensive root formatting check @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25814 feat: reuse compressed rollout search snippets @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25840 fix: main oops @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25724 Test runtime selector before first turn @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25844 Reduce stack pressure in session startup and config rebuilds @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25847 Run Codex async main on a sized stack @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25868 Skip startup prewarm when websockets are disabled @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25707 [codex-analytics] Track CodexErr details in turn analytics @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25858 Add environmentId to request_permissions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25916 Fix Windows release PDB staging @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24859 Use environment secrets for Azure signing @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25509 Fix Windows running thread resume path normalization @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25135 Populate workspace kind on Codex turn events @knittel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#24622 Switch runtime to cloud config bundle @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25911 core: stop passing legacy SandboxPolicy to guardian reviews @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25668 Split cloud config bundle service modules @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25890 [codex] Keep hosted tools visible in code-only mode @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25948 Revert "Use environment secrets for Azure signing" @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25953 feat: add skills extension scaffold @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25915 [codex] Fix Windows BuildBuddy Bazel wrapper execution @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25959 feat: add extension turn-input contributors @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25963 Allow EDU accounts to fetch cloud config bundles @joeflorencio-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25988 revert: publish release symbol artifacts @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26155 fix: serialize goal progress accounting @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26156 chore: mechanical rename @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26167 Implement v1 skills extension prompt injection @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26176 fix: main @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25949 [codex] Restore setup helper UAC manifest @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 69-other-changes-in-rust-v0-137-0
  source_release: codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece
  source_type: github_releases
  theme: uncategorized
  title: 69 other changes in rust-v0.137.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece]]'
source_type: github_releases
theme: uncategorized
title: 69 other changes in rust-v0.137.0
type: change
---

<!-- chronolog:begin region="header" -->
# 69 other changes in rust-v0.137.0

**Codex CLI** · 2026-06-04 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.137.0) · from [[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|0.137.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hosted web and image tools are available in more code-mode flows, with standalone web searches able to run in parallel (#25176, #25702, #25890, #25923).

> Root formatting and Justfile workflows are more complete and Windows-aware (#24983, #25165, #25683).

> Bazel CI’s BuildBuddy wrapper was reintroduced with Windows-safe process handling and validation (#25915).

> #25329 feat(tui): allow function keys through f24 in keymaps @fcoury-oai

> #24617 Add config bundle transport types @joeflorencio-openai

> #25435 Add build_unsigned_archive release mode @shijie-oai

> #24619 Compose requirements layers @joeflorencio-openai

> #24620 Add cloud-managed config layer support @joeflorencio-openai

> #25462 Revert "Add build_unsigned_archive release mode" @shijie-oai

> #25113 store and expose parent_thread_id on Threads @owenlin0

> #25060 Add goal extension idle continuation @jif-oai

> #25576 Use templates for goal steering prompts @jif-oai

> #25577 Remove Plan-mode gate from idle turn injection @jif-oai

> #25096 Add goal extension GoalApi @jif-oai

> #25087 Read compressed rollouts and materialize before append @jif-oai

> #25628 [codex] fix compressed rollout fixture SessionMeta initialization @fcoury-oai

> #25316 feat(tui): restore output-free cancelled prompts @fcoury-oai

> #25624 Preserve renamed thread titles during reconciliation @jif-oai

> #25089 Compress cold local rollouts @jif-oai

> #25603 [codex] Inherit raw events for spawned child listeners @vivi

> #25655 nit: drop todo @jif-oai

> #25654 Parallelize cold rollout compression @jif-oai

> #25121 exec-server: add environment path refs @starr-openai

> #24983 [codex] Make justfile recipes Windows-aware @iceweasel-oai

> #25659 Throttle repeated rollout compression runs @jif-oai

> #25165 Check root Python script formatting in CI @anp-oai

> #25149 exec-server: canonicalize bound filesystem paths @starr-openai

> #25669 fix: deflake zsh-fork approval test @jif-oai

> #24979 feat: gate unified exec zsh fork composition @bolinfest

> #25679 Add rollout compression counters @jif-oai

> #25680 Add rollout compression histograms @jif-oai

> #25689 [codex] Generalize deferred nested tool guidance @sayan-oai

> #25690 Add Python version compatibility guidance @anp-oai

> #25701 fix: rename McpServer to TestAppServer @bolinfest

> #25684 Move tool search metadata onto ToolExecutor @jif-oai

> #25625 fix(tui): clarify footer shortcut overlay hints @fcoury-oai

> #25649 [codex] Publish release symbol artifacts @nornagon-openai

> #25661 Reject directory rollout paths for pathless side chats @bolinfest

> #22668 Wire managed MITM CA trust into child env @winston-openai

> #25712 app-server: remove experimental persist_extended_history bool flag @owenlin0

> #24621 Move cloud requirements crate to cloud config @joeflorencio-openai

> #25683 [codex] Add comprehensive root formatting check @anp-oai

> #25814 feat: reuse compressed rollout search snippets @jif-oai

> #25840 fix: main oops @jif-oai

> #25724 Test runtime selector before first turn @jif-oai

> #25844 Reduce stack pressure in session startup and config rebuilds @jif-oai

> #25847 Run Codex async main on a sized stack @jif-oai

> #25868 Skip startup prewarm when websockets are disabled @jif-oai

> #25707 [codex-analytics] Track CodexErr details in turn analytics @rhan-oai

> #25858 Add environmentId to request_permissions @jif-oai

> #25916 Fix Windows release PDB staging @shijie-oai

> #24859 Use environment secrets for Azure signing @shijie-oai

> #25509 Fix Windows running thread resume path normalization @etraut-openai

> #25135 Populate workspace kind on Codex turn events @knittel-openai

> #24622 Switch runtime to cloud config bundle @joeflorencio-openai

> #25911 core: stop passing legacy SandboxPolicy to guardian reviews @bolinfest

> #25668 Split cloud config bundle service modules @joeflorencio-openai

> #25890 [codex] Keep hosted tools visible in code-only mode @aibrahim-oai

> #25948 Revert "Use environment secrets for Azure signing" @shijie-oai

> #25953 feat: add skills extension scaffold @jif-oai

> #25915 [codex] Fix Windows BuildBuddy Bazel wrapper execution @anp-oai

> #25959 feat: add extension turn-input contributors @jif-oai

> #25963 Allow EDU accounts to fetch cloud config bundles @joeflorencio-openai

> #25988 revert: publish release symbol artifacts @shijie-oai

> #26155 fix: serialize goal progress accounting @jif-oai

> #26156 chore: mechanical rename @jif-oai

> #26167 Implement v1 skills extension prompt injection @jif-oai

> #26176 fix: main @jif-oai

> #25949 [codex] Restore setup helper UAC manifest @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.137.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-04-6-developer-workflow-changes-in-rust-v0-137-0|6 Developer Workflow changes in rust-v0.137.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-04-25702-codex-enable-parallel-standalone-web-search-calls-sayan-oai|♯25702 codex enable parallel standalone web search calls @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-04-3-image-generation-changes-in-rust-v0-137-0|3 Image Generation changes in rust-v0.137.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-04-2-interface-experience-changes-in-rust-v0-137-0|2 Interface Experience changes in rust-v0.137.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-04-19-apps-and-integrations-changes-in-rust-v0-137-0|19 Apps and Integrations changes in rust-v0.137.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-04-2-enterprise-and-administration-changes-in-rust-v0-137-0|2 Enterprise and Administration changes in rust-v0.137.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-04-local-session-history-is-safer-for-compressed-rollouts-renamed-titles-pathless-s|Local session history is safer for compressed rollouts, renamed titles, pathless…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-06-04-4-collaboration-changes-in-rust-v0-137-0|4 Collaboration changes in rust-v0.137.0]] · Collaboration
- [[Changes/Codex CLI/2026-06-04-3-context-window-changes-in-rust-v0-137-0|3 Context Window changes in rust-v0.137.0]] · Context Window
- [[Changes/Codex CLI/2026-06-04-2-mobile-and-desktop-changes-in-rust-v0-137-0|2 Mobile and Desktop changes in rust-v0.137.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-04-12-agent-mode-changes-in-rust-v0-137-0|12 Agent Mode changes in rust-v0.137.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-04-25682-codex-document-out-of-line-test-module-convention-anp-oai|♯25682 codex document out-of-line test module convention @anp-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-04-3-model-support-changes-in-rust-v0-137-0|3 Model Support changes in rust-v0.137.0]] · Model Support
- [[Changes/Codex CLI/2026-06-04-8-safety-and-privacy-changes-in-rust-v0-137-0|8 Safety and Privacy changes in rust-v0.137.0]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-04-946018&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-04-69-other-changes-in-rust-v0-137-0.md%0ACard%20ID%3A%20codex-cli-2026-06-04-946018%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.137.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->