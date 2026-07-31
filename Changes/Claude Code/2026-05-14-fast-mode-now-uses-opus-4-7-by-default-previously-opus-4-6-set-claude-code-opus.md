---
card_id: claude-code-2026-05-14-47ff02
date: '2026-05-14'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1221
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-06-gateway-v1-models-discovery-for-the-model-picker-is-now-opt-in-via-claude-code-e|claude-code-2026-05-06-5398e4]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: c9d63481506717d49e809d56245b95ae18482087484c1cab545c18ac38d7c04b
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-06-gateway-v1-models-discovery-for-the-model-picker-is-now-opt-in-via-claude-code-e|claude-code-2026-05-06-5398e4]]'
- '[[Changes/Cursor/2026-05-11-high-bugbot-spends-more-time-reasoning-reviews-are-more-expensive-and-take-longe|cursor-2026-05-11-5baefc]]'
- '[[Changes/Cursor/2026-05-11-custom-describe-in-natural-language-when-bugbot-should-use-default-or-high-effor|cursor-2026-05-11-7647fd]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-14-v2-1-142-github-322792825-ffda4d4f|claude-code-2026-05-14-v2-1-142-github-322792825-ffda4d4f]]'
theme: model-support
type: change
---

# Fast mode now uses Opus 4.7 by default (previously Opus 4.6). Set `CLAUDE_CODE_O

<!-- chronolog:begin region="description" -->
Fast mode now uses Opus 4.7 by default (previously Opus 4.6). Set `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` to pin fast mode to Opus 4.6
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fast mode now uses Opus 4.7 by default (previously Opus 4.6). Set `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` to pin fast mode to Opus 4.6
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.142
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-06-gateway-v1-models-discovery-for-the-model-picker-is-now-opt-in-via-claude-code-e|claude-code-2026-05-06-5398e4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1221
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes