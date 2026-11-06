---
card_id: codex-cli-2026-01-09-bd02cc
date: '2026-01-09'
description: 'Codex CLI · 2026-01-09 · Model Support: 4 changes in 0.80.0 — #8844
  Fix app-server `write_models_cache` to treat models with less priority number as
  higher…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1096
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 611446400443f75f418722c76ef43e54412b7df49cb795a22a814f425e4aa9ee
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-09-bd02cc
  comparison: ''
  date: '2026-01-09'
  description: 'Codex CLI — 0.80.0: 4 Model Support changes'
  evidence:
  - quote: '#8844 Fix app-server `write_models_cache` to treat models with less priority
      number as higher priority. @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8856 Override truncation policy at model info level @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8847 Warn in /model if BASE_URL set @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8792 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-model-support-changes-in-rust-v0-80-0
  source_release: codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf
  source_type: github_releases
  theme: model-support
  title: 4 Model Support changes in rust-v0.80.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-01-08-large-tool-outputs-are-written-to-disk-and-models-are-encouraged-to-use-efficien|Large
  tool outputs are written to disk and models are encouraged to use efficient…]]'
- '[[Changes/Claude Code/2026-01-09-merged-slash-commands-and-skills-simplifying-the-mental-model-with-no-change-in|Merged
  slash commands and skills, simplifying the mental model with no change in behavior]]'
- '[[Changes/Cline/2026-01-09-2-model-support-changes-in-v3-48-0|2 Model Support changes
  in v3.48.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf]]'
source_type: github_releases
theme: model-support
title: 4 Model Support changes in rust-v0.80.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Model Support changes in rust-v0.80.0

**Codex CLI** · 2026-01-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.80.0) · from [[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|0.80.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #8844 Fix app-server `write_models_cache` to treat models with less priority number as higher priority. @aibrahim-oai

> #8856 Override truncation policy at model info level @aibrahim-oai

> #8847 Warn in /model if BASE_URL set @gt-oai

> #8792 Update models.json @github-actions

Source: https://github.com/openai/codex/releases/tag/rust-v0.80.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-09-2-apps-and-integrations-changes-in-rust-v0-80-0|2 Apps and Integrations changes in rust-v0.80.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-09-2-agent-mode-changes-in-rust-v0-80-0|2 Agent Mode changes in rust-v0.80.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-09-codex-cli-subprocesses-again-inherit-env-vars-like-ld-library-path-dyld-library|Codex CLI subprocesses again inherit env vars like…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-09-8939-chore-move-app-server-tests-from-chat-completion-to-responses-celia-oai|♯8939 chore move app server tests from chat completion to responses @celia-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-09-app-server-readme-now-documents-skills-support-and-usage-8853|App-server README now documents skills support and usage]] · Files and Data
- [[Changes/Codex CLI/2026-01-09-4-developer-workflow-changes-in-rust-v0-80-0|4 Developer Workflow changes in rust-v0.80.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-09-2-mobile-and-desktop-changes-in-rust-v0-80-0|2 Mobile and Desktop changes in rust-v0.80.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-09-3-interface-experience-changes-in-rust-v0-80-0|3 Interface Experience changes in rust-v0.80.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety and Privacy changes in rust-v0.80.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-09-62-other-changes-in-rust-v0-80-0|62 other changes in rust-v0.80.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-01-09 · Cline · [[Changes/Cline/2026-01-09-2-model-support-changes-in-v3-48-0|2 Model Support changes in v3.48.0]]
- Later: 2026-01-10 · Cline · [[Changes/Cline/2026-01-10-removing-minimax-2-1-from-free-model-list-as-the-free-trial-has-ended|Removing Minimax-2.1 from free model list as the free trial has ended]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-09-bd02cc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-09-4-model-support-changes-in-rust-v0-80-0.md%0ACard%20ID%3A%20codex-cli-2026-01-09-bd02cc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.80.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->