---
card_id: cline-2026-10-07-23efa0
date: '2026-10-07'
description: 'Cline · 2026-10-07 · Model Support: 3 changes in v4.1.23 — If a model''s
  response ends without a recognized finish reason, Cline asks it to continue once…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1367
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b72dcec78c508066f6c34573b07e146d4e8ed45b65df1b48f2f3df76124e0d62
product: cline
product_name: Cline
record:
  card_id: cline-2026-10-07-23efa0
  comparison: ''
  date: '2026-10-07'
  description: 'Cline — v4.1.23: 3 Model Support changes'
  evidence:
  - quote: If a model's response ends without a recognized finish reason, Cline asks
      it to continue once instead of treating the response as complete.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.23
  - quote: Refreshed the model catalog. The Cline recommended list adds GPT-6.1 Sol,
      and the free list adds Solar Mini 4 and drops DeepSeek V4.1 Flash and space-bunny-alpha.
      Default models change for 302.AI, AKI.IO, Blue Claw, CoralBricks, CrossModel,
      DevPass, DigitalOcean, GMI Cloud, LLM Gateway, Mistral, NanoGPT, Neon, Nvidia,
      Ofox, Requesty, Subconscious, The Grid AI, Vivgrid, and Vultr. Vultr's model
      ids were renamed upstream, so a pinned Vultr model may need to be re-selected.
      If you use one of those providers without pinning a model, expect a different
      default.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.23
  - quote: Kimi K3 and other models that only accept certain reasoning levels no longer
      reject requests. Cline picks the closest level the model supports.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.23
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 3-model-support-changes-in-v4-1-23
  source_release: cline-2026-10-07-v4-1-23-github-405494670-768378b9
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in v4.1.23
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-10-07-we-re-introducing-gpt-6-with-intelligent-ui-in-chatgpt-chatgpt-can-now-combine-t|GPT-6
  and Intelligent UI in ChatGPT]]'
- '[[Changes/Claude/2026-10-07-claude-haiku-5-5-launch|Claude Haiku 5.5 launch]]'
- '[[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added
  Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]]'
source_release: '[[Releases/Cline/cline-2026-10-07-v4-1-23-github-405494670-768378b9|cline-2026-10-07-v4-1-23-github-405494670-768378b9]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in v4.1.23
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in v4.1.23

**Cline** · 2026-10-07 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.23) · from [[Releases/Cline/cline-2026-10-07-v4-1-23-github-405494670-768378b9|v4.1.23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> If a model's response ends without a recognized finish reason, Cline asks it to continue once instead of treating the response as complete.

> Refreshed the model catalog. The Cline recommended list adds GPT-6.1 Sol, and the free list adds Solar Mini 4 and drops DeepSeek V4.1 Flash and space-bunny-alpha. Default models change for 302.AI, AKI.IO, Blue Claw, CoralBricks, CrossModel, DevPass, DigitalOcean, GMI Cloud, LLM Gateway, Mistral, NanoGPT, Neon, Nvidia, Ofox, Requesty, Subconscious, The Grid AI, Vivgrid, and Vultr. Vultr's model ids were renamed upstream, so a pinned Vultr model may need to be re-selected. If you use one of those providers without pinning a model, expect a different default.

> Kimi K3 and other models that only accept certain reasoning levels no longer reject requests. Cline picks the closest level the model supports.

Source: https://github.com/cline/cline/releases/tag/v4.1.23
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-10-07-when-an-mcp-tool-returns-more-output-than-fits-in-context-cline-can-now-read-the|When an MCP tool returns more output than fits in context, Cline can now read the rest]] · Apps and Integrations
- [[Changes/Cline/2026-10-07-generate-commit-message-now-follows-your-clinerules-so-conventions-like-language|Generate Commit Message now follows your .clinerules, so conventions like…]] · Developer Workflow
- [[Changes/Cline/2026-10-07-3-other-changes-in-v4-1-23|3 other changes in v4.1.23]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-07 · Claude Code · [[Changes/Claude Code/2026-10-07-added-claude-haiku-5-5-claude-haiku-5-5-now-the-default-haiku-model-on-the-anthr|Added Claude Haiku 5.5 (claude-haiku-5-5), now the default Haiku model…]]
- Later: 2026-10-07 · Codex CLI · [[Changes/Codex CLI/2026-10-07-9-model-support-changes-in-rust-v0-161-0|9 Model Support changes in rust-v0.161.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-10-07-23efa0&body=Card%3A%20Changes%2FCline%2F2026-10-07-3-model-support-changes-in-v4-1-23.md%0ACard%20ID%3A%20cline-2026-10-07-23efa0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.23%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->