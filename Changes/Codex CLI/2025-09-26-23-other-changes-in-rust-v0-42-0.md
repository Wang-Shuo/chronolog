---
card_id: codex-cli-2025-09-26-020fda
date: '2025-09-26'
description: 'Codex CLI · 2025-09-26 · Other changes: 23 changes in 0.42.0 — New `responses-api-proxy`
  component to simplify and secure response handling/proxying (#4246)'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 814b106dea9b8df0cb1cadc1cfa0ed1b9ed9d8d4e1ee47d67a77738c398ef49f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-26-020fda
  comparison: ''
  date: '2025-09-26'
  description: 'Codex CLI — 0.42.0: 23 other changes'
  evidence:
  - quote: New `responses-api-proxy` component to simplify and secure response handling/proxying
      (#4246)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: 'Added secure mode: `CODEX_SECURE_MODE=1` to restrict process observability
      (#4220)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: 'More explicit `codex exec` events, including `item.started` and improved
      output display (#4177, #4250, #4113)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: 'Internal cleanup and refactors for state, footer logic, and unused code
      (#4174, #4259, #4310)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4304] /status followup (#4304)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4310] chore: dead code removal; remove frame count and stateful render
      helpers (#4310)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4255] Add todo-list tool support (#4255)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4246] feat: introduce responses-api-proxy (#4246)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4113] Show exec output on success with trimmed display (#4113)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4275] Move approvals to use ListSelectionView (#4275)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4259] Refactor the footer logic to a new file (#4259)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4229] ref: state - 2 (#4229)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4264] Actually mount sse once (#4264)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4254] Add codex exec testing helpers (#4254)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4177] Add explicit codex exec events (#4177)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4194] chore: refactor attempt_stream_responses() out of stream_responses()
      (#4194)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4220] feat: add support for CODEX_SECURE_MODE=1 to restrict process
      observability (#4220)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4196] revamp /status (#4196)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4174] ref: full state refactor (#4174)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4205] github: update codespell action to v2.1 in workflow (#4205)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4188] chore: drop unused values from env_flags (#4188)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#3194] pageless session list (#3194)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  - quote: '[#4160] Simplify tool implemetations (#4160)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.42.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 23-other-changes-in-rust-v0-42-0
  source_release: codex-cli-2025-09-26-rust-v0-42-0-github-250387883-27046aff
  source_type: github_releases
  theme: uncategorized
  title: 23 other changes in rust-v0.42.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-26-rust-v0-42-0-github-250387883-27046aff|codex-cli-2025-09-26-rust-v0-42-0-github-250387883-27046aff]]'
source_type: github_releases
theme: uncategorized
title: 23 other changes in rust-v0.42.0
type: change
---

<!-- chronolog:begin region="header" -->
# 23 other changes in rust-v0.42.0

**Codex CLI** · 2025-09-26 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.42.0) · from [[Releases/Codex CLI/codex-cli-2025-09-26-rust-v0-42-0-github-250387883-27046aff|0.42.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New `responses-api-proxy` component to simplify and secure response handling/proxying (#4246)

> Added secure mode: `CODEX_SECURE_MODE=1` to restrict process observability (#4220)

> More explicit `codex exec` events, including `item.started` and improved output display (#4177, #4250, #4113)

> Internal cleanup and refactors for state, footer logic, and unused code (#4174, #4259, #4310)

> [#4304] /status followup (#4304)

> [#4310] chore: dead code removal; remove frame count and stateful render helpers (#4310)

> [#4255] Add todo-list tool support (#4255)

> [#4246] feat: introduce responses-api-proxy (#4246)

> [#4113] Show exec output on success with trimmed display (#4113)

> [#4275] Move approvals to use ListSelectionView (#4275)

> [#4259] Refactor the footer logic to a new file (#4259)

> [#4229] ref: state - 2 (#4229)

> [#4264] Actually mount sse once (#4264)

> [#4254] Add codex exec testing helpers (#4254)

> [#4177] Add explicit codex exec events (#4177)

> [#4194] chore: refactor attempt_stream_responses() out of stream_responses() (#4194)

> [#4220] feat: add support for CODEX_SECURE_MODE=1 to restrict process observability (#4220)

> [#4196] revamp /status (#4196)

> [#4174] ref: full state refactor (#4174)

> [#4205] github: update codespell action to v2.1 in workflow (#4205)

> [#4188] chore: drop unused values from env_flags (#4188)

> [#3194] pageless session list (#3194)

> [#4160] Simplify tool implemetations (#4160)

Source: https://github.com/openai/codex/releases/tag/rust-v0.42.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-26-3-developer-workflow-changes-in-rust-v0-42-0|3 Developer Workflow changes in rust-v0.42.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-09-26-4-apps-and-integrations-changes-in-rust-v0-42-0|4 Apps and Integrations changes in rust-v0.42.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-09-26-4101-hide-the-status-indicator-when-the-answer-stream-starts-4101|♯4101 hide the status indicator when the answer stream starts (♯4101)]] · Interface Experience
- [[Changes/Codex CLI/2025-09-26-2-safety-and-privacy-changes-in-rust-v0-42-0|2 Safety and Privacy changes in rust-v0.42.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-09-26-stability-and-correctness-token-usage-fix-for-compaction-sse-mounting-reliabilit|Stability and correctness]] · Reliability and Performance
- [[Changes/Codex CLI/2025-09-26-4195-send-text-parameter-for-non-gpt-5-models-4195|♯4195 Send text parameter for non-gpt-5 models (♯4195)]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-26-020fda&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-26-23-other-changes-in-rust-v0-42-0.md%0ACard%20ID%3A%20codex-cli-2025-09-26-020fda%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.42.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->