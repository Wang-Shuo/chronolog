---
card_id: codex-cli-2026-04-23-c67a3c
date: '2026-04-23'
description: 'Codex CLI · 2026-04-23 · Developer Workflow: 11 changes in 0.123.0 —
  Prevented stale proxy environment variables from being restored from shell snapshots…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1132
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8b1ece19006e68f7b2d2af6d36f5019412fe2346880e92d18e56288c10494163
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-23-c67a3c
  comparison: ''
  date: '2026-04-23'
  description: 'Codex CLI — 0.123.0: 11 Developer Workflow changes'
  evidence:
  - quote: Prevented stale proxy environment variables from being restored from shell
      snapshots (#17271).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: 'Added and tightened the Code Review skill instructions used by Codex-driven
      reviews (#18746, #18818).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: Reduced Rust dev build debug-info overhead while preserving useful backtraces
      (#18844).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18441 Avoid false shell snapshot cleanup warnings @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18746 Add Code Review skill @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#17271 fix: fix stale proxy env restoration after shell snapshots @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18602 Warn when trusting Git subdirectories @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18818 [codex] Tighten code review skill wording @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18271 show bash mode in the TUI @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18741 fix(tui): disable enhanced keys for VS Code WSL @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  - quote: '#18820 Queue follow-up input during user shell commands @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.123.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-developer-workflow-changes-in-rust-v0-123-0
  source_release: codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18
  source_type: github_releases
  theme: developer-workflow
  title: 11 Developer Workflow changes in rust-v0.123.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-4-developer-workflow-changes-in-v2-1-119|4 Developer
  Workflow changes in v2.1.119]]'
- '[[Changes/Claude Code/2026-04-23-wsl-on-windows-can-now-inherit-windows-side-managed-settings-via-the-wslinherits|WSL
  on Windows can now inherit Windows-side managed settings…]]'
- '[[Changes/Codex CLI/2026-04-23-2-developer-workflow-changes-in-rust-v0-124-0|2
  Developer Workflow changes in rust-v0.124.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18]]'
source_type: github_releases
theme: developer-workflow
title: 11 Developer Workflow changes in rust-v0.123.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Developer Workflow changes in rust-v0.123.0

**Codex CLI** · 2026-04-23 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.123.0) · from [[Releases/Codex CLI/codex-cli-2026-04-23-rust-v0-123-0-github-312509536-cebe4f18|0.123.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Prevented stale proxy environment variables from being restored from shell snapshots (#17271).

> Added and tightened the Code Review skill instructions used by Codex-driven reviews (#18746, #18818).

> Reduced Rust dev build debug-info overhead while preserving useful backtraces (#18844).

> #18441 Avoid false shell snapshot cleanup warnings @etraut-openai

> #18746 Add Code Review skill @pakrym-oai

> #17271 fix: fix stale proxy env restoration after shell snapshots @viyatb-oai

> #18602 Warn when trusting Git subdirectories @etraut-openai

> #18818 [codex] Tighten code review skill wording @pakrym-oai

> #18271 show bash mode in the TUI @abhinav-oai

> #18741 fix(tui): disable enhanced keys for VS Code WSL @fcoury-oai

> #18820 Queue follow-up input during user shell commands @etraut-openai

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
- [[Changes/Codex CLI/2026-04-23-9-apps-and-integrations-changes-in-rust-v0-123-0|9 Apps and Integrations changes in rust-v0.123.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-23-18858-stabilize-debug-clear-memories-integration-test-jif-oai|♯18858 Stabilize debug clear memories integration test @jif-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-23-18423-chore-document-intentional-await-holding-cases-bolinfest|♯18423 chore: document intentional await-holding cases @bolinfest]] · Files and Data
- [[Changes/Codex CLI/2026-04-23-45-other-changes-in-rust-v0-123-0|45 other changes in rust-v0.123.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-2-developer-workflow-changes-in-rust-v0-124-0|2 Developer Workflow changes in rust-v0.124.0]]
- Later: 2026-04-23 · Gemini CLI · [[Changes/Gemini CLI/2026-04-23-3-developer-workflow-changes-in-v0-39-0|3 Developer Workflow changes in v0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-23-c67a3c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-23-11-developer-workflow-changes-in-rust-v0-123-0.md%0ACard%20ID%3A%20codex-cli-2026-04-23-c67a3c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.123.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->