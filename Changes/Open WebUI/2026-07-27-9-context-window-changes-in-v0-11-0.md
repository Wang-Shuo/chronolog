---
card_id: open-webui-2026-07-27-c867ae
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Context Window: 9 changes in v0.11.0 — \U0001F4CA
  **Chat status at a glance.** The slash menu now shows how full the context window
  is, and a…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1180
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4792860845a662fa82883f656d5a258097b43e6268d6a3bcd5aabbc1b9dd84f8
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-c867ae
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 9 Context Window changes'
  evidence:
  - quote: "\U0001F4CA **Chat status at a glance.** The slash menu now shows how full
      the context window is, and a new status command opens a panel with context usage,
      queued messages, running tasks, and the chat ID. [Commit](https://github.com/open-webui/open-webui/commit/7a9928ef172b7c280c377c86cb52957e39340158),
      [Commit](https://github.com/open-webui/open-webui/commit/263bbc77d803e83b9af4b04c0cae29705af5f072)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA9B **Model for summarizing long chats.** Administrators can now
      pick a dedicated model to write context compaction summaries, separate from
      the task model, with the conversation's own model used when none is chosen.
      [#26806](https://github.com/open-webui/open-webui/pull/26806), [#27051](https://github.com/open-webui/open-webui/issues/27051)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4CF **Context compaction token cap.** Administrators can now set
      a \"Token Cap\" that limits how high per-model context compaction thresholds
      are allowed to reach, giving finer control over long-conversation summarization.
      [Commit](https://github.com/open-webui/open-webui/commit/5c389ad93f0668d4bab717d14bd189b679338ef2),
      [Commit](https://github.com/open-webui/open-webui/commit/31996a5acfe1458720fa19f1b9fb4da95749b5e6),
      [Commit](https://github.com/open-webui/open-webui/commit/44c2a27ce0695d8e9c7e72f9a84dc325cb15096a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⚖️ **Retained messages after compaction.** Administrators can now set what
      share of recent messages survives when a long conversation is summarized, between
      a tenth and half of it. [Commit](https://github.com/open-webui/open-webui/commit/33cf3fbb7f017ab1b79dce5c5ca4d4e1c3092844),
      [#27050](https://github.com/open-webui/open-webui/issues/27050)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ✂️ **Context compaction turn boundaries.** Long-conversation compaction
      now summarizes only completed earlier turns instead of sometimes cutting through
      the middle of a single turn, keeping the current turn's tool calls and results
      intact. [#27035](https://github.com/open-webui/open-webui/issues/27035), [Commit](https://github.com/open-webui/open-webui/commit/959558fd82eb2a3c980231acd500b73ba4b698b3),
      [Commit](https://github.com/open-webui/open-webui/commit/17e6496538e5f3147203b7520012a985cab044b7)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA9F **System prompt through compaction.** The system message now
      stays at the front of the conversation when a long chat is summarized, instead
      of being folded into the summary and lost from that point on. [Commit](https://github.com/open-webui/open-webui/commit/70549c5c8a50315aa3bf909ebedea8cc3e602077),
      [Commit](https://github.com/open-webui/open-webui/commit/15688686af9dd73ec974e35f96a7ea24294dbe4f),
      [Commit](https://github.com/open-webui/open-webui/commit/44f4f9dce48f1ad2af0c5f3210fa5aa701bad624),
      [#26713](https://github.com/open-webui/open-webui/pull/26713), [#26710](https://github.com/open-webui/open-webui/issues/26710)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F7 **Context compaction continuity.** After a compaction, the
      retained recent messages now stay in the prompt on every following turn instead
      of disappearing after the first, preserving conversational continuity and prompt
      caching. [#27037](https://github.com/open-webui/open-webui/issues/27037), [Commit](https://github.com/open-webui/open-webui/commit/0c23466a3e9a1fb7d32875a0614f1ca8e583bc73),
      [Commit](https://github.com/open-webui/open-webui/commit/f730733bc44eff5812eff0e51ebca0bbcfa1bc6e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F51F **Context size after tool calls.** The context meter and long-conversation
      compaction now read the size of the latest request rather than adding up every
      call in a tool loop, and understand the counts reported by Ollama and llama.cpp
      as well as the OpenAI-style ones, so compaction no longer fires far below its
      threshold, or never at all, and the usage shown is no longer inflated. [Commit](https://github.com/open-webui/open-webui/commit/df94268e892cbb66675170a6c78846aef23f6e89),
      [Commit](https://github.com/open-webui/open-webui/commit/e8f2c123e63c9073c9ae4ee00573144ce6d4b2e9),
      [#27031](https://github.com/open-webui/open-webui/issues/27031), [#26752](https://github.com/open-webui/open-webui/pull/26752),
      [#24410](https://github.com/open-webui/open-webui/discussions/24410)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F68F **Stopping a reply when Redis is configured.** The stop button
      now actually halts generation on Redis-backed deployments, where the listener
      that carries stop requests between instances quietly died after a few idle seconds
      and left tokens streaming on, and a new \"REDIS_SOCKET_TIMEOUT\" setting controls
      that timeout. [#27104](https://github.com/open-webui/open-webui/pull/27104),
      [#26779](https://github.com/open-webui/open-webui/issues/26779)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 9-context-window-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: context-window
  title: 9 Context Window changes in v0.11.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-07-22-refactor-exclude-transient-ci-configuration-files-from-workspace-context-by-davi|Refactor:
  exclude transient CI configuration files from workspace context]]'
- '[[Changes/Cline/2026-07-24-add-claude-opus-5-across-the-anthropic-claude-code-bedrock-vertex-cline-and-open|Add
  Claude Opus 5 across the Anthropic, Claude Code, Bedrock, Vertex, Cline…]]'
- '[[Changes/Lovable/2026-07-25-leaked-api-keys-are-revoked-automatically|Leaked API
  keys are revoked automatically]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: context-window
title: 9 Context Window changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Context Window changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📊 **Chat status at a glance.** The slash menu now shows how full the context window is, and a new status command opens a panel with context usage, queued messages, running tasks, and the chat ID. [Commit](https://github.com/open-webui/open-webui/commit/7a9928ef172b7c280c377c86cb52957e39340158), [Commit](https://github.com/open-webui/open-webui/commit/263bbc77d803e83b9af4b04c0cae29705af5f072)

> 🪛 **Model for summarizing long chats.** Administrators can now pick a dedicated model to write context compaction summaries, separate from the task model, with the conversation's own model used when none is chosen. [#26806](https://github.com/open-webui/open-webui/pull/26806), [#27051](https://github.com/open-webui/open-webui/issues/27051)

> 📏 **Context compaction token cap.** Administrators can now set a "Token Cap" that limits how high per-model context compaction thresholds are allowed to reach, giving finer control over long-conversation summarization. [Commit](https://github.com/open-webui/open-webui/commit/5c389ad93f0668d4bab717d14bd189b679338ef2), [Commit](https://github.com/open-webui/open-webui/commit/31996a5acfe1458720fa19f1b9fb4da95749b5e6), [Commit](https://github.com/open-webui/open-webui/commit/44c2a27ce0695d8e9c7e72f9a84dc325cb15096a)

> ⚖️ **Retained messages after compaction.** Administrators can now set what share of recent messages survives when a long conversation is summarized, between a tenth and half of it. [Commit](https://github.com/open-webui/open-webui/commit/33cf3fbb7f017ab1b79dce5c5ca4d4e1c3092844), [#27050](https://github.com/open-webui/open-webui/issues/27050)

> ✂️ **Context compaction turn boundaries.** Long-conversation compaction now summarizes only completed earlier turns instead of sometimes cutting through the middle of a single turn, keeping the current turn's tool calls and results intact. [#27035](https://github.com/open-webui/open-webui/issues/27035), [Commit](https://github.com/open-webui/open-webui/commit/959558fd82eb2a3c980231acd500b73ba4b698b3), [Commit](https://github.com/open-webui/open-webui/commit/17e6496538e5f3147203b7520012a985cab044b7)

> 🪟 **System prompt through compaction.** The system message now stays at the front of the conversation when a long chat is summarized, instead of being folded into the summary and lost from that point on. [Commit](https://github.com/open-webui/open-webui/commit/70549c5c8a50315aa3bf909ebedea8cc3e602077), [Commit](https://github.com/open-webui/open-webui/commit/15688686af9dd73ec974e35f96a7ea24294dbe4f), [Commit](https://github.com/open-webui/open-webui/commit/44f4f9dce48f1ad2af0c5f3210fa5aa701bad624), [#26713](https://github.com/open-webui/open-webui/pull/26713), [#26710](https://github.com/open-webui/open-webui/issues/26710)

> 🧷 **Context compaction continuity.** After a compaction, the retained recent messages now stay in the prompt on every following turn instead of disappearing after the first, preserving conversational continuity and prompt caching. [#27037](https://github.com/open-webui/open-webui/issues/27037), [Commit](https://github.com/open-webui/open-webui/commit/0c23466a3e9a1fb7d32875a0614f1ca8e583bc73), [Commit](https://github.com/open-webui/open-webui/commit/f730733bc44eff5812eff0e51ebca0bbcfa1bc6e)

> 🔟 **Context size after tool calls.** The context meter and long-conversation compaction now read the size of the latest request rather than adding up every call in a tool loop, and understand the counts reported by Ollama and llama.cpp as well as the OpenAI-style ones, so compaction no longer fires far below its threshold, or never at all, and the usage shown is no longer inflated. [Commit](https://github.com/open-webui/open-webui/commit/df94268e892cbb66675170a6c78846aef23f6e89), [Commit](https://github.com/open-webui/open-webui/commit/e8f2c123e63c9073c9ae4ee00573144ce6d4b2e9), [#27031](https://github.com/open-webui/open-webui/issues/27031), [#26752](https://github.com/open-webui/open-webui/pull/26752), [#24410](https://github.com/open-webui/open-webui/discussions/24410)

> 🚏 **Stopping a reply when Redis is configured.** The stop button now actually halts generation on Redis-backed deployments, where the listener that carries stop requests between instances quietly died after a few idle seconds and left tokens streaming on, and a new "REDIS_SOCKET_TIMEOUT" setting controls that timeout. [#27104](https://github.com/open-webui/open-webui/pull/27104), [#26779](https://github.com/open-webui/open-webui/issues/26779)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-39-model-support-changes-in-v0-11-0|39 Model Support changes in v0.11.0]] · Model Support
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-07-25 · Lovable · [[Changes/Lovable/2026-07-25-leaked-api-keys-are-revoked-automatically|Leaked API keys are revoked automatically]]
- Later: 2026-07-28 · Dify · [[Changes/Dify/2026-07-28-refactor-agents-simplify-repository-context-by-lyzno1-in-https-github-com-langge|refactor(agents): simplify repository context]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-c867ae&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-9-context-window-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-c867ae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->