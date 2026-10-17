---
card_id: claude-code-2026-03-26-3ab0fb
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Safety and Privacy: 2 changes in v2.1.85
  — Added conditional `if` field for hooks using permission rule syntax (e.g., `Bash(git
  *)`)…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1075
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cb3e893b02feb817ab98e67becfc457571c213b1d4cb3bb750cf828104f99006
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-26-3ab0fb
  comparison: ''
  date: '2026-03-26'
  description: 'Claude Code — v2.1.85: 2 Safety and Privacy changes'
  evidence:
  - quote: Added conditional `if` field for hooks using permission rule syntax (e.g.,
      `Bash(git *)`) to filter when they run, reducing process spawning overhead
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
  - quote: Fixed Remote Control session status staying stuck on "Requires Action"
      after a permission is resolved
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-85
  source_release: claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.85
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety
  and Privacy changes in v2.1.81]]'
- '[[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety
  and Privacy changes in v2.1.83]]'
- '[[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed
  the "allow Claude to edit its own settings for this session" permission option…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7|claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.85
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.85

**Claude Code** · 2026-03-26 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.85) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-85-github-302129484-6eb9dcd7|v2.1.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added conditional `if` field for hooks using permission rule syntax (e.g., `Bash(git *)`) to filter when they run, reducing process spawning overhead

> Fixed Remote Control session status staying stuck on "Requires Action" after a permission is resolved

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-mcp-oauth-now-follows-rfc-9728-protected-resource-metadata-discovery-to-find-the|MCP OAuth now follows RFC 9728 Protected Resource Metadata discovery to find…]] · Account and Access
- [[Changes/Claude Code/2026-03-26-improved-scroll-performance-with-large-transcripts-by-replacing-wasm-yoga-layout|Improved scroll performance with large transcripts by replacing WASM yoga-layout…]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-26-added-timestamp-markers-in-transcripts-when-scheduled-tasks-loop-croncreate-fire|Added timestamp markers in transcripts when scheduled tasks (/loop, CronCreate) fire]] · Automation and Scheduling
- [[Changes/Claude Code/2026-03-26-improved-mention-file-autocomplete-performance-on-large-repositories|Improved @-mention file autocomplete performance on large repositories]] · Interface Experience
- [[Changes/Claude Code/2026-03-26-reduced-ui-stutter-when-compaction-triggers-on-large-sessions|Reduced UI stutter when compaction triggers on large sessions]] · Context Window
- [[Changes/Claude Code/2026-03-26-4-apps-and-integrations-changes-in-v2-1-85|4 Apps and Integrations changes in v2.1.85]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-26-improved-powershell-dangerous-command-detection|Improved PowerShell dangerous command detection]] · Developer Workflow
- [[Changes/Claude Code/2026-03-26-tool-parameters-in-opentelemetry-tool-result-events-are-now-gated-behind-otel-lo|tool_parameters in OpenTelemetry tool_result events are now gated behind…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]]
- Later: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-3ab0fb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-2-safety-and-privacy-changes-in-v2-1-85.md%0ACard%20ID%3A%20claude-code-2026-03-26-3ab0fb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->