---
card_id: codex-cli-2026-05-20-cafd0c
date: '2026-05-20'
description: 'Codex CLI · 2026-05-20 · Developer Workflow: 3 changes in 0.132.0 —
  TUI startup is faster because terminal capability probes are now batched instead
  of waiting…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1159
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ce5fead80b39c214978161c28c8d32b56380c5bf6d82af60002f2bc307988f59
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-20-cafd0c
  comparison: ''
  date: '2026-05-20'
  description: 'Codex CLI — 0.132.0: 3 Developer Workflow changes'
  evidence:
  - quote: TUI startup is faster because terminal capability probes are now batched
      instead of waiting on several serial checks before the first interactive frame.
      (#23175)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23175 [1 of 2] Optimize TUI startup terminal probes @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22706 [codex] Remove legacy shell output formatting paths @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-developer-workflow-changes-in-rust-v0-132-0
  source_release: codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in rust-v0.132.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-18-5-developer-workflow-changes-in-v1-15-5|5 Developer
  Workflow changes in v1.15.5]]'
- '[[Changes/Claude Code/2026-05-19-3-developer-workflow-changes-in-v2-1-144|3 Developer
  Workflow changes in v2.1.144]]'
- '[[Changes/GitHub Copilot CLI/2026-05-19-2-developer-workflow-changes-in-v1-0-49|2
  Developer Workflow changes in v1.0.49]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in rust-v0.132.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in rust-v0.132.0

**Codex CLI** · 2026-05-20 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.132.0) · from [[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|0.132.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> TUI startup is faster because terminal capability probes are now batched instead of waiting on several serial checks before the first interactive frame. (#23175)

> #23175 [1 of 2] Optimize TUI startup terminal probes @etraut-openai

> #22706 [codex] Remove legacy shell output formatting paths @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.132.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-20-3-interface-experience-changes-in-rust-v0-132-0|3 Interface Experience changes in rust-v0.132.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0|5 Safety and Privacy changes in rust-v0.132.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-20-codex-exec-resume-now-accepts-output-schema-so-resumed-automations-can-keep-sess|codex exec resume now accepts --output-schema, so resumed automations can keep…]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-05-20-23069-multiagent-trim-model-visible-description-cap-to-5-models-sayan-oai|♯23069 multiagent: trim model-visible description, cap to 5 models @sayan-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-20-windows-installs-are-more-robust-codex-doctor-now-detects-npm-managed-installs-c|Windows installs are more robust]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9 Apps and Integrations changes in rust-v0.132.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-20-2-account-and-access-changes-in-rust-v0-132-0|2 Account and Access changes in rust-v0.132.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-20-2-memory-and-personalization-changes-in-rust-v0-132-0|2 Memory and Personalization changes in rust-v0.132.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-20-23147-make-multi-agent-v2-tool-namespace-configurable-jif-oai|♯23147 Make multi-agent v2 tool namespace configurable @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-20-3-editor-experience-changes-in-rust-v0-132-0|3 Editor Experience changes in rust-v0.132.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-20-31-other-changes-in-rust-v0-132-0|31 other changes in rust-v0.132.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-19-2-developer-workflow-changes-in-v1-0-49|2 Developer Workflow changes in v1.0.49]]
- Later: 2026-05-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-20-4-developer-workflow-changes-in-v1-0-51|4 Developer Workflow changes in v1.0.51]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-20-cafd0c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-20-3-developer-workflow-changes-in-rust-v0-132-0.md%0ACard%20ID%3A%20codex-cli-2026-05-20-cafd0c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.132.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->