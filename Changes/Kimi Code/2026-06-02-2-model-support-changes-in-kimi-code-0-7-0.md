---
card_id: kimi-code-2026-06-02-b2844e
date: '2026-06-02'
description: 'Kimi Code · 2026-06-02 · Model Support: 2 changes in Kimi Code 0.7.0
  (2026-06-02) — Add `/provider` command for managing AI providers, support custom
  registry…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1240
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 99ea5705bd51893a5af447eeebfb94eab5af3243a93eb6b299bfe4e8e4594821
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-06-02-b2844e
  comparison: ''
  date: '2026-06-02'
  description: 'Kimi Code — Kimi Code 0.7.0 (2026-06-02): 2 Model Support changes'
  evidence:
  - quote: Add `/provider` command for managing AI providers, support custom registry
      imports, and introduce a tabbed model selector. It replaces the deprecated `/connect`
      command — use `/provider` instead.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: 'Add `KIMI_MODEL_ADAPTIVE_THINKING` (and a matching `adaptive_thinking`
      model-alias field) to force adaptive thinking (`thinking: { type: ''adaptive''
      }`) on or off, overriding the Anthropic model-name version inference. This lets
      custom-named compatible endpoints that back an adaptive-capable model opt in
      even when the model name does not encode a parseable Claude version.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 2-model-support-changes-in-kimi-code-0-7-0
  source_release: kimi-code-2026-06-02-0-7-0-ba929959
  source_type: kimi_code_changelog
  theme: model-support
  title: 2 Model Support changes in Kimi Code 0.7.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-02-removed-claude-code-opus-4-6-fast-mode-override-the-environment-variable-is-now|Removed
  CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE; the environment variable is now a no-op]]'
- '[[Changes/HeyGen/2026-06-02-ai-governance-provides-a-centralized-place-for-admins-to-manage-how-ai-powered-f|AI
  Governance – Provides a centralized place for admins to manage how AI-powered…]]'
- '[[Changes/Kimi Code/2026-06-02-4-model-support-changes-in-kimi-code-0-8-0|4 Model
  Support changes in Kimi Code 0.8.0]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-06-02-0-7-0-ba929959|kimi-code-2026-06-02-0-7-0-ba929959]]'
source_type: kimi_code_changelog
theme: model-support
title: 2 Model Support changes in Kimi Code 0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in Kimi Code 0.7.0

**Kimi Code** · 2026-06-02 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-06-02-0-7-0-ba929959|Kimi Code 0.7.0 (2026-06-02)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add `/provider` command for managing AI providers, support custom registry imports, and introduce a tabbed model selector. It replaces the deprecated `/connect` command — use `/provider` instead.

> Add `KIMI_MODEL_ADAPTIVE_THINKING` (and a matching `adaptive_thinking` model-alias field) to force adaptive thinking (`thinking: { type: 'adaptive' }`) on or off, overriding the Anthropic model-name version inference. This lets custom-named compatible endpoints that back an adaptive-capable model opt in even when the model name does not encode a parseable Claude version.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-06-02-render-scheduled-reminders-distinctly-in-the-tui-expose-cron-fired-events-to-sdk|Render scheduled reminders distinctly in the TUI, expose cron fired events to SDK…]] · Automation and Scheduling
- [[Changes/Kimi Code/2026-06-02-report-truncated-compaction-summaries-clearly-and-apply-valid-completion-token-b|Report truncated compaction summaries clearly and apply valid completion token…]] · Editor Experience
- [[Changes/Kimi Code/2026-06-02-clarify-kimi-platform-api-key-login-labels-and-prompt-details|Clarify Kimi Platform API key login labels and prompt details]] · Account and Access
- [[Changes/Kimi Code/2026-06-02-polish-a-small-tui-visual-interaction|Polish a small TUI visual interaction]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-02 · Kimi Code · [[Changes/Kimi Code/2026-06-02-4-model-support-changes-in-kimi-code-0-8-0|4 Model Support changes in Kimi Code 0.8.0]]
- Later: 2026-06-02 · Krea · [[Changes/Krea/2026-06-02-krea-2-on-artificial-analysis|Krea 2 on Artificial Analysis]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-06-02-b2844e&body=Card%3A%20Changes%2FKimi%20Code%2F2026-06-02-2-model-support-changes-in-kimi-code-0-7-0.md%0ACard%20ID%3A%20kimi-code-2026-06-02-b2844e%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->