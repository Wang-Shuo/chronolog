---
card_id: claude-code-2026-03-26-e267e3
date: '2026-03-26'
description: 'Claude Code · 2026-03-26 · Developer Workflow: 5 changes in v2.1.84
  — Added `WorktreeCreate` hook support for `type: "http"` — return the created worktree
  path…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2753
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 578e93f50187326ffb90e90372c21d3d9d7ac84f0bbab7448011c04c879c5076
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-26-e267e3
  comparison: ''
  date: '2026-03-26'
  description: 'Claude Code — v2.1.84: 5 Developer Workflow changes'
  evidence:
  - quote: 'Added `WorktreeCreate` hook support for `type: "http"` — return the created
      worktree path via `hookSpecificOutput.worktreePath` in the response JSON'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Added `x-client-request-id` header to API requests for debugging timeouts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Deep links (`claude-cli://`) now open in your preferred terminal instead
      of whichever terminal happens to be first in the detection list
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Background bash tasks that appear stuck on an interactive prompt now surface
      a notification after ~45 seconds
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  - quote: Reduced terminal flickering when animated tool progress scrolls above the
      viewport
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-developer-workflow-changes-in-v2-1-84
  source_release: claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa
  source_type: github_releases
  theme: developer-workflow
  title: 5 Developer Workflow changes in v2.1.84
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-23-2-developer-workflow-changes-in-v1-0-11|2
  Developer Workflow changes in v1.0.11]]'
- '[[Changes/Gemini CLI/2026-03-24-feat-skills-improve-async-pr-review-workflow-and-logging-by-mattkorwel-in-https|feat(skills):
  improve async-pr-review workflow and logging]]'
- '[[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer
  Workflow changes in v0.8.11]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa]]'
source_type: github_releases
theme: developer-workflow
title: 5 Developer Workflow changes in v2.1.84
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Developer Workflow changes in v2.1.84

**Claude Code** · 2026-03-26 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.84) · from [[Releases/Claude Code/claude-code-2026-03-26-v2-1-84-github-301540101-d02104aa|v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `WorktreeCreate` hook support for `type: "http"` — return the created worktree path via `hookSpecificOutput.worktreePath` in the response JSON

> Added `x-client-request-id` header to API requests for debugging timeouts

> Deep links (`claude-cli://`) now open in your preferred terminal instead of whichever terminal happens to be first in the detection list

> Background bash tasks that appear stuck on an interactive prompt now surface a notification after ~45 seconds

> Reduced terminal flickering when animated tool progress scrolls above the viewport

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.84
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-26-2-reliability-and-performance-changes-in-v2-1-84|2 Reliability and Performance changes in v2.1.84]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-26-added-allowedchannelplugins-managed-setting-for-team-enterprise-admins-to-define|Added allowedChannelPlugins managed setting for team/enterprise admins to define…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-26-added-anthropic-default-opus-sonnet-haiku-model-supports-env-vars-to-override-ef|Added ANTHROPIC_DEFAULT{OPUS,SONNET,HAIKU}MODEL_SUPPORTS env vars to override…]] · Model Support
- [[Changes/Claude Code/2026-03-26-slash-commands-unavailable-for-the-current-auth-setup-voice-mobile-chrome-upgrad|Slash commands unavailable for the current auth setup…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-26-added-powershell-tool-for-windows-as-an-opt-in-preview-learn-more-at-https-code|Added PowerShell tool for Windows as an opt-in preview]] · Mobile and Desktop
- [[Changes/Claude Code/2026-03-26-2-agent-mode-changes-in-v2-1-84|2 Agent Mode changes in v2.1.84]] · Agent Mode
- [[Changes/Claude Code/2026-03-26-2-context-window-changes-in-v2-1-84|2 Context Window changes in v2.1.84]] · Context Window
- [[Changes/Claude Code/2026-03-26-6-other-changes-in-v2-1-84|6 other changes in v2.1.84]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-25 · Open WebUI · [[Changes/Open WebUI/2026-03-25-34-developer-workflow-changes-in-v0-8-11|34 Developer Workflow changes in v0.8.11]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-improved-powershell-dangerous-command-detection|Improved PowerShell dangerous command detection]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-26-e267e3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-26-5-developer-workflow-changes-in-v2-1-84.md%0ACard%20ID%3A%20claude-code-2026-03-26-e267e3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.84%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->