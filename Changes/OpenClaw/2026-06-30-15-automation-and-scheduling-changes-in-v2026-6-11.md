---
card_id: openclaw-2026-06-30-9eb5e4
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Automation and Scheduling: 15 changes in v2026.6.11
  — Telegram forum-topic cron jobs now keep separately configured failure alerts…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2477
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d65cc5c36d9c2641a214e1d8e932264ad21c9c041d409aeb0ca7daeae7c011ba
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-9eb5e4
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 15 Automation and Scheduling changes'
  evidence:
  - quote: 'Telegram forum-topic cron jobs now keep separately configured failure
      alerts going to their intended destination, even when the main announcement
      uses a topic in the same chat. #95794 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'First-run setup now opens the credential prompt for a newly installed
      external provider instead of appearing to loop and leaving OpenAI selected.
      #95792 Related #95765 .'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Agent replies and scheduled cron runs now handle fast-mode fallback retries
      more reliably, keeping the state needed for the final attempt to finish or report
      progress correctly. 14e448e Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Plugin Gateway methods now work through openclaw gateway call after registration,
      so plugin authors can use them from scripts and cron jobs instead of hitting
      an unknown method error. #94154 Related #94127 . Thanks @brycemurray, @pick-cat,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Channel capability checks now return a clear timeout when an integration
      stops responding, keeping troubleshooting from hanging in a terminal or automation
      run. 8ecdb97 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Gateway-launched agents no longer lose owner-only OpenClaw tools during
      tasks such as live cron checks, so authorized operations can use the intended
      tools with the correct request context. c2ee9b0 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'The Control UI Overview now counts and flags only enabled cron jobs that
      still need attention, while disabled jobs retain their past failure details
      without appearing as current problems. #95723 Related #95716 . Thanks @voytas75,
      @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenClaw Doctor now gives accurate guidance for working isolated shell-prompt
      cron jobs instead of repeatedly suggesting a --fix command that cannot clear
      the warning. #94784 Related #94655 . Thanks @altaywtf, @geekoagent, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows daemon recovery is less likely to miss process detection or cleanup
      when PATH is incomplete, unusual, or shadowed because scheduled-task fallback
      now finds PowerShell and taskkill in trusted system locations. 2a140e6 Thanks
      @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Isolated cron jobs using deleteAfterRun now remove their temporary session
      and transcript after finishing, including runs with delivery disabled, reducing
      stale files, accumulated context, and manual cleanup. #84794 Related #84707
      . Thanks @bottenbenny, @turbotheturtle.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Cron history now reliably finds entries whose job IDs include extra surrounding
      spaces, and rejects nested or blank IDs before they can create log records that
      cannot be read back safely. #93567 Thanks @alix-007, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Adding or removing a cron job no longer causes another recurring job that
      is already due to lose its pending run. #94323 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Browser automation users keep the same reference-rich snapshots, including
      useful branches in compact results, with less avoidable processing during snapshot
      generation. #96072 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Commands given extremely large timeout settings now use a safe maximum
      instead of failing because the runtime cannot schedule the requested wait. 66b94ba
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Improves release-check automation and required evidence handling. #95094
      , #95466 , #95876 , #95880 , #95919 , #95928 , #95991 , #96235 Thanks @romneyda,
      @jason-allen-oneal, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-automation-and-scheduling-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 15 Automation and Scheduling changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-06-26-add-a-hint-to-the-per-turn-step-limit-error-pointing-users-to-the-loop-control-m|Add
  a hint to the per-turn step limit error pointing users…]]'
- '[[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6
  Automation and Scheduling changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr
  auto now starts a self-paced loop that fixes one thing per run and paces itself…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 15 Automation and Scheduling changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Automation and Scheduling changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Telegram forum-topic cron jobs now keep separately configured failure alerts going to their intended destination, even when the main announcement uses a topic in the same chat. #95794 Thanks @vincentkoc.

> First-run setup now opens the credential prompt for a newly installed external provider instead of appearing to loop and leaving OpenAI selected. #95792 Related #95765 .

> Agent replies and scheduled cron runs now handle fast-mode fallback retries more reliably, keeping the state needed for the final attempt to finish or report progress correctly. 14e448e Thanks @vincentkoc.

> Plugin Gateway methods now work through openclaw gateway call after registration, so plugin authors can use them from scripts and cron jobs instead of hitting an unknown method error. #94154 Related #94127 . Thanks @brycemurray, @pick-cat, @vincentkoc.

> Channel capability checks now return a clear timeout when an integration stops responding, keeping troubleshooting from hanging in a terminal or automation run. 8ecdb97 Thanks @vincentkoc.

> Gateway-launched agents no longer lose owner-only OpenClaw tools during tasks such as live cron checks, so authorized operations can use the intended tools with the correct request context. c2ee9b0 Thanks @vincentkoc.

> The Control UI Overview now counts and flags only enabled cron jobs that still need attention, while disabled jobs retain their past failure details without appearing as current problems. #95723 Related #95716 . Thanks @voytas75, @zengwen-dt.

> OpenClaw Doctor now gives accurate guidance for working isolated shell-prompt cron jobs instead of repeatedly suggesting a --fix command that cannot clear the warning. #94784 Related #94655 . Thanks @altaywtf, @geekoagent, @zengwen-dt.

> Windows daemon recovery is less likely to miss process detection or cleanup when PATH is incomplete, unusual, or shadowed because scheduled-task fallback now finds PowerShell and taskkill in trusted system locations. 2a140e6 Thanks @vincentkoc.

> Isolated cron jobs using deleteAfterRun now remove their temporary session and transcript after finishing, including runs with delivery disabled, reducing stale files, accumulated context, and manual cleanup. #84794 Related #84707 . Thanks @bottenbenny, @turbotheturtle.

> Cron history now reliably finds entries whose job IDs include extra surrounding spaces, and rejects nested or blank IDs before they can create log records that cannot be read back safely. #93567 Thanks @alix-007, @vincentkoc.

> Adding or removing a cron job no longer causes another recurring job that is already due to lose its pending run. #94323 Thanks @yetval.

> Browser automation users keep the same reference-rich snapshots, including useful branches in compact results, with less avoidable processing during snapshot generation. #96072 Thanks @vincentkoc.

> Commands given extremely large timeout settings now use a safe maximum instead of failing because the runtime cannot schedule the requested wait. 66b94ba

> Improves release-check automation and required evidence handling. #95094 , #95466 , #95876 , #95880 , #95919 , #95928 , #95991 , #96235 Thanks @romneyda, @jason-allen-oneal, @vincentkoc.

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
## Nearby in Automation and Scheduling

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr auto now starts a self-paced loop that fixes one thing per run and paces itself…]]
- Later: 2026-07-01 · Open WebUI · [[Changes/Open WebUI/2026-07-01-models-with-null-capabilities-chatting-with-a-model-whose-capabilities-are-unset|🤖 Models with null capabilities. Chatting with a model whose capabilities…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-9eb5e4&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-15-automation-and-scheduling-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-9eb5e4%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->