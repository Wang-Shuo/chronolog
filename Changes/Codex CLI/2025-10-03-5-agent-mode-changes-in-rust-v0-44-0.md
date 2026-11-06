---
card_id: codex-cli-2025-10-03-135865
date: '2025-10-03'
description: 'Codex CLI · 2025-10-03 · Agent Mode: 5 changes in 0.44.0 — #4627 fix
  false "task complete" state during agent message'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 820
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d900ca48b9e9a759abe48244b35bd9fe03d3fe9a58faa64328bf6a2a9c3919ed
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-03-135865
  comparison: ''
  date: '2025-10-03'
  description: 'Codex CLI — 0.44.0: 5 Agent Mode changes'
  evidence:
  - quote: '#4627 fix false "task complete" state during agent message'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4610 Rename assistant message to agent message and fix item type field
      naming'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4577 canonicalize display of Agents.md paths on Windows.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4544 Fall back to configured instruction files if AGENTS.md isn''t available'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4324 tui: separator above final agent message'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-agent-mode-changes-in-rust-v0-44-0
  source_release: codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in rust-v0.44.0
  type: change
related_changes:
- '[[Changes/Cursor/2025-09-29-6-agent-mode-changes-in-1-7|6 Agent Mode changes in
  1.7]]'
- '[[Changes/Cursor/2025-09-29-image-file-support-for-agent|Image file support for
  Agent]]'
- '[[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar|Improved
  the experience of writing prompts while the agent is running -- up/down…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37|codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in rust-v0.44.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in rust-v0.44.0

**Codex CLI** · 2025-10-03 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.44.0) · from [[Releases/Codex CLI/codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37|0.44.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #4627 fix false "task complete" state during agent message

> #4610 Rename assistant message to agent message and fix item type field naming

> #4577 canonicalize display of Agents.md paths on Windows.

> #4544 Fall back to configured instruction files if AGENTS.md isn't available

> #4324 tui: separator above final agent message

Source: https://github.com/openai/codex/releases/tag/rust-v0.44.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-03-3-safety-and-privacy-changes-in-rust-v0-44-0|3 Safety and Privacy changes in rust-v0.44.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-10-03-4568-fix-hang-on-second-oauth-login-attempt|♯4568 Fix hang on second oauth login attempt]] · Account and Access
- [[Changes/Codex CLI/2025-10-03-2-context-window-changes-in-rust-v0-44-0|2 Context Window changes in rust-v0.44.0]] · Context Window
- [[Changes/Codex CLI/2025-10-03-3-interface-experience-changes-in-rust-v0-44-0|3 Interface Experience changes in rust-v0.44.0]] · Interface Experience
- [[Changes/Codex CLI/2025-10-03-17-apps-and-integrations-changes-in-rust-v0-44-0|17 Apps and Integrations changes in rust-v0.44.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-10-03-6-model-support-changes-in-rust-v0-44-0|6 Model Support changes in rust-v0.44.0]] · Model Support
- [[Changes/Codex CLI/2025-10-03-experimental-reduce-repetitive-approval-for-read-only-commands-on-windows-4269|(experimental) Reduce repetitive approval for read-only commands on Windows (♯4269)]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-10-03-2-editor-experience-changes-in-rust-v0-44-0|2 Editor Experience changes in rust-v0.44.0]] · Editor Experience
- [[Changes/Codex CLI/2025-10-03-4469-no-background-for-command-or-file-popup|♯4469 no background for /command or @file popup]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-03-4511-wire-up-web-search-item|♯4511 Wire up web search item]] · Search and Browsing
- [[Changes/Codex CLI/2025-10-03-70-other-changes-in-rust-v0-44-0|70 other changes in rust-v0.44.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-10-01 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-01-improved-the-experience-of-writing-prompts-while-the-agent-is-running-up-down-ar|Improved the experience of writing prompts while the agent is running -- up/down…]]
- Later: 2025-10-07 · Gemini CLI · [[Changes/Gemini CLI/2025-10-07-2-agent-mode-changes-in-v0-8-0|2 Agent Mode changes in v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-03-135865&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-03-5-agent-mode-changes-in-rust-v0-44-0.md%0ACard%20ID%3A%20codex-cli-2025-10-03-135865%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.44.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->