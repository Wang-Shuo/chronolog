---
card_id: claude-code-2026-05-07-6fb4d0
date: '2026-05-07'
description: 'Claude Code · 2026-05-07 · Developer Workflow: Added `worktree.baseRef`
  setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1146
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: b38b16091534b375a8b16e4296eb974e375ad8c9a5c12ec9adc1ef965218b2fd
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-05-07-6fb4d0
  comparison: ''
  confidence: low
  date: '2026-05-07'
  description: 'Claude Code — v2.1.133: Added `worktree.baseRef` setting (`fresh`
    | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation
    worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default
    `fresh` changes `EnterWorktree`''s base back to `origin/<default>` (it has been
    local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed
    commits in new worktrees'
  evidence:
  - quote: 'Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether
      `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>`
      or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`''s base
      back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef:
      "head"` to keep unpushed commits in new worktrees'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-worktree-baseref-setting-fresh-head-to-choose-whether-worktree-enterworktr
  source_release: claude-code-2026-05-07-v2-1-133-github-319164825-08653677
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - worktree
    score: 50
    theme: developer-workflow
  theme_resolution: manual-semantic-rule-v1
  title: Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-added-prurltemplate-setting-to-point-the-footer-pr-badge-at-a-custom-code-review|Added
  prUrlTemplate setting to point the footer PR badge at a custom code-review…]]'
- '[[Changes/Claude Code/2026-04-28-opentelemetry-added-claude-code-at-mention-log-event-for-mention-resolution|OpenTelemetry:
  added claude_code.at_mention log event for @-mention resolution]]'
- '[[Changes/Claude Code/2026-05-06-added-claude-code-package-manager-auto-update-when-set-on-homebrew-or-winget-ins|Added
  CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE: when set on Homebrew or WinGet…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|claude-code-2026-05-07-v2-1-133-github-319164825-08653677]]'
source_type: github_releases
theme: developer-workflow
title: Added worktree.baseRef setting (fresh  /  head) to choose whether --worktree…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`…

**Claude Code** · 2026-05-07 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.133) · from [[Releases/Claude Code/claude-code-2026-05-07-v2-1-133-github-319164825-08653677|v2.1.133]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `worktree.baseRef` setting (`fresh` | `head`) to choose whether `--worktree`, `EnterWorktree`, and agent-isolation worktrees branch from `origin/<default>` or local `HEAD`. **Note:** the default `fresh` changes `EnterWorktree`'s base back to `origin/<default>` (it has been local `HEAD` since 2.1.128) — set `worktree.baseRef: "head"` to keep unpushed commits in new worktrees
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.133
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-07-hooks-now-receive-the-active-effort-level-via-the-effort-level-json-input-field|Hooks now receive the active effort level via the effort.level JSON input field…]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-07-improved-focus-mode-behavior|Improved focus mode behavior]] · Interface Experience
- [[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-07-added-parentsettingsbehavior-admin-tier-key-first-wins-merge-to-let-admins-opt-s|Added parentSettingsBehavior admin-tier key ('first-wins'  /  'merge') to let…]] · Enterprise and Administration
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-06 · Claude Code · [[Changes/Claude Code/2026-05-06-added-claude-code-package-manager-auto-update-when-set-on-homebrew-or-winget-ins|Added CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE: when set on Homebrew or WinGet…]]
- Later: 2026-05-07 · Cursor · [[Changes/Cursor/2026-05-07-a-new-pr-review-experience-is-now-available-in-cursor-3-take-prs-from-creation-t|A new PR review experience is now available in Cursor 3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-07-6fb4d0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-07-added-worktree-baseref-setting-fresh-head-to-choose-whether-worktree-enterworktr.md%0ACard%20ID%3A%20claude-code-2026-05-07-6fb4d0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.133%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->