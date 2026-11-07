---
card_id: codex-cli-2026-04-23-534b9b
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Agent Mode: 8 changes in 0.123.0 — Improved
  realtime handoffs so background agents receive transcript deltas and can explicitly
  stay…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1022
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 49a914c2b38ad10a52cc8081d149cd2a7252bef860c70c14f2effa72f41a8098
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-534b9b
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.123.0: 8 Agent Mode changes'
  evidence:
  - quote: 'Improved realtime handoffs so background agents receive transcript deltas
      and can explicitly stay silent when appropriate (#18597, #18761, #18635).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: Queued normal follow-up text submitted while a manual shell command is
      running, preventing stuck `Working` states (#18820).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18094 [codex] Use background agent task auth for backend calls @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18697 [codex] Fix agent identity auth test fixture @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18701 [codex] prefer inherited spawn agent model @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18393 feat(auto-review) Handle request_permissions calls @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18850 Move external agent config out of core @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18873 chore: default multi-agent v2 fork to all @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-agent-mode-changes-in-rust-v0-123-0
  source_release: codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18
  source_type: github_releases
  theme: agent-mode
  title: 8 Agent Mode changes in rust-v0.123.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-04-22-kimi-cli-with-kimi-k2-6-excels-at-long-horizon-agentic-execution-tasks-through-a|Kimi
  CLI with Kimi K2.6 excels at long horizon agentic execution tasks through…]]'
- '[[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-118|2 Agent Mode
  changes in v2.1.118]]'
- '[[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119|2 Agent Mode
  changes in v2.1.119]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18]]'
source_type: github_releases
theme: agent-mode
title: 8 Agent Mode changes in rust-v0.123.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Agent Mode changes in rust-v0.123.0

**Codex CLI** · 2026-04-23 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.123.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|0.123.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved realtime handoffs so background agents receive transcript deltas and can explicitly stay silent when appropriate (#18597, #18761, #18635).

> Queued normal follow-up text submitted while a manual shell command is running, preventing stuck `Working` states (#18820).

> #18094 [codex] Use background agent task auth for backend calls @adrian-openai

> #18697 [codex] Fix agent identity auth test fixture @adrian-openai

> #18701 [codex] prefer inherited spawn agent model @tibo-openai

> #18393 feat(auto-review) Handle request_permissions calls @dylan-hurd-oai

> #18850 Move external agent config out of core @pakrym-oai

> #18873 chore: default multi-agent v2 fork to all @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.123.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-18662-feat-add-metric-to-track-the-number-of-turns-with-memory-usage-jif-oai|♯18662 feat: add metric to track the number of turns with memory usage @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-23-2-collaboration-changes-in-rust-v0-123-0|2 Collaboration changes in rust-v0.123.0]] · Collaboration
- [[Changes/Codex CLI/2026-04-23-6-model-support-changes-in-rust-v0-123-0|6 Model Support changes in rust-v0.123.0]] · Model Support
- [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-18633-use-app-server-thread-names-in-tui-picker-etraut-openai|♯18633 Use app server thread names in TUI picker @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added /mcp verbose for full MCP server diagnostics, resources, and resource…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-9-apps-and-integrations-changes-in-rust-v0-123-0|9 Apps and Integrations changes in rust-v0.123.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-18858-stabilize-debug-clear-memories-integration-test-jif-oai|♯18858 Stabilize debug clear memories integration test @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-developer-workflow-changes-in-rust-v0-123-0|11 Developer Workflow changes in rust-v0.123.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423 chore: document intentional await-holding cases @bolinfest]] · Files and Data
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-123-0|45 other changes in rust-v0.123.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-23 · Claude Code · [[Changes/Claude Code/2026-04-23-2-agent-mode-changes-in-v2-1-119|2 Agent Mode changes in v2.1.119]]
- Later: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent Mode changes in rust-v0.124.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-534b9b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-8-agent-mode-changes-in-rust-v0-123-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-534b9b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.123.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->