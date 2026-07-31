---
card_id: claude-code-2026-04-02-a9c889
date: '2026-04-02'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1106
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-01-added-claude-code-plugin-keep-marketplace-on-failure-env-var-to-keep-the-existin|claude-code-2026-04-01-5bb86f]]'
extractor_version: fallback-v2
impact: significant
machine_hash: f015997814d4b885a4b93a08fb37d0207557eaf7a01bcbb60b8992eb788a0666
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|claude-code-2026-03-27-dcb91e]]'
- '[[Changes/Claude Code/2026-04-01-added-mcp-connection-nonblocking-true-for-p-mode-to-skip-the-mcp-connection-wait|claude-code-2026-04-01-210067]]'
- '[[Changes/Claude Code/2026-04-01-added-claude-code-plugin-keep-marketplace-on-failure-env-var-to-keep-the-existin|claude-code-2026-04-01-5bb86f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc|claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc]]'
theme: apps-integrations
type: change
---

# Added support for multi-line prompts in `claude-cli://open?q=` deep links (encod

<!-- chronolog:begin region="description" -->
Added support for multi-line prompts in `claude-cli://open?q=` deep links (encoded newlines `%0A` no longer rejected)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added support for multi-line prompts in `claude-cli://open?q=` deep links (encoded newlines `%0A` no longer rejected)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-01-added-claude-code-plugin-keep-marketplace-on-failure-env-var-to-keep-the-existin|claude-code-2026-04-01-5bb86f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1106
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes