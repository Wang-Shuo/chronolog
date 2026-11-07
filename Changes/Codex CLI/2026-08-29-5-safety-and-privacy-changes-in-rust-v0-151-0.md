---
card_id: codex-cli-2026-08-29-13767a
date: '2026-08-29'
description: 'Codex CLI · 2026-08-29 · Safety and Privacy: 5 changes in 0.151.0 —
  Preserved restored permission profiles across TUI turns and prevented `/cd` from
  weakening…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2223
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 64410c57bcad8b64bbd5636deef1698e84cd249096ea3dfd7d75d9f8764b1d62
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-29-13767a
  comparison: ''
  date: '2026-08-29'
  description: 'Codex CLI — 0.151.0: 5 Safety and Privacy changes'
  evidence:
  - quote: Preserved restored permission profiles across TUI turns and prevented `/cd`
      from weakening sandbox restrictions. (#41192)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: 'Improved remote sandbox enforcement using the executor’s actual home directory,
      operating system, and path conventions. (#41196, #41204, #41207, #41209)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: Prevented stale Guardian classifications from authorizing actions after
      permission state changes. (#41196)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41192 Preserve restored permission profiles in TUI sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  - quote: '#41204 Propagate executor home directories into sandbox contexts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.151.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-safety-and-privacy-changes-in-rust-v0-151-0
  source_release: codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in rust-v0.151.0
  type: change
related_changes:
- '[[Changes/Devin/2026-08-28-new-org-permission-manage-personal-automations|New Org
  Permission: Manage Personal Automations]]'
- '[[Changes/Kimi Code/2026-08-28-web-fix-switching-the-permission-mode-in-one-session-changing-it-for-every-sessi|web:
  Fix switching the permission mode in one session changing it for every session]]'
- '[[Changes/v0/2026-08-28-2-safety-and-privacy-changes-in-gpt-5-6-sol-sign-in-inside-previews|2
  Safety and Privacy changes in GPT-5.6 Sol, sign-in inside previews…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d|codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in rust-v0.151.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in rust-v0.151.0

**Codex CLI** · 2026-08-29 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.151.0) · from [[Releases/Codex CLI/codex-cli-2026-08-29-rust-v0-151-0-github-378941035-5571827d|0.151.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Preserved restored permission profiles across TUI turns and prevented `/cd` from weakening sandbox restrictions. (#41192)

> Improved remote sandbox enforcement using the executor’s actual home directory, operating system, and path conventions. (#41196, #41204, #41207, #41209)

> Prevented stale Guardian classifications from authorizing actions after permission state changes. (#41196)

> #41192 Preserve restored permission profiles in TUI sessions @copyberry

> #41204 Propagate executor home directories into sandbox contexts @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.151.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-29-11-apps-and-integrations-changes-in-rust-v0-151-0|11 Apps and Integrations changes in rust-v0.151.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-29-3-model-support-changes-in-rust-v0-151-0|3 Model Support changes in rust-v0.151.0]] · Model Support
- [[Changes/Codex CLI/2026-08-29-2-agent-mode-changes-in-rust-v0-151-0|2 Agent Mode changes in rust-v0.151.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-29-6-other-changes-in-rust-v0-151-0|6 other changes in rust-v0.151.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-28 · v0 · [[Changes/v0/2026-08-28-2-safety-and-privacy-changes-in-gpt-5-6-sol-sign-in-inside-previews|2 Safety and Privacy changes in GPT-5.6 Sol, sign-in inside previews…]]
- Later: 2026-08-31 · Open WebUI · [[Changes/Open WebUI/2026-08-31-security-advisory-this-release-includes-security-and-access-control-fixes-we-rec|🛡️ Security Advisory: This release includes security and access-control fixes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-29-13767a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-29-5-safety-and-privacy-changes-in-rust-v0-151-0.md%0ACard%20ID%3A%20codex-cli-2026-08-29-13767a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.151.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->