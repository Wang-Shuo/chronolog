---
card_id: openclaw-2026-09-11-477082
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Memory and Personalization: 14 changes in v2026.9.4
  — It also adds GPT Image 2.5 support, more control over cloud sessions, and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1149
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ebfeca58bbb5eee58f3795e570848c2787bab0aac5f6af91a616277a05791fd7
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-477082
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 14 Memory and Personalization changes'
  evidence:
  - quote: It also adds GPT Image 2.5 support, more control over cloud sessions, and
      interactive questions in the terminal, alongside fixes for updates, memory,
      and messaging.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: An empty background memory check no longer makes a fresh Claw think setup
      is already finished, so you still get its first naming conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: An error at the very end of an import no longer has to hide work that already
      finished. OpenClaw preserves completed memory-import results when the final
      cleanup fails, and can recognize a retry of the same request without copying
      everything again. If an error says the import completed, check the report and
      imported files before starting over. That retry protection is temporary and
      does not survive restarting OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Memory fixes help your Claw find remembered details and return to older
      conversations. There is also clearer guidance when memories cannot be saved,
      or when deleting a conversation leaves its memories behind.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Asking for a short list of memories no longer drops a better match just
      because you requested fewer results. Your Claw can also keep looking when an
      optional search gets stuck, and a local memory-search service gets time to start
      before OpenClaw gives up on it. These fixes help remembered information reach
      your conversation without unnecessary repair steps.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: OpenClaw can wait through temporary limits from your memory-search provider
      and use the right model when it switches to your configured backup. It also
      stops telling you to rebuild working memory search just because the main provider
      has recovered. If you change to an incompatible model, you still need to rebuild
      with openclaw memory index --force .
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Mac users running OpenClaw with Bun can enable native memory search with
      brew install sqlite . If you previously used a custom SQLite startup script,
      replace it with the OPENCLAW_SQLITE_LIBRARY setting to avoid a startup failure.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: With the default settings, a note no longer becomes long-term memory simply
      because OpenClaw repeatedly encounters it during background scans. It must also
      turn up in different memory searches, helping keep incidental notes from being
      saved just because they keep appearing. After updating, some older notes may
      take longer to qualify, while memories already saved stay in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Default long-term memory selection adds a search-use signal. Conceptual
      illustration, not a screenshot. Previously saved memories remain. Some older
      notes may take longer to qualify after updating.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Deleting a conversation now tells you when its saved history can still
      appear in memory search and shows the command for forgetting those memories
      . Forgetting remains a separate step, which you need to run on the computer
      hosting OpenClaw, even if you deleted the conversation remotely.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If another tool adds memories to your LanceDB memory extension , your Claw
      can find them on its next search without restarting OpenClaw. You can also list
      or delete those newly added memories without first having to make a change from
      inside OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Codex conversations managed by OpenClaw regain workspace personality, preferences,
      skills, and memory guidance, including later edits. This applies to supported
      managed connections; other connection types keep their existing handling and
      may show a warning.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Plugins with lots of saved data use less extra memory when listing it,
      helping reduce the strain of a large collection. The first use after the storage
      update may take extra time and disk space.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Cloud workers settings now lets administrators change advanced options,
      set spare-computer limits, and choose a default profile for each repository.
      Save your changes and restart OpenClaw to apply them. You can also hover over
      a cloud session to see its known operating system, CPU, and memory capacity.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-memory-and-personalization-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: memory
  title: 14 Memory and Personalization changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2
  Memory and Personalization changes in rust-v0.154.0]]'
- '[[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2
  Memory and Personalization changes in v2.1.268]]'
- '[[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory
  and Personalization changes in 1.17.1]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: memory
title: 14 Memory and Personalization changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Memory and Personalization changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> It also adds GPT Image 2.5 support, more control over cloud sessions, and interactive questions in the terminal, alongside fixes for updates, memory, and messaging.

> An empty background memory check no longer makes a fresh Claw think setup is already finished, so you still get its first naming conversation.

> An error at the very end of an import no longer has to hide work that already finished. OpenClaw preserves completed memory-import results when the final cleanup fails, and can recognize a retry of the same request without copying everything again. If an error says the import completed, check the report and imported files before starting over. That retry protection is temporary and does not survive restarting OpenClaw.

> Memory fixes help your Claw find remembered details and return to older conversations. There is also clearer guidance when memories cannot be saved, or when deleting a conversation leaves its memories behind.

> Asking for a short list of memories no longer drops a better match just because you requested fewer results. Your Claw can also keep looking when an optional search gets stuck, and a local memory-search service gets time to start before OpenClaw gives up on it. These fixes help remembered information reach your conversation without unnecessary repair steps.

> OpenClaw can wait through temporary limits from your memory-search provider and use the right model when it switches to your configured backup. It also stops telling you to rebuild working memory search just because the main provider has recovered. If you change to an incompatible model, you still need to rebuild with openclaw memory index --force .

> Mac users running OpenClaw with Bun can enable native memory search with brew install sqlite . If you previously used a custom SQLite startup script, replace it with the OPENCLAW_SQLITE_LIBRARY setting to avoid a startup failure.

> With the default settings, a note no longer becomes long-term memory simply because OpenClaw repeatedly encounters it during background scans. It must also turn up in different memory searches, helping keep incidental notes from being saved just because they keep appearing. After updating, some older notes may take longer to qualify, while memories already saved stay in place.

> Default long-term memory selection adds a search-use signal. Conceptual illustration, not a screenshot. Previously saved memories remain. Some older notes may take longer to qualify after updating.

> Deleting a conversation now tells you when its saved history can still appear in memory search and shows the command for forgetting those memories . Forgetting remains a separate step, which you need to run on the computer hosting OpenClaw, even if you deleted the conversation remotely.

> If another tool adds memories to your LanceDB memory extension , your Claw can find them on its next search without restarting OpenClaw. You can also list or delete those newly added memories without first having to make a change from inside OpenClaw.

> Codex conversations managed by OpenClaw regain workspace personality, preferences, skills, and memory guidance, including later edits. This applies to supported managed connections; other connection types keep their existing handling and may show a warning.

> Plugins with lots of saved data use less extra memory when listing it, helping reduce the strain of a large collection. The first use after the storage update may take extra time and disk space.

> Cloud workers settings now lets administrators change advanced options, set spare-computer limits, and choose a default profile for each repository. Save your changes and restart OpenClaw to apply them. You can also hover over a cloud session to see its known operating system, CPU, and memory capacity.

Source: https://docs.openclaw.ai/releases/2026.9.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-11-messages-arriving-while-openclaw-is-paused-now-wait-until-it-is-ready-again-and|Messages arriving while OpenClaw is paused now wait until it is ready again…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-11-images-you-send-stay-visible-while-the-conversation-updates-and-scrolling-back-t|Images you send stay visible while the conversation updates, and scrolling back…]] · Files and Data
- [[Changes/OpenClaw/2026-09-11-7-automation-and-scheduling-changes-in-v2026-9-4|7 Automation and Scheduling changes in v2026.9.4]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-11-with-diagnostic-recording-enabled-openrouter-can-return-finished-music-or-a-usag|With diagnostic recording enabled, OpenRouter can return finished music…]] · Music Generation
- [[Changes/OpenClaw/2026-09-11-18-developer-workflow-changes-in-v2026-9-4|18 Developer Workflow changes in v2026.9.4]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-11-2-reliability-and-performance-changes-in-v2026-9-4|2 Reliability and Performance changes in v2026.9.4]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-11-16-mobile-and-desktop-changes-in-v2026-9-4|16 Mobile and Desktop changes in v2026.9.4]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-the-bundled-video-frames-skill-and-its-helper-script-have-been-removed-if-you-us|The bundled video-frames skill and its helper script have been removed]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-11-5-interface-experience-changes-in-v2026-9-4|5 Interface Experience changes in v2026.9.4]] · Interface Experience
- [[Changes/OpenClaw/2026-09-11-you-can-now-answer-your-claw-s-questions-and-enter-secrets-from-the-terminal-wit|Answer your Claw’s questions and enter secrets from the terminal, with clearer…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-11-2-image-generation-changes-in-v2026-9-4|2 Image Generation changes in v2026.9.4]] · Image Generation
- [[Changes/OpenClaw/2026-09-11-3-pricing-model-changes-in-v2026-9-4|3 Pricing Model changes in v2026.9.4]] · Pricing Model
- [[Changes/OpenClaw/2026-09-11-you-can-now-reach-the-official-app-store-listing-straight-from-the-iphone-setup|Reach the official App Store listing straight from the iPhone setup guide]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-5-editor-experience-changes-in-v2026-9-4|5 Editor Experience changes in v2026.9.4]] · Editor Experience
- [[Changes/OpenClaw/2026-09-11-you-can-now-choose-deepgram-flux-to-turn-incoming-voice-notes-into-text-your-cla|Choose Deepgram Flux to turn incoming voice notes into text your Claw can use…]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-8-voice-and-audio-changes-in-v2026-9-4|8 Voice and Audio changes in v2026.9.4]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-12-safety-and-privacy-changes-in-v2026-9-4|12 Safety and Privacy changes in v2026.9.4]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-11-22-apps-and-integrations-changes-in-v2026-9-4|22 Apps and Integrations changes in v2026.9.4]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-20-model-support-changes-in-v2026-9-4|20 Model Support changes in v2026.9.4]] · Model Support
- [[Changes/OpenClaw/2026-09-11-14-account-and-access-changes-in-v2026-9-4|14 Account and Access changes in v2026.9.4]] · Account and Access
- [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an|Search installed and available plugins together, browse by purpose, and keep…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-3-search-and-browsing-changes-in-v2026-9-4|3 Search and Browsing changes in v2026.9.4]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-11-you-can-now-enable-desktop-access-for-azure-cloud-workers-whether-openclaw-manag|Enable desktop access for Azure cloud workers , whether OpenClaw manages them…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-3-collaboration-changes-in-v2026-9-4|3 Collaboration changes in v2026.9.4]] · Collaboration
- [[Changes/OpenClaw/2026-09-11-25-agent-mode-changes-in-v2026-9-4|25 Agent Mode changes in v2026.9.4]] · Agent Mode
- [[Changes/OpenClaw/2026-09-11-2-context-window-changes-in-v2026-9-4|2 Context Window changes in v2026.9.4]] · Context Window
- [[Changes/OpenClaw/2026-09-11-56-other-changes-in-v2026-9-4|56 other changes in v2026.9.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-10 · Dify · [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]]
- Later: 2026-09-11 · Raycast · [[Changes/Raycast/2026-09-11-projects|Projects]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-477082&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-14-memory-and-personalization-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-477082%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->