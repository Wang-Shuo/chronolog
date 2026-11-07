---
card_id: openclaw-2026-10-08-1df4ac
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Context Window: Model retries and context. One-shot
  model requests through the Gateway retain the original task when retrying the same…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2577
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 10fd7685bc48a4c8c5c364e28cb2df0d41b1d6bdbd51327b6adf1210c9a0bc5b
product: openclaw
product_name: OpenClaw
record:
  ai_generated: true
  card_id: openclaw-2026-10-08-1df4ac
  comparison: ''
  confidence: low
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: Model retries and context. One-shot model requests
    through the Gateway retain the original task when retrying the same model. Chat
    Completions conversations also use valid provider token counts to judge how full
    the conversation is, reducing reliance on estimates that can trigger recovery
    too early. #160803 by @changeroa , reported by @Oldrich333 and verified by @obviyus
    ; ab24b53 by @RileyJJY .'
  evidence:
  - quote: 'Model retries and context. One-shot model requests through the Gateway
      retain the original task when retrying the same model. Chat Completions conversations
      also use valid provider token counts to judge how full the conversation is,
      reducing reliance on estimates that can trigger recovery too early. #160803
      by @changeroa , reported by @Oldrich333 and verified by @obviyus ; ab24b53 by
      @RileyJJY .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: openclaw
  product_name: OpenClaw
  slug: model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: context-window
  theme_matches:
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Model retries and context
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved
  token counts behind a Claude apps gateway on Amazon Bedrock…]]'
- '[[Changes/Codex CLI/2026-10-08-10-context-window-changes-in-rust-v0-162-0|10 Context
  Window changes in rust-v0.162.0]]'
- '[[Changes/Ollama/2026-10-08-ollama-launch-claude-uses-the-model-s-full-context-length-by-jberg5-in-https-git|ollama
  launch claude uses the model''s full context length]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: context-window
title: Model retries and context
type: change
---

<!-- chronolog:begin region="header" -->
# Model retries and context

**OpenClaw** · 2026-10-08 · [[Themes/context-window|Context Window]] · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Model retries and context. One-shot model requests through the Gateway retain the original task when retrying the same model. Chat Completions conversations also use valid provider token counts to judge how full the conversation is, reducing reliance on estimates that can trigger recovery too early. #160803 by @changeroa , reported by @Oldrich333 and verified by @obviyus ; ab24b53 by @RileyJJY .
>
> Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-08 · Ollama · [[Changes/Ollama/2026-10-08-ollama-launch-claude-uses-the-model-s-full-context-length-by-jberg5-in-https-git|ollama launch claude uses the model's full context length]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context Window changes in v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-1df4ac&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the.md%0ACard%20ID%3A%20openclaw-2026-10-08-1df4ac%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->