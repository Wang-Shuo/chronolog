---
card_id: cursor-2026-02-17-05c80f
date: '2026-02-17'
description: 'Cursor · 2026-02-17 · Agent Mode: Previously, all subagents ran synchronously,
  blocking the parent agent until they complete. Subagents can now run…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 957
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 2b56b0eefc8fe33bdb0930619ef3cd366eb5d035e28bd0261497b4482eaec5dd
product: cursor
product_name: Cursor
record:
  ai_generated: true
  card_id: cursor-2026-02-17-05c80f
  comparison: ''
  confidence: low
  date: '2026-02-17'
  description: 'Cursor — Plugins, Sandbox Access Controls, and Async Subagents: Previously,
    all subagents ran synchronously, blocking the parent agent until they complete.
    Subagents can now run asynchronously, allowing the parent to continue working
    while subagents run in the background.'
  evidence:
  - quote: Previously, all subagents ran synchronously, blocking the parent agent
      until they complete. Subagents can now run asynchronously, allowing the parent
      to continue working while subagents run in the background.
    source_release: https://cursor.com/changelog/2-5
  - quote: Subagents can also spawn their own subagents, creating a tree of coordinated
      work. This allows Cursor to take on bigger tasks like multi-file features, large
      refactors, and challenging bugs.
    source_release: https://cursor.com/changelog/2-5
  - quote: We've also made some performance improvements to subagents since our last
      release. They now run with lower latency, better streaming feedback, and more
      responsive parallel execution.
    source_release: https://cursor.com/changelog/2-5
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: cursor
  product_name: Cursor
  slug: async-subagents
  source_release: cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320
  source_type: cursor_changelog
  theme: agent-mode
  title: Async subagents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-05-updated-resume-to-re-use-agent-value-specified-in-previous-conversation-by-defau|Updated
  --resume to re-use --agent value specified in previous conversation by default]]'
- '[[Changes/Claude Code/2026-02-06-2-agent-mode-changes-in-v2-1-33|2 Agent Mode changes
  in v2.1.33]]'
- '[[Changes/Cursor/2026-02-12-cursor-can-now-work-autonomously-over-longer-horizons-to-complete-larger-more-co-48843c|Long-running
  Agents in Research Preview]]'
source_release: '[[Releases/Cursor/cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320|cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320]]'
source_type: cursor_changelog
theme: agent-mode
title: Async subagents
type: change
---

<!-- chronolog:begin region="header" -->
# Async subagents

**Cursor** · 2026-02-17 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://cursor.com/changelog/2-5) · from [[Releases/Cursor/cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320|Plugins, Sandbox Access Controls, and Async Subagents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Previously, all subagents ran synchronously, blocking the parent agent until they complete. Subagents can now run asynchronously, allowing the parent to continue working while subagents run in the background.
>
> Subagents can also spawn their own subagents, creating a tree of coordinated work. This allows Cursor to take on bigger tasks like multi-file features, large refactors, and challenging bugs.
>
> We've also made some performance improvements to subagents since our last release. They now run with lower latency, better streaming feedback, and more responsive parallel execution.
>
> Source: https://cursor.com/changelog/2-5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-02-17-plugins-on-the-cursor-marketplace-0cef65|Plugins on the Cursor Marketplace]] · Apps and Integrations
- [[Changes/Cursor/2026-02-17-manual-edits-no-longer-create-in-line-diffs|Manual edits no longer create in-line diffs]] · Editor Experience
- [[Changes/Cursor/2026-02-17-sandbox-network-access-controls|Sandbox network access controls]] · Safety and Privacy
- [[Changes/Cursor/2026-02-17-removed-auto-accept-on-commit-setting-so-pending-diffs-are-automatically-accepte|Removed Auto-Accept on Commit setting so pending diffs are automatically accepted…]] · Developer Workflow
- [[Changes/Cursor/2026-02-17-3-interface-experience-changes-in-2-5|3 Interface Experience changes in 2.5]] · Interface Experience
- [[Changes/Cursor/2026-02-17-agents-can-now-search-past-conversations-and-use-chat-history-as-context|Agents can now search past conversations and use chat history as context]] · Context Window
- [[Changes/Cursor/2026-02-17-3-safety-and-privacy-changes-in-2-5|3 Safety and Privacy changes in 2.5]] · Safety and Privacy
- [[Changes/Cursor/2026-02-17-6-agent-mode-changes-in-2-5|6 Agent Mode changes in 2.5]] · Agent Mode
- [[Changes/Cursor/2026-02-17-this-release-introduces-plugins-for-extending-cursor-improvements-to-core-agent|Cursor introduces plugins for extending Cursor, improvements to core agent…]] · Agent Mode
- [[Changes/Cursor/2026-02-17-2-reliability-and-performance-changes-in-2-5|2 Reliability and Performance changes in 2.5]] · Reliability and Performance
- [[Changes/Cursor/2026-02-17-the-global-ignore-list-is-now-empty-by-default-to-fix-sandboxing-issues-existing|The global ignore list is now empty by default to fix sandboxing issues]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-12 · Cursor · [[Changes/Cursor/2026-02-12-cursor-can-now-work-autonomously-over-longer-horizons-to-complete-larger-more-co-48843c|Long-running Agents in Research Preview]]
- Later: 2026-02-18 · Claude Code · [[Changes/Claude Code/2026-02-18-2-agent-mode-changes-in-v2-1-47|2 Agent Mode changes in v2.1.47]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-02-17-05c80f&body=Card%3A%20Changes%2FCursor%2F2026-02-17-async-subagents.md%0ACard%20ID%3A%20cursor-2026-02-17-05c80f%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2F2-5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->