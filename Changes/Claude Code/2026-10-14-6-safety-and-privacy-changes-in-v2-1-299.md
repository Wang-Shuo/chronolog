---
card_id: claude-code-2026-10-14-e6188f
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Safety and Privacy: 6 changes in v2.1.299
  — Fixed tools of an MCP server named `constructor` or `toString` asking for permission
  in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1277
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c2a932a68f50ae5bde7d5638884b8148be1a774f71f15dfa66647c074f2d94b3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-e6188f
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.299: 6 Safety and Privacy changes'
  evidence:
  - quote: Fixed tools of an MCP server named `constructor` or `toString` asking for
      permission in auto mode and bypass permissions mode
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Fixed Claude in Chrome asking for permission while no browser is connected;
      it now says the extension is not connected
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Fixed a cloud session sometimes ignoring the answer to a permission prompt
      or a question when the answer was given while the session's worker was being
      replaced
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Fixed Enter answering a question or permission prompt that had been held
      back while you typed an unsent message
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Fixed permission prompts cutting off or wrapping too early when the reason
      text contains keycap or joined emoji
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  - quote: Improved enforcement of managed permission rules, managed hooks and organization
      MCP tool names against user-installed mods
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-299
  source_release: claude-code-2026-10-14-v2-1-299-github-412217284-623d9162
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.299
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety
  and Privacy changes in v2.1.296]]'
- '[[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security|Origin
  now integrates with over 20 apps for deployments, CI, code review, security…]]'
- '[[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety
  and Privacy changes in v2.1.300]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|claude-code-2026-10-14-v2-1-299-github-412217284-623d9162]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.299
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.299

**Claude Code** · 2026-10-14 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.299) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-299-github-412217284-623d9162|v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed tools of an MCP server named `constructor` or `toString` asking for permission in auto mode and bypass permissions mode

> Fixed Claude in Chrome asking for permission while no browser is connected; it now says the extension is not connected

> Fixed a cloud session sometimes ignoring the answer to a permission prompt or a question when the answer was given while the session's worker was being replaced

> Fixed Enter answering a question or permission prompt that had been held back while you typed an unsent message

> Fixed permission prompts cutting off or wrapping too early when the reason text contains keycap or joined emoji

> Improved enforcement of managed permission rules, managed hooks and organization MCP tool names against user-installed mods

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.299
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-added-a-one-time-note-when-plan-mode-won-t-ask-before-most-edits-or-commands-bec|Added a one-time note when plan mode won't ask before most edits or commands because…]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19 Apps and Integrations changes in v2.1.299]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-14-2-context-window-changes-in-v2-1-299|2 Context Window changes in v2.1.299]] · Context Window
- [[Changes/Claude Code/2026-10-14-10-developer-workflow-changes-in-v2-1-299|10 Developer Workflow changes in v2.1.299]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-model-support-changes-in-v2-1-299|2 Model Support changes in v2.1.299]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-files-and-data-changes-in-v2-1-299|2 Files and Data changes in v2.1.299]] · Files and Data
- [[Changes/Claude Code/2026-10-14-added-support-for-turning-off-the-attribution-block-in-claude-desktop-s-code-tab|Added support for turning off the attribution block in Claude Desktop's Code tab]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-14-5-agent-mode-changes-in-v2-1-299|5 Agent Mode changes in v2.1.299]] · Agent Mode
- [[Changes/Claude Code/2026-10-14-added-effort-and-fast-in-agent-view-to-set-what-new-sessions-start-with-a-bare-m|Added /effort and /fast in agent view to set what new sessions start with]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-improved-memory-and-disk-use-when-pdfs-are-mentioned-their-bytes-are-no-longer-k|Improved memory and disk use when PDFs are @-mentioned]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-14-added-usage-warnings-for-max-effort-workflows-always-on-context-and-large-tool-r|Added /usage warnings for max effort, workflows, always-on context and large tool…]] · Context Window
- [[Changes/Claude Code/2026-10-14-improved-the-error-shown-when-a-cloud-session-is-refused-because-your-claude-ai|Improved the error shown when a cloud session is refused because your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-14-vscode-improved-startup-the-model-picker-and-slash-command-menu-now-fill-in-righ|VSCode Improved startup]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-11-other-changes-in-v2-1-299|11 other changes in v2.1.299]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]]
- Later: 2026-10-15 · Claude Code · [[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety and Privacy changes in v2.1.301]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-e6188f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-6-safety-and-privacy-changes-in-v2-1-299.md%0ACard%20ID%3A%20claude-code-2026-10-14-e6188f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.299%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->