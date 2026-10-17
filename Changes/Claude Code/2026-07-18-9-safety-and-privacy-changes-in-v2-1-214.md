---
card_id: claude-code-2026-07-18-832703
date: '2026-07-18'
description: 'Claude Code · 2026-07-18 · Safety and Privacy: 9 changes in v2.1.214
  — Fixed a permission-check bypass affecting commands run in Windows PowerShell 5.1
  sessions'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1189
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c203f69250859d41db600f7b0cd1645f653b756b24469a213930ecc5c3e7362e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-07-18-832703
  comparison: ''
  date: '2026-07-18'
  description: 'Claude Code — v2.1.214: 9 Safety and Privacy changes'
  evidence:
  - quote: Fixed a permission-check bypass affecting commands run in Windows PowerShell
      5.1 sessions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Fixed Bash permission checks to fail closed on file-descriptor redirect
      forms that bash parses differently than the permission analyzer
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Fixed Bash permission checks misjudging very long commands — commands over
      10,000 characters now always prompt instead of running automatically
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Fixed Bash permission checks treating zsh variable subscripts and modifiers
      in `[[ ]]` comparisons as inert text — these commands now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Fixed Bash permission checks to no longer auto-approve certain `help` and
      `man` commands that could run unsafe options, command substitutions, or backslash
      paths
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Fixed permission prompts on remote sessions that could proceed before the
      local confirmation dialog
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Added permission prompts for `docker` commands (including the Podman `docker`
      shim) carrying daemon-redirect flags (`--url`, `--connection`, `--identity`,
      and Podman's remote mode) that previously ran without one
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Changed single-segment `dir/**` hook `if:` conditions to match only `<cwd>/dir`;
      write `**/dir/**` for any-depth matching. `deny`/`ask` permission rules keep
      their any-depth match.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  - quote: Changed `file` commands using `-m`/`--magic-file` or `-f`/`--files-from`
      to require permission instead of being auto-allowed as read-only
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-safety-and-privacy-changes-in-v2-1-214
  source_release: claude-code-2026-07-18-v2-1-214-github-355973317-478680c5
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in v2.1.214
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed
  multi-second per-turn slowdowns in sessions with many permission deny/ask rules]]'
- '[[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety
  and Privacy changes in v2.1.211]]'
- '[[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety
  and Privacy changes in v2.1.212]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-18-v2-1-214-github-355973317-478680c5|claude-code-2026-07-18-v2-1-214-github-355973317-478680c5]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in v2.1.214
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in v2.1.214

**Claude Code** · 2026-07-18 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.214) · from [[Releases/Claude Code/claude-code-2026-07-18-v2-1-214-github-355973317-478680c5|v2.1.214]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed a permission-check bypass affecting commands run in Windows PowerShell 5.1 sessions

> Fixed Bash permission checks to fail closed on file-descriptor redirect forms that bash parses differently than the permission analyzer

> Fixed Bash permission checks misjudging very long commands — commands over 10,000 characters now always prompt instead of running automatically

> Fixed Bash permission checks treating zsh variable subscripts and modifiers in `[[ ]]` comparisons as inert text — these commands now prompt for approval

> Fixed Bash permission checks to no longer auto-approve certain `help` and `man` commands that could run unsafe options, command substitutions, or backslash paths

> Fixed permission prompts on remote sessions that could proceed before the local confirmation dialog

> Added permission prompts for `docker` commands (including the Podman `docker` shim) carrying daemon-redirect flags (`--url`, `--connection`, `--identity`, and Podman's remote mode) that previously ran without one

> Changed single-segment `dir/**` hook `if:` conditions to match only `<cwd>/dir`; write `**/dir/**` for any-depth matching. `deny`/`ask` permission rules keep their any-depth match.

> Changed `file` commands using `-m`/`--magic-file` or `-f`/`--files-from` to require permission instead of being auto-allowed as read-only

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.214
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-07-18-added-an-iso-modified-timestamp-to-memory-file-frontmatter|Added an ISO modified timestamp to memory file frontmatter]] · Memory and Personalization
- [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]] · Agent Mode
- [[Changes/Claude Code/2026-07-18-added-a-periodic-progress-heartbeat-for-long-running-tool-calls-that-previously|Added a periodic progress heartbeat for long-running tool calls that previously went…]] · Reliability and Performance
- [[Changes/Claude Code/2026-07-18-changed-sessionstart-hooks-to-report-source-fork-when-a-session-begins-as-a-fork|Changed SessionStart hooks to report source "fork" when a session begins as a fork…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-17 · Claude Code · [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]]
- Later: 2026-07-20 · Claude Code · [[Changes/Claude Code/2026-07-20-5-safety-and-privacy-changes-in-v2-1-216|5 Safety and Privacy changes in v2.1.216]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-07-18-832703&body=Card%3A%20Changes%2FClaude%20Code%2F2026-07-18-9-safety-and-privacy-changes-in-v2-1-214.md%0ACard%20ID%3A%20claude-code-2026-07-18-832703%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.214%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->