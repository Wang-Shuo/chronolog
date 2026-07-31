---
card_id: claude-code-2026-06-29-34190b
date: '2026-06-29'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1267
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|claude-code-2026-06-25-82838a]]'
extractor_version: fallback-v2
impact: significant
machine_hash: d0006bc6509c138da0984c6cb307b8a7b103d493456a26d478c0fe7cfd543540
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-06-24-we-re-updating-gpt-5-5-instant-our-most-used-model-in-chatgpt-to-improve-convers|chatgpt-2026-06-24-0f2a65]]'
- '[[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|claude-code-2026-06-25-82838a]]'
- '[[Changes/ChatGPT/2026-06-26-as-of-june-26-2026-gpt-4-5-is-no-longer-available-in-chatgpt-including-for-custo|chatgpt-2026-06-26-46ba84]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-29-v2-1-196-github-346482381-e21be272|claude-code-2026-06-29-v2-1-196-github-346482381-e21be272]]'
theme: model-support
type: change
---

# Added support for organization default models — admins set it in the org console

<!-- chronolog:begin region="description" -->
Added support for organization default models — admins set it in the org console; it shows as "Org default" (or "Role default") in `/model` when you haven't picked one yourself
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added support for organization default models — admins set it in the org console; it shows as "Org default" (or "Role default") in `/model` when you haven't picked one yourself
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.196
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|claude-code-2026-06-25-82838a]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1267
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes