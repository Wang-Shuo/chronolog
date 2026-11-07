---
card_id: ollama-2026-10-08-2694b3
date: '2026-10-08'
description: 'Ollama · 2026-10-08 · Model Support: 4 changes in v0.40.2 — To make
  downgrading safe, Ollama keeps the original copy as a backup, so upgraded models
  are…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1368
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ef5e18718be81a7c833a55157ef8bb325b9628f93669f66d55153a9d57472451
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-10-08-2694b3
  comparison: ''
  date: '2026-10-08'
  description: 'Ollama — v0.40.2: 4 Model Support changes'
  evidence:
  - quote: To make downgrading safe, Ollama keeps the original copy as a backup, so
      upgraded models are temporarily kept on disk. A future release will remove these
      backups automatically.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.2
  - quote: 'To remove backed up models now (requires `jq`):'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.2
  - quote: This only deletes the backups. If you later downgrade to a version older
      than 0.40, you'll need to re-pull those models.
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.2
  - quote: '`ollama list` no longer shows duplicate entries for upgraded models by
      @dhiltgen in https://github.com/ollama/ollama/pull/18874'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.40.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 4-model-support-changes-in-v0-40-2
  source_release: ollama-2026-10-08-v0-40-2-github-407063639-d2785d50
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in v0.40.2
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-11-model-support-changes-in-rust-v0-162-0|11 Model
  Support changes in rust-v0.162.0]]'
- '[[Changes/GitHub Copilot CLI/2026-10-08-add-claude-haiku-5-5-to-model-selection-and-model-completions|Add
  Claude Haiku 5.5 to model selection and --model completions]]'
- '[[Changes/Midjourney/2026-10-08-we-re-finding-in-tests-that-this-helps-make-the-model-better-at-prompt-accuracy|We''re
  finding in tests that this helps make the model better at prompt accuracy…]]'
source_release: '[[Releases/Ollama/ollama-2026-10-08-v0-40-2-github-407063639-d2785d50|ollama-2026-10-08-v0-40-2-github-407063639-d2785d50]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in v0.40.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in v0.40.2

**Ollama** · 2026-10-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.40.2) · from [[Releases/Ollama/ollama-2026-10-08-v0-40-2-github-407063639-d2785d50|v0.40.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> To make downgrading safe, Ollama keeps the original copy as a backup, so upgraded models are temporarily kept on disk. A future release will remove these backups automatically.

> To remove backed up models now (requires `jq`):

> This only deletes the backups. If you later downgrade to a version older than 0.40, you'll need to re-pull those models.

> `ollama list` no longer shows duplicate entries for upgraded models by @dhiltgen in https://github.com/ollama/ollama/pull/18874

Source: https://github.com/ollama/ollama/releases/tag/v0.40.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-10-08-ollama-launch-claude-uses-the-model-s-full-context-length-by-jberg5-in-https-git|ollama launch claude uses the model's full context length]] · Context Window
- [[Changes/Ollama/2026-10-08-models-downloaded-with-earlier-versions-of-ollama-are-upgraded-in-the-background|Models downloaded with earlier versions of Ollama are upgraded in the background…]] · Reliability and Performance
- [[Changes/Ollama/2026-10-08-readme-add-oxi-to-community-integrations-by-maziluiosif-in-https-github-com-olla|README: add oxi to community integrations]] · Apps and Integrations
- [[Changes/Ollama/2026-10-08-other-changes|Other changes]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-08 · Midjourney · [[Changes/Midjourney/2026-10-08-we-re-finding-in-tests-that-this-helps-make-the-model-better-at-prompt-accuracy|We're finding in tests that this helps make the model better at prompt accuracy…]]
- Later: 2026-10-08 · OpenClaw · [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-10-08-2694b3&body=Card%3A%20Changes%2FOllama%2F2026-10-08-4-model-support-changes-in-v0-40-2.md%0ACard%20ID%3A%20ollama-2026-10-08-2694b3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.40.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->