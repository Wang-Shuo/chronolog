---
card_id: codex-cli-2026-06-08-a39250
date: '2026-06-08'
description: 'Codex CLI · 2026-06-08 · Model Support: 6 changes in 0.138.0 — Local
  image attachments and standalone image generations now expose their saved file paths
  to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1246
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a0d90ece157f3a0836b2afb0e4e773e2afbb2101be12d5bd10dcd7317f8c4a15
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-08-a39250
  comparison: ''
  date: '2026-06-08'
  description: 'Codex CLI — 0.138.0: 6 Model Support changes'
  evidence:
  - quote: 'Local image attachments and standalone image generations now expose their
      saved file paths to the model, which makes follow-up edits and file references
      more reliable. (#25944, #25947)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: 'Reasoning effort selection is more flexible: the TUI adds fallback shortcuts
      for terminals that miss `Alt` bindings, and model-defined effort levels now
      flow through in the order advertised by the model. (#25623, #26444, #26446)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25944 Expose local image paths to models @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#25623 fix(tui): add reasoning effort fallback shortcuts @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26444 [codex] Support model-defined reasoning efforts @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  - quote: '#26446 [codex] Use model-advertised reasoning effort order @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.138.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-model-support-changes-in-rust-v0-138-0
  source_release: codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a
  source_type: github_releases
  theme: model-support
  title: 6 Model Support changes in rust-v0.138.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-06-3-model-support-changes-in-v2-1-166|3 Model Support
  changes in v2.1.166]]'
- '[[Changes/ChatGPT/2026-06-08-long-press-send-to-choose-a-model-users-on-paid-plans-can-now-long-press-the-sen|Long-press
  send to choose a model]]'
- '[[Changes/Claude Code/2026-06-08-added-a-disablebundledskills-setting-and-claude-code-disable-bundled-skills-envi|Added
  a disableBundledSkills setting and CLAUDE_CODE_DISABLE_BUNDLED_SKILLS…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a]]'
source_type: github_releases
theme: model-support
title: 6 Model Support changes in rust-v0.138.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Model Support changes in rust-v0.138.0

**Codex CLI** · 2026-06-08 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.138.0) · from [[Releases/Codex CLI/codex-cli-2026-06-08-rust-v0-138-0-github-336275797-115d015a|0.138.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Local image attachments and standalone image generations now expose their saved file paths to the model, which makes follow-up edits and file references more reliable. (#25944, #25947)

> Reasoning effort selection is more flexible: the TUI adds fallback shortcuts for terminals that miss `Alt` bindings, and model-defined effort levels now flow through in the order advertised by the model. (#25623, #26444, #26446)

> #25944 Expose local image paths to models @won-openai

> #25623 fix(tui): add reasoning effort fallback shortcuts @fcoury-oai

> #26444 [codex] Support model-defined reasoning efforts @aibrahim-oai

> #26446 [codex] Use model-advertised reasoning effort order @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.138.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-08-6-safety-and-privacy-changes-in-rust-v0-138-0|6 Safety and Privacy changes in rust-v0.138.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-08-2-image-generation-changes-in-rust-v0-138-0|2 Image Generation changes in rust-v0.138.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-08-4-mobile-and-desktop-changes-in-rust-v0-138-0|4 Mobile and Desktop changes in rust-v0.138.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-08-2-account-and-access-changes-in-rust-v0-138-0|2 Account and Access changes in rust-v0.138.0]] · Account and Access
- [[Changes/Codex CLI/2026-06-08-7-developer-workflow-changes-in-rust-v0-138-0|7 Developer Workflow changes in rust-v0.138.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-08-19-apps-and-integrations-changes-in-rust-v0-138-0|19 Apps and Integrations changes in rust-v0.138.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-08-4-context-window-changes-in-rust-v0-138-0|4 Context Window changes in rust-v0.138.0]] · Context Window
- [[Changes/Codex CLI/2026-06-08-8-agent-mode-changes-in-rust-v0-138-0|8 Agent Mode changes in rust-v0.138.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-08-3-editor-experience-changes-in-rust-v0-138-0|3 Editor Experience changes in rust-v0.138.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-08-54-other-changes-in-rust-v0-138-0|54 other changes in rust-v0.138.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-08 · Claude Code · [[Changes/Claude Code/2026-06-08-added-a-disablebundledskills-setting-and-claude-code-disable-bundled-skills-envi|Added a disableBundledSkills setting and CLAUDE_CODE_DISABLE_BUNDLED_SKILLS…]]
- Later: 2026-06-09 · Claude Code · [[Changes/Claude Code/2026-06-09-introducing-claude-fable-5-a-mythos-class-model-that-we-ve-made-safe-for-general|Introducing Claude Fable 5: a Mythos-class model that we’ve made safe for general use]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-08-a39250&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-08-6-model-support-changes-in-rust-v0-138-0.md%0ACard%20ID%3A%20codex-cli-2026-06-08-a39250%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.138.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->