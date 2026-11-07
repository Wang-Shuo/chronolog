---
card_id: codex-cli-2026-07-09-d0079c
date: '2026-07-09'
description: 'Codex CLI · 2026-07-09 · Developer Workflow: 6 changes in 0.144.0 —
  Pasted terminal control sequences can no longer corrupt TUI rendering or resumed…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1209
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 03eea65c2b1402e0e9230ecdad0e773e6ac1ce890af6f6c53f27ecc99c0c313a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-09-d0079c
  comparison: ''
  date: '2026-07-09'
  description: 'Codex CLI — 0.144.0: 6 Developer Workflow changes'
  evidence:
  - quote: Pasted terminal control sequences can no longer corrupt TUI rendering or
      resumed conversation history. (#31494)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31297 feat(core): emit canonical command execution items @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31501 trace hook command execution @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31494 tui: sanitize terminal controls in user messages @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31496 Fall back to HTTP when Apple Git is unavailable @fc-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  - quote: '#31629 core: stop emitting legacy command events directly @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.144.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-developer-workflow-changes-in-rust-v0-144-0
  source_release: codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in rust-v0.144.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-07-7-developer-workflow-changes-in-v1-0-69|7
  Developer Workflow changes in v1.0.69]]'
- '[[Changes/OpenCode/2026-07-07-desktop-make-terminal-shortcuts-take-priority-when-the-terminal-is-focused|Desktop
  Make terminal shortcuts take priority when the terminal is focused]]'
- '[[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7
  Developer Workflow changes in rust-v0.143.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in rust-v0.144.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in rust-v0.144.0

**Codex CLI** · 2026-07-09 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.144.0) · from [[Releases/Codex CLI/codex-cli-2026-07-09-rust-v0-144-0-github-351657410-407edb96|0.144.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Pasted terminal control sequences can no longer corrupt TUI rendering or resumed conversation history. (#31494)

> #31297 feat(core): emit canonical command execution items @owenlin0

> #31501 trace hook command execution @wiltzius-openai

> #31494 tui: sanitize terminal controls in user messages @etraut-openai

> #31496 Fall back to HTTP when Apple Git is unavailable @fc-oai

> #31629 core: stop emitting legacy command events directly @owenlin0

Source: https://github.com/openai/codex/releases/tag/rust-v0.144.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-09-31191-handle-completion-separators-and-popup-dismissal-charliemarsh-oai|♯31191 Handle completion separators and popup dismissal @charliemarsh-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-07-09-31596-use-the-image-generation-extension-by-default-won-openai|♯31596 Use the image generation extension by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-07-09-responses-websockets-continue-using-the-low-latency-transport-while-respecting-s|Responses WebSockets continue using the low-latency transport while respecting…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-09-31356-ci-run-v8-source-builds-on-windows-2025-anp-oai|♯31356 ci: run V8 source builds on Windows 2025 @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-09-11-apps-and-integrations-changes-in-rust-v0-144-0|11 Apps and Integrations changes in rust-v0.144.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-09-31587-stabilize-shared-rollout-budget-test-jif-oai|♯31587 Stabilize shared rollout budget test @jif-oai]] · Collaboration
- [[Changes/Codex CLI/2026-07-09-31525-core-migrate-standalone-web-search-to-extension-owned-turn-items-owenlin0|♯31525 core: migrate standalone web search to extension-owned turn items @owenlin0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-09-5-account-and-access-changes-in-rust-v0-144-0|5 Account and Access changes in rust-v0.144.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-09-8-model-support-changes-in-rust-v0-144-0|8 Model Support changes in rust-v0.144.0]] · Model Support
- [[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit reset credits now show their type and expiration, and let you choose…]] · Pricing Model
- [[Changes/Codex CLI/2026-07-09-3-context-window-changes-in-rust-v0-144-0|3 Context Window changes in rust-v0.144.0]] · Context Window
- [[Changes/Codex CLI/2026-07-09-3-interface-experience-changes-in-rust-v0-144-0|3 Interface Experience changes in rust-v0.144.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4 Safety and Privacy changes in rust-v0.144.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-07-09-4-agent-mode-changes-in-rust-v0-144-0|4 Agent Mode changes in rust-v0.144.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-09-43-other-changes-in-rust-v0-144-0|43 other changes in rust-v0.144.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-07-08 · Codex CLI · [[Changes/Codex CLI/2026-07-08-7-developer-workflow-changes-in-rust-v0-143-0|7 Developer Workflow changes in rust-v0.143.0]]
- Later: 2026-07-10 · Claude Code · [[Changes/Claude Code/2026-07-10-4-developer-workflow-changes-in-v2-1-206|4 Developer Workflow changes in v2.1.206]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-09-d0079c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-09-6-developer-workflow-changes-in-rust-v0-144-0.md%0ACard%20ID%3A%20codex-cli-2026-07-09-d0079c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.144.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->