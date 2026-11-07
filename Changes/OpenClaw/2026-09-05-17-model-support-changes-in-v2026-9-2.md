---
card_id: openclaw-2026-09-05-4f7b15
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Model Support: 17 changes in v2026.9.2 — OpenClaw
  v2026.9.2 pairs support for OpenAI''s GPT-6 Astra and Meta''s Muse Spark 1.3 with…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1335
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d80b887cd8d8c4609193f5deb97179fafba20b8b103cceb86678f7b3d124de15
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-4f7b15
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 17 Model Support changes'
  evidence:
  - quote: OpenClaw v2026.9.2 pairs support for OpenAI's GPT-6 Astra and Meta's Muse
      Spark 1.3 with practical reliability improvements. Update reports survive reconnects,
      eligible interrupted tasks resume after a restart, and completed answers remain
      available through specific saving failures. Both model additions support text
      and images for accounts with access. On supported OpenAI API connections, you
      can correct ongoing work without waiting for Astra to finish its response.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Operators investigating slow requests can now separate the wait before
      a Gateway handler starts, the handler's elapsed time, and the first response
      through the existing diagnostics exporters. The Gateway RPC metrics cover authenticated
      WebSocket requests, and normal logs also show slow reply-preparation stages
      separately from waiting for a model or tool. Health observations retain pauses
      that repeated reads could previously hide, so a later healthy check does not
      erase the earlier observation from enabled monitoring.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: On the computer running OpenClaw, an interactive openclaw triage --run
      can attempt an installation repair using configured models and their permitted
      fallbacks. Doctor lint runs before and after the attempt, skips inference when
      it finds no errors initially, and keeps the result unsuccessful if errors remain
      afterward. The attempt is limited to one turn, ten minutes overall, five minutes
      for the turn, and 40 tool calls.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Put a supported text directive before a task and OpenClaw keeps the task,
      including its formatting, while applying the requested controls. Thinking, verbosity,
      and authorized tracing can stay with that one message through queueing and model
      changes, then later messages return to their inherited preferences. A standalone
      directive still saves a default, and model selection remains persistent. Telegram’s
      separate handling of multiline commands can still discard later lines before
      they reach this shared parser.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: OpenClaw v2026.9.2 adds support for OpenAI's GPT-6 Astra and Meta's Muse
      Spark 1.3 alongside fixes that help conversations continue and active work finish.
      On its supported API-key path, Astra also lets you send live corrections and
      keep receiving output while direct tools run. Codex can retain its thread after
      supported compaction interruptions, long CLI-backed replies avoid being stopped
      while still producing output, and temporary provider failures get more appropriate
      recovery and retry guidance. People sharing a Gateway can also choose their
      own model account for each chat.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: OpenClaw v2026.9.2 adds support for OpenAI's GPT-6 Astra , so accounts
      with access can choose it for conversations using text and images. You can select
      openai/gpt-6-astra with an OpenAI API-key profile or an eligible ChatGPT/Codex
      subscription. Subscription model discovery confirms account access before offering
      Astra; an unavailable catalog can temporarily leave it out of the picker.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: On the official OpenAI endpoint with an API key and the built-in OpenClaw
      runtime, Astra can continue reasoning and responding while direct tools run.
      A cached WebSocket also lets you send a correction into the active response,
      including text or images, without waiting for it to finish first. Accepted instructions
      remain attached to the conversation through continuation and reconnect. SSE
      keeps ordinary queued delivery, and these built-in-runtime capabilities are
      separate from native Codex execution.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Fresh Meta setups now choose Standard 1.3, while existing primary-model
      selections and older catalog choices remain available. Contributor has separate
      access and data-use terms, so check the provider guide before choosing that
      version.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Hosted catalog updates can now import eligible tool-capable text models
      from models.dev for providers that opt in, so adding each supported model no
      longer needs a separate OpenClaw change. New listings appear after a refreshed
      catalog has been published and downloaded and the Gateway has restarted. Provider
      policies and configured allowlists continue to apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Managed llama.cpp also resolves a selected Hugging Face GGUF file without
      scanning unrelated files in a large repository, while self-hosted discovery
      keeps its time budget stable when the computer's clock changes. These fixes
      preserve the existing model-address and integrity requirements.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Ordinary post-tool summaries stay on the completed work's prepared model
      and account. Supervised tool-only runs that cannot safely produce a summary
      retain their completed work and explain that no final summary was produced,
      without repeating those actions.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Recognized biological-risk and cyber-policy refusals now explain the refused
      turn without telling you to start over or automatically trying another model.
      You can continue the same conversation with a later request; the provider's
      safety policy still determines what it accepts.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Supported moves from Opus 5, Sonnet 5, Opus 4.8, or Fable 5 onto Fable
      5.1 can retain readable earlier reasoning. Fable 5.1 also keeps the hidden runtime
      context needed for that continuity in saved transcripts and exports, while leaving
      it out of visible chat and compaction summaries. Other Anthropic-compatible
      models return to transient runtime context, avoiding repeated old details on
      later requests. Switching away and back, changing thinking level, or rewriting
      the prompt can still invalidate reasoning.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A model can still be working before it has visible text to send. Anthropic,
      Google, Mistral, Bedrock, and Ollama now count parsed keepalives, reasoning,
      and other response events as activity, and active CLI-backed answers retain
      their existing quiet allowance and time to finish delivery. Truly silent calls
      and overall run limits still expire.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Recovery also handles a temporary failure to save an already accepted restart
      attempt, adopting that same execution without another model request while its
      original recovery owner remains valid. Cancellation, newer work or another restart
      ends that particular adoption opportunity. When the assistant is simply waiting
      after an earlier tool error, a deliverable waiting message now shows the current
      state, while the error remains visible if there is no usable message to replace
      it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Existing Codex chats keep the tools they started with. Use /new or /reset
      in an ordinary unlocked chat to get the current tools; keep a supervised chat
      intact and start a separate ordinary session from the global New Session page
      with a concrete Codex-backed model. Saved Codex scripts that call tools.openclaw__agents_wait
      must change to tools.agents_wait .
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: If final filtering removes everything from a reply, OpenClaw now reports
      a failure instead of leaving the conversation looking successful with nothing
      to read, including when a fallback model also produces no visible answer. Deliberate
      silence and valid delivery or continuation paths keep their existing behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 17-model-support-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: model-support
  title: 17 Model Support changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/OpenCode/2026-09-04-core-fixes-issue-of-gpt-6-astra-not-showing-up-for-openai-subscription-users|Core
  Fixes issue of gpt-6-astra not showing up for openai subscription users]]'
- '[[Changes/OpenCode/2026-09-04-allow-codex-oauth-model-filtering-to-recognize-integer-gpt-versions-like-gpt-6|Allow
  Codex OAuth model filtering to recognize integer GPT versions like gpt-6]]'
- '[[Changes/Ollama/2026-09-05-ollama-models-can-now-be-used-directly-in-chatgpt-desktop-so-you-can-keep-your-e|Ollama
  models can now be used directly in ChatGPT Desktop, so you can keep…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: model-support
title: 17 Model Support changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Model Support changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw v2026.9.2 pairs support for OpenAI's GPT-6 Astra and Meta's Muse Spark 1.3 with practical reliability improvements. Update reports survive reconnects, eligible interrupted tasks resume after a restart, and completed answers remain available through specific saving failures. Both model additions support text and images for accounts with access. On supported OpenAI API connections, you can correct ongoing work without waiting for Astra to finish its response.

> Operators investigating slow requests can now separate the wait before a Gateway handler starts, the handler's elapsed time, and the first response through the existing diagnostics exporters. The Gateway RPC metrics cover authenticated WebSocket requests, and normal logs also show slow reply-preparation stages separately from waiting for a model or tool. Health observations retain pauses that repeated reads could previously hide, so a later healthy check does not erase the earlier observation from enabled monitoring.

> On the computer running OpenClaw, an interactive openclaw triage --run can attempt an installation repair using configured models and their permitted fallbacks. Doctor lint runs before and after the attempt, skips inference when it finds no errors initially, and keeps the result unsuccessful if errors remain afterward. The attempt is limited to one turn, ten minutes overall, five minutes for the turn, and 40 tool calls.

> Put a supported text directive before a task and OpenClaw keeps the task, including its formatting, while applying the requested controls. Thinking, verbosity, and authorized tracing can stay with that one message through queueing and model changes, then later messages return to their inherited preferences. A standalone directive still saves a default, and model selection remains persistent. Telegram’s separate handling of multiline commands can still discard later lines before they reach this shared parser.

> OpenClaw v2026.9.2 adds support for OpenAI's GPT-6 Astra and Meta's Muse Spark 1.3 alongside fixes that help conversations continue and active work finish. On its supported API-key path, Astra also lets you send live corrections and keep receiving output while direct tools run. Codex can retain its thread after supported compaction interruptions, long CLI-backed replies avoid being stopped while still producing output, and temporary provider failures get more appropriate recovery and retry guidance. People sharing a Gateway can also choose their own model account for each chat.

> OpenClaw v2026.9.2 adds support for OpenAI's GPT-6 Astra , so accounts with access can choose it for conversations using text and images. You can select openai/gpt-6-astra with an OpenAI API-key profile or an eligible ChatGPT/Codex subscription. Subscription model discovery confirms account access before offering Astra; an unavailable catalog can temporarily leave it out of the picker.

> On the official OpenAI endpoint with an API key and the built-in OpenClaw runtime, Astra can continue reasoning and responding while direct tools run. A cached WebSocket also lets you send a correction into the active response, including text or images, without waiting for it to finish first. Accepted instructions remain attached to the conversation through continuation and reconnect. SSE keeps ordinary queued delivery, and these built-in-runtime capabilities are separate from native Codex execution.

> Fresh Meta setups now choose Standard 1.3, while existing primary-model selections and older catalog choices remain available. Contributor has separate access and data-use terms, so check the provider guide before choosing that version.

> Hosted catalog updates can now import eligible tool-capable text models from models.dev for providers that opt in, so adding each supported model no longer needs a separate OpenClaw change. New listings appear after a refreshed catalog has been published and downloaded and the Gateway has restarted. Provider policies and configured allowlists continue to apply.

> Managed llama.cpp also resolves a selected Hugging Face GGUF file without scanning unrelated files in a large repository, while self-hosted discovery keeps its time budget stable when the computer's clock changes. These fixes preserve the existing model-address and integrity requirements.

> Ordinary post-tool summaries stay on the completed work's prepared model and account. Supervised tool-only runs that cannot safely produce a summary retain their completed work and explain that no final summary was produced, without repeating those actions.

> Recognized biological-risk and cyber-policy refusals now explain the refused turn without telling you to start over or automatically trying another model. You can continue the same conversation with a later request; the provider's safety policy still determines what it accepts.

> Supported moves from Opus 5, Sonnet 5, Opus 4.8, or Fable 5 onto Fable 5.1 can retain readable earlier reasoning. Fable 5.1 also keeps the hidden runtime context needed for that continuity in saved transcripts and exports, while leaving it out of visible chat and compaction summaries. Other Anthropic-compatible models return to transient runtime context, avoiding repeated old details on later requests. Switching away and back, changing thinking level, or rewriting the prompt can still invalidate reasoning.

> A model can still be working before it has visible text to send. Anthropic, Google, Mistral, Bedrock, and Ollama now count parsed keepalives, reasoning, and other response events as activity, and active CLI-backed answers retain their existing quiet allowance and time to finish delivery. Truly silent calls and overall run limits still expire.

> Recovery also handles a temporary failure to save an already accepted restart attempt, adopting that same execution without another model request while its original recovery owner remains valid. Cancellation, newer work or another restart ends that particular adoption opportunity. When the assistant is simply waiting after an earlier tool error, a deliverable waiting message now shows the current state, while the error remains visible if there is no usable message to replace it.

> Existing Codex chats keep the tools they started with. Use /new or /reset in an ordinary unlocked chat to get the current tools; keep a supervised chat intact and start a separate ordinary session from the global New Session page with a concrete Codex-backed model. Saved Codex scripts that call tools.openclaw__agents_wait must change to tools.agents_wait .

> If final filtering removes everything from a reply, OpenClaw now reports a failure instead of leaving the conversation looking successful with nothing to read, including when a fallback model also produces no visible answer. Deliberate silence and valid delivery or continuation paths keep their existing behavior.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-05 · Ollama · [[Changes/Ollama/2026-09-05-ollama-models-can-now-be-used-directly-in-chatgpt-desktop-so-you-can-keep-your-e|Ollama models can now be used directly in ChatGPT Desktop, so you can keep…]]
- Later: 2026-09-08 · Lovable · [[Changes/Lovable/2026-09-08-gpt-6-astra-gemini-3-8-flash-and-gemini-3-5-transcribe-for-your-app-s-ai-feature|GPT-6 Astra, Gemini 3.8 Flash, and Gemini 3.5 Transcribe for your app's AI features]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-4f7b15&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-17-model-support-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-4f7b15%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->