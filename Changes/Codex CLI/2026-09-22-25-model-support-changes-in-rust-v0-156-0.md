---
card_id: codex-cli-2026-09-22-e3d46f
date: '2026-09-22'
description: 'Codex CLI · 2026-09-22 · Model Support: 25 changes in 0.156.0 — #44650
  Enforce managed model provider selection and definitions @alexsong-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1352
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: db250aff9cae4649f55a3ee30a3c24a8fbcebf433045f879c893a3649b4cbd9d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-22-e3d46f
  comparison: ''
  date: '2026-09-22'
  description: 'Codex CLI — 0.156.0: 25 Model Support changes'
  evidence:
  - quote: '#44650 Enforce managed model provider selection and definitions @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44656 Attribute turn metrics to the models used during the turn @eternal-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44675 Refresh global instructions at model-request boundaries @vkg-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44883 Reject token-budget history notes for unsupported starting models
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44893 Expose available access programs in model discovery @faizan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#44930 Embed friendly instructions in bundled GPT-5.4 and GPT-5.5 @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45831 Allow session-only model and reasoning selection in the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45915 Make Code Mode wrappers transparent to Guardian model policies
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45928 Bound model catalog decode errors and classify request timeouts
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#45933 Avoid redundant model catalog lookups in reused Guardian reviewers
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46026 Centralize model-message resolution and rendering in `codex-prompts`
      @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46281 Connect app-server workspace discovery to model request routing
      @acrognale-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46291 Filter saved reasoning overrides from requests when disabled @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46292 Preserve selected reasoning effort for synchronous Guardian reviews
      @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46324 Broaden compaction fallback to the current model @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46487 Keep TUI exploration grouped across reasoning and nonzero exits
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46503 Use catalog model display names throughout the TUI @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46508 Refresh the model catalog before turns after auth changes @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46519 Use paused time in sampler and model catalog timeout tests @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46530 Gate reasoning effort updates on explicit model support @felixxia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46533 Disable reasoning summaries by default for new TUI threads @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46561 Support explicit provider model catalog URLs @andrewgu-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46565 Preserve reasoning order in TUI activity groups @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46711 Align persisted TUI activity groups and reasoning with live output
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  - quote: '#46917 Enforce current provider requirements for the model catalog @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.156.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 25-model-support-changes-in-rust-v0-156-0
  source_release: codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4
  source_type: github_releases
  theme: model-support
  title: 25 Model Support changes in rust-v0.156.0
  type: change
related_changes:
- '[[Changes/Claude/2026-09-22-claude-opus-5-5-launch|Claude Opus 5.5 launch]]'
- '[[Changes/Claude Code/2026-09-22-5-model-support-changes-in-v2-1-280|5 Model Support
  changes in v2.1.280]]'
- '[[Changes/Cline/2026-09-22-3-model-support-changes-in-v4-1-20|3 Model Support changes
  in v4.1.20]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4]]'
source_type: github_releases
theme: model-support
title: 25 Model Support changes in rust-v0.156.0
type: change
---

<!-- chronolog:begin region="header" -->
# 25 Model Support changes in rust-v0.156.0

**Codex CLI** · 2026-09-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.156.0) · from [[Releases/Codex CLI/codex-cli-2026-09-22-rust-v0-156-0-github-394061815-b23dd5f4|0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #44650 Enforce managed model provider selection and definitions @alexsong-oai

> #44656 Attribute turn metrics to the models used during the turn @eternal-openai

> #44675 Refresh global instructions at model-request boundaries @vkg-oai

> #44883 Reject token-budget history notes for unsupported starting models @jif-oai

> #44893 Expose available access programs in model discovery @faizan-oai

> #44930 Embed friendly instructions in bundled GPT-5.4 and GPT-5.5 @rhan-oai

> #45831 Allow session-only model and reasoning selection in the TUI @etraut-openai

> #45915 Make Code Mode wrappers transparent to Guardian model policies @jif-oai

> #45928 Bound model catalog decode errors and classify request timeouts @jif-oai

> #45933 Avoid redundant model catalog lookups in reused Guardian reviewers @jif-oai

> #46026 Centralize model-message resolution and rendering in `codex-prompts` @rhan-oai

> #46281 Connect app-server workspace discovery to model request routing @acrognale-oai

> #46291 Filter saved reasoning overrides from requests when disabled @felixxia-oai

> #46292 Preserve selected reasoning effort for synchronous Guardian reviews @felixxia-oai

> #46324 Broaden compaction fallback to the current model @aibrahim-oai

> #46487 Keep TUI exploration grouped across reasoning and nonzero exits @etraut-openai

> #46503 Use catalog model display names throughout the TUI @etraut-openai

> #46508 Refresh the model catalog before turns after auth changes @jif-oai

> #46519 Use paused time in sampler and model catalog timeout tests @jif-oai

> #46530 Gate reasoning effort updates on explicit model support @felixxia-oai

> #46533 Disable reasoning summaries by default for new TUI threads @celia-oai

> #46561 Support explicit provider model catalog URLs @andrewgu-oai

> #46565 Preserve reasoning order in TUI activity groups @etraut-openai

> #46711 Align persisted TUI activity groups and reasoning with live output @etraut-openai

> #46917 Enforce current provider requirements for the model catalog @alexsong-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.156.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13 Account and Access changes in rust-v0.156.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-22-32-interface-experience-changes-in-rust-v0-156-0|32 Interface Experience changes in rust-v0.156.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-22-2-search-and-browsing-changes-in-rust-v0-156-0|2 Search and Browsing changes in rust-v0.156.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-09-22-46027-document-and-test-wildcards-in-network-proxy-domain-patterns-viyatb-oai|♯46027 Document and test ? wildcards in network proxy domain patterns @viyatb-oai]] · Files and Data
- [[Changes/Codex CLI/2026-09-22-42-apps-and-integrations-changes-in-rust-v0-156-0|42 Apps and Integrations changes in rust-v0.156.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-22-45544-discourage-logging-full-image-generation-results-gan-tu|♯45544 Discourage logging full image generation results @Gan-Tu]] · Image Generation
- [[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context Window changes in rust-v0.156.0]] · Context Window
- [[Changes/Codex CLI/2026-09-22-45849-preserve-the-app-server-shutdown-signal-future-across-loop-iterations-jger|♯45849 Preserve the app-server shutdown signal future across loop iterations @jgershen-oai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-22-11-mobile-and-desktop-changes-in-rust-v0-156-0|11 Mobile and Desktop changes in rust-v0.156.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-22-34-agent-mode-changes-in-rust-v0-156-0|34 Agent Mode changes in rust-v0.156.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-22-46040-default-tui-animations-off-when-a-screen-reader-is-detected-etraut-openai|♯46040 Default TUI animations off when a screen reader is detected @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-09-22-9-collaboration-changes-in-rust-v0-156-0|9 Collaboration changes in rust-v0.156.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-22-6-editor-experience-changes-in-rust-v0-156-0|6 Editor Experience changes in rust-v0.156.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-22-17-voice-and-audio-changes-in-rust-v0-156-0|17 Voice and Audio changes in rust-v0.156.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-22-45960-tag-memory-usage-telemetry-with-the-memory-version-jif-oai|♯45960 Tag memory usage telemetry with the memory version @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-22-22-developer-workflow-changes-in-rust-v0-156-0|22 Developer Workflow changes in rust-v0.156.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-22-248-other-changes-in-rust-v0-156-0|248 other changes in rust-v0.156.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-22 · Cline · [[Changes/Cline/2026-09-22-3-model-support-changes-in-v4-1-20|3 Model Support changes in v4.1.20]]
- Later: 2026-09-22 · Google Antigravity · [[Changes/Google Antigravity/2026-09-22-you-can-now-attach-microsoft-office-documents-word-excel-and-powerpoint-to-a-pro|You can now attach Microsoft Office documents (Word, Excel, and PowerPoint)…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-22-e3d46f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-22-25-model-support-changes-in-rust-v0-156-0.md%0ACard%20ID%3A%20codex-cli-2026-09-22-e3d46f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.156.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->