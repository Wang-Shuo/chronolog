---
card_id: claude-code-2026-05-12-abb705
date: '2026-05-12'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1146
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|claude-code-2026-05-11-368eed]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: b7ca6594c4f466450724f3e4a81169d9dcaee3a1d675ca5b3d18cb1fce683022
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-11-added-claude-plugin-details-name-to-show-a-plugin-s-component-inventory-and-proj|claude-code-2026-05-11-05cc0b]]'
- '[[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|claude-code-2026-05-11-368eed]]'
- '[[Changes/Cursor/2026-05-11-get-started-by-installing-the-integration-in-the-cursor-dashboard-learn-more-in|cursor-2026-05-11-df0e2b]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-12-v2-1-140-github-321395205-971146de|claude-code-2026-05-12-v2-1-140-github-321395205-971146de]]'
theme: apps-integrations
type: change
---

# Plugins now warn when a default component folder (e.g. `commands/`) is silently

<!-- chronolog:begin region="description" -->
Plugins now warn when a default component folder (e.g. `commands/`) is silently ignored because `plugin.json` sets the matching key. Shown in `/doctor`, `claude plugin list`, and `/plugin`.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Plugins now warn when a default component folder (e.g. `commands/`) is silently ignored because `plugin.json` sets the matching key. Shown in `/doctor`, `claude plugin list`, and `/plugin`.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.140
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-11-added-goal-command-set-a-completion-condition-and-claude-keeps-working-across-tu|claude-code-2026-05-11-368eed]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1146
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes