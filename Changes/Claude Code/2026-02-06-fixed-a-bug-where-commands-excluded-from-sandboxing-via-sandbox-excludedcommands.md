---
card_id: claude-code-2026-02-06-1233de
date: '2026-02-06'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1027
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: e97ba2113b356e5469dbf8257ac243250dcc7f180524ec03b876448feff418b4
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
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands
  source_release: claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedComman
  type: change
related_changes:
- '[[Changes/Claude Code/2026-01-14-fixed-security-vulnerability-where-wildcard-permission-rules-could-match-compoun|claude-code-2026-01-14-a0bfb2]]'
- '[[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|claude-code-2026-01-29-fc6c51]]'
- '[[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|claude-code-2026-01-30-3cd8a3]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29|claude-code-2026-02-06-v2-1-34-github-283772587-e48b5e29]]'
source_type: github_releases
theme: safety-privacy
title: Fixed a bug where commands excluded from sandboxing (via sandbox.excludedComman
type: change
---

# Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedComman

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.34: Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed a bug where commands excluded from sandboxing (via `sandbox.excludedCommands` or `dangerouslyDisableSandbox`) could bypass the Bash ask permission rule when `autoAllowBashIfSandboxed` was enabled
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.34
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1027
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes