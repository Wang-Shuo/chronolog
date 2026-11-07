---
card_id: openclaw-2026-10-12-31a96f
date: '2026-10-12'
description: 'OpenClaw · 2026-10-12 · Model Support: 9 changes in v2026.10.2 — Compaction
  during model cooldowns. A working configured fallback can summarize a long…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1372
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2087193864bfa342bf30bccab1f7bf389f7f143741b7fed74d10796bf0b7a507
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-12-31a96f
  comparison: ''
  date: '2026-10-12'
  description: 'OpenClaw — v2026.10.2: 9 Model Support changes'
  evidence:
  - quote: 'Compaction during model cooldowns. A working configured fallback can summarize
      a long conversation while the primary credentials cool down after a quota failure,
      without changing the selected session model. Explicit compaction-model overrides
      stay exact; see the compaction guide . #166459 , thanks to @steipete and @hawkit
      .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Local model replies. Models with strict Chat Completions templates can
      keep replying after background notices that previously caused a message-format
      error. #167309 , thanks to @jlapenna and @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: Local llama.cpp setup. Setup checks whether the server can run before downloading
      model files and explains alternatives when it cannot. Managed macOS binaries
      require 13.3 or later; older Macs can use a working existing or compatible custom
      server through local-model service configuration . e0de414 , thanks to @NovaUnboundAi
      , @xXG0DLessXx and @VACInc .
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Loading models for saved chats. Continuing a conversation from the saved-session
      catalog or changing chat settings no longer hangs indefinitely while loading
      the model list. A timeout lets you retry without leaving a partially created
      chat or applying a rejected settings change later. Bulk settings changes still
      report each chat''s result separately. See session-control guidance . #166089
      , #166376 , thanks to @ericcaiwx-star , @steipete and @dprev .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Model-list changes during startup. A model-list update between startup
      checks and execution no longer causes the reported refusal to start a chat or
      scheduled job. #168410 , thanks to @RomneyDa .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Claude history caching. After a large document, image or tool exchange,
      Claude can still reuse eligible cached earlier conversation history. Bedrock
      also chooses a caching duration supported by the selected model and profile.
      See prompt-caching guidance . #168042 , thanks to @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Conversation history and caching. Reopened chats keep the same shortened
      tool-result text the model saw originally. Browser chats can keep reusing cached
      conversation text when a helper reports back privately, and Claude caches earlier
      history without temporary instructions that disappear later. See prompt-caching
      guidance . #168392 , thanks to @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Codex max thinking. Scheduled and webhook turns honor the existing max-thinking
      setting when the selected model supports it, instead of silently using its default
      effort. #165444 , thanks to @Oldrich333 .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  - quote: 'Background tools. Tasks no longer get cancelled as stalled after background
      tools have successfully finished, even if the next model response reaches its
      output limit. See queue guidance . #166997 , thanks to @SunnyShu0925 , @steipete
      , @hannesrudolph and @hippoley .'
    source_release: https://docs.openclaw.ai/releases/2026.10.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-model-support-changes-in-v2026-10-2
  source_release: openclaw-2026-10-12-v2026-10-2-9abf70fc
  source_type: openclaw_changelog
  theme: model-support
  title: 9 Model Support changes in v2026.10.2
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support
  changes in v2026.10.1]]'
- '[[Changes/GitHub Copilot CLI/2026-10-12-2-model-support-changes-in-v1-0-96|2 Model
  Support changes in v1.0.96]]'
- '[[Changes/Ollama/2026-10-12-3-model-support-changes-in-v0-40-4|3 Model Support
  changes in v0.40.4]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|openclaw-2026-10-12-v2026-10-2-9abf70fc]]'
source_type: openclaw_changelog
theme: model-support
title: 9 Model Support changes in v2026.10.2
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Model Support changes in v2026.10.2

