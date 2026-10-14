---
card_id: claude-code-2026-09-15-d69af3
date: '2026-09-15'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1230
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: paradigm-shift
machine_hash: f8d8a6b7586bcae8e63b038665e7fae821d416454730c1998c230966b545864e
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-09-15-d69af3
  comparison: ''
  confidence: low
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: Added `x-claude-code-request-class`, `x-claude-code-agent-type`,
    `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted`
    request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`'
  evidence:
  - quote: Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`,
      `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers
      for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v3
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - context
    score: 50
    theme: context-window
  - matched_terms:
    - llm
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-11-improved-compaction-progress-the-retry-countdown-and-stall-hint-now-appear-durin|claude-code-2026-08-11-cbd6f1]]'
- '[[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|claude-code-2026-09-04-b7c741]]'
- '[[Changes/Cursor/2026-09-10-today-we-re-launching-projects-in-cursor-projects-lets-you-take-on-larger-bodies|cursor-2026-09-10-bf27c0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: context-window
title: Added x-claude-code-request-class, x-claude-code-agent-type, x-claude-code-
type: change
---

# Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.273: Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
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
- Lag Days: 1230
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes