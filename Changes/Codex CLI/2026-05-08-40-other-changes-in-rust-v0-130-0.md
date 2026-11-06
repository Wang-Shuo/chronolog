---
card_id: codex-cli-2026-05-08-fb880a
date: '2026-05-08'
description: 'Codex CLI · 2026-05-08 · Other changes: 40 changes in 0.130.0 — App-server
  clients can page large threads with unloaded, summary, or full turn item views…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 05764711416e8a3e945f022d1aa6d83432ba8a083c2c30c94568e78aadbb4704
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-08-fb880a
  comparison: ''
  date: '2026-05-08'
  description: 'Codex CLI — 0.130.0: 40 other changes'
  evidence:
  - quote: App-server clients can page large threads with unloaded, summary, or full
      turn item views. (#21566)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '`view_image` can resolve files through the selected environment for multi-environment
      sessions. (#21143)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: Live app-server threads now pick up config changes without requiring a
      restart. (#21187)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: 'Turn diffs stay accurate across apply-patch operations, including partial
      failures that still mutated files. (#21180, #21518)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: 'Thread summaries, renames, resume, and fork paths work better through
      `ThreadStore`, including threads without local rollout paths. (#21264, #21265,
      #21266)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: Removed stale “research preview” wording from the `codex exec` startup
      banner. (#21683)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: Updated install and tooling docs to consistently use `cargo install --locked`.
      (#21592)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: 'Hardened dependency and CI hygiene with fully qualified GitHub Action
      pins, a Dependabot cooldown, and a `cargo-shear` upgrade. (#21436, #21547, #21599)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21494 [codex] fix PluginListParams test initializer @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21356 feat: make built-in MCPs first-class runtime servers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21498 [codex] add account id to feedback uploads @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21487 device-key: clean up unused crate @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21518 fix: preserve exact turn diffs after partial apply_patch failures
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#18747 [codex-analytics] add tool review event schema @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21187 app-server: refresh live threads from latest config snapshot @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21461 [codex] Move tool specs onto handlers @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21547 Upgrade `cargo-shear` to 1.11.2 @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21266 [codex] Fix pathless thread summaries @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21265 Route ThreadManager rollout path reads through thread store @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21582 Use descriptive names for Cargo profile options @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21574 Add a Cargo build profile for benchmarking @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21436 [codex] Fully qualify hash-pins in GitHub Actions @ww-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21592 Ensure all mentions of cargo-install are --locked @gankra-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21584 Disable empty Cargo test targets @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21566 feat(app-server, threadstore): Thread pagination APIs and ThreadStore
      contract @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21556 codex-otel: add configurable trace metadata @bbrown-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21599 [codex] Apply a Dependabot cooldown of 7 days @ww-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21602 Use `--locked` in cargo build and lint invocations @zanie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#20664 Add stdio exec-server client transport @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21596 [codex] Remove remote thread store implementation @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21143 Route view_image through selected environments @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#20666 Add CODEX_HOME environments TOML provider @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21646 Revert "Use `--locked` in cargo build and lint invocations" @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21434 [codex-analytics] plumb protocol-native review timing @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21485 Remove skills list extra roots @xli-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21685 Fix duplicate CLI issue template description @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21686 Fix issue template labels @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21688 Fix feature request Contributing link @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21683 Remove exec research preview banner wording @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  - quote: '#21676 Omit service_tier from remote /responses/compact requests under
      API auth @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.130.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 40-other-changes-in-rust-v0-130-0
  source_release: codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9
  source_type: github_releases
  theme: uncategorized
  title: 40 other changes in rust-v0.130.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9|codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9]]'
source_type: github_releases
theme: uncategorized
title: 40 other changes in rust-v0.130.0
type: change
---

<!-- chronolog:begin region="header" -->
# 40 other changes in rust-v0.130.0

**Codex CLI** · 2026-05-08 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.130.0) · from [[Releases/Codex CLI/codex-cli-2026-05-08-rust-v0-130-0-github-319777370-eab676f9|0.130.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App-server clients can page large threads with unloaded, summary, or full turn item views. (#21566)

> `view_image` can resolve files through the selected environment for multi-environment sessions. (#21143)

> Live app-server threads now pick up config changes without requiring a restart. (#21187)

> Turn diffs stay accurate across apply-patch operations, including partial failures that still mutated files. (#21180, #21518)

> Thread summaries, renames, resume, and fork paths work better through `ThreadStore`, including threads without local rollout paths. (#21264, #21265, #21266)

> Removed stale “research preview” wording from the `codex exec` startup banner. (#21683)

> Updated install and tooling docs to consistently use `cargo install --locked`. (#21592)

> Hardened dependency and CI hygiene with fully qualified GitHub Action pins, a Dependabot cooldown, and a `cargo-shear` upgrade. (#21436, #21547, #21599)

> #21494 [codex] fix PluginListParams test initializer @xli-oai

> #21356 feat: make built-in MCPs first-class runtime servers @jif-oai

> #21498 [codex] add account id to feedback uploads @pakrym-oai

> #21487 device-key: clean up unused crate @euroelessar

> #21518 fix: preserve exact turn diffs after partial apply_patch failures @jif-oai

> #18747 [codex-analytics] add tool review event schema @rhan-oai

> #21187 app-server: refresh live threads from latest config snapshot @jif-oai

> #21461 [codex] Move tool specs onto handlers @pakrym-oai

> #21547 Upgrade `cargo-shear` to 1.11.2 @charliemarsh-oai

> #21266 [codex] Fix pathless thread summaries @wiltzius-openai

> #21265 Route ThreadManager rollout path reads through thread store @wiltzius-openai

> #21582 Use descriptive names for Cargo profile options @zanie-oai

> #21574 Add a Cargo build profile for benchmarking @zanie-oai

> #21436 [codex] Fully qualify hash-pins in GitHub Actions @ww-oai

> #21592 Ensure all mentions of cargo-install are --locked @gankra-oai

> #21584 Disable empty Cargo test targets @charliemarsh-oai

> #21566 feat(app-server, threadstore): Thread pagination APIs and ThreadStore contract @owenlin0

> #21556 codex-otel: add configurable trace metadata @bbrown-oai

> #21599 [codex] Apply a Dependabot cooldown of 7 days @ww-oai

> #21602 Use `--locked` in cargo build and lint invocations @zanie-oai

> #20664 Add stdio exec-server client transport @starr-openai

> #21596 [codex] Remove remote thread store implementation @wiltzius-openai

> #21143 Route view_image through selected environments @starr-openai

> #20666 Add CODEX_HOME environments TOML provider @starr-openai

> #21646 Revert "Use `--locked` in cargo build and lint invocations" @pakrym-oai

> #21434 [codex-analytics] plumb protocol-native review timing @rhan-oai

> #21485 Remove skills list extra roots @xli-oai

> #21685 Fix duplicate CLI issue template description @etraut-openai

> #21686 Fix issue template labels @etraut-openai

> #21688 Fix feature request Contributing link @etraut-openai

> #21683 Remove exec research preview banner wording @etraut-openai

> #21676 Omit service_tier from remote /responses/compact requests under API auth @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.130.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-08-20665-make-environment-providers-own-default-selection-starr-openai|♯20665 Make environment providers own default selection @starr-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-05-08-2-context-window-changes-in-rust-v0-130-0|2 Context Window changes in rust-v0.130.0]] · Context Window
- [[Changes/Codex CLI/2026-05-08-2-editor-experience-changes-in-rust-v0-130-0|2 Editor Experience changes in rust-v0.130.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-08-2-safety-and-privacy-changes-in-rust-v0-130-0|2 Safety and Privacy changes in rust-v0.130.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-08-8-apps-and-integrations-changes-in-rust-v0-130-0|8 Apps and Integrations changes in rust-v0.130.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-08-2-account-and-access-changes-in-rust-v0-130-0|2 Account and Access changes in rust-v0.130.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-08-added-configurable-opentelemetry-trace-metadata-and-richer-review-feedback-analy|Added configurable OpenTelemetry trace metadata and richer review/feedback analytics…]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-08-added-a-faster-cargo-profiling-build-profile-and-disabled-empty-doctest-targets|Added a faster Cargo profiling build profile and disabled empty doctest targets…]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-08-fb880a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-08-40-other-changes-in-rust-v0-130-0.md%0ACard%20ID%3A%20codex-cli-2026-05-08-fb880a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.130.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->