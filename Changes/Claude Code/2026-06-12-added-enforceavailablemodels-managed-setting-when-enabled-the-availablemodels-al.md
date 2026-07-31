---
card_id: claude-code-2026-06-12-f8c57e
date: '2026-06-12'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1250
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-10-added-model-attribute-to-the-claude-code-lines-of-code-count-otel-metric|claude-code-2026-06-10-2a22f5]]'
extractor_version: fallback-v2
impact: significant
machine_hash: a0e63a9642e2c9dd5c6809e8675e41d66eb1bf02524453983b536392ff4e0a0b
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-06-10-pro-standard-pro-plans-only|chatgpt-2026-06-10-c9cf00]]'
- '[[Changes/Claude Code/2026-06-10-added-model-attribute-to-the-claude-code-lines-of-code-count-otel-metric|claude-code-2026-06-10-2a22f5]]'
- '[[Changes/ChatGPT/2026-06-12-as-of-june-12-2026-gpt-5-2-models-are-no-longer-available-in-chatgpt-this-applie|chatgpt-2026-06-12-a53a9d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-12-v2-1-175-github-338335820-6f3a7124|claude-code-2026-06-12-v2-1-175-github-338335820-6f3a7124]]'
theme: model-support
type: change
---

# Added `enforceAvailableModels` managed setting — when enabled, the `availableMod

<!-- chronolog:begin region="description" -->
Added `enforceAvailableModels` managed setting — when enabled, the `availableModels` allowlist also constrains the Default model (a Default that would resolve to a disallowed model now falls back to the first allowed model), and user or project settings can no longer widen a managed `availableModels` list
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `enforceAvailableModels` managed setting — when enabled, the `availableModels` allowlist also constrains the Default model (a Default that would resolve to a disallowed model now falls back to the first allowed model), and user or project settings can no longer widen a managed `availableModels` list
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.175
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-10-added-model-attribute-to-the-claude-code-lines-of-code-count-otel-metric|claude-code-2026-06-10-2a22f5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1250
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes