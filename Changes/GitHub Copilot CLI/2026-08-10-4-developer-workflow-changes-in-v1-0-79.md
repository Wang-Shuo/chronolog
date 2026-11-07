---
card_id: github-copilot-cli-2026-08-10-d90bbe
date: '2026-08-10'
description: 'GitHub Copilot CLI · 2026-08-10 · Developer Workflow: 4 changes in 1.0.79
  — Added a `worktreeBaseRef` setting that controls whether `/worktree`, `/worktree…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2890
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 62703345ca84ec11ee3c09366c452866835038535cec3abde5089a3337ab5509
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-10-d90bbe
  comparison: ''
  date: '2026-08-10'
  description: 'GitHub Copilot CLI — 1.0.79: 4 Developer Workflow changes'
  evidence:
  - quote: Added a `worktreeBaseRef` setting that controls whether `/worktree`, `/worktree
      new`, and `--worktree` start from HEAD or the remote default branch. All three
      now default to HEAD; previously `--worktree` started from the remote default
      branch.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: '`/theme` now only shows its deprecation notice for a valid color mode,
      so a mistyped mode no longer suggests an invalid command or hides the notice
      from your next valid `/theme`.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Use `/worktree new` to start a new session in a new worktree
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  - quote: Queue prompts, shell commands, and supported slash commands in local sessions
      to run in order after the current task finishes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.79
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-developer-workflow-changes-in-v1-0-79
  source_release: github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v1.0.79
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-07-added-a-cancel-and-confirm-step-when-removing-an-unavailable-paste-changes-a-com|Added
  a cancel-and-confirm step when removing an unavailable paste changes…]]'
- '[[Changes/Codex CLI/2026-08-07-15-developer-workflow-changes-in-rust-v0-147-0|15
  Developer Workflow changes in rust-v0.147.0]]'
- '[[Changes/Cline/2026-08-09-include-files-that-were-untracked-when-a-snapshot-was-taken-in-checkpoint-diffs|Include
  files that were untracked when a snapshot was taken in checkpoint diffs…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v1.0.79
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v1.0.79

**GitHub Copilot CLI** · 2026-08-10 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.79) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-10-v1-0-79-github-368051224-d4fdfd9a|1.0.79]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `worktreeBaseRef` setting that controls whether `/worktree`, `/worktree new`, and `--worktree` start from HEAD or the remote default branch. All three now default to HEAD; previously `--worktree` started from the remote default branch.

> `/theme` now only shows its deprecation notice for a valid color mode, so a mistyped mode no longer suggests an invalid command or hides the notice from your next valid `/theme`.

> Use `/worktree new` to start a new session in a new worktree

> Queue prompts, shell commands, and supported slash commands in local sessions to run in order after the current task finishes

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.79
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-10-a-failed-session-history-load-no-longer-leaves-the-timeline-permanently-empty-th|A failed session-history load no longer leaves the timeline permanently empty]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-08-10-2-interface-experience-changes-in-v1-0-79|2 Interface Experience changes in v1.0.79]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-improve-teleported-subagent-tasks-navigation-with-nested-tree-browsing-current-a|Improve teleported subagent /tasks navigation with nested tree browsing, current/all…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-08-10-2-editor-experience-changes-in-v1-0-79|2 Editor Experience changes in v1.0.79]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-10-2-mobile-and-desktop-changes-in-v1-0-79|2 Mobile and Desktop changes in v1.0.79]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-08-10-3-apps-and-integrations-changes-in-v1-0-79|3 Apps and Integrations changes in v1.0.79]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-10-compute-context-attribution-against-the-auto-resolved-model-so-token-totals-are|Compute /context attribution against the Auto-resolved model so token totals…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-08-10-11-safety-and-privacy-changes-in-v1-0-79|11 Safety and Privacy changes in v1.0.79]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-10-3-model-support-changes-in-v1-0-79|3 Model Support changes in v1.0.79]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-10-login-links-are-clickable-during-web-and-device-code-sign-in|Login links are clickable during web and device-code sign-in]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-10-2-enterprise-and-administration-changes-in-v1-0-79|2 Enterprise and Administration changes in v1.0.79]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-10-11-other-changes-in-v1-0-79|11 other changes in v1.0.79]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-09 · Cline · [[Changes/Cline/2026-08-09-include-files-that-were-untracked-when-a-snapshot-was-taken-in-checkpoint-diffs|Include files that were untracked when a snapshot was taken in checkpoint diffs…]]
- Later: 2026-08-11 · Gemini CLI · [[Changes/Gemini CLI/2026-08-11-4-developer-workflow-changes-in-v0-55-1|4 Developer Workflow changes in v0.55.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-10-d90bbe&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-10-4-developer-workflow-changes-in-v1-0-79.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-10-d90bbe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.79%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->