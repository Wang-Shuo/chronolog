---
card_id: openclaw-2026-09-11-d6b2f2
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Apps and Integrations: 22 changes in v2026.9.4
  — OpenClaw 2026.9.4 makes plugins and skills easier to find, and lets you turn past…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2828
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 31dcd7a1ef88d8c6d4fe318d8b7a3fcfd1bd3bf058f089e627c8c7069862ebb3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-d6b2f2
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 22 Apps and Integrations changes'
  evidence:
  - quote: OpenClaw 2026.9.4 makes plugins and skills easier to find, and lets you
      turn past conversations into reusable skills through a chat you can steer.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If OpenClaw will not start because of Node, the software it runs on, it
      can now find a compatible copy already on your computer or offer to install
      one just for OpenClaw . You approve the first installation; after that, OpenClaw
      can reuse it automatically. This gives you a way past the startup problem without
      changing Node for your other apps. Some systems, including Alpine Linux, still
      need manual installation. If you cannot start normally, basic help and troubleshooting
      commands remain available on some older Node versions.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: A way past startup trouble without changing Node for your other apps. Conceptual
      illustration, not a screenshot. Some systems, including Alpine Linux, still
      need manual installation.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Updating OpenClaw gets fixes for stalled upgrades, plugins left behind,
      and confusing recovery messages. There are also improvements to bringing older
      conversations and settings forward, backing up the files you need, and cleaning
      up history without getting in the way of other work.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Running openclaw update now checks eligible plugins even if the main app
      is already up to date, including after you updated it separately. When nothing
      changes, it skips unnecessary follow-up work. If you deliberately kept a plugin
      at a particular version, that choice stays in place and notices of newer official
      releases explain how to change it. Plugin updates may need a restart, and plugin
      downloads during an app update can extend the time OpenClaw is unavailable.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Slack can show its configured reaction when it picks up your mention even
      if you have ongoing status reactions turned off. Messages containing Windows
      paths also keep their formatting without accidentally turning the text that
      follows into code.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If a separately installed Feishu plugin stopped letting your Claw work
      with documents, wikis, Drive, or Bitable from chat, those tools are available
      again with your existing permissions. Changes to tool and account settings now
      apply to new requests without restarting OpenClaw, while work already underway
      keeps its earlier settings. Your Claw also receives the emphasis you put in
      formatted messages, links, and mentions.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you use a plugin to manage conversation history , summaries are less
      likely to fail because a connection closed too soon. OpenClaw also avoids unexpectedly
      switching to a backup plugin while a turn starts. Cancelling can still stop
      further changes to the conversation while the plugin finishes closing its connections.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: OpenCode Go and Zen requests made outside an ongoing conversation no longer
      fail just because the service needs session information that was missing. OpenClaw
      supplies it automatically for the supported direct connections, including requests
      from the command line and supported integrations. Custom server connections
      keep their existing requirements.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Scheduled commands run by OpenClaw can work without turning off secret
      protection, and Codex chats can set up automations using the tools already available
      in the conversation. Tasks also avoid startup failures caused by model settings
      refreshing or an unrelated plugin being disabled. Your existing permissions
      still apply, and disabled plugins stay off.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If Codex Computer Use cannot start because native plugins are disabled,
      it now explains that promptly and tells you how to enable them and retry installation.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you manage plugins from the terminal, error messages now point to recovery
      commands for your profile or container and explain whether you need to restart
      OpenClaw. Plugin checks also report cleanup failures instead of claiming success,
      and slow catalog responses no longer keep commands waiting indefinitely.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: People building plugins get fixes for type errors and missing supporting
      files that could stop a build. You can also opt into live previews in the browser
      , seeing changes to your plugin against a real OpenClaw installation. If you
      wrap the multi-account configuration helper, check its updated types when rebuilding;
      the SDK guide covers development setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Requests using model plugins are less likely to fail because a connection
      closed while work was still finishing. OpenClaw keeps those connections available
      through cancellation, plugin reloads, and shutdown. A plugin that cannot finish
      closing can still delay shutdown.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you connect external tools through MCP , large text replies from connected
      devices no longer include an unnecessary duplicate copy. Stopping a standalone
      MCP service gives ongoing tool work time to finish cleaning up, and an accepted
      disconnect no longer gets stuck waiting on response cleanup. Failed disconnects
      still report a problem that may need attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Apps using OpenClaw through Chat Completions or the Responses API can now
      tell when an answer stopped at its output limit. They keep the partial answer
      and receive a clear signal that it was cut short, including during streaming,
      so they can decide what to show or do next. Connected apps also get a more accurate
      report of which settings changed after a configuration update.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Reports opens at the short /reports address inside OpenClaw, and embedded
      plugin pages use more of the window. Plugin panels also load in affected containers
      where file permissions previously got in the way.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you use separate Team Reports report or export links, change /reports/...
      to /plugins/team-reports/... ; old links do not redirect automatically. The
      guide explains how to keep a custom address if you need one.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Turning tools off now carries through to supported connected agents, including
      Copilot, even when you return to a conversation that previously allowed them.
      If an integration cannot honor that restriction, OpenClaw stops rather than
      continuing with tools enabled. Update the plugin or choose a supported agent
      to continue.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: For Slack connections using HTTP webhooks, OpenClaw now enforces limits
      on oversized, slow, or excessive incoming requests before processing them. Feishu
      and Lark webhooks also reject signed requests dated more than an hour before
      or after the computer's clock. Keep that clock synchronized, and check Feishu
      troubleshooting if delayed deliveries are rejected. Feishu's WebSocket connection
      mode is unaffected.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Old plugin messages outside the current conversation no longer stop its
      history from loading, and long conversations keep recent messages available
      when your Claw pauses to wait for other work. If a text-only reply fails partway
      through, the model also receives a short note about that failure when you continue,
      so the attempt no longer disappears from its context.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Build and package checks better recognize which dependencies and files
      belong in each release package. This reduces false failures when maintainers
      prepare plugins and check their contents.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 22-apps-and-integrations-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 22 Apps and Integrations changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Devin/2026-09-11-datadog-mcp-on-the-stable-endpoint|Datadog MCP on the
  Stable Endpoint]]'
