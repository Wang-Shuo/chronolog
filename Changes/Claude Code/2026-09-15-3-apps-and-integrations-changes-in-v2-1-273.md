---
card_id: claude-code-2026-09-15-34b623
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Apps and Integrations: 3 changes in v2.1.273
  — Added a notification when an MCP server disconnects mid-session and automatic…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1272
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fa3934eba733394452a46726169ffada8237532a700b5a0208f3517c11eefe52
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-15-34b623
  comparison: ''
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: 3 Apps and Integrations changes'
  evidence:
  - quote: Added a notification when an MCP server disconnects mid-session and automatic
      reconnection gives up, pointing at `/mcp`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Added forking a session started with `claude --remote-control` or `/remote-control`
      from the Claude app; the fork runs as a background session on your computer
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Changed `OTEL_LOG_TOOL_DETAILS=1` to also include real agent, skill, plugin
      and MCP server names on cost and token metrics
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-273
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.273
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-14-for-new-health-plugin-connections-chatgpt-will-now-default-to-each-user-s-global|For
  new Health plugin connections, ChatGPT will now default to each user’s global…]]'
- '[[Changes/ChatGPT/2026-09-14-you-can-change-your-health-permissions-anytime-in-settings-plugins-health-learn|You
  can change your Health permissions anytime in Settings → Plugins → Health]]'
- '[[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5
  Apps and Integrations changes in v2.1.271]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.273
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.273

**Claude Code** · 2026-09-15 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a notification when an MCP server disconnects mid-session and automatic reconnection gives up, pointing at `/mcp`

> Added forking a session started with `claude --remote-control` or `/remote-control` from the Claude app; the fork runs as a background session on your computer

> Changed `OTEL_LOG_TOOL_DETAILS=1` to also include real agent, skill, plugin and MCP server names on cost and token metrics

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-improved-the-routine-detail-page-menu-and-rename-in-the-b|Claude Code on the web Improved the routine detail page]] · Interface Experience
- [[Changes/Claude Code/2026-09-15-improved-artifact-database-writes-an-update-can-now-remove-a-single-field-instea|Improved artifact database writes]] · Files and Data
- [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Agent Mode
- [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]] · Model Support
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]] · Editor Experience
- [[Changes/Claude Code/2026-09-15-4-account-and-access-changes-in-v2-1-273|4 Account and Access changes in v2.1.273]] · Account and Access
- [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|Added x-claude-code-request-class, x-claude-code-agent-type…]] · Context Window
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-removed-the-full-page-desktop-app-download-screen-that-ne|Claude Code on the web Removed the full-page desktop-app download screen that new…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]] · Developer Workflow
- [[Changes/Claude Code/2026-09-15-8-other-changes-in-v2-1-273|8 other changes in v2.1.273]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5 Apps and Integrations changes in v2.1.271]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-10-apps-and-integrations-changes-in-v2-1-274|10 Apps and Integrations changes in v2.1.274]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-34b623&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-3-apps-and-integrations-changes-in-v2-1-273.md%0ACard%20ID%3A%20claude-code-2026-09-15-34b623%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->