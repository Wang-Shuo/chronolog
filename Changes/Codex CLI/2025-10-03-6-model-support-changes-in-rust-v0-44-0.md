---
card_id: codex-cli-2025-10-03-611243
date: '2025-10-03'
description: 'Codex CLI · 2025-10-03 · Model Support: 6 changes in 0.44.0 — #4641
  Move gpt-5-codex to top'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 998
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4ffe40567b9b2e1d722624ff8b9197c3b6ee80b3ea61168d9728fe7dcaa80e39
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-03-611243
  comparison: ''
  date: '2025-10-03'
  description: 'Codex CLI — 0.44.0: 6 Model Support changes'
  evidence:
  - quote: '#4641 Move gpt-5-codex to top'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4178 Make model switcher two-stage'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4475 show "Viewed Image" when the model views an image'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4569 fix: update the gpt-5-codex prompt to be more explicit that it should
      always used fenced code blocks info tags'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4332 chore: remove model upgrade popup'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  - quote: '#4335 fix: set gpt-5-codex medium preset reasoning'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.44.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-model-support-changes-in-rust-v0-44-0
  source_release: codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in rust-v0.44.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-10-02-2-model-support-changes-in-v0-0-333|2 Model
  Support changes in v0.0.333]]'
- '[[Changes/GitHub Copilot CLI/2025-10-02-added-usage-slash-command-to-provide-stats-about-premium-request-usage-session-t|Added
  /usage slash command to provide stats about Premium request usage, session…]]'
- '[[Changes/ChatGPT/2025-10-03-we-re-updating-gpt-5-instant-to-better-recognize-and-support-people-in-moments-o-ea32fc|Updating
  GPT-5]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37|codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in rust-v0.44.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in rust-v0.44.0

**Codex CLI** · 2025-10-03 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.44.0) · from [[Releases/Codex CLI/codex-cli-2025-10-03-rust-v0-44-0-github-252055554-66c49f37|0.44.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #4641 Move gpt-5-codex to top

> #4178 Make model switcher two-stage

> #4475 show "Viewed Image" when the model views an image

> #4569 fix: update the gpt-5-codex prompt to be more explicit that it should always used fenced code blocks info tags

> #4332 chore: remove model upgrade popup

> #4335 fix: set gpt-5-codex medium preset reasoning

Source: https://github.com/openai/codex/releases/tag/rust-v0.44.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-03-3-safety-and-privacy-changes-in-rust-v0-44-0|3 Safety and Privacy changes in rust-v0.44.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-10-03-5-agent-mode-changes-in-rust-v0-44-0|5 Agent Mode changes in rust-v0.44.0]] · Agent Mode
- [[Changes/Codex CLI/2025-10-03-4568-fix-hang-on-second-oauth-login-attempt|♯4568 Fix hang on second oauth login attempt]] · Account and Access
- [[Changes/Codex CLI/2025-10-03-2-context-window-changes-in-rust-v0-44-0|2 Context Window changes in rust-v0.44.0]] · Context Window
- [[Changes/Codex CLI/2025-10-03-3-interface-experience-changes-in-rust-v0-44-0|3 Interface Experience changes in rust-v0.44.0]] · Interface Experience
- [[Changes/Codex CLI/2025-10-03-17-apps-and-integrations-changes-in-rust-v0-44-0|17 Apps and Integrations changes in rust-v0.44.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-10-03-experimental-reduce-repetitive-approval-for-read-only-commands-on-windows-4269|(experimental) Reduce repetitive approval for read-only commands on Windows (♯4269)]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-10-03-2-editor-experience-changes-in-rust-v0-44-0|2 Editor Experience changes in rust-v0.44.0]] · Editor Experience
- [[Changes/Codex CLI/2025-10-03-4469-no-background-for-command-or-file-popup|♯4469 no background for /command or @file popup]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-03-4511-wire-up-web-search-item|♯4511 Wire up web search item]] · Search and Browsing
- [[Changes/Codex CLI/2025-10-03-70-other-changes-in-rust-v0-44-0|70 other changes in rust-v0.44.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-10-03 · ChatGPT · [[Changes/ChatGPT/2025-10-03-we-re-updating-gpt-5-instant-to-better-recognize-and-support-people-in-moments-o-ea32fc|Updating GPT-5]]
- Later: 2025-10-03 · Ollama · [[Changes/Ollama/2025-10-03-ollama-flash-attention-can-now-be-overridden-to-0-for-models-that-have-flash-att|OLLAMA_FLASH_ATTENTION can now be overridden to 0 for models that have flash…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-03-611243&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-03-6-model-support-changes-in-rust-v0-44-0.md%0ACard%20ID%3A%20codex-cli-2025-10-03-611243%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.44.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->