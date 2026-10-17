---
card_id: claude-code-2026-07-11-7d7dc5
date: '2026-07-11'
description: 'Claude Code · 2026-07-11 · Apps and Integrations: 2 changes in v2.1.207
  — Plugin hooks/monitors/MCP headersHelper: `${user_config.*}` in shell-form commands
  is…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1206
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c1c57d93cf1d14572c41b29845bcf11bb645c0ca4ba5bb3631e46a2eef938c67
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-11-7d7dc5
  comparison: ''
  date: '2026-07-11'
  description: 'Claude Code — v2.1.207: 2 Apps and Integrations changes'
  evidence:
  - quote: 'Plugin hooks/monitors/MCP headersHelper: `${user_config.*}` in shell-form
      commands is now rejected (shell-injection fix). Hooks: use exec form (`args`
      array) or `$CLAUDE_PLUGIN_OPTION_<KEY>`; monitors and headersHelper: read the
      value inside the script (config file or the server''s `env` block).'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
  - quote: Plugin option values (`pluginConfigs`) are no longer read from project-level
      `.claude/settings.json`; only user, `--settings`, and managed settings are honored
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-apps-and-integrations-changes-in-v2-1-207
  source_release: claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v2.1.207
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-08-reserved-the-claude-browser-mcp-server-name-alongside-claude-preview-ahead-of-th|Reserved
  the "Claude Browser" MCP server name (alongside "Claude Preview") ahead…]]'
- '[[Changes/ChatGPT/2026-07-09-we-re-also-replacing-the-app-directory-with-the-plugin-directory-existing-app-co|We’re
  also replacing the App Directory with the Plugin Directory]]'
- '[[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|Skills
  are now generally available]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91|claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v2.1.207
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v2.1.207

**Claude Code** · 2026-07-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.207) · from [[Releases/Claude Code/claude-code-2026-07-11-v2-1-207-github-352355755-d77b8e91|v2.1.207]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugin hooks/monitors/MCP headersHelper: `${user_config.*}` in shell-form commands is now rejected (shell-injection fix). Hooks: use exec form (`args` array) or `$CLAUDE_PLUGIN_OPTION_<KEY>`; monitors and headersHelper: read the value inside the script (config file or the server's `env` block).

> Plugin option values (`pluginConfigs`) are no longer read from project-level `.claude/settings.json`; only user, `--settings`, and managed settings are honored

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.207
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety and Privacy changes in v2.1.207]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-11-improved-agent-view-pasting-the-same-text-again-now-expands-the-collapsed-pasted|Improved agent view]] · Interface Experience
- [[Changes/Claude Code/2026-07-11-2-agent-mode-changes-in-v2-1-207|2 Agent Mode changes in v2.1.207]] · Agent Mode
- [[Changes/Claude Code/2026-07-11-auto-mode-is-now-available-without-claude-code-enable-auto-mode-opt-in-on-bedroc|Auto mode is now available without CLAUDE_CODE_ENABLE_AUTO_MODE opt-in on Bedrock…]] · Agent Mode
- [[Changes/Claude Code/2026-07-11-changed-bedrock-vertex-and-claude-platform-on-aws-to-default-to-claude-opus-4-8|Changed Bedrock, Vertex, and Claude Platform on AWS to default to Claude Opus 4.8]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-09 · ChatGPT · [[Changes/ChatGPT/2026-07-09-enterprise-and-edu-users-can-find-skills-under-plugins-in-the-sidebar-on-the-ski|Skills are now generally available]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-3-apps-and-integrations-changes-in-v2-1-208|3 Apps and Integrations changes in v2.1.208]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-11-7d7dc5&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-11-2-apps-and-integrations-changes-in-v2-1-207.md%0ACard%20ID%3A%20claude-code-2026-07-11-7d7dc5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.207%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->