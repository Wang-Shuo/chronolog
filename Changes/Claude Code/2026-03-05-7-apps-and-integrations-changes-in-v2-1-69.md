---
card_id: claude-code-2026-03-05-9054a2
date: '2026-03-05'
description: 'Claude Code · 2026-03-05 · Apps and Integrations: 7 changes in v2.1.69
  — Added the `/claude-api` skill for building applications with the Claude API and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1078
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7e81f40c84d03894dca6c9b7838467bf391d307d452153fae98725edb602c83e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-05-9054a2
  comparison: ''
  date: '2026-03-05'
  description: 'Claude Code — v2.1.69: 7 Apps and Integrations changes'
  evidence:
  - quote: Added the `/claude-api` skill for building applications with the Claude
      API and Anthropic SDK
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Added optional name argument to `/remote-control` and `claude remote-control`
      (`/remote-control My Project` or `--name "My Project"`) to set a custom session
      title visible in claude.ai/code
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Added `pluginTrustMessage` in managed settings to append organization-specific
      context to the plugin trust warning shown before installation
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Added plugin source type `git-subdir` to point to a subdirectory within
      a git repo
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Improved MCP `-p` startup by pipelining claude.ai config fetch with local
      connections and using a concurrency pool instead of sequential batching
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: Changed claude.ai MCP connector failures to show a notification instead
      of silently disappearing from the tool list
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  - quote: '[SDK] Changed task creation to no longer require the `activeForm` field
      — the spinner falls back to the task subject'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-apps-and-integrations-changes-in-v2-1-69
  source_release: claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v2.1.69
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-03-3-apps-and-integrations-changes-in-2-6|3 Apps and Integrations
  changes in 2.6]]'
- '[[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams|MCP
  Apps]]'
- '[[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added
  /reload-plugins command to activate pending plugin changes without restarting]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44|claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v2.1.69
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v2.1.69

**Claude Code** · 2026-03-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.69) · from [[Releases/Claude Code/claude-code-2026-03-05-v2-1-69-github-293216328-162b2e44|v2.1.69]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added the `/claude-api` skill for building applications with the Claude API and Anthropic SDK

> Added optional name argument to `/remote-control` and `claude remote-control` (`/remote-control My Project` or `--name "My Project"`) to set a custom session title visible in claude.ai/code

> Added `pluginTrustMessage` in managed settings to append organization-specific context to the plugin trust warning shown before installation

> Added plugin source type `git-subdir` to point to a subdirectory within a git repo

> Improved MCP `-p` startup by pipelining claude.ai config fetch with local connections and using a concurrency pool instead of sequential batching

> Changed claude.ai MCP connector failures to show a notification instead of silently disappearing from the tool list

> [SDK] Changed task creation to no longer require the `activeForm` field — the spinner falls back to the task subject

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.69
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-05-2-agent-mode-changes-in-v2-1-69|2 Agent Mode changes in v2.1.69]] · Agent Mode
- [[Changes/Claude Code/2026-03-05-changed-sonnet-4-5-users-on-pro-max-team-premium-to-be-automatically-migrated-to|Changed Sonnet 4.5 users on Pro/Max/Team Premium to be automatically migrated…]] · Model Support
- [[Changes/Claude Code/2026-03-05-9-reliability-and-performance-changes-in-v2-1-69|9 Reliability and Performance changes in v2.1.69]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-05-added-reload-plugins-command-to-activate-pending-plugin-changes-without-restarti|Added /reload-plugins command to activate pending plugin changes without restarting]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-05-3-interface-experience-changes-in-v2-1-69|3 Interface Experience changes in v2.1.69]] · Interface Experience
- [[Changes/Claude Code/2026-03-05-improved-macos-startup-for-claude-ai-enterprise-team-users-by-skipping-an-unnece|Improved macOS startup for Claude.ai enterprise/team users by skipping…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-05-3-voice-and-audio-changes-in-v2-1-69|3 Voice and Audio changes in v2.1.69]] · Voice and Audio
- [[Changes/Claude Code/2026-03-05-5-safety-and-privacy-changes-in-v2-1-69|5 Safety and Privacy changes in v2.1.69]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-05-2-mobile-and-desktop-changes-in-v2-1-69|2 Mobile and Desktop changes in v2.1.69]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-05-6-developer-workflow-changes-in-v2-1-69|6 Developer Workflow changes in v2.1.69]] · Developer Workflow
- [[Changes/Claude Code/2026-03-05-2-account-and-access-changes-in-v2-1-69|2 Account and Access changes in v2.1.69]] · Account and Access
- [[Changes/Claude Code/2026-03-05-3-context-window-changes-in-v2-1-69|3 Context Window changes in v2.1.69]] · Context Window
- [[Changes/Claude Code/2026-03-05-3-other-changes-in-v2-1-69|3 other changes in v2.1.69]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-03 · Cursor · [[Changes/Cursor/2026-03-03-mcp-apps-support-interactive-user-interfaces-like-charts-from-amplitude-diagrams|MCP Apps]]
- Later: 2026-03-06 · Claude Code · [[Changes/Claude Code/2026-03-06-reduced-remote-control-poll-rate-to-once-per-10-minutes-while-connected-was-1-2s|Reduced Remote Control /poll rate to once per 10 minutes while connected…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-05-9054a2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-05-7-apps-and-integrations-changes-in-v2-1-69.md%0ACard%20ID%3A%20claude-code-2026-03-05-9054a2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.69%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->