---
card_id: openclaw-2026-06-30-757cee
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Model Support: 32 changes in v2026.6.11 — We
  heard the feedback. v2026.6.11 focuses on the rough edges that make OpenClaw feel
  less…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: faba0d3141898069f3632cb62a748791b0d03219a5f450409732c7582c647e5c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-757cee
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 32 Model Support changes'
  evidence:
  - quote: We heard the feedback. v2026.6.11 focuses on the rough edges that make
      OpenClaw feel less dependable, with fixes for misplaced replies, stuck sends,
      reconnects, model setup failures, and safer admin defaults.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Heartbeat checks using reasoning-capable models now show the assistant''s
      intended reply instead of exposing internal reasoning in Telegram, WhatsApp,
      and other channels, while opt-in Thinking messages still work. #92356 Related
      #92260 . Thanks @jmpei, @tangtaizong666, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'People sharing an OpenClaw gateway can now assign different models to
      individual direct-message contacts across supported chat channels, while existing
      group and wildcard model choices keep working as before. #95120 Related #53638
      . Thanks @gandalf-at-lerian, @thomaszta, @xydigit-zt.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Model selection and setup recover more clearly when catalogs, credentials,
      streams, timeouts, compaction, or fallbacks go wrong. Affected OpenAI , OpenRouter
      , and OpenCode Go configurations now report or recover from failures more consistently
      instead of leaving users with a stale choice or a stalled request.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Gateway operators can again see provider, model, request status, and timing
      details in normal logs, making model-routing and transport problems easier to
      diagnose without enabling extra debug logging. #89648 Related #89300 . Thanks
      @enominera, @xiaobao-k8s.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Models reached through Google, Mistral, OpenAI Responses, Azure OpenAI
      Responses, and ChatGPT/Codex Responses now receive clean system instructions
      without OpenClaw''s internal cache-boundary marker leaking into the prompt.
      #89716 Thanks @enominera, @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Cron tool calls using Gemini models through OpenAI-compatible providers
      now run without nullable fields triggering provider schema rejections. #91559
      Related #91542 . Thanks @pick-cat, @qiukui666.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'The chat /models list and other plugin-aware model or provider selection
      paths now respond quickly instead of stalling for seconds and consuming a CPU
      core through repeated setup scans, while plugin changes still refresh normally.
      #93356 Thanks @obuchowski.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Hosted Ollama Cloud users can keep only the models they explicitly configured
      after a restart, without the full shared catalog being added back, while automatic
      discovery continues for local and self-hosted Ollama servers. #93956 Thanks
      @jason-allen-oneal.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Cron jobs can now retry or switch to a configured fallback model when
      a local provider returns the generic LLM request failed. error, instead of failing
      with the fallback unused. #94062 Related #93931 . Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Dashboard child sessions now handle allowed provider-qualified model choices
      consistently and give accurate recovery guidance when saved model state is stale.
      #94752 Related #94713 . Thanks @gr4via.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenRouter users can now select and run the advertised short DeepSeek
      V4 model IDs without requests failing with model_not_found because OpenClaw
      sent a duplicated provider prefix. #95268 Related #95198 . Thanks @daniel-alejandro-t,
      @darren2030.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'With /reasoning on , DeepSeek-style OpenAI-compatible models now show
      the final answer separately from their reasoning instead of folding it into
      the reasoning block, with no configuration change required. #95283 Related #95280
      . Thanks @marvinthebored, @vincentkoc, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'LM Studio users can now run quantized or multi-variant local models without
      false assistant-turn failures or phantom suffixed model entries caused by mismatched
      model keys. #95401 Thanks @monkeyleet.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Configured fallback models can now answer when Claude CLI runs out of
      credits or hits a generic runner failure, instead of leaving users with the
      failure message as the final response. #95508 Related #95489 . Thanks @mikasa0818,
      @riazrahaman, @sallyom.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Gemini-backed web searches using freshness: "day" or pd now complete instead
      of failing with a provider 400 error, while broader freshness choices and explicit
      date ranges retain stricter filtering. #95682 Thanks @sunjae-k, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Vercel AI Gateway users can now run models chosen from the live catalog,
      including live-only model IDs that are absent from OpenClaw''s bundled list.
      #95710 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Tool-heavy model responses can stream with less overhead while repeated
      tool-call IDs and encrypted reasoning details stay matched to the correct call
      across Google and OpenAI-compatible providers. #95957 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Codex-backed conversations now return to normal routing after automatic
      fast mode is cleared, preventing later turns or model changes from reusing a
      stale priority tier. 8afc1f7
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Live model-switch retries now preserve the original fast-mode cutoff for
      long-running sessions, while explicit fast mode avoids misleading automatic-cutoff
      progress messages. d990115 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Users no longer see a fast-mode reset notice while model fallback attempts
      are still running; it appears only when the run reaches its final fallback attempt.
      6eb72a8
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Users and operators now get clearer handling when a configured live model
      becomes unavailable because OpenClaw recognizes the provider's "selected model
      was not found" response as a model-not-found failure instead of a generic error.
      2405d02 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenAI Responses users, including affected Bedrock Mantle GPT-5.x reasoning
      setups, now get one clean final answer with aligned saved transcripts and replay
      context instead of dozens of repeated cumulative copies. #92399 Related #91959
      . Thanks @amersheeny, @daimingnj, @phoenixyy, @pigfoot.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Scheduled jobs and isolated sessions using opencode-go models now move
      stalled requests into configured timeout or fallback handling instead of hanging
      for minutes before ending with a generic LLM request failed error. #93965 Related
      #93610 . Thanks @forceconstant, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'After changing the default model, starting a fresh channel session with
      /new or /reset now uses the new default instead of silently reusing the previous
      cached model, while explicit /model overrides remain unchanged. #77339 Related
      #77322 . Thanks @mjamiv, @zaynl.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: '/status now keeps the active model and how to clear a pinned choice on
      one compact line, so Discord and other chat users can scan model status without
      a multi-line explanation. #95797 Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Canceling an OpenClaw run during tool work now ends it promptly instead
      of starting another model turn or leaving the session locked. #94412 Thanks
      @szsip239, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Scheduled OpenClaw jobs using cloud models now recover from silent, stuck
      model calls by default, helping prevent later cron work from backing up while
      local or self-hosted providers keep their existing timeout behavior. #94445
      Thanks @bek91.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Connected agents such as OpenCode now start through OpenClaw even when
      their harness cannot select a requested model, while genuinely unsupported model
      choices still return the original error. #96068 Related #95869 . Thanks @sabatech-dev,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenTelemetry trace backends such as Langfuse now show the actual provider/model
      name instead of "unknown" for slash-qualified model IDs. #89981 Thanks @mycarrysun,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Individual scheduled jobs can now use their own fallback models, run with
      fallbacks disabled, or return to normal fallback inheritance through the CLI
      instead of requiring operators to edit lower-level payload data. #93369 Related
      #90302 . Thanks @849261680, @walliiee.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Provider-specific tool allow/deny settings now align more consistently
      with OpenClaw's doctor warnings, including configurations with provider aliases,
      model-specific keys, OpenRouter-style model IDs, or malformed policy entries.
      8f2882f
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 32-model-support-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: model-support
  title: 32 Model Support changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-30-5-model-support-changes-in-v1-0-66|5 Model
  Support changes in v1.0.66]]'
