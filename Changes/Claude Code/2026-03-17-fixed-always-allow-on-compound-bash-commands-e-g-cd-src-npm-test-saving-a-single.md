---
card_id: claude-code-2026-03-17-8c3bdf
date: '2026-03-17'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1066
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 1f7009a4f6edd867358b4b03727ea3247c0a19a011db8d1e194df7c551ea0992
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-17-8c3bdf
  comparison: ''
  date: '2026-03-17'
  description: 'Claude Code — v2.1.77: Fixed "Always Allow" on compound bash commands
    (e.g. `cd src && npm test`) saving a single rule for the full string instead of
    per-subcommand, leading to dead rules and repeated permission prompts'
  evidence:
  - quote: Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`)
      saving a single rule for the full string instead of per-subcommand, leading
      to dead rules and repeated permission prompts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-always-allow-on-compound-bash-commands-e-g-cd-src-npm-test-saving-a-single
  source_release: claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`)
    savin
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|claude-code-2026-03-11-933354]]'
- '[[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|claude-code-2026-03-12-bcb8f1]]'
- '[[Changes/Claude Code/2026-03-17-added-allowread-sandbox-filesystem-setting-to-re-allow-read-access-within-denyre|claude-code-2026-03-17-468805]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
source_type: github_releases
theme: safety-privacy
title: Fixed "Always Allow" on compound bash commands (e.g. cd src && npm test) savin
type: change
---

# Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`) savin

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.77: Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`) saving a single rule for the full string instead of per-subcommand, leading to dead rules and repeated permission prompts
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`) saving a single rule for the full string instead of per-subcommand, leading to dead rules and repeated permission prompts
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
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
- Lag Days: 1066
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes