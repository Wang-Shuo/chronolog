---
card_id: openclaw-2026-06-30-c27b30
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Developer Workflow: 9 changes in v2026.6.11
  — iMessage command-and-link messages now stay together as one OpenClaw turn when
  delayed…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2849
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5e4b2c2a785305b444cb7c93afe4f3e951119997cfa0684638471dfca182997a
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-c27b30
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 9 Developer Workflow changes'
  evidence:
  - quote: 'iMessage command-and-link messages now stay together as one OpenClaw turn
      when delayed link previews arrive, while unrelated quick messages remain separate
      for users who enabled same-sender DM coalescing. #93143 Thanks @omarshahine.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Git-based OpenClaw installs now use the repository's pinned pnpm version
      even when another global pnpm or surrounding project package manager is present,
      so setup commands no longer run against the wrong package-manager environment.
      bd74a62 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows users can complete source installs without a llama.cpp setup step
      blocking or slowing them, and the installer restores their existing shell setting
      afterward. ea9065b Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows ARM64 users now get matching ARM64 Node and MinGit downloads when
      running the PowerShell installer through an x64-emulated shell. fac091b Thanks
      @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows gateway cleanup and listener checks now handle UTF-16 WMIC command-line
      data consistently, reducing failed or conflicting identification of the running
      gateway process. 15c880a Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: WebChat and the Control UI keep active conversations and failure states
      visible more consistently after reconnects, while mobile clients and the terminal
      UI recover completed, rejected, or interrupted sends without leaving them looking
      stuck.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows port diagnostics now use the intended system tools even when PATH
      entries are missing or shadowed, so gateway and service port conflicts are less
      likely to be obscured by command-resolution failures. c4facb2 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows-targeted Crabbox workflows are less likely to fail or fall back
      to slower shell handling when launching Node tools through .cmd and .bat shims.
      d48dcc6 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows users can run crabbox , git , and other Node-backed tools through
      npm-installed command shims without Crabbox stopping before the tool opens.
      77f4e45 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-developer-workflow-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: developer-workflow
  title: 9 Developer Workflow changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-29-2-developer-workflow-changes-in-v2-1-196|2 Developer
  Workflow changes in v2.1.196]]'
- '[[Changes/Open WebUI/2026-06-29-42-developer-workflow-changes-in-v0-10-0|42 Developer
  Workflow changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21
  Developer Workflow changes in v1.0.66]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: developer-workflow
title: 9 Developer Workflow changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Developer Workflow changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> iMessage command-and-link messages now stay together as one OpenClaw turn when delayed link previews arrive, while unrelated quick messages remain separate for users who enabled same-sender DM coalescing. #93143 Thanks @omarshahine.

> Git-based OpenClaw installs now use the repository's pinned pnpm version even when another global pnpm or surrounding project package manager is present, so setup commands no longer run against the wrong package-manager environment. bd74a62 Thanks @vincentkoc.

> Windows users can complete source installs without a llama.cpp setup step blocking or slowing them, and the installer restores their existing shell setting afterward. ea9065b Thanks @vincentkoc.

> Windows ARM64 users now get matching ARM64 Node and MinGit downloads when running the PowerShell installer through an x64-emulated shell. fac091b Thanks @vincentkoc.

> Windows gateway cleanup and listener checks now handle UTF-16 WMIC command-line data consistently, reducing failed or conflicting identification of the running gateway process. 15c880a Thanks @vincentkoc.

> WebChat and the Control UI keep active conversations and failure states visible more consistently after reconnects, while mobile clients and the terminal UI recover completed, rejected, or interrupted sends without leaving them looking stuck.

> Windows port diagnostics now use the intended system tools even when PATH entries are missing or shadowed, so gateway and service port conflicts are less likely to be obscured by command-resolution failures. c4facb2 Thanks @vincentkoc.

> Windows-targeted Crabbox workflows are less likely to fail or fall back to slower shell handling when launching Node tools through .cmd and .bat shims. d48dcc6 Thanks @vincentkoc.

> Windows users can run crabbox , git , and other Node-backed tools through npm-installed command shims without Crabbox stopping before the tool opens. 77f4e45 Thanks @vincentkoc.

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
- [[Changes/OpenClaw/2026-06-30-4-reliability-and-performance-changes-in-v2026-6-11|4 Reliability and Performance changes in v2026.6.11]] · Reliability and Performance
- [[Changes/OpenClaw/2026-06-30-3-interface-experience-changes-in-v2026-6-11|3 Interface Experience changes in v2026.6.11]] · Interface Experience
- [[Changes/OpenClaw/2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11|15 Automation and Scheduling changes in v2026.6.11]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-06-30-when-a-codex-subscription-reaches-its-usage-limit-openclaw-now-moves-to-configur|When a Codex subscription reaches its usage limit, OpenClaw now moves to configured…]] · Pricing Model
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21 Developer Workflow changes in v1.0.66]]
- Later: 2026-06-30 · OpenCode · [[Changes/OpenCode/2026-06-30-2-developer-workflow-changes-in-v1-17-12|2 Developer Workflow changes in v1.17.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-c27b30&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-9-developer-workflow-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-c27b30%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->