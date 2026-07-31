---
card_id: claude-code-2026-02-04-78de84
date: '2026-02-04'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1122
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-16-added-support-for-pretooluse-hooks-to-return-additionalcontext-to-the-model|claude-code-2026-01-16-7efdf0]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 24b1e624c58931cb6d7f55ea3206165d433c9febdd5fc232769d380004affa89
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-02-04-jan-10-2026-we-lowered-the-standard-and-light-thinking-time-as-we-observed-users|chatgpt-2026-02-04-24aba4]]'
- '[[Changes/ChatGPT/2026-02-04-february-4-2026-we-re-restoring-the-extended-thinking-level-for-gpt-5-2-thinking|chatgpt-2026-02-04-63f8b6]]'
- '[[Changes/ChatGPT/2026-02-04-february-3-2026-we-made-another-small-reduction-to-standard-thinking-time-based|chatgpt-2026-02-04-976d5d]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-04-v2-1-31-github-282782741-04ea99e1|claude-code-2026-02-04-v2-1-31-github-282782741-04ea99e1]]'
theme: model-support
type: change
---

# Improved system prompts to more clearly guide the model toward using dedicated t

<!-- chronolog:begin region="description" -->
Improved system prompts to more clearly guide the model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents (`cat`, `sed`, `grep`, `find`), reducing unnecessary bash command usage
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved system prompts to more clearly guide the model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents (`cat`, `sed`, `grep`, `find`), reducing unnecessary bash command usage
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.31
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-16-added-support-for-pretooluse-hooks-to-return-additionalcontext-to-the-model|claude-code-2026-01-16-7efdf0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1122
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes