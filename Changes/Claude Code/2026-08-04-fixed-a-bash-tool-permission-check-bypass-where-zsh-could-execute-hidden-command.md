---
card_id: claude-code-2026-08-04-965dd1
date: '2026-08-04'
description: 'Claude Code · 2026-08-04 · Safety and Privacy: Fixed a Bash tool permission-check
  bypass where zsh could execute hidden commands in `[[ ]]` regex conditionals…'
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
extractor_version: fallback-v4
impact: incremental
machine_hash: c3176a2cad21b69b45984324a4464a7dc4e5e21e4051b033c5fcca3ba45f8d09
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-04-965dd1
  comparison: ''
  date: '2026-08-04'
  description: 'Claude Code — v2.1.221: Fixed a Bash tool permission-check bypass
    where zsh could execute hidden commands in `[[ ]]` regex conditionals; affected
    commands now prompt for permission'
  evidence:
  - quote: Fixed a Bash tool permission-check bypass where zsh could execute hidden
      commands in `[[ ]]` regex conditionals; affected commands now prompt for permission
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-a-bash-tool-permission-check-bypass-where-zsh-could-execute-hidden-command
  source_release: claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed a Bash tool permission-check bypass where zsh could execute hidden
    commands…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-24-added-sandbox-network-strictallowlist-setting-to-deny-non-allowlisted-hosts-for|Added
  sandbox.network.strictAllowlist setting to deny non-allowlisted hosts…]]'
- '[[Changes/Claude Code/2026-08-04-added-mode-mask-for-sandbox-credential-files-on-linux-and-wsl-sandboxed-commands|Added
  mode: "mask" for sandbox credential files on Linux and WSL]]'
- '[[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved
  auto mode safety]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce]]'
source_type: github_releases
theme: safety-privacy
title: Fixed a Bash tool permission-check bypass where zsh could execute hidden commands…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed a Bash tool permission-check bypass where zsh could execute hidden commands…

**Claude Code** · 2026-08-04 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.221) · from [[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|v2.1.221]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a Bash tool permission-check bypass where zsh could execute hidden commands in `[[ ]]` regex conditionals; affected commands now prompt for permission
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-04-added-mode-mask-for-sandbox-credential-files-on-linux-and-wsl-sandboxed-commands|Added mode: "mask" for sandbox credential files on Linux and WSL]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-04-added-a-prompt-audit-subcommand-to-the-claude-api-skill-for-auditing-prompts-and|Added a prompt-audit subcommand to the claude-api skill for auditing prompts…]] · Model Support
- [[Changes/Claude Code/2026-08-04-vscode-added-focus-view-a-chat-menu-toggle-that-hides-tool-activity-behind-an-ex|VSCode Added Focus view]] · Interface Experience
- [[Changes/Claude Code/2026-08-04-added-warnings-to-claude-plugin-validate-when-a-marketplace-or-plugin-name-would|Added warnings to claude plugin validate when a marketplace or plugin name would…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-04 · Claude Code · [[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved auto mode safety]]
- Later: 2026-08-06 · Claude Code · [[Changes/Claude Code/2026-08-06-fixed-a-bash-permission-bypass-where-a-crafted-command-could-hide-parts-of-itsel|Fixed a Bash permission bypass where a crafted command could hide parts of itself…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-04-965dd1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-04-fixed-a-bash-tool-permission-check-bypass-where-zsh-could-execute-hidden-command.md%0ACard%20ID%3A%20claude-code-2026-08-04-965dd1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.221%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->