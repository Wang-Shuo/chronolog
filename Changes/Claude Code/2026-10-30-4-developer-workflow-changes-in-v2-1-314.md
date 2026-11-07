---
card_id: claude-code-2026-10-30-686d6f
date: '2026-10-30'
description: 'Claude Code · 2026-10-30 · Developer Workflow: 4 changes in v2.1.314
  — Self-hosted runner: Improved the error shown when a session''s branch isn''t on
  the git…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1322
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 936464c1cc6d6d6168e4119ba16ec370a20b97726bd93af0cdd69266dc5f2deb
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-30-686d6f
  comparison: ''
  date: '2026-10-30'
  description: 'Claude Code — v2.1.314: 4 Developer Workflow changes'
  evidence:
  - quote: 'Self-hosted runner: Improved the error shown when a session''s branch
      isn''t on the git remote: it now covers a never-pushed branch, says how to fix
      each case, and no longer suggests retrying'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Changed the Bash tool's shell to clear any inherited `which` alias or function
      and to stop passing exported `which`/`unsetenv` functions to commands, so `which`
      is the system command or zsh builtin
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Changed `/permissions` Recently blocked to refuse approving a call you
      can't read in full, including one the terminal is too short to show
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  - quote: Changed hook `if` conditions such as `Monitor(tail *)` to match the Monitor
      tool's shell commands as `Bash(tail *)` matches Bash's
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-developer-workflow-changes-in-v2-1-314
  source_release: claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7
  source_type: github_releases
  theme: developer-workflow
  title: 4 Developer Workflow changes in v2.1.314
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-29-2-developer-workflow-changes-in-v2026-10-9|2 Developer
  Workflow changes in v2026.10.9]]'
- '[[Changes/OpenCode/2026-10-29-5-developer-workflow-changes-in-v2-2-2|5 Developer
  Workflow changes in v2.2.2]]'
- '[[Changes/OpenCode/2026-10-29-5-developer-workflow-changes-in-v2-2-1|5 Developer
  Workflow changes in v2.2.1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7]]'
source_type: github_releases
theme: developer-workflow
title: 4 Developer Workflow changes in v2.1.314
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Developer Workflow changes in v2.1.314

**Claude Code** · 2026-10-30 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.314) · from [[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Self-hosted runner: Improved the error shown when a session's branch isn't on the git remote: it now covers a never-pushed branch, says how to fix each case, and no longer suggests retrying

> Changed the Bash tool's shell to clear any inherited `which` alias or function and to stop passing exported `which`/`unsetenv` functions to commands, so `which` is the system command or zsh builtin

> Changed `/permissions` Recently blocked to refuse approving a call you can't read in full, including one the terminal is too short to show

> Changed hook `if` conditions such as `Monitor(tail *)` to match the Monitor tool's shell commands as `Bash(tail *)` matches Bash's

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-30-3-agent-mode-changes-in-v2-1-314|3 Agent Mode changes in v2.1.314]] · Agent Mode
- [[Changes/Claude Code/2026-10-30-3-reliability-and-performance-changes-in-v2-1-314|3 Reliability and Performance changes in v2.1.314]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-30-3-enterprise-and-administration-changes-in-v2-1-314|3 Enterprise and Administration changes in v2.1.314]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-30-2-model-support-changes-in-v2-1-314|2 Model Support changes in v2.1.314]] · Model Support
- [[Changes/Claude Code/2026-10-30-improved-the-cloud-session-error-shown-while-a-request-refused-for-your-claude-a|Improved the cloud session error shown while a request refused for your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety and Privacy changes in v2.1.314]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-30-2-mobile-and-desktop-changes-in-v2-1-314|2 Mobile and Desktop changes in v2.1.314]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-30-2-editor-experience-changes-in-v2-1-314|2 Editor Experience changes in v2.1.314]] · Editor Experience
- [[Changes/Claude Code/2026-10-30-10-other-changes-in-v2-1-314|10 other changes in v2.1.314]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-29 · OpenCode · [[Changes/OpenCode/2026-10-29-5-developer-workflow-changes-in-v2-2-1|5 Developer Workflow changes in v2.2.1]]
- Later: 2026-10-30 · OpenCode · [[Changes/OpenCode/2026-10-30-worktree-and-shell-mode-shortcuts|Worktree and Shell Mode Shortcuts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-30-686d6f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-30-4-developer-workflow-changes-in-v2-1-314.md%0ACard%20ID%3A%20claude-code-2026-10-30-686d6f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.314%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->