---
card_id: openclaw-2026-09-08-4104d1
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Mobile and Desktop: 10 changes in v2026.9.3
  — Available create-capable CLI agents appear by default, subject to terminal availability…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2858
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2fd90afd0c88d6da2775f12b099642f1e048eca5ac3ed75f718acf1fff3371d3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-4104d1
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 10 Mobile and Desktop changes'
  evidence:
  - quote: Available create-capable CLI agents appear by default, subject to terminal
      availability, permissions and node authority; explicit opt-outs remain available.
      Bun-hosted Gateways can start native Codex and Claude Code terminals on Linux
      and macOS using Node on the Gateway PATH.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: WhatsApp approval reactions remain available for replay after transient
      Gateway failures instead of being discarded prematurely. The Gateway still decides
      which answer is accepted first.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: You can send a follow-up while Android is working without clearing that
      run’s output, and reopened chats return to the latest content while manual scrolling
      still pauses following. Android keeps completed runs settled when delayed history
      or send acknowledgements arrive, and overlapping history requests no longer
      leave the chat’s health refresh unfinished. Resolved approval cards disappear
      together with their outcome, while a failed file share leaves the preview open
      so you can retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: During prolonged outages, Android backs off repeated reconnect attempts
      and resumes retrying when the network returns. Settings search finds existing
      options by name or category, and model settings follow the selected agent’s
      credentials and accepted configuration changes. Failed model refreshes show
      a warning while preserving choices and drafts, with another attempt available
      through Refresh chat.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Android’s compact Model sheet keeps more of the conversation visible while
      distinguishing the space left in the current context from the latest run’s accumulated
      usage. Stale counters clear after compaction and history refresh, and optional
      model-call details remain available without treating unknown usage as zero.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Persistent paired computers retain the current worker build between sessions,
      avoiding another installation when that build is already present. A new build
      still needs installation on first use. Android setup also saves replacement
      access before retiring setup credentials, so a newly supplied setup code keeps
      its intended meaning.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Chrome relay tabs can also recover after attachment loss without restarting
      the browser stack. Opening an old browser result keeps a stopped managed browser
      stopped and offers Start browser when needed. Preview capture preserves focus
      for verified visible attached Chrome sessions on macOS and Linux, and screenshot
      annotations follow the actual image scale and crop.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Remote desktop input sends supplementary Unicode characters as complete
      code points, avoiding split characters during typing and deletion. The keyboard
      stays disabled until connected control is ready.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Failed cloud-tool results are recorded as failures before they enter conversation
      history. A failed desktop cleanup remains visible and can be retried before
      another desktop opens. OpenClaw keeps the resources needed to finish that cleanup,
      and blocks reopening while the previous desktop remains unresolved.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Desktop viewing and control end when the requesting Gateway connection
      disconnects or loses authority. Connection-bound tickets and both relay directions
      are checked, while internal callers without a connection retain their existing
      timeout-based behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-mobile-and-desktop-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 10 Mobile and Desktop changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile
  and Desktop changes in v2026.9.2]]'
- '[[Changes/Qoder/2026-09-05-installer-better-process-detection-and-install-recovery-on-windows|Installer:
  Better process detection and install recovery on Windows]]'
- '[[Changes/ChatGPT/2026-09-08-turn-a-sketch-into-an-image-on-mobile-type-in-the-message-box-and-select-sketch|Turn
  a sketch into an image]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 10 Mobile and Desktop changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Mobile and Desktop changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Available create-capable CLI agents appear by default, subject to terminal availability, permissions and node authority; explicit opt-outs remain available. Bun-hosted Gateways can start native Codex and Claude Code terminals on Linux and macOS using Node on the Gateway PATH.

> WhatsApp approval reactions remain available for replay after transient Gateway failures instead of being discarded prematurely. The Gateway still decides which answer is accepted first.

> You can send a follow-up while Android is working without clearing that run’s output, and reopened chats return to the latest content while manual scrolling still pauses following. Android keeps completed runs settled when delayed history or send acknowledgements arrive, and overlapping history requests no longer leave the chat’s health refresh unfinished. Resolved approval cards disappear together with their outcome, while a failed file share leaves the preview open so you can retry.

> During prolonged outages, Android backs off repeated reconnect attempts and resumes retrying when the network returns. Settings search finds existing options by name or category, and model settings follow the selected agent’s credentials and accepted configuration changes. Failed model refreshes show a warning while preserving choices and drafts, with another attempt available through Refresh chat.

> Android’s compact Model sheet keeps more of the conversation visible while distinguishing the space left in the current context from the latest run’s accumulated usage. Stale counters clear after compaction and history refresh, and optional model-call details remain available without treating unknown usage as zero.

> Persistent paired computers retain the current worker build between sessions, avoiding another installation when that build is already present. A new build still needs installation on first use. Android setup also saves replacement access before retiring setup credentials, so a newly supplied setup code keeps its intended meaning.

> Chrome relay tabs can also recover after attachment loss without restarting the browser stack. Opening an old browser result keeps a stopped managed browser stopped and offers Start browser when needed. Preview capture preserves focus for verified visible attached Chrome sessions on macOS and Linux, and screenshot annotations follow the actual image scale and crop.

> Remote desktop input sends supplementary Unicode characters as complete code points, avoiding split characters during typing and deletion. The keyboard stays disabled until connected control is ready.

> Failed cloud-tool results are recorded as failures before they enter conversation history. A failed desktop cleanup remains visible and can be retried before another desktop opens. OpenClaw keeps the resources needed to finish that cleanup, and blocks reopening while the previous desktop remains unresolved.

> Desktop viewing and control end when the requesting Gateway connection disconnects or loses authority. Connection-bound tickets and both relay directions are checked, while internal callers without a connection retain their existing timeout-based behavior.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
- [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-08 · ChatGPT · [[Changes/ChatGPT/2026-09-08-turn-a-sketch-into-an-image-on-mobile-type-in-the-message-box-and-select-sketch|Turn a sketch into an image]]
- Later: 2026-09-08 · Qoder · [[Changes/Qoder/2026-09-08-mobile-remote-control-once-enabled-you-can-use-your-phone-to-create-and-run-task|Mobile Remote Control]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-4104d1&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-4104d1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->