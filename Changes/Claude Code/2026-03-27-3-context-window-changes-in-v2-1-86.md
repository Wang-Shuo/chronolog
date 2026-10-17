---
card_id: claude-code-2026-03-27-ec9161
date: '2026-03-27'
description: 'Claude Code · 2026-03-27 · Context Window: 3 changes in v2.1.86 — Reduced
  token overhead when mentioning files with `@` — raw string content no longer…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1058
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 006872c2fbbcc7d98494f8643e730d1f38e7190495603edc1e6abb8a40785496
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-27-ec9161
  comparison: ''
  date: '2026-03-27'
  description: 'Claude Code — v2.1.86: 3 Context Window changes'
  evidence:
  - quote: Reduced token overhead when mentioning files with `@` — raw string content
      no longer JSON-escaped
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
  - quote: Improved prompt cache hit rate for Bedrock, Vertex, and Foundry users by
      removing dynamic content from tool descriptions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
  - quote: Skill descriptions in the `/skills` listing are now capped at 250 characters
      to reduce context usage
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-context-window-changes-in-v2-1-86
  source_release: claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859
  source_type: github_releases
  theme: context-window
  title: 3 Context Window changes in v2.1.86
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|Large
  pastes are now handled as attachments]]'
- '[[Changes/Claude Code/2026-03-26-reduced-ui-stutter-when-compaction-triggers-on-large-sessions|Reduced
  UI stutter when compaction triggers on large sessions]]'
- '[[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context
  Window changes in v2.1.84]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
source_type: github_releases
theme: context-window
title: 3 Context Window changes in v2.1.86
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Context Window changes in v2.1.86

**Claude Code** · 2026-03-27 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.86) · from [[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|v2.1.86]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reduced token overhead when mentioning files with `@` — raw string content no longer JSON-escaped

> Improved prompt cache hit rate for Bedrock, Vertex, and Foundry users by removing dynamic content from tool descriptions

> Skill descriptions in the `/skills` listing are now capped at 250 characters to reduce context usage

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|Added X-Claude-Code-Session-Id header to API requests so proxies can aggregate…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-27-added-jj-and-sl-to-vcs-directory-exclusion-lists-so-grep-and-file-autocomplete-d|Added .jj and .sl to VCS directory exclusion lists so Grep and file autocomplete…]] · Editor Experience
- [[Changes/Claude Code/2026-03-27-memory-filenames-in-the-saved-n-memories-notice-now-highlight-on-hover-and-open|Memory filenames in the "Saved N memories" notice now highlight on hover and open on click]] · Memory and Personalization
- [[Changes/Claude Code/2026-03-27-auto-mode-now-shows-unavailable-for-your-plan-when-disabled-by-plan-restrictions|Auto mode now shows "unavailable for your plan" when disabled by plan restrictions…]] · Agent Mode
- [[Changes/Claude Code/2026-03-27-changed-skills-menu-to-sort-alphabetically-for-easier-scanning|Changed /skills menu to sort alphabetically for easier scanning]] · Interface Experience
- [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-27-read-tool-now-uses-compact-line-number-format-and-deduplicates-unchanged-re-read|Read tool now uses compact line-number format and deduplicates unchanged re-reads…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context Window changes in v2.1.84]]
- Later: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-changed-hook-output-over-50k-characters-to-be-saved-to-disk-with-a-file-path-pre|Changed hook output over 50K characters to be saved to disk with a file path…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-27-ec9161&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-27-3-context-window-changes-in-v2-1-86.md%0ACard%20ID%3A%20claude-code-2026-03-27-ec9161%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.86%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->