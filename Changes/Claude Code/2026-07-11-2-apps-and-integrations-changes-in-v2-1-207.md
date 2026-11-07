---
card_id: claude-code-2026-07-11-7d7dc5
date: '2026-07-11'
description: 'Claude Code · 2026-07-11 · Apps and Integrations: 2 changes in v2.1.207
  — Plugin hooks/monitors/MCP headersHelper: `${user_config.*}` in shell-form commands
  is…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2766
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: edfcf13ca964f474a1895d1dfdc715ad5e05b3894528c3bff691964d7c0f134c
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
- '[[Changes/OpenHands/2026-07-09-chore-bump-sdk-packages-to-v1-34-0-by-all-hands-bot-in-https-github-com-openhand|chore:
  bump SDK packages to v1.34.0]]'
- '[[Changes/GitHub Copilot CLI/2026-07-10-9-apps-and-integrations-changes-in-v1-0-70|9
  Apps and Integrations changes in v1.0.70]]'
- '[[Changes/Replit/2026-07-10-integrations|Integrations]]'
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

- Earlier: 2026-07-10 · Replit · [[Changes/Replit/2026-07-10-integrations|Integrations]]
- Later: 2026-07-11 · Ollama · [[Changes/Ollama/2026-07-11-2-apps-and-integrations-changes-in-v0-32-0|2 Apps and Integrations changes in v0.32.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-11-7d7dc5&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-11-2-apps-and-integrations-changes-in-v2-1-207.md%0ACard%20ID%3A%20claude-code-2026-07-11-7d7dc5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.207%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->