---
card_id: claude-code-2026-08-13-c096f6
date: '2026-08-13'
description: 'Claude Code · 2026-08-13 · Safety and Privacy: 9 changes in v2.1.232
  — Added secret redaction for GitLab token families (`glrt-`, `gloas-`, `glptt-`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1215
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: da1bbd6f63ee8125483e56b500364c345fddd3a1fcf8cf1a8f4a9b74c3b86372
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-13-c096f6
  comparison: ''
  date: '2026-08-13'
  description: 'Claude Code — v2.1.232: 9 Safety and Privacy changes'
  evidence:
  - quote: Added secret redaction for GitLab token families (`glrt-`, `gloas-`, `glptt-`,
      `glagent-`, `glimt-`, `glsoat-`, `glcbt-`, `glft-`, `glffct-`) and full redaction
      of routable `glpat-`/`gldt-` tokens; the `glab` CLI config store gets the same
      sandbox and credential-path protection as `gh`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Fable 5 is offered as an advisor in `/advisor` again for organizations
      with Fable access, with usage-credits consent set up through `/model fable`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Fixed a PowerShell permission bypass where variable-writing parameters
      could silently overwrite `$PSDefaultParameterValues` and redirect later commands'
      file access
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Fixed a Windows permission bypass where Git Bash followed Cygwin-style
      symlinks that path validation saw as regular files; writes through them now
      require permission approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Fixed the consent message for interactive `--advisor fable` launches, which
      told you to run `/model fable` in an interactive session that had just exited
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: 'Improved the managed settings approval dialog: shows endpoint URLs, uses
      clearer wording for telemetry-only changes, skips routine OpenTelemetry options,
      and requires approval for server-managed sandbox binary overrides (`sandbox.bwrapPath`,
      `sandbox.socatPath`, `sandbox.ripgrep`)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Bash input redirections (`< file`) are now permission-checked like their
      argument spellings on all platforms
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Hardened the Linux filesystem sandbox against a protected-path bypass
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Changed `sandbox.ripgrep` to be honored only from user, managed, and `--settings`
      settings; project settings can no longer override the sandbox's ripgrep binary
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-safety-and-privacy-changes-in-v2-1-232
  source_release: claude-code-2026-08-13-v2-1-232-github-370225682-71e478db
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in v2.1.232
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-07-2-safety-and-privacy-changes-in-v2-1-224|2 Safety
  and Privacy changes in v2.1.224]]'
- '[[Changes/Claude Code/2026-08-08-2-safety-and-privacy-changes-in-v2-1-225|2 Safety
  and Privacy changes in v2.1.225]]'
- '[[Changes/Claude Code/2026-08-12-improved-sandbox-ipv6-literals-in-network-domain-lists-are-now-bracketed-1-443-a|Improved
  sandbox: IPv6 literals in network domain lists are now bracketed…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-13-v2-1-232-github-370225682-71e478db|claude-code-2026-08-13-v2-1-232-github-370225682-71e478db]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in v2.1.232
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in v2.1.232

**Claude Code** · 2026-08-13 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.232) · from [[Releases/Claude Code/claude-code-2026-08-13-v2-1-232-github-370225682-71e478db|v2.1.232]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added secret redaction for GitLab token families (`glrt-`, `gloas-`, `glptt-`, `glagent-`, `glimt-`, `glsoat-`, `glcbt-`, `glft-`, `glffct-`) and full redaction of routable `glpat-`/`gldt-` tokens; the `glab` CLI config store gets the same sandbox and credential-path protection as `gh`

> Fable 5 is offered as an advisor in `/advisor` again for organizations with Fable access, with usage-credits consent set up through `/model fable`

> Fixed a PowerShell permission bypass where variable-writing parameters could silently overwrite `$PSDefaultParameterValues` and redirect later commands' file access

> Fixed a Windows permission bypass where Git Bash followed Cygwin-style symlinks that path validation saw as regular files; writes through them now require permission approval

> Fixed the consent message for interactive `--advisor fable` launches, which told you to run `/model fable` in an interactive session that had just exited

> Improved the managed settings approval dialog: shows endpoint URLs, uses clearer wording for telemetry-only changes, skips routine OpenTelemetry options, and requires approval for server-managed sandbox binary overrides (`sandbox.bwrapPath`, `sandbox.socatPath`, `sandbox.ripgrep`)

> Bash input redirections (`< file`) are now permission-checked like their argument spellings on all platforms

> Hardened the Linux filesystem sandbox against a protected-path bypass

> Changed `sandbox.ripgrep` to be honored only from user, managed, and `--settings` settings; project settings can no longer override the sandbox's ripgrep binary

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-13-enterprise-policy-a-url-typed-blockedmarketplaces-entry-for-a-bare-repo-url-keep|Enterprise policy: a url-typed blockedMarketplaces entry for a bare repo URL keeps…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-13-4-apps-and-integrations-changes-in-v2-1-232|4 Apps and Integrations changes in v2.1.232]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-13-improved-fullscreen-streaming-long-sessions-stay-responsive-because-the-whole-co|Improved fullscreen streaming]] · Interface Experience
- [[Changes/Claude Code/2026-08-13-4-agent-mode-changes-in-v2-1-232|4 Agent Mode changes in v2.1.232]] · Agent Mode
- [[Changes/Claude Code/2026-08-13-remote-control-resuming-a-conversation-whose-session-was-deleted-from-claude-ai|Remote Control: resuming a conversation whose session was deleted from claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-08-13-cowork-sessions-no-longer-inline-external-imports-from-user-scope-memory-files|Cowork sessions no longer inline external @-imports from user-scope memory files]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-13-hardened-the-auto-generated-cross-session-messaging-socket-directory-on-shared-t|Hardened the auto-generated cross-session messaging socket directory on shared /tmp]] · Collaboration
- [[Changes/Claude Code/2026-08-13-gateway-the-desktop-overlay-now-accepts-every-released-desktop-setting-was-11-ha|Gateway: the desktop: overlay now accepts every released Desktop setting…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the|Subagent forking is now on by default]] · Agent Mode
- [[Changes/Claude Code/2026-08-13-remote-control-the-terminal-now-says-whether-a-session-was-taken-over-by-another|Remote Control: the terminal now says whether a session was taken over by another…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-13-pasted-and-clipboard-images-are-read-without-blocking-the-event-loop|Pasted and clipboard images are read without blocking the event loop]] · Automation and Scheduling
- [[Changes/Claude Code/2026-08-13-added-config-rows-for-dialog-expiry-and-messages-from-your-other-sessions-cross|Added /config rows…]] · Other changes
- [[Changes/Claude Code/2026-08-13-5-other-changes-in-v2-1-232|5 other changes in v2.1.232]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-12 · Claude Code · [[Changes/Claude Code/2026-08-12-improved-sandbox-ipv6-literals-in-network-domain-lists-are-now-bracketed-1-443-a|Improved sandbox: IPv6 literals in network domain lists are now bracketed…]]
- Later: 2026-08-14 · Claude Code · [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-13-c096f6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-13-9-safety-and-privacy-changes-in-v2-1-232.md%0ACard%20ID%3A%20claude-code-2026-08-13-c096f6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.232%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->