---
card_id: gemini-cli-2026-01-28-63a6bb
date: '2026-01-28'
description: 'Gemini CLI · 2026-01-28 · Automation and Scheduling: 12 changes in Release
  v0.26.0 — chore(automation): recursive labeling for workstream descendants by…'
diffusion:
  first_in_tracked: '[[Changes/OpenHands/2024-09-04-better-syntax-error-loop-detection-by-tobitege-in-https-github-com-all-hands-ai|Better
    syntax error loop detection]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 511
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c336bb04117cb5640efae31ab6527c63866489703b49b816bc7da309f00c7332
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-01-28-63a6bb
  comparison: ''
  date: '2026-01-28'
  description: 'Gemini CLI — Release v0.26.0: 12 Automation and Scheduling changes'
  evidence:
  - quote: 'chore(automation): recursive labeling for workstream descendants by @bdmorgan
      in https://github.com/google-gemini/gemini-cli/pull/16609'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'chore(automation): remove automated PR size and complexity labeler by
      @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16648'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'chore(automation): improve scheduled issue triage discovery and throughput
      by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16652'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'feat(scheduler): add types needed for event driven scheduler by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/16641'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'chore(automation): ensure status/need-triage is applied and never cleared
      automatically by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16657'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'feat(scheduler): add SchedulerStateManager for reactive tool state by
      @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/16651'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'chore(automation): enforce ''help wanted'' label permissions and update
      guidelines by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16707'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: "feat(automation): enforce '\U0001F512 maintainer only' and fix bot loop
      by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16751"
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'feat(scheduler): add functional awaitConfirmation utility by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/16721'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'refactor(core): decouple scheduler into orchestration, policy, and confirmation
      by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/16895'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'refactor(cli): centralize tool mapping and decouple legacy scheduler by
      @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17044'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  - quote: 'feat(cli): add experiment gate for event-driven scheduler by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/17055'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 12-automation-and-scheduling-changes-in-v0-26-0
  source_release: gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9
  source_type: github_releases
  theme: automation-scheduling
  title: 12 Automation and Scheduling changes in v0.26.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-12-18-7961-refactor-tui-event-loop-to-enable-dropping-recreating-crossterm-event-strea|♯7961
  refactor TUI event loop to enable dropping + recreating crossterm event stream]]'
- '[[Changes/Gemini CLI/2026-01-07-chore-core-remove-legacy-fallback-flags-and-migrate-loop-detection-by-adamfweidm|chore(core):
  remove legacy fallback flags and migrate loop detection]]'
- '[[Changes/Gemini CLI/2026-01-21-2-automation-and-scheduling-changes-in-v0-25-0|2
  Automation and Scheduling changes in v0.25.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9|gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9]]'
source_type: github_releases
theme: automation-scheduling
title: 12 Automation and Scheduling changes in v0.26.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Automation and Scheduling changes in v0.26.0

**Gemini CLI** · 2026-01-28 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0) · from [[Releases/Gemini CLI/gemini-cli-2026-01-28-v0-26-0-github-280517876-a39d31c9|Release v0.26.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> chore(automation): recursive labeling for workstream descendants by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16609

> chore(automation): remove automated PR size and complexity labeler by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16648

> chore(automation): improve scheduled issue triage discovery and throughput by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16652

> feat(scheduler): add types needed for event driven scheduler by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/16641

> chore(automation): ensure status/need-triage is applied and never cleared automatically by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16657

> feat(scheduler): add SchedulerStateManager for reactive tool state by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/16651

> chore(automation): enforce 'help wanted' label permissions and update guidelines by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16707

> feat(automation): enforce '🔒 maintainer only' and fix bot loop by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/16751

> feat(scheduler): add functional awaitConfirmation utility by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/16721

> refactor(core): decouple scheduler into orchestration, policy, and confirmation by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/16895

> refactor(cli): centralize tool mapping and decouple legacy scheduler by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17044

> feat(cli): add experiment gate for event-driven scheduler by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17055

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.26.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-01-28-8-developer-workflow-changes-in-v0-26-0|8 Developer Workflow changes in v0.26.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-01-28-docs-update-project-context-and-pr-creator-workflow-by-ntaylormullen-in-https-gi|docs: update project context and pr-creator workflow]] · Projects and Workspaces
- [[Changes/Gemini CLI/2026-01-28-8-agent-mode-changes-in-v0-26-0|8 Agent Mode changes in v0.26.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-01-28-4-model-support-changes-in-v0-26-0|4 Model Support changes in v0.26.0]] · Model Support
- [[Changes/Gemini CLI/2026-01-28-remove-missing-sidebar-item-by-chrstnb-in-https-github-com-google-gemini-gemini|Remove missing sidebar item]] · Interface Experience
- [[Changes/Gemini CLI/2026-01-28-4-apps-and-integrations-changes-in-v0-26-0|4 Apps and Integrations changes in v0.26.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-01-28-feat-core-enhanced-anchored-iterative-context-compression-with-self-verification|feat(core): enhanced anchored iterative context compression with self-verification]] · Context Window
- [[Changes/Gemini CLI/2026-01-28-feat-admin-implement-admin-controls-polling-and-restart-prompt-by-skeshive-in-ht|feat(admin): implement admin controls polling and restart prompt]] · Enterprise and Administration
- [[Changes/Gemini CLI/2026-01-28-3-safety-and-privacy-changes-in-v0-26-0|3 Safety and Privacy changes in v0.26.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-01-28-48-other-changes-in-v0-26-0|48 other changes in v0.26.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-01-21 · Gemini CLI · [[Changes/Gemini CLI/2026-01-21-2-automation-and-scheduling-changes-in-v0-25-0|2 Automation and Scheduling changes in v0.25.0]]
- Later: 2026-02-04 · Gemini CLI · [[Changes/Gemini CLI/2026-02-04-3-automation-and-scheduling-changes-in-v0-27-0|3 Automation and Scheduling changes in v0.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-09-04 · OpenHands · [[Changes/OpenHands/2024-09-04-better-syntax-error-loop-detection-by-tobitege-in-https-github-com-all-hands-ai|Better syntax error loop detection]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-01-28-63a6bb&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-01-28-12-automation-and-scheduling-changes-in-v0-26-0.md%0ACard%20ID%3A%20gemini-cli-2026-01-28-63a6bb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.26.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->