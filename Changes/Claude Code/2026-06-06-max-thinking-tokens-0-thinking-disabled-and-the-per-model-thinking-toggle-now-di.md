---
card_id: claude-code-2026-06-06-d2e989
date: '2026-06-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1244
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-06-claude-code-now-retries-a-turn-once-on-the-fallback-model-when-the-api-rejects-a|claude-code-2026-06-06-1aecaf]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 679219bb79118d7bcdd4dd0b5ecc01f333f7cfc5d4398287f521648e17400f87
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-03-effort-now-confirms-when-your-chosen-level-will-persist-as-the-default-for-new-s|claude-code-2026-06-03-ef012f]]'
- '[[Changes/Claude Code/2026-06-06-added-fallbackmodel-setting-to-configure-up-to-three-fallback-models-tried-in-or|claude-code-2026-06-06-0d153f]]'
- '[[Changes/Claude Code/2026-06-06-claude-code-now-retries-a-turn-once-on-the-fallback-model-when-the-api-rejects-a|claude-code-2026-06-06-1aecaf]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|claude-code-2026-06-06-v2-1-166-github-335118845-ef990727]]'
theme: model-support
type: change
---

# `MAX_THINKING_TOKENS=0`, `--thinking disabled`, and the per-model thinking toggl

<!-- chronolog:begin region="description" -->
`MAX_THINKING_TOKENS=0`, `--thinking disabled`, and the per-model thinking toggle now disable thinking on models that think by default via the Claude API (3P providers unchanged)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `MAX_THINKING_TOKENS=0`, `--thinking disabled`, and the per-model thinking toggle now disable thinking on models that think by default via the Claude API (3P providers unchanged)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-06-claude-code-now-retries-a-turn-once-on-the-fallback-model-when-the-api-rejects-a|claude-code-2026-06-06-1aecaf]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1244
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes