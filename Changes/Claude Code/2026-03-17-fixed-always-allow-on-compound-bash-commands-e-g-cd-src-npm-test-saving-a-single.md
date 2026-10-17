---
card_id: claude-code-2026-03-17-8c3bdf
date: '2026-03-17'
description: 'Claude Code · 2026-03-17 · Safety and Privacy: Fixed "Always Allow"
  on compound bash commands (e.g. `cd src && npm test`) saving a single rule for the
  full…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1066
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: df8450d0232df5d450801c2a7265fe80d6477b8a62bfa2a4870b4a10014d7b1e
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
  extractor_version: fallback-v4
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
    saving…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed
  freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]'
- '[[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|Fixed
  voice mode silently failing on the macOS native binary for users whose…]]'
- '[[Changes/Claude Code/2026-03-17-added-allowread-sandbox-filesystem-setting-to-re-allow-read-access-within-denyre|Added
  allowRead sandbox filesystem setting to re-allow read access within…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c]]'
source_type: github_releases
superseded: true
theme: safety-privacy
title: Fixed "Always Allow" on compound bash commands (e.g. cd src && npm test) saving…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`) saving…

**Claude Code** · 2026-03-17 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.77) · from [[Releases/Claude Code/claude-code-2026-03-17-v2-1-77-github-297726061-caf6c30c|v2.1.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`) saving a single rule for the full string instead of per-subcommand, leading to dead rules and repeated permission prompts
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.77
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-17-added-allowread-sandbox-filesystem-setting-to-re-allow-read-access-within-denyre|Added allowRead sandbox filesystem setting to re-allow read access within…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon|/copy now accepts an optional index: /copy N copies the Nth-latest assistant response]] · Interface Experience
- [[Changes/Claude Code/2026-03-17-increased-default-maximum-output-token-limits-for-claude-opus-4-6-to-64k-tokens|Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens…]] · Model Support
- [[Changes/Claude Code/2026-03-17-fixed-pretooluse-hooks-returning-allow-bypassing-deny-permission-rules-including|Fixed PreToolUse hooks returning "allow" bypassing deny permission rules…]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-12 · Claude Code · [[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|Fixed voice mode silently failing on the macOS native binary for users whose…]]
- Later: 2026-03-18 · Claude Code · [[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed custom status line showing nothing when workspace trust is blocking it]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-17-8c3bdf&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-17-fixed-always-allow-on-compound-bash-commands-e-g-cd-src-npm-test-saving-a-single.md%0ACard%20ID%3A%20claude-code-2026-03-17-8c3bdf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.77%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->