---
card_id: openclaw-2026-09-11-d887fd
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Account and Access: 14 changes in v2026.9.4
  — A new agent can now use an API key you have already saved in OpenClaw''s protected…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1261
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d7f2492efbda5a4859c664d977b0d856e736e559d20f1ef5896dcf9b344c0d82
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-d887fd
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 14 Account and Access changes'
  evidence:
  - quote: A new agent can now use an API key you have already saved in OpenClaw's
      protected storage, fixing a setup failure that left ordinary chats working but
      new-agent setup stuck. Moonshot's China API-key setup also stops asking you
      to reinstall a provider that is already installed, and browser sign-in explains
      when you have pasted a phone setup code into the wrong place.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Phone setup help now points you to openclaw qr , and the Android instructions
      explain how to connect to the computer running OpenClaw and set up the login
      your phone needs. They cover both a trusted home network and Tailscale. Use
      HTTPS for browser access when possible, because HTTP does not encrypt your login
      details or messages.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When you reload the app, it can show a saved copy of your conversation
      and sidebar while it reconnects, so you have something to read during the wait.
      This works with remembered Gateway tokens or paired-device sign-ins ; other
      sign-in methods still show the connection screen. Sending messages and other
      actions wait for the connection.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: An old “update in progress” message can stop blocking settings changes
      and account sign-in even when the update itself is no longer running. openclaw
      update repair can clear eligible stuck updates once it confirms the updater
      has stopped and OpenClaw is working. Some older requests that never got started
      clear automatically after a day, provided nothing still needs recovery. They
      remain in history as failed attempts, with guidance to retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: For Mattermost setups that store login tokens separately from account settings,
      editing one account no longer unnecessarily reconnects the others; settings
      shared by all accounts can still restart them together. A replacement progress
      message also stays visible while the old one is being removed, even when both
      contain the same plan.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If a Tlon message cannot send because setup is incomplete, the error now
      tells you which account needs attention and which settings are missing. You
      can go straight to the relevant part of Tlon setup without guessing, and the
      error does not reveal your login code.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Supported OpenAI sign-in methods can reuse an account or key already saved
      by Codex, saving you another login or paste. Agents sharing a sign-in also handle
      renewal more reliably, and a renewal that finished too late for one request
      can help the next request succeed.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If sign-in still needs attention, OpenClaw better distinguishes saved credentials
      from a connection that has not picked them up and tells you which computer to
      check. Older credentials awaiting repair no longer disable unrelated providers;
      use openclaw doctor --fix for the affected accounts.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Direct OpenAI access needs an API key, selected explicitly if you already
      use a ChatGPT sign-in; fal needs its own credentials. Your default image model
      stays unchanged, so choose one of the new variants when you want to use it.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Your Claw's instructions also allow it to use existing login details for
      tasks you authorize, such as signing into a website, while keeping your other
      permissions in place. When it cannot offer secure setup in chat, it directs
      you to terminal prompts that hide what you type.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Password login now rejects blank passwords and known example values. If
      one prevents your Gateway from starting, replace it, restart OpenClaw, and update
      the apps that connect to it. Short real passwords produce a warning rather than
      a new startup block.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: More model connections can use protected API keys without turning protection
      off. Doctor also gives administrators a working repair for certain older device
      sign-in failures , making it easier to reconnect affected devices.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you use IPv4-mapped network rules for a reverse proxy or device pairing,
      review the addresses you allow. Those rules now cover their full stated range,
      fixing connections that were wrongly rejected. Broad rules may therefore trust
      more addresses than before, including the computer itself; keep the allowed
      range as narrow as your setup needs. Other login and approval checks still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Command errors do a better job of telling you what to do next, such as
      supplying login details or choosing which agent to use, without making a missing
      option look like a broken installation. If openclaw agent loses its connection
      or times out after a task was accepted, the error gives you the task’s ID so
      you can check what happened before trying again. Check its conversation history
      and Gateway status first, because the work may have continued after the connection
      was lost.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-account-and-access-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: account-access
  title: 14 Account and Access changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-10-2-account-and-access-changes-in-v2-1-268|2 Account
  and Access changes in v2.1.268]]'
- '[[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and
  Access changes in 1.17.1]]'
- '[[Changes/Lovable/2026-09-11-require-two-factor-authentication-for-your-workspace|Require
  two-factor authentication for your workspace]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: account-access
title: 14 Account and Access changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Account and Access changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> A new agent can now use an API key you have already saved in OpenClaw's protected storage, fixing a setup failure that left ordinary chats working but new-agent setup stuck. Moonshot's China API-key setup also stops asking you to reinstall a provider that is already installed, and browser sign-in explains when you have pasted a phone setup code into the wrong place.

> Phone setup help now points you to openclaw qr , and the Android instructions explain how to connect to the computer running OpenClaw and set up the login your phone needs. They cover both a trusted home network and Tailscale. Use HTTPS for browser access when possible, because HTTP does not encrypt your login details or messages.

> When you reload the app, it can show a saved copy of your conversation and sidebar while it reconnects, so you have something to read during the wait. This works with remembered Gateway tokens or paired-device sign-ins ; other sign-in methods still show the connection screen. Sending messages and other actions wait for the connection.

> An old “update in progress” message can stop blocking settings changes and account sign-in even when the update itself is no longer running. openclaw update repair can clear eligible stuck updates once it confirms the updater has stopped and OpenClaw is working. Some older requests that never got started clear automatically after a day, provided nothing still needs recovery. They remain in history as failed attempts, with guidance to retry.

> For Mattermost setups that store login tokens separately from account settings, editing one account no longer unnecessarily reconnects the others; settings shared by all accounts can still restart them together. A replacement progress message also stays visible while the old one is being removed, even when both contain the same plan.

> If a Tlon message cannot send because setup is incomplete, the error now tells you which account needs attention and which settings are missing. You can go straight to the relevant part of Tlon setup without guessing, and the error does not reveal your login code.

> Supported OpenAI sign-in methods can reuse an account or key already saved by Codex, saving you another login or paste. Agents sharing a sign-in also handle renewal more reliably, and a renewal that finished too late for one request can help the next request succeed.

> If sign-in still needs attention, OpenClaw better distinguishes saved credentials from a connection that has not picked them up and tells you which computer to check. Older credentials awaiting repair no longer disable unrelated providers; use openclaw doctor --fix for the affected accounts.

> Direct OpenAI access needs an API key, selected explicitly if you already use a ChatGPT sign-in; fal needs its own credentials. Your default image model stays unchanged, so choose one of the new variants when you want to use it.

> Your Claw's instructions also allow it to use existing login details for tasks you authorize, such as signing into a website, while keeping your other permissions in place. When it cannot offer secure setup in chat, it directs you to terminal prompts that hide what you type.

> Password login now rejects blank passwords and known example values. If one prevents your Gateway from starting, replace it, restart OpenClaw, and update the apps that connect to it. Short real passwords produce a warning rather than a new startup block.

> More model connections can use protected API keys without turning protection off. Doctor also gives administrators a working repair for certain older device sign-in failures , making it easier to reconnect affected devices.

> If you use IPv4-mapped network rules for a reverse proxy or device pairing, review the addresses you allow. Those rules now cover their full stated range, fixing connections that were wrongly rejected. Broad rules may therefore trust more addresses than before, including the computer itself; keep the allowed range as narrow as your setup needs. Other login and approval checks still apply.

> Command errors do a better job of telling you what to do next, such as supplying login details or choosing which agent to use, without making a missing option look like a broken installation. If openclaw agent loses its connection or times out after a task was accepted, the error gives you the task’s ID so you can check what happened before trying again. Check its conversation history and Gateway status first, because the work may have continued after the connection was lost.

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
- [[Changes/OpenClaw/2026-09-11-12-safety-and-privacy-changes-in-v2026-9-4|12 Safety and Privacy changes in v2026.9.4]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-11-22-apps-and-integrations-changes-in-v2026-9-4|22 Apps and Integrations changes in v2026.9.4]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-20-model-support-changes-in-v2026-9-4|20 Model Support changes in v2026.9.4]] · Model Support
- [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an|Search installed and available plugins together, browse by purpose, and keep…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-3-search-and-browsing-changes-in-v2026-9-4|3 Search and Browsing changes in v2026.9.4]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-11-you-can-now-enable-desktop-access-for-azure-cloud-workers-whether-openclaw-manag|Enable desktop access for Azure cloud workers , whether OpenClaw manages them…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-3-collaboration-changes-in-v2026-9-4|3 Collaboration changes in v2026.9.4]] · Collaboration
- [[Changes/OpenClaw/2026-09-11-25-agent-mode-changes-in-v2026-9-4|25 Agent Mode changes in v2026.9.4]] · Agent Mode
- [[Changes/OpenClaw/2026-09-11-2-context-window-changes-in-v2026-9-4|2 Context Window changes in v2026.9.4]] · Context Window
- [[Changes/OpenClaw/2026-09-11-56-other-changes-in-v2026-9-4|56 other changes in v2026.9.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-11 · Lovable · [[Changes/Lovable/2026-09-11-require-two-factor-authentication-for-your-workspace|Require two-factor authentication for your workspace]]
- Later: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-changed-claude-apps-gateway-bedrock-vertex-ai-and-foundry-sessions-so-that-they|Changed Claude apps gateway, Bedrock, Vertex AI, and Foundry sessions so that they…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-d887fd&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-14-account-and-access-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-d887fd%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->