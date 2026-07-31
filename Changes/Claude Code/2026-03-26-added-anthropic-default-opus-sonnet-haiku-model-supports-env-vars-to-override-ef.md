---
card_id: claude-code-2026-03-26-3c8e42
date: '2026-03-26'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1172
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|claude-code-2026-03-19-9f5e79]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 162ff0234828e10071aede7a15d426fb890ac467381b248f617414fce82e61e9
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|claude-code-2026-03-17-edeb5b]]'
- '[[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|claude-code-2026-03-19-9f5e79]]'
- '[[Changes/Cursor/2026-03-25-self-hosted-cloud-agents-offer-the-same-capabilities-as-cursor-hosted-cloud-agen|cursor-2026-03-25-6db779]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
theme: model-support
type: change
---

# Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to overrid

<!-- chronolog:begin region="description" -->
Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override effort/thinking capability detection for pinned default models for 3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize the `/model` picker label
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override effort/thinking capability detection for pinned default models for 3p (Bedrock, Vertex, Foundry), and `_MODEL_NAME`/`_DESCRIPTION` to customize the `/model` picker label
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-19-added-effort-frontmatter-support-for-skills-and-slash-commands-to-override-the-m|claude-code-2026-03-19-9f5e79]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1172
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes