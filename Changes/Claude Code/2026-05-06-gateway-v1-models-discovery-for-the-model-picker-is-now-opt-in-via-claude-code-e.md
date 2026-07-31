---
card_id: claude-code-2026-05-06-5398e4
date: '2026-05-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1213
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-04-updated-model-picker-collapsed-duplicate-opus-4-7-entries-and-current-opus-now-s|claude-code-2026-05-04-cbf221]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 53147ceff082e2c46541a9f7b4eee6f299054e13ece2edc0abade7e82382731c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-05-04-enterprises-also-have-the-option-to-block-new-providers-or-model-versions-by-def|cursor-2026-05-04-793636]]'
- '[[Changes/Cursor/2026-05-04-model-access-controls|cursor-2026-05-04-babd3e]]'
- '[[Changes/ChatGPT/2026-05-05-we-re-rolling-out-gpt-5-5-instant-as-chatgpt-s-new-default-model-it-replaces-gpt|chatgpt-2026-05-05-224f9a]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f|claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f]]'
theme: model-support
type: change
---

# Gateway `/v1/models` discovery for the `/model` picker is now opt-in via `CLAUDE

<!-- chronolog:begin region="description" -->
Gateway `/v1/models` discovery for the `/model` picker is now opt-in via `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` (was automatic in 2.1.126–2.1.128)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Gateway `/v1/models` discovery for the `/model` picker is now opt-in via `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` (was automatic in 2.1.126–2.1.128)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-04-updated-model-picker-collapsed-duplicate-opus-4-7-entries-and-current-opus-now-s|claude-code-2026-05-04-cbf221]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1213
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes