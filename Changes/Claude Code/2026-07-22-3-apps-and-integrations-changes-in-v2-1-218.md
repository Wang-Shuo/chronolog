---
card_id: claude-code-2026-07-22-7ebd31
date: '2026-07-22'
description: 'Claude Code · 2026-07-22 · Apps and Integrations: 3 changes in v2.1.218
  — Added HTTP status and error text to `claude mcp list` and `/mcp` when a server
  fails…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1217
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b159791b7121b6a1885a59ee856fce69e4374a14c0f974afa40041da84f1cf6a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-22-7ebd31
  comparison: ''
  date: '2026-07-22'
  description: 'Claude Code — v2.1.218: 3 Apps and Integrations changes'
  evidence:
  - quote: Added HTTP status and error text to `claude mcp list` and `/mcp` when a
      server fails to connect, and a warning for MCP config values with hidden leading
      or trailing whitespace
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
  - quote: Changed agent markdown files to reject agent names containing `:`, which
      is reserved for plugin namespacing
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
  - quote: Added `yes`/`no`/`on`/`off`/`1`/`0` (case-insensitive) as accepted values
      for skill and plugin frontmatter booleans, alongside `true`/`false`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-218
  source_release: claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.218
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-18-changed-sessionstart-hooks-to-report-source-fork-when-a-session-begins-as-a-fork|Changed
  SessionStart hooks to report source "fork" when a session begins as a fork…]]'
- '[[Changes/Claude Code/2026-07-20-background-sessions-mcp-and-install-github-app-now-park-a-needs-input-request-in|Background
  sessions: /mcp and /install-github-app now park…]]'
- '[[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped
  the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.218
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.218

**Claude Code** · 2026-07-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.218) · from [[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|v2.1.218]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added HTTP status and error text to `claude mcp list` and `/mcp` when a server fails to connect, and a warning for MCP config values with hidden leading or trailing whitespace

> Changed agent markdown files to reject agent names containing `:`, which is reserved for plugin namespacing

> Added `yes`/`no`/`on`/`off`/`1`/`0` (case-insensitive) as accepted values for skill and plugin frontmatter booleans, alongside `true`/`false`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-22-changed-plan-mode-with-auto-to-no-longer-prompt-for-bash-commands-the-static-ana|Changed plan mode with auto to no longer prompt for Bash commands the static…]] · Agent Mode
- [[Changes/Claude Code/2026-07-22-changed-server-managed-settings-so-benign-feature-and-cost-toggles-no-longer-tri|Changed server-managed settings so benign feature and cost toggles no longer trigger…]] · Pricing Model
- [[Changes/Claude Code/2026-07-22-3-safety-and-privacy-changes-in-v2-1-218|3 Safety and Privacy changes in v2.1.218]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-22-added-an-announcement-when-fast-mode-changes-as-a-result-of-switching-models-via|Added an announcement when fast mode changes as a result of switching models…]] · Model Support
- [[Changes/Claude Code/2026-07-22-changed-deep-research-to-start-only-when-invoked-manually-claude-no-longer-launc|Changed /deep-research to start only when invoked manually]] · Search and Browsing
- [[Changes/Claude Code/2026-07-22-added-screen-reader-announcements-of-deleted-text-for-word-and-line-deletions-op|Added screen-reader announcements of deleted text for word and line deletions…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-07-22-changed-code-review-to-run-as-a-background-subagent-so-review-work-no-longer-fil|Changed /code-review to run as a background subagent, so review work no longer…]] · Developer Workflow
- [[Changes/Claude Code/2026-07-22-changed-skills-with-context-fork-to-run-in-the-background-by-default-opt-out-per|Changed skills with context: fork to run in the background by default]] · Context Window
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-capped-the-frontend-design-plugin-suggestion-tip-at-3-lifetime-impressions-inste|Capped the frontend-design plugin suggestion tip at 3 lifetime impressions instead…]]
- Later: 2026-07-24 · Claude Code · [[Changes/Claude Code/2026-07-24-5-apps-and-integrations-changes-in-v2-1-219|5 Apps and Integrations changes in v2.1.219]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-22-7ebd31&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-22-3-apps-and-integrations-changes-in-v2-1-218.md%0ACard%20ID%3A%20claude-code-2026-07-22-7ebd31%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.218%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->