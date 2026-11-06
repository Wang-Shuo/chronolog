---
card_id: claude-code-2026-07-24-09043f
date: '2026-07-24'
description: 'Claude Code · 2026-07-24 · Apps and Integrations: 5 changes in v2.1.219
  — Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1219
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 885f60fa6aed715a9ab1fae1010de82659f7913088811c71b0ebc047ae80a07b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-24-09043f
  comparison: ''
  date: '2026-07-24'
  description: 'Claude Code — v2.1.219: 5 Apps and Integrations changes'
  evidence:
  - quote: Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK `register_repo_root`
      control request registers a new working directory mid-session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  - quote: Added `mcp_server_errors` to the headless stream-json init event, listing
      `--mcp-config` entries skipped by config validation; terminal runs print a startup
      warning
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  - quote: Added HTTP status and error text to `claude mcp list` and `/mcp` when a
      server fails to connect, and a warning for MCP config values with hidden leading
      or trailing whitespace
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  - quote: Improved the "Remote Control is only available via api.anthropic.com" error
      to name the specific setting that caused it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  - quote: Changed managed MCP allowlist/denylist `${VAR}` entries to resolve from
      the startup environment and managed-settings env instead of settings-file env
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-apps-and-integrations-changes-in-v2-1-219
  source_release: claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v2.1.219
  type: change
related_changes:
- '[[Changes/Lovable/2026-07-23-let-your-app-s-users-connect-their-own-notion|Let
  your app''s users connect their own Notion]]'
- '[[Changes/Lovable/2026-07-23-recommended-connectors-in-search|Recommended connectors
  in search]]'
- '[[Changes/Ollama/2026-07-23-improved-integrations-restored-claude-code-channels-fixed-anthropic-thinking-str|Improved
  integrations: restored Claude Code Channels, fixed Anthropic thinking…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233|claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v2.1.219
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v2.1.219

**Claude Code** · 2026-07-24 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.219) · from [[Releases/Claude Code/claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233|v2.1.219]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `DirectoryAdded` hook that fires after `/add-dir` or the SDK `register_repo_root` control request registers a new working directory mid-session

> Added `mcp_server_errors` to the headless stream-json init event, listing `--mcp-config` entries skipped by config validation; terminal runs print a startup warning

> Added HTTP status and error text to `claude mcp list` and `/mcp` when a server fails to connect, and a warning for MCP config values with hidden leading or trailing whitespace

> Improved the "Remote Control is only available via api.anthropic.com" error to name the specific setting that caused it

> Changed managed MCP allowlist/denylist `${VAR}` entries to resolve from the startup environment and managed-settings env instead of settings-file env

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-24-2-interface-experience-changes-in-v2-1-219|2 Interface Experience changes in v2.1.219]] · Interface Experience
- [[Changes/Claude Code/2026-07-24-3-model-support-changes-in-v2-1-219|3 Model Support changes in v2.1.219]] · Model Support
- [[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety and Privacy changes in v2.1.219]] · Safety and Privacy
- [[Changes/Claude Code/2026-07-24-4-agent-mode-changes-in-v2-1-219|4 Agent Mode changes in v2.1.219]] · Agent Mode
- [[Changes/Claude Code/2026-07-24-2-other-changes-in-v2-1-219|2 other changes in v2.1.219]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-23 · Ollama · [[Changes/Ollama/2026-07-23-improved-integrations-restored-claude-code-channels-fixed-anthropic-thinking-str|Improved integrations: restored Claude Code Channels, fixed Anthropic thinking…]]
- Later: 2026-07-24 · Cline · [[Changes/Cline/2026-07-24-include-the-host-plugin-version-in-telemetry-events|Include the host plugin version in telemetry events]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-24-09043f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-24-5-apps-and-integrations-changes-in-v2-1-219.md%0ACard%20ID%3A%20claude-code-2026-07-24-09043f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.219%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->