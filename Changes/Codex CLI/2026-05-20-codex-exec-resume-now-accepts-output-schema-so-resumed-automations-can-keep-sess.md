---
card_id: codex-cli-2026-05-20-69568f
date: '2026-05-20'
description: 'Codex CLI · 2026-05-20 · Automation and Scheduling: `codex exec resume`
  now accepts `--output-schema`, so resumed automations can keep session context while…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 869
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 07bcb934dd33901b6c094e9fef4fbbead9912ee6db6c07d0ef3b067dd4d688cf
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-20-69568f
  comparison: ''
  date: '2026-05-20'
  description: 'Codex CLI — 0.132.0: `codex exec resume` now accepts `--output-schema`,
    so resumed automations can keep session context while still enforcing structured
    JSON output. (#23123)'
  evidence:
  - quote: '`codex exec resume` now accepts `--output-schema`, so resumed automations
      can keep session context while still enforcing structured JSON output. (#23123)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: codex-exec-resume-now-accepts-output-schema-so-resumed-automations-can-keep-sess
  source_release: codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4
  source_type: github_releases
  theme: automation-scheduling
  theme_matches:
  - matched_terms:
    - automations
    score: 50
    theme: automation-scheduling
  - matched_terms:
    - context
    score: 50
    theme: context-window
  theme_resolution: manual-semantic-rule-v1
  title: '`codex exec resume` now accepts `--output-schema`, so resumed automations
    can keep…'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-01-claude-code-skill-activated-opentelemetry-event-now-fires-for-user-typed-slash-c|claude_code.skill_activated
  OpenTelemetry event now fires for user-typed slash…]]'
- '[[Changes/Open WebUI/2026-05-09-2-automation-and-scheduling-changes-in-v0-9-3|2
  Automation and Scheduling changes in v0.9.3]]'
- '[[Changes/Dify/2026-05-12-human-input-exposed-selected-action-values-for-human-in-the-loop-flows-thanks-bl|Human
  input — exposed selected action values for Human-in-the-loop flows]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4]]'
source_type: github_releases
theme: automation-scheduling
title: codex exec resume now accepts --output-schema, so resumed automations can keep…
type: change
---

<!-- chronolog:begin region="header" -->
# `codex exec resume` now accepts `--output-schema`, so resumed automations can keep…

**Codex CLI** · 2026-05-20 · [[Themes/automation-scheduling|Automation and Scheduling]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.132.0) · from [[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|0.132.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `codex exec resume` now accepts `--output-schema`, so resumed automations can keep session context while still enforcing structured JSON output. (#23123)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.132.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-20-3-interface-experience-changes-in-rust-v0-132-0|3 Interface Experience changes in rust-v0.132.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0|5 Safety and Privacy changes in rust-v0.132.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-20-23069-multiagent-trim-model-visible-description-cap-to-5-models-sayan-oai|♯23069 multiagent: trim model-visible description, cap to 5 models @sayan-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-20-windows-installs-are-more-robust-codex-doctor-now-detects-npm-managed-installs-c|Windows installs are more robust]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9 Apps and Integrations changes in rust-v0.132.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-20-2-account-and-access-changes-in-rust-v0-132-0|2 Account and Access changes in rust-v0.132.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-20-3-developer-workflow-changes-in-rust-v0-132-0|3 Developer Workflow changes in rust-v0.132.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-20-2-memory-and-personalization-changes-in-rust-v0-132-0|2 Memory and Personalization changes in rust-v0.132.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-20-23147-make-multi-agent-v2-tool-namespace-configurable-jif-oai|♯23147 Make multi-agent v2 tool namespace configurable @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-20-3-editor-experience-changes-in-rust-v0-132-0|3 Editor Experience changes in rust-v0.132.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-20-31-other-changes-in-rust-v0-132-0|31 other changes in rust-v0.132.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-05-12 · Dify · [[Changes/Dify/2026-05-12-human-input-exposed-selected-action-values-for-human-in-the-loop-flows-thanks-bl|Human input — exposed selected action values for Human-in-the-loop flows]]
- Later: 2026-05-20 · Cursor · [[Changes/Cursor/2026-05-20-no-repo-automations|No-repo automations]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-20-69568f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-20-codex-exec-resume-now-accepts-output-schema-so-resumed-automations-can-keep-sess.md%0ACard%20ID%3A%20codex-cli-2026-05-20-69568f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.132.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->