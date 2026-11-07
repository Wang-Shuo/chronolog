---
card_id: codex-cli-2026-04-20-5e7a71
date: '2026-04-20'
description: 'Codex CLI · 2026-04-20 · Agent Mode: 10 changes in 0.122.0 — Refactored
  config loading and `AGENTS.md` discovery behind narrower filesystem and manager…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1019
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a419392b128e5054c1e2d8ccfe9e88f36e1a7ba6bfaf3fe4260f4f0276dffd9a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-20-5e7a71
  comparison: ''
  date: '2026-04-20'
  description: 'Codex CLI — 0.122.0: 10 Agent Mode changes'
  evidence:
  - quote: 'Refactored config loading and `AGENTS.md` discovery behind narrower filesystem
      and manager abstractions (#18209, #18035).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18035 Refactor AGENTS.md discovery into AgentsMdManager @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17387 Register agent tasks behind use_agent_identity @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18169 Use codex-auto-review for guardian reviews @jeffsharris'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18021 Guardian -> Auto-Review @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18369 Feat/auto review dev message marker @won-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17978 Persist and prewarm agent tasks per thread @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#17980 [codex] Use AgentAssertion downstream behind use_agent_identity
      @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18644 feat: add mem 2 agent header @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  - quote: '#18654 fix: exec policy loading for sub-agents @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.122.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 10-agent-mode-changes-in-rust-v0-122-0
  source_release: codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e
  source_type: github_releases
  theme: agent-mode
  title: 10 Agent Mode changes in rust-v0.122.0
  type: change
related_changes:
- '[[Changes/Replit/2026-04-17-new-agent-modes-dropdown|New Agent modes dropdown]]'
- '[[Changes/Replit/2026-04-17-replit-agent-on-google-cloud-marketplace|Replit Agent
  on Google Cloud Marketplace]]'
- '[[Changes/Claude Code/2026-04-20-2-agent-mode-changes-in-v2-1-116|2 Agent Mode
  changes in v2.1.116]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e]]'
source_type: github_releases
theme: agent-mode
title: 10 Agent Mode changes in rust-v0.122.0
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Agent Mode changes in rust-v0.122.0

**Codex CLI** · 2026-04-20 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.122.0) · from [[Releases/Codex CLI/codex-cli-2026-04-20-rust-v0-122-0-github-311361536-9a010c0e|0.122.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Refactored config loading and `AGENTS.md` discovery behind narrower filesystem and manager abstractions (#18209, #18035).

> #18035 Refactor AGENTS.md discovery into AgentsMdManager @pakrym-oai

> #17387 Register agent tasks behind use_agent_identity @adrian-openai

> #18169 Use codex-auto-review for guardian reviews @jeffsharris

> #18021 Guardian -> Auto-Review @won-openai

> #18369 Feat/auto review dev message marker @won-openai

> #17978 Persist and prewarm agent tasks per thread @adrian-openai

> #17980 [codex] Use AgentAssertion downstream behind use_agent_identity @adrian-openai

> #18644 feat: add mem 2 agent header @jif-oai

> #18654 fix: exec policy loading for sub-agents @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.122.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-20-6-developer-workflow-changes-in-rust-v0-122-0|6 Developer Workflow changes in rust-v0.122.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-20-tool-discovery-and-image-generation-are-now-enabled-by-default-with-higher-detai|Tool discovery and image generation are now enabled by default, with higher-detail…]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-17153-launch-image-generation-by-default-won-openai|♯17153 Launch image generation by default @won-openai]] · Image Generation
- [[Changes/Codex CLI/2026-04-20-6-model-support-changes-in-rust-v0-122-0|6 Model Support changes in rust-v0.122.0]] · Model Support
- [[Changes/Codex CLI/2026-04-20-10-context-window-changes-in-rust-v0-122-0|10 Context Window changes in rust-v0.122.0]] · Context Window
- [[Changes/Codex CLI/2026-04-20-4-memory-and-personalization-changes-in-rust-v0-122-0|4 Memory and Personalization changes in rust-v0.122.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-20-18398-refactor-use-cloneable-async-channels-for-shared-receivers-bolinfest|♯18398 refactor: use cloneable async channels for shared receivers @bolinfest]] · Collaboration
- [[Changes/Codex CLI/2026-04-20-28-apps-and-integrations-changes-in-rust-v0-122-0|28 Apps and Integrations changes in rust-v0.122.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-20-plugin-workflows-now-include-tabbed-browsing-inline-enable-disable-toggles-marke|Plugin workflows now include tabbed browsing, inline enable/disable toggles…]] · Search and Browsing
- [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-04-20-2-interface-experience-changes-in-rust-v0-122-0|2 Interface Experience changes in rust-v0.122.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-20-2-mobile-and-desktop-changes-in-rust-v0-122-0|2 Mobile and Desktop changes in rust-v0.122.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-20-100-other-changes-in-rust-v0-122-0|100 other changes in rust-v0.122.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-04-20 · Claude Code · [[Changes/Claude Code/2026-04-20-2-agent-mode-changes-in-v2-1-116|2 Agent Mode changes in v2.1.116]]
- Later: 2026-04-20 · ElevenLabs · [[Changes/ElevenLabs/2026-04-20-elevenagents|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-20-5e7a71&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-20-10-agent-mode-changes-in-rust-v0-122-0.md%0ACard%20ID%3A%20codex-cli-2026-04-20-5e7a71%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.122.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->