---
card_id: codex-cli-2026-04-15-c7138a
date: '2026-04-15'
description: 'Codex CLI · 2026-04-15 · Agent Mode: 7 changes in 0.121.0 — #17385 Add
  use_agent_identity feature flag @adrian-openai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1014
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4340751aa00a541cc71b35576772f18ebe1289a230e89c14200fbf0cb5326aa5
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-15-c7138a
  comparison: ''
  date: '2026-04-15'
  description: 'Codex CLI — 0.121.0: 7 Agent Mode changes'
  evidence:
  - quote: '#17385 Add use_agent_identity feature flag @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17483 Update issue labeler agent labels @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17506 Expose instruction sources (AGENTS.md) via app server @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17247 Make forked agent spawns keep parent model config @friel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17855 support plugins in external agent config migration @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17884 Fix clippy warnings in external agent config migration @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  - quote: '#17386 Register agent identities behind use_agent_identity @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.121.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-agent-mode-changes-in-rust-v0-121-0
  source_release: codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03
  source_type: github_releases
  theme: agent-mode
  title: 7 Agent Mode changes in rust-v0.121.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-04-13-elevenagents|ElevenAgents]]'
- '[[Changes/Cursor/2026-04-14-ask-a-quick-side-question-without-derailing-the-agent-s-main-task-btw-allows-you|/btw
  support in CLI]]'
- '[[Changes/Gemini CLI/2026-04-14-6-agent-mode-changes-in-v0-38-0|6 Agent Mode changes
  in v0.38.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03]]'
source_type: github_releases
theme: agent-mode
title: 7 Agent Mode changes in rust-v0.121.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Agent Mode changes in rust-v0.121.0

**Codex CLI** · 2026-04-15 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.121.0) · from [[Releases/Codex CLI/codex-cli-2026-04-15-rust-v0-121-0-github-309557036-bb698f03|0.121.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #17385 Add use_agent_identity feature flag @adrian-openai

> #17483 Update issue labeler agent labels @etraut-openai

> #17506 Expose instruction sources (AGENTS.md) via app server @etraut-openai

> #17247 Make forked agent spawns keep parent model config @friel-openai

> #17855 support plugins in external agent config migration @alexsong-oai

> #17884 Fix clippy warnings in external agent config migration @canvrno-oai

> #17386 Register agent identities behind use_agent_identity @adrian-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.121.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-15-3-model-support-changes-in-rust-v0-121-0|3 Model Support changes in rust-v0.121.0]] · Model Support
- [[Changes/Codex CLI/2026-04-15-17684-adjust-default-tool-search-result-caps-malone-oai|♯17684 Adjust default tool search result caps @malone-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-15-9-memory-and-personalization-changes-in-rust-v0-121-0|9 Memory and Personalization changes in rust-v0.121.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-15-9-apps-and-integrations-changes-in-rust-v0-121-0|9 Apps and Integrations changes in rust-v0.121.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-15-4-context-window-changes-in-rust-v0-121-0|4 Context Window changes in rust-v0.121.0]] · Context Window
- [[Changes/Codex CLI/2026-04-15-4-developer-workflow-changes-in-rust-v0-121-0|4 Developer Workflow changes in rust-v0.121.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-15-17640-fix-stability-exec-server-jif-oai|♯17640 fix: stability exec server @jif-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-04-15-added-realtime-and-app-server-apis-for-output-modality-transcript-completion-eve|Added realtime and app-server APIs for output modality, transcript completion…]] · Editor Experience
- [[Changes/Codex CLI/2026-04-15-17414-fix-thread-list-cwd-filtering-for-windows-verbatim-paths-etraut-openai|♯17414 Fix thread/list cwd filtering for Windows verbatim paths @etraut-openai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-15-10-safety-and-privacy-changes-in-rust-v0-121-0|10 Safety and Privacy changes in rust-v0.121.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-15-17717-codex-refactor-marketplace-add-into-shared-core-flow-xli-oai|♯17717 codex Refactor marketplace add into shared core flow @xli-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-15-99-other-changes-in-rust-v0-121-0|99 other changes in rust-v0.121.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-14 · Gemini CLI · [[Changes/Gemini CLI/2026-04-14-6-agent-mode-changes-in-v0-38-0|6 Agent Mode changes in v0.38.0]]
- Later: 2026-04-15 · Windsurf · [[Changes/Windsurf/2026-04-15-devin-in-windsurf|Devin in Windsurf]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-15-c7138a&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-15-7-agent-mode-changes-in-rust-v0-121-0.md%0ACard%20ID%3A%20codex-cli-2026-04-15-c7138a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.121.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->