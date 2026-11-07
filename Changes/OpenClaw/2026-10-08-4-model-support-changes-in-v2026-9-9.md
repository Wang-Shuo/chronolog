---
card_id: openclaw-2026-10-08-8710d6
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Model Support: 4 changes in v2026.9.9 — OpenClaw
  2026.9.9 adds GPT-6.1 Sol to the Codex model list and supports Claude Haiku 5.5…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1368
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f8600b817d7ab8d0c63c8ac378892bfc9769dec58b2c704dced0b1d146d60240
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-8710d6
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 4 Model Support changes'
  evidence:
  - quote: OpenClaw 2026.9.9 adds GPT-6.1 Sol to the Codex model list and supports
      Claude Haiku 5.5 through Anthropic and Claude CLI, improves recovery after failed
      updates, fixes missing iMessage replies, and keeps an old scheduled job from
      interrupting a newer conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Conversation titles. When your model server handles one request at a time,
      OpenClaw can try naming a new conversation again after its first reply finishes
      instead of leaving it with a random name. Names you choose yourself are preserved.
      #163817 by @MertBasar0 and @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: GPT-6.1 Sol. The Codex model list includes GPT-6.1 Sol, though using it
      still requires an eligible account and a compatible Codex setup , including
      the related provider support . When Codex repeatedly refuses an action, the
      request can also finish instead of remaining stuck until it times out. 65e89fc
      by @IstiqlalBhat , with coauthors @RomneyDa and @fuller-stack-dev .
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Editing scheduled jobs. Agents can recover from supported mistakes in
      how a model formats a scheduled-job update, instead of repeatedly failing and
      leaving the old message in place. #158543 by @carlosjarenom , reported by @louria
      and verified by @obviyus .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-model-support-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: model-support
  title: 4 Model Support changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-08-add-claude-haiku-5-5-to-model-selection-and-model-completions|Add
  Claude Haiku 5.5 to model selection and --model completions]]'
- '[[Changes/Midjourney/2026-10-08-we-re-finding-in-tests-that-this-helps-make-the-model-better-at-prompt-accuracy|We''re
  finding in tests that this helps make the model better at prompt accuracy…]]'
- '[[Changes/Ollama/2026-10-08-4-model-support-changes-in-v0-40-2|4 Model Support
  changes in v0.40.2]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: model-support
title: 4 Model Support changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw 2026.9.9 adds GPT-6.1 Sol to the Codex model list and supports Claude Haiku 5.5 through Anthropic and Claude CLI, improves recovery after failed updates, fixes missing iMessage replies, and keeps an old scheduled job from interrupting a newer conversation.

> Conversation titles. When your model server handles one request at a time, OpenClaw can try naming a new conversation again after its first reply finishes instead of leaving it with a random name. Names you choose yourself are preserved. #163817 by @MertBasar0 and @obviyus .

> GPT-6.1 Sol. The Codex model list includes GPT-6.1 Sol, though using it still requires an eligible account and a compatible Codex setup , including the related provider support . When Codex repeatedly refuses an action, the request can also finish instead of remaining stuck until it times out. 65e89fc by @IstiqlalBhat , with coauthors @RomneyDa and @fuller-stack-dev .

> Editing scheduled jobs. Agents can recover from supported mistakes in how a model formats a scheduled-job update, instead of repeatedly failing and leaving the old message in place. #158543 by @carlosjarenom , reported by @louria and verified by @obviyus .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the|Model retries and context]] · Context Window
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-08 · Ollama · [[Changes/Ollama/2026-10-08-4-model-support-changes-in-v0-40-2|4 Model Support changes in v0.40.2]]
- Later: 2026-10-08 · OpenHands · [[Changes/OpenHands/2026-10-08-test-e2e-launch-the-same-model-profile-test-from-the-beta-profile-by-enyst-in-ht|test(e2e): launch the same-model profile test from the BETA profile]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-8710d6&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-4-model-support-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-8710d6%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->