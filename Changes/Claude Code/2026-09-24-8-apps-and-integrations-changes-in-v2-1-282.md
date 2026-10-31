---
card_id: claude-code-2026-09-24-b8440f
date: '2026-09-24'
description: 'Claude Code · 2026-09-24 · Apps and Integrations: 8 changes in v2.1.282
  — Added the `allowClaudeInChromeWithManagedMcp` managed setting to let `claude…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1281
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b80858742a0a2ebf2e1caf344d65606fad913ea9e38a3fca834c82d2d18ced61
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-24-b8440f
  comparison: ''
  date: '2026-09-24'
  description: 'Claude Code — v2.1.282: 8 Apps and Integrations changes'
  evidence:
  - quote: Added the `allowClaudeInChromeWithManagedMcp` managed setting to let `claude
      --chrome` run alongside an exclusive `managed-mcp.json`; the error shown when
      Chrome is blocked now names it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: Added `store.readiness_grace_seconds` to the Claude apps gateway so `/readyz`
      can stay ready through a short Postgres outage such as a database failover
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: Changed `Skill(anthropic-skills:*)` and `Skill(claude-ai:*)` allow rules
      to cover only skills synced from claude.ai, not plugins or other skills that
      merely use such a name
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: Changed skill folders, command files and workflow commands in the `anthropic-skills`
      or `claude-ai` namespace to no longer load; a plugin so named still loads but
      yields name ties to synced skills
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: Changed MCP servers configured under the name `anthropic-skills` or `claude-ai`
      to list no skills or prompts (their tools still work); rename the server in
      your MCP configuration to list them again
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: '[Cloud sessions] Added Claude GitHub App status to Settings › Connectors
      › GitHub: whether the app is installed and reachable for your account, plus
      steps to connect, install or reconnect'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: '[Cloud sessions] Added attaching a repository from a different GitHub
      owner, such as a fork''s upstream, to a running cloud session that already has
      one, including sessions started from Slack'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  - quote: '[Claude Tag] Changed the bordered cards Claude uses in Slack replies for
      plans, tables and details to render wide by default instead of a narrow width'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-apps-and-integrations-changes-in-v2-1-282
  source_release: claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in v2.1.282
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8
  Apps and Integrations changes in v2.1.280]]'
- '[[Changes/Claude Code/2026-09-23-17-apps-and-integrations-changes-in-v2-1-281|17
  Apps and Integrations changes in v2.1.281]]'
- '[[Changes/Cursor/2026-09-23-integrations|Integrations]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4|claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in v2.1.282
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in v2.1.282

**Claude Code** · 2026-09-24 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.282) · from [[Releases/Claude Code/claude-code-2026-09-24-v2-1-282-github-395840120-957e42c4|v2.1.282]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added the `allowClaudeInChromeWithManagedMcp` managed setting to let `claude --chrome` run alongside an exclusive `managed-mcp.json`; the error shown when Chrome is blocked now names it

> Added `store.readiness_grace_seconds` to the Claude apps gateway so `/readyz` can stay ready through a short Postgres outage such as a database failover

> Changed `Skill(anthropic-skills:*)` and `Skill(claude-ai:*)` allow rules to cover only skills synced from claude.ai, not plugins or other skills that merely use such a name

> Changed skill folders, command files and workflow commands in the `anthropic-skills` or `claude-ai` namespace to no longer load; a plugin so named still loads but yields name ties to synced skills

> Changed MCP servers configured under the name `anthropic-skills` or `claude-ai` to list no skills or prompts (their tools still work); rename the server in your MCP configuration to list them again

> [Cloud sessions] Added Claude GitHub App status to Settings › Connectors › GitHub: whether the app is installed and reachable for your account, plus steps to connect, install or reconnect

> [Cloud sessions] Added attaching a repository from a different GitHub owner, such as a fork's upstream, to a running cloud session that already has one, including sessions started from Slack

> [Claude Tag] Changed the bordered cards Claude uses in Slack replies for plans, tables and details to render wide by default instead of a narrow width

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.282
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-24-2-model-support-changes-in-v2-1-282|2 Model Support changes in v2.1.282]] · Model Support
- [[Changes/Claude Code/2026-09-24-improved-the-error-shown-on-windows-when-a-session-can-t-be-resumed-because-its|Improved the error shown on Windows when a session can't be resumed because…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-24-4-interface-experience-changes-in-v2-1-282|4 Interface Experience changes in v2.1.282]] · Interface Experience
- [[Changes/Claude Code/2026-09-24-updated-the-claude-api-skill-pre-output-refusal-billing-now-links-to-the-how-ref|Updated the claude-api skill]] · Pricing Model
- [[Changes/Claude Code/2026-09-24-changed-windows-wsl-managed-settings-so-an-admin-policy-that-is-present-but-inva|Changed Windows/WSL managed settings so an admin policy that is present but invalid…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-24-2-agent-mode-changes-in-v2-1-282|2 Agent Mode changes in v2.1.282]] · Agent Mode
- [[Changes/Claude Code/2026-09-24-4-safety-and-privacy-changes-in-v2-1-282|4 Safety and Privacy changes in v2.1.282]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-24-6-other-changes-in-v2-1-282|6 other changes in v2.1.282]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-23 · Cursor · [[Changes/Cursor/2026-09-23-integrations|Integrations]]
- Later: 2026-09-25 · Claude Code · [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-24-b8440f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-24-8-apps-and-integrations-changes-in-v2-1-282.md%0ACard%20ID%3A%20claude-code-2026-09-24-b8440f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.282%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->