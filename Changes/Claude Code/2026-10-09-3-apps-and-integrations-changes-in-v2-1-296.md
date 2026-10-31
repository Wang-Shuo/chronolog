---
card_id: claude-code-2026-10-09-dffa47
date: '2026-10-09'
description: 'Claude Code · 2026-10-09 · Apps and Integrations: 3 changes in v2.1.296
  — Added a note in `/plugin` on a plugin whose hooks are left out because another…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1296
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a02ebbd348f5928dc80aebf41c35fb6235f298aa722269fce7134202505ed9b0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-09-dffa47
  comparison: ''
  date: '2026-10-09'
  description: 'Claude Code — v2.1.296: 3 Apps and Integrations changes'
  evidence:
  - quote: Added a note in `/plugin` on a plugin whose hooks are left out because
      another enabled plugin has the same name
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: 'Improved `--debug` output for hooks: command hooks on tool calls, prompts,
      SessionStart and Stop now log their command, plugin, outcome and duration when
      they finish, so a slow hook is identifiable'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: Changed the default limit on MCP tool descriptions sent up front and on
      MCP server instructions from 2,048 to 4,096 characters
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-296
  source_release: claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.296
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-07-3-apps-and-integrations-changes-in-v2-1-293|3
  Apps and Integrations changes in v2.1.293]]'
- '[[Changes/Claude Code/2026-10-08-improved-how-prompt-hooks-on-stop-and-subagentstop-written-as-instructions-such|Improved
  how prompt hooks on Stop and SubagentStop written as instructions…]]'
- '[[Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295|14
  Apps and Integrations changes in v2.1.295]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.296
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.296

**Claude Code** · 2026-10-09 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) · from [[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a note in `/plugin` on a plugin whose hooks are left out because another enabled plugin has the same name

> Improved `--debug` output for hooks: command hooks on tool calls, prompts, SessionStart and Stop now log their command, plugin, outcome and duration when they finish, so a slow hook is identifiable

> Changed the default limit on MCP tool descriptions sent up front and on MCP server instructions from 2,048 to 4,096 characters

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-09-3-editor-experience-changes-in-v2-1-296|3 Editor Experience changes in v2.1.296]] · Editor Experience
- [[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer Workflow changes in v2.1.296]] · Developer Workflow
- [[Changes/Claude Code/2026-10-09-improved-transcript-toggle-ctrl-o-responsiveness-in-code-heavy-conversations-by|Improved transcript toggle (ctrl+o) responsiveness in code-heavy conversations…]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety and Privacy changes in v2.1.296]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context Window changes in v2.1.296]] · Context Window
- [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]] · Agent Mode
- [[Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price|Updated /cost, the status line, --max-budget-usd and the SDK's cost figures…]] · Pricing Model
- [[Changes/Claude Code/2026-10-09-improved-the-errors-for-a-refused-cloud-session-they-now-say-why-your-organizati|Improved the errors for a refused cloud session]] · Account and Access
- [[Changes/Claude Code/2026-10-09-improved-fullscreen-mode-the-link-under-the-mouse-pointer-is-now-underlined-to-s|Improved fullscreen mode]] · Interface Experience
- [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]] · Model Support
- [[Changes/Claude Code/2026-10-09-3-other-changes-in-v2-1-296|3 other changes in v2.1.296]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-08 · Claude Code · [[Changes/Claude Code/2026-10-08-14-apps-and-integrations-changes-in-v2-1-295|14 Apps and Integrations changes in v2.1.295]]
- Later: 2026-10-13 · Cursor · [[Changes/Cursor/2026-10-13-2-apps-and-integrations-changes-in-origin-app-marketplace|2 Apps and Integrations changes in Origin App Marketplace]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-09-dffa47&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-09-3-apps-and-integrations-changes-in-v2-1-296.md%0ACard%20ID%3A%20claude-code-2026-10-09-dffa47%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.296%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->