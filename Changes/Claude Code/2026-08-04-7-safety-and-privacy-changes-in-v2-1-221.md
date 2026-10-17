---
card_id: claude-code-2026-08-04-f260eb
date: '2026-08-04'
description: 'Claude Code · 2026-08-04 · Safety and Privacy: 7 changes in v2.1.221
  — Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed
  commands…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1206
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ebbcd12357239bed3d784b6996405e22de9452c934f25379d0144aca91371c52
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-04-f260eb
  comparison: ''
  date: '2026-08-04'
  description: 'Claude Code — v2.1.221: 7 Safety and Privacy changes'
  evidence:
  - quote: 'Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed
      commands read a sentinel copy (the whole file, or just the spans captured by
      an `extract` regex) while the sandbox proxy substitutes the real value on egress;
      on macOS file masking falls back to `deny`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Fixed a Bash tool permission-check bypass where zsh could execute hidden
      commands in `[[ ]]` regex conditionals; affected commands now prompt for permission
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Fixed PowerShell permission checks mishandling paths containing quote characters
      on Windows; such paths now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: 'Improved auto mode: permission checks for parallel tool calls are now
      cache-efficient, and switching modes while a check is pending reliably prompts
      instead of applying the stale result'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Reduced prompt-cache costs for auto-mode permission checks by reusing the
      cached conversation prefix across decisions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: 'Improved Windows startup: process creation times are now read via a native
      kernel32 call instead of spawning PowerShell, so endpoint security tools that
      gate `powershell.exe` no longer prompt'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Removed the repeated "Permission mode changed while the auto-mode classifier
      call was queued" notice from approval prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-safety-and-privacy-changes-in-v2-1-221
  source_release: claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in v2.1.221
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-07-23-health-is-built-with-layered-privacy-and-security-safeguards-connected-medical-r|Health
  is built with layered privacy and security safeguards]]'
- '[[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety
  and Privacy changes in v2.1.219]]'
- '[[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved
  auto mode safety]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in v2.1.221
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in v2.1.221

**Claude Code** · 2026-08-04 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.221) · from [[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|v2.1.221]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed commands read a sentinel copy (the whole file, or just the spans captured by an `extract` regex) while the sandbox proxy substitutes the real value on egress; on macOS file masking falls back to `deny`

> Fixed a Bash tool permission-check bypass where zsh could execute hidden commands in `[[ ]]` regex conditionals; affected commands now prompt for permission

> Fixed PowerShell permission checks mishandling paths containing quote characters on Windows; such paths now prompt for approval

> Improved auto mode: permission checks for parallel tool calls are now cache-efficient, and switching modes while a check is pending reliably prompts instead of applying the stale result

> Reduced prompt-cache costs for auto-mode permission checks by reusing the cached conversation prefix across decisions

> Improved Windows startup: process creation times are now read via a native kernel32 call instead of spawning PowerShell, so endpoint security tools that gate `powershell.exe` no longer prompt

> Removed the repeated "Permission mode changed while the auto-mode classifier call was queued" notice from approval prompts

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-04-improved-stats-panel-to-count-cache-tokens-in-its-token-totals-with-a-breakdown|Improved Stats panel to count cache tokens in its token totals, with a breakdown…]] · Context Window
- [[Changes/Claude Code/2026-08-04-4-apps-and-integrations-changes-in-v2-1-221|4 Apps and Integrations changes in v2.1.221]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-04-changed-emoji-autocomplete-to-accept-common-alternate-shortcodes-like-thumbsup-t|Changed emoji autocomplete to accept common alternate shortcodes like :thumbsup:…]] · Editor Experience
- [[Changes/Claude Code/2026-08-04-3-model-support-changes-in-v2-1-221|3 Model Support changes in v2.1.221]] · Model Support
- [[Changes/Claude Code/2026-08-04-vscode-added-focus-view-a-chat-menu-toggle-that-hides-tool-activity-behind-an-ex|VSCode Added Focus view]] · Interface Experience
- [[Changes/Claude Code/2026-08-04-3-developer-workflow-changes-in-v2-1-221|3 Developer Workflow changes in v2.1.221]] · Developer Workflow
- [[Changes/Claude Code/2026-08-04-changed-fast-mode-to-report-on-the-stream-when-usage-credits-run-out-mid-session|Changed fast mode to report on the stream when usage credits run out mid-session…]] · Pricing Model
- [[Changes/Claude Code/2026-08-04-3-other-changes-in-v2-1-221|3 other changes in v2.1.221]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-04 · Claude Code · [[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved auto mode safety]]
- Later: 2026-08-06 · Claude Code · [[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety and Privacy changes in v2.1.223]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-04-f260eb&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-04-7-safety-and-privacy-changes-in-v2-1-221.md%0ACard%20ID%3A%20claude-code-2026-08-04-f260eb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.221%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->