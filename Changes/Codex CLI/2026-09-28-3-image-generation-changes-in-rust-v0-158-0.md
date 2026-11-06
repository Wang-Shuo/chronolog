---
card_id: codex-cli-2026-09-28-7a66a6
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Image Generation: 3 changes in 0.158.0 — Image
  generation and editing can explicitly request transparent backgrounds, and edits
  now…'
diffusion:
  first_in_tracked: "[[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|\U0001F3A8
    DALL-E Integration]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 932
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: image-generation
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 61ba2b259f580fa497d0c0dea476f453ecbd01a474a1a8068f95812d60a5c2ea
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-7a66a6
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 3 Image Generation changes'
  evidence:
  - quote: 'Image generation and editing can explicitly request transparent backgrounds,
      and edits now accept file-backed conversation images. (#47484, #47956)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47484 Add explicit background control to image generation @alicec-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47742 Honor network policy in history notes and image generation extensions
      @jackz100'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-image-generation-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: image-generation
  title: 3 Image Generation changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation
  changes in v0.11.4]]'
- '[[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544
  Discourage logging full image generation results @Gan-Tu]]'
- '[[Changes/Codex CLI/2026-09-25-47327-preserve-image-generation-request-ids-on-failure-chrisdong-oai|♯47327
  Preserve image generation request IDs on failure @chrisdong-oai]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: image-generation
title: 3 Image Generation changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Image Generation changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/image-generation|Image Generation]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Image generation and editing can explicitly request transparent backgrounds, and edits now accept file-backed conversation images. (#47484, #47956)

> #47484 Add explicit background control to image generation @alicec-oai

> #47742 Honor network policy in history notes and image generation extensions @jackz100

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
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Image Generation

- Earlier: 2026-09-25 · Codex CLI · [[Changes/Codex CLI/2026-09-25-47327-preserve-image-generation-request-ids-on-failure-chrisdong-oai|♯47327 Preserve image generation request IDs on failure @chrisdong-oai]]
- Later: 2026-09-28 · ElevenLabs · [[Changes/ElevenLabs/2026-09-28-flows|Flows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-03-10 · Open WebUI · [[Changes/Open WebUI/2024-03-10-dall-e-integration-introduced-dall-e-integration-for-image-generation-alongside|🎨 DALL-E Integration]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-7a66a6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-3-image-generation-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-7a66a6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->