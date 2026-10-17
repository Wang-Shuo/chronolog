---
card_id: claude-code-2026-05-15-db12a3
date: '2026-05-15'
description: 'Claude Code · 2026-05-15 · Developer Workflow: 2 changes in v2.1.143
  — Added `worktree.bgIsolation: "none"` setting to let background sessions edit the
  working…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1154
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2c132139bee9aab4c226fe094f44ae8bc0e9f2a5167ebfe9ce793fb30407b457
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-15-db12a3
  comparison: ''
  date: '2026-05-15'
  description: 'Claude Code — v2.1.143: 2 Developer Workflow changes'
  evidence:
  - quote: 'Added `worktree.bgIsolation: "none"` setting to let background sessions
      edit the working copy directly without `EnterWorktree`, for repos where worktrees
      are impractical'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  - quote: Worktree cleanup no longer falls back to `rm -rf` when `git worktree remove`
      fails, preventing loss of gitignored or in-progress files
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-developer-workflow-changes-in-v2-1-143
  source_release: claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v2.1.143
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-11-added-hook-args-string-field-exec-form-that-spawns-the-command-directly-without|Added
  hook args: string field (exec form) that spawns the command directly…]]'
- '[[Changes/Cursor/2026-05-13-environment-configuration-as-code-827fd1|Environment
  configuration as code]]'
- '[[Changes/Cursor/2026-05-13-removed-noisy-in-app-terminal-notifications-and-improved-shortcut-behavior|Removed
  noisy in-app terminal notifications and improved shortcut behavior]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v2.1.143
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v2.1.143

**Claude Code** · 2026-05-15 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.143) · from [[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|v2.1.143]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `worktree.bgIsolation: "none"` setting to let background sessions edit the working copy directly without `EnterWorktree`, for repos where worktrees are impractical

> Worktree cleanup no longer falls back to `rm -rf` when `git worktree remove` fails, preventing loss of gitignored or in-progress files

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-15-bg-and-detach-now-preserve-allow-dangerously-skip-permissions-so-the-forked-work|/bg and ←-detach now preserve --allow-dangerously-skip-permissions…]] · Editor Experience
- [[Changes/Claude Code/2026-05-15-3-safety-and-privacy-changes-in-v2-1-143|3 Safety and Privacy changes in v2.1.143]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-15-the-powershell-tool-is-now-enabled-by-default-on-windows-for-bedrock-vertex-and|The PowerShell tool is now enabled by default on Windows for Bedrock, Vertex…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-05-15-3-apps-and-integrations-changes-in-v2-1-143|3 Apps and Integrations changes in v2.1.143]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-15-2-model-support-changes-in-v2-1-143|2 Model Support changes in v2.1.143]] · Model Support
- [[Changes/Claude Code/2026-05-15-2-agent-mode-changes-in-v2-1-143|2 Agent Mode changes in v2.1.143]] · Agent Mode
- [[Changes/Claude Code/2026-05-15-added-projected-context-cost-per-turn-and-per-invocation-token-estimates-to-the|Added projected context cost (per-turn and per-invocation token estimates)…]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-13 · Cursor · [[Changes/Cursor/2026-05-13-removed-noisy-in-app-terminal-notifications-and-improved-shortcut-behavior|Removed noisy in-app terminal notifications and improved shortcut behavior]]
- Later: 2026-05-19 · Claude Code · [[Changes/Claude Code/2026-05-19-3-developer-workflow-changes-in-v2-1-144|3 Developer Workflow changes in v2.1.144]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-15-db12a3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-15-2-developer-workflow-changes-in-v2-1-143.md%0ACard%20ID%3A%20claude-code-2026-05-15-db12a3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.143%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->