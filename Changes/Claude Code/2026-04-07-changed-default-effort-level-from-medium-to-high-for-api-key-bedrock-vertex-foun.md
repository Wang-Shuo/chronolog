---
card_id: claude-code-2026-04-07-ff50d2
date: '2026-04-07'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]'
  lag_days: 985
  role: follower
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-04-added-forceremotesettingsrefresh-policy-setting-when-set-the-cli-blocks-startup|claude-code-2026-04-04-a0bc10]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5cdc3768812fd38c2f24ca29801a6c41ebefa3365434ba7a0af9c15c0f9f7a6c
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-03-17-we-ve-simplified-the-model-picker-to-make-it-easier-to-choose-the-right-level-of|chatgpt-2026-03-17-2fd325]]'
- '[[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|chatgpt-2026-03-18-64ffa1]]'
- '[[Changes/Claude Code/2026-04-04-added-forceremotesettingsrefresh-policy-setting-when-set-the-cli-blocks-startup|claude-code-2026-04-04-a0bc10]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-07-v2-1-94-github-306300914-5622fba4|claude-code-2026-04-07-v2-1-94-github-306300914-5622fba4]]'
theme: enterprise-admin
type: change
---

# Changed default effort level from medium to high for API-key, Bedrock/Vertex/Fou

<!-- chronolog:begin region="description" -->
Changed default effort level from medium to high for API-key, Bedrock/Vertex/Foundry, Team, and Enterprise users (control this with `/effort`)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed default effort level from medium to high for API-key, Bedrock/Vertex/Foundry, Team, and Enterprise users (control this with `/effort`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.94
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-04-added-forceremotesettingsrefresh-policy-setting-when-set-the-cli-blocks-startup|claude-code-2026-04-04-a0bc10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: enterprise-admin
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]
- Lag Days: 985
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes