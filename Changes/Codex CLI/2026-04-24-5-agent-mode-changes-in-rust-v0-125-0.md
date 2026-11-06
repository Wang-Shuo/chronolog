---
card_id: codex-cli-2026-04-24-20cad0
date: '2026-04-24'
description: 'Codex CLI · 2026-04-24 · Agent Mode: 5 changes in 0.125.0 — Rollout
  tracing now records tool, code-mode, session, and multi-agent relationships, with
  a debug…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1023
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7c26cc843c66b6e9ec6dbf415b80c724face3508dfbd8c1b45a1196b845a0755
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-24-20cad0
  comparison: ''
  date: '2026-04-24'
  description: 'Codex CLI — 0.125.0: 5 Agent Mode changes'
  evidence:
  - quote: 'Rollout tracing now records tool, code-mode, session, and multi-agent
      relationships, with a debug reducer command for inspection. (#18878, #18879,
      #18880)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19129 Reject agents.max_threads with multi_agent_v2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19168 Use Auto-review wording for fallback rationale @maja-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#18879 [rollout_trace] Trace sessions and multi-agent edges @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  - quote: '#19261 Resolve relative agent role config paths from layers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.125.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-agent-mode-changes-in-rust-v0-125-0
  source_release: codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in rust-v0.125.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-04-23-11-agent-mode-changes-in-rust-v0-124-0|11 Agent
  Mode changes in rust-v0.124.0]]'
- '[[Changes/Gemini CLI/2026-04-23-6-agent-mode-changes-in-v0-39-0|6 Agent Mode changes
  in v0.39.0]]'
- '[[Changes/GitHub Copilot CLI/2026-04-23-7-agent-mode-changes-in-v1-0-35|7 Agent
  Mode changes in v1.0.35]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in rust-v0.125.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in rust-v0.125.0

**Codex CLI** · 2026-04-24 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.125.0) · from [[Releases/Codex CLI/codex-cli-2026-04-24-rust-v0-125-0-github-313349252-d42d093c|0.125.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Rollout tracing now records tool, code-mode, session, and multi-agent relationships, with a debug reducer command for inspection. (#18878, #18879, #18880)

> #19129 Reject agents.max_threads with multi_agent_v2 @jif-oai

> #19168 Use Auto-review wording for fallback rationale @maja-openai

> #18879 [rollout_trace] Trace sessions and multi-agent edges @cassirer-openai

> #19261 Resolve relative agent role config paths from layers @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.125.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-24-9-safety-and-privacy-changes-in-rust-v0-125-0|9 Safety and Privacy changes in rust-v0.125.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-24-2-context-window-changes-in-rust-v0-125-0|2 Context Window changes in rust-v0.125.0]] · Context Window
- [[Changes/Codex CLI/2026-04-24-19167-ci-add-macos-keychain-entitlements-euroelessar|♯19167 ci: add macOS keychain entitlements @euroelessar]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-24-windows-bazel-ci-now-uses-a-stable-path-and-shared-query-startup-path-for-better|Windows Bazel CI now uses a stable PATH and shared query startup path for better…]] · Collaboration
- [[Changes/Codex CLI/2026-04-24-2-developer-workflow-changes-in-rust-v0-125-0|2 Developer Workflow changes in rust-v0.125.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-24-5-model-support-changes-in-rust-v0-125-0|5 Model Support changes in rust-v0.125.0]] · Model Support
- [[Changes/Codex CLI/2026-04-24-11-apps-and-integrations-changes-in-rust-v0-125-0|11 Apps and Integrations changes in rust-v0.125.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-24-32-other-changes-in-rust-v0-125-0|32 other changes in rust-v0.125.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-23-7-agent-mode-changes-in-v1-0-35|7 Agent Mode changes in v1.0.35]]
- Later: 2026-04-24 · Cursor · [[Changes/Cursor/2026-04-24-multi-root-workspaces-in-agents-window|Multi-root workspaces in Agents Window]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-24-20cad0&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-24-5-agent-mode-changes-in-rust-v0-125-0.md%0ACard%20ID%3A%20codex-cli-2026-04-24-20cad0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.125.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->