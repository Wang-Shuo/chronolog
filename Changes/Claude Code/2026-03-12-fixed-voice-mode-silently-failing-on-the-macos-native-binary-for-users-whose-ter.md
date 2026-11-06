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
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: fix
machine_hash: c213898e2dfe2d58222e09eb8f335b9dc1a6ba328ab4fbe4f12c310958937780
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
  theme_resolution: manual-semantic-rule-v2
  title: Fixed voice mode silently failing on the macOS native binary for users whose…
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-11-2-safety-and-privacy-changes-in-rust-v0-114-0|2
  Safety and Privacy changes in rust-v0.114.0]]'
- '[[Changes/Gemini CLI/2026-03-11-refactor-cli-fully-remove-react-anti-patterns-improve-type-safety-and-fix-ux-ove|refactor(cli):
  fully remove React anti patterns, improve type safety and fix UX…]]'
- '[[Changes/GitHub Copilot CLI/2026-03-11-2-safety-and-privacy-changes-in-v1-0-4|2
  Safety and Privacy changes in v1.0.4]]'
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

- [[Changes/Claude Code/2026-03-12-added-automemorydirectory-setting-to-configure-a-custom-directory-for-auto-memor|Added autoMemoryDirectory setting to configure a custom directory for auto-memory…]] · Memory and Personalization
- [[Changes/Claude Code/2026-03-12-added-actionable-suggestions-to-context-command-identifies-context-heavy-tools-m|Added actionable suggestions to /context command]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|VSCode Improved scroll wheel responsiveness in the integrated terminal…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-12-changed-plugin-dir-so-local-dev-copies-now-override-installed-marketplace-plugin|Changed --plugin-dir so local dev copies now override installed marketplace…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-11 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-11-2-safety-and-privacy-changes-in-v1-0-4|2 Safety and Privacy changes in v1.0.4]]
- Later: 2026-03-12 · Cline · [[Changes/Cline/2026-03-12-markdown-image-loading-now-requires-user-consent|Markdown image loading now requires user consent]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-12-bcb8f1&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter.md%0ACard%20ID%3A%20claude-code-2026-03-12-bcb8f1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.74%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->