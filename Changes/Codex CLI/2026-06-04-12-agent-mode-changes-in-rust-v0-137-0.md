---
card_id: codex-cli-2026-06-04-b76c2b
date: '2026-06-04'
description: 'Codex CLI · 2026-06-04 · Agent Mode: 12 changes in 0.137.0 — Multi-agent
  v2 keeps runtime choice with each thread and exposes cleaner follow-up and metadata…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1064
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4706a1ea549a857f023efc6e638d35bb9f049283323d7cd2bd726a0cbcb8accd
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-04-b76c2b
  comparison: ''
  date: '2026-06-04'
  description: 'Codex CLI — 0.137.0: 12 Agent Mode changes'
  evidence:
  - quote: 'Multi-agent v2 keeps runtime choice with each thread and exposes cleaner
      follow-up and metadata defaults for spawned agents (#25266, #25636, #25720,
      #25721, #25722, #25841, #26114).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: 'Moved repo review rules and contributor conventions into `AGENTS.md`,
      including Rust test-module layout and Python 3 compatibility guidance (#25682,
      #25690, #25738).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25266 Set multi-agent v2 dogfood defaults @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#23763 Preserve auto-review approval policy in codex exec @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25636 [codex] Rename multi-agent v2 assign_task to followup_task @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25720 Add multi-agent runtime metadata types @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25721 Persist multi-agent runtime metadata @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25722 Resolve per-thread multi-agent runtime @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25841 session: keep startup prewarm aligned with resolved multi-agent
      runtime @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#25723 Test remote multi-agent runtime selector override @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26114 feat: default hide_spawn_agent_metadata to true @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  - quote: '#26144 Reject MAv2 close_agent self-targets @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.137.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 12-agent-mode-changes-in-rust-v0-137-0
  source_release: codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece
  source_type: github_releases
  theme: agent-mode
  title: 12 Agent Mode changes in rust-v0.137.0
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-06-03-2-agent-mode-changes-in-kimi-code-0-9-0|2 Agent
  Mode changes in Kimi Code 0.9.0]]'
- '[[Changes/Ollama/2026-06-03-nemotron-3-ultra-https-ollama-com-library-nemotron-3-ultra-nvidia-nemotron-3-ult|Nemotron-3-Ultra((source
  link) NVIDIA Nemotron 3…]]'
- '[[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode
  changes in v2.1.163]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece]]'
source_type: github_releases
theme: agent-mode
title: 12 Agent Mode changes in rust-v0.137.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Agent Mode changes in rust-v0.137.0

**Codex CLI** · 2026-06-04 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.137.0) · from [[Releases/Codex CLI/codex-cli-2026-06-04-rust-v0-137-0-github-334076532-fadfeece|0.137.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Multi-agent v2 keeps runtime choice with each thread and exposes cleaner follow-up and metadata defaults for spawned agents (#25266, #25636, #25720, #25721, #25722, #25841, #26114).

> Moved repo review rules and contributor conventions into `AGENTS.md`, including Rust test-module layout and Python 3 compatibility guidance (#25682, #25690, #25738).

> #25266 Set multi-agent v2 dogfood defaults @jif-oai

> #23763 Preserve auto-review approval policy in codex exec @won-openai

> #25636 [codex] Rename multi-agent v2 assign_task to followup_task @jif-oai

> #25720 Add multi-agent runtime metadata types @jif-oai

> #25721 Persist multi-agent runtime metadata @jif-oai

> #25722 Resolve per-thread multi-agent runtime @jif-oai

> #25841 session: keep startup prewarm aligned with resolved multi-agent runtime @jif-oai

> #25723 Test remote multi-agent runtime selector override @jif-oai

> #26114 feat: default hide_spawn_agent_metadata to true @jif-oai

> #26144 Reject MAv2 close_agent self-targets @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.137.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-04-6-developer-workflow-changes-in-rust-v0-137-0|6 Developer Workflow changes in rust-v0.137.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-04-25702-codex-enable-parallel-standalone-web-search-calls-sayan-oai|♯25702 codex enable parallel standalone web search calls @sayan-oai]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-04-3-image-generation-changes-in-rust-v0-137-0|3 Image Generation changes in rust-v0.137.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-04-2-interface-experience-changes-in-rust-v0-137-0|2 Interface Experience changes in rust-v0.137.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-04-19-apps-and-integrations-changes-in-rust-v0-137-0|19 Apps and Integrations changes in rust-v0.137.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-04-2-enterprise-and-administration-changes-in-rust-v0-137-0|2 Enterprise and Administration changes in rust-v0.137.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-06-04-local-session-history-is-safer-for-compressed-rollouts-renamed-titles-pathless-s|Local session history is safer for compressed rollouts, renamed titles, pathless…]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-06-04-4-collaboration-changes-in-rust-v0-137-0|4 Collaboration changes in rust-v0.137.0]] · Collaboration
- [[Changes/Codex CLI/2026-06-04-3-context-window-changes-in-rust-v0-137-0|3 Context Window changes in rust-v0.137.0]] · Context Window
- [[Changes/Codex CLI/2026-06-04-2-mobile-and-desktop-changes-in-rust-v0-137-0|2 Mobile and Desktop changes in rust-v0.137.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-04-25682-codex-document-out-of-line-test-module-convention-anp-oai|♯25682 codex document out-of-line test module convention @anp-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-04-3-model-support-changes-in-rust-v0-137-0|3 Model Support changes in rust-v0.137.0]] · Model Support
- [[Changes/Codex CLI/2026-06-04-8-safety-and-privacy-changes-in-rust-v0-137-0|8 Safety and Privacy changes in rust-v0.137.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-04-69-other-changes-in-rust-v0-137-0|69 other changes in rust-v0.137.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-04 · Claude Code · [[Changes/Claude Code/2026-06-04-2-agent-mode-changes-in-v2-1-163|2 Agent Mode changes in v2.1.163]]
- Later: 2026-06-04 · Cursor · [[Changes/Cursor/2026-06-04-added-the-ability-for-agents-to-embed-buttons-in-canvases-that-will-run-a-specif|Added the ability for agents to embed buttons in canvases that will run a specific…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-04-b76c2b&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-04-12-agent-mode-changes-in-rust-v0-137-0.md%0ACard%20ID%3A%20codex-cli-2026-06-04-b76c2b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.137.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->