- '[[Changes/Lovable/2026-09-11-get-a-warning-when-another-lovable-project-already-uses-your-supabase-project|Get
  a warning when another Lovable project already uses your Supabase project]]'
- '[[Changes/Lovable/2026-09-11-connect-other-mcp-clients-to-the-lovable-mcp-server|Connect
  other MCP clients to the Lovable MCP server]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 22 Apps and Integrations changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 22 Apps and Integrations changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw 2026.9.4 makes plugins and skills easier to find, and lets you turn past conversations into reusable skills through a chat you can steer.

> If OpenClaw will not start because of Node, the software it runs on, it can now find a compatible copy already on your computer or offer to install one just for OpenClaw . You approve the first installation; after that, OpenClaw can reuse it automatically. This gives you a way past the startup problem without changing Node for your other apps. Some systems, including Alpine Linux, still need manual installation. If you cannot start normally, basic help and troubleshooting commands remain available on some older Node versions.

> A way past startup trouble without changing Node for your other apps. Conceptual illustration, not a screenshot. Some systems, including Alpine Linux, still need manual installation.

> Updating OpenClaw gets fixes for stalled upgrades, plugins left behind, and confusing recovery messages. There are also improvements to bringing older conversations and settings forward, backing up the files you need, and cleaning up history without getting in the way of other work.

> Running openclaw update now checks eligible plugins even if the main app is already up to date, including after you updated it separately. When nothing changes, it skips unnecessary follow-up work. If you deliberately kept a plugin at a particular version, that choice stays in place and notices of newer official releases explain how to change it. Plugin updates may need a restart, and plugin downloads during an app update can extend the time OpenClaw is unavailable.

> Slack can show its configured reaction when it picks up your mention even if you have ongoing status reactions turned off. Messages containing Windows paths also keep their formatting without accidentally turning the text that follows into code.

> If a separately installed Feishu plugin stopped letting your Claw work with documents, wikis, Drive, or Bitable from chat, those tools are available again with your existing permissions. Changes to tool and account settings now apply to new requests without restarting OpenClaw, while work already underway keeps its earlier settings. Your Claw also receives the emphasis you put in formatted messages, links, and mentions.

