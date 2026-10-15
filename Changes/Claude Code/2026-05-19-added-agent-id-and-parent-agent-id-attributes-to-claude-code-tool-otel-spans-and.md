---
card_id: claude-code-2026-05-19-78d620
date: '2026-05-19'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1048
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 6f5fc9c6794dcb1870bebe4c02675e0187a5870969f87efaf2fd36978f0f08e4
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-05-19-78d620
  comparison: ''
  confidence: low
  date: '2026-05-19'
  description: 'Claude Code — v2.1.145: Added `agent_id` and `parent_agent_id` attributes
    to `claude_code.tool` OTEL spans, and fixed trace parenting so background subagent
    spans nest under the dispatching Agent tool span'
  evidence:
  - quote: Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool`
      OTEL spans, and fixed trace parenting so background subagent spans nest under
      the dispatching Agent tool span
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-agent-id-and-parent-agent-id-attributes-to-claude-code-tool-otel-spans-and
  source_release: claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4
  source_type: github_releases
  theme: agent-mode
  title: Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL
    spans…
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-18-composer-2-5-is-now-available-in-cursor|cursor-2026-05-18-3afa8e]]'
- '[[Changes/Claude Code/2026-05-19-added-resume-support-for-background-sessions-sessions-started-via-claude-bg-or-a|claude-code-2026-05-19-215520]]'
- '[[Changes/Claude Code/2026-05-19-claude-agents-terminal-tab-title-now-shows-the-awaiting-input-count-so-an-alt-ta|claude-code-2026-05-19-2f1483]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4|claude-code-2026-05-19-v2-1-145-github-325388499-227a5ce4]]'
source_type: github_releases
theme: agent-mode
title: Added agent_id and parent_agent_id attributes to claude_code.tool OTEL spans…
type: change
---

# Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spans…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.145: Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spans, and fixed trace parenting so background subagent spans nest under the dispatching Agent tool span
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spans, and fixed trace parenting so background subagent spans nest under the dispatching Agent tool span
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.145
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: agent-mode
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|cursor-2023-07-06-d7057e]]
- Lag Days: 1048
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes