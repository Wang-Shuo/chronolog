---
card_id: claude-code-2026-04-01-071170
date: '2026-04-01'
description: 'Claude Code · 2026-04-01 · Apps and Integrations: 3 changes in v2.1.89
  — Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection
  wait…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b462a60de1cca98b9212b33b8dcb11cdbd9412242633e58e8fbd711f18120fd3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-01-071170
  comparison: ''
  date: '2026-04-01'
  description: 'Claude Code — v2.1.89: 3 Apps and Integrations changes'
  evidence:
  - quote: Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection
      wait entirely, and bounded `--mcp-config` server connections at 5s instead of
      blocking on the slowest server
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  - quote: Improved `@`-mention typeahead to rank source files above MCP resources
      with similar names
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  - quote: Documented `TaskCreated` hook event and its blocking behavior
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-89
  source_release: claude-code-2026-04-01-v2-1-89-github-303967782-358023f0
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.89
  type: change
related_changes:
- '[[Changes/OpenHands/2026-03-30-added-support-for-hooks-by-xingyaoww-in-https-github-com-openhands-openhands-pul|Added
  support for hooks]]'
- '[[Changes/Codex CLI/2026-03-31-12-apps-and-integrations-changes-in-rust-v0-118-0|12
  Apps and Integrations changes in rust-v0.118.0]]'
- '[[Changes/GitHub Copilot CLI/2026-03-31-5-apps-and-integrations-changes-in-v1-0-14|5
  Apps and Integrations changes in v1.0.14]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|claude-code-2026-04-01-v2-1-89-github-303967782-358023f0]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.89
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.89

**Claude Code** · 2026-04-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.89) · from [[Releases/Claude Code/claude-code-2026-04-01-v2-1-89-github-303967782-358023f0|v2.1.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `MCP_CONNECTION_NONBLOCKING=true` for `-p` mode to skip the MCP connection wait entirely, and bounded `--mcp-config` server connections at 5s instead of blocking on the slowest server

> Improved `@`-mention typeahead to rank source files above MCP resources with similar names

> Documented `TaskCreated` hook event and its blocking behavior

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.89
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-01-usage-now-hides-redundant-current-week-sonnet-only-bar-for-pro-and-enterprise-pl|/usage now hides redundant "Current week (Sonnet only)" bar for Pro and Enterprise plans]] · Model Support
- [[Changes/Claude Code/2026-04-01-changed-edit-to-work-on-files-viewed-via-bash-with-sed-n-or-cat-without-requirin|Changed Edit to work on files viewed via Bash with sed -n or cat, without…]] · Editor Experience
- [[Changes/Claude Code/2026-04-01-4-developer-workflow-changes-in-v2-1-89|4 Developer Workflow changes in v2.1.89]] · Developer Workflow
- [[Changes/Claude Code/2026-04-01-3-agent-mode-changes-in-v2-1-89|3 Agent Mode changes in v2.1.89]] · Agent Mode
- [[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety and Privacy changes in v2.1.89]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-01-changed-hook-output-over-50k-characters-to-be-saved-to-disk-with-a-file-path-pre|Changed hook output over 50K characters to be saved to disk with a file path…]] · Context Window
- [[Changes/Claude Code/2026-04-01-powershell-tool-on-windows-external-command-arguments-containing-both-a-double-q|PowerShell tool on Windows]] · Mobile and Desktop
- [[Changes/Claude Code/2026-04-01-added-claude-code-no-flicker-1-environment-variable-to-opt-into-flicker-free-alt|Added CLAUDE_CODE_NO_FLICKER=1 environment variable to opt into flicker-free…]] · Interface Experience
- [[Changes/Claude Code/2026-04-01-6-other-changes-in-v2-1-89|6 other changes in v2.1.89]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-31 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-31-5-apps-and-integrations-changes-in-v1-0-14|5 Apps and Integrations changes in v1.0.14]]
- Later: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-2-apps-and-integrations-changes-in-v2-1-90|2 Apps and Integrations changes in v2.1.90]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-01-071170&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-01-3-apps-and-integrations-changes-in-v2-1-89.md%0ACard%20ID%3A%20claude-code-2026-04-01-071170%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.89%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->