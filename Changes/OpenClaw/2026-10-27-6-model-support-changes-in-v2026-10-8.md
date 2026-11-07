---
card_id: openclaw-2026-10-27-1c5b2b
date: '2026-10-27'
description: 'OpenClaw · 2026-10-27 · Model Support: 6 changes in v2026.10.8 — Doctor
  now keeps the model you chose for summarizing long Codex conversations. If an earlier…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1387
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 86c0245f8ce5131b22d0c87b2ea17b30bff793bb90f99c77ceb34133d4f16a34
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-27-1c5b2b
  comparison: ''
  date: '2026-10-27'
  description: 'OpenClaw — v2026.10.8: 6 Model Support changes'
  evidence:
  - quote: Doctor now keeps the model you chose for summarizing long Codex conversations.
      If an earlier repair deleted that setting, restore it manually.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Incoming messages can now trigger recovery of a failed model runtime without
      a Gateway restart. If both recovery attempts fail, the input is retained for
      an operator to inspect and resend after fixing the problem.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Oversized model-provider responses now report their streaming error promptly
      instead of leaving the request waiting.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Configured Claude CLI models remain selectable with eligible saved Anthropic
      subscription credentials, and model switches keep the configured CLI runtime.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Resumed Claude CLI and Gemini CLI sessions can receive recent conversation
      updates they missed while cron or Talk added activity to the same conversation.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  - quote: Long native conversations can use an eligible configured fallback model
      to summarize their history when the primary summary fails. Sessions locked to
      one model still refuse cross-model fallback.
    source_release: https://docs.openclaw.ai/releases/2026.10.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 6-model-support-changes-in-v2026-10-8
  source_release: openclaw-2026-10-27-v2026-10-8-9d674f40
  source_type: openclaw_changelog
  theme: model-support
  title: 6 Model Support changes in v2026.10.8
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-10-27-add-banner-about-gemini-cli-not-being-optimized-for-gemini-4-by-srithreepo-in-ht|Add
  Banner about Gemini CLI not being optimized for Gemini 4]]'
- '[[Changes/GitHub Copilot CLI/2026-10-27-managed-model-fusion-now-starts-sessions-on-auto-and-applies-fusiontier-settings|Managed
  model "fusion" now starts sessions on Auto and applies fusionTier settings]]'
- '[[Changes/Ollama/2026-10-27-speculative-decoding-now-supports-dflash2-draft-models-on-mlx|Speculative
  decoding now supports DFlash2 draft models on MLX]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|openclaw-2026-10-27-v2026-10-8-9d674f40]]'
source_type: openclaw_changelog
theme: model-support
title: 6 Model Support changes in v2026.10.8
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v2026.10.8

**OpenClaw** · 2026-10-27 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.8) · from [[Releases/OpenClaw/openclaw-2026-10-27-v2026-10-8-9d674f40|v2026.10.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Doctor now keeps the model you chose for summarizing long Codex conversations. If an earlier repair deleted that setting, restore it manually.

> Incoming messages can now trigger recovery of a failed model runtime without a Gateway restart. If both recovery attempts fail, the input is retained for an operator to inspect and resend after fixing the problem.

> Oversized model-provider responses now report their streaming error promptly instead of leaving the request waiting.

> Configured Claude CLI models remain selectable with eligible saved Anthropic subscription credentials, and model switches keep the configured CLI runtime.

> Resumed Claude CLI and Gemini CLI sessions can receive recent conversation updates they missed while cron or Talk added activity to the same conversation.

> Long native conversations can use an eligible configured fallback model to summarize their history when the primary summary fails. Sessions locked to one model still refuse cross-model fallback.

Source: https://docs.openclaw.ai/releases/2026.10.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-27-6-voice-and-audio-changes-in-v2026-10-8|6 Voice and Audio changes in v2026.10.8]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-27-2-developer-workflow-changes-in-v2026-10-8|2 Developer Workflow changes in v2026.10.8]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-27-on-linux-doctor-can-repair-a-managed-gateway-that-is-using-an-unsupported-node-v|On Linux, Doctor can repair a managed Gateway that is using an unsupported Node…]] · Interface Experience
- [[Changes/OpenClaw/2026-10-27-4-automation-and-scheduling-changes-in-v2026-10-8|4 Automation and Scheduling changes in v2026.10.8]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-27-oversized-macos-camera-clips-and-screen-recordings-now-return-an-error-instead-o|Oversized macOS camera clips and screen recordings now return an error instead…]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-27-future-macos-updates-wait-for-the-serving-gateway-to-exit-and-release-its-databa|Future macOS updates wait for the serving Gateway to exit and release its databases…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-27-4-memory-and-personalization-changes-in-v2026-10-8|4 Memory and Personalization changes in v2026.10.8]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-27-5-account-and-access-changes-in-v2026-10-8|5 Account and Access changes in v2026.10.8]] · Account and Access
- [[Changes/OpenClaw/2026-10-27-2-safety-and-privacy-changes-in-v2026-10-8|2 Safety and Privacy changes in v2026.10.8]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-27-the-control-ui-now-reconnects-when-a-visible-tab-has-lost-contact-but-still-show|The Control UI now reconnects when a visible tab has lost contact but still shows…]] · Editor Experience
- [[Changes/OpenClaw/2026-10-27-7-agent-mode-changes-in-v2026-10-8|7 Agent Mode changes in v2026.10.8]] · Agent Mode
- [[Changes/OpenClaw/2026-10-27-9-apps-and-integrations-changes-in-v2026-10-8|9 Apps and Integrations changes in v2026.10.8]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-27-malformed-microsoft-teams-message-html-no-longer-causes-the-parsing-stalls-that|Malformed Microsoft Teams message HTML no longer causes the parsing stalls…]] · Collaboration
- [[Changes/OpenClaw/2026-10-27-32-other-changes-in-v2026-10-8|32 other changes in v2026.10.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-27 · Ollama · [[Changes/Ollama/2026-10-27-speculative-decoding-now-supports-dflash2-draft-models-on-mlx|Speculative decoding now supports DFlash2 draft models on MLX]]
- Later: 2026-10-27 · OpenCode · [[Changes/OpenCode/2026-10-27-13-model-support-changes-in-v2-2-0|13 Model Support changes in v2.2.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-27-1c5b2b&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-27-6-model-support-changes-in-v2026-10-8.md%0ACard%20ID%3A%20openclaw-2026-10-27-1c5b2b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->