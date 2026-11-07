---
card_id: openclaw-2026-06-30-259e70
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Context Window: 20 changes in v2026.6.11 — WhatsApp
  group conversations now preserve the right message and group context more reliably…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2477
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b6d42868d5d5838e638798d47688cd83b3ede3528408cbd7988a2c801c815157
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-259e70
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 20 Context Window changes'
  evidence:
  - quote: 'WhatsApp group conversations now preserve the right message and group
      context more reliably during retries, reconnects, and group changes. #94338
      Related #7433 . Thanks @mcaxtr, @octopuslabs-fl, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'WhatsApp replies now stay attached to the direct or group message being
      answered instead of appearing as a separate message that loses the conversation
      context. #95483 Thanks @mcaxtr.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Channel progress now shows a repeated status when work genuinely returns
      to it after another update, instead of hiding useful context as a duplicate.
      8a75c4d
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Expired provider tokens no longer bury useful operator logs under repeated
      fallback warnings, while the first warning and later duplicate summaries remain
      available for diagnosis. #94233 Related #56979 . Thanks @goutamadwant, @yanan1991.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Google Gemini 3.5 Flash can now be selected with its full 1,048,576-token
      context window, avoiding missing-model errors and needless prompt-size rejections.
      #94726 Related #94723 . Thanks @ajwan8998, @anguslogan01, @kevinat.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Follow-up answers from xAI reasoning models such as Grok Composer now
      preserve earlier reasoning context more reliably, even when configurable reasoning
      effort is unsupported. #95686 Thanks @fuller-stack-dev, @geraint0923.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Xiaomi Token Plan users can now use up to 128K output tokens with mimo-v2.5
      and mimo-v2.5-pro instead of being stopped at the outdated 32,000-token limit.
      #95934 Thanks @idootop.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Ollama Cloud users can now find and select glm-5.2:cloud with its 1,000,000-token
      context window, reasoning, and tool support even when it is absent from the
      public model list. 11484f8
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'WebChat''s current-session status now matches the conversation you are
      actually using, so the session identity, thinking level, token context, and
      cost details no longer come from the fallback main session. #89800 Related #89773
      . Thanks @killo3967, @sweetcornna.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Your conversation is less likely to lose its context after you press stop
      during automatic compaction because the compaction request is now cancelled
      too. #89886 Related #89868 . Thanks @lykeion-dev, @openperf, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Repeated instructions sent after compaction now remain in the conversation,
      preventing lost turns, orphaned replies, and malformed history that some providers
      reject. #94328 Thanks @vincentkoc, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Usage footers selected with /usage full or /usage tokens now remain visible
      after daily or idle session rollover, so users do not have to turn them on again.
      #95322 Thanks @litang9.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Long-running main conversations now keep their prior context when users
      return after an overnight or delayed follow-up, rather than silently starting
      over after an otherwise normal completion. #95472 Thanks @xydt-tanshanshan.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Telegram reply chains keep cached replies attached after context changes
      instead of failing when those cached replies are reused. #82909 Thanks @lidge-jun.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Slack operators can now store tokens and signing secrets as supported SecretRef
      inputs, while reads, writes, allowlist and target lookups, and setup checks
      use the resolved credentials instead of rejecting or misreading the references.
      7da955f Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Plugins using heartbeat_prompt_contribution now deliver their heartbeat-specific
      context to models when agents run through harness runtimes such as the Codex
      app-server, without affecting ordinary user turns or plugins that do not use
      the hook. #96233 Thanks @azogheb, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Long-context, tool-heavy agent sessions now keep prompt-cache reuse steadier
      across repeated turns without losing per-result size limits, while advanced
      operators can configure larger tool-result caps for large-context models without
      configuration rejection. a60947f Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Long, tool-heavy agent sessions are less likely to bloat model requests
      as tool output accumulates, while repeated turns keep stable prompt-cache reuse.
      2f33999 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When users reopen a Control UI conversation from History, their prompts
      now appear with the assistant''s replies, preserving the question-and-answer
      context without blank gaps in long transcripts. #93841 Related #90241 . Thanks
      @mushuiyu886, @pronzcw.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Control UI users now see shorter System, Light, and Dark theme tooltips,
      while screen readers announce less repetitive labels without losing the surrounding
      Color mode context. #95837 Thanks @hannesrudolph, @sannidhyasah.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 20-context-window-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: context-window
  title: 20 Context Window changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-06-29-2-context-window-changes-in-kimi-code-0-20-2|2 Context
  Window changes in Kimi Code 0.20.2]]'
- '[[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window
  changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep
  session-store searches and context lookups responsive]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: context-window
title: 20 Context Window changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Context Window changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> WhatsApp group conversations now preserve the right message and group context more reliably during retries, reconnects, and group changes. #94338 Related #7433 . Thanks @mcaxtr, @octopuslabs-fl, @xialonglee.

