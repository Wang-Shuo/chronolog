---
card_id: claude-code-2026-04-02-dbcea0
date: '2026-04-02'
description: 'Claude Code · 2026-04-02 · Apps and Integrations: 4 changes in v2.1.91
  — Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeChars"]`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1106
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c78a4a9056576435ea4e4b278c97b0b6ca1614cd939a52c8e96e421b88cc9f52
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-02-dbcea0
  comparison: ''
  date: '2026-04-02'
  description: 'Claude Code — v2.1.91: 4 Apps and Integrations changes'
  evidence:
  - quote: Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeChars"]`
      annotation (up to 500K), allowing larger results like DB schemas to pass through
      without truncation
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
  - quote: Added `disableSkillShellExecution` setting to disable inline shell execution
      in skills, custom slash commands, and plugin commands
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
  - quote: Added support for multi-line prompts in `claude-cli://open?q=` deep links
      (encoded newlines `%0A` no longer rejected)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
  - quote: Plugins can now ship executables under `bin/` and invoke them as bare commands
      from the Bash tool
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-91
  source_release: claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.91
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced
  startup event-loop stalls when many claude.ai MCP connectors are configured…]]'
- '[[Changes/Claude Code/2026-04-01-3-apps-and-integrations-changes-in-v2-1-89|3 Apps
  and Integrations changes in v2.1.89]]'
- '[[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps
  and Integrations changes in v2.1.90]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc|claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.91
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.91

**Claude Code** · 2026-04-02 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.91) · from [[Releases/Claude Code/claude-code-2026-04-02-v2-1-91-github-304899951-a56266fc|v2.1.91]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeChars"]` annotation (up to 500K), allowing larger results like DB schemas to pass through without truncation

> Added `disableSkillShellExecution` setting to disable inline shell execution in skills, custom slash commands, and plugin commands

> Added support for multi-line prompts in `claude-cli://open?q=` deep links (encoded newlines `%0A` no longer rejected)

> Plugins can now ship executables under `bin/` and invoke them as bare commands from the Bash tool

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.91
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-02-improved-performance-faster-stripansi-on-bun-by-routing-through-bun-stripansi|Improved performance: faster stripAnsi on Bun by routing through Bun.stripANSI]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-02-2-context-window-changes-in-v2-1-91|2 Context Window changes in v2.1.91]] · Context Window
- [[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|Fixed plan mode in remote sessions losing track of the plan file after a container…]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-02-feedback-now-explains-why-it-s-unavailable-instead-of-disappearing-from-the-slas|/feedback now explains why it's unavailable instead of disappearing from the slash menu]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps and Integrations changes in v2.1.90]]
- Later: 2026-04-02 · Cursor · [[Changes/Cursor/2026-04-02-2-apps-and-integrations-changes-in-3-0|2 Apps and Integrations changes in 3.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-02-dbcea0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-02-4-apps-and-integrations-changes-in-v2-1-91.md%0ACard%20ID%3A%20claude-code-2026-04-02-dbcea0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.91%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->