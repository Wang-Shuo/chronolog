---
card_id: claude-code-2026-08-28-568584
date: '2026-08-28'
description: 'Claude Code · 2026-08-28 · Developer Workflow: 3 changes in v2.1.251
  — Added `attach`, `logs`, `stop`, `respawn`, and `rm` to `claude --help`; the `--resume`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 99ecff57e6e230a40945d016b0202e9b8ab341e89e8caa44b9e1e611f182521c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-28-568584
  comparison: ''
  date: '2026-08-28'
  description: 'Claude Code — v2.1.251: 3 Developer Workflow changes'
  evidence:
  - quote: Added `attach`, `logs`, `stop`, `respawn`, and `rm` to `claude --help`;
      the `--resume` message for a running background session now names the exact
      `claude attach <id>` command
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: 'Improved cloud sessions: when the session''s network proxy drops a connection
      during a Bash command, the tool result now names the host and reason instead
      of only "connection reset"'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed project-level `.claude/settings.json` `env` to no longer set `CLAUDE_CONFIG_DIR`,
      `CLAUDE_CODE_TMPDIR`, or `TMPDIR`/`TMP`/`TEMP`; set them in your shell, user,
      or managed settings instead
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-developer-workflow-changes-in-v2-1-251
  source_release: claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2.1.251
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-25-2-developer-workflow-changes-in-v2-1-246|2 Developer
  Workflow changes in v2.1.246]]'
- '[[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed
  terminal hyperlinks in rendered markdown]]'
- '[[Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t|Changed
  Anthropic telemetry export failures to log at debug level…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in v2.1.251
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2.1.251

**Claude Code** · 2026-08-28 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) · from [[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `attach`, `logs`, `stop`, `respawn`, and `rm` to `claude --help`; the `--resume` message for a running background session now names the exact `claude attach <id>` command

> Improved cloud sessions: when the session's network proxy drops a connection during a Bash command, the tool result now names the host and reason instead of only "connection reset"

> Changed project-level `.claude/settings.json` `env` to no longer set `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR`, or `TMPDIR`/`TMP`/`TEMP`; set them in your shell, user, or managed settings instead

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]] · Account and Access
- [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing Model
- [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]] · Context Window
- [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Agent Mode
- [[Changes/Claude Code/2026-08-28-added-a-spend-limit-bar-to-usage-and-a-rate-limits-spend-limit-status-line-field|Added a Spend limit bar to /usage and a rate_limits.spend_limit status line…]] · Interface Experience
- [[Changes/Claude Code/2026-08-28-5-model-support-changes-in-v2-1-251|5 Model Support changes in v2.1.251]] · Model Support
- [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-28-7-other-changes-in-v2-1-251|7 other changes in v2.1.251]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t|Changed Anthropic telemetry export failures to log at debug level…]]
- Later: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-28-568584&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-28-3-developer-workflow-changes-in-v2-1-251.md%0ACard%20ID%3A%20claude-code-2026-08-28-568584%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.251%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->