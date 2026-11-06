---
card_id: codex-cli-2026-02-17-327a6e
date: '2026-02-17'
description: 'Codex CLI · 2026-02-17 · Model Support: 11 changes in 0.102.0 — Added
  a `model/rerouted` notification so clients can detect and render model reroute events…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1135
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0521d32ad9efe51e237326b10affb0141cc60f9ba426000eabba0526b618e018
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-17-327a6e
  comparison: ''
  date: '2026-02-17'
  description: 'Codex CLI — 0.102.0: 11 Model Support changes'
  evidence:
  - quote: Added a `model/rerouted` notification so clients can detect and render
      model reroute events explicitly. (#12001)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11636 Better error message for model limit hit. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#10671 Add js_repl_tools_only model and routing restrictions @fjord-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11679 fix: dont show NUX for upgrade-target models that are hidden @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11671 chore(core) Restrict model-suggested rules @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11793 fix: send unfiltered models over model/list @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11659 Handle model-switch base instructions after compaction @charley-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11672 feat(core): add structured network approval plumbing and policy
      decision model @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11884 fix: only emit unknown model warning on user turns @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#11833 Don''t allow model_supports_reasoning_summaries to disable reasoning
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  - quote: '#12001 Feat: add model reroute notification @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.102.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-model-support-changes-in-rust-v0-102-0
  source_release: codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0
  source_type: github_releases
  theme: model-support
  title: 11 Model Support changes in rust-v0.102.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-02-13-as-previously-announced-we-have-retired-gpt-4o-gpt-4-1-gpt-4-1-mini-and-openai-o|Retiring
  GPT-4o and other legacy models]]'
- '[[Changes/Cline/2026-02-13-ui-ux-fixes-with-minimax-model-family|UI/UX fixes with
  minimax model family]]'
- '[[Changes/Claude Code/2026-02-17-added-support-for-claude-sonnet-4-6|Added support
  for Claude Sonnet 4.6]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0|codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0]]'
source_type: github_releases
theme: model-support
title: 11 Model Support changes in rust-v0.102.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Model Support changes in rust-v0.102.0

**Codex CLI** · 2026-02-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.102.0) · from [[Releases/Codex CLI/codex-cli-2026-02-17-rust-v0-102-0-github-287401154-1bf3dbd0|0.102.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a `model/rerouted` notification so clients can detect and render model reroute events explicitly. (#12001)

> #11636 Better error message for model limit hit. @xl-openai

> #10671 Add js_repl_tools_only model and routing restrictions @fjord-oai

> #11679 fix: dont show NUX for upgrade-target models that are hidden @sayan-oai

> #11671 chore(core) Restrict model-suggested rules @dylan-hurd-oai

> #11793 fix: send unfiltered models over model/list @sayan-oai

> #11659 Handle model-switch base instructions after compaction @charley-oai

> #11672 feat(core): add structured network approval plumbing and policy decision model @viyatb-oai

> #11884 fix: only emit unknown model warning on user turns @sayan-oai

> #11833 Don't allow model_supports_reasoning_summaries to disable reasoning @etraut-openai

> #12001 Feat: add model reroute notification @shijie-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.102.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-17-3-developer-workflow-changes-in-rust-v0-102-0|3 Developer Workflow changes in rust-v0.102.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-17-15-apps-and-integrations-changes-in-rust-v0-102-0|15 Apps and Integrations changes in rust-v0.102.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-02-17-2-mobile-and-desktop-changes-in-rust-v0-102-0|2 Mobile and Desktop changes in rust-v0.102.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-17-9-safety-and-privacy-changes-in-rust-v0-102-0|9 Safety and Privacy changes in rust-v0.102.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-17-11860-fixed-screen-reader-regression-in-cli-etraut-openai|♯11860 Fixed screen reader regression in CLI @etraut-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-02-17-11224-chore-clarify-web-search-deprecation-notices-and-consolidate-tests-sayan-o|♯11224 chore: clarify web_search deprecation notices and consolidate tests @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-02-17-4-context-window-changes-in-rust-v0-102-0|4 Context Window changes in rust-v0.102.0]] · Context Window
- [[Changes/Codex CLI/2026-02-17-4-memory-and-personalization-changes-in-rust-v0-102-0|4 Memory and Personalization changes in rust-v0.102.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-17-3-interface-experience-changes-in-rust-v0-102-0|3 Interface Experience changes in rust-v0.102.0]] · Interface Experience
- [[Changes/Codex CLI/2026-02-17-7-agent-mode-changes-in-rust-v0-102-0|7 Agent Mode changes in rust-v0.102.0]] · Agent Mode
- [[Changes/Codex CLI/2026-02-17-59-other-changes-in-rust-v0-102-0|59 other changes in rust-v0.102.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-02-17 · Claude Code · [[Changes/Claude Code/2026-02-17-added-support-for-claude-sonnet-4-6|Added support for Claude Sonnet 4.6]]
- Later: 2026-02-17 · Codex CLI · [[Changes/Codex CLI/2026-02-17-11699-chore-rm-remote-models-fflag-sayan-oai|♯11699 chore: rm remote models fflag @sayan-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-17-327a6e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-17-11-model-support-changes-in-rust-v0-102-0.md%0ACard%20ID%3A%20codex-cli-2026-02-17-327a6e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.102.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->