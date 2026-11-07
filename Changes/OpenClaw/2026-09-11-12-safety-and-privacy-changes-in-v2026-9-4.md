---
card_id: openclaw-2026-09-11-d334c0
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Safety and Privacy: 12 changes in v2026.9.4
  — Requests such as checking OpenClaw’s system status can work again from server
  messages…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2236
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b75dfed5ad33919b368077fef4c36da48a960a4b0ae83baa6ba4bcf84c5c52a3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-d334c0
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 12 Safety and Privacy changes'
  evidence:
  - quote: Requests such as checking OpenClaw’s system status can work again from
      server messages when you have permission, fixing a case where the request was
      refused despite the tool being available.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Replies from a resumed Google Chat conversation can use its saved destination
      correctly again. This fixes a case where changing capital letters in the destination
      caused a permission error, even though your Claw was allowed to send there.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When an automatic memory save lacks permission to write, the logs now name
      the file it could not save. They also explain more reasons why Active Memory
      skipped a search, making missing memories easier to investigate. These are clearer
      warnings, so a reported save problem still needs attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Android notification replies reconnect to the saved computer for that conversation
      when needed. The notification now tells you whether a reply is queued, failed,
      or has an unknown status. Queued confirms that the app saved your reply for
      sending; it does not confirm delivery. If the result is unknown, open the conversation
      before sending again. You may still need to approve a connection-security prompt
      before the reply can proceed.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Android setup also makes the selected security option available to accessibility
      tools. When your Claw checks a phone or Apple Watch battery, the result now
      includes a clear percentage, helping avoid confusion between a full charge and
      one percent.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: This release fixes computer-use errors that could stop your Claw before
      it had even found the right window. Supported desktop controls are available
      from the start, and bringing a window forward no longer looks like a failure
      when it worked. Your Claw still needs permission to use the computer, and the
      computer must support the controls it requests.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: You can read what a plugin does, check what it needs, and follow installation
      through to setup without leaving the browser. Plugin settings puts its configuration,
      permissions, and troubleshooting information together, with clearer messages
      when setup is unfinished. The install dialog stays with your latest choice and
      waits through the required restart before confirming completion. Installing
      or changing plugins still requires the appropriate permissions and your consent.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Owners and administrators can search Codex plugins , open their setup links,
      and see installation, permission, and account-connection information together.
      Opening a setup link does not finish the step—return and submit the completion
      response when you are done. After connecting, use /codex plugins refresh to
      update the app list, then /new or /reset where required; refreshing does not
      sign in or enable an app for you.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When an agent is limited to its workspace, it can now send files from the
      current chat's sandbox without being able to attach files from another chat's
      sandbox. Plugins that send these attachments must identify the correct workspace,
      so some third-party plugins may need an update.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you have read-only access, opening an MCP App in a separate view no
      longer gives you permission to run its tools. You can still view the App and
      use the resources you are allowed to read. For MCP tools running on the same
      computer, rejecting an oversized upload also stops a tool command queued behind
      it from running on that connection.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Backups and support bundles leave out recognized private update records.
      If you move a protected folder, keep its privacy-marker file with it. Files
      copied elsewhere without that marker are not protected from export.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Running openclaw security audit --fix now keeps the WhatsApp group access
      list you already chose, instead of adding people just because they had previously
      paired with your Claw. When changing an open group policy to restricted access,
      it can still use approved senders if you have not supplied a list. People added
      by an earlier repair are not removed automatically, so review your list if you
      were affected.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 12-safety-and-privacy-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 12 Safety and Privacy changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and
  Privacy changes in 1.17.1]]'
- '[[Changes/Windsurf/2026-09-10-devin-cloud|Devin Cloud]]'
- '[[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety
  and Privacy changes in v2.1.269]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 12 Safety and Privacy changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Safety and Privacy changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Requests such as checking OpenClaw’s system status can work again from server messages when you have permission, fixing a case where the request was refused despite the tool being available.

> Replies from a resumed Google Chat conversation can use its saved destination correctly again. This fixes a case where changing capital letters in the destination caused a permission error, even though your Claw was allowed to send there.

> When an automatic memory save lacks permission to write, the logs now name the file it could not save. They also explain more reasons why Active Memory skipped a search, making missing memories easier to investigate. These are clearer warnings, so a reported save problem still needs attention.

> Android notification replies reconnect to the saved computer for that conversation when needed. The notification now tells you whether a reply is queued, failed, or has an unknown status. Queued confirms that the app saved your reply for sending; it does not confirm delivery. If the result is unknown, open the conversation before sending again. You may still need to approve a connection-security prompt before the reply can proceed.

> Android setup also makes the selected security option available to accessibility tools. When your Claw checks a phone or Apple Watch battery, the result now includes a clear percentage, helping avoid confusion between a full charge and one percent.

> This release fixes computer-use errors that could stop your Claw before it had even found the right window. Supported desktop controls are available from the start, and bringing a window forward no longer looks like a failure when it worked. Your Claw still needs permission to use the computer, and the computer must support the controls it requests.

> You can read what a plugin does, check what it needs, and follow installation through to setup without leaving the browser. Plugin settings puts its configuration, permissions, and troubleshooting information together, with clearer messages when setup is unfinished. The install dialog stays with your latest choice and waits through the required restart before confirming completion. Installing or changing plugins still requires the appropriate permissions and your consent.

> Owners and administrators can search Codex plugins , open their setup links, and see installation, permission, and account-connection information together. Opening a setup link does not finish the step—return and submit the completion response when you are done. After connecting, use /codex plugins refresh to update the app list, then /new or /reset where required; refreshing does not sign in or enable an app for you.

> When an agent is limited to its workspace, it can now send files from the current chat's sandbox without being able to attach files from another chat's sandbox. Plugins that send these attachments must identify the correct workspace, so some third-party plugins may need an update.

> If you have read-only access, opening an MCP App in a separate view no longer gives you permission to run its tools. You can still view the App and use the resources you are allowed to read. For MCP tools running on the same computer, rejecting an oversized upload also stops a tool command queued behind it from running on that connection.

> Backups and support bundles leave out recognized private update records. If you move a protected folder, keep its privacy-marker file with it. Files copied elsewhere without that marker are not protected from export.

> Running openclaw security audit --fix now keeps the WhatsApp group access list you already chose, instead of adding people just because they had previously paired with your Claw. When changing an open group policy to restricted access, it can still use approved senders if you have not supplied a list. People added by an earlier repair are not removed automatically, so review your list if you were affected.

Source: https://docs.openclaw.ai/releases/2026.9.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-11-messages-arriving-while-openclaw-is-paused-now-wait-until-it-is-ready-again-and|Messages arriving while OpenClaw is paused now wait until it is ready again…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-11-images-you-send-stay-visible-while-the-conversation-updates-and-scrolling-back-t|Images you send stay visible while the conversation updates, and scrolling back…]] · Files and Data
- [[Changes/OpenClaw/2026-09-11-7-automation-and-scheduling-changes-in-v2026-9-4|7 Automation and Scheduling changes in v2026.9.4]] · Automation and Scheduling
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
## Nearby in Safety and Privacy

- Earlier: 2026-09-11 · Claude Code · [[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety and Privacy changes in v2.1.269]]
- Later: 2026-09-11 · Raycast · [[Changes/Raycast/2026-09-11-ai-tool-confirmations-now-default-to-auto-so-sessions-no-longer-ask-for-permissi|AI : Tool confirmations now default to Auto, so sessions no longer ask…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-d334c0&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-12-safety-and-privacy-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-d334c0%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->