---
card_id: claude-code-2026-09-15-d69af3
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Context Window: Added `x-claude-code-request-class`,
  `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|Extended
    prompt length for project generation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1230
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 15730c2fbd89d19e112d972540d310dbfecd79d7eb6b7abbe05b04cd05c720bf
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
  extractor_version: fallback-v4
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
  title: Added `x-claude-code-request-class`, `x-claude-code-agent-type`…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-11-improved-compaction-progress-the-retry-countdown-and-stall-hint-now-appear-durin|Improved
  compaction progress]]'
- '[[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|Added
  /skill-doctor to show which loaded skills go unused and what they cost…]]'
- '[[Changes/Cursor/2026-09-10-today-we-re-launching-projects-in-cursor-projects-lets-you-take-on-larger-bodies|Cursor
  launches Projects]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: context-window
title: Added x-claude-code-request-class, x-claude-code-agent-type…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `x-claude-code-request-class`, `x-claude-code-agent-type`…

**Claude Code** · 2026-09-15 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `x-claude-code-request-class`, `x-claude-code-agent-type`, `x-claude-code-prev-tool-durations`, `x-claude-code-compaction` and `x-claude-code-context-compacted` request headers for LLM gateways; opt in with `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-fixed-read-on-macos-refusing-a-dragged-in-screenshot-or-any-file-the-system-repo|Fixed Read on macOS refusing a dragged-in screenshot, or any file the system reports…]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-15-added-forking-a-session-started-with-claude-remote-control-or-remote-control-fro|Added forking a session started with claude --remote-control or /remote-control…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-added-a-notification-when-an-mcp-server-disconnects-mid-session-and-automatic-re|Added a notification when an MCP server disconnects mid-session and automatic…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-fixed-bash-commands-the-permission-checker-cannot-fully-analyze-skipping-the-pro|Fixed Bash commands the permission checker cannot fully analyze skipping the prompt…]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-10 · Cursor · [[Changes/Cursor/2026-09-10-today-we-re-launching-projects-in-cursor-projects-lets-you-take-on-larger-bodies|Cursor launches Projects]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-added-autocompactwindow-to-subagent-frontmatter-and-agents-definitions-so-a-suba|Added autoCompactWindow to subagent frontmatter and --agents definitions…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|Extended prompt length for project generation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-d69af3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to.md%0ACard%20ID%3A%20claude-code-2026-09-15-d69af3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->