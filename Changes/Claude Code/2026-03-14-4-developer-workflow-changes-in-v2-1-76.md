---
card_id: claude-code-2026-03-14-88e225
date: '2026-03-14'
description: 'Claude Code · 2026-03-14 · Developer Workflow: 4 changes in v2.1.76
  — Added `worktree.sparsePaths` setting for `claude --worktree` in large monorepos
  to check…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1092
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ae5f395930966acb07c872f1b24c574d04d9a34941587048130bb0cadff5727c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-14-88e225
  comparison: ''
  date: '2026-03-14'
  description: 'Claude Code — v2.1.76: 4 Developer Workflow changes'
  evidence:
  - quote: Added `worktree.sparsePaths` setting for `claude --worktree` in large monorepos
      to check out only the directories you need via git sparse-checkout
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  - quote: Improved `--worktree` startup performance by reading git refs directly
      and skipping redundant `git fetch` when the remote branch is already available
      locally
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  - quote: Improved blockquote readability on dark terminal themes — text is now italic
      with a left bar instead of dim
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  - quote: Improved stale worktree cleanup — worktrees left behind after an interrupted
      parallel run are now automatically cleaned up
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-developer-workflow-changes-in-v2-1-76
  source_release: claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v2.1.76
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-10-3-developer-workflow-changes-in-v2-1-72|3 Developer
  Workflow changes in v2.1.72]]'
- '[[Changes/Claude Code/2026-03-11-deprecated-output-style-command-use-config-instead-output-style-is-now-fixed-at|Deprecated
  /output-style command — use /config instead]]'
- '[[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|VSCode
  Improved scroll wheel responsiveness in the integrated terminal…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc|claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v2.1.76
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v2.1.76

**Claude Code** · 2026-03-14 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.76) · from [[Releases/Claude Code/claude-code-2026-03-14-v2-1-76-github-296929324-94cd2ffc|v2.1.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `worktree.sparsePaths` setting for `claude --worktree` in large monorepos to check out only the directories you need via git sparse-checkout

> Improved `--worktree` startup performance by reading git refs directly and skipping redundant `git fetch` when the remote branch is already available locally

> Improved blockquote readability on dark terminal themes — text is now italic with a left bar instead of dim

> Improved stale worktree cleanup — worktrees left behind after an interrupted parallel run are now automatically cleaned up

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.76
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-14-added-session-quality-survey-enterprise-admins-can-configure-the-sample-rate-via|Added session quality survey]] · Enterprise and Administration
- [[Changes/Claude Code/2026-03-14-added-effort-slash-command-to-set-model-effort-level|Added /effort slash command to set model effort level]] · Model Support
- [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-14-added-postcompact-hook-that-fires-after-compaction-completes|Added PostCompact hook that fires after compaction completes]] · Context Window
- [[Changes/Claude Code/2026-03-14-added-n-name-name-cli-flag-to-set-a-display-name-for-the-session-at-startup|Added -n / --name name CLI flag to set a display name for the session at startup]] · Projects and Workspaces
- [[Changes/Claude Code/2026-03-14-improved-voice-to-show-your-dictation-language-on-enable-and-warn-when-your-lang|Improved /voice to show your dictation language on enable and warn…]] · Voice and Audio
- [[Changes/Claude Code/2026-03-14-improved-background-agent-behavior-killing-a-background-agent-now-preserves-its|Improved background agent behavior]] · Agent Mode
- [[Changes/Claude Code/2026-03-14-improved-model-fallback-notifications-now-always-visible-instead-of-hidden-behin|Improved model fallback notifications]] · Model Support
- [[Changes/Claude Code/2026-03-14-4-apps-and-integrations-changes-in-v2-1-76|4 Apps and Integrations changes in v2.1.76]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-12 · Claude Code · [[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|VSCode Improved scroll wheel responsiveness in the integrated terminal…]]
- Later: 2026-03-17 · Claude Code · [[Changes/Claude Code/2026-03-17-background-bash-tasks-are-now-killed-if-output-exceeds-5gb-preventing-runaway-pr|Background bash tasks are now killed if output exceeds 5GB, preventing runaway…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-14-88e225&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-14-4-developer-workflow-changes-in-v2-1-76.md%0ACard%20ID%3A%20claude-code-2026-03-14-88e225%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.76%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->