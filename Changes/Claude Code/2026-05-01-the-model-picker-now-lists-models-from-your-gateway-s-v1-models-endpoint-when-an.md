---
card_id: claude-code-2026-05-01-f3cdd1
date: '2026-05-01'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1208
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-22-improved-model-selections-now-persist-across-restarts-even-when-the-project-pins|claude-code-2026-04-22-aaa371]]'
extractor_version: fallback-v2
impact: significant
machine_hash: efb3cfb0a8dab0af0057d9a82ae20911611cadfbd4c238503b8984660898daf3
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-16-added-xhigh-effort-level-for-opus-4-7-sitting-between-high-and-max-available-via|claude-code-2026-04-16-9592dc]]'
- '[[Changes/Claude Code/2026-04-22-improved-model-selections-now-persist-across-restarts-even-when-the-project-pins|claude-code-2026-04-22-aaa371]]'
- '[[Changes/ChatGPT/2026-04-28-we-re-making-it-easier-to-choose-the-right-model-before-you-send-a-message-model|chatgpt-2026-04-28-5e72af]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb|claude-code-2026-05-01-v2-1-126-github-316244540-de18d9bb]]'
theme: model-support
type: change
---

# The `/model` picker now lists models from your gateway's `/v1/models` endpoint w

<!-- chronolog:begin region="description" -->
The `/model` picker now lists models from your gateway's `/v1/models` endpoint when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The `/model` picker now lists models from your gateway's `/v1/models` endpoint when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.126
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-22-improved-model-selections-now-persist-across-restarts-even-when-the-project-pins|claude-code-2026-04-22-aaa371]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1208
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes