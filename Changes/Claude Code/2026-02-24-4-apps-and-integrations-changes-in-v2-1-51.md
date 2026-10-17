---
card_id: claude-code-2026-02-24-827263
date: '2026-02-24'
description: 'Claude Code · 2026-02-24 · Apps and Integrations: 4 changes in v2.1.51
  — Added `claude remote-control` subcommand for external builds, enabling local…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1069
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0c5565f2c6224355cb59e037f90c7cbdf98f244a0c88d6a71215f89d72521c0e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-24-827263
  comparison: ''
  date: '2026-02-24'
  description: 'Claude Code — v2.1.51: 4 Apps and Integrations changes'
  evidence:
  - quote: Added `claude remote-control` subcommand for external builds, enabling
      local environment serving for all users.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  - quote: Updated plugin marketplace default git timeout from 30s to 120s and added
      `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` to configure.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  - quote: Added support for custom npm registries and specific version pinning when
      installing plugins from npm sources
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  - quote: Added `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, and `CLAUDE_CODE_ORGANIZATION_UUID`
      environment variables for SDK callers to provide account info synchronously,
      eliminating a race condition where early telemetry events lacked account metadata.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-51
  source_release: claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.51
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-02-19-preview-diagrams-and-mini-apps-directly-in-chat|Preview
  diagrams and mini apps directly in chat]]'
- '[[Changes/Claude Code/2026-02-19-2-apps-and-integrations-changes-in-v2-1-49|2 Apps
  and Integrations changes in v2.1.49]]'
- '[[Changes/Claude Code/2026-02-20-claude-code-simple-mode-now-also-disables-mcp-tools-attachments-hooks-and-claude|CLAUDE_CODE_SIMPLE
  mode now also disables MCP tools, attachments, hooks…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.51
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.51

**Claude Code** · 2026-02-24 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.51) · from [[Releases/Claude Code/claude-code-2026-02-24-v2-1-51-github-289665343-b4bbdd9c|v2.1.51]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `claude remote-control` subcommand for external builds, enabling local environment serving for all users.

> Updated plugin marketplace default git timeout from 30s to 120s and added `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` to configure.

> Added support for custom npm registries and specific version pinning when installing plugins from npm sources

> Added `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, and `CLAUDE_CODE_ORGANIZATION_UUID` environment variables for SDK callers to provide account info synchronously, eliminating a race condition where early telemetry events lacked account metadata.

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.51
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety and Privacy changes in v2.1.51]] · Safety and Privacy
- [[Changes/Claude Code/2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa|BashTool now skips login shell (-l flag) by default when a shell snapshot…]] · Developer Workflow
- [[Changes/Claude Code/2026-02-24-tool-results-larger-than-50k-characters-are-now-persisted-to-disk-previously-100|Tool results larger than 50K characters are now persisted to disk (previously 100K)]] · Context Window
- [[Changes/Claude Code/2026-02-24-the-model-picker-now-shows-human-readable-labels-e-g-sonnet-4-5-instead-of-raw-m|The /model picker now shows human-readable labels (e.g., "Sonnet 4.5") instead…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-02-20 · Claude Code · [[Changes/Claude Code/2026-02-20-claude-code-simple-mode-now-also-disables-mcp-tools-attachments-hooks-and-claude|CLAUDE_CODE_SIMPLE mode now also disables MCP tools, attachments, hooks…]]
- Later: 2026-02-25 · ChatGPT · [[Changes/ChatGPT/2026-02-25-sources-from-apps-paste-a-link-to-a-slack-channel-or-google-drive-file-or-folder|Sources from apps]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-24-827263&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-24-4-apps-and-integrations-changes-in-v2-1-51.md%0ACard%20ID%3A%20claude-code-2026-02-24-827263%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.51%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->