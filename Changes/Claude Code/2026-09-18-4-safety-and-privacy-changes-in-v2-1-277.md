---
card_id: claude-code-2026-09-18-62db2f
date: '2026-09-18'
description: 'Claude Code · 2026-09-18 · Safety and Privacy: 4 changes in v2.1.277
  — Fixed the Write tool silently ending the turn as a declined permission when the
  target…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1251
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 35088d2b99f1978a3fe71cdf77edb0214ad5f50e1ce01adec799cf8681f332ac
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-18-62db2f
  comparison: ''
  date: '2026-09-18'
  description: 'Claude Code — v2.1.277: 4 Safety and Privacy changes'
  evidence:
  - quote: Fixed the Write tool silently ending the turn as a declined permission
      when the target path is an existing directory; it now reports a clear error
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: Improved the dangerous-rm permission prompt to name the flagged rm command
      and suggest a `${VAR:?}` guard, so headless runs can recover
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: 'Improved the Artifact tool''s permission prompts: shorter sentences, pages
      and artifacts named by title or file name, and links listed after the text'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  - quote: Changed the Bash sandbox instructions on Bedrock, Vertex and Foundry to
      the first-party wording, which frames the sandbox as the boundary of what the
      task was given
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-safety-and-privacy-changes-in-v2-1-277
  source_release: claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in v2.1.277
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety
  and Privacy changes in v2.1.273]]'
- '[[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety
  and Privacy changes in v2.1.275]]'
- '[[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety
  and Privacy changes in v2.1.274]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36|claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in v2.1.277
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in v2.1.277

**Claude Code** · 2026-09-18 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.277) · from [[Releases/Claude Code/claude-code-2026-09-18-v2-1-277-github-391616593-06a20f36|v2.1.277]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed the Write tool silently ending the turn as a declined permission when the target path is an existing directory; it now reports a clear error

> Improved the dangerous-rm permission prompt to name the flagged rm command and suggest a `${VAR:?}` guard, so headless runs can recover

> Improved the Artifact tool's permission prompts: shorter sentences, pages and artifacts named by title or file name, and links listed after the text

> Changed the Bash sandbox instructions on Bedrock, Vertex and Foundry to the first-party wording, which frames the sandbox as the boundary of what the task was given

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.277
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-18-3-enterprise-and-administration-changes-in-v2-1-277|3 Enterprise and Administration changes in v2.1.277]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-18-changed-ultrareview-in-non-interactive-sessions-to-refuse-when-the-repository-ha|Changed /ultrareview in non-interactive sessions to refuse when the repository has…]] · Collaboration
- [[Changes/Claude Code/2026-09-18-vscode-added-the-session-s-cost-and-token-usage-to-the-account-usage-dialog-and|VSCode Added the session's cost and token usage to the Account & usage dialog…]] · Pricing Model
- [[Changes/Claude Code/2026-09-18-removed-the-background-haiku-auto-title-request-from-claude-p-runs-launched-outs|Removed the background Haiku auto-title request from claude -p runs launched…]] · Editor Experience
- [[Changes/Claude Code/2026-09-18-vscode-added-a-sign-out-row-to-the-panel-menu-with-logout-in-the-typed-command-m|VSCode Added a Sign out row to the panel menu, with /logout in the typed command menu]] · Interface Experience
- [[Changes/Claude Code/2026-09-18-improved-ultrareview-when-there-s-nothing-to-review-messages-say-which-case-you|Improved /ultrareview when there's nothing to review]] · Developer Workflow
- [[Changes/Claude Code/2026-09-18-6-apps-and-integrations-changes-in-v2-1-277|6 Apps and Integrations changes in v2.1.277]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-18-claude-code-on-the-web-changed-the-admin-claude-code-setting-labeled-web-to-clou|Claude Code on the web Changed the admin Claude Code setting labeled…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-18-4-agent-mode-changes-in-v2-1-277|4 Agent Mode changes in v2.1.277]] · Agent Mode
- [[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed Fable to always appear in /model on the Anthropic API]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]]
- Later: 2026-09-21 · ChatGPT · [[Changes/ChatGPT/2026-09-21-privacy-center-is-rolling-out-to-signed-in-chatgpt-free-go-plus-and-pro-users-it-0d2f36|Privacy Center in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-18-62db2f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-18-4-safety-and-privacy-changes-in-v2-1-277.md%0ACard%20ID%3A%20claude-code-2026-09-18-62db2f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.277%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->