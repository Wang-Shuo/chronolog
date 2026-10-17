---
card_id: claude-code-2026-10-09-6b9e9b
date: '2026-10-09'
description: 'Claude Code · 2026-10-09 · Context Window: 2 changes in v2.1.296 — Added
  `autoCompactWindow` to subagent frontmatter and `--agents` definitions, so a subagent…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1254
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0ab7bab15b1b8a30b085ae5e8dbdfb143047d9b25a702170e2cb1d1d5428319f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-09-6b9e9b
  comparison: ''
  date: '2026-10-09'
  description: 'Claude Code — v2.1.296: 2 Context Window changes'
  evidence:
  - quote: Added `autoCompactWindow` to subagent frontmatter and `--agents` definitions,
      so a subagent can auto-compact earlier than the main conversation's window
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: Added an `allow_large` option to the Read tool so Claude can read a text
      file past the usual size limits in one call when it needs the whole file and
      the context has room
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-context-window-changes-in-v2-1-296
  source_release: claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a
  source_type: github_releases
  theme: context-window
  title: 2 Context Window changes in v2.1.296
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-01-changed-opus-4-7-and-fable-to-use-a-1m-context-window-by-default-on-bedrock-vert|Changed
  Opus 4.7+ and Fable to use a 1M context window by default on Bedrock…]]'
- '[[Changes/Claude Code/2026-10-02-changed-autocompact-to-save-the-auto-compact-window-per-model-so-each-model-keep|Changed
  /autocompact to save the auto-compact window per model, so each model…]]'
- '[[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved
  token counts behind a Claude apps gateway on Amazon Bedrock…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a]]'
source_type: github_releases
theme: context-window
title: 2 Context Window changes in v2.1.296
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Context Window changes in v2.1.296

**Claude Code** · 2026-10-09 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) · from [[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `autoCompactWindow` to subagent frontmatter and `--agents` definitions, so a subagent can auto-compact earlier than the main conversation's window

> Added an `allow_large` option to the Read tool so Claude can read a text file past the usual size limits in one call when it needs the whole file and the context has room

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-09-cloud-sessions-added-a-status-filter-to-the-sessions-and-runners-lists-on-a-self|Cloud sessions Added a status filter to the Sessions and Runners lists…]] · Editor Experience
- [[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer Workflow changes in v2.1.296]] · Developer Workflow
- [[Changes/Claude Code/2026-10-09-improved-transcript-toggle-ctrl-o-responsiveness-in-code-heavy-conversations-by|Improved transcript toggle (ctrl+o) responsiveness in code-heavy conversations…]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety and Privacy changes in v2.1.296]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-09-2-mobile-and-desktop-changes-in-v2-1-296|2 Mobile and Desktop changes in v2.1.296]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]] · Agent Mode
- [[Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price|Updated /cost, the status line, --max-budget-usd and the SDK's cost figures…]] · Pricing Model
- [[Changes/Claude Code/2026-10-09-improved-the-errors-for-a-refused-cloud-session-they-now-say-why-your-organizati|Improved the errors for a refused cloud session]] · Account and Access
- [[Changes/Claude Code/2026-10-09-improved-fullscreen-mode-the-link-under-the-mouse-pointer-is-now-underlined-to-s|Improved fullscreen mode]] · Interface Experience
- [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]] · Model Support
- [[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3 Apps and Integrations changes in v2.1.296]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-09-3-other-changes-in-v2-1-296|3 other changes in v2.1.296]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-improved-token-counts-behind-a-claude-apps-gateway-on-amazon-bedrock-which-conte|Improved token counts behind a Claude apps gateway on Amazon Bedrock…]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-09-6b9e9b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-09-2-context-window-changes-in-v2-1-296.md%0ACard%20ID%3A%20claude-code-2026-10-09-6b9e9b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.296%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->