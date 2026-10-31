---
card_id: claude-code-2026-10-20-7e4f88
date: '2026-10-20'
description: 'Claude Code · 2026-10-20 · Safety and Privacy: 3 changes in v2.1.305
  — Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux can create
  user…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1283
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b2fd66b0db420813aa434d9327ec8207fe80d6f10d4a7fb35e9fdf82bf4cf4c8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-20-7e4f88
  comparison: ''
  date: '2026-10-20'
  description: 'Claude Code — v2.1.305: 3 Safety and Privacy changes'
  evidence:
  - quote: Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux
      can create user namespaces (Chromium, rootless podman); this lets them get around
      the sandbox's file protections
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  - quote: 'Fixed startup warnings printing as raw text above the logo: they now go
      to the debug log, and permission rules that restrict nothing show as warning
      rows under the banner'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  - quote: Improved MCP consent dialogs so an Enter meant for the prompt is less likely
      to be taken as Accept
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-305
  source_release: claude-code-2026-10-20-v2-1-305-github-418781864-90995baa
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.305
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety
  and Privacy changes in v2.1.301]]'
- '[[Changes/Claude Code/2026-10-16-2-safety-and-privacy-changes-in-v2-1-302|2 Safety
  and Privacy changes in v2.1.302]]'
- '[[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added
  decider: "person" to a mod''s tool.check answer: only the permission dialog…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-20-v2-1-305-github-418781864-90995baa|claude-code-2026-10-20-v2-1-305-github-418781864-90995baa]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.305
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.305

**Claude Code** · 2026-10-20 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.305) · from [[Releases/Claude Code/claude-code-2026-10-20-v2-1-305-github-418781864-90995baa|v2.1.305]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux can create user namespaces (Chromium, rootless podman); this lets them get around the sandbox's file protections

> Fixed startup warnings printing as raw text above the logo: they now go to the debug log, and permission rules that restrict nothing show as warning rows under the banner

> Improved MCP consent dialogs so an Enter meant for the prompt is less likely to be taken as Accept

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.305
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-20-2-developer-workflow-changes-in-v2-1-305|2 Developer Workflow changes in v2.1.305]] · Developer Workflow
- [[Changes/Claude Code/2026-10-20-vscode-changed-the-message-shown-when-a-session-does-not-start-in-time-and-no-ho|VSCode Changed the message shown when a session does not start in time and no hook…]] · Account and Access
- [[Changes/Claude Code/2026-10-20-4-apps-and-integrations-changes-in-v2-1-305|4 Apps and Integrations changes in v2.1.305]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-20-claude-tag-added-public-slack-channels-claude-hasn-t-joined-to-the-claude-tag-ad|Claude Tag Added public Slack channels Claude hasn't joined to the Claude Tag…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-20-improved-a-mod-s-image-to-draw-its-picture-in-iterm2-3-5-and-later-with-fullscre|Improved a mod's Image to draw its picture in iTerm2 3.5 and later with fullscreen…]] · Interface Experience
- [[Changes/Claude Code/2026-10-20-vscode-added-a-running-start-up-hooks-spinner-status-with-a-screen-reader-announ|VSCode Added a "Running start-up hooks" spinner status, with a screen reader…]] · Accessibility and Localization
- [[Changes/Claude Code/2026-10-20-4-other-changes-in-v2-1-305|4 other changes in v2.1.305]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-19 · Claude Code · [[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added decider: "person" to a mod's tool.check answer: only the permission dialog…]]
- Later: 2026-10-21 · Claude Code · [[Changes/Claude Code/2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm|Added the claude_code.safety_event OpenTelemetry event for each tool call…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-20-7e4f88&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-20-3-safety-and-privacy-changes-in-v2-1-305.md%0ACard%20ID%3A%20claude-code-2026-10-20-7e4f88%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.305%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->