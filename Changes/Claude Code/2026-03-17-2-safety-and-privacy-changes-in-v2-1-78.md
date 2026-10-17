---
card_id: claude-code-2026-03-17-1a03a1
date: '2026-03-17'
description: 'Claude Code · 2026-03-17 · Safety and Privacy: 2 changes in v2.1.78
  — Fixed `deny: ["mcp__servername"]` permission rules not removing MCP server tools
  before…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1066
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a52a569fd538efcd9f76adaf0ee6d519314048aac389bd4a6523cdac5ae76756
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-17-1a03a1
  comparison: ''
  date: '2026-03-17'
  description: 'Claude Code — v2.1.78: 2 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed `deny: ["mcp__servername"]` permission rules not removing MCP server
      tools before sending to the model, allowing it to see and attempt blocked tools'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
  - quote: '**Security:** Fixed silent sandbox disable when `sandbox.enabled: true`
      is set but dependencies are missing — now shows a visible startup warning'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-78
  source_release: claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.78
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed
  freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]'
- '[[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|Fixed
  voice mode silently failing on the macOS native binary for users whose…]]'
- '[[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety
  and Privacy changes in v2.1.76]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721|claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.78
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.78

**Claude Code** · 2026-03-17 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.78) · from [[Releases/Claude Code/claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721|v2.1.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed `deny: ["mcp__servername"]` permission rules not removing MCP server tools before sending to the model, allowing it to see and attempt blocked tools

> **Security:** Fixed silent sandbox disable when `sandbox.enabled: true` is set but dependencies are missing — now shows a visible startup warning

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-17-3-apps-and-integrations-changes-in-v2-1-78|3 Apps and Integrations changes in v2.1.78]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-17-2-interface-experience-changes-in-v2-1-78|2 Interface Experience changes in v2.1.78]] · Interface Experience
- [[Changes/Claude Code/2026-03-17-improved-memory-usage-and-startup-time-when-resuming-large-sessions|Improved memory usage and startup time when resuming large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]]
- Later: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety and Privacy changes in v2.1.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-17-1a03a1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-17-2-safety-and-privacy-changes-in-v2-1-78.md%0ACard%20ID%3A%20claude-code-2026-03-17-1a03a1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.78%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->