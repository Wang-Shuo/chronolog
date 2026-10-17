---
card_id: claude-code-2026-03-17-553440
date: '2026-03-17'
description: 'Claude Code · 2026-03-17 · Apps and Integrations: 3 changes in v2.1.78
  — Added `StopFailure` hook event that fires when the turn ends due to an API error
  (rate…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1090
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1b8d13948ea288e36180f5b0139e2cda87cc19dcdaf43f760e7d9284d629444e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-17-553440
  comparison: ''
  date: '2026-03-17'
  description: 'Claude Code — v2.1.78: 3 Apps and Integrations changes'
  evidence:
  - quote: Added `StopFailure` hook event that fires when the turn ends due to an
      API error (rate limit, auth failure, etc.)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
  - quote: Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that
      survives plugin updates; `/plugin uninstall` prompts before deleting it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
  - quote: Added `effort`, `maxTurns`, and `disallowedTools` frontmatter support for
      plugin-shipped agents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-78
  source_release: claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.78
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-11-we-ve-added-more-than-30-new-plugins-from-partners-such-as-atlassian-datadog-git-901313|New
  Plugins on the Cursor Marketplace]]'
- '[[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed
  --plugin-dir so local dev copies now override installed marketplace…]]'
- '[[Changes/Claude Code/2026-03-14-4-apps-and-integrations-changes-in-v2-1-76|4 Apps
  and Integrations changes in v2.1.76]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721|claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.78
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.78

**Claude Code** · 2026-03-17 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.78) · from [[Releases/Claude Code/claude-code-2026-03-17-v2-1-78-github-298204446-1f2c1721|v2.1.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `StopFailure` hook event that fires when the turn ends due to an API error (rate limit, auth failure, etc.)

> Added `${CLAUDE_PLUGIN_DATA}` variable for plugin persistent state that survives plugin updates; `/plugin uninstall` prompts before deleting it

> Added `effort`, `maxTurns`, and `disallowedTools` frontmatter support for plugin-shipped agents

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.78
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-17-2-safety-and-privacy-changes-in-v2-1-78|2 Safety and Privacy changes in v2.1.78]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-17-2-interface-experience-changes-in-v2-1-78|2 Interface Experience changes in v2.1.78]] · Interface Experience
- [[Changes/Claude Code/2026-03-17-improved-memory-usage-and-startup-time-when-resuming-large-sessions|Improved memory usage and startup time when resuming large sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-17-terminal-notifications-iterm2-kitty-ghostty-popups-progress-bar-now-reach-the-ou|Terminal notifications (iTerm2/Kitty/Ghostty popups, progress bar) now reach…]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-4-apps-and-integrations-changes-in-v2-1-76|4 Apps and Integrations changes in v2.1.76]]
- Later: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-2-apps-and-integrations-changes-in-v2-1-77|2 Apps and Integrations changes in v2.1.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-17-553440&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-17-3-apps-and-integrations-changes-in-v2-1-78.md%0ACard%20ID%3A%20claude-code-2026-03-17-553440%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.78%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->