**OpenClaw** · 2026-10-12 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.2) · from [[Releases/OpenClaw/openclaw-2026-10-12-v2026-10-2-9abf70fc|v2026.10.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Compaction during model cooldowns. A working configured fallback can summarize a long conversation while the primary credentials cool down after a quota failure, without changing the selected session model. Explicit compaction-model overrides stay exact; see the compaction guide . #166459 , thanks to @steipete and @hawkit .

> Local model replies. Models with strict Chat Completions templates can keep replying after background notices that previously caused a message-format error. #167309 , thanks to @jlapenna and @steipete .

> Local llama.cpp setup. Setup checks whether the server can run before downloading model files and explains alternatives when it cannot. Managed macOS binaries require 13.3 or later; older Macs can use a working existing or compatible custom server through local-model service configuration . e0de414 , thanks to @NovaUnboundAi , @xXG0DLessXx and @VACInc .

> Loading models for saved chats. Continuing a conversation from the saved-session catalog or changing chat settings no longer hangs indefinitely while loading the model list. A timeout lets you retry without leaving a partially created chat or applying a rejected settings change later. Bulk settings changes still report each chat's result separately. See session-control guidance . #166089 , #166376 , thanks to @ericcaiwx-star , @steipete and @dprev .

> Model-list changes during startup. A model-list update between startup checks and execution no longer causes the reported refusal to start a chat or scheduled job. #168410 , thanks to @RomneyDa .

> Claude history caching. After a large document, image or tool exchange, Claude can still reuse eligible cached earlier conversation history. Bedrock also chooses a caching duration supported by the selected model and profile. See prompt-caching guidance . #168042 , thanks to @steipete .

> Conversation history and caching. Reopened chats keep the same shortened tool-result text the model saw originally. Browser chats can keep reusing cached conversation text when a helper reports back privately, and Claude caches earlier history without temporary instructions that disappear later. See prompt-caching guidance . #168392 , thanks to @steipete .

> Codex max thinking. Scheduled and webhook turns honor the existing max-thinking setting when the selected model supports it, instead of silently using its default effort. #165444 , thanks to @Oldrich333 .

> Background tools. Tasks no longer get cancelled as stalled after background tools have successfully finished, even if the next model response reaches its output limit. See queue guidance . #166997 , thanks to @SunnyShu0925 , @steipete , @hannesrudolph and @hippoley .

Source: https://docs.openclaw.ai/releases/2026.10.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-12-5-apps-and-integrations-changes-in-v2026-10-2|5 Apps and Integrations changes in v2026.10.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-12-4-memory-and-personalization-changes-in-v2026-10-2|4 Memory and Personalization changes in v2026.10.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-12-older-session-history-doctor-can-continue-repairing-leftover-session-files-while|Older session history]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-12-2-pricing-model-changes-in-v2026-10-2|2 Pricing Model changes in v2026.10.2]] · Pricing Model
- [[Changes/OpenClaw/2026-10-12-4-context-window-changes-in-v2026-10-2|4 Context Window changes in v2026.10.2]] · Context Window
- [[Changes/OpenClaw/2026-10-12-dictation-holding-the-microphone-and-releasing-it-no-longer-stops-recording-prem|Dictation. Holding the microphone and releasing it no longer stops recording prematurely]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-12-managed-browser-tabs-at-the-shared-tab-limit-locally-managed-browser-cleanup-fav|Managed browser tabs]] · Editor Experience
- [[Changes/OpenClaw/2026-10-12-2-developer-workflow-changes-in-v2026-10-2|2 Developer Workflow changes in v2026.10.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-12-home-notifications-creating-many-chats-no-longer-fills-home-s-notification-queue|Home notifications]] · Collaboration
- [[Changes/OpenClaw/2026-10-12-manually-started-jobs-an-accepted-automation-can-keep-using-its-allowed-tools-af|Manually started jobs]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-12-5-agent-mode-changes-in-v2026-10-2|5 Agent Mode changes in v2026.10.2]] · Agent Mode
- [[Changes/OpenClaw/2026-10-12-2-mobile-and-desktop-changes-in-v2026-10-2|2 Mobile and Desktop changes in v2026.10.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-12-plugin-approval-waits-affected-plugin-tools-can-wait-for-your-approval-for-the-e|Plugin approval waits]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-12-summaries-before-completion-replies-when-a-long-conversation-needs-a-summary-ope|Summaries before completion replies]] · Interface Experience
- [[Changes/OpenClaw/2026-10-12-23-other-changes-in-v2026-10-2|23 other changes in v2026.10.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-12 · Ollama · [[Changes/Ollama/2026-10-12-3-model-support-changes-in-v0-40-4|3 Model Support changes in v0.40.4]]
- Later: 2026-10-12 · OpenHands · [[Changes/OpenHands/2026-10-12-3-model-support-changes-in-v1-27-0|3 Model Support changes in v1.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-12-31a96f&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-12-9-model-support-changes-in-v2026-10-2.md%0ACard%20ID%3A%20openclaw-2026-10-12-31a96f%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->