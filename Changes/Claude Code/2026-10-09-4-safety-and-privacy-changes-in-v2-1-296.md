---
card_id: claude-code-2026-10-09-52b83d
date: '2026-10-09'
description: 'Claude Code · 2026-10-09 · Safety and Privacy: 4 changes in v2.1.296
  — Fixed cloud sessions skipping auto mode''s checks on Claude in Chrome actions
  that a…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2264
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a1b15a37a1af6e1d7d37fce224327c091672de3067f5d27fe4f2d76900b9e62c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-09-52b83d
  comparison: ''
  date: '2026-10-09'
  description: 'Claude Code — v2.1.296: 4 Safety and Privacy changes'
  evidence:
  - quote: Fixed cloud sessions skipping auto mode's checks on Claude in Chrome actions
      that a saved permission allows when their feature flags had not loaded
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: Fixed Bash permission checks auto-approving some commands that assign the
      `BASH_ARGV0` shell variable and then use it; these now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: 'Windows: Fixed PowerShell commands longer than about 1 KB always asking
      for permission, so allow rules and read-only detection now apply up to 32 KB'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  - quote: '[Claude Tag] Added creating, editing and deleting workspace and channel
      memory files on the Activity page''s Memory tab for members with the Claude
      Tag Admin permission'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-296
  source_release: claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.296
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0|13
  Safety and Privacy changes in rust-v0.162.0]]'
- '[[Changes/GitHub Copilot CLI/2026-10-08-2-safety-and-privacy-changes-in-v1-0-94|2
  Safety and Privacy changes in v1.0.94]]'
- '[[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows
  MXC sandbox]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.296
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.296

**Claude Code** · 2026-10-09 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) · from [[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed cloud sessions skipping auto mode's checks on Claude in Chrome actions that a saved permission allows when their feature flags had not loaded

> Fixed Bash permission checks auto-approving some commands that assign the `BASH_ARGV0` shell variable and then use it; these now prompt for approval

> Windows: Fixed PowerShell commands longer than about 1 KB always asking for permission, so allow rules and read-only detection now apply up to 32 KB

> [Claude Tag] Added creating, editing and deleting workspace and channel memory files on the Activity page's Memory tab for members with the Claude Tag Admin permission

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.296
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-09-3-editor-experience-changes-in-v2-1-296|3 Editor Experience changes in v2.1.296]] · Editor Experience
- [[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer Workflow changes in v2.1.296]] · Developer Workflow
- [[Changes/Claude Code/2026-10-09-improved-transcript-toggle-ctrl-o-responsiveness-in-code-heavy-conversations-by|Improved transcript toggle (ctrl+o) responsiveness in code-heavy conversations…]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-09-2-context-window-changes-in-v2-1-296|2 Context Window changes in v2.1.296]] · Context Window
- [[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode changes in v2.1.296]] · Agent Mode
- [[Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price|Updated /cost, the status line, --max-budget-usd and the SDK's cost figures…]] · Pricing Model
- [[Changes/Claude Code/2026-10-09-improved-the-errors-for-a-refused-cloud-session-they-now-say-why-your-organizati|Improved the errors for a refused cloud session]] · Account and Access
- [[Changes/Claude Code/2026-10-09-improved-fullscreen-mode-the-link-under-the-mouse-pointer-is-now-underlined-to-s|Improved fullscreen mode]] · Interface Experience
- [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]] · Model Support
- [[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3 Apps and Integrations changes in v2.1.296]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-09-3-other-changes-in-v2-1-296|3 other changes in v2.1.296]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-08 · OpenClaw · [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]]
- Later: 2026-10-09 · Devin · [[Changes/Devin/2026-10-09-create-scan-and-create-profile-with-devin|Create scan and Create profile with Devin]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-09-52b83d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-09-4-safety-and-privacy-changes-in-v2-1-296.md%0ACard%20ID%3A%20claude-code-2026-10-09-52b83d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.296%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->