---
card_id: openclaw-2026-10-10-46d42b
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Model Support: 18 changes in v2026.10.1 — Model
  choices and prices can update without restarting OpenClaw, at a catalog check or
  after…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1370
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4cf883fa7deb1012e554c490b1645c5c312e2e49c021a37c45882715fc73ec46
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-46d42b
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 18 Model Support changes'
  evidence:
  - quote: Model choices and prices can update without restarting OpenClaw, at a catalog
      check or after an explicit model-list refresh. Work already underway keeps its
      original model information and prices. If a downloaded catalog contains incorrect
      choices or prices, disable remote catalog refresh until a corrected newer catalog
      is available.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: OpenAI API-key users can select supported chat models their account lists
      before those models reach the bundled catalog. These entries use conservative,
      text-only limits, and an omitted cost means the price is unknown. Model-list
      fixes also reduce repeated preparation and duplicated data, keep DeepInfra discovery
      working with unexpected metadata, and prevent overflowing Vercel prices from
      appearing as infinite costs.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: GitHub Copilot adds bundled Claude Sonnet 5.5 and Opus 5.5 definitions
      for accounts with access. Ollama Cloud can honor maximum thinking for GLM 5.3,
      GLM 5.3 Flash, Kimi K3 and DeepSeek V4.1 Flash, including verified models reached
      directly at ollama.com; local relays still use high effort for compatibility.
      Eligible Daybreak Blue and Red accounts regain xhigh and max, while supported
      Codex and other provider replies retain your chosen thinking settings.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: New Baseten setups start with DeepSeek V4.1 Flash, with supported Flash
      image and thinking options and current Pro conversation replay restored. If
      your saved Inkling model is unavailable, select a replacement manually. Thinking
      Off does not always stop reasoning. On Ollama Cloud GLM 5.3 and GLM 5.3 Flash
      it uses low effort and keeps reasoning out of the answer; on xAI models without
      effort controls it leaves native reasoning in place.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Model settings show which runtime and account handle background summaries,
      titles and progress narration. Eligible automatically selected background models
      for the same provider can use your primary model's CLI runtime when their API
      credentials are unavailable. Usable API credentials and explicit model or runtime
      choices keep their own routes and billing. See the CLI backend guide .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: With experimental Decision assistance enabled and a model selected, a conversational
      turn can leave out optional tools judged unnecessary. Required tools and permissions
      remain intact, and later turns start with their normal tools. It is off by default,
      but a saved opt-in can start this automatic behavior after upgrading . Unsupported
      runtimes, including Codex app-server, keep their normal tools.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: GitHub invitations need an existing verified Cloudflare OIDC account-ID
      mapping. Choose a single GitHub or email target and use the profile or invitation
      ID for revocation. Person-wide revocation requires host support and ends recorded
      grants, so independent access can remain. See the user model and identity requirements
      .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Model setup lets you correct a bad LM Studio or llama.cpp address and continue.
      If the Gateway restarts during web setup, a successful settings refresh can
      reopen provider selection or offer verification of a saved model. Check again
      retries a failed refresh; a saved model still needs verification. See the setup
      reference .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Model choices: Choosing a model focuses search immediately, keeps long
      choices readable and distinguishes configured Codex alternatives.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Sending several files in a supported quoted list or compact array keeps
      every attachment in order, including filenames with spaces or commas. Long code
      blocks and unusual line endings keep their formatting and captions. Supported
      speech-only answers can complete alongside model reasoning without filler chat
      text. See the TTS reply guide and restricted-profile setup .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: A queued follow-up can still finish after its original request closes,
      and a system-clock change no longer stretches its normal quiet period. Canceling
      while model settings load frees the conversation for your next message. Reset
      and deletion wait for channel work that has already started to settle.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Choosing a provider now keeps your model on that provider when an alias
      collides with its name. openai/gpt-4o-mini selects OpenAI; use openrouter/openai/gpt-4o-mini
      to retain the former OpenRouter alias route. Check affected selections, because
      the route can change credentials, availability and cost. Adding fallbacks keeps
      the primary model, queued choices survive older cleanup, and shared fallback
      changes require omitting --agent .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Windows local-model setup can recover when llama.cpp is missing Visual
      C++ runtime files by placing them beside the managed server. If that recovery
      fails, rerun setup or configure a compatible server manually.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Older ZAI and Ollama Cloud configurations may need manual changes. ZAI
      usage checks now use supported configuration, the auth store, ZAI_API_KEY or
      Z_AI_API_KEY . Replace Ollama Cloud's retired https://ai.ollama.com address
      with https://ollama.com in models.providers.ollama-cloud.baseUrl ; Doctor no
      longer corrects or warns about the old address.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: OpenAI and Azure Responses keep your requested JSON output format, and
      recovered DeepSeek calls keep literal names and empty-string arguments. Models
      that see images directly avoid unrelated media-provider loading errors.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Failed requests give clearer retry hints and preserve the original rejection,
      while local SQLite errors stop pointless model switching. Eligible malformed
      or output-limited tool calls get at most one recovery attempt; incomplete calls
      do not execute, and completed results stay available. Check results before repeating
      work, because earlier actions may already have finished. Remote Codex launch
      failures point to execution approval without rotating healthy credentials.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Claude CLI resumes pick up updated instructions, affected Ollama models
      regain tool execution with Tool Search, and Gemma 4 can recover complete standalone
      tool requests returned as text. ChatGPT also gains a bounded retry for a specific
      rejected WebSocket continuation, preserving completed tool results.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Reply model lookup honors disabled plugins for custom providers, aliases
      and model overrides. 120b43633fde . Thanks @steipete .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 18-model-support-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: model-support
  title: 18 Model Support changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/OpenHands/2026-10-08-test-e2e-launch-the-same-model-profile-test-from-the-beta-profile-by-enyst-in-ht|test(e2e):
  launch the same-model profile test from the BETA profile]]'
- '[[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude
  Tag Changed Claude in Slack to show the footer with the session link, model…]]'
- '[[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support
  changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: model-support
title: 18 Model Support changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Model Support changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Model choices and prices can update without restarting OpenClaw, at a catalog check or after an explicit model-list refresh. Work already underway keeps its original model information and prices. If a downloaded catalog contains incorrect choices or prices, disable remote catalog refresh until a corrected newer catalog is available.

> OpenAI API-key users can select supported chat models their account lists before those models reach the bundled catalog. These entries use conservative, text-only limits, and an omitted cost means the price is unknown. Model-list fixes also reduce repeated preparation and duplicated data, keep DeepInfra discovery working with unexpected metadata, and prevent overflowing Vercel prices from appearing as infinite costs.

> GitHub Copilot adds bundled Claude Sonnet 5.5 and Opus 5.5 definitions for accounts with access. Ollama Cloud can honor maximum thinking for GLM 5.3, GLM 5.3 Flash, Kimi K3 and DeepSeek V4.1 Flash, including verified models reached directly at ollama.com; local relays still use high effort for compatibility. Eligible Daybreak Blue and Red accounts regain xhigh and max, while supported Codex and other provider replies retain your chosen thinking settings.

> New Baseten setups start with DeepSeek V4.1 Flash, with supported Flash image and thinking options and current Pro conversation replay restored. If your saved Inkling model is unavailable, select a replacement manually. Thinking Off does not always stop reasoning. On Ollama Cloud GLM 5.3 and GLM 5.3 Flash it uses low effort and keeps reasoning out of the answer; on xAI models without effort controls it leaves native reasoning in place.

> Model settings show which runtime and account handle background summaries, titles and progress narration. Eligible automatically selected background models for the same provider can use your primary model's CLI runtime when their API credentials are unavailable. Usable API credentials and explicit model or runtime choices keep their own routes and billing. See the CLI backend guide .

> With experimental Decision assistance enabled and a model selected, a conversational turn can leave out optional tools judged unnecessary. Required tools and permissions remain intact, and later turns start with their normal tools. It is off by default, but a saved opt-in can start this automatic behavior after upgrading . Unsupported runtimes, including Codex app-server, keep their normal tools.

> GitHub invitations need an existing verified Cloudflare OIDC account-ID mapping. Choose a single GitHub or email target and use the profile or invitation ID for revocation. Person-wide revocation requires host support and ends recorded grants, so independent access can remain. See the user model and identity requirements .

> Model setup lets you correct a bad LM Studio or llama.cpp address and continue. If the Gateway restarts during web setup, a successful settings refresh can reopen provider selection or offer verification of a saved model. Check again retries a failed refresh; a saved model still needs verification. See the setup reference .

> Model choices: Choosing a model focuses search immediately, keeps long choices readable and distinguishes configured Codex alternatives.

> Sending several files in a supported quoted list or compact array keeps every attachment in order, including filenames with spaces or commas. Long code blocks and unusual line endings keep their formatting and captions. Supported speech-only answers can complete alongside model reasoning without filler chat text. See the TTS reply guide and restricted-profile setup .

> A queued follow-up can still finish after its original request closes, and a system-clock change no longer stretches its normal quiet period. Canceling while model settings load frees the conversation for your next message. Reset and deletion wait for channel work that has already started to settle.

> Choosing a provider now keeps your model on that provider when an alias collides with its name. openai/gpt-4o-mini selects OpenAI; use openrouter/openai/gpt-4o-mini to retain the former OpenRouter alias route. Check affected selections, because the route can change credentials, availability and cost. Adding fallbacks keeps the primary model, queued choices survive older cleanup, and shared fallback changes require omitting --agent .

> Windows local-model setup can recover when llama.cpp is missing Visual C++ runtime files by placing them beside the managed server. If that recovery fails, rerun setup or configure a compatible server manually.

> Older ZAI and Ollama Cloud configurations may need manual changes. ZAI usage checks now use supported configuration, the auth store, ZAI_API_KEY or Z_AI_API_KEY . Replace Ollama Cloud's retired https://ai.ollama.com address with https://ollama.com in models.providers.ollama-cloud.baseUrl ; Doctor no longer corrects or warns about the old address.

> OpenAI and Azure Responses keep your requested JSON output format, and recovered DeepSeek calls keep literal names and empty-string arguments. Models that see images directly avoid unrelated media-provider loading errors.

> Failed requests give clearer retry hints and preserve the original rejection, while local SQLite errors stop pointless model switching. Eligible malformed or output-limited tool calls get at most one recovery attempt; incomplete calls do not execute, and completed results stay available. Check results before repeating work, because earlier actions may already have finished. Remote Codex launch failures point to execution approval without rotating healthy credentials.

> Claude CLI resumes pick up updated instructions, affected Ollama models regain tool execution with Tool Search, and Gemma 4 can recover complete standalone tool requests returned as text. ChatGPT also gains a bounded retry for a specific rejected WebSocket continuation, preserving completed tool results.

> Reply model lookup honors disabled plugins for custom providers, aliases and model overrides. 120b43633fde . Thanks @steipete .

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-49-model-support-changes-in-v0-12-0|49 Model Support changes in v0.12.0]]
- Later: 2026-10-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-12-2-model-support-changes-in-v1-0-96|2 Model Support changes in v1.0.96]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-46d42b&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-18-model-support-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-46d42b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->