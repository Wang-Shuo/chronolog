---
card_id: claude-code-2026-03-12-bcb8f1
date: '2026-03-12'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1061
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 582b057b452c0095f4c08ca031786fc0c2d72c1a4d4c441f0b098d9661f3de7b
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
  extractor_version: fallback-v3
  impact: incremental
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
  title: Fixed voice mode silently failing on the macOS native binary for users whose
    ter
  type: change
related_changes:
- '[[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|cursor-2026-03-05-9c8870]]'
- '[[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|claude-code-2026-03-07-85bd62]]'
- '[[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|claude-code-2026-03-11-933354]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae|claude-code-2026-03-12-v2-1-74-github-295929475-2ee971ae]]'
source_type: github_releases
theme: safety-privacy
title: Fixed voice mode silently failing on the macOS native binary for users whose
  ter
type: change
---

# Fixed voice mode silently failing on the macOS native binary for users whose ter

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.74: Fixed voice mode silently failing on the macOS native binary for users whose terminal had never been granted microphone permission — the binary now includes the `audio-input` entitlement so macOS prompts correctly
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed voice mode silently failing on the macOS native binary for users whose terminal had never been granted microphone permission — the binary now includes the `audio-input` entitlement so macOS prompts correctly
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.74
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
- Lag Days: 1061
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes