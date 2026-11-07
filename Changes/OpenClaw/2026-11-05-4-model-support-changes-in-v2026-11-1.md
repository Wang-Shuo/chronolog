---
card_id: openclaw-2026-11-05-548efd
date: '2026-11-05'
description: 'OpenClaw · 2026-11-05 · Model Support: 4 changes in v2026.11.1 — Changes
  Gemini Flash text models on the official Google AI Studio endpoint to use Interactions…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1396
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cf5cdc24d19963bdd2d55d3632d6b19709150755eef6bac5027ef52a26ea4dc0
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-11-05-548efd
  comparison: ''
  date: '2026-11-05'
  description: 'OpenClaw — v2026.11.1: 4 Model Support changes'
  evidence:
  - quote: Changes Gemini Flash text models on the official Google AI Studio endpoint
      to use Interactions by default, with more consistent request settings, key rotation
      and sampling. Explicit API settings take precedence, and custom endpoints default
      to GenerateContent. Interactions ignores explicit cache handles; select google-generative-ai
      if you need them. See the Google provider guide .
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Reports the output limit when it stops a reasoning-only turn, and warns
      you to check a timed-out tool’s result before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Uses the provider’s wait time for rate-limited model profiles and allows
      retry on a later turn when no wait time is available.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  - quote: Changes requests to numbered OpenAI GPT models found by Bedrock Mantle
      to use the Responses API.
    source_release: https://docs.openclaw.ai/releases/2026.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-model-support-changes-in-v2026-11-1
  source_release: openclaw-2026-11-05-v2026-11-1-7d3de823
  source_type: openclaw_changelog
  theme: model-support
  title: 4 Model Support changes in v2026.11.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-11-03-17-model-support-changes-in-v2026-10-10|17 Model
  Support changes in v2026.10.10]]'
- '[[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes
  in 1.19.0]]'
- '[[Changes/Gemini CLI/2026-11-04-feat-cli-add-models-command-and-list-models-flag-for-model-discovery-by-urielefr|feat(cli):
  add models command and --list-models flag for model discovery]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-11-05-v2026-11-1-7d3de823|openclaw-2026-11-05-v2026-11-1-7d3de823]]'
source_type: openclaw_changelog
theme: model-support
title: 4 Model Support changes in v2026.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2026.11.1

**OpenClaw** · 2026-11-05 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.11.1) · from [[Releases/OpenClaw/openclaw-2026-11-05-v2026-11-1-7d3de823|v2026.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changes Gemini Flash text models on the official Google AI Studio endpoint to use Interactions by default, with more consistent request settings, key rotation and sampling. Explicit API settings take precedence, and custom endpoints default to GenerateContent. Interactions ignores explicit cache handles; select google-generative-ai if you need them. See the Google provider guide .

> Reports the output limit when it stops a reasoning-only turn, and warns you to check a timed-out tool’s result before retrying.

> Uses the provider’s wait time for rate-limited model profiles and allows retry on a later turn when no wait time is available.

> Changes requests to numbered OpenAI GPT models found by Bedrock Mantle to use the Responses API.

Source: https://docs.openclaw.ai/releases/2026.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-11-05-reduces-prompt-cache-misses-across-completion-heartbeat-and-background-turns-by|Reduces prompt-cache misses across completion, heartbeat and background turns…]] · Editor Experience
- [[Changes/OpenClaw/2026-11-05-keeps-accepted-talk-work-running-when-you-end-talk-on-an-android-phone-connected|Keeps accepted Talk work running when you end Talk on an Android phone connected…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-11-05-5-apps-and-integrations-changes-in-v2026-11-1|5 Apps and Integrations changes in v2026.11.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-11-05-3-context-window-changes-in-v2026-11-1|3 Context Window changes in v2026.11.1]] · Context Window
- [[Changes/OpenClaw/2026-11-05-7-voice-and-audio-changes-in-v2026-11-1|7 Voice and Audio changes in v2026.11.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-11-05-5-memory-and-personalization-changes-in-v2026-11-1|5 Memory and Personalization changes in v2026.11.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-11-05-2-safety-and-privacy-changes-in-v2026-11-1|2 Safety and Privacy changes in v2026.11.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-11-05-prevents-oversized-mac-camera-clips-and-screen-recordings-from-disconnecting-the|Prevents oversized Mac camera clips and screen recordings from disconnecting…]] · Multimodal Input
- [[Changes/OpenClaw/2026-11-05-4-agent-mode-changes-in-v2026-11-1|4 Agent Mode changes in v2026.11.1]] · Agent Mode
- [[Changes/OpenClaw/2026-11-05-4-account-and-access-changes-in-v2026-11-1|4 Account and Access changes in v2026.11.1]] · Account and Access
- [[Changes/OpenClaw/2026-11-05-avoids-restoring-cold-archived-conversations-just-to-refresh-usage-and-cost-repo|Avoids restoring cold archived conversations just to refresh usage and cost reports…]] · Pricing Model
- [[Changes/OpenClaw/2026-11-05-allows-authorized-native-commands-to-restore-archived-source-sessions-and-report|Allows authorized native commands to restore archived source sessions, and reports…]] · Collaboration
- [[Changes/OpenClaw/2026-11-05-3-developer-workflow-changes-in-v2026-11-1|3 Developer Workflow changes in v2026.11.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-11-05-keeps-the-windows-scheduled-task-available-during-update-recovery-until-the-gate|Keeps the Windows scheduled task available during update recovery until the Gateway…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-11-05-40-other-changes-in-v2026-11-1|40 other changes in v2026.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-11-04 · Gemini CLI · [[Changes/Gemini CLI/2026-11-04-feat-cli-add-models-command-and-list-models-flag-for-model-discovery-by-urielefr|feat(cli): add models command and --list-models flag for model discovery]]
- Later: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-7-model-support-changes-in-rust-v0-167-0|7 Model Support changes in rust-v0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-11-05-548efd&body=Card%3A%20Changes%2FOpenClaw%2F2026-11-05-4-model-support-changes-in-v2026-11-1.md%0ACard%20ID%3A%20openclaw-2026-11-05-548efd%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->