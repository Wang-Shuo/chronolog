---
card_id: codex-cli-2026-08-20-3583bd
date: '2026-08-20'
description: 'Codex CLI · 2026-08-20 · Safety and Privacy: 18 changes in 0.149.0 —
  Resumed and forked threads now restore their active permission profile instead of
  silently…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2214
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 55712c1dfd66a96e9a39d33ed55f67ffda2ae90ce87f151ceb761282c413d795
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-20-3583bd
  comparison: ''
  date: '2026-08-20'
  description: 'Codex CLI — 0.149.0: 18 Safety and Privacy changes'
  evidence:
  - quote: Resumed and forked threads now restore their active permission profile
      instead of silently falling back to current defaults. (#39153)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38830 Isolate external editor buffers from sandbox-writable paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38916 Honor legacy `:project_roots` permission entries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#38919 Reject obsolete app-server permission profile fields @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39067 Add desktop security enforcement diagnostics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39083 Harden Windows sandbox provisioning against reparse points @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39084 Preserve filesystem permission path conventions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39103 Drop capabilities from Linux sandbox processes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39117 Reject lossy legacy permission projections @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39145 Persist active permission profiles in turn context @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39153 Restore permission profiles when resuming threads @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39242 Add safe permission profile intersection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39266 Require fresh approval beneath denied permission paths @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39279 Propagate Windows sandbox ACL update failures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39290 Add Windows sandbox diagnostics to `codex doctor` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39325 Stop migrating Cursor sandbox settings @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39629 Preserve parent repository discovery through sandbox metadata mounts
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  - quote: '#39632 Expose permission profile resolution in the core API @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.149.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-safety-and-privacy-changes-in-rust-v0-149-0
  source_release: codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944
  source_type: github_releases
  theme: safety-privacy
  title: 18 Safety and Privacy changes in rust-v0.149.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-19-2-safety-and-privacy-changes-in-v2-1-236|2 Safety
  and Privacy changes in v2.1.236]]'
- '[[Changes/Lovable/2026-08-19-a-simpler-publish-dialog|A simpler Publish dialog]]'
- '[[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety
  and Privacy changes in v2.1.238]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944]]'
source_type: github_releases
theme: safety-privacy
title: 18 Safety and Privacy changes in rust-v0.149.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Safety and Privacy changes in rust-v0.149.0

**Codex CLI** · 2026-08-20 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.149.0) · from [[Releases/Codex CLI/codex-cli-2026-08-20-rust-v0-149-0-github-374028976-829da944|0.149.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Resumed and forked threads now restore their active permission profile instead of silently falling back to current defaults. (#39153)

> #38830 Isolate external editor buffers from sandbox-writable paths @copyberry

> #38916 Honor legacy `:project_roots` permission entries @copyberry

> #38919 Reject obsolete app-server permission profile fields @copyberry

> #39067 Add desktop security enforcement diagnostics @copyberry

> #39083 Harden Windows sandbox provisioning against reparse points @copyberry

> #39084 Preserve filesystem permission path conventions @copyberry

> #39103 Drop capabilities from Linux sandbox processes @copyberry

> #39117 Reject lossy legacy permission projections @copyberry

> #39145 Persist active permission profiles in turn context @copyberry

> #39153 Restore permission profiles when resuming threads @copyberry

> #39242 Add safe permission profile intersection @copyberry

> #39266 Require fresh approval beneath denied permission paths @copyberry

> #39279 Propagate Windows sandbox ACL update failures @copyberry

> #39290 Add Windows sandbox diagnostics to `codex doctor` @copyberry

> #39325 Stop migrating Cursor sandbox settings @copyberry

> #39629 Preserve parent repository discovery through sandbox metadata mounts @copyberry

> #39632 Expose permission profile resolution in the core API @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.149.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-20-2-reliability-and-performance-changes-in-rust-v0-149-0|2 Reliability and Performance changes in rust-v0.149.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-08-20-6-model-support-changes-in-rust-v0-149-0|6 Model Support changes in rust-v0.149.0]] · Model Support
- [[Changes/Codex CLI/2026-08-20-18-developer-workflow-changes-in-rust-v0-149-0|18 Developer Workflow changes in rust-v0.149.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-20-2-memory-and-personalization-changes-in-rust-v0-149-0|2 Memory and Personalization changes in rust-v0.149.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-20-39045-add-managed-gates-for-in-app-chat-and-dictation-copyberry|♯39045 Add managed gates for in-app chat and dictation @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-20-9-context-window-changes-in-rust-v0-149-0|9 Context Window changes in rust-v0.149.0]] · Context Window
- [[Changes/Codex CLI/2026-08-20-2-collaboration-changes-in-rust-v0-149-0|2 Collaboration changes in rust-v0.149.0]] · Collaboration
- [[Changes/Codex CLI/2026-08-20-5-editor-experience-changes-in-rust-v0-149-0|5 Editor Experience changes in rust-v0.149.0]] · Editor Experience
- [[Changes/Codex CLI/2026-08-20-7-mobile-and-desktop-changes-in-rust-v0-149-0|7 Mobile and Desktop changes in rust-v0.149.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-20-3-interface-experience-changes-in-rust-v0-149-0|3 Interface Experience changes in rust-v0.149.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-20-33-apps-and-integrations-changes-in-rust-v0-149-0|33 Apps and Integrations changes in rust-v0.149.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-20-8-account-and-access-changes-in-rust-v0-149-0|8 Account and Access changes in rust-v0.149.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-20-39072-persist-generated-images-through-turn-executors-copyberry|♯39072 Persist generated images through turn executors @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-20-12-agent-mode-changes-in-rust-v0-149-0|12 Agent Mode changes in rust-v0.149.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-20-39283-document-secure-devcontainer-dns-exfiltration-risk-copyberry|♯39283 Document secure devcontainer DNS exfiltration risk @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-08-20-39006-emit-api-key-turn-cost-telemetry-from-app-server-copyberry|♯39006 Emit API-key turn cost telemetry from app-server @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-20-125-other-changes-in-rust-v0-149-0|125 other changes in rust-v0.149.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-20 · Claude Code · [[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety and Privacy changes in v2.1.238]]
- Later: 2026-08-21 · Claude Code · [[Changes/Claude Code/2026-08-21-fixed-fullscreen-mode-answering-a-permission-prompt-or-pressing-a-button-when-yo|Fixed fullscreen mode answering a permission prompt or pressing a button when you…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-20-3583bd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0.md%0ACard%20ID%3A%20codex-cli-2026-08-20-3583bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.149.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->