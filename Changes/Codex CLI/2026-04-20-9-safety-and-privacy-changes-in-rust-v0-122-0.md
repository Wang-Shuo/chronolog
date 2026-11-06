---
card_id: codex-cli-2026-04-20-b0326e
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Safety and Privacy: 9 changes in 0.122.0 —
  Filesystem permissions now support deny-read glob policies, managed deny-read requirements…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1100
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a1c6e272c1dff2feda5fef296d55e144fa629fa1963f6fb7579c666f358d8ecd
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-b0326e
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 9 Safety and Privacy changes'
  evidence:
  - quote: 'Filesystem permissions now support deny-read glob policies, managed deny-read
      requirements, platform sandbox enforcement, and isolated `codex exec` runs that
      ignore user config or rules (#15979, #17740, #18096, #18646).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: 'Security-sensitive flows were tightened: logout revokes managed ChatGPT
      tokens, project hooks and exec policies require trusted workspaces, and Windows
      sandbox setup avoids broad user-profile and SSH-root grants (#17825, #14718,
      #18443, #18493).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: 'Added a security-boundaries reference to `SECURITY.md` for sandboxing,
      approvals, and network controls (#17848, #18004).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17848 [docs] Add security boundaries reference in SECURITY.md @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18004 [docs] Restore SECURITY.md update from PR 17848 @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18096 feat(sandbox): add glob deny-read platform enforcement @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18296 fix: fix fs sandbox helper for apply_patch @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18443 Do not grant Windows sandbox ACLs on USERPROFILE @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18493 Filter Windows sandbox roots from SSH config dependencies @efrazer-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.122.0
  type: change
related_changes:
- '[[Changes/Replit/2026-04-17-custom-groups-for-scim-organizations|Custom groups
  for SCIM organizations]]'
- '[[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|Fixed
  a crash in the permission dialog when an agent teams teammate requested tool…]]'
- '[[Changes/Claude Code/2026-04-20-security-sandbox-auto-allow-no-longer-bypasses-the-dangerous-path-safety-check-f|Security:
  sandbox auto-allow no longer bypasses the dangerous-path safety check…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Filesystem permissions now support deny-read glob policies, managed deny-read requirements, platform sandbox enforcement, and isolated `codex exec` runs that ignore user config or rules (#15979, #17740, #18096, #18646).

> Security-sensitive flows were tightened: logout revokes managed ChatGPT tokens, project hooks and exec policies require trusted workspaces, and Windows sandbox setup avoids broad user-profile and SSH-root grants (#17825, #14718, #18443, #18493).

> Added a security-boundaries reference to `SECURITY.md` for sandboxing, approvals, and network controls (#17848, #18004).

> #17848 [docs] Add security boundaries reference in SECURITY.md @evawong-oai

> #18004 [docs] Restore SECURITY.md update from PR 17848 @evawong-oai

> #18096 feat(sandbox): add glob deny-read platform enforcement @viyatb-oai

> #18296 fix: fix fs sandbox helper for apply_patch @viyatb-oai

> #18443 Do not grant Windows sandbox ACLs on USERPROFILE @efrazer-oai

> #18493 Filter Windows sandbox roots from SSH config dependencies @efrazer-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6 Developer Workflow changes in rust-v0.122.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-10-agent-mode-changes-in-rust-v0-122-0|10 Agent Mode changes in rust-v0.122.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Model Support
- [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]] · Context Window
- [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-20-18398-refactor-use-cloneable-async-channels-for-shared-receivers-bolinfest|♯18398 refactor: use cloneable async channels for shared receivers @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28 Apps and Integrations changes in rust-v0.122.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2 Interface Experience changes in rust-v0.122.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-20-2-mobile-and-desktop-changes-in-rust-v0-122-0|2 Mobile and Desktop changes in rust-v0.122.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-20-100-other-changes-in-rust-v0-122-0|100 other changes in rust-v0.122.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-security-sandbox-auto-allow-no-longer-bypasses-the-dangerous-path-safety-check-f|Security: sandbox auto-allow no longer bypasses the dangerous-path safety check…]]
- Later: 2026-04-21 · Open WebUI · [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-b0326e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-b0326e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->