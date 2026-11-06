---
card_id: claude-code-2026-06-02-65dbd0
date: '2026-06-02'
description: 'Claude Code · 2026-06-02 · Developer Workflow: 2 changes in v2.1.160
  — `acceptEdits` mode now prompts before writing build-tool config files that grant
  code…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1172
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ecf313aacc7f48b5fe7e2dc2de89a1f91b5dda2ba83d5d0f9f8a1eeb308b8ef7
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-02-65dbd0
  comparison: ''
  date: '2026-06-02'
  description: 'Claude Code — v2.1.160: 2 Developer Workflow changes'
  evidence:
  - quote: '`acceptEdits` mode now prompts before writing build-tool config files
      that grant code execution (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`,
      `.pre-commit-config.yaml`, `.devcontainer/`, etc.)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.160
  - quote: Improved background-session teardown (`claude rm`/`stop`, idle reap) to
      send SIGTERM to running shell subprocesses before SIGKILL, so cleanup handlers
      run
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.160
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-developer-workflow-changes-in-v2-1-160
  source_release: claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v2.1.160
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0|11
  Developer Workflow changes in rust-v0.136.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-01-lsp-show-lsp-test-and-lsp-reload-correctly-discover-project-lsp-config-when-the|/lsp
  show, /lsp test, and /lsp reload correctly discover project LSP config…]]'
- '[[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer
  Workflow changes in v0.9.6]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a|claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v2.1.160
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v2.1.160

**Claude Code** · 2026-06-02 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.160) · from [[Releases/Claude Code/claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a|v2.1.160]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `acceptEdits` mode now prompts before writing build-tool config files that grant code execution (`.npmrc`, `.yarnrc*`, `bunfig.toml`, `.bazelrc`, `.pre-commit-config.yaml`, `.devcontainer/`, etc.)

> Improved background-session teardown (`claude rm`/`stop`, idle reap) to send SIGTERM to running shell subprocesses before SIGKILL, so cleanup handlers run

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.160
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-02-improved-auto-mode-classifier-latency-by-reducing-reasoning-on-routine-actions-l|Improved auto mode classifier latency by reducing reasoning on routine actions…]] · Reliability and Performance
- [[Changes/Claude Code/2026-06-02-removed-claude-code-opus-4-6-fast-mode-override-the-environment-variable-is-now|Removed CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE; the environment variable is now a no-op]] · Model Support
- [[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|Added a prompt before writing to shell startup files…]] · Account and Access
- [[Changes/Claude Code/2026-06-02-edit-no-longer-requires-a-separate-read-after-viewing-a-file-with-grep-single-fi|Edit no longer requires a separate Read after viewing a file with grep]] · Editor Experience
- [[Changes/Claude Code/2026-06-02-improved-performance-of-opening-recently-inactive-background-agent-sessions-in-c|Improved performance of opening recently-inactive background agent sessions…]] · Agent Mode
- [[Changes/Claude Code/2026-06-02-removed-the-jetbrains-plugin-install-suggestion-from-startup|Removed the JetBrains plugin install suggestion from startup]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-02-renamed-the-dynamic-workflow-trigger-keyword-from-workflow-to-ultracode-the-word|Renamed the dynamic-workflow trigger keyword from workflow to ultracode]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-01 · Open WebUI · [[Changes/Open WebUI/2026-06-01-27-developer-workflow-changes-in-v0-9-6|27 Developer Workflow changes in v0.9.6]]
- Later: 2026-06-02 · Claude Code · [[Changes/Claude Code/2026-06-02-2-developer-workflow-changes-in-v2-1-161|2 Developer Workflow changes in v2.1.161]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-02-65dbd0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-02-2-developer-workflow-changes-in-v2-1-160.md%0ACard%20ID%3A%20claude-code-2026-06-02-65dbd0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.160%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->