---
card_id: claude-code-2026-06-25-e31098
date: '2026-06-25'
description: 'Claude Code · 2026-06-25 · Reliability and Performance: Added automatic
  memory-pressure reaping for idle background shell commands (disable with…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1288
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: d5d160136d0310b547d0a5333285ab8229f06e1bc63e01b88c16e4102b35e2c5
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-25-e31098
  comparison: ''
  date: '2026-06-25'
  description: 'Claude Code — v2.1.193: Added automatic memory-pressure reaping for
    idle background shell commands (disable with `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1`)'
  evidence:
  - quote: Added automatic memory-pressure reaping for idle background shell commands
      (disable with `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1`)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-automatic-memory-pressure-reaping-for-idle-background-shell-commands-disab
  source_release: claude-code-2026-06-25-v2-1-193-github-344922230-0655000d
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Added automatic memory-pressure reaping for idle background shell commands…
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-22-2-reliability-and-performance-changes-in-rust-v0-142-0|2
  Reliability and Performance changes in rust-v0.142.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans|Show
  per-model token totals in /usage and speed up large history scans]]'
- '[[Changes/Claude Code/2026-06-24-reduced-long-session-memory-growth-from-terminal-output-cache|Reduced
  long-session memory growth from terminal output cache]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|claude-code-2026-06-25-v2-1-193-github-344922230-0655000d]]'
source_type: github_releases
theme: reliability-performance
title: Added automatic memory-pressure reaping for idle background shell commands…
type: change
---

<!-- chronolog:begin region="header" -->
# Added automatic memory-pressure reaping for idle background shell commands…

**Claude Code** · 2026-06-25 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.193) · from [[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|v2.1.193]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added automatic memory-pressure reaping for idle background shell commands (disable with `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1`)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2 Apps and Integrations changes in v2.1.193]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-25-added-live-file-path-autocomplete-to-bash-mode|Added live file path autocomplete to bash mode (!)]] · Editor Experience
- [[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|Added claude_code.assistant_response OpenTelemetry log event containing…]] · Model Support
- [[Changes/Claude Code/2026-06-25-added-a-startup-notice-when-mcp-servers-need-authentication-pointing-at-mcp|Added a startup notice when MCP servers need authentication, pointing at /mcp]] · Account and Access
- [[Changes/Claude Code/2026-06-25-3-agent-mode-changes-in-v2-1-193|3 Agent Mode changes in v2.1.193]] · Agent Mode
- [[Changes/Claude Code/2026-06-25-improved-add-dir-message-when-the-directory-is-already-a-working-directory|Improved /add-dir message when the directory is already a working directory]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-06-24 · Claude Code · [[Changes/Claude Code/2026-06-24-reduced-long-session-memory-growth-from-terminal-output-cache|Reduced long-session memory growth from terminal output cache]]
- Later: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-apps-can-display-richer-safety-buffering-ui-using-server-provided-visibility-and|Apps can display richer safety-buffering UI using server-provided visibility…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-25-e31098&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-25-added-automatic-memory-pressure-reaping-for-idle-background-shell-commands-disab.md%0ACard%20ID%3A%20claude-code-2026-06-25-e31098%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.193%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->