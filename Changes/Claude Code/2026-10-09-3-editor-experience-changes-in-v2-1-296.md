---
card_id: claude-code-2026-10-09-0822ee
date: '2026-10-09'
description: 'Claude Code · 2026-10-09 · Editor Experience: 3 changes in v2.1.296
  — Added a `code` key to the Claude apps gateway''s `managed.policies[]`: the same
  settings…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1305
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0e0c522240596328936c3f6538ba92c8aaea07a032c6c2216857c9e9e2e96911
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-09-0822ee
  comparison: ''
  date: '2026-10-09'
  description: 'Claude Code — v2.1.296: 3 Editor Experience changes'
  evidence:
  - quote: 'Added a `code` key to the Claude apps gateway''s `managed.policies[]`:
      the same settings as `cli`, also applied in Claude Desktop''s Code tab; beside
      `desktop`, it turns on Claude Desktop''s gateway mode'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: 'Improved Claude Desktop''s Code tab behind a Claude apps gateway: when
      a session can''t start, including on a machine not set up for the gateway''s
      `code` settings, the reason shows as a reply'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: '[Cloud sessions] Added a status filter to the Sessions and Runners lists
      on a self-hosted environment''s Activity tab in admin settings; you can pick
      several statuses at once'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-editor-experience-changes-in-v2-1-296
  source_release: claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a
  source_type: github_releases
  theme: editor-experience
  title: 3 Editor Experience changes in v2.1.296
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-06-added-prompt-autocomplete-an-event-a-mod-hooks-to-add-its-own-rows-to-the-prompt|Added
  prompt.autocomplete, an event a mod hooks to add its own rows to the prompt…]]'
- '[[Changes/Claude Code/2026-10-07-improved-the-bash-edit-diff-note-to-say-the-listed-files-changed-while-the-comma|Improved
  the Bash edit diff note to say the listed files changed while the command…]]'
- '[[Changes/Claude Code/2026-10-08-changed-tab-stops-to-count-from-where-a-text-starts-instead-of-from-the-screen-s|Changed
  tab stops to count from where a text starts instead of from the screen''s left edge]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a]]'
source_type: github_releases
theme: editor-experience
title: 3 Editor Experience changes in v2.1.296
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Editor Experience changes in v2.1.296

**Claude Code** · 2026-10-09 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) · from [[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `code` key to the Claude apps gateway's `managed.policies[]`: the same settings as `cli`, also applied in Claude Desktop's Code tab; beside `desktop`, it turns on Claude Desktop's gateway mode

> Improved Claude Desktop's Code tab behind a Claude apps gateway: when a session can't start, including on a machine not set up for the gateway's `code` settings, the reason shows as a reply

> [Cloud sessions] Added a status filter to the Sessions and Runners lists on a self-hosted environment's Activity tab in admin settings; you can pick several statuses at once

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer Workflow changes in v2.1.296]] · Developer Workflow
- [[Changes/Claude Code/2026-10-09-improved-transcript-toggle-ctrl-o-responsiveness-in-code-heavy-conversations-by|Improved transcript toggle (ctrl+o) responsiveness in code-heavy conversations…]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety and Privacy changes in v2.1.296]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context Window changes in v2.1.296]] · Context Window
- [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]] · Agent Mode
- [[Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price|Updated /cost, the status line, --max-budget-usd and the SDK's cost figures…]] · Pricing Model
- [[Changes/Claude Code/2026-10-09-improved-the-errors-for-a-refused-cloud-session-they-now-say-why-your-organizati|Improved the errors for a refused cloud session]] · Account and Access
- [[Changes/Claude Code/2026-10-09-improved-fullscreen-mode-the-link-under-the-mouse-pointer-is-now-underlined-to-s|Improved fullscreen mode]] · Interface Experience
- [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]] · Model Support
- [[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3 Apps and Integrations changes in v2.1.296]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-09-3-other-changes-in-v2-1-296|3 other changes in v2.1.296]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-changed-tab-stops-to-count-from-where-a-text-starts-instead-of-from-the-screen-s|Changed tab stops to count from where a text starts instead of from the screen's left edge]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-3-editor-experience-changes-in-v2-1-300|3 Editor Experience changes in v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-09-0822ee&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-09-3-editor-experience-changes-in-v2-1-296.md%0ACard%20ID%3A%20claude-code-2026-10-09-0822ee%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.296%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->