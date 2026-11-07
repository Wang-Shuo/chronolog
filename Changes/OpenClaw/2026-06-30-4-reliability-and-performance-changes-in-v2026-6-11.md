---
card_id: openclaw-2026-06-30-85ea5f
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Reliability and Performance: 4 changes in v2026.6.11
  — Codex runs now follow the current fast-mode choice instead of carrying over an…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening
    Projects is now much faster]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2780
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ff0ae3bbe73dfa616abdf16a0d70e9c0c0de1695228487125c2b60aca663d62b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-85ea5f
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 4 Reliability and Performance changes'
  evidence:
  - quote: Codex runs now follow the current fast-mode choice instead of carrying
      over an old speed tier, and the status line clearly shows when fast mode is
      automatic. 77012f9 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Fast-mode runs now keep their speed setting through model fallback retries
      and show the configured automatic threshold in status, avoiding inconsistent
      retry behavior and an unhelpful generic label. aa3797c Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When Linux memory pressure kills a child command or session, systemd-managed
      OpenClaw gateways now stay running and keep channel connections alive while
      reporting the child failure. #93585 Thanks @snowzlm.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'People inspecting very large or out-of-order sessions can open usage details
      and still get the latest timestamped log entries without OpenClaw retaining
      the entire parsed log history in memory. #96019 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-reliability-and-performance-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: reliability-performance
  title: 4 Reliability and Performance changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-30-perform-tokenizer-warmup-in-parallel-on-a-background-thread-for-better-startup-p|Perform
  tokenizer warmup in parallel on a background thread for better startup performance]]'
- '[[Changes/Lovable/2026-06-30-faster-ai-responses-in-your-app-with-openai-priority-processing|Faster
  AI responses in your app with OpenAI priority processing]]'
- '[[Changes/Ollama/2026-06-30-2-reliability-and-performance-changes-in-v0-31-1|2
  Reliability and Performance changes in v0.31.1]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: reliability-performance
title: 4 Reliability and Performance changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Reliability and Performance changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Codex runs now follow the current fast-mode choice instead of carrying over an old speed tier, and the status line clearly shows when fast mode is automatic. 77012f9 Thanks @vincentkoc.

> Fast-mode runs now keep their speed setting through model fallback retries and show the configured automatic threshold in status, avoiding inconsistent retry behavior and an unhelpful generic label. aa3797c Thanks @vincentkoc.

> When Linux memory pressure kills a child command or session, systemd-managed OpenClaw gateways now stay running and keep channel connections alive while reporting the child failure. #93585 Thanks @snowzlm.

> People inspecting very large or out-of-order sessions can open usage details and still get the latest timestamped log entries without OpenClaw retaining the entire parsed log history in memory. #96019 Thanks @vincentkoc.

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
- [[Changes/OpenClaw/2026-06-30-32-model-support-changes-in-v2026-6-11|32 Model Support changes in v2026.6.11]] · Model Support
- [[Changes/OpenClaw/2026-06-30-qqbot-group-admins-can-choose-how-broadly-slash-commands-are-available-and-priva|QQBot group admins can choose how broadly slash commands are available…]] · Enterprise and Administration
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
## Nearby in Reliability and Performance

- Earlier: 2026-06-30 · Ollama · [[Changes/Ollama/2026-06-30-2-reliability-and-performance-changes-in-v0-31-1|2 Reliability and Performance changes in v0.31.1]]
- Later: 2026-07-01 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-07-01-ai-generated-survey-insights-with-copilot-highlights-web-viva-glint|AI-generated survey insights with Copilot Highlights Web (Viva Glint)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-19 · Descript · [[Changes/Descript/2018-11-19-opening-projects-is-now-much-faster|Opening Projects is now much faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-85ea5f&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-85ea5f%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->