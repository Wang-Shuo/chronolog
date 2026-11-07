---
card_id: openclaw-2026-09-11-1748f6
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Automation and Scheduling: 7 changes in v2026.9.4
  — Automations are easier to manage, with direct links to edit them and names you
  can…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 983
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3115b85b681a87e051a65d652937272f64d012f6008df5935681c59019bfec5b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-1748f6
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 7 Automation and Scheduling changes'
  evidence:
  - quote: Automations are easier to manage, with direct links to edit them and names
      you can recognize. Scheduled tasks also get fixes for getting stuck, returning
      results to your chat, and staying quiet when there is nothing to report.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: A clash between scheduled tasks could make OpenClaw keep retrying until
      it stopped responding. That loop is fixed. Tasks that hand work to another agent
      also avoid a pause they could never resume, leaving OpenClaw to deliver the
      result through the task's existing settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If an automation result is waiting while your Claw answers you, canceling
      that result can now unblock actions such as pinning the conversation. Your Claw
      can finish its reply without adding the canceled result to the chat.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: You can jump straight to an automation's editor from Settings → Agents
      → Automations, even when the task is paused. Lists now show the friendly names
      you saved, and you can group scheduled conversations together so they are easier
      to find. Large automation lists also spend less time loading where results will
      be sent.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you manage automations from the command line, missing jobs and invalid
      options come with more useful guidance. Warnings also explain what to check
      when a saved task cannot run because scheduling is turned off.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Cancelling cannot undo changes already made to a page. If you automate
      browser commands, check their reported results before continuing, because a
      blocked task does not always return an error status.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: The FAQ is organized around the question you are trying to answer, and
      the documentation home gives you direct paths to releases, skills, automations,
      and building plugins. Setup examples are clearer, and repairs to older bookmarks
      and help links make the relevant instructions easier to reach. Simplified Chinese
      navigation also gains translated labels, including separate Releases and Contributing
      tabs.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 7-automation-and-scheduling-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 7 Automation and Scheduling changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7
  Automation and Scheduling changes in v2026.9.3]]'
- '[[Changes/OpenHands/2026-09-09-9-automation-and-scheduling-changes-in-v1-17-0|9
  Automation and Scheduling changes in v1.17.0]]'
- '[[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation
  and Scheduling changes in 1.17.1]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 7 Automation and Scheduling changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Automation and Scheduling changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Automations are easier to manage, with direct links to edit them and names you can recognize. Scheduled tasks also get fixes for getting stuck, returning results to your chat, and staying quiet when there is nothing to report.

> A clash between scheduled tasks could make OpenClaw keep retrying until it stopped responding. That loop is fixed. Tasks that hand work to another agent also avoid a pause they could never resume, leaving OpenClaw to deliver the result through the task's existing settings.

> If an automation result is waiting while your Claw answers you, canceling that result can now unblock actions such as pinning the conversation. Your Claw can finish its reply without adding the canceled result to the chat.

> You can jump straight to an automation's editor from Settings → Agents → Automations, even when the task is paused. Lists now show the friendly names you saved, and you can group scheduled conversations together so they are easier to find. Large automation lists also spend less time loading where results will be sent.

> If you manage automations from the command line, missing jobs and invalid options come with more useful guidance. Warnings also explain what to check when a saved task cannot run because scheduling is turned off.

> Cancelling cannot undo changes already made to a page. If you automate browser commands, check their reported results before continuing, because a blocked task does not always return an error status.

> The FAQ is organized around the question you are trying to answer, and the documentation home gives you direct paths to releases, skills, automations, and building plugins. Setup examples are clearer, and repairs to older bookmarks and help links make the relevant instructions easier to reach. Simplified Chinese navigation also gains translated labels, including separate Releases and Contributing tabs.

Source: https://docs.openclaw.ai/releases/2026.9.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-11-messages-arriving-while-openclaw-is-paused-now-wait-until-it-is-ready-again-and|Messages arriving while OpenClaw is paused now wait until it is ready again…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-11-images-you-send-stay-visible-while-the-conversation-updates-and-scrolling-back-t|Images you send stay visible while the conversation updates, and scrolling back…]] · Files and Data
- [[Changes/OpenClaw/2026-09-11-with-diagnostic-recording-enabled-openrouter-can-return-finished-music-or-a-usag|With diagnostic recording enabled, OpenRouter can return finished music…]] · Music Generation
- [[Changes/OpenClaw/2026-09-11-18-developer-workflow-changes-in-v2026-9-4|18 Developer Workflow changes in v2026.9.4]] · Developer Workflow
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
## Nearby in Automation and Scheduling

- Earlier: 2026-09-10 · Dify · [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]]
- Later: 2026-09-11 · OpenHands · [[Changes/OpenHands/2026-09-11-3-automation-and-scheduling-changes-in-v1-18-0|3 Automation and Scheduling changes in v1.18.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-1748f6&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-7-automation-and-scheduling-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-1748f6%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->