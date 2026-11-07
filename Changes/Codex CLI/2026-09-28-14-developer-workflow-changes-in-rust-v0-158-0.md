---
card_id: codex-cli-2026-09-28-d0f70e
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Developer Workflow: 14 changes in 0.158.0 —
  Terminal input approval is enabled by default for commands running with elevated…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2939
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2bb7091e59b82e565f634e11a3f30352112e1847c9408a57cfec88d600fb1aa3
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-d0f70e
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 14 Developer Workflow changes'
  evidence:
  - quote: 'Terminal input approval is enabled by default for commands running with
      elevated permissions; runtime-only grants no longer cause unnecessary reviews.
      (#47799, #48073)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47529 Emit command lifecycle events for unified exec launch failures
      @steipete-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47539 Test interrupted one-shot command launch failure persistence @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47611 Use the shared process launcher for Unix shell snapshots @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47748 Align Cargo and Bazel Rust debug information defaults @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47799 Enable terminal input approval by default @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47967 Surface Flex capacity failures as a distinct terminal error @sdcoffey'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47974 Preserve Git directory protections across writable roots @aionescu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48069 Handle early command yields in the Guardian network approval test
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48078 Replay exec-server shell snapshots through unnamed files @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48099 Honor shell environment policy in legacy snapshots @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48101 Show multiline command previews in `/ps` @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48121 Keep startup drafts visible during command center session handoff
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48132 Allow Left to open the command center from read-only conversations
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-developer-workflow-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: developer-workflow
  title: 14 Developer Workflow changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/Devin/2026-09-25-pr-links-respect-your-pr-link-preference-everywhere|PR
  Links Respect Your PR-Link Preference Everywhere]]'
- '[[Changes/Devin/2026-09-25-azure-devops-pipeline-logs-and-self-hosted-servers|Azure
  DevOps: Pipeline Logs and Self-Hosted Servers]]'
- '[[Changes/Claude Code/2026-09-28-changed-recap-to-decline-with-a-short-notice-when-it-arrives-relayed-from-a-chat|Changed
  /recap to decline with a short notice when it arrives relayed from a chat…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: developer-workflow
title: 14 Developer Workflow changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Developer Workflow changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Terminal input approval is enabled by default for commands running with elevated permissions; runtime-only grants no longer cause unnecessary reviews. (#47799, #48073)

> #47529 Emit command lifecycle events for unified exec launch failures @steipete-oai

> #47539 Test interrupted one-shot command launch failure persistence @jif-oai

> #47611 Use the shared process launcher for Unix shell snapshots @charliemarsh-oai

> #47748 Align Cargo and Bazel Rust debug information defaults @aibrahim-oai

> #47799 Enable terminal input approval by default @jif-oai

> #47967 Surface Flex capacity failures as a distinct terminal error @sdcoffey

> #47974 Preserve Git directory protections across writable roots @aionescu-oai

> #48069 Handle early command yields in the Guardian network approval test @jif-oai

> #48078 Replay exec-server shell snapshots through unnamed files @jif-oai

> #48099 Honor shell environment policy in legacy snapshots @jif-oai

> #48101 Show multiline command previews in `/ps` @etraut-openai

> #48121 Keep startup drafts visible during command center session handoff @etraut-openai

> #48132 Allow Left to open the command center from read-only conversations @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0|13 Apps and Integrations changes in rust-v0.158.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-28-8-account-and-access-changes-in-rust-v0-158-0|8 Account and Access changes in rust-v0.158.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0|3 Mobile and Desktop changes in rust-v0.158.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-changed-recap-to-decline-with-a-short-notice-when-it-arrives-relayed-from-a-chat|Changed /recap to decline with a short notice when it arrives relayed from a chat…]]
- Later: 2026-09-28 · ElevenLabs · [[Changes/ElevenLabs/2026-09-28-flows-ffc074|Flows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-d0f70e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-d0f70e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->