> If you use a plugin to manage conversation history , summaries are less likely to fail because a connection closed too soon. OpenClaw also avoids unexpectedly switching to a backup plugin while a turn starts. Cancelling can still stop further changes to the conversation while the plugin finishes closing its connections.

> OpenCode Go and Zen requests made outside an ongoing conversation no longer fail just because the service needs session information that was missing. OpenClaw supplies it automatically for the supported direct connections, including requests from the command line and supported integrations. Custom server connections keep their existing requirements.

> Scheduled commands run by OpenClaw can work without turning off secret protection, and Codex chats can set up automations using the tools already available in the conversation. Tasks also avoid startup failures caused by model settings refreshing or an unrelated plugin being disabled. Your existing permissions still apply, and disabled plugins stay off.

> If Codex Computer Use cannot start because native plugins are disabled, it now explains that promptly and tells you how to enable them and retry installation.

> If you manage plugins from the terminal, error messages now point to recovery commands for your profile or container and explain whether you need to restart OpenClaw. Plugin checks also report cleanup failures instead of claiming success, and slow catalog responses no longer keep commands waiting indefinitely.

> People building plugins get fixes for type errors and missing supporting files that could stop a build. You can also opt into live previews in the browser , seeing changes to your plugin against a real OpenClaw installation. If you wrap the multi-account configuration helper, check its updated types when rebuilding; the SDK guide covers development setup.

> Requests using model plugins are less likely to fail because a connection closed while work was still finishing. OpenClaw keeps those connections available through cancellation, plugin reloads, and shutdown. A plugin that cannot finish closing can still delay shutdown.

> If you connect external tools through MCP , large text replies from connected devices no longer include an unnecessary duplicate copy. Stopping a standalone MCP service gives ongoing tool work time to finish cleaning up, and an accepted disconnect no longer gets stuck waiting on response cleanup. Failed disconnects still report a problem that may need attention.

> Apps using OpenClaw through Chat Completions or the Responses API can now tell when an answer stopped at its output limit. They keep the partial answer and receive a clear signal that it was cut short, including during streaming, so they can decide what to show or do next. Connected apps also get a more accurate report of which settings changed after a configuration update.

> Reports opens at the short /reports address inside OpenClaw, and embedded plugin pages use more of the window. Plugin panels also load in affected containers where file permissions previously got in the way.

> If you use separate Team Reports report or export links, change /reports/... to /plugins/team-reports/... ; old links do not redirect automatically. The guide explains how to keep a custom address if you need one.

> Turning tools off now carries through to supported connected agents, including Copilot, even when you return to a conversation that previously allowed them. If an integration cannot honor that restriction, OpenClaw stops rather than continuing with tools enabled. Update the plugin or choose a supported agent to continue.

> For Slack connections using HTTP webhooks, OpenClaw now enforces limits on oversized, slow, or excessive incoming requests before processing them. Feishu and Lark webhooks also reject signed requests dated more than an hour before or after the computer's clock. Keep that clock synchronized, and check Feishu troubleshooting if delayed deliveries are rejected. Feishu's WebSocket connection mode is unaffected.

> Old plugin messages outside the current conversation no longer stop its history from loading, and long conversations keep recent messages available when your Claw pauses to wait for other work. If a text-only reply fails partway through, the model also receives a short note about that failure when you continue, so the attempt no longer disappears from its context.

> Build and package checks better recognize which dependencies and files belong in each release package. This reduces false failures when maintainers prepare plugins and check their contents.

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
## Nearby in Apps and Integrations

- Earlier: 2026-09-11 · Lovable · [[Changes/Lovable/2026-09-11-connect-other-mcp-clients-to-the-lovable-mcp-server|Connect other MCP clients to the Lovable MCP server]]
- Later: 2026-09-11 · Raycast · [[Changes/Raycast/2026-09-11-window-management-custom-layouts-have-a-new-other-windows-option-minimize-others|Window Management : Custom layouts have a new Other Windows option: Minimize Others…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-d6b2f2&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-22-apps-and-integrations-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-d6b2f2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->