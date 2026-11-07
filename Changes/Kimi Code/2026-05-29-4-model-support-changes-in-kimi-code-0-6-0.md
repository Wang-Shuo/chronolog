---
card_id: kimi-code-2026-05-29-977ed0
date: '2026-05-29'
description: 'Kimi Code · 2026-05-29 · Model Support: 4 changes in Kimi Code 0.6.0
  (2026-05-29) — Recover from provider model token limit errors during long conversations.'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1236
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9fea25baf00407eb7535062dd16a813028750f3b4439d7ddf8220aa4adeffc51
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-05-29-977ed0
  comparison: ''
  date: '2026-05-29'
  description: 'Kimi Code — Kimi Code 0.6.0 (2026-05-29): 4 Model Support changes'
  evidence:
  - quote: Recover from provider model token limit errors during long conversations.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Automatically retry when a model response stream is dropped mid-flight
      (a `terminated` error) instead of failing the turn.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Keep blocked prompt hook conversations available to subsequent model turns.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Slim the LLM diagnostic logs with fewer, more compact fields.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 4-model-support-changes-in-kimi-code-0-6-0
  source_release: kimi-code-2026-05-29-0-6-0-a089212f
  source_type: kimi_code_changelog
  theme: model-support
  title: 4 Model Support changes in Kimi Code 0.6.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-28-3-model-support-changes-in-v1-0-55|3 Model
  Support changes in v1.0.55]]'
- '[[Changes/OpenCode/2026-05-28-2-model-support-changes-in-v1-15-12|2 Model Support
  changes in v1.15.12]]'
- '[[Changes/GitHub Copilot CLI/2026-05-29-2-model-support-changes-in-v1-0-56|2 Model
  Support changes in v1.0.56]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-05-29-0-6-0-a089212f|kimi-code-2026-05-29-0-6-0-a089212f]]'
source_type: kimi_code_changelog
theme: model-support
title: 4 Model Support changes in Kimi Code 0.6.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in Kimi Code 0.6.0

**Kimi Code** · 2026-05-29 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-05-29-0-6-0-a089212f|Kimi Code 0.6.0 (2026-05-29)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Recover from provider model token limit errors during long conversations.

> Automatically retry when a model response stream is dropped mid-flight (a `terminated` error) instead of failing the turn.

> Keep blocked prompt hook conversations available to subsequent model turns.

> Slim the LLM diagnostic logs with fewer, more compact fields.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-05-29-relocate-shared-tool-service-typing-to-the-tool-support-layer|Relocate shared tool service typing to the tool support layer]] · Collaboration
- [[Changes/Kimi Code/2026-05-29-3-apps-and-integrations-changes-in-kimi-code-0-6-0|3 Apps and Integrations changes in Kimi Code 0.6.0]] · Apps and Integrations
- [[Changes/Kimi Code/2026-05-29-4-context-window-changes-in-kimi-code-0-6-0|4 Context Window changes in Kimi Code 0.6.0]] · Context Window
- [[Changes/Kimi Code/2026-05-29-3-agent-mode-changes-in-kimi-code-0-6-0|3 Agent Mode changes in Kimi Code 0.6.0]] · Agent Mode
- [[Changes/Kimi Code/2026-05-29-support-querying-sessions-by-sessionid-or-workdir-in-listsessions-and-show-a-hel|Support querying sessions by sessionId or workDir in listSessions, and show…]] · Developer Workflow
- [[Changes/Kimi Code/2026-05-29-4-other-changes-in-kimi-code-0-6-0|4 other changes in Kimi Code 0.6.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-29 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-29-2-model-support-changes-in-v1-0-56|2 Model Support changes in v1.0.56]]
- Later: 2026-05-30 · Claude Code · [[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4|Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-05-29-977ed0&body=Card%3A%20Changes%2FKimi%20Code%2F2026-05-29-4-model-support-changes-in-kimi-code-0-6-0.md%0ACard%20ID%3A%20kimi-code-2026-05-29-977ed0%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->