---
card_id: claude-code-2026-06-06-1aecaf
date: '2026-06-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1244
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-06-added-fallbackmodel-setting-to-configure-up-to-three-fallback-models-tried-in-or|claude-code-2026-06-06-0d153f]]'
extractor_version: fallback-v2
impact: significant
machine_hash: ab5eed007c4f2b6d525beb2ba1d0808260633e474762b32b4532c1b160204aa8
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-30-auto-mode-is-now-available-on-bedrock-vertex-and-foundry-for-opus-4-7-and-opus-4|claude-code-2026-05-30-2e7a31]]'
- '[[Changes/Claude Code/2026-06-03-effort-now-confirms-when-your-chosen-level-will-persist-as-the-default-for-new-s|claude-code-2026-06-03-ef012f]]'
- '[[Changes/Claude Code/2026-06-06-added-fallbackmodel-setting-to-configure-up-to-three-fallback-models-tried-in-or|claude-code-2026-06-06-0d153f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-06-v2-1-166-github-335118845-ef990727|claude-code-2026-06-06-v2-1-166-github-335118845-ef990727]]'
theme: model-support
type: change
---

# Claude Code now retries a turn once on the fallback model when the API rejects a

<!-- chronolog:begin region="description" -->
Claude Code now retries a turn once on the fallback model when the API rejects an unexpected non-retryable error; auth, rate-limit, request-size, and transport errors still surface immediately
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Claude Code now retries a turn once on the fallback model when the API rejects an unexpected non-retryable error; auth, rate-limit, request-size, and transport errors still surface immediately
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.166
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-06-added-fallbackmodel-setting-to-configure-up-to-three-fallback-models-tried-in-or|claude-code-2026-06-06-0d153f]]
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