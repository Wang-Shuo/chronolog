---
card_id: claude-code-2026-04-14-9b9435
date: '2026-04-14'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1191
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|claude-code-2026-03-26-3c8e42]]'
extractor_version: fallback-v2
impact: significant
machine_hash: a00d549d4c3310f45349795eca412b8559f7d3a658fb82ed8a4109c3cd94280e
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|claude-code-2026-03-26-3c8e42]]'
- '[[Changes/ChatGPT/2026-04-09-pro-100-month-built-for-longer-high-intensity-codex-sessions-it-includes-unlimit|chatgpt-2026-04-09-384163]]'
- '[[Changes/ChatGPT/2026-04-09-today-we-re-releasing-gpt-5-3-instant-mini-in-chatgpt-it-replaces-gpt-5-instant|chatgpt-2026-04-09-dba9dd]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5]]'
theme: model-support
type: change
---

# Improved `/model` to warn before switching models mid-conversation, since the ne

<!-- chronolog:begin region="description" -->
Improved `/model` to warn before switching models mid-conversation, since the next response re-reads the full history uncached
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved `/model` to warn before switching models mid-conversation, since the next response re-reads the full history uncached
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|claude-code-2026-03-26-3c8e42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1191
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes