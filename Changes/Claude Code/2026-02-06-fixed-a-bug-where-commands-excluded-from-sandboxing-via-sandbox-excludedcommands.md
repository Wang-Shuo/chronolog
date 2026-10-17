---
card_id: claude-code-2026-02-06-1233de
date: '2026-02-06'
description: 'Claude Code · 2026-02-06 · Safety and Privacy: Fixed a bug where commands
  excluded from sandboxing (via `sandbox.excludedCommands` or…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1027
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: fix
machine_hash: 11099edf84e61b654e1a4dd6ec02e9c1d3b802ccb55d7342ab955a9e79af9e26
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-06-1233de
  comparison: ''
  date: '2026-02-06'
  description: 'Claude Code — v2.1.34: Fixed a bug where commands excluded from sandboxing
    (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the
    Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled'
  evidence:
  - quote: Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedCommands`
      or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when
      `autoAllowBashIfSandboxed` was enabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.34
  extractor_version: fallback-v5
  impact: incremental
  kind: fix
  product: claude-code
  product_name: Claude Code
  slug: fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands
  source_release: claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed a bug where commands excluded from sandboxing…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|Fixed
  per-user temp directory isolation to prevent permission conflicts on shared systems]]'
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|Permissions
  now respect content-level ask over tool-level allow]]'
- '[[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed
  permission dialogs stealing focus while actively typing]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29|claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29]]'
source_type: github_releases
theme: safety-privacy
title: Fixed a bug where commands excluded from sandboxing…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed a bug where commands excluded from sandboxing…

**Claude Code** · 2026-02-06 · [[Themes/safety-privacy|Safety and Privacy]] · Fix · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.34) · from [[Releases/Claude Code/claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29|v2.1.34]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.34
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]]
- Later: 2026-02-10 · Claude Code · [[Changes/Claude Code/2026-02-10-2-safety-and-privacy-changes-in-v2-1-38|2 Safety and Privacy changes in v2.1.38]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-06-1233de&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-06-fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands.md%0ACard%20ID%3A%20claude-code-2026-02-06-1233de%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.34%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->