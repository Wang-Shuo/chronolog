---
card_id: codex-cli-2026-10-23-588b24
date: '2026-10-23'
description: 'Codex CLI · 2026-10-23 · Safety and Privacy: 15 changes in 0.164.0 —
  Set model, reasoning effort, speed, and permission profiles directly with inline
  `/model`…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1286
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ad1673c91ea3a93b9fa51ceee6238129c64b5a9da9dee1d34bf97097de180186
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-23-588b24
  comparison: ''
  date: '2026-10-23'
  description: 'Codex CLI — 0.164.0: 15 Safety and Privacy changes'
  evidence:
  - quote: 'Set model, reasoning effort, speed, and permission profiles directly with
      inline `/model` and `/permissions` arguments. (#54378, #54383)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: Queued prompts now wait for pending permission selections to resolve before
      continuing. (#55682)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: 'Hardened sandbox checks for case-variant metadata paths on macOS and replaceable
      symlinks used to locate executables. (#54273, #55384)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: Updated the embedded JavaScript runtime with safety checks for optimized
      `Array.sort` operations. (#54519)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54119 Allow stdin review under active grants with sandbox prompts disabled
      @tepman-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54265 Add regression coverage for Guardian sandbox retry approvals @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54383 Support inline permission profile selection with `/permissions`
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54385 Allow saving current permission settings as presets @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54445 Remove obsolete protected-path monitoring from the Linux sandbox
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54519 Upgrade V8 to 152.2.0 and backport Array.sort safety guards @seanh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55378 Migrate the Windows MXC sandbox to `mxc-sdk` @johnl-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55384 Reject replaceable symlinks in pre-sandbox executable lookup @keeley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55593 Reject unpackaged Windows sandbox provisioning clients @chess-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55620 Move Linux sandbox unit tests into separate files @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55682 Fix TUI permission selection and session state handling @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-safety-and-privacy-changes-in-rust-v0-164-0
  source_release: codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d
  source_type: github_releases
  theme: safety-privacy
  title: 15 Safety and Privacy changes in rust-v0.164.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-22-security-release-v2026-10-6-adds-remediations-for-the-emudhra-certificate-compro|Security
  release: v2026.10.6 adds remediations for the eMudhra certificate compromise]]'
- '[[Changes/OpenCode/2026-10-22-upgraded-the-bundled-bun-runtime-to-1-4-4|Upgraded
  the bundled Bun runtime to 1.4.4]]'
- '[[Changes/Claude Code/2026-10-23-4-safety-and-privacy-changes-in-v2-1-310|4 Safety
  and Privacy changes in v2.1.310]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d]]'
source_type: github_releases
theme: safety-privacy
title: 15 Safety and Privacy changes in rust-v0.164.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Safety and Privacy changes in rust-v0.164.0

**Codex CLI** · 2026-10-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.164.0) · from [[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|0.164.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Set model, reasoning effort, speed, and permission profiles directly with inline `/model` and `/permissions` arguments. (#54378, #54383)

> Queued prompts now wait for pending permission selections to resolve before continuing. (#55682)

> Hardened sandbox checks for case-variant metadata paths on macOS and replaceable symlinks used to locate executables. (#54273, #55384)

> Updated the embedded JavaScript runtime with safety checks for optimized `Array.sort` operations. (#54519)

> #54119 Allow stdin review under active grants with sandbox prompts disabled @tepman-oai

> #54265 Add regression coverage for Guardian sandbox retry approvals @jif-oai

> #54383 Support inline permission profile selection with `/permissions` @fcoury-oai

> #54385 Allow saving current permission settings as presets @fcoury-oai

> #54445 Remove obsolete protected-path monitoring from the Linux sandbox @viyatb-oai

> #54519 Upgrade V8 to 152.2.0 and backport Array.sort safety guards @seanh-oai

> #55378 Migrate the Windows MXC sandbox to `mxc-sdk` @johnl-oai

> #55384 Reject replaceable symlinks in pre-sandbox executable lookup @keeley-openai

> #55593 Reject unpackaged Windows sandbox provisioning clients @chess-oai

> #55620 Move Linux sandbox unit tests into separate files @bolinfest

> #55682 Fix TUI permission selection and session state handling @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-23-24-account-and-access-changes-in-rust-v0-164-0|24 Account and Access changes in rust-v0.164.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-23-8-mobile-and-desktop-changes-in-rust-v0-164-0|8 Mobile and Desktop changes in rust-v0.164.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]] · Context Window
- [[Changes/Codex CLI/2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0|30 Apps and Integrations changes in rust-v0.164.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-9-interface-experience-changes-in-rust-v0-164-0|9 Interface Experience changes in rust-v0.164.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-23-9-model-support-changes-in-rust-v0-164-0|9 Model Support changes in rust-v0.164.0]] · Model Support
- [[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14 Developer Workflow changes in rust-v0.164.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice and Audio changes in rust-v0.164.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-23-183-other-changes-in-rust-v0-164-0|183 other changes in rust-v0.164.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-23 · Claude Code · [[Changes/Claude Code/2026-10-23-4-safety-and-privacy-changes-in-v2-1-310|4 Safety and Privacy changes in v2.1.310]]
- Later: 2026-10-23 · Dify · [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-23-588b24&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0.md%0ACard%20ID%3A%20codex-cli-2026-10-23-588b24%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.164.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->