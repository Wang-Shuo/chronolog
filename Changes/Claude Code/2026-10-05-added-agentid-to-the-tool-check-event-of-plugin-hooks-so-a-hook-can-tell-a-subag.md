---
card_id: claude-code-2026-10-05-fd658b
date: '2026-10-05'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 021955a5441a0592b96687cd974741c64c342fa21aa9c65e7c9cf398bbeea1a8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-05-fd658b
  comparison: ''
  date: '2026-10-05'
  description: 'Claude Code — v2.1.290: Added `agentId` to the `tool.check` event
    of plugin hooks, so a hook can tell a subagent''s permission check from the main
    session''s'
  evidence:
  - quote: Added `agentId` to the `tool.check` event of plugin hooks, so a hook can
      tell a subagent's permission check from the main session's
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-agentid-to-the-tool-check-event-of-plugin-hooks-so-a-hook-can-tell-a-subag
  source_release: claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - subagent
    score: 50
    theme: agent-mode
  - matched_terms:
    - plugin
    score: 50
    theme: apps-integrations
  theme_resolution: manual-semantic-rule-v2
  title: Added `agentId` to the `tool.check` event of plugin hooks, so a hook can
    tell a
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity|chatgpt-2026-09-25-48984c]]'
- '[[Changes/ChatGPT/2026-09-25-to-view-your-history-in-chatgpt-on-the-web-go-to-settings-security-and-login-the|chatgpt-2026-09-25-5908d0]]'
- '[[Changes/Claude Code/2026-09-30-added-a-count-such-as-2-of-5-to-the-permission-prompt-when-several-permission-re|claude-code-2026-09-30-453980]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6|claude-code-2026-10-05-v2-1-290-github-403993621-ae06f2b6]]'
source_type: github_releases
theme: safety-privacy
title: Added agentId to the tool.check event of plugin hooks, so a hook can tell a
type: change
---

# Added `agentId` to the `tool.check` event of plugin hooks, so a hook can tell a

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.290: Added `agentId` to the `tool.check` event of plugin hooks, so a hook can tell a subagent's permission check from the main session's
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `agentId` to the `tool.check` event of plugin hooks, so a hook can tell a subagent's permission check from the main session's
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.290
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1268
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes