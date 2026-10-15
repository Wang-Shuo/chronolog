---
card_id: claude-code-2026-10-14-592dcf
date: '2026-10-14'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 10398123f2bf492a1aed377b32f3f4b99cc3a82576b131269b17206b109480cf
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-10-14-592dcf
  comparison: ''
  confidence: low
  date: '2026-10-14'
  description: 'Claude Code — v2.1.299: Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`
    to change idle compaction''s 200K-token minimum; `"idleCompaction": false` in
    settings.json turns it off. Both need v2.1.290 or later'
  evidence:
  - quote: 'Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction''s
      200K-token minimum; `"idleCompaction": false` in settings.json turns it off.
      Both need v2.1.290 or later'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-claude-code-idle-compact-min-tokens-to-change-idle-compaction-s-200k-token
  source_release: claude-code-2026-10-14-v2-1-299-github-412217284-623d9162
  source_type: github_releases
  theme: context-window
  title: Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction's 200K-token
    minimum
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|claude-code-2026-09-15-d69af3]]'
- '[[Changes/Claude Code/2026-10-09-added-autocompactwindow-to-subagent-frontmatter-and-agents-definitions-so-a-suba|claude-code-2026-10-09-bc35b4]]'
- '[[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|claude-code-2026-10-14-0e9e30]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|claude-code-2026-10-14-v2-1-299-github-412217284-623d9162]]'
source_type: github_releases
theme: context-window
title: Added CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS to change idle compaction's 200K-token
  minimum
type: change
---

# Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction's 200K-token minimum

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.299: Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction's 200K-token minimum; `"idleCompaction": false` in settings.json turns it off. Both need v2.1.290 or later
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` to change idle compaction's 200K-token minimum; `"idleCompaction": false` in settings.json turns it off. Both need v2.1.290 or later
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1259
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes