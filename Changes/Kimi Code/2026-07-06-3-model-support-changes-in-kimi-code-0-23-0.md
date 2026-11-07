---
card_id: kimi-code-2026-07-06-b1b89d
date: '2026-07-06'
description: 'Kimi Code · 2026-07-06 · Model Support: 3 changes in Kimi Code 0.23.0
  (2026-07-06) — Add experimental on-demand tool loading (`select_tools`) under the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1274
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 31834082add53c5ddcd9cd3b72c6e96a44cc172f6cb41c437109000a39d9d9db
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-07-06-b1b89d
  comparison: ''
  date: '2026-07-06'
  description: 'Kimi Code — Kimi Code 0.23.0 (2026-07-06): 3 Model Support changes'
  evidence:
  - quote: 'Add experimental on-demand tool loading (`select_tools`) under the `tool-select`
      flag: a supporting model loads MCP tools only when needed instead of sending
      all of them in every request, preserving the provider prompt cache. Off by default
      and only active on models that declare the `select_tools` capability.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Feed AskUserQuestion answers back to the model as question text and option
      labels instead of positional ids, so the model no longer has to map them back.
      Question texts must now be unique per call and option labels unique per question;
      existing clients keep answering with option ids, so no client change is required.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Keep prior reasoning across turns for Kimi models by default when Thinking
      is on. Set `[thinking] keep = "off"` to disable.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 3-model-support-changes-in-kimi-code-0-23-0
  source_release: kimi-code-2026-07-06-0-23-0-6c09d1f0
  source_type: kimi_code_changelog
  theme: model-support
  title: 3 Model Support changes in Kimi Code 0.23.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-07-06-we-re-rolling-out-gpt-5-5-instant-mini-in-chatgpt-it-replaces-gpt-5-3-instant-mi|GPT-5.5
  Instant Mini in ChatGPT]]'
- '[[Changes/ElevenLabs/2026-07-06-elevencreative-studio|ElevenCreative Studio]]'
- '[[Changes/ElevenLabs/2026-07-06-elevencreative-studio-d7b18f|ElevenCreative Studio]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-06-0-23-0-6c09d1f0|kimi-code-2026-07-06-0-23-0-6c09d1f0]]'
source_type: kimi_code_changelog
theme: model-support
title: 3 Model Support changes in Kimi Code 0.23.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in Kimi Code 0.23.0

**Kimi Code** · 2026-07-06 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-06-0-23-0-6c09d1f0|Kimi Code 0.23.0 (2026-07-06)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add experimental on-demand tool loading (`select_tools`) under the `tool-select` flag: a supporting model loads MCP tools only when needed instead of sending all of them in every request, preserving the provider prompt cache. Off by default and only active on models that declare the `select_tools` capability.

> Feed AskUserQuestion answers back to the model as question text and option labels instead of positional ids, so the model no longer has to map them back. Question texts must now be unique per call and option labels unique per question; existing clients keep answering with option ids, so no client change is required.

> Keep prior reasoning across turns for Kimi models by default when Thinking is on. Set `[thinking] keep = "off"` to disable.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-07-06-3-mobile-and-desktop-changes-in-kimi-code-0-23-0|3 Mobile and Desktop changes in Kimi Code 0.23.0]] · Mobile and Desktop
- [[Changes/Kimi Code/2026-07-06-web-replace-the-swarm-footer-with-a-single-inline-tool-card-that-shows-live-suba|web: Replace the swarm footer with a single inline tool card that shows live…]] · Agent Mode
- [[Changes/Kimi Code/2026-07-06-2-context-window-changes-in-kimi-code-0-23-0|2 Context Window changes in Kimi Code 0.23.0]] · Context Window
- [[Changes/Kimi Code/2026-07-06-web-add-an-archived-sessions-page-in-settings-to-browse-and-restore-archived-ses|web: Add an Archived sessions page in Settings to browse and restore archived sessions]] · Search and Browsing
- [[Changes/Kimi Code/2026-07-06-web-align-the-markdown-diff-code-block-with-the-design-system-code-text-keeps-th|web: Align the markdown diff code block with the design system: code text keeps…]] · Editor Experience
- [[Changes/Kimi Code/2026-07-06-4-other-changes-in-kimi-code-0-23-0|4 other changes in Kimi Code 0.23.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-06 · ElevenLabs · [[Changes/ElevenLabs/2026-07-06-elevencreative-studio-d7b18f|ElevenCreative Studio]]
- Later: 2026-07-06 · Ollama · [[Changes/Ollama/2026-07-06-hardened-gguf-model-creation|Hardened GGUF model creation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-06-b1b89d&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-06-3-model-support-changes-in-kimi-code-0-23-0.md%0ACard%20ID%3A%20kimi-code-2026-07-06-b1b89d%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->