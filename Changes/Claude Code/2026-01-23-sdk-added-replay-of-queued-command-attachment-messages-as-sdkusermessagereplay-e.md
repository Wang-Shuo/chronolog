---
card_id: claude-code-2026-01-23-d838c0
date: '2026-01-23'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1037
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-23-changed-skills-without-additional-permissions-or-hooks-to-be-allowed-without-req|claude-code-2026-01-23-869c23]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 4366c04ed2e707475106c2ef04816a08275fc332d9b124b913093c61baec3f21
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-20-added-search-to-installed-plugins-list-type-to-filter-by-name-or-description|claude-code-2026-01-20-5e8d97]]'
- '[[Changes/Claude Code/2026-01-22-vscode-added-native-plugin-management-support|claude-code-2026-01-22-3dded3]]'
- '[[Changes/Claude Code/2026-01-23-changed-skills-without-additional-permissions-or-hooks-to-be-allowed-without-req|claude-code-2026-01-23-869c23]]'
source_release: '[[Releases/Claude Code/claude-code-2026-01-23-v2-1-19-github-279515857-4e1f7640|claude-code-2026-01-23-v2-1-19-github-279515857-4e1f7640]]'
theme: apps-integrations
type: change
---

# [SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageRep

<!-- chronolog:begin region="description" -->
[SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageReplay` events when `replayUserMessages` is enabled
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageReplay` events when `replayUserMessages` is enabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.19
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-23-changed-skills-without-additional-permissions-or-hooks-to-be-allowed-without-req|claude-code-2026-01-23-869c23]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1037
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes