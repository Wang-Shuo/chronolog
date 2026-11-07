---
card_id: kimi-code-2026-07-15-9f7841
date: '2026-07-15'
description: 'Kimi Code · 2026-07-15 · Model Support: The per-step LLM retry limit
  is raised from 3 to 10 attempts, so transient provider failures (429 / overload)
  are…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1283
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 927bf64cda5fb76b59d0a99b8ad47287b37cdfe419e1b8a6080959260f492b30
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-07-15-9f7841
  comparison: ''
  date: '2026-07-15'
  description: 'Kimi Code — Kimi Code 0.24.2 (2026-07-15): The per-step LLM retry
    limit is raised from 3 to 10 attempts, so transient provider failures (429 / overload)
    are retried before a turn fails; tune with `loop_control.max_retries_per_step`.'
  evidence:
  - quote: The per-step LLM retry limit is raised from 3 to 10 attempts, so transient
      provider failures (429 / overload) are retried before a turn fails; tune with
      `loop_control.max_retries_per_step`.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: kimi-code
  product_name: Kimi Code
  slug: the-per-step-llm-retry-limit-is-raised-from-3-to-10-attempts-so-transient-provid
  source_release: kimi-code-2026-07-15-0-24-2-2faa0103
  source_type: kimi_code_changelog
  theme: model-support
  title: The per-step LLM retry limit is raised from 3 to 10 attempts, so transient
    provider…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-improved-the-bash-powershell-tool-message-when-a-command-hits-its-timeout-and-is|Improved
  the Bash/PowerShell tool message when a command hits its timeout…]]'
- '[[Changes/Kimi Code/2026-07-14-2-model-support-changes-in-kimi-code-0-24-1|2 Model
  Support changes in Kimi Code 0.24.1]]'
- '[[Changes/OpenCode/2026-07-14-desktop-fixed-spacing-between-model-provider-sections-in-settings|Desktop
  Fixed spacing between model provider sections in Settings]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-15-0-24-2-2faa0103|kimi-code-2026-07-15-0-24-2-2faa0103]]'
source_type: kimi_code_changelog
theme: model-support
title: The per-step LLM retry limit is raised from 3 to 10 attempts, so transient
  provider…
type: change
---

<!-- chronolog:begin region="header" -->
# The per-step LLM retry limit is raised from 3 to 10 attempts, so transient provider…

**Kimi Code** · 2026-07-15 · [[Themes/model-support|Model Support]] · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-15-0-24-2-2faa0103|Kimi Code 0.24.2 (2026-07-15)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The per-step LLM retry limit is raised from 3 to 10 attempts, so transient provider failures (429 / overload) are retried before a turn fails; tune with `loop_control.max_retries_per_step`.
>
> Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-07-15-kimi-p-now-stays-alive-by-default-while-background-tasks-are-pending-with-no-eff|kimi -p now stays alive by default while background tasks are pending, with no…]] · Interface Experience
- [[Changes/Kimi Code/2026-07-15-3-agent-mode-changes-in-kimi-code-0-24-2|3 Agent Mode changes in Kimi Code 0.24.2]] · Agent Mode
- [[Changes/Kimi Code/2026-07-15-11-other-changes-in-kimi-code-0-24-2|11 other changes in Kimi Code 0.24.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-14 · OpenCode · [[Changes/OpenCode/2026-07-14-desktop-fixed-spacing-between-model-provider-sections-in-settings|Desktop Fixed spacing between model provider sections in Settings]]
- Later: 2026-07-15 · Lovable · [[Changes/Lovable/2026-07-15-gpt-5-6-and-gemini-text-to-speech-models-for-your-app-s-ai-features|GPT-5.6 and Gemini text-to-speech models for your app's AI features]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-15-9f7841&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-15-the-per-step-llm-retry-limit-is-raised-from-3-to-10-attempts-so-transient-provid.md%0ACard%20ID%3A%20kimi-code-2026-07-15-9f7841%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->