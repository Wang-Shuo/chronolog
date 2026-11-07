---
card_id: openclaw-2026-09-11-2c948b
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Developer Workflow: 18 changes in v2026.9.4
  — If the background service is still using an old Node after an upgrade, openclaw
  gateway…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2922
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4455d51741ca88fb185bd503aa96dd57a7f71754d871de83f5316fd67e03b6f2
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-2c948b
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 18 Developer Workflow changes'
  evidence:
  - quote: If the background service is still using an old Node after an upgrade,
      openclaw gateway install can now switch it to an available supported version.
      This is a separate repair from getting the command line working.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Removing OpenClaw now comes with instructions that match how you installed
      it, including Git and installations kept in their own folder. The uninstall
      guide explains which files and launchers to remove and which may be shared with
      other tools. Remove the background service first, and save any settings or workspaces
      you want to keep before deleting files.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When you use Claude Code, Codex, OpenCode, or Pi in a terminal on a paired
      computer, choosing or dropping a file now puts its location into the terminal
      for you to use. You can edit it before pressing Enter. Reloading while several
      terminal tabs are reconnecting also keeps tabs that previously disappeared from
      the list.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If uploads remain blocked after a crash, follow the terminal recovery steps
      . Stop all OpenClaw host processes sharing the upload folder on the computer
      running that terminal before removing the lock named in the error.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Updates from recent stable releases can get past failures that prevented
      them from finishing or left OpenClaw stopped afterward. Updating from the browser
      also gets a startup fix, and active conversations are less likely to hold up
      an update. Some fixes only help after the newer updater is installed, so if
      your current version is stuck, follow the update guidance rather than repeatedly
      trying the same failing command.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you run OpenClaw from a Git checkout, updates can recover when an upstream
      release tag changes, and Windows gets a fix for updates failing before they
      begin. Status now warns when a failed update check left its information out
      of date. That warning clears after the updater next fetches successfully. If
      your checkout has several possible update sources, the development-channel guide
      explains how to choose one.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If another tool manages your OpenClaw settings, a new read-only configuration
      option keeps OpenClaw from overwriting them, including during automatic recovery.
      Set OPENCLAW_CONFIG_READONLY=1 for both the running service and terminal commands.
      Conversations and other working data still need somewhere writable, and model
      changes can apply to the current session without changing the saved default.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Matrix keeps message text that could previously be mistaken for an attachment
      and disappear from quoted replies or conversation history. A mention marked
      as plain text also stays plain when earlier code formatting is unfinished. In
      the terminal, reaction lists show which emoji people used instead of leaving
      the label blank.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you prepare Mac setup from the command line, you can now read a password
      or token from a private file without putting it in the command itself. Setup
      also respects the profile you chose instead of changing the default profile.
      The remote setup guide explains these options and the separate command to use
      when the app is already running.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you run openclaw models status --probe directly from the terminal, stop
      the Gateway first and wait for the command to exit before starting it again.
      The result can appear while the check is still closing its files and connections.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Guidance is easier to find when you want to start a task at a set time
      or when a command finishes , or set up an automatic response to an event with
      a hook . These guides explain existing features, with clearer instructions for
      choosing and setting them up.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When a website pop-up stops a browser command , OpenClaw tells you which
      prompt needs an answer and which steps remain unfinished. Answering one pop-up
      also no longer prevents the next one from being answered. Longer tasks in an
      already open browser avoid the premature connection failures covered by these
      fixes.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Commands on connected devices no longer time out early or wait longer just
      because the system clock changed. Time spent waking the device counts toward
      the same limit as running the command. If you use scripts, omit numeric options
      when you want their defaults—passing an empty value now gives a clear error
      before OpenClaw contacts the device.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When your Claw needs an answer, you can now choose an option or type a
      response directly in the terminal , including while a task is waiting for your
      reply. Press Esc to put the question aside and /question to bring it back.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Secret requests get a masked entry box that keeps what you type out of
      the conversation and input history. Saving a secret requires a Gateway connection,
      and terminal entry accepts one line at a time. Use the web app if you need to
      change which sites can use it. Local sessions support ordinary questions, which
      you should answer before closing the terminal.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Long addresses and other text now wrap in terminal chat without gaining
      extra spaces, so you can copy them as written. Tables keep related values lined
      up, and progress indicators stop leaving repeated lines behind in narrow windows.
      If you use scripts to read command results, approvals JSON and transcript output
      also keep the unrelated announcements out of the way.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Code Mode uses less of its result space for formatting, leaving more room
      for the information your Claw asked for. The terminal also shows that data as
      written, without treating parts of it as message formatting. Code that calls
      itself too deeply now returns an error the Claw can work from, making it possible
      to correct that code and continue.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: A worktree gives your Claw a separate working copy of a code project. Setup
      retries now keep the version you originally selected, and projects with many
      branches keep the option to start a worktree available. You can type a branch
      or commit that is missing from the suggestions, with an error if it cannot be
      found.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 18-developer-workflow-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: developer-workflow
  title: 18 Developer Workflow changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow
  changes in 1.17.1]]'
- '[[Changes/Claude Code/2026-09-11-added-otel-metrics-include-repository-to-tag-opentelemetry-metrics-and-events-wi|Added
  OTEL_METRICS_INCLUDE_REPOSITORY to tag OpenTelemetry metrics and events…]]'
- '[[Changes/Devin/2026-09-11-azure-devops-citations|Azure DevOps Citations]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: developer-workflow
title: 18 Developer Workflow changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Developer Workflow changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> If the background service is still using an old Node after an upgrade, openclaw gateway install can now switch it to an available supported version. This is a separate repair from getting the command line working.

> Removing OpenClaw now comes with instructions that match how you installed it, including Git and installations kept in their own folder. The uninstall guide explains which files and launchers to remove and which may be shared with other tools. Remove the background service first, and save any settings or workspaces you want to keep before deleting files.

> When you use Claude Code, Codex, OpenCode, or Pi in a terminal on a paired computer, choosing or dropping a file now puts its location into the terminal for you to use. You can edit it before pressing Enter. Reloading while several terminal tabs are reconnecting also keeps tabs that previously disappeared from the list.

> If uploads remain blocked after a crash, follow the terminal recovery steps . Stop all OpenClaw host processes sharing the upload folder on the computer running that terminal before removing the lock named in the error.

> Updates from recent stable releases can get past failures that prevented them from finishing or left OpenClaw stopped afterward. Updating from the browser also gets a startup fix, and active conversations are less likely to hold up an update. Some fixes only help after the newer updater is installed, so if your current version is stuck, follow the update guidance rather than repeatedly trying the same failing command.

> If you run OpenClaw from a Git checkout, updates can recover when an upstream release tag changes, and Windows gets a fix for updates failing before they begin. Status now warns when a failed update check left its information out of date. That warning clears after the updater next fetches successfully. If your checkout has several possible update sources, the development-channel guide explains how to choose one.

> If another tool manages your OpenClaw settings, a new read-only configuration option keeps OpenClaw from overwriting them, including during automatic recovery. Set OPENCLAW_CONFIG_READONLY=1 for both the running service and terminal commands. Conversations and other working data still need somewhere writable, and model changes can apply to the current session without changing the saved default.

> Matrix keeps message text that could previously be mistaken for an attachment and disappear from quoted replies or conversation history. A mention marked as plain text also stays plain when earlier code formatting is unfinished. In the terminal, reaction lists show which emoji people used instead of leaving the label blank.

> If you prepare Mac setup from the command line, you can now read a password or token from a private file without putting it in the command itself. Setup also respects the profile you chose instead of changing the default profile. The remote setup guide explains these options and the separate command to use when the app is already running.

> If you run openclaw models status --probe directly from the terminal, stop the Gateway first and wait for the command to exit before starting it again. The result can appear while the check is still closing its files and connections.

> Guidance is easier to find when you want to start a task at a set time or when a command finishes , or set up an automatic response to an event with a hook . These guides explain existing features, with clearer instructions for choosing and setting them up.

> When a website pop-up stops a browser command , OpenClaw tells you which prompt needs an answer and which steps remain unfinished. Answering one pop-up also no longer prevents the next one from being answered. Longer tasks in an already open browser avoid the premature connection failures covered by these fixes.

> Commands on connected devices no longer time out early or wait longer just because the system clock changed. Time spent waking the device counts toward the same limit as running the command. If you use scripts, omit numeric options when you want their defaults—passing an empty value now gives a clear error before OpenClaw contacts the device.

> When your Claw needs an answer, you can now choose an option or type a response directly in the terminal , including while a task is waiting for your reply. Press Esc to put the question aside and /question to bring it back.

> Secret requests get a masked entry box that keeps what you type out of the conversation and input history. Saving a secret requires a Gateway connection, and terminal entry accepts one line at a time. Use the web app if you need to change which sites can use it. Local sessions support ordinary questions, which you should answer before closing the terminal.

> Long addresses and other text now wrap in terminal chat without gaining extra spaces, so you can copy them as written. Tables keep related values lined up, and progress indicators stop leaving repeated lines behind in narrow windows. If you use scripts to read command results, approvals JSON and transcript output also keep the unrelated announcements out of the way.

> Code Mode uses less of its result space for formatting, leaving more room for the information your Claw asked for. The terminal also shows that data as written, without treating parts of it as message formatting. Code that calls itself too deeply now returns an error the Claw can work from, making it possible to correct that code and continue.

> A worktree gives your Claw a separate working copy of a code project. Setup retries now keep the version you originally selected, and projects with many branches keep the option to start a worktree available. You can type a branch or commit that is missing from the suggestions, with an error if it cannot be found.

Source: https://docs.openclaw.ai/releases/2026.9.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-11-messages-arriving-while-openclaw-is-paused-now-wait-until-it-is-ready-again-and|Messages arriving while OpenClaw is paused now wait until it is ready again…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-11-images-you-send-stay-visible-while-the-conversation-updates-and-scrolling-back-t|Images you send stay visible while the conversation updates, and scrolling back…]] · Files and Data
- [[Changes/OpenClaw/2026-09-11-7-automation-and-scheduling-changes-in-v2026-9-4|7 Automation and Scheduling changes in v2026.9.4]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-11-with-diagnostic-recording-enabled-openrouter-can-return-finished-music-or-a-usag|With diagnostic recording enabled, OpenRouter can return finished music…]] · Music Generation
- [[Changes/OpenClaw/2026-09-11-2-reliability-and-performance-changes-in-v2026-9-4|2 Reliability and Performance changes in v2026.9.4]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-11-16-mobile-and-desktop-changes-in-v2026-9-4|16 Mobile and Desktop changes in v2026.9.4]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-the-bundled-video-frames-skill-and-its-helper-script-have-been-removed-if-you-us|The bundled video-frames skill and its helper script have been removed]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-11-5-interface-experience-changes-in-v2026-9-4|5 Interface Experience changes in v2026.9.4]] · Interface Experience
- [[Changes/OpenClaw/2026-09-11-14-memory-and-personalization-changes-in-v2026-9-4|14 Memory and Personalization changes in v2026.9.4]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-11-you-can-now-answer-your-claw-s-questions-and-enter-secrets-from-the-terminal-wit|Answer your Claw’s questions and enter secrets from the terminal, with clearer…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-11-2-image-generation-changes-in-v2026-9-4|2 Image Generation changes in v2026.9.4]] · Image Generation
- [[Changes/OpenClaw/2026-09-11-3-pricing-model-changes-in-v2026-9-4|3 Pricing Model changes in v2026.9.4]] · Pricing Model
- [[Changes/OpenClaw/2026-09-11-you-can-now-reach-the-official-app-store-listing-straight-from-the-iphone-setup|Reach the official App Store listing straight from the iPhone setup guide]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-5-editor-experience-changes-in-v2026-9-4|5 Editor Experience changes in v2026.9.4]] · Editor Experience
- [[Changes/OpenClaw/2026-09-11-you-can-now-choose-deepgram-flux-to-turn-incoming-voice-notes-into-text-your-cla|Choose Deepgram Flux to turn incoming voice notes into text your Claw can use…]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-8-voice-and-audio-changes-in-v2026-9-4|8 Voice and Audio changes in v2026.9.4]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-12-safety-and-privacy-changes-in-v2026-9-4|12 Safety and Privacy changes in v2026.9.4]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-11-22-apps-and-integrations-changes-in-v2026-9-4|22 Apps and Integrations changes in v2026.9.4]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-20-model-support-changes-in-v2026-9-4|20 Model Support changes in v2026.9.4]] · Model Support
- [[Changes/OpenClaw/2026-09-11-14-account-and-access-changes-in-v2026-9-4|14 Account and Access changes in v2026.9.4]] · Account and Access
- [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an|Search installed and available plugins together, browse by purpose, and keep…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-3-search-and-browsing-changes-in-v2026-9-4|3 Search and Browsing changes in v2026.9.4]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-11-you-can-now-enable-desktop-access-for-azure-cloud-workers-whether-openclaw-manag|Enable desktop access for Azure cloud workers , whether OpenClaw manages them…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-3-collaboration-changes-in-v2026-9-4|3 Collaboration changes in v2026.9.4]] · Collaboration
- [[Changes/OpenClaw/2026-09-11-25-agent-mode-changes-in-v2026-9-4|25 Agent Mode changes in v2026.9.4]] · Agent Mode
- [[Changes/OpenClaw/2026-09-11-2-context-window-changes-in-v2026-9-4|2 Context Window changes in v2026.9.4]] · Context Window
- [[Changes/OpenClaw/2026-09-11-56-other-changes-in-v2026-9-4|56 other changes in v2026.9.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-11 · Devin · [[Changes/Devin/2026-09-11-azure-devops-citations|Azure DevOps Citations]]
- Later: 2026-09-12 · Qoder · [[Changes/Qoder/2026-09-12-file-review-reduced-cpu-usage-when-multiple-code-diffs-are-expanded-alongside-an|File review: Reduced CPU usage when multiple code diffs are expanded alongside…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-2c948b&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-18-developer-workflow-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-2c948b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->