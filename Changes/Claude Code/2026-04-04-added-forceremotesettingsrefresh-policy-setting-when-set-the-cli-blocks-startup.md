---
card_id: claude-code-2026-04-04-a0bc10
date: '2026-04-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]'
  lag_days: 982
  role: follower
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v2
impact: incremental
machine_hash: 623dced4c27d9db4a2afd1b8cc1c332b57007d024771fb6f70d5f62f02bd359a
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-03-on-teams-and-enterprise-plans-admins-can-now-create-team-marketplaces-to-share-p|cursor-2026-03-03-ba695c]]'
- '[[Changes/ChatGPT/2026-03-17-we-ve-simplified-the-model-picker-to-make-it-easier-to-choose-the-right-level-of|chatgpt-2026-03-17-2fd325]]'
- '[[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|chatgpt-2026-03-18-64ffa1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5|claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5]]'
theme: enterprise-admin
type: change
---

# Added `forceRemoteSettingsRefresh` policy setting: when set, the CLI blocks star

<!-- chronolog:begin region="description" -->
Added `forceRemoteSettingsRefresh` policy setting: when set, the CLI blocks startup until remote managed settings are freshly fetched, and exits if the fetch fails (fail-closed)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `forceRemoteSettingsRefresh` policy setting: when set, the CLI blocks startup until remote managed settings are freshly fetched, and exits if the fetch fails (fail-closed)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.92
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No prior tracked change.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: enterprise-admin
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]
- Lag Days: 982
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes