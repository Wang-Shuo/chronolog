---
card_id: claude-code-2026-06-08-b5f6b1
date: '2026-06-08'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1246
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-06-max-thinking-tokens-0-thinking-disabled-and-the-per-model-thinking-toggle-now-di|claude-code-2026-06-06-d2e989]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 232cafe8483dc48eb8e491080069d810d860370991ec14778aacd8cd080ef2c5
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-06-added-fallbackmodel-setting-to-configure-up-to-three-fallback-models-tried-in-or|claude-code-2026-06-06-0d153f]]'
- '[[Changes/Claude Code/2026-06-06-claude-code-now-retries-a-turn-once-on-the-fallback-model-when-the-api-rejects-a|claude-code-2026-06-06-1aecaf]]'
- '[[Changes/Claude Code/2026-06-06-max-thinking-tokens-0-thinking-disabled-and-the-per-model-thinking-toggle-now-di|claude-code-2026-06-06-d2e989]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d|claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d]]'
theme: model-support
type: change
---

# Added a `disableBundledSkills` setting and `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS`

<!-- chronolog:begin region="description" -->
Added a `disableBundledSkills` setting and `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS` environment variable to hide bundled skills, workflows, and built-in slash commands from the model
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a `disableBundledSkills` setting and `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS` environment variable to hide bundled skills, workflows, and built-in slash commands from the model
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.169
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-06-max-thinking-tokens-0-thinking-disabled-and-the-per-model-thinking-toggle-now-di|claude-code-2026-06-06-d2e989]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1246
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes