---
card_id: claude-code-2026-03-06-7eca43
date: '2026-03-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1079
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-03-05-added-optional-name-argument-to-remote-control-and-claude-remote-control-remote|claude-code-2026-03-05-be31df]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 58adad333c1870494f1e85f998c329dc8b9b77a0f1f0cefbfaa872483757f00d
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams|cursor-2026-03-03-08d82a]]'
- '[[Changes/Claude Code/2026-03-05-added-the-claude-api-skill-for-building-applications-with-the-claude-api-and-ant|claude-code-2026-03-05-4574a6]]'
- '[[Changes/Claude Code/2026-03-05-added-optional-name-argument-to-remote-control-and-claude-remote-control-remote|claude-code-2026-03-05-be31df]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-06-v2-1-70-github-293754953-afac13c0|claude-code-2026-03-06-v2-1-70-github-293754953-afac13c0]]'
theme: apps-integrations
type: change
---

# Reduced Remote Control `/poll` rate to once per 10 minutes while connected (was

<!-- chronolog:begin region="description" -->
Reduced Remote Control `/poll` rate to once per 10 minutes while connected (was 1–2s), cutting server load ~300×. Reconnection is unaffected — transport loss immediately wakes fast polling.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Reduced Remote Control `/poll` rate to once per 10 minutes while connected (was 1–2s), cutting server load ~300×. Reconnection is unaffected — transport loss immediately wakes fast polling.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.70
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-03-05-added-optional-name-argument-to-remote-control-and-claude-remote-control-remote|claude-code-2026-03-05-be31df]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1079
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes