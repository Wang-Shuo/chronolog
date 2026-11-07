---
card_id: cline-2026-09-22-0d732d
date: '2026-09-22'
description: 'Cline · 2026-09-22 · Model Support: 3 changes in v4.1.20 — Refreshed
  the model catalog: 203 to 209 providers and 6,079 to 6,237 models. Kimi For Coding
  splits…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1352
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7f0513e1cb345a0126f8b98ec43867f632755919b12643e6147af46c50f7b300
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-22-0d732d
  comparison: ''
  date: '2026-09-22'
  description: 'Cline — v4.1.20: 3 Model Support changes'
  evidence:
  - quote: 'Refreshed the model catalog: 203 to 209 providers and 6,079 to 6,237 models.
      Kimi For Coding splits into separate kimi.com and kimi.ai providers, and AI21
      Labs, ainetcafe, Inco, OCI Generative AI, Tempr, and Vispark are new. The resolved
      default model changes for 36 providers that do not pin one — most landing on
      DeepSeek V4.1 Flash, GLM 5.3 Flash, or MiMo V2.6 Flash. If you use one of those
      providers without pinning a model, expect a different default.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.20
  - quote: Compaction no longer silently falls back to truncation partway through
      a long task. The summarizer kept the credentials captured when the task started,
      so once they refreshed its request failed with an authorization error that was
      swallowed; it now follows the task's current credentials and model.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.20
  - quote: A model turn that hits its output-token limit before making a tool call
      no longer ends the task. It is retried up to three times with a reminder to
      respond concisely and split large work across tool calls.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.20
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 3-model-support-changes-in-v4-1-20
  source_release: cline-2026-09-22-v4-1-20-github-394105689-95df91cb
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v4.1.20
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support
  changes in v0.11.4]]'
- '[[Changes/Claude/2026-09-22-claude-opus-5-5-launch|Claude Opus 5.5 launch]]'
- '[[Changes/Claude Code/2026-09-22-5-model-support-changes-in-v2-1-280|5 Model Support
  changes in v2.1.280]]'
source_release: '[[Releases/Cline/cline-2026-09-22-v4-1-20-github-394105689-95df91cb|cline-2026-09-22-v4-1-20-github-394105689-95df91cb]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v4.1.20
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v4.1.20

**Cline** · 2026-09-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.20) · from [[Releases/Cline/cline-2026-09-22-v4-1-20-github-394105689-95df91cb|v4.1.20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Refreshed the model catalog: 203 to 209 providers and 6,079 to 6,237 models. Kimi For Coding splits into separate kimi.com and kimi.ai providers, and AI21 Labs, ainetcafe, Inco, OCI Generative AI, Tempr, and Vispark are new. The resolved default model changes for 36 providers that do not pin one — most landing on DeepSeek V4.1 Flash, GLM 5.3 Flash, or MiMo V2.6 Flash. If you use one of those providers without pinning a model, expect a different default.

> Compaction no longer silently falls back to truncation partway through a long task. The summarizer kept the credentials captured when the task started, so once they refreshed its request failed with an authorization error that was swallowed; it now follows the task's current credentials and model.

> A model turn that hits its output-token limit before making a tool call no longer ends the task. It is retried up to three times with a reminder to respond concisely and split large work across tool calls.

Source: https://github.com/cline/cline/releases/tag/v4.1.20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-22-models-that-advertise-a-large-output-limit-now-get-a-bigger-default-output-budge|Models that advertise a large output limit now get a bigger default output budget]] · Pricing Model
- [[Changes/Cline/2026-09-22-output-from-background-commands-now-streams-into-the-command-row-while-the-comma|Output from background commands now streams into the command row while the command…]] · Developer Workflow
- [[Changes/Cline/2026-09-22-2-agent-mode-changes-in-v4-1-20|2 Agent Mode changes in v4.1.20]] · Agent Mode
- [[Changes/Cline/2026-09-22-rules-are-found-and-shown-consistently-the-rules-panel-listed-only-clinerules-an|Rules are found and shown consistently]] · Mobile and Desktop
- [[Changes/Cline/2026-09-22-2-context-window-changes-in-v4-1-20|2 Context Window changes in v4.1.20]] · Context Window
- [[Changes/Cline/2026-09-22-2-other-changes-in-v4-1-20|2 other changes in v4.1.20]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-5-model-support-changes-in-v2-1-280|5 Model Support changes in v2.1.280]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-25-model-support-changes-in-rust-v0-156-0|25 Model Support changes in rust-v0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-22-0d732d&body=Card%3A%20Changes%2FCline%2F2026-09-22-3-model-support-changes-in-v4-1-20.md%0ACard%20ID%3A%20cline-2026-09-22-0d732d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->