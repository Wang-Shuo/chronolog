---
card_id: openclaw-2026-11-03-e4268f
date: '2026-11-03'
description: 'OpenClaw · 2026-11-03 · Model Support: 17 changes in v2026.10.10 — When
  enabled for a model, your active conversation and manual compaction get priority
  over…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1394
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 565b89cb98862cb701ce92220eb0b577408bc0761404a7477da9bafa18ebe04f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-11-03-e4268f
  comparison: ''
  date: '2026-11-03'
  description: 'OpenClaw — v2026.10.10: 17 Model Support changes'
  evidence:
  - quote: When enabled for a model, your active conversation and manual compaction
      get priority over background work.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Typing the first message in New Session stays responsive even with a large
      model catalog.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: On Linux x64 CPU systems, guided setup helps you download and test local
      models for reading text in images and describing pictures. A separately configured
      cloud chat model may still receive the original image.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Choose Gemini 4 Argon on supported Google and Vertex routes, including
      its available thinking levels. Google API-key setup now selects it as your primary
      model, so check that choice if you want to keep another default.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: New conversations and side questions now wait when all model-request slots
      are occupied instead of failing immediately. Waiting adds time, and a parent
      whose helpers also need occupied slots can still stall.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Changing the policy of a busy Codex conversation now leaves its current
      model and settings intact if the change cannot be applied, instead of switching
      models unexpectedly.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: New configurations for supported Codex models now use corrected capacity
      defaults; existing configurations are not changed by this fix.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Scheduled jobs now keep their selected account and allowed tools in affected
      handoffs, and supported deliveries appear in the conversation or topic that
      received them. Older jobs without a saved account selection can keep using environment
      or provider-config keys, but must explicitly select a stored account with model@profile
      before using it; model fallback will not bypass that choice.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Conversations on paired and cloud computers give a clearer reason when
      a model or credential is missing, a worker stops mid-reply, or a turn produces
      no answer. If a worker disappears while the Gateway stays up, text it already
      received can remain in conversation history, but interrupted tools are not resumed.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Workboard cards now reflect the overall task result through model fallback
      rather than showing a false failure while work continues. Board tabs and menus
      are easier to reach on narrow screens, and after a storage problem is resolved,
      later Workboard, Logbook and Team Reports operations can recover without restarting
      the Gateway. An uncertain in-flight write is not replayed automatically.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Model pickers refresh when the catalog changes during an unfinished read,
      rather than keeping the older model list.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: More long conversations can keep going when their model runs out of room,
      by shortening earlier history or using a supported recovery path. A summary
      may leave out details, and a single oversized message may still need shortening.
      Eligible direct OpenAI API-key conversations now use provider compaction by
      default; that compaction call can cost more than a local summary. You can turn
      it off in the model configuration.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: If you have fallback models configured , a reply can switch to another
      eligible model after a safe-to-retry timeout, exhausted context recovery or
      an explicit organization token-quota error. A longer fallback chain can take
      longer overall; billing and sign-in problems still need their own remedies.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Switching models now keeps your requested thinking level, using a supported
      level for the current model and restoring your preference when you switch back.
      If an earlier switch already overwrote it, set it again once.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Model pickers make supported choices easier to find and show more useful
      errors when a configured model is missing. A catalog change does not replace
      a model you pinned earlier.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Adding a working model provider no longer shows another provider's discovery
      failure as a problem with the key you just saved. Discovery warnings name the
      unavailable provider when it is known.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Windows no longer reports a failed local-model shutdown when the service
      has stopped and only its termination helper is still finishing.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 17-model-support-changes-in-v2026-10-10
  source_release: openclaw-2026-11-03-v2026-10-10-c26ff355
  source_type: openclaw_changelog
  theme: model-support
  title: 17 Model Support changes in v2026.10.10
  type: change
related_changes:
- '[[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-15|2 Model Support
  changes in v0.40.15]]'
- '[[Changes/Ollama/2026-11-03-2-model-support-changes-in-v0-40-14|2 Model Support
  changes in v0.40.14]]'
- '[[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support
  changes in v0.13.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|openclaw-2026-11-03-v2026-10-10-c26ff355]]'
source_type: openclaw_changelog
theme: model-support
title: 17 Model Support changes in v2026.10.10
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Model Support changes in v2026.10.10

**OpenClaw** · 2026-11-03 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.10) · from [[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|v2026.10.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> When enabled for a model, your active conversation and manual compaction get priority over background work.

> Typing the first message in New Session stays responsive even with a large model catalog.

> On Linux x64 CPU systems, guided setup helps you download and test local models for reading text in images and describing pictures. A separately configured cloud chat model may still receive the original image.

> Choose Gemini 4 Argon on supported Google and Vertex routes, including its available thinking levels. Google API-key setup now selects it as your primary model, so check that choice if you want to keep another default.

> New conversations and side questions now wait when all model-request slots are occupied instead of failing immediately. Waiting adds time, and a parent whose helpers also need occupied slots can still stall.

> Changing the policy of a busy Codex conversation now leaves its current model and settings intact if the change cannot be applied, instead of switching models unexpectedly.

> New configurations for supported Codex models now use corrected capacity defaults; existing configurations are not changed by this fix.

> Scheduled jobs now keep their selected account and allowed tools in affected handoffs, and supported deliveries appear in the conversation or topic that received them. Older jobs without a saved account selection can keep using environment or provider-config keys, but must explicitly select a stored account with model@profile before using it; model fallback will not bypass that choice.

> Conversations on paired and cloud computers give a clearer reason when a model or credential is missing, a worker stops mid-reply, or a turn produces no answer. If a worker disappears while the Gateway stays up, text it already received can remain in conversation history, but interrupted tools are not resumed.

> Workboard cards now reflect the overall task result through model fallback rather than showing a false failure while work continues. Board tabs and menus are easier to reach on narrow screens, and after a storage problem is resolved, later Workboard, Logbook and Team Reports operations can recover without restarting the Gateway. An uncertain in-flight write is not replayed automatically.

> Model pickers refresh when the catalog changes during an unfinished read, rather than keeping the older model list.

> More long conversations can keep going when their model runs out of room, by shortening earlier history or using a supported recovery path. A summary may leave out details, and a single oversized message may still need shortening. Eligible direct OpenAI API-key conversations now use provider compaction by default; that compaction call can cost more than a local summary. You can turn it off in the model configuration.

> If you have fallback models configured , a reply can switch to another eligible model after a safe-to-retry timeout, exhausted context recovery or an explicit organization token-quota error. A longer fallback chain can take longer overall; billing and sign-in problems still need their own remedies.

> Switching models now keeps your requested thinking level, using a supported level for the current model and restoring your preference when you switch back. If an earlier switch already overwrote it, set it again once.

> Model pickers make supported choices easier to find and show more useful errors when a configured model is missing. A catalog change does not replace a model you pinned earlier.

> Adding a working model provider no longer shows another provider's discovery failure as a problem with the key you just saved. Discovery warnings name the unavailable provider when it is known.

> Windows no longer reports a failed local-model shutdown when the service has stopped and only its termination helper is still finishing.

Source: https://docs.openclaw.ai/releases/2026.10.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-11-03-generated-images-music-and-video-can-wait-behind-a-busy-chat-without-reporting-f|Generated images, music and video can wait behind a busy chat without reporting…]] · Multimodal Input
- [[Changes/OpenClaw/2026-11-03-you-can-now-guide-the-same-running-conversation-from-the-control-ui-or-an-admini|Guide the same running conversation from the Control UI or an administrator-linked…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-11-03-2-files-and-data-changes-in-v2026-10-10|2 Files and Data changes in v2026.10.10]] · Files and Data
- [[Changes/OpenClaw/2026-11-03-6-account-and-access-changes-in-v2026-10-10|6 Account and Access changes in v2026.10.10]] · Account and Access
- [[Changes/OpenClaw/2026-11-03-image-generation-and-editing-now-reject-invalid-size-and-shape-options-before-co|Image generation and editing now reject invalid size and shape options before…]] · Image Generation
- [[Changes/OpenClaw/2026-11-03-9-agent-mode-changes-in-v2026-10-10|9 Agent Mode changes in v2026.10.10]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-13-interface-experience-changes-in-v2026-10-10|13 Interface Experience changes in v2026.10.10]] · Interface Experience
- [[Changes/OpenClaw/2026-11-03-you-can-now-work-directly-in-a-folder-on-another-computer-connected-to-openclaw|Work directly in a folder on another computer connected to OpenClaw]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-5-context-window-changes-in-v2026-10-10|5 Context Window changes in v2026.10.10]] · Context Window
- [[Changes/OpenClaw/2026-11-03-15-memory-and-personalization-changes-in-v2026-10-10|15 Memory and Personalization changes in v2026.10.10]] · Memory and Personalization
- [[Changes/OpenClaw/2026-11-03-4-automation-and-scheduling-changes-in-v2026-10-10|4 Automation and Scheduling changes in v2026.10.10]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-11-03-3-editor-experience-changes-in-v2026-10-10|3 Editor Experience changes in v2026.10.10]] · Editor Experience
- [[Changes/OpenClaw/2026-11-03-web-search-now-honors-more-of-your-chosen-provider-settings-result-counts-and-ti|Web search now honors more of your chosen provider settings, result counts…]] · Search and Browsing
- [[Changes/OpenClaw/2026-11-03-6-collaboration-changes-in-v2026-10-10|6 Collaboration changes in v2026.10.10]] · Collaboration
- [[Changes/OpenClaw/2026-11-03-6-voice-and-audio-changes-in-v2026-10-10|6 Voice and Audio changes in v2026.10.10]] · Voice and Audio
- [[Changes/OpenClaw/2026-11-03-7-safety-and-privacy-changes-in-v2026-10-10|7 Safety and Privacy changes in v2026.10.10]] · Safety and Privacy
- [[Changes/OpenClaw/2026-11-03-4-mobile-and-desktop-changes-in-v2026-10-10|4 Mobile and Desktop changes in v2026.10.10]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-11-03-retrying-a-meeting-transcript-from-summary-or-transcript-now-restores-all-availa|Retrying a meeting transcript from Summary or Transcript now restores all available pages]] · Meeting Notes
- [[Changes/OpenClaw/2026-11-03-18-developer-workflow-changes-in-v2026-10-10|18 Developer Workflow changes in v2026.10.10]] · Developer Workflow
- [[Changes/OpenClaw/2026-11-03-21-apps-and-integrations-changes-in-v2026-10-10|21 Apps and Integrations changes in v2026.10.10]] · Apps and Integrations
- [[Changes/OpenClaw/2026-11-03-incognito-conversations-now-keep-openclaw-conversation-contents-in-memory-instea|Incognito conversations now keep OpenClaw conversation contents in memory instead…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-11-03-83-other-changes-in-v2026-10-10|83 other changes in v2026.10.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-11-03 · Open WebUI · [[Changes/Open WebUI/2026-11-03-4-model-support-changes-in-v0-13-0|4 Model Support changes in v0.13.0]]
- Later: 2026-11-04 · Dify · [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-11-03-e4268f&body=Card%3A%20Changes%2FOpenClaw%2F2026-11-03-17-model-support-changes-in-v2026-10-10.md%0ACard%20ID%3A%20openclaw-2026-11-03-e4268f%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->