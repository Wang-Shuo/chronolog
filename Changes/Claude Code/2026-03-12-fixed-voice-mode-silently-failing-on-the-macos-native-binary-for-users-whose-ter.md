---
card_id: claude-code-2026-03-12-bcb8f1
date: '2026-03-12'
description: 'Claude Code · 2026-03-12 · Safety and Privacy: Fixed voice mode silently
  failing on the macOS native binary for users whose terminal had never been granted…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1061
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: fix
machine_hash: 40bca5f5af3f201a2a54d0a7742c72fae69eef2cc6fd8ca59d6310e7fc97926a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-12-bcb8f1
  comparison: ''
  date: '2026-03-12'
  description: 'Claude Code — v2.1.74: Fixed voice mode silently failing on the macOS
    native binary for users whose terminal had never been granted microphone permission
    — the binary now includes the `audio-input` entitlement so macOS prompts correctly'
  evidence:
  - quote: Fixed voice mode silently failing on the macOS native binary for users
      whose terminal had never been granted microphone permission — the binary now
      includes the `audio-input` entitlement so macOS prompts correctly
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.74
  extractor_version: fallback-v5
  impact: incremental
  kind: fix
  product: claude-code
  product_name: Claude Code
  slug: fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter
  source_release: claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - voice
    - audio
    score: 160
    theme: voice
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  - matched_terms:
    - macos
    score: 50
    theme: mobile-desktop
  theme_resolution: manual-semantic-rule-v2
  title: Fixed voice mode silently failing on the macOS native binary for users whose…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed
  false-positive permission prompts for compound bash commands containing…]]'
- '[[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety
  and Privacy changes in v2.1.72]]'
- '[[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed
  freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae|claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae]]'
source_type: github_releases
theme: safety-privacy
title: Fixed voice mode silently failing on the macOS native binary for users whose…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed voice mode silently failing on the macOS native binary for users whose…

**Claude Code** · 2026-03-12 · [[Themes/safety-privacy|Safety and Privacy]] · Fix · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.74) · from [[Releases/Claude Code/claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae|v2.1.74]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed voice mode silently failing on the macOS native binary for users whose terminal had never been granted microphone permission — the binary now includes the `audio-input` entitlement so macOS prompts correctly
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.74
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-12-2-memory-and-personalization-changes-in-v2-1-74|2 Memory and Personalization changes in v2.1.74]] · Memory and Personalization
- [[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|VSCode Improved scroll wheel responsiveness in the integrated terminal…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed --plugin-dir so local dev copies now override installed marketplace…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-11 · Claude Code · [[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed freezes and 100% CPU loops triggered by permission prompts for complex bash commands]]
- Later: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-12-bcb8f1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter.md%0ACard%20ID%3A%20claude-code-2026-03-12-bcb8f1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.74%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->