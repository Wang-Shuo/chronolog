---
card_id: open-webui-2026-09-21-879b16
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Memory and Personalization: 6 changes in v0.11.4
  — \U0001F6B0 **Rejected picture addresses.** A model entry carrying a picture address
  the…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1159
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f68c033fb6f27858409f5015c4a8dcecd4ec949cff043c0fc5bee692126b1ebb
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-879b16
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 6 Memory and Personalization changes'
  evidence:
  - quote: "\U0001F6B0 **Rejected picture addresses.** A model entry carrying a picture
      address the server refuses no longer leaves that address in memory, where anyone
      signed in could pile them up. [#29971](https://github.com/open-webui/open-webui/pull/29971)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9EA **Memory replies carry less.** The memory tool no longer hands
      the model each memory's stored metadata, and a memory now records the model's
      id rather than the whole model entry. [Commit](https://github.com/open-webui/open-webui/commit/e9a0164690a8b1e190bdc8f4613e9d918b26d327)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F507 **Memory fully off.** With memory switched off, stored memories
      are no longer folded into a reply's context and the memory tools are no longer
      offered to the model, where both went on reaching it behind the switch. [#30228](https://github.com/open-webui/open-webui/pull/30228),
      [#30227](https://github.com/open-webui/open-webui/issues/30227)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9E0 **Memory review behind the switch.** The background review
      that drafts new memories from a conversation no longer runs when memories are
      switched off or the account is barred from them, where it went on spending a
      task-model call every interval turn and failing at the write. [#30309](https://github.com/open-webui/open-webui/pull/30309)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4BE **Deleted tool memory.** Deleting a tool or a function left
      the whole of its code in memory for as long as the server ran; it is now let
      go of along with the rest. [#29983](https://github.com/open-webui/open-webui/pull/29983)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F680 **Cheaper model refreshes.** The model registry shared through
      Redis is now written only when the models themselves change, rather than on
      every refresh because of the countdown Ollama attaches to a model it holds in
      memory. [Commit](https://github.com/open-webui/open-webui/commit/649c012ecf308a994ea180127f7f8f94d0aec311)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-memory-and-personalization-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: memory
  title: 6 Memory and Personalization changes in v0.11.4
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-17-7-memory-and-personalization-changes-in-rust-v0-155-0|7
  Memory and Personalization changes in rust-v0.155.0]]'
- '[[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31
  Memory and Personalization changes in v2026.9.5]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear
  down the processes an internal git command started when it times out, so a slow…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: memory
title: 6 Memory and Personalization changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Memory and Personalization changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🚰 **Rejected picture addresses.** A model entry carrying a picture address the server refuses no longer leaves that address in memory, where anyone signed in could pile them up. [#29971](https://github.com/open-webui/open-webui/pull/29971)

> 🧪 **Memory replies carry less.** The memory tool no longer hands the model each memory's stored metadata, and a memory now records the model's id rather than the whole model entry. [Commit](https://github.com/open-webui/open-webui/commit/e9a0164690a8b1e190bdc8f4613e9d918b26d327)

> 🔇 **Memory fully off.** With memory switched off, stored memories are no longer folded into a reply's context and the memory tools are no longer offered to the model, where both went on reaching it behind the switch. [#30228](https://github.com/open-webui/open-webui/pull/30228), [#30227](https://github.com/open-webui/open-webui/issues/30227)

> 🧠 **Memory review behind the switch.** The background review that drafts new memories from a conversation no longer runs when memories are switched off or the account is barred from them, where it went on spending a task-model call every interval turn and failing at the write. [#30309](https://github.com/open-webui/open-webui/pull/30309)

> 💾 **Deleted tool memory.** Deleting a tool or a function left the whole of its code in memory for as long as the server ran; it is now let go of along with the rest. [#29983](https://github.com/open-webui/open-webui/pull/29983)

> 🚀 **Cheaper model refreshes.** The model registry shared through Redis is now written only when the models themselves change, rather than on every refresh because of the countdown Ollama attaches to a model it holds in memory. [Commit](https://github.com/open-webui/open-webui/commit/649c012ecf308a994ea180127f7f8f94d0aec311)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-tear-down-the-processes-an-internal-git-command-started-when-it-times-out-so-a-s|Tear down the processes an internal git command started when it times out, so a slow…]]
- Later: 2026-09-22 · Codex CLI · [[Changes/Codex CLI/2026-09-22-6-memory-and-personalization-changes-in-rust-v0-156-0|6 Memory and Personalization changes in rust-v0.156.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-879b16&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-6-memory-and-personalization-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-879b16%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->