- '[[Changes/Kimi Code/2026-06-30-refresh-provider-model-lists-automatically-in-the-background-instead-of-only-at|Refresh
  provider model lists automatically in the background instead of only…]]'
- '[[Changes/Ollama/2026-06-30-tightened-gemma-4-moe-model-loading-in-the-mlx-engine|Tightened
  Gemma 4 MoE model loading in the MLX engine]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: model-support
title: 32 Model Support changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 32 Model Support changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> We heard the feedback. v2026.6.11 focuses on the rough edges that make OpenClaw feel less dependable, with fixes for misplaced replies, stuck sends, reconnects, model setup failures, and safer admin defaults.

> Heartbeat checks using reasoning-capable models now show the assistant's intended reply instead of exposing internal reasoning in Telegram, WhatsApp, and other channels, while opt-in Thinking messages still work. #92356 Related #92260 . Thanks @jmpei, @tangtaizong666, @vincentkoc.

> People sharing an OpenClaw gateway can now assign different models to individual direct-message contacts across supported chat channels, while existing group and wildcard model choices keep working as before. #95120 Related #53638 . Thanks @gandalf-at-lerian, @thomaszta, @xydigit-zt.

> Model selection and setup recover more clearly when catalogs, credentials, streams, timeouts, compaction, or fallbacks go wrong. Affected OpenAI , OpenRouter , and OpenCode Go configurations now report or recover from failures more consistently instead of leaving users with a stale choice or a stalled request.

> Gateway operators can again see provider, model, request status, and timing details in normal logs, making model-routing and transport problems easier to diagnose without enabling extra debug logging. #89648 Related #89300 . Thanks @enominera, @xiaobao-k8s.

> Models reached through Google, Mistral, OpenAI Responses, Azure OpenAI Responses, and ChatGPT/Codex Responses now receive clean system instructions without OpenClaw's internal cache-boundary marker leaking into the prompt. #89716 Thanks @enominera, @masatohoshino.

> Cron tool calls using Gemini models through OpenAI-compatible providers now run without nullable fields triggering provider schema rejections. #91559 Related #91542 . Thanks @pick-cat, @qiukui666.

> The chat /models list and other plugin-aware model or provider selection paths now respond quickly instead of stalling for seconds and consuming a CPU core through repeated setup scans, while plugin changes still refresh normally. #93356 Thanks @obuchowski.

> Hosted Ollama Cloud users can keep only the models they explicitly configured after a restart, without the full shared catalog being added back, while automatic discovery continues for local and self-hosted Ollama servers. #93956 Thanks @jason-allen-oneal.

> Cron jobs can now retry or switch to a configured fallback model when a local provider returns the generic LLM request failed. error, instead of failing with the fallback unused. #94062 Related #93931 . Thanks @hugenshen.

> Dashboard child sessions now handle allowed provider-qualified model choices consistently and give accurate recovery guidance when saved model state is stale. #94752 Related #94713 . Thanks @gr4via.

> OpenRouter users can now select and run the advertised short DeepSeek V4 model IDs without requests failing with model_not_found because OpenClaw sent a duplicated provider prefix. #95268 Related #95198 . Thanks @daniel-alejandro-t, @darren2030.

> With /reasoning on , DeepSeek-style OpenAI-compatible models now show the final answer separately from their reasoning instead of folding it into the reasoning block, with no configuration change required. #95283 Related #95280 . Thanks @marvinthebored, @vincentkoc, @zengwen-dt.

> LM Studio users can now run quantized or multi-variant local models without false assistant-turn failures or phantom suffixed model entries caused by mismatched model keys. #95401 Thanks @monkeyleet.

> Configured fallback models can now answer when Claude CLI runs out of credits or hits a generic runner failure, instead of leaving users with the failure message as the final response. #95508 Related #95489 . Thanks @mikasa0818, @riazrahaman, @sallyom.

> Gemini-backed web searches using freshness: "day" or pd now complete instead of failing with a provider 400 error, while broader freshness choices and explicit date ranges retain stricter filtering. #95682 Thanks @sunjae-k, @vincentkoc.

> Vercel AI Gateway users can now run models chosen from the live catalog, including live-only model IDs that are absent from OpenClaw's bundled list. #95710 Thanks @vincentkoc.

> Tool-heavy model responses can stream with less overhead while repeated tool-call IDs and encrypted reasoning details stay matched to the correct call across Google and OpenAI-compatible providers. #95957 Thanks @vincentkoc.

> Codex-backed conversations now return to normal routing after automatic fast mode is cleared, preventing later turns or model changes from reusing a stale priority tier. 8afc1f7

> Live model-switch retries now preserve the original fast-mode cutoff for long-running sessions, while explicit fast mode avoids misleading automatic-cutoff progress messages. d990115 Thanks @vincentkoc.

> Users no longer see a fast-mode reset notice while model fallback attempts are still running; it appears only when the run reaches its final fallback attempt. 6eb72a8

> Users and operators now get clearer handling when a configured live model becomes unavailable because OpenClaw recognizes the provider's "selected model was not found" response as a model-not-found failure instead of a generic error. 2405d02 Thanks @vincentkoc.

> OpenAI Responses users, including affected Bedrock Mantle GPT-5.x reasoning setups, now get one clean final answer with aligned saved transcripts and replay context instead of dozens of repeated cumulative copies. #92399 Related #91959 . Thanks @amersheeny, @daimingnj, @phoenixyy, @pigfoot.

> Scheduled jobs and isolated sessions using opencode-go models now move stalled requests into configured timeout or fallback handling instead of hanging for minutes before ending with a generic LLM request failed error. #93965 Related #93610 . Thanks @forceconstant, @zhangguiping-xydt.

> After changing the default model, starting a fresh channel session with /new or /reset now uses the new default instead of silently reusing the previous cached model, while explicit /model overrides remain unchanged. #77339 Related #77322 . Thanks @mjamiv, @zaynl.

> /status now keeps the active model and how to clear a pinned choice on one compact line, so Discord and other chat users can scan model status without a multi-line explanation. #95797 Thanks @solvely-colin.

> Canceling an OpenClaw run during tool work now ends it promptly instead of starting another model turn or leaving the session locked. #94412 Thanks @szsip239, @vincentkoc.

> Scheduled OpenClaw jobs using cloud models now recover from silent, stuck model calls by default, helping prevent later cron work from backing up while local or self-hosted providers keep their existing timeout behavior. #94445 Thanks @bek91.

> Connected agents such as OpenCode now start through OpenClaw even when their harness cannot select a requested model, while genuinely unsupported model choices still return the original error. #96068 Related #95869 . Thanks @sabatech-dev, @vincentkoc.

> OpenTelemetry trace backends such as Langfuse now show the actual provider/model name instead of "unknown" for slash-qualified model IDs. #89981 Thanks @mycarrysun, @vincentkoc.

> Individual scheduled jobs can now use their own fallback models, run with fallbacks disabled, or return to normal fallback inheritance through the CLI instead of requiring operators to edit lower-level payload data. #93369 Related #90302 . Thanks @849261680, @walliiee.

> Provider-specific tool allow/deny settings now align more consistently with OpenClaw's doctor warnings, including configurations with provider aliases, model-specific keys, OpenRouter-style model IDs, or malformed policy entries. 8f2882f

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11|15 Mobile and Desktop changes in v2026.6.11]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-06-30-5-collaboration-changes-in-v2026-6-11|5 Collaboration changes in v2026.6.11]] · Collaboration
- [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Memory and Personalization
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-6-voice-and-audio-changes-in-v2026-6-11|6 Voice and Audio changes in v2026.6.11]] · Voice and Audio
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur|When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…]] · Pricing Model
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-30 · Ollama · [[Changes/Ollama/2026-06-30-tightened-gemma-4-moe-model-loading-in-the-mlx-engine|Tightened Gemma 4 MoE model loading in the MLX engine]]
- Later: 2026-06-30 · OpenCode · [[Changes/OpenCode/2026-06-30-4-model-support-changes-in-v1-17-12|4 Model Support changes in v1.17.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-757cee&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-32-model-support-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-757cee%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->