> WhatsApp replies now stay attached to the direct or group message being answered instead of appearing as a separate message that loses the conversation context. #95483 Thanks @mcaxtr.

> Channel progress now shows a repeated status when work genuinely returns to it after another update, instead of hiding useful context as a duplicate. 8a75c4d

> Expired provider tokens no longer bury useful operator logs under repeated fallback warnings, while the first warning and later duplicate summaries remain available for diagnosis. #94233 Related #56979 . Thanks @goutamadwant, @yanan1991.

> Google Gemini 3.5 Flash can now be selected with its full 1,048,576-token context window, avoiding missing-model errors and needless prompt-size rejections. #94726 Related #94723 . Thanks @ajwan8998, @anguslogan01, @kevinat.

> Follow-up answers from xAI reasoning models such as Grok Composer now preserve earlier reasoning context more reliably, even when configurable reasoning effort is unsupported. #95686 Thanks @fuller-stack-dev, @geraint0923.

> Xiaomi Token Plan users can now use up to 128K output tokens with mimo-v2.5 and mimo-v2.5-pro instead of being stopped at the outdated 32,000-token limit. #95934 Thanks @idootop.

> Ollama Cloud users can now find and select glm-5.2:cloud with its 1,000,000-token context window, reasoning, and tool support even when it is absent from the public model list. 11484f8

> WebChat's current-session status now matches the conversation you are actually using, so the session identity, thinking level, token context, and cost details no longer come from the fallback main session. #89800 Related #89773 . Thanks @killo3967, @sweetcornna.

> Your conversation is less likely to lose its context after you press stop during automatic compaction because the compaction request is now cancelled too. #89886 Related #89868 . Thanks @lykeion-dev, @openperf, @vincentkoc.

> Repeated instructions sent after compaction now remain in the conversation, preventing lost turns, orphaned replies, and malformed history that some providers reject. #94328 Thanks @vincentkoc, @yetval.

> Usage footers selected with /usage full or /usage tokens now remain visible after daily or idle session rollover, so users do not have to turn them on again. #95322 Thanks @litang9.

> Long-running main conversations now keep their prior context when users return after an overnight or delayed follow-up, rather than silently starting over after an otherwise normal completion. #95472 Thanks @xydt-tanshanshan.

> Telegram reply chains keep cached replies attached after context changes instead of failing when those cached replies are reused. #82909 Thanks @lidge-jun.

> Slack operators can now store tokens and signing secrets as supported SecretRef inputs, while reads, writes, allowlist and target lookups, and setup checks use the resolved credentials instead of rejecting or misreading the references. 7da955f Thanks @vincentkoc.

> Plugins using heartbeat_prompt_contribution now deliver their heartbeat-specific context to models when agents run through harness runtimes such as the Codex app-server, without affecting ordinary user turns or plugins that do not use the hook. #96233 Thanks @azogheb, @vincentkoc.

> Long-context, tool-heavy agent sessions now keep prompt-cache reuse steadier across repeated turns without losing per-result size limits, while advanced operators can configure larger tool-result caps for large-context models without configuration rejection. a60947f Thanks @vincentkoc.

> Long, tool-heavy agent sessions are less likely to bloat model requests as tool output accumulates, while repeated turns keep stable prompt-cache reuse. 2f33999 Thanks @vincentkoc.

> When users reopen a Control UI conversation from History, their prompts now appear with the assistant's replies, preserving the question-and-answer context without blank gaps in long transcripts. #93841 Related #90241 . Thanks @mushuiyu886, @pronzcw.

> Control UI users now see shorter System, Light, and Dark theme tooltips, while screen readers announce less repetitive labels without losing the surrounding Color mode context. #95837 Thanks @hannesrudolph, @sannidhyasah.

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-32-agent-mode-changes-in-v2026-6-11|32 Agent Mode changes in v2026.6.11]] · Agent Mode
- [[Changes/OpenClaw/2026-06-30-15-mobile-and-desktop-changes-in-v2026-6-11|15 Mobile and Desktop changes in v2026.6.11]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-06-30-5-collaboration-changes-in-v2026-6-11|5 Collaboration changes in v2026.6.11]] · Collaboration
- [[Changes/OpenClaw/2026-06-30-26-memory-and-personalization-changes-in-v2026-6-11|26 Memory and Personalization changes in v2026.6.11]] · Memory and Personalization
- [[Changes/OpenClaw/2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11|34 Apps and Integrations changes in v2026.6.11]] · Apps and Integrations
- [[Changes/OpenClaw/2026-06-30-6-voice-and-audio-changes-in-v2026-6-11|6 Voice and Audio changes in v2026.6.11]] · Voice and Audio
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
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
## Nearby in Context Window

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]]
- Later: 2026-06-30 · OpenCode · [[Changes/OpenCode/2026-06-30-desktop-show-stored-token-and-cost-totals-in-the-session-context|Desktop Show stored token and cost totals in the session context]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-259e70&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-20-context-window-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-259e70%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->