---
card_id: openclaw-2026-10-18-819292
date: '2026-10-18'
description: 'OpenClaw · 2026-10-18 · Model Support: 4 changes in v2026.10.5 — Background
  learning sends conversation and tool content to your configured model provider and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1378
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b69f8a4f742de7e8068d9a12cdbb47fe0286929243e0ca083d90a6591a28a9d6
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-18-819292
  comparison: ''
  date: '2026-10-18'
  description: 'OpenClaw — v2026.10.5: 4 Model Support changes'
  evidence:
  - quote: Background learning sends conversation and tool content to your configured
      model provider and can add usage charges. Choose Off to stop background learning
      and unused-skill cleanup; you can still request learning with /learn .
    source_release: https://docs.openclaw.ai/releases/2026.10.5
  - quote: Model selection and sign-in recover through more credential and connection
      changes, and local runtimes get setup and tool-use fixes. Google and Vertex
      add Gemini 4 Argon, while Google also adds Gemini 3.8 Flash.
    source_release: https://docs.openclaw.ai/releases/2026.10.5
  - quote: Rerunning Google API-key setup chooses Argon as the primary model, so check
      that choice if you want to keep another default.
    source_release: https://docs.openclaw.ai/releases/2026.10.5
  - quote: Scheduled jobs retain saved model choices and return results to the chat
      that created them through more recovery and delivery cases. Webhooks can reject
      work when capacity is unavailable so senders can retry.
    source_release: https://docs.openclaw.ai/releases/2026.10.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-model-support-changes-in-v2026-10-5
  source_release: openclaw-2026-10-18-v2026-10-5-fdda4c73
  source_type: openclaw_changelog
  theme: model-support
  title: 4 Model Support changes in v2026.10.5
  type: change
related_changes:
- '[[Changes/v0/2026-10-16-gemini-4-requests-no-longer-fail-when-run-at-higher-effort-levels|Gemini
  4 requests no longer fail when run at higher effort levels]]'
- '[[Changes/DeepSeek API/2026-10-17-deepseek-v4-1-flash-1017-update|DeepSeek-V4.1-Flash-1017
  Update]]'
- '[[Changes/Ollama/2026-10-18-6-model-support-changes-in-v0-40-7|6 Model Support
  changes in v0.40.7]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-18-v2026-10-5-fdda4c73|openclaw-2026-10-18-v2026-10-5-fdda4c73]]'
source_type: openclaw_changelog
theme: model-support
title: 4 Model Support changes in v2026.10.5
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2026.10.5

**OpenClaw** · 2026-10-18 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.5) · from [[Releases/OpenClaw/openclaw-2026-10-18-v2026-10-5-fdda4c73|v2026.10.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Background learning sends conversation and tool content to your configured model provider and can add usage charges. Choose Off to stop background learning and unused-skill cleanup; you can still request learning with /learn .

> Model selection and sign-in recover through more credential and connection changes, and local runtimes get setup and tool-use fixes. Google and Vertex add Gemini 4 Argon, while Google also adds Gemini 3.8 Flash.

> Rerunning Google API-key setup chooses Argon as the primary model, so check that choice if you want to keep another default.

> Scheduled jobs retain saved model choices and return results to the chat that created them through more recovery and delivery cases. Webhooks can reject work when capacity is unavailable so senders can retry.

Source: https://docs.openclaw.ai/releases/2026.10.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-18-memory-search-recognizes-more-accented-and-korean-spellings-and-keeps-keyword-se|Memory search recognizes more accented and Korean spellings and keeps keyword search…]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-18-2-developer-workflow-changes-in-v2026-10-5|2 Developer Workflow changes in v2026.10.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-18-2-agent-mode-changes-in-v2026-10-5|2 Agent Mode changes in v2026.10.5]] · Agent Mode
- [[Changes/OpenClaw/2026-10-18-3-apps-and-integrations-changes-in-v2026-10-5|3 Apps and Integrations changes in v2026.10.5]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-18-the-dashboard-handles-reconnects-and-long-chat-histories-with-fewer-interruption|The Dashboard handles reconnects and long chat histories with fewer interruptions…]] · Account and Access
- [[Changes/OpenClaw/2026-10-18-openclaw-2026-10-5-refreshes-the-sidebar-adds-saved-versions-and-undo-to-skill-w|OpenClaw 2026.10.5 refreshes the sidebar, adds saved versions and Undo to Skill…]] · Interface Experience
- [[Changes/OpenClaw/2026-10-18-review-the-conversation-before-publishing-the-link-exposes-existing-and-future-u|Review the conversation before publishing]] · Collaboration
- [[Changes/OpenClaw/2026-10-18-8-other-changes-in-v2026-10-5|8 other changes in v2026.10.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-18 · Ollama · [[Changes/Ollama/2026-10-18-6-model-support-changes-in-v0-40-7|6 Model Support changes in v0.40.7]]
- Later: 2026-10-19 · Claude Code · [[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support changes in v2.1.304]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-18-819292&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-18-4-model-support-changes-in-v2026-10-5.md%0ACard%20ID%3A%20openclaw-2026-10-18-819292%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->