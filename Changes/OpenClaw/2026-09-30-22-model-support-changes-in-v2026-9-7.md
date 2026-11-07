---
card_id: openclaw-2026-09-30-af92e1
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Model Support: 22 changes in v2026.9.7 — In
  browser setup, arriving suggestions no longer interrupt your typing. Reloading first-run…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1360
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2df5a1c97fff1e8ff80636898b66f5171fad7cc57f3f249209f03956b31f43b3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-af92e1
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 22 Model Support changes'
  evidence:
  - quote: In browser setup, arriving suggestions no longer interrupt your typing.
      Reloading first-run Model Setup returns to its pending question while the same
      Gateway stays running, but unsubmitted answers are lost. Cancelling the attempt
      frees the provider choices once cancellation is confirmed.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can drop or paste images into Side chat for the current question. Choose
      an image-capable utility model, then use Retry if the previous model could not
      read the image. Images are not saved in restored history, so reattach them for
      later questions. Compatible CLI setups without direct provider credentials also
      gain a text-only fallback, without tools or images.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Large model lists are more responsive to search, and the picker opens to
      the selected model’s provider. Usage keeps previous totals visible while refreshing
      and lets you retry failures. Doctor reports incomplete totals; request usage
      again to retry. If Cmd+K returns no models, check model settings for provider-refresh
      problems.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Saved settings apply without waiting for a file-change notification, and
      temporary database contention no longer leaves supported changes waiting for
      another edit. Changing channel connection settings also preserves unaffected
      conversation lists and model choices. Configuration errors now explain whether
      a file could not be read, a setting is invalid, or a rejected edit saved nothing.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Conversation compaction keeps already-summarized messages out of affected
      later summaries and loads saved history in the background so other work can
      continue. Messages arriving as a summary finishes use the updated conversation,
      and recovery stops when the run times out. If a model exhausts its output budget
      without producing a summary, OpenClaw stops repeating the same request and suggests
      lowering thinking or increasing maxTokens before retrying. Saved history remains
      intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Replies keep their paragraph breaks and related tool activity together,
      and show message times and the answering model when recorded. Scrolling also
      avoids a stall that could happen after repeated sends.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Use this runtime only on a single-user Gateway, with OpenClaw as the sole
      controller of the session. Start a new or reset chat after changing its instructions,
      tools, model, credentials, or execution environment. Resetting or deleting the
      local chat does not delete hosted history or files. Check that returned attachments
      arrived. Choose another runtime if you need per-turn tool restrictions from
      prompt hooks, restrictions on native shell/file/web access, or strictly tool-free
      background calls.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: GPT-6 Sol and Luna appear for accounts with access through supported OpenAI
      API, ChatGPT, and native Codex connections. Discovery fixes help subscription
      accounts find them without changing existing model choices. To use OpenClaw's
      own runtime, select it explicitly in the runtime settings ; choosing the model
      alone does not switch runtimes.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Claude Opus 5.5 becomes the default for new Anthropic and Claude CLI setups
      and the rolling opus choice. Explicit Opus 5 selections stay unchanged. Opus
      5.5 always uses thinking, even when you hide it. Automatic PDF analysis can
      use 5.5 independently of your chat model; set a PDF model explicitly to keep
      a particular version.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Claude Sonnet 5.5 is available through Anthropic, and the rolling sonnet
      choice now selects it. Explicit version selections, including sonnet-5 , stay
      pinned, while fresh setup still defaults to Opus 5.5. Thinking defaults to high;
      choosing off still permits notes between tool calls.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Claude Code 2.1.277 rejects the new model ID. Use an explicit sonnet-5
      selection to keep Sonnet 5 on that version.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Model menus show known choices while the full list loads and keep your
      current model easy to find. Repeated background refreshes no longer stall native
      agent runs. Reopen the menu to see newly discovered models; your account and
      role restrictions still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: OpenClaw avoids repeatedly sending requests that a provider has already
      rejected, while temporary failures keep their normal retry handling . Plugin
      background requests can use your configured fallback models unless you explicitly
      chose a model. Before retrying a failed turn, check whether its tools already
      completed any actions.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: OpenClaw does less repeated work when receiving long replies and preparing
      large model requests. Buffered Anthropic replies also give other conversations
      time to respond.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Gemini 3.8 Live keeps spoken turns in history and handles requests for
      agent help more consistently. Grok Talk avoids duplicate saved utterances and
      supports longer playback. Speaking over Talk replies interrupts playback again
      during agent consults unless you disabled interruption; Gemini Extended Thinking
      may still resume speaking after an interruption.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can choose Gemini 3.8 Flash or Flash-Lite to generate speech , with
      delivery instructions kept separate from the words spoken. Gemini 3.1 Flash
      TTS Preview remains the default.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can opt into Gemini Interactions for streamed replies, reasoning, images,
      and tools. Google defaults stay unchanged. This connection sends the needed
      history with each request without asking the API to store it, and can recover
      interrupted replies under the normal retry rules. Cached-content handles and
      video clipping offsets are not supported.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Cost estimates now use the provider handling the request, and total CLI
      token counts are kept separate from the current conversation's context usage.
      Missing SuperGrok usage percentages are explained rather than shown as zero.
      You can also choose Ultra for planning and verification guidance across OpenClaw
      and Claude Code models. It uses only the reasoning the model supports; native
      Codex needs supported reasoning choices. Cost figures remain estimates.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Supported newer standard Grok models get thinking controls and image-input
      support without waiting for each model name to be added. Grok 4.20 and variants
      such as Fast are excluded. DeepSeek Flash also honors thinking settings on affected
      OpenAI-compatible connections.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Already-paired nodes can reconnect with --pair-if-needed after their setup
      code expires, provided their saved credentials still match the selected Gateway.
      New pairing still needs a fresh code. If you use a saved certificate fingerprint,
      verify the selected fingerprint before reconnecting because this recovery path
      does not compare it. Remote Codex connections can also retry brief connection
      failures before sending work; model and tool requests already sent are not replayed.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You have more control over who can use OpenClaw, which models they can
      use, and whether they can upload files.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Administrators can choose which models each role can use , including in
      supported native Codex runs. Removing a model stops affected requests. Visitor
      Access now requires an explicit modelPolicy ; {} uses the source agent's models.
      Restricted Codex runs are refused if their connection cannot enforce the policy.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 22-model-support-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: model-support
  title: 22 Model Support changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-30-changed-how-failed-api-requests-are-retried-one-limit-now-covers-a-whole-model-c|Changed
  how failed API requests are retried]]'
- '[[Changes/Cline/2026-09-30-6-model-support-changes-in-v4-1-22|6 Model Support changes
  in v4.1.22]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-2-model-support-changes-in-v1-0-90|2 Model
  Support changes in v1.0.90]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: model-support
title: 22 Model Support changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 22 Model Support changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> In browser setup, arriving suggestions no longer interrupt your typing. Reloading first-run Model Setup returns to its pending question while the same Gateway stays running, but unsubmitted answers are lost. Cancelling the attempt frees the provider choices once cancellation is confirmed.

> You can drop or paste images into Side chat for the current question. Choose an image-capable utility model, then use Retry if the previous model could not read the image. Images are not saved in restored history, so reattach them for later questions. Compatible CLI setups without direct provider credentials also gain a text-only fallback, without tools or images.

> Large model lists are more responsive to search, and the picker opens to the selected model’s provider. Usage keeps previous totals visible while refreshing and lets you retry failures. Doctor reports incomplete totals; request usage again to retry. If Cmd+K returns no models, check model settings for provider-refresh problems.

> Saved settings apply without waiting for a file-change notification, and temporary database contention no longer leaves supported changes waiting for another edit. Changing channel connection settings also preserves unaffected conversation lists and model choices. Configuration errors now explain whether a file could not be read, a setting is invalid, or a rejected edit saved nothing.

> Conversation compaction keeps already-summarized messages out of affected later summaries and loads saved history in the background so other work can continue. Messages arriving as a summary finishes use the updated conversation, and recovery stops when the run times out. If a model exhausts its output budget without producing a summary, OpenClaw stops repeating the same request and suggests lowering thinking or increasing maxTokens before retrying. Saved history remains intact.

> Replies keep their paragraph breaks and related tool activity together, and show message times and the answering model when recorded. Scrolling also avoids a stall that could happen after repeated sends.

> Use this runtime only on a single-user Gateway, with OpenClaw as the sole controller of the session. Start a new or reset chat after changing its instructions, tools, model, credentials, or execution environment. Resetting or deleting the local chat does not delete hosted history or files. Check that returned attachments arrived. Choose another runtime if you need per-turn tool restrictions from prompt hooks, restrictions on native shell/file/web access, or strictly tool-free background calls.

> GPT-6 Sol and Luna appear for accounts with access through supported OpenAI API, ChatGPT, and native Codex connections. Discovery fixes help subscription accounts find them without changing existing model choices. To use OpenClaw's own runtime, select it explicitly in the runtime settings ; choosing the model alone does not switch runtimes.

> Claude Opus 5.5 becomes the default for new Anthropic and Claude CLI setups and the rolling opus choice. Explicit Opus 5 selections stay unchanged. Opus 5.5 always uses thinking, even when you hide it. Automatic PDF analysis can use 5.5 independently of your chat model; set a PDF model explicitly to keep a particular version.

> Claude Sonnet 5.5 is available through Anthropic, and the rolling sonnet choice now selects it. Explicit version selections, including sonnet-5 , stay pinned, while fresh setup still defaults to Opus 5.5. Thinking defaults to high; choosing off still permits notes between tool calls.

> Claude Code 2.1.277 rejects the new model ID. Use an explicit sonnet-5 selection to keep Sonnet 5 on that version.

> Model menus show known choices while the full list loads and keep your current model easy to find. Repeated background refreshes no longer stall native agent runs. Reopen the menu to see newly discovered models; your account and role restrictions still apply.

> OpenClaw avoids repeatedly sending requests that a provider has already rejected, while temporary failures keep their normal retry handling . Plugin background requests can use your configured fallback models unless you explicitly chose a model. Before retrying a failed turn, check whether its tools already completed any actions.

> OpenClaw does less repeated work when receiving long replies and preparing large model requests. Buffered Anthropic replies also give other conversations time to respond.

> Gemini 3.8 Live keeps spoken turns in history and handles requests for agent help more consistently. Grok Talk avoids duplicate saved utterances and supports longer playback. Speaking over Talk replies interrupts playback again during agent consults unless you disabled interruption; Gemini Extended Thinking may still resume speaking after an interruption.

> You can choose Gemini 3.8 Flash or Flash-Lite to generate speech , with delivery instructions kept separate from the words spoken. Gemini 3.1 Flash TTS Preview remains the default.

> You can opt into Gemini Interactions for streamed replies, reasoning, images, and tools. Google defaults stay unchanged. This connection sends the needed history with each request without asking the API to store it, and can recover interrupted replies under the normal retry rules. Cached-content handles and video clipping offsets are not supported.

> Cost estimates now use the provider handling the request, and total CLI token counts are kept separate from the current conversation's context usage. Missing SuperGrok usage percentages are explained rather than shown as zero. You can also choose Ultra for planning and verification guidance across OpenClaw and Claude Code models. It uses only the reasoning the model supports; native Codex needs supported reasoning choices. Cost figures remain estimates.

> Supported newer standard Grok models get thinking controls and image-input support without waiting for each model name to be added. Grok 4.20 and variants such as Fast are excluded. DeepSeek Flash also honors thinking settings on affected OpenAI-compatible connections.

> Already-paired nodes can reconnect with --pair-if-needed after their setup code expires, provided their saved credentials still match the selected Gateway. New pairing still needs a fresh code. If you use a saved certificate fingerprint, verify the selected fingerprint before reconnecting because this recovery path does not compare it. Remote Codex connections can also retry brief connection failures before sending work; model and tool requests already sent are not replayed.

> You have more control over who can use OpenClaw, which models they can use, and whether they can upload files.

> Administrators can choose which models each role can use , including in supported native Codex runs. Removing a model stops affected requests. Visitor Access now requires an explicit modelPolicy ; {} uses the source agent's models. Restricted Codex runs are refused if their connection cannot enforce the policy.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-30-2-model-support-changes-in-v1-0-90|2 Model Support changes in v1.0.90]]
- Later: 2026-09-30 · OpenCode · [[Changes/OpenCode/2026-09-30-send-namespaced-session-and-parent-session-identity-headers-with-model-requests|Send namespaced session and parent-session identity headers with model requests]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-af92e1&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-22-model-support-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-af92e1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->