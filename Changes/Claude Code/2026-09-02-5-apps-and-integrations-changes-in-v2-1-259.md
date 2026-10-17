---
card_id: claude-code-2026-09-02-b9f15f
date: '2026-09-02'
description: 'Claude Code · 2026-09-02 · Apps and Integrations: 5 changes in v2.1.259
  — Added `managedMcpServers` managed setting: organizations can provide HTTP/SSE
  MCP…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8f1a6a7b4e61d9d74f3cd21a7b60f32b8a234de10ed02b3b6e51f9948b3611d1
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-02-b9f15f
  comparison: ''
  date: '2026-09-02'
  description: 'Claude Code — v2.1.259: 5 Apps and Integrations changes'
  evidence:
  - quote: 'Added `managedMcpServers` managed setting: organizations can provide HTTP/SSE
      MCP servers to every user (same entry shape as `.mcp.json`); entries that name
      a command to run are skipped'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Added `--json` to `claude plugin validate` for a machine-readable validation
      report
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: 'Improved headless/SDK session start: the first turn begins up to 50 ms
      sooner when MCP servers finish connecting'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: Improved `/install-github-app` to explain it is GitHub-only and point to
      the GitLab CI/CD docs when run inside a GitLab repository
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  - quote: 'Changed `allowedMcpServers` to govern only servers users add: a literal
      `managed-mcp.json` server your allowlist used to filter out now loads on upgrade;
      use `deniedMcpServers` to keep it off'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-apps-and-integrations-changes-in-v2-1-259
  source_release: claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f
  source_type: github_releases
  theme: apps-integrations
  title: 5 Apps and Integrations changes in v2.1.259
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4
  Apps and Integrations changes in v2.1.251]]'
- '[[Changes/ChatGPT/2026-09-01-eligible-chatgpt-for-clinicians-users-in-the-united-states-can-now-use-healthcar|Healthcare
  Public Data in ChatGPT for Clinicians]]'
- '[[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2
  Apps and Integrations changes in v2.1.257]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f|claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f]]'
source_type: github_releases
theme: apps-integrations
title: 5 Apps and Integrations changes in v2.1.259
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Apps and Integrations changes in v2.1.259

**Claude Code** · 2026-09-02 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.259) · from [[Releases/Claude Code/claude-code-2026-09-02-v2-1-259-github-381579834-0f335a0f|v2.1.259]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `managedMcpServers` managed setting: organizations can provide HTTP/SSE MCP servers to every user (same entry shape as `.mcp.json`); entries that name a command to run are skipped

> Added `--json` to `claude plugin validate` for a machine-readable validation report

> Improved headless/SDK session start: the first turn begins up to 50 ms sooner when MCP servers finish connecting

> Improved `/install-github-app` to explain it is GitHub-only and point to the GitLab CI/CD docs when run inside a GitLab repository

> Changed `allowedMcpServers` to govern only servers users add: a literal `managed-mcp.json` server your allowlist used to filter out now loads on upgrade; use `deniedMcpServers` to keep it off

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.259
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-02-improved-terminal-resize-and-first-render-performance-for-long-responses-by-reus|Improved terminal resize and first-render performance for long responses by reusing…]] · Developer Workflow
- [[Changes/Claude Code/2026-09-02-vscode-added-an-active-quick-filter-and-a-status-filter-menu-needs-input-working|VSCode Added an Active quick filter and a status filter menu…]] · Interface Experience
- [[Changes/Claude Code/2026-09-02-4-safety-and-privacy-changes-in-v2-1-259|4 Safety and Privacy changes in v2.1.259]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-02-2-agent-mode-changes-in-v2-1-259|2 Agent Mode changes in v2.1.259]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]]
- Later: 2026-09-03 · ChatGPT · [[Changes/ChatGPT/2026-09-03-today-we-added-the-zendesk-and-onenote-plugins-in-the-plugin-directory-the-zende-012cbd|Zendesk & OneNote Plugins in ChatGPT and Codex Beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-02-b9f15f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-02-5-apps-and-integrations-changes-in-v2-1-259.md%0ACard%20ID%3A%20claude-code-2026-09-02-b9f15f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.259%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->