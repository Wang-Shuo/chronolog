---
card_id: codex-cli-2026-01-21-51aef8
date: '2026-01-21'
description: 'Codex CLI · 2026-01-21 · Safety and Privacy: 3 changes in 0.88.0 — #9314
  fix(windows-sandbox): deny .git file entries under writable roots @MaxMiksa'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1011
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f247281a467d7509d22c660877ea9552a132b8687a33080de8059fc4983b9dce
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-21-51aef8
  comparison: ''
  date: '2026-01-21'
  description: 'Codex CLI — 0.88.0: 3 Safety and Privacy changes'
  evidence:
  - quote: '#9314 fix(windows-sandbox): deny .git file entries under writable roots
      @MaxMiksa'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9319 fix(windows-sandbox): parse PATH list entries for audit roots @MaxMiksa'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  - quote: '#9532 fix(cli): add execute permission to bin/codex.js @zerone0x'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.88.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-safety-and-privacy-changes-in-rust-v0-88-0
  source_release: codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in rust-v0.88.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0|5 Safety
  and Privacy changes in rust-v0.81.0]]'
- '[[Changes/Gemini CLI/2026-01-14-7-safety-and-privacy-changes-in-v0-24-0|7 Safety
  and Privacy changes in v0.24.0]]'
- '[[Changes/Codex CLI/2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n|revert
  Linux sandboxing now falls back to Landlock-only restrictions when user…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4|codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in rust-v0.88.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in rust-v0.88.0

**Codex CLI** · 2026-01-21 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.88.0) · from [[Releases/Codex CLI/codex-cli-2026-01-21-rust-v0-88-0-github-278754265-4d0aa1b4|0.88.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #9314 fix(windows-sandbox): deny .git file entries under writable roots @MaxMiksa

> #9319 fix(windows-sandbox): parse PATH list entries for audit roots @MaxMiksa

> #9532 fix(cli): add execute permission to bin/codex.js @zerone0x

Source: https://github.com/openai/codex/releases/tag/rust-v0.88.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-21-3-apps-and-integrations-changes-in-rust-v0-88-0|3 Apps and Integrations changes in rust-v0.88.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-21-8590-fix-core-require-approval-for-force-delete-on-windows-hdcodedev|♯8590 fix(core): require approval for force delete on Windows @hdcodedev]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-21-9459-feat-personality-introduce-model-personality-config-dylan-hurd-oai|♯9459 feat(personality) introduce model_personality config @dylan-hurd-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-01-21-9543-fix-memory-leak-issue-jif-oai|♯9543 fix: memory leak issue @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-21-9-collaboration-changes-in-rust-v0-88-0|9 Collaboration changes in rust-v0.88.0]] · Collaboration
- [[Changes/Codex CLI/2026-01-21-2-agent-mode-changes-in-rust-v0-88-0|2 Agent Mode changes in rust-v0.88.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-21-5-model-support-changes-in-rust-v0-88-0|5 Model Support changes in rust-v0.88.0]] · Model Support
- [[Changes/Codex CLI/2026-01-21-3-interface-experience-changes-in-rust-v0-88-0|3 Interface Experience changes in rust-v0.88.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-21-9-developer-workflow-changes-in-rust-v0-88-0|9 Developer Workflow changes in rust-v0.88.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-21-63-other-changes-in-rust-v0-88-0|63 other changes in rust-v0.88.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-15 · Codex CLI · [[Changes/Codex CLI/2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n|revert Linux sandboxing now falls back to Landlock-only restrictions when user…]]
- Later: 2026-01-22 · Codex CLI · [[Changes/Codex CLI/2026-01-22-2-safety-and-privacy-changes-in-rust-v0-89-0|2 Safety and Privacy changes in rust-v0.89.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-21-51aef8&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-21-3-safety-and-privacy-changes-in-rust-v0-88-0.md%0ACard%20ID%3A%20codex-cli-2026-01-21-51aef8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.88.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->