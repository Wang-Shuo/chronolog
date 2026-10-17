---
card_id: claude-code-2026-08-28-fe1922
date: '2026-08-28'
description: 'Claude Code · 2026-08-28 · Safety and Privacy: 6 changes in v2.1.251
  — Fixed file tools (Read, Write, Edit) following a symlink swapped inside the working…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1230
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4438b1848ac4fbb56982cb7e4e1ab808eb744aef7bb97e4d0d64566e5f2099c0
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-28-fe1922
  comparison: ''
  date: '2026-08-28'
  description: 'Claude Code — v2.1.251: 6 Safety and Privacy changes'
  evidence:
  - quote: Fixed file tools (Read, Write, Edit) following a symlink swapped inside
      the working directory after the permission check, which could read or write
      outside the approved location
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Fixed the Workflow tool reading (and quoting in errors) a `scriptPath`
      outside what the session may read before the permission check ran
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Fixed Bash permission checks auto-approving commands that assign an arithmetic
      expression to an integer shell variable (e.g. `OPTIND=1/0`, `RANDOM=2+2`); these
      now prompt for approval
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed Claude in Chrome so browser actions always go through Claude Code's
      permission checks, including in sessions with telemetry disabled, which previously
      used the Chrome extension's own prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed how Bash command output files are created and read back when commands
      run in the sandbox, so a sandboxed command cannot redirect or replace them
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  - quote: Changed server-managed settings that terminate sandbox TLS, route sandbox
      traffic through your own proxy, inject credentials, or weaken sandbox isolation
      to require approval before they apply
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-safety-and-privacy-changes-in-v2-1-251
  source_release: claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v2.1.251
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety
  and Privacy changes in v2.1.246]]'
- '[[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety
  and Privacy changes in v2.1.247]]'
- '[[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety
  and Privacy changes in v2.1.248]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v2.1.251
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v2.1.251

**Claude Code** · 2026-08-28 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) · from [[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed file tools (Read, Write, Edit) following a symlink swapped inside the working directory after the permission check, which could read or write outside the approved location

> Fixed the Workflow tool reading (and quoting in errors) a `scriptPath` outside what the session may read before the permission check ran

> Fixed Bash permission checks auto-approving commands that assign an arithmetic expression to an integer shell variable (e.g. `OPTIND=1/0`, `RANDOM=2+2`); these now prompt for approval

> Changed Claude in Chrome so browser actions always go through Claude Code's permission checks, including in sessions with telemetry disabled, which previously used the Chrome extension's own prompts

> Changed how Bash command output files are created and read back when commands run in the sandbox, so a sandboxed command cannot redirect or replace them

> Changed server-managed settings that terminate sandbox TLS, route sandbox traffic through your own proxy, inject credentials, or weaken sandbox isolation to require approval before they apply

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]] · Account and Access
- [[Changes/Claude Code/2026-08-28-4-model-support-changes-in-v2-1-251|4 Model Support changes in v2.1.251]] · Model Support
- [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing Model
- [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]] · Developer Workflow
- [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]] · Context Window
- [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Agent Mode
- [[Changes/Claude Code/2026-08-28-improved-amazon-bedrock-session-start-under-claude-code-provider-managed-by-host|Improved Amazon Bedrock session start under CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-28-8-other-changes-in-v2-1-251|8 other changes in v2.1.251]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety and Privacy changes in v2.1.248]]
- Later: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed remote and scheduled sessions failing…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-28-fe1922&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-28-6-safety-and-privacy-changes-in-v2-1-251.md%0ACard%20ID%3A%20claude-code-2026-08-28-fe1922%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.251%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->