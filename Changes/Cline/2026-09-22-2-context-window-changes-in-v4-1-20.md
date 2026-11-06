---
card_id: cline-2026-09-22-ca4b92
date: '2026-09-22'
description: 'Cline · 2026-09-22 · Context Window: 2 changes in v4.1.20 — UserPromptSubmit
  and TaskStart hooks can inject context again. What those hooks returned as…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1237
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2de0ea2e4cade273ec1a44703903055be8df7583d99925cc65ea166f7b8dd29b
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-22-ca4b92
  comparison: ''
  date: '2026-09-22'
  description: 'Cline — v4.1.20: 2 Context Window changes'
  evidence:
  - quote: UserPromptSubmit and TaskStart hooks can inject context again. What those
      hooks returned as `contextModification` was being dropped — only `cancel` survived
      — so a hook meant to add repository facts or house rules to a task silently
      did nothing. The context is now delivered as a `<hook_context>` block on the
      run's first request, the same as before the regression, and the raw block never
      renders in the transcript. A hook also no longer receives its own previously
      injected text back as the next turn's prompt.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.20
  - quote: Unsent text in the composer survives Retry. Retry sent no composer content
      but still ran the same cleanup as approval actions, deleting the only copy of
      anything typed while a request was in flight. Text, quote context, images, and
      files are now tracked as one draft that only submitting actions consume.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.20
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 2-context-window-changes-in-v4-1-20
  source_release: cline-2026-09-22-v4-1-20-github-394105689-95df91cb
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v4.1.20
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-16-test-cover-conversation-context-menu-by-aivong-openhands-in-https-github-com-ope|test:
  cover conversation context menu]]'
- '[[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long
  tasks now compact when they actually need to rather than running out of room]]'
- '[[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context
  Window changes in rust-v0.155.0]]'
source_release: '[[Releases/Cline/cline-2026-09-22-v4-1-20-github-394105689-95df91cb|cline-2026-09-22-v4-1-20-github-394105689-95df91cb]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v4.1.20
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v4.1.20

**Cline** · 2026-09-22 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.20) · from [[Releases/Cline/cline-2026-09-22-v4-1-20-github-394105689-95df91cb|v4.1.20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> UserPromptSubmit and TaskStart hooks can inject context again. What those hooks returned as `contextModification` was being dropped — only `cancel` survived — so a hook meant to add repository facts or house rules to a task silently did nothing. The context is now delivered as a `<hook_context>` block on the run's first request, the same as before the regression, and the raw block never renders in the transcript. A hook also no longer receives its own previously injected text back as the next turn's prompt.

> Unsent text in the composer survives Retry. Retry sent no composer content but still ran the same cleanup as approval actions, deleting the only copy of anything typed while a request was in flight. Text, quote context, images, and files are now tracked as one draft that only submitting actions consume.

Source: https://github.com/cline/cline/releases/tag/v4.1.20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-22-3-model-support-changes-in-v4-1-20|3 Model Support changes in v4.1.20]] · Model Support
- [[Changes/Cline/2026-09-22-models-that-advertise-a-large-output-limit-now-get-a-bigger-default-output-budge|Models that advertise a large output limit now get a bigger default output budget]] · Pricing Model
- [[Changes/Cline/2026-09-22-output-from-background-commands-now-streams-into-the-command-row-while-the-comma|Output from background commands now streams into the command row while the command…]] · Developer Workflow
- [[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes in v4.1.20]] · Agent Mode
- [[Changes/Cline/2026-09-22-rules-are-found-and-shown-consistently-the-rules-panel-listed-only-clinerules-an|Rules are found and shown consistently]] · Mobile and Desktop
- [[Changes/Cline/2026-09-22-2-other-changes-in-v4-1-20|2 other changes in v4.1.20]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-22-ca4b92&body=Card%3A%20Changes%2FCline%2F2026-09-22-2-context-window-changes-in-v4-1-20.md%0ACard%20ID%3A%20cline-2026-09-22-ca4b92%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->