---
card_id: codex-cli-2026-10-27-ea39c9
date: '2026-10-27'
description: 'Codex CLI · 2026-10-27 · Other changes: 39 changes in 0.165.0 — Added
  experimental attached thread forks to the app-server API. (#56351)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f6f172e1b208c824c6898d9a0c6a377e29d5c07bbe8be96467921064d62f2aee
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-27-ea39c9
  comparison: ''
  date: '2026-10-27'
  description: 'Codex CLI — 0.165.0: 39 other changes'
  evidence:
  - quote: Added experimental attached thread forks to the app-server API. (#56351)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: Kept TUI preferences editable and immediately applicable when execution
      settings are invalid. (#56091)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56081 Cache decrypted Codex auth and managed secrets @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56090 Honor server approval reviewer defaults on fresh TUI startup @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56091 Keep TUI preferences editable when execution settings are invalid
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56097 Prepare TUI startup to accept multiple backend sessions @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56124 Forward Guardian reviewer events to parent raw-event subscribers
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56127 Avoid blocking EMA auth status checks on account refresh @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56154 Add managed network review domains before allow rules @olliem-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56210 Stabilize the marketplace staging cleanup test @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56222 Consolidate Bazel CI setup into `prepare-bazel-ci` @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56236 Make the code mode yield/resume test yield explicitly between phases
      @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56246 Bump Bazelisk to 1.30.0 in the Bazel CI setup action @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56247 Consolidate Rust unit tests under dedicated test modules @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56248 Bump uv to 0.13.5 in CI and release workflows @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56250 Avoid redundant settings checkpoints when resuming threads @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56261 Isolate V8 source dependencies and their C++ runtime settings @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56263 Reject backslashes in HTTP(S) marketplace URL userinfo @willwang-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56265 Add a built-in Google Cloud Vertex AI provider @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56274 Wait for cloud config refresh cancellation in loader lifetime tests
      @goodman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56277 Support bounded request bodies in AWS SigV4 signing @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56280 Group consecutive transcript prompts into one background block
      @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56288 Pin Linux artifact signing to Cosign v3.1.4 @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56290 Lock Python release build tools with uv @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56293 Use fixed-token auth fixtures in Vertex tests @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56297 Mark built-in dummy credentials and strengthen collision checks
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56301 Add TLS forwarding tests for MITM SigV4 requests @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56302 Add hook configuration to environment attachments @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56308 Separate directory and repository scopes in the TUI @bc-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56312 Track accepted conversation history in rollout traces @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56314 Add managed configuration loaders for custom config servers @smurching-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56342 Match rollout trace image content across request snapshots @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56351 Add experimental attached thread forks @btraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56364 Allow callers to set the thread source for sampling @keyz'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56371 Make the Guardian review timeout configurable @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56439 Update `ctutils` from 0.4.2 to 0.4.5 @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56459 Add Guardian V3 feature configuration @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56460 Add Guardian v3 local board helpers @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  - quote: '#56461 Add silent append support to message boards @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.165.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 39-other-changes-in-rust-v0-165-0
  source_release: codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb
  source_type: github_releases
  theme: uncategorized
  title: 39 other changes in rust-v0.165.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb|codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb]]'
source_type: github_releases
theme: uncategorized
title: 39 other changes in rust-v0.165.0
type: change
---

<!-- chronolog:begin region="header" -->
# 39 other changes in rust-v0.165.0

**Codex CLI** · 2026-10-27 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.165.0) · from [[Releases/Codex CLI/codex-cli-2026-10-27-rust-v0-165-0-github-425927431-1fa685eb|0.165.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added experimental attached thread forks to the app-server API. (#56351)

> Kept TUI preferences editable and immediately applicable when execution settings are invalid. (#56091)

> #56081 Cache decrypted Codex auth and managed secrets @celia-oai

> #56090 Honor server approval reviewer defaults on fresh TUI startup @etraut-openai

> #56091 Keep TUI preferences editable when execution settings are invalid @etraut-openai

> #56097 Prepare TUI startup to accept multiple backend sessions @bc-openai

> #56124 Forward Guardian reviewer events to parent raw-event subscribers @jif-oai

> #56127 Avoid blocking EMA auth status checks on account refresh @jif-oai

> #56154 Add managed network review domains before allow rules @olliem-oai

> #56210 Stabilize the marketplace staging cleanup test @felixxia-oai

> #56222 Consolidate Bazel CI setup into `prepare-bazel-ci` @anp-oai

> #56236 Make the code mode yield/resume test yield explicitly between phases @goodman-oai

> #56246 Bump Bazelisk to 1.30.0 in the Bazel CI setup action @anp-oai

> #56247 Consolidate Rust unit tests under dedicated test modules @dkovalenko-oai

> #56248 Bump uv to 0.13.5 in CI and release workflows @anp-oai

> #56250 Avoid redundant settings checkpoints when resuming threads @owenlin0

> #56261 Isolate V8 source dependencies and their C++ runtime settings @seanh-oai

> #56263 Reject backslashes in HTTP(S) marketplace URL userinfo @willwang-openai

> #56265 Add a built-in Google Cloud Vertex AI provider @celia-oai

> #56274 Wait for cloud config refresh cancellation in loader lifetime tests @goodman-oai

> #56277 Support bounded request bodies in AWS SigV4 signing @viyatb-oai

> #56280 Group consecutive transcript prompts into one background block @bc-openai

> #56288 Pin Linux artifact signing to Cosign v3.1.4 @anp-oai

> #56290 Lock Python release build tools with uv @anp-oai

> #56293 Use fixed-token auth fixtures in Vertex tests @anp-oai

> #56297 Mark built-in dummy credentials and strengthen collision checks @viyatb-oai

> #56301 Add TLS forwarding tests for MITM SigV4 requests @viyatb-oai

> #56302 Add hook configuration to environment attachments @andrewgu-oai

> #56308 Separate directory and repository scopes in the TUI @bc-openai

> #56312 Track accepted conversation history in rollout traces @cassirer-openai

> #56314 Add managed configuration loaders for custom config servers @smurching-oai

> #56342 Match rollout trace image content across request snapshots @cassirer-openai

> #56351 Add experimental attached thread forks @btraut-openai

> #56364 Allow callers to set the thread source for sampling @keyz

> #56371 Make the Guardian review timeout configurable @vivi

> #56439 Update `ctutils` from 0.4.2 to 0.4.5 @felixxia-oai

> #56459 Add Guardian V3 feature configuration @felixxia-oai

> #56460 Add Guardian v3 local board helpers @felixxia-oai

> #56461 Add silent append support to message boards @felixxia-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.165.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-27-9-model-support-changes-in-rust-v0-165-0|9 Model Support changes in rust-v0.165.0]] · Model Support
- [[Changes/Codex CLI/2026-10-27-added-a-repository-filter-to-the-session-picker-and-directory-grouping-to-the-ag|Added a repository filter to the session picker and directory grouping to the agent…]] · Interface Experience
- [[Changes/Codex CLI/2026-10-27-3-safety-and-privacy-changes-in-rust-v0-165-0|3 Safety and Privacy changes in rust-v0.165.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-27-4-agent-mode-changes-in-rust-v0-165-0|4 Agent Mode changes in rust-v0.165.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-27-2-context-window-changes-in-rust-v0-165-0|2 Context Window changes in rust-v0.165.0]] · Context Window
- [[Changes/Codex CLI/2026-10-27-10-apps-and-integrations-changes-in-rust-v0-165-0|10 Apps and Integrations changes in rust-v0.165.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-27-3-developer-workflow-changes-in-rust-v0-165-0|3 Developer Workflow changes in rust-v0.165.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-27-5-memory-and-personalization-changes-in-rust-v0-165-0|5 Memory and Personalization changes in rust-v0.165.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-27-3-account-and-access-changes-in-rust-v0-165-0|3 Account and Access changes in rust-v0.165.0]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-27-ea39c9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-27-39-other-changes-in-rust-v0-165-0.md%0ACard%20ID%3A%20codex-cli-2026-10-27-ea39c9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.165.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->