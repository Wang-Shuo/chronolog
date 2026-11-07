---
card_id: claude-code-2026-05-22-7017bd
date: '2026-05-22'
description: 'Claude Code · 2026-05-22 · Safety and Privacy: 2 changes in v2.1.149
  — Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`,
  `cd~`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1132
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4c5448d41b0e4a317ad30460ce69bfc87e98fc45921e9244089f4239ee0ba090
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-22-7017bd
  comparison: ''
  date: '2026-05-22'
  description: 'Claude Code — v2.1.149: 2 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`,
      `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later
      command read outside the workspace'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.149
  - quote: Fixed a permission-analysis gap where the parser trusted stale variable-tracking
      values for `PWD`/`OLDPWD`/`DIRSTACK` across `cd`/`pushd`/`popd`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.149
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-149
  source_release: claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.149
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-20-core-invalid-opencode-permission-json-no-longer-crashes-startup|Core
  Invalid OPENCODE_PERMISSION JSON no longer crashes startup]]'
- '[[Changes/Claude/2026-05-21-claude-now-works-with-more-security-and-compliance-tools|Claude
  now works with more security and compliance tools]]'
- '[[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17
  Safety and Privacy changes in rust-v0.133.0]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f|claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.149
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.149

**Claude Code** · 2026-05-22 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.149) · from [[Releases/Claude Code/claude-code-2026-05-22-v2-1-149-github-328077450-086ee33f|v2.1.149]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later command read outside the workspace

> Fixed a permission-analysis gap where the parser trusted stale variable-tracking values for `PWD`/`OLDPWD`/`DIRSTACK` across `cd`/`pushd`/`popd`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.149
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-22-markdown-output-now-renders-gfm-task-list-checkboxes-todo-x-done-instead-of-plai|Markdown output now renders GFM task list checkboxes (-   todo / - x done)…]] · Interface Experience
- [[Changes/Claude Code/2026-05-22-improved-feedback-reports-to-include-the-conversation-that-happened-before-conte|Improved /feedback reports to include the conversation that happened before…]] · Context Window
- [[Changes/Claude Code/2026-05-22-2-apps-and-integrations-changes-in-v2-1-149|2 Apps and Integrations changes in v2.1.149]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-22-diff-detail-view-can-now-be-scrolled-with-the-keyboard-arrows-j-k-pgup-pgdn-spac|/diff detail view can now be scrolled with the keyboard…]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-21 · Codex CLI · [[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17 Safety and Privacy changes in rust-v0.133.0]]
- Later: 2026-05-22 · Gemini CLI · [[Changes/Gemini CLI/2026-05-22-docs-add-vi-mode-shortcuts-and-clarify-mcp-custom-sandbox-setup-by-chrisjcthomas|docs: add vi mode shortcuts and clarify MCP/custom sandbox setup]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-22-7017bd&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-22-2-safety-and-privacy-changes-in-v2-1-149.md%0ACard%20ID%3A%20claude-code-2026-05-22-7017bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.149%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->