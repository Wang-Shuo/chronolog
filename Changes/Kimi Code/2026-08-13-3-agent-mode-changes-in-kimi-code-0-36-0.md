---
card_id: kimi-code-2026-08-13-f6ffc8
date: '2026-08-13'
description: 'Kimi Code · 2026-08-13 · Agent Mode: 3 changes in Kimi Code 0.36.0 (2026-08-13)
  — Upgrade the experimental subagent model setting to a model pool: the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0898320a301a6ae9f51df928a8ce04a3b4dd3d77eb434350b8fa7ada103ce988
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-08-13-f6ffc8
  comparison: ''
  date: '2026-08-13'
  description: 'Kimi Code — Kimi Code 0.36.0 (2026-08-13): 3 Agent Mode changes'
  evidence:
  - quote: 'Upgrade the experimental subagent model setting to a model pool: the `[secondary_model]`
      section can now hold a set of candidate models with descriptions, and the main
      agent picks from them per spawn based on the task.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'Minimal: run `/secondary-model` in the TUI, or write a single `default_model`
      line in `config.toml`, to make every subagent run the same model by default;
      add `force = true` to pin that choice so the main agent cannot override it.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'Declare a named pool with a one-line scenario description for each alias
      — the descriptions are what the main agent sees when choosing:'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 3-agent-mode-changes-in-kimi-code-0-36-0
  source_release: kimi-code-2026-08-13-0-36-0-b841eb68
  source_type: kimi_code_changelog
  theme: agent-mode
  title: 3 Agent Mode changes in Kimi Code 0.36.0
  type: change
related_changes:
- '[[Changes/Cursor/2026-08-13-2-agent-mode-changes-in-08-13-26|2 Agent Mode changes
  in 08.13.26]]'
- '[[Changes/Cursor/2026-08-13-agents-do-their-best-work-when-they-start-in-a-ready-environment-repos-cloned-de-6161c7|Agents
  do their best work when they start in a ready environment]]'
- '[[Changes/Cursor/2026-08-13-when-a-bad-commit-or-dependency-update-breaks-your-environment-agents-keep-using|More
  resilient agent runs]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-08-13-0-36-0-b841eb68|kimi-code-2026-08-13-0-36-0-b841eb68]]'
source_type: kimi_code_changelog
theme: agent-mode
title: 3 Agent Mode changes in Kimi Code 0.36.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Agent Mode changes in Kimi Code 0.36.0

**Kimi Code** · 2026-08-13 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-08-13-0-36-0-b841eb68|Kimi Code 0.36.0 (2026-08-13)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Upgrade the experimental subagent model setting to a model pool: the `[secondary_model]` section can now hold a set of candidate models with descriptions, and the main agent picks from them per spawn based on the task.

> Minimal: run `/secondary-model` in the TUI, or write a single `default_model` line in `config.toml`, to make every subagent run the same model by default; add `force = true` to pin that choice so the main agent cannot override it.

> Declare a named pool with a one-line scenario description for each alias — the descriptions are what the main agent sees when choosing:

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-08-13-2-interface-experience-changes-in-kimi-code-0-36-0|2 Interface Experience changes in Kimi Code 0.36.0]] · Interface Experience
- [[Changes/Kimi Code/2026-08-13-set-kimi-code-experimental-secondary-model-1-or-the-master-flag-kimi-code-experi|Set KIMI_CODE_EXPERIMENTAL_SECONDARY_MODEL=1…]] · Model Support
- [[Changes/Kimi Code/2026-08-13-show-project-mcp-launch-targets-in-the-workspace-trust-prompt-default-to-declini|Show project MCP launch targets in the workspace trust prompt, default to declining…]] · Safety and Privacy
- [[Changes/Kimi Code/2026-08-13-recommended-setups|Recommended setups]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-13 · Cursor · [[Changes/Cursor/2026-08-13-when-a-bad-commit-or-dependency-update-breaks-your-environment-agents-keep-using|More resilient agent runs]]
- Later: 2026-08-13 · OpenHands · [[Changes/OpenHands/2026-08-13-chore-enforce-typed-openhands-typescript-client-for-agent-server-api-calls-no-ad|chore: enforce typed @openhands/typescript-client for agent-server API calls…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-08-13-f6ffc8&body=Card%3A%20Changes%2FKimi%20Code%2F2026-08-13-3-agent-mode-changes-in-kimi-code-0-36-0.md%0ACard%20ID%3A%20kimi-code-2026-08-13-f6ffc8%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->