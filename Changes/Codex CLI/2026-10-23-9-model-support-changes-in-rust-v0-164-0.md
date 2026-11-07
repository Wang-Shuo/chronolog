---
card_id: codex-cli-2026-10-23-eea8cc
date: '2026-10-23'
description: 'Codex CLI · 2026-10-23 · Model Support: 9 changes in 0.164.0 — #53745
  Remove `modelSlug` from the latest-model resolver output @kkahadze-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1383
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2e9300a179b5488a9153828a7f50a3d9004335021ba6333bcad9db2ae8453f7a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-23-eea8cc
  comparison: ''
  date: '2026-10-23'
  description: 'Codex CLI — 0.164.0: 9 Model Support changes'
  evidence:
  - quote: '#53745 Remove `modelSlug` from the latest-model resolver output @kkahadze-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54169 Reload the model catalog after account changes @smurching-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#54946 Preserve model catalog caches across header credential rotation
      @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55144 Add observation-only model request lifecycle hooks @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55265 Avoid cloning the full catalog for model metadata lookups @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55293 Keep only the latest adjacent reasoning effort update in requests
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55923 Preserve thread model settings across resume and revert @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55958 Preserve provider model catalogs when refreshes fail @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  - quote: '#55991 Avoid double-counting retained reasoning in token usage @dkovalenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.164.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-model-support-changes-in-rust-v0-164-0
  source_release: codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d
  source_type: github_releases
  theme: model-support
  title: 9 Model Support changes in rust-v0.164.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-22-3-model-support-changes-in-v1-0-103|3 Model
  Support changes in v1.0.103]]'
- '[[Changes/Lovable/2026-10-22-gemini-2-5-chat-models-are-retired-for-your-app-s-ai-features|Gemini
  2.5 chat models are retired for your app''s AI features]]'
- '[[Changes/OpenClaw/2026-10-22-4-model-support-changes-in-v2026-10-6|4 Model Support
  changes in v2026.10.6]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d]]'
source_type: github_releases
theme: model-support
title: 9 Model Support changes in rust-v0.164.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in rust-v0.164.0

**Codex CLI** · 2026-10-23 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.164.0) · from [[Releases/Codex CLI/codex-cli-2026-10-23-rust-v0-164-0-github-421457270-d867151d|0.164.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #53745 Remove `modelSlug` from the latest-model resolver output @kkahadze-oai

> #54169 Reload the model catalog after account changes @smurching-oai

> #54946 Preserve model catalog caches across header credential rotation @hlevy-openai

> #55144 Add observation-only model request lifecycle hooks @vivi

> #55265 Avoid cloning the full catalog for model metadata lookups @charliemarsh-oai

> #55293 Keep only the latest adjacent reasoning effort update in requests @felixxia-oai

> #55923 Preserve thread model settings across resume and revert @etraut-openai

> #55958 Preserve provider model catalogs when refreshes fail @abhinav-oai

> #55991 Avoid double-counting retained reasoning in token usage @dkovalenko-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.164.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-23-24-account-and-access-changes-in-rust-v0-164-0|24 Account and Access changes in rust-v0.164.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-2-reliability-and-performance-changes-in-rust-v0-164-0|2 Reliability and Performance changes in rust-v0.164.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-10-23-8-collaboration-changes-in-rust-v0-164-0|8 Collaboration changes in rust-v0.164.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-23-4-memory-and-personalization-changes-in-rust-v0-164-0|4 Memory and Personalization changes in rust-v0.164.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-23-13-agent-mode-changes-in-rust-v0-164-0|13 Agent Mode changes in rust-v0.164.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-23-2-image-generation-changes-in-rust-v0-164-0|2 Image Generation changes in rust-v0.164.0]] · Image Generation
- [[Changes/Codex CLI/2026-10-23-8-mobile-and-desktop-changes-in-rust-v0-164-0|8 Mobile and Desktop changes in rust-v0.164.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-23-18-context-window-changes-in-rust-v0-164-0|18 Context Window changes in rust-v0.164.0]] · Context Window
- [[Changes/Codex CLI/2026-10-23-30-apps-and-integrations-changes-in-rust-v0-164-0|30 Apps and Integrations changes in rust-v0.164.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]] · Account and Access
- [[Changes/Codex CLI/2026-10-23-9-interface-experience-changes-in-rust-v0-164-0|9 Interface Experience changes in rust-v0.164.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-23-14-developer-workflow-changes-in-rust-v0-164-0|14 Developer Workflow changes in rust-v0.164.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-23-3-voice-and-audio-changes-in-rust-v0-164-0|3 Voice and Audio changes in rust-v0.164.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-23-183-other-changes-in-rust-v0-164-0|183 other changes in rust-v0.164.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-22 · OpenClaw · [[Changes/OpenClaw/2026-10-22-4-model-support-changes-in-v2026-10-6|4 Model Support changes in v2026.10.6]]
- Later: 2026-10-23 · Dify · [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-23-eea8cc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-23-9-model-support-changes-in-rust-v0-164-0.md%0ACard%20ID%3A%20codex-cli-2026-10-23-eea8cc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.164.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->