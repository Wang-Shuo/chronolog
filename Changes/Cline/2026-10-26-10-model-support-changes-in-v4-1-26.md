---
card_id: cline-2026-10-26-e7e603
date: '2026-10-26'
description: 'Cline · 2026-10-26 · Model Support: 10 changes in v4.1.26 — Cloud tasks:
  Settings > API Configuration has a Local | Cloud toggle when cloud sessions are
  on…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1386
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9a45209f50b67a1f88c94a9c46ed732467ac4eac058bff2ac3985bcc33fd7674
product: cline
product_name: Cline
record:
  card_id: cline-2026-10-26-e7e603
  comparison: ''
  date: '2026-10-26'
  description: 'Cline — v4.1.26: 10 Model Support changes'
  evidence:
  - quote: 'Cloud tasks: Settings > API Configuration has a Local | Cloud toggle when
      cloud sessions are on. Cloud picks the Cline model new cloud tasks run on, saved
      separately from your local models. Clicking the model label in a cloud session''s
      composer opens it there.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: With no model chosen, the Cline provider uses Claude Sonnet 5.5 again,
      which is back at the top of Cline's recommended list.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: Model requests retry at most 3 times instead of 5.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: Kimi K3 now gets `max` reasoning for Extra High and Max, instead of an
      `xhigh` setting it rejects.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: Refreshed the model catalog. Adds the CommandCode, Reflection, Liquid Inference
      and Munito AI providers and drops CrofAI, iFlow and Llama. The Cline free list
      adds Reflection Beam, Nemotron 3.5 Lightning and Laguna S 2.1 and drops Mimo
      V2.6 Flash and Muse Spark 1.3 Contributor. ClinePass now defaults to Kimi K3.1
      Pro and adds MiniMax M3.1 Flash and DeepSeek V4.1 Flash 1017. Default models
      change for most other providers, mostly to Kimi K3.1 Pro, MiniMax M3.1 Flash
      or DeepSeek V4.1 Flash 1017. If you use a provider without pinning a model,
      expect a different default.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: 'GPT-6 models (such as `gpt-6-sol` and `gpt-6.1-sol`) work on OpenAI and
      Azure OpenAI-compatible endpoints, and SAP AI Core no longer rejects requests
      with "Unsupported parameter: ''max_tokens''". Both now get `max_completion_tokens`.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: Gemini API keys (the `gemini` provider) no longer send native Google Search.
      Free-tier keys failed every turn with a 429 quota error on Gemini 3+, and on
      Gemini 2.x every Cline tool was dropped.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: A turn whose connection drops after the model has streamed only reasoning
      is now retried instead of ending the task.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: '`ask_question`: the model keeps going after you pick an option, and empty
      answers are rejected.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  - quote: '`run_commands` with an empty command list now returns an error instead
      of a silent success. On PowerShell, the tool tells the model how quote escaping
      works and to confirm recursive deletes first.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.26
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 10-model-support-changes-in-v4-1-26
  source_release: cline-2026-10-26-v4-1-26-github-424033561-1dc8e551
  source_type: github_releases
  theme: model-support
  title: 10 Model Support changes in v4.1.26
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-25-16-model-support-changes-in-v0-12-4|16 Model Support
  changes in v0.12.4]]'
- '[[Changes/ChatGPT/2026-10-26-gpt-6-1-terra-is-rolling-out-in-chatgpt-work-and-codex-it-supports-a-range-of-ta|GPT-6.1
  Terra]]'
- '[[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support
  changes in v2.1.311]]'
source_release: '[[Releases/Cline/cline-2026-10-26-v4-1-26-github-424033561-1dc8e551|cline-2026-10-26-v4-1-26-github-424033561-1dc8e551]]'
source_type: github_releases
theme: model-support
title: 10 Model Support changes in v4.1.26
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Model Support changes in v4.1.26

**Cline** · 2026-10-26 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.26) · from [[Releases/Cline/cline-2026-10-26-v4-1-26-github-424033561-1dc8e551|v4.1.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Cloud tasks: Settings > API Configuration has a Local | Cloud toggle when cloud sessions are on. Cloud picks the Cline model new cloud tasks run on, saved separately from your local models. Clicking the model label in a cloud session's composer opens it there.

> With no model chosen, the Cline provider uses Claude Sonnet 5.5 again, which is back at the top of Cline's recommended list.

> Model requests retry at most 3 times instead of 5.

> Kimi K3 now gets `max` reasoning for Extra High and Max, instead of an `xhigh` setting it rejects.

> Refreshed the model catalog. Adds the CommandCode, Reflection, Liquid Inference and Munito AI providers and drops CrofAI, iFlow and Llama. The Cline free list adds Reflection Beam, Nemotron 3.5 Lightning and Laguna S 2.1 and drops Mimo V2.6 Flash and Muse Spark 1.3 Contributor. ClinePass now defaults to Kimi K3.1 Pro and adds MiniMax M3.1 Flash and DeepSeek V4.1 Flash 1017. Default models change for most other providers, mostly to Kimi K3.1 Pro, MiniMax M3.1 Flash or DeepSeek V4.1 Flash 1017. If you use a provider without pinning a model, expect a different default.

> GPT-6 models (such as `gpt-6-sol` and `gpt-6.1-sol`) work on OpenAI and Azure OpenAI-compatible endpoints, and SAP AI Core no longer rejects requests with "Unsupported parameter: 'max_tokens'". Both now get `max_completion_tokens`.

> Gemini API keys (the `gemini` provider) no longer send native Google Search. Free-tier keys failed every turn with a 429 quota error on Gemini 3+, and on Gemini 2.x every Cline tool was dropped.

> A turn whose connection drops after the model has streamed only reasoning is now retried instead of ending the task.

> `ask_question`: the model keeps going after you pick an option, and empty answers are rejected.

> `run_commands` with an empty command list now returns an error instead of a silent success. On PowerShell, the tool tells the model how quote escaping works and to confirm recursive deletes first.

Source: https://github.com/cline/cline/releases/tag/v4.1.26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-10-26-starting-or-resuming-a-cloud-sandbox-shows-a-progress-card-with-the-repo-branch|Starting or resuming a cloud sandbox shows a progress card with the repo, branch…]] · Safety and Privacy
- [[Changes/Cline/2026-10-26-starting-a-command-no-longer-moves-keyboard-focus-into-the-terminal-so-text-you|Starting a command no longer moves keyboard focus into the terminal, so text you're…]] · Developer Workflow
- [[Changes/Cline/2026-10-26-auto-compaction-no-longer-runs-for-models-with-an-unknown-context-limit-and-it-n|Auto-compaction no longer runs for models with an unknown context limit, and it no…]] · Context Window
- [[Changes/Cline/2026-10-26-5-other-changes-in-v4-1-26|5 other changes in v4.1.26]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-26 · Claude Code · [[Changes/Claude Code/2026-10-26-5-model-support-changes-in-v2-1-311|5 Model Support changes in v2.1.311]]
- Later: 2026-10-26 · ElevenLabs · [[Changes/ElevenLabs/2026-10-26-fast-llm-service-tier|Fast LLM service tier]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-10-26-e7e603&body=Card%3A%20Changes%2FCline%2F2026-10-26-10-model-support-changes-in-v4-1-26.md%0ACard%20ID%3A%20cline-2026-10-26-e7e603%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->