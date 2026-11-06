---
card_id: codex-cli-2026-09-28-1b63bd
date: '2026-09-28'
description: 'Codex CLI · 2026-09-28 · Apps and Integrations: 13 changes in 0.158.0
  — #47610 Use native POSIX spawning for command hooks @charliemarsh-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 37d84f81f553d6f50b534c9370bfba5dd4940b1fcb96592ec93ac54dda335d90
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-28-1b63bd
  comparison: ''
  date: '2026-09-28'
  description: 'Codex CLI — 0.158.0: 13 Apps and Integrations changes'
  evidence:
  - quote: '#47610 Use native POSIX spawning for command hooks @charliemarsh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47647 Apply Guardian computer-use review to the Browser connector @johnl-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47662 Expose tool dispatch and timing observations to extensions @euroelessar'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47677 Support model catalog overrides for MCP resource tool specs @rhan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47820 Add integration coverage for host agent controllers @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47858 Validate loaded plugins outside the cache lock @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47899 Add diagnostic reasons to MCP attribution errors @peilin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47935 Allow cached catalogs to satisfy MCP startup readiness @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47936 Make MCP and Code Mode input schema budgets configurable @vivi'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47939 Separate selected plugin identities from MCP contributions @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47981 Prepare MCP calls directly from advertised tool identities @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#47988 Reuse MCP handlers across equivalent bindings @hlevy-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  - quote: '#48035 Remove plugin extension metadata from discovery and summaries @victor-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.158.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 13-apps-and-integrations-changes-in-rust-v0-158-0
  source_release: codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7
  source_type: github_releases
  theme: apps-integrations
  title: 13 Apps and Integrations changes in rust-v0.158.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-25-9-apps-and-integrations-changes-in-rust-v0-157-0|9
  Apps and Integrations changes in rust-v0.157.0]]'
- '[[Changes/OpenHands/2026-09-25-chore-deps-bump-openhands-extensions-to-0-24-0-by-devinvinson-in-https-github-co|chore(deps):
  bump @openhands/extensions to 0.24.0]]'
- '[[Changes/Claude Code/2026-09-28-8-apps-and-integrations-changes-in-v2-1-284|8
  Apps and Integrations changes in v2.1.284]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7]]'
source_type: github_releases
theme: apps-integrations
title: 13 Apps and Integrations changes in rust-v0.158.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Apps and Integrations changes in rust-v0.158.0

**Codex CLI** · 2026-09-28 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.158.0) · from [[Releases/Codex CLI/codex-cli-2026-09-28-rust-v0-158-0-github-397962047-f52f49e7|0.158.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #47610 Use native POSIX spawning for command hooks @charliemarsh-oai

> #47647 Apply Guardian computer-use review to the Browser connector @johnl-oai

> #47662 Expose tool dispatch and timing observations to extensions @euroelessar

> #47677 Support model catalog overrides for MCP resource tool specs @rhan-oai

> #47820 Add integration coverage for host agent controllers @jif-oai

> #47858 Validate loaded plugins outside the cache lock @jif-oai

> #47899 Add diagnostic reasons to MCP attribution errors @peilin-openai

> #47935 Allow cached catalogs to satisfy MCP startup readiness @hlevy-openai

> #47936 Make MCP and Code Mode input schema budgets configurable @vivi

> #47939 Separate selected plugin identities from MCP contributions @sayan-oai

> #47981 Prepare MCP calls directly from advertised tool identities @hlevy-openai

> #47988 Reuse MCP handlers across equivalent bindings @hlevy-openai

> #48035 Remove plugin extension metadata from discovery and summaries @victor-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.158.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-28-47975-prevent-stale-voice-answers-from-reappearing-during-speech-recovery-etraut|♯47975 Prevent stale voice answers from reappearing during speech recovery @etraut-openai]] · Voice and Audio
- [[Changes/Codex CLI/2026-09-28-8-account-and-access-changes-in-rust-v0-158-0|8 Account and Access changes in rust-v0.158.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-28-3-mobile-and-desktop-changes-in-rust-v0-158-0|3 Mobile and Desktop changes in rust-v0.158.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-09-28-3-memory-and-personalization-changes-in-rust-v0-158-0|3 Memory and Personalization changes in rust-v0.158.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-09-28-2-collaboration-changes-in-rust-v0-158-0|2 Collaboration changes in rust-v0.158.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model Support changes in rust-v0.158.0]] · Model Support
- [[Changes/Codex CLI/2026-09-28-3-image-generation-changes-in-rust-v0-158-0|3 Image Generation changes in rust-v0.158.0]] · Image Generation
- [[Changes/Codex CLI/2026-09-28-4-editor-experience-changes-in-rust-v0-158-0|4 Editor Experience changes in rust-v0.158.0]] · Editor Experience
- [[Changes/Codex CLI/2026-09-28-6-interface-experience-changes-in-rust-v0-158-0|6 Interface Experience changes in rust-v0.158.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-28-47984-add-multi-agent-spawn-latency-and-failure-metrics-owenlin0|♯47984 Add multi-agent spawn latency and failure metrics @owenlin0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-09-28-14-developer-workflow-changes-in-rust-v0-158-0|14 Developer Workflow changes in rust-v0.158.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-09-28-11-agent-mode-changes-in-rust-v0-158-0|11 Agent Mode changes in rust-v0.158.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-28-17-context-window-changes-in-rust-v0-158-0|17 Context Window changes in rust-v0.158.0]] · Context Window
- [[Changes/Codex CLI/2026-09-28-96-other-changes-in-rust-v0-158-0|96 other changes in rust-v0.158.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-8-apps-and-integrations-changes-in-v2-1-284|8 Apps and Integrations changes in v2.1.284]]
- Later: 2026-09-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-28-4-apps-and-integrations-changes-in-v1-0-89|4 Apps and Integrations changes in v1.0.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-28-1b63bd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-28-13-apps-and-integrations-changes-in-rust-v0-158-0.md%0ACard%20ID%3A%20codex-cli-2026-09-28-1b63bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.158.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->