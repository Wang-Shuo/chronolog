---
card_id: codex-cli-2026-09-28-06a74e
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Safety and Privacy: 9 changes in 0.158.0 —
  Fixed Windows sandbox failures involving ordinary Windows 10 paths, rejected stored…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1261
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1844e8bb28881a0e2585c063908f607fd80fb4f37fc53bc0f3c655c5b76c6092
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-06a74e
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 9 Safety and Privacy changes'
  evidence:
  - quote: 'Fixed Windows sandbox failures involving ordinary Windows 10 paths, rejected
      stored credentials, and large permission policies. (#47672, #47695, #47919)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47568 Record sandbox backends in command execution analytics @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47673 Clarify registered Windows sandbox setup errors @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47695 Repair rejected Windows sandbox credentials during provisioning
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47867 Render remote permission paths using executor context @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47879 Fix macOS system-alias matching in patch permission checks @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47919 Transport large Windows sandbox launch payloads through the environment
      @malsamiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48017 Test same-cell permission grants and strict review in code mode
      @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48073 Avoid stdin approval for runtime-only permission grants @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-25-fix-mcp-keep-oauth-credentials-on-cloud-saves-and-skip-consent-when-tokens-still|fix(mcp):
  keep OAuth credentials on cloud saves and skip consent when tokens still work]]'
- '[[Changes/Replit/2026-09-25-control-access-to-design-systems-and-slide-templates|Control
  access to design systems and slide templates]]'
- '[[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety
  and Privacy changes in v2.1.284]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Fixed Windows sandbox failures involving ordinary Windows 10 paths, rejected stored credentials, and large permission policies. (#47672, #47695, #47919)

> #47568 Record sandbox backends in command execution analytics @iceweasel-oai

> #47673 Clarify registered Windows sandbox setup errors @zm-oai

> #47695 Repair rejected Windows sandbox credentials during provisioning @zm-oai

> #47867 Render remote permission paths using executor context @iceweasel-oai

> #47879 Fix macOS system-alias matching in patch permission checks @felixxia-oai

> #47919 Transport large Windows sandbox launch payloads through the environment @malsamiri-oai

> #48017 Test same-cell permission grants and strict review in code mode @anp-oai

> #48073 Avoid stdin approval for runtime-only permission grants @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]]
- Later: 2026-09-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-28-2-safety-and-privacy-changes-in-v1-0-89|2 Safety and Privacy changes in v1.0.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-06a74e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-06a74e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->