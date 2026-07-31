---
card_id: claude-code-2026-06-19-7f158e
date: '2026-06-19'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1257
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-12-added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al|claude-code-2026-06-12-f8c57e]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: e621c482299687d62dc018850d8f81e02c09502b3585e4a527c980c71a6aba2b
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-10-added-model-attribute-to-the-claude-code-lines-of-code-count-otel-metric|claude-code-2026-06-10-2a22f5]]'
- '[[Changes/ChatGPT/2026-06-12-as-of-june-12-2026-gpt-5-2-models-are-no-longer-available-in-chatgpt-this-applie|chatgpt-2026-06-12-a53a9d]]'
- '[[Changes/Claude Code/2026-06-12-added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al|claude-code-2026-06-12-f8c57e]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-19-v2-1-183-github-341696059-98586912|claude-code-2026-06-19-v2-1-183-github-341696059-98586912]]'
theme: model-support
type: change
---

# Added a warning when the requested model is deprecated or automatically updated

<!-- chronolog:begin region="description" -->
Added a warning when the requested model is deprecated or automatically updated to a newer model, shown on stderr in print mode (`-p`) and now also covering models set in agent frontmatter
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a warning when the requested model is deprecated or automatically updated to a newer model, shown on stderr in print mode (`-p`) and now also covering models set in agent frontmatter
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.183
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-12-added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al|claude-code-2026-06-12-f8c57e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1257
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes