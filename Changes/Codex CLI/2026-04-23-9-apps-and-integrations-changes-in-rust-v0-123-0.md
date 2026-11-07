---
card_id: codex-cli-2026-04-23-c40ee6
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Apps and Integrations: 9 changes in 0.123.0
  — Made plugin MCP loading accept both `mcpServers` and top-level server maps in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2687
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 25524ccb0bf278418672dcffc37d28baa50c1724c9248e622c6bd246bc609952
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-c40ee6
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.123.0: 9 Apps and Integrations changes'
  evidence:
  - quote: Made plugin MCP loading accept both `mcpServers` and top-level server maps
      in `.mcp.json` (#18780).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: 'Updated app-server protocol docs for threadless MCP resource reads and
      namespaced dynamic tools (#18292, #18413).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: Refreshed generated Python app-server SDK types from the current schema
      (#18862).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18610 Add verbose diagnostics for /mcp @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18722 chore(guardian) disable mcps and plugins @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18780 feat: Support more plugin MCP file shapes. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18292 Make MCP resource read threadless @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18093 Propagate thread id in MCP tool metadata @rennie-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18862 Refresh generated Python app-server SDK types @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-apps-and-integrations-changes-in-rust-v0-123-0
  source_release: codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18
  source_type: github_releases
  theme: apps-integrations
  title: 9 Apps and Integrations changes in rust-v0.123.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-5-apps-and-integrations-changes-in-v2-1-118|5
  Apps and Integrations changes in v2.1.118]]'
- '[[Changes/Codex CLI/2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0|12
  Apps and Integrations changes in rust-v0.124.0]]'
- '[[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added
  /mcp verbose for full MCP server diagnostics, resources, and resource…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18]]'
source_type: github_releases
theme: apps-integrations
title: 9 Apps and Integrations changes in rust-v0.123.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in rust-v0.123.0

**Codex CLI** · 2026-04-23 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.123.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|0.123.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Made plugin MCP loading accept both `mcpServers` and top-level server maps in `.mcp.json` (#18780).

> Updated app-server protocol docs for threadless MCP resource reads and namespaced dynamic tools (#18292, #18413).

> Refreshed generated Python app-server SDK types from the current schema (#18862).

> #18610 Add verbose diagnostics for /mcp @etraut-openai

> #18722 chore(guardian) disable mcps and plugins @dylan-hurd-oai

> #18780 feat: Support more plugin MCP file shapes. @xl-openai

> #18292 Make MCP resource read threadless @mzeng-openai

> #18093 Propagate thread id in MCP tool metadata @rennie-openai

> #18862 Refresh generated Python app-server SDK types @sdcoffey

Source: https://github.com/openai/codex/releases/tag/rust-v0.123.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-23-18662-feat-add-metric-to-track-the-number-of-turns-with-memory-usage-jif-oai|♯18662 feat: add metric to track the number of turns with memory usage @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-23-18794-organize-context-fragments-pakrym-oai|♯18794 Organize context fragments @pakrym-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-23-2-collaboration-changes-in-rust-v0-123-0|2 Collaboration changes in rust-v0.123.0]] · Collaboration
- [[Changes/Codex CLI/2026-04-23-8-agent-mode-changes-in-rust-v0-123-0|8 Agent Mode changes in rust-v0.123.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-23-6-model-support-changes-in-rust-v0-123-0|6 Model Support changes in rust-v0.123.0]] · Model Support
- [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-23-18633-use-app-server-thread-names-in-tui-picker-etraut-openai|♯18633 Use app server thread names in TUI picker @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-04-23-added-mcp-verbose-for-full-mcp-server-diagnostics-resources-and-resource-templat|Added /mcp verbose for full MCP server diagnostics, resources, and resource…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-18858-stabilize-debug-clear-memories-integration-test-jif-oai|♯18858 Stabilize debug clear memories integration test @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-11-developer-workflow-changes-in-rust-v0-123-0|11 Developer Workflow changes in rust-v0.123.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423 chore: document intentional await-holding cases @bolinfest]] · Files and Data
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-123-0|45 other changes in rust-v0.123.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-12-apps-and-integrations-changes-in-rust-v0-124-0|12 Apps and Integrations changes in rust-v0.124.0]]
- Later: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-4-apps-and-integrations-changes-in-v0-39-0|4 Apps and Integrations changes in v0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-c40ee6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-9-apps-and-integrations-changes-in-rust-v0-123-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-c40ee6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.123.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->