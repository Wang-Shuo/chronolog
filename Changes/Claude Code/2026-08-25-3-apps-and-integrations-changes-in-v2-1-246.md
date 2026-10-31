---
card_id: claude-code-2026-08-25-c3e0f4
date: '2026-08-25'
description: 'Claude Code · 2026-08-25 · Apps and Integrations: 3 changes in v2.1.246
  — Improved `/cd`: the new directory''s project settings, hooks, `.mcp.json` servers…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9759fb65f61848c9c599d2027e0a25136fef0d2374e56a01ac6decfb667c7969
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-25-c3e0f4
  comparison: ''
  date: '2026-08-25'
  description: 'Claude Code — v2.1.246: 3 Apps and Integrations changes'
  evidence:
  - quote: 'Improved `/cd`: the new directory''s project settings, hooks, `.mcp.json`
      servers (behind the usual approval prompt), skills, and agents now take effect
      right after the move instead of on `--resume`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: Improved non-interactive sessions (`-p`, SDK, cloud sessions) to automatically
      continue a response cut off mid-stream by a server error, connection loss, or
      stall instead of ending with an error
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  - quote: 'Changed OpenTelemetry plugin events for plugins synced from claude.ai:
      `plugin_id_hash` now reflects the plugin''s real marketplace, and `enabled_via`
      is `admin-install` for admin-installed plugins'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-246
  source_release: claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.246
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-08-21-plugin-availability-depends-on-your-plan-region-and-workspace-settings-desktop-i|Plugin
  availability depends on your plan, region, and workspace settings]]'
- '[[Changes/ChatGPT/2026-08-21-find-more-useful-plugins-rankings-now-prioritize-plugins-people-keep-using-after|Find
  more useful plugins]]'
- '[[Changes/Claude Code/2026-08-21-2-apps-and-integrations-changes-in-v2-1-239|2
  Apps and Integrations changes in v2.1.239]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0|claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.246
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.246

**Claude Code** · 2026-08-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.246) · from [[Releases/Claude Code/claude-code-2026-08-25-v2-1-246-github-376644211-dd9805a0|v2.1.246]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved `/cd`: the new directory's project settings, hooks, `.mcp.json` servers (behind the usual approval prompt), skills, and agents now take effect right after the move instead of on `--resume`

> Improved non-interactive sessions (`-p`, SDK, cloud sessions) to automatically continue a response cut off mid-stream by a server error, connection loss, or stall instead of ending with an error

> Changed OpenTelemetry plugin events for plugins synced from claude.ai: `plugin_id_hash` now reflects the plugin's real marketplace, and `enabled_via` is `admin-install` for admin-installed plugins

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.246
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved subagent results]] · Agent Mode
- [[Changes/Claude Code/2026-08-25-improved-bash-tool-latency-on-bash-shells-by-replaying-snapshot-functions-withou|Improved Bash tool latency on bash shells by replaying snapshot functions without…]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety and Privacy changes in v2.1.246]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-25-windows-macos-fixed-headless-sessions-not-cleaning-up-stale-entries-in-claude-se|Windows/macOS: Fixed headless sessions not cleaning up stale entries…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-25-added-the-turn-s-completion-time-to-the-end-of-turn-duration-line-e-g-saut-ed-fo|Added the turn's completion time to the end-of-turn duration line…]] · Editor Experience
- [[Changes/Claude Code/2026-08-25-2-developer-workflow-changes-in-v2-1-246|2 Developer Workflow changes in v2.1.246]] · Developer Workflow
- [[Changes/Claude Code/2026-08-25-improved-attribution-of-usage-telemetry-to-your-organization-for-workload-identi|Improved attribution of usage telemetry to your organization for workload identity…]] · Account and Access
- [[Changes/Claude Code/2026-08-25-goal-changed-idle-sessions-to-start-at-most-three-check-ins-on-long-running-back|/goal: Changed idle sessions to start at most three check-ins on long-running…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-21 · Claude Code · [[Changes/Claude Code/2026-08-21-2-apps-and-integrations-changes-in-v2-1-239|2 Apps and Integrations changes in v2.1.239]]
- Later: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-2-apps-and-integrations-changes-in-v2-1-247|2 Apps and Integrations changes in v2.1.247]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-25-c3e0f4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-25-3-apps-and-integrations-changes-in-v2-1-246.md%0ACard%20ID%3A%20claude-code-2026-08-25-c3e0f4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.246%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->