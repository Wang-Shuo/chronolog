---
card_id: codex-cli-2026-08-26-849b33
date: '2026-08-26'
description: 'Codex CLI · 2026-08-26 · Safety and Privacy: 12 changes in 0.150.0 —
  Bind shortcuts to cycle permission modes, and use `.` in Vim mode to repeat your
  last…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1228
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b2556f4cb7cef5eb9f6d68e30c39433662cc728741c154e909ef79abf10a27bc
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-26-849b33
  comparison: ''
  date: '2026-08-26'
  description: 'Codex CLI — 0.150.0: 12 Safety and Privacy changes'
  evidence:
  - quote: 'Bind shortcuts to cycle permission modes, and use `.` in Vim mode to repeat
      your last edit. (#39873, #40521)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: 'Untrusted projects no longer supply project-level `AGENTS.md` instructions,
      and managed deny-read rules remain enforced after permission changes. (#39837,
      #40004)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39752 Expose uncompiled permission profile selection @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39873 Add keybindings for cycling TUI permission modes @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39971 Fix elevated Windows sandbox setup activation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39976 Allow semaphore limit queries in the macOS sandbox @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40004 Preserve managed deny-read rules across permission updates @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40024 Honor granular sandbox approvals in unified exec @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40295 Classify permission instructions under the permissions namespace
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40381 Preserve sandbox errors during session initialization @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40475 Request read control when updating Windows sandbox ACLs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40551 Derive sandbox contexts from turn environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-safety-and-privacy-changes-in-rust-v0-150-0
  source_release: codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c
  source_type: github_releases
  theme: safety-privacy
  title: 12 Safety and Privacy changes in rust-v0.150.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-26120-clarify-privacy-notice-wording-and-selection-options-b|SSR
  Agent Issue Fix (26120): Clarify privacy notice wording and selection options]]'
- '[[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety
  and Privacy changes in v0.11.1]]'
- '[[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety
  and Privacy changes in v2.1.247]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c]]'
source_type: github_releases
theme: safety-privacy
title: 12 Safety and Privacy changes in rust-v0.150.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Safety and Privacy changes in rust-v0.150.0

**Codex CLI** · 2026-08-26 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.150.0) · from [[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|0.150.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Bind shortcuts to cycle permission modes, and use `.` in Vim mode to repeat your last edit. (#39873, #40521)

> Untrusted projects no longer supply project-level `AGENTS.md` instructions, and managed deny-read rules remain enforced after permission changes. (#39837, #40004)

> #39752 Expose uncompiled permission profile selection @copyberry

> #39873 Add keybindings for cycling TUI permission modes @copyberry

> #39971 Fix elevated Windows sandbox setup activation @copyberry

> #39976 Allow semaphore limit queries in the macOS sandbox @copyberry

> #40004 Preserve managed deny-read rules across permission updates @copyberry

> #40024 Honor granular sandbox approvals in unified exec @copyberry

> #40295 Classify permission instructions under the permissions namespace @copyberry

> #40381 Preserve sandbox errors during session initialization @copyberry

> #40475 Request read control when updating Windows sandbox ACLs @copyberry

> #40551 Derive sandbox contexts from turn environments @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.150.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-26-39953-support-voice-aware-configuration-and-version-skew-builds-copyberry|♯39953 Support voice-aware configuration and version-skew builds @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-26-6-interface-experience-changes-in-rust-v0-150-0|6 Interface Experience changes in rust-v0.150.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-26-10-model-support-changes-in-rust-v0-150-0|10 Model Support changes in rust-v0.150.0]] · Model Support
- [[Changes/Codex CLI/2026-08-26-24-apps-and-integrations-changes-in-rust-v0-150-0|24 Apps and Integrations changes in rust-v0.150.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-26-15-developer-workflow-changes-in-rust-v0-150-0|15 Developer Workflow changes in rust-v0.150.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-26-40544-include-transparent-background-in-image-generation-analytics-copyberry|♯40544 Include transparent background in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-26-14-agent-mode-changes-in-rust-v0-150-0|14 Agent Mode changes in rust-v0.150.0]] · Agent Mode
- [[Changes/Codex CLI/2026-08-26-2-account-and-access-changes-in-rust-v0-150-0|2 Account and Access changes in rust-v0.150.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-26-39811-restrict-macos-preference-reads-to-full-disk-policies-copyberry|♯39811 Restrict macOS preference reads to full-disk policies @copyberry]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-26-40488-export-turn-cost-as-an-otel-metric-copyberry|♯40488 Export turn cost as an OTEL metric @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-26-3-memory-and-personalization-changes-in-rust-v0-150-0|3 Memory and Personalization changes in rust-v0.150.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-26-40436-add-a-managed-gate-for-in-app-local-automation-copyberry|♯40436 Add a managed gate for in-app local automation @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-08-26-14-context-window-changes-in-rust-v0-150-0|14 Context Window changes in rust-v0.150.0]] · Context Window
- [[Changes/Codex CLI/2026-08-26-110-other-changes-in-rust-v0-150-0|110 other changes in rust-v0.150.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]]
- Later: 2026-08-26 · Lovable · [[Changes/Lovable/2026-08-26-log-out-everywhere|Log out everywhere]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-26-849b33&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-26-12-safety-and-privacy-changes-in-rust-v0-150-0.md%0ACard%20ID%3A%20codex-cli-2026-08-26-849b33%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.150.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->