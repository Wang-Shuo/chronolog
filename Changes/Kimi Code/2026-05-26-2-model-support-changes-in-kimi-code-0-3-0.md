---
card_id: kimi-code-2026-05-26-c2b3e0
date: '2026-05-26'
description: 'Kimi Code · 2026-05-26 · Model Support: 2 changes in Kimi Code 0.3.0
  (2026-05-26) — The `openai` provider now works out of the box for OpenAI-compatible…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1233
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8e353e3e63e3b6a77f46a32f930396b82abded436fb2da6927b94e026c2b0af
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-05-26-c2b3e0
  comparison: ''
  date: '2026-05-26'
  description: 'Kimi Code — Kimi Code 0.3.0 (2026-05-26): 2 Model Support changes'
  evidence:
  - quote: 'The `openai` provider now works out of the box for OpenAI-compatible reasoner
      models: it auto-detects thinking fields in responses (`reasoning_content` /
      `reasoning_details` / `reasoning`) and auto-injects `reasoning_effort` when
      history contains prior thinking. DeepSeek, Qwen, One API and other gateway-fronted
      services no longer need a hand-set `reasoning_key`, which remains available
      as an explicit override for non-standard gateways.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Preserve catalog-declared interleaved reasoning fields for OpenAI-compatible
      models configured through `/connect`.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 2-model-support-changes-in-kimi-code-0-3-0
  source_release: kimi-code-2026-05-26-0-3-0-92e16055
  source_type: kimi_code_changelog
  theme: model-support
  title: 2 Model Support changes in Kimi Code 0.3.0
  type: change
related_changes:
- '[[Changes/Superwhisper/2026-05-25-support-for-parakeet-local-models-on-arm-based-processors|Support
  for Parakeet local models on ARM based processors]]'
- '[[Changes/AnythingLLM/2026-05-26-11-model-support-changes-in-v1-13-0|11 Model Support
  changes in v1.13.0]]'
- '[[Changes/Kimi Code/2026-05-26-3-model-support-changes-in-kimi-code-0-2-0|3 Model
  Support changes in Kimi Code 0.2.0]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-05-26-0-3-0-92e16055|kimi-code-2026-05-26-0-3-0-92e16055]]'
source_type: kimi_code_changelog
theme: model-support
title: 2 Model Support changes in Kimi Code 0.3.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in Kimi Code 0.3.0

**Kimi Code** · 2026-05-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-05-26-0-3-0-92e16055|Kimi Code 0.3.0 (2026-05-26)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The `openai` provider now works out of the box for OpenAI-compatible reasoner models: it auto-detects thinking fields in responses (`reasoning_content` / `reasoning_details` / `reasoning`) and auto-injects `reasoning_effort` when history contains prior thinking. DeepSeek, Qwen, One API and other gateway-fronted services no longer need a hand-set `reasoning_key`, which remains available as an explicit override for non-standard gateways.

> Preserve catalog-declared interleaved reasoning fields for OpenAI-compatible models configured through `/connect`.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-05-26-2-agent-mode-changes-in-kimi-code-0-3-0|2 Agent Mode changes in Kimi Code 0.3.0]] · Agent Mode
- [[Changes/Kimi Code/2026-05-26-prevent-running-the-model-and-sessions-slash-commands-while-streaming-or-compact|Prevent running the /model and /sessions slash commands while streaming…]] · Context Window
- [[Changes/Kimi Code/2026-05-26-exit-promptly-when-the-controlling-terminal-goes-away-the-tui-now-handles-sighup|Exit promptly when the controlling terminal goes away]] · Developer Workflow
- [[Changes/Kimi Code/2026-05-26-avoid-overly-small-local-completion-caps-that-can-truncate-reasoning-before-summ|Avoid overly small local completion caps that can truncate reasoning before…]] · Editor Experience
- [[Changes/Kimi Code/2026-05-26-logout-now-opens-a-picker-so-you-can-choose-which-provider-to-log-out-of-instead|/logout now opens a picker so you can choose which provider to log out of, instead…]] · Interface Experience
- [[Changes/Kimi Code/2026-05-26-3-other-changes-in-kimi-code-0-3-0|3 other changes in Kimi Code 0.3.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-26 · Kimi Code · [[Changes/Kimi Code/2026-05-26-3-model-support-changes-in-kimi-code-0-2-0|3 Model Support changes in Kimi Code 0.2.0]]
- Later: 2026-05-27 · Claude Code · [[Changes/Claude Code/2026-05-27-2-model-support-changes-in-v2-1-152|2 Model Support changes in v2.1.152]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-05-26-c2b3e0&body=Card%3A%20Changes%2FKimi%20Code%2F2026-05-26-2-model-support-changes-in-kimi-code-0-3-0.md%0ACard%20ID%3A%20kimi-code-2026-05-26-c2b3e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->