---
card_id: codex-cli-2026-04-23-7c7744
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Safety and Privacy: 6 changes in 0.123.0 —
  Added host-specific `remote_sandbox_config` requirements for remote environments
  (#18763).'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a2fee96f66de30c1d685c130eb2e8122896ba04a2dd4c79f9aa87bb99a7b2d02
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-7c7744
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.123.0: 6 Safety and Privacy changes'
  evidence:
  - quote: Added host-specific `remote_sandbox_config` requirements for remote environments
      (#18763).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: Made `codex exec` inherit root-level shared flags such as sandbox and model
      options (#18630).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18713 protocol: preserve glob scan depth in permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18763 Add remote_sandbox_config to our config requirements @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18275 sandboxing: intersect permission profiles semantically @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#15578 Add Windows sandbox unified exec runtime support @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-safety-and-privacy-changes-in-rust-v0-123-0
  source_release: codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in rust-v0.123.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-fixed-mcp-step-up-authorization-silently-refreshing-instead-of-prompting-for-re|Fixed
  MCP step-up authorization silently refreshing instead of prompting…]]'
- '[[Changes/Claude Code/2026-04-23-4-safety-and-privacy-changes-in-v2-1-119|4 Safety
  and Privacy changes in v2.1.119]]'
- '[[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17
  Safety and Privacy changes in rust-v0.124.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in rust-v0.123.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in rust-v0.123.0

**Codex CLI** · 2026-04-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.123.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|0.123.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added host-specific `remote_sandbox_config` requirements for remote environments (#18763).

> Made `codex exec` inherit root-level shared flags such as sandbox and model options (#18630).

> #18713 protocol: preserve glob scan depth in permission profiles @bolinfest

> #18763 Add remote_sandbox_config to our config requirements @abhinav-oai

> #18275 sandboxing: intersect permission profiles semantically @bolinfest

> #15578 Add Windows sandbox unified exec runtime support @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.123.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-18662-feat-add-metric-to-track-the-number-of-turns-with-memory-usage-jif-oai|♯18662 feat: add metric to track the number of turns with memory usage @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-23-2-collaboration-changes-in-rust-v0-123-0|2 Collaboration changes in rust-v0.123.0]] · Collaboration
- [[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode changes in rust-v0.123.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-6-model-support-changes-in-rust-v0-123-0|6 Model Support changes in rust-v0.123.0]] · Model Support
- [[Changes/Codex CLI/2026-04-23-18633-use-app-server-thread-names-in-tui-picker-etraut-openai|♯18633 Use app server thread names in TUI picker @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added /mcp verbose for full MCP server diagnostics, resources, and resource…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-9-apps-and-integrations-changes-in-rust-v0-123-0|9 Apps and Integrations changes in rust-v0.123.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-18858-stabilize-debug-clear-memories-integration-test-jif-oai|♯18858 Stabilize debug clear memories integration test @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-developer-workflow-changes-in-rust-v0-123-0|11 Developer Workflow changes in rust-v0.123.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423 chore: document intentional await-holding cases @bolinfest]] · Files and Data
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-123-0|45 other changes in rust-v0.123.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17 Safety and Privacy changes in rust-v0.124.0]]
- Later: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-6-safety-and-privacy-changes-in-v0-39-0|6 Safety and Privacy changes in v0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-7c7744&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-7c7744%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.123.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->