---
card_id: dify-2026-09-10-9414e0
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Memory and Personalization: 2 changes in v1.17.1
  - Bug Fixes and Improvements — **Chatflow Agent V2 forgot everything between turns.**…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1148
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 21bf02d864d3eda17da3a191c8ab145bed53783c7f953ef15f99af7a37982360
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-9414e0
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 2 Memory and Personalization
    changes'
  evidence:
  - quote: '**Chatflow Agent V2 forgot everything between turns.** Sessions are now
      keyed by `conversation_id`, so memory persists across a conversation. A follow-up
      fixed the related case where publishing a new Agent roster version mid-conversation
      paired a new configuration with the previous participant and failed generation
      validation — existing conversations now stay pinned to the version they started
      on, and only new conversations pick up the current one. (#41871, #42105)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**A hard kill silently and permanently destroys vector recall.** Weaviate
      holds its HNSW index in memory and persists it through a commit log; `docker
      kill`, `docker rm -f`, an OOM kill, or a stop that exceeds Docker''s grace period
      can leave that log incomplete. Measured on `1.39.2`, after a hard kill the object
      count, object listing, BM25 search, and fetch-by-ID all looked healthy while
      `near_vector` could reach only 680 of 700 objects. Nothing is logged, and it
      does not heal — the only repair is re-indexing the knowledge base. Always stop
      with `docker compose stop -t -1 weaviate`.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 2-memory-and-personalization-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: memory
  title: 2 Memory and Personalization changes in 1.17.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10
  Memory and Personalization changes in v2026.9.3]]'
- '[[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2
  Memory and Personalization changes in rust-v0.154.0]]'
- '[[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2
  Memory and Personalization changes in v2.1.268]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: memory
title: 2 Memory and Personalization changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Memory and Personalization changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Chatflow Agent V2 forgot everything between turns.** Sessions are now keyed by `conversation_id`, so memory persists across a conversation. A follow-up fixed the related case where publishing a new Agent roster version mid-conversation paired a new configuration with the previous participant and failed generation validation — existing conversations now stay pinned to the version they started on, and only new conversations pick up the current one. (#41871, #42105)

> **A hard kill silently and permanently destroys vector recall.** Weaviate holds its HNSW index in memory and persists it through a commit log; `docker kill`, `docker rm -f`, an OOM kill, or a stop that exceeds Docker's grace period can leave that log incomplete. Measured on `1.39.2`, after a hard kill the object count, object listing, BM25 search, and fetch-by-ID all looked healthy while `near_vector` could reach only 680 of 700 objects. Nothing is logged, and it does not heal — the only repair is re-indexing the knowledge base. Always stop with `docker compose stop -t -1 weaviate`.

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Safety and Privacy
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2 Memory and Personalization changes in v2.1.268]]
- Later: 2026-09-11 · OpenClaw · [[Changes/OpenClaw/2026-09-11-14-memory-and-personalization-changes-in-v2026-9-4|14 Memory and Personalization changes in v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-9414e0&body=Card%3A%20Changes%2FDify%2F2026-09-10-2-memory-and-personalization-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-9414e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->