---
card_id: codex-cli-2026-02-11-97f092
date: '2026-02-11'
description: 'Codex CLI · 2026-02-11 · Model Support: 15 changes in 0.99.0 — #10748
  Update explorer role default model @jif-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1129
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8c8d93801b95189f2212003cb270529627a0efd86aa444eafc6ab530997a1426
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-11-97f092
  comparison: ''
  date: '2026-02-11'
  description: 'Codex CLI — 0.99.0: 15 Model Support changes'
  evidence:
  - quote: '#10748 Update explorer role default model @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10775 nit: gpt-5.3-codex announcement @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#10782 nit: gpt-5.3-codex announcement 2 @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11051 Gate view_image tool by model input_modalities @wiltzius-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11228 Use longest remote model prefix matching @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11238 Remove offline fallback for models @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#9739 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11255 Revert "Update models.json" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11256 Revert "Revert "Update models.json"" @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11239 Disable dynamic model refresh for custom model providers @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11330 test(core): stabilize ARM bazel remote-model and parallelism tests
      @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11349 Strip unsupported images from prompt history to guard against model
      switch @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11274 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11376 Update models.json @github-actions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  - quote: '#11386 Prefer websocket transport when model opts in @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.99.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-model-support-changes-in-rust-v0-99-0
  source_release: codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016
  source_type: github_releases
  theme: model-support
  title: 15 Model Support changes in rust-v0.99.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-02-07-add-support-for-claude-opus-4-6-fast-preview|Add
  support for Claude Opus 4.6 Fast (Preview)]]'
- '[[Changes/ChatGPT/2026-02-10-we-re-making-an-update-to-gpt-5-2-instant-in-chatgpt-and-the-api-that-improves-r|GPT-5.2
  Instant Update]]'
- '[[Changes/Gemini CLI/2026-02-10-docs-document-gemini-cli-home-environment-variable-by-adamfweidman-in-https-gith|docs:
  document GEMINI_CLI_HOME environment variable]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016]]'
source_type: github_releases
theme: model-support
title: 15 Model Support changes in rust-v0.99.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Model Support changes in rust-v0.99.0

**Codex CLI** · 2026-02-11 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.99.0) · from [[Releases/Codex CLI/codex-cli-2026-02-11-rust-v0-99-0-github-285424682-f7f48016|0.99.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #10748 Update explorer role default model @jif-oai

> #10775 nit: gpt-5.3-codex announcement @jif-oai

> #10782 nit: gpt-5.3-codex announcement 2 @jif-oai

> #11051 Gate view_image tool by model input_modalities @wiltzius-openai

> #11228 Use longest remote model prefix matching @aibrahim-oai

> #11238 Remove offline fallback for models @aibrahim-oai

> #9739 Update models.json @github-actions

> #11255 Revert "Update models.json" @aibrahim-oai

> #11256 Revert "Revert "Update models.json"" @aibrahim-oai

> #11239 Disable dynamic model refresh for custom model providers @etraut-openai

> #11330 test(core): stabilize ARM bazel remote-model and parallelism tests @dylan-hurd-oai

> #11349 Strip unsupported images from prompt history to guard against model switch @aibrahim-oai

> #11274 Update models.json @github-actions

> #11376 Update models.json @github-actions

> #11386 Prefer websocket transport when model opts in @pakrym-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.99.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-11-3-search-and-browsing-changes-in-rust-v0-99-0|3 Search and Browsing changes in rust-v0.99.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-11-9-developer-workflow-changes-in-rust-v0-99-0|9 Developer Workflow changes in rust-v0.99.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-11-6-context-window-changes-in-rust-v0-99-0|6 Context Window changes in rust-v0.99.0]] · Context Window
- [[Changes/Codex CLI/2026-02-11-13-apps-and-integrations-changes-in-rust-v0-99-0|13 Apps and Integrations changes in rust-v0.99.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety and Privacy changes in rust-v0.99.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-11-7-memory-and-personalization-changes-in-rust-v0-99-0|7 Memory and Personalization changes in rust-v0.99.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-11-enterprise-admin-requirements-can-now-restrict-web-search-modes-and-define-netwo|Enterprise/admin requirements can now restrict web search modes and define network…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-02-11-2-editor-experience-changes-in-rust-v0-99-0|2 Editor Experience changes in rust-v0.99.0]] · Editor Experience
- [[Changes/Codex CLI/2026-02-11-11294-chore-put-crypto-provider-logic-in-a-shared-crate-bolinfest|♯11294 chore: put crypto provider logic in a shared crate @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-02-11-11336-always-expose-view-image-and-return-unsupported-image-input-error-aibrahim|♯11336 Always expose view_image and return unsupported image-input error @aibrahim-oai]] · Multimodal Input
- [[Changes/Codex CLI/2026-02-11-10-agent-mode-changes-in-rust-v0-99-0|10 Agent Mode changes in rust-v0.99.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-11-4-mobile-and-desktop-changes-in-rust-v0-99-0|4 Mobile and Desktop changes in rust-v0.99.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-11-8-interface-experience-changes-in-rust-v0-99-0|8 Interface Experience changes in rust-v0.99.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-11-added-statusline-to-configure-which-metadata-appears-in-the-tui-footer-interacti|Added /statusline to configure which metadata appears in the TUI footer interactively]] · Other changes
- [[Changes/Codex CLI/2026-02-11-116-other-changes-in-rust-v0-99-0|116 other changes in rust-v0.99.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-10 · Gemini CLI · [[Changes/Gemini CLI/2026-02-10-docs-document-gemini-cli-home-environment-variable-by-adamfweidman-in-https-gith|docs: document GEMINI_CLI_HOME environment variable]]
- Later: 2026-02-11 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-11-2-model-support-changes-in-v0-0-407|2 Model Support changes in v0.0.407]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-11-97f092&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-11-15-model-support-changes-in-rust-v0-99-0.md%0ACard%20ID%3A%20codex-cli-2026-02-11-97f092%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.99.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->