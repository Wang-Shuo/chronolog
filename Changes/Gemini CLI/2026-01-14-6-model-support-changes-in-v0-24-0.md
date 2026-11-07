---
card_id: gemini-cli-2026-01-14-ba990f
date: '2026-01-14'
description: 'Gemini CLI · 2026-01-14 · Model Support: 6 changes in Release v0.24.0
  — chore(core): refactor model resolution and cleanup fallback logic by @adamfweidman
  in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1101
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 46e998a0344cae91b91aebbd4158754667d5170b4619de761dd8f187ff52eee7
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-01-14-ba990f
  comparison: ''
  date: '2026-01-14'
  description: 'Gemini CLI — Release v0.24.0: 6 Model Support changes'
  evidence:
  - quote: 'chore(core): refactor model resolution and cleanup fallback logic by @adamfweidman
      in https://github.com/google-gemini/gemini-cli/pull/15228'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'feat: automatic `/model` persistence across Gemini CLI sessions by @niyasrad
      in https://github.com/google-gemini/gemini-cli/pull/13199'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: do not persist the fallback model by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15483
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: 'Agent Skills: Add gemini skills CLI management command by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/15837'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: Opt-in to persist model from /model by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15820
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  - quote: remove manual string when displaying manual model in the footer by @sehoon38
      in https://github.com/google-gemini/gemini-cli/pull/15967
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 6-model-support-changes-in-v0-24-0
  source_release: gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in v0.24.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-01-13-3-model-support-changes-in-v1-1-16|3 Model Support
  changes in v1.1.16]]'
- '[[Changes/Cline/2026-01-14-add-gpt-5-2-codex-openai-model-support|Add gpt-5.2-codex
  OpenAI model support]]'
- '[[Changes/Codex CLI/2026-01-14-8-model-support-changes-in-rust-v0-81-0|8 Model
  Support changes in rust-v0.81.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547|gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in v0.24.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in v0.24.0

**Gemini CLI** · 2026-01-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0) · from [[Releases/Gemini CLI/gemini-cli-2026-01-14-v0-24-0-github-276723271-62398547|Release v0.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> chore(core): refactor model resolution and cleanup fallback logic by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/15228

> feat: automatic `/model` persistence across Gemini CLI sessions by @niyasrad in https://github.com/google-gemini/gemini-cli/pull/13199

> do not persist the fallback model by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15483

> Agent Skills: Add gemini skills CLI management command by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/15837

> Opt-in to persist model from /model by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15820

> remove manual string when displaying manual model in the footer by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/15967

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.24.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-01-14-7-safety-and-privacy-changes-in-v0-24-0|7 Safety and Privacy changes in v0.24.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-01-14-10-agent-mode-changes-in-v0-24-0|10 Agent Mode changes in v0.24.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-01-14-feat-add-folder-suggestions-to-dir-add-command-by-jackwotherspoon-in-https-githu|feat: add folder suggestions to /dir add command]] · Developer Workflow
- [[Changes/Gemini CLI/2026-01-14-9-apps-and-integrations-changes-in-v0-24-0|9 Apps and Integrations changes in v0.24.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-01-14-4-editor-experience-changes-in-v0-24-0|4 Editor Experience changes in v0.24.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-01-14-2-context-window-changes-in-v0-24-0|2 Context Window changes in v0.24.0]] · Context Window
- [[Changes/Gemini CLI/2026-01-14-38-other-changes-in-v0-24-0|38 other changes in v0.24.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-01-14 · Codex CLI · [[Changes/Codex CLI/2026-01-14-8-model-support-changes-in-rust-v0-81-0|8 Model Support changes in rust-v0.81.0]]
- Later: 2026-01-14 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-01-14-add-support-for-gpt-5-2-codex-model|Add support for GPT-5.2-Codex model]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-01-14-ba990f&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-01-14-6-model-support-changes-in-v0-24-0.md%0ACard%20ID%3A%20gemini-cli-2026-01-14-ba990f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.24.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->