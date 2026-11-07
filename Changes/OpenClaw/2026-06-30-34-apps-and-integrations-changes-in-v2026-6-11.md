---
card_id: openclaw-2026-06-30-6cf271
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Apps and Integrations: 34 changes in v2026.6.11
  — Exec approval results from external channel plugins now return to the channel
  or DM…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2755
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2d9bb3d95594bd4186ab67ba9e47e15ab366aba665098e6c5708918e834aa661
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-6cf271
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 34 Apps and Integrations changes'
  evidence:
  - quote: 'Exec approval results from external channel plugins now return to the
      channel or DM where the command started instead of falling back to WebChat or
      seeming to disappear after approval. #96140 Related #96103 . Thanks @lansenger-pm,
      @vincentkoc, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: MCP channel integrations now keep conversation lists, message reads, event
      polls, and waits within predictable bounds even when a client requests excessive
      limits or timeouts. a39e548 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Configured channels now remain visible in openclaw channels status --json
      , while scheduled announcements reject stale entries that have no active plugin
      to deliver them. a641c0d
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Qwen and vLLM now preserve existing chat-template settings consistently
      when thinking is switched on or off, and provider plugins can use the same tested
      helper. 2ba9d6e Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: OpenAI-compatible proxy providers can handle thinking levels and legacy
      reasoning_effort fields more consistently, with plugin developers and provider
      maintainers using one documented normalization helper across OpenRouter, Kilocode,
      and the SDK. 35bafea
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Bundled Codex and Copilot integrations now keep mirrored chat history
      and transcript updates tied to the correct OpenClaw session as storage evolves,
      while existing file-backed active transcripts continue working during the migration.
      #89518 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Plugin-channel conversations keep their intended session more reliably
      through startup, doctor checks, and state repairs, with older binding records
      migrated into OpenClaw's shared database. 9f888d9
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Configured plugin policies keep blocking or rewriting sensitive tool calls
      after Gateway registry changes, reloads, or later hook initialization instead
      of being silently skipped. #94545 Thanks @jesse-merhi.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: '"Always allow" approvals for plugin conversation bindings now carry over
      from the old settings file and are less likely to be lost or overwritten when
      multiple OpenClaw processes are running. ae41b00 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Slack router relay mode lets managed or multi-gateway deployments centralize
      incoming Slack traffic while the correct OpenClaw gateway still handles mentions,
      thread affinity, and replies.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Managed Slack deployments can now use a central router to send mentions
      and ongoing threads to the right OpenClaw gateway while replies still appear
      through Slack. #94707 Thanks @pash-openai, @sjf-oa.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: The Raft channel and Raft plugin now support a local CLI wake bridge, so
      External Agents can wake OpenClaw for pending workspace work and operators can
      check setup and status through the supported path.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Plugin management now handles more official integrations through normal
      external package installation and repair flows. The plugin inventory and related
      setup checks give users clearer results when a package is missing, incompatible,
      or needs to be reinstalled.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When plugins.allow uses a channel or package name instead of the real
      plugin id, startup guidance now identifies the unmatched entry and shows the
      discovered plugin ids needed to correct the configuration. #68389 Related #68352
      . Thanks @aym9999, @jirboy, @lyfuci, @pahuchi-joe, @zmxccxy.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Plugin trust warnings for first-time or fresh installs now include a ready-to-copy
      plugins.allow example and commands to list or inspect plugin ids, so users can
      resolve the warning before trusting or reinstalling plugin code. #78105 Related
      #68780 . Thanks @jirboy, @pahuchi-joe.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Codex migrations now work with standard global plugin installs because
      openclaw migrate can find the installed provider instead of failing with Unknown
      migration provider . #89612 Related #89609 . Thanks @mugabuga, @zerone0x.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Plugin installs and updates recover from stale OpenClaw-managed dependency
      pins instead of failing with npm EOVERRIDE , without later synchronization downgrading
      or removing packages users installed explicitly. #91786 Related #91772 . Thanks
      @amknight, @mkdelta221.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Channel plugin developers can now carry native sender and conversation
      identifiers through hooks and selected exec workflows, giving integrations more
      precise routing without breaking existing sender and chat fields. #91903 Thanks
      @lanzhi-lee, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Plugin discovery now repeats fewer blocking filesystem checks during startup,
      reducing avoidable cold-start work for bundled plugin trees, especially on slower
      Windows filesystems, without changing bundle discovery behavior. #93919 Related
      #76209 . Thanks @ml12580, @shenhonglong456-ai.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Pinned official plugins no longer stay on an old release when operators
      follow the repair advice from openclaw doctor or deep gateway status after an
      upgrade. #95541 Thanks @ooiuuii, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Managed npm plugin updates are less likely to break work on a running
      gateway with missing-module errors, because the older plugin files remain available
      until a later gateway start cleans them up. #95589 Thanks @ooiuuii, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Official plugin cards for supported brands now show recognizable icons
      in ClawHub and other catalogs, and plugin authors can provide marketplace artwork
      through the documented manifest field. #95845 Thanks @patrick-erichsen.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Official plugin icons in ClawHub and other catalogs are no longer forced
      into the same hard-coded color, allowing Simple Icons to use its default artwork
      instead. #95987 Thanks @patrick-erichsen.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'People installing or updating the official Yuanbao channel plugin through
      OpenClaw''s trusted catalog now get version 2.15.0, with the expected integrity
      check and missing-plugin guidance aligned to that release. #94470 Thanks @jase-283.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Plugin and CLI developers now see a clearer supported command-formatting
      API, while device pairing, node registration, and doctor guidance keep producing
      the same shell-safe commands. 23b4f33
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Gateway restarts no longer leave configured Codex, Copilot, or trusted
      plugin-based agents temporarily unavailable, and untrusted workspace plugins
      remain blocked from activating themselves. #95652 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Malformed gateway restart requests now fail clearly without scheduling
      a restart, preventing bad or accidental integration calls from unexpectedly
      restarting the gateway. 108d6d7 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Plugin workflows are less likely to stall or overload the gateway when
      an integration requests too much subagent session history, because each read
      is now capped at a safe limit. b66b450 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Completed plugin subagent and QA runs are no longer misreported as failures
      when gateways return alternate completion envelope shapes, making successful
      handoffs more reliable for plugin authors and operators. d1b268f Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'openclaw config validate now accepts command-based MCP server setups that
      explicitly use transport: "stdio" , avoiding false validation errors while still
      rejecting invalid remote-style stdio configurations. #95102 Related #95082 .
      Thanks @ken-jo, @lzyyzznl.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Plugin authors can now use the documented targetSessionKey on subagent_ended
      events to match them with the corresponding spawn, instead of relying on agentId
      or childSessionKey fields that are not emitted. #95191 Related #95186 . Thanks
      @ken-jo, @mahaohao-ch.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Scheduled jobs and built-in tools now finish, retry, report failures, and
      preserve their intended inputs more consistently. Improvements to the plugin
      SDK runtime also make tool-backed extensions more reliable when loading, returning
      results, or running scheduled work.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'SDK runs created with timeoutMs: 0 now keep the requested zero timeout
      without an unwanted client-side watchdog. 2bdcc83 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'SDK applications now receive tool.call.failed when terminal tools fail
      or are blocked, instead of a misleading completion event, so existing failure
      handling can react correctly. #95383 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 34-apps-and-integrations-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 34 Apps and Integrations changes in v2026.6.11
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps
  and Integrations changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9
  Apps and Integrations changes in v1.0.66]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-allow-tool-calls-to-continue-when-hooks-time-out|Allow
  tool calls to continue when hooks time out]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 34 Apps and Integrations changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 34 Apps and Integrations changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Exec approval results from external channel plugins now return to the channel or DM where the command started instead of falling back to WebChat or seeming to disappear after approval. #96140 Related #96103 . Thanks @lansenger-pm, @vincentkoc, @yetval.

> MCP channel integrations now keep conversation lists, message reads, event polls, and waits within predictable bounds even when a client requests excessive limits or timeouts. a39e548 Thanks @vincentkoc.

> Configured channels now remain visible in openclaw channels status --json , while scheduled announcements reject stale entries that have no active plugin to deliver them. a641c0d

> Qwen and vLLM now preserve existing chat-template settings consistently when thinking is switched on or off, and provider plugins can use the same tested helper. 2ba9d6e Thanks @vincentkoc.

> OpenAI-compatible proxy providers can handle thinking levels and legacy reasoning_effort fields more consistently, with plugin developers and provider maintainers using one documented normalization helper across OpenRouter, Kilocode, and the SDK. 35bafea

> Bundled Codex and Copilot integrations now keep mirrored chat history and transcript updates tied to the correct OpenClaw session as storage evolves, while existing file-backed active transcripts continue working during the migration. #89518 Thanks @jalehman.

> Plugin-channel conversations keep their intended session more reliably through startup, doctor checks, and state repairs, with older binding records migrated into OpenClaw's shared database. 9f888d9

> Configured plugin policies keep blocking or rewriting sensitive tool calls after Gateway registry changes, reloads, or later hook initialization instead of being silently skipped. #94545 Thanks @jesse-merhi.

> "Always allow" approvals for plugin conversation bindings now carry over from the old settings file and are less likely to be lost or overwritten when multiple OpenClaw processes are running. ae41b00 Thanks @vincentkoc.

> Slack router relay mode lets managed or multi-gateway deployments centralize incoming Slack traffic while the correct OpenClaw gateway still handles mentions, thread affinity, and replies.

> Managed Slack deployments can now use a central router to send mentions and ongoing threads to the right OpenClaw gateway while replies still appear through Slack. #94707 Thanks @pash-openai, @sjf-oa.

> The Raft channel and Raft plugin now support a local CLI wake bridge, so External Agents can wake OpenClaw for pending workspace work and operators can check setup and status through the supported path.

> Plugin management now handles more official integrations through normal external package installation and repair flows. The plugin inventory and related setup checks give users clearer results when a package is missing, incompatible, or needs to be reinstalled.

> When plugins.allow uses a channel or package name instead of the real plugin id, startup guidance now identifies the unmatched entry and shows the discovered plugin ids needed to correct the configuration. #68389 Related #68352 . Thanks @aym9999, @jirboy, @lyfuci, @pahuchi-joe, @zmxccxy.

> Plugin trust warnings for first-time or fresh installs now include a ready-to-copy plugins.allow example and commands to list or inspect plugin ids, so users can resolve the warning before trusting or reinstalling plugin code. #78105 Related #68780 . Thanks @jirboy, @pahuchi-joe.

> Codex migrations now work with standard global plugin installs because openclaw migrate can find the installed provider instead of failing with Unknown migration provider . #89612 Related #89609 . Thanks @mugabuga, @zerone0x.

> Plugin installs and updates recover from stale OpenClaw-managed dependency pins instead of failing with npm EOVERRIDE , without later synchronization downgrading or removing packages users installed explicitly. #91786 Related #91772 . Thanks @amknight, @mkdelta221.

> Channel plugin developers can now carry native sender and conversation identifiers through hooks and selected exec workflows, giving integrations more precise routing without breaking existing sender and chat fields. #91903 Thanks @lanzhi-lee, @vincentkoc.

> Plugin discovery now repeats fewer blocking filesystem checks during startup, reducing avoidable cold-start work for bundled plugin trees, especially on slower Windows filesystems, without changing bundle discovery behavior. #93919 Related #76209 . Thanks @ml12580, @shenhonglong456-ai.

> Pinned official plugins no longer stay on an old release when operators follow the repair advice from openclaw doctor or deep gateway status after an upgrade. #95541 Thanks @ooiuuii, @vincentkoc.

> Managed npm plugin updates are less likely to break work on a running gateway with missing-module errors, because the older plugin files remain available until a later gateway start cleans them up. #95589 Thanks @ooiuuii, @vincentkoc.

> Official plugin cards for supported brands now show recognizable icons in ClawHub and other catalogs, and plugin authors can provide marketplace artwork through the documented manifest field. #95845 Thanks @patrick-erichsen.

> Official plugin icons in ClawHub and other catalogs are no longer forced into the same hard-coded color, allowing Simple Icons to use its default artwork instead. #95987 Thanks @patrick-erichsen.

> People installing or updating the official Yuanbao channel plugin through OpenClaw's trusted catalog now get version 2.15.0, with the expected integrity check and missing-plugin guidance aligned to that release. #94470 Thanks @jase-283.

> Plugin and CLI developers now see a clearer supported command-formatting API, while device pairing, node registration, and doctor guidance keep producing the same shell-safe commands. 23b4f33

> Gateway restarts no longer leave configured Codex, Copilot, or trusted plugin-based agents temporarily unavailable, and untrusted workspace plugins remain blocked from activating themselves. #95652 Thanks @vincentkoc.

> Malformed gateway restart requests now fail clearly without scheduling a restart, preventing bad or accidental integration calls from unexpectedly restarting the gateway. 108d6d7 Thanks @vincentkoc.

> Plugin workflows are less likely to stall or overload the gateway when an integration requests too much subagent session history, because each read is now capped at a safe limit. b66b450 Thanks @vincentkoc.

> Completed plugin subagent and QA runs are no longer misreported as failures when gateways return alternate completion envelope shapes, making successful handoffs more reliable for plugin authors and operators. d1b268f Thanks @vincentkoc.

> openclaw config validate now accepts command-based MCP server setups that explicitly use transport: "stdio" , avoiding false validation errors while still rejecting invalid remote-style stdio configurations. #95102 Related #95082 . Thanks @ken-jo, @lzyyzznl.

> Plugin authors can now use the documented targetSessionKey on subagent_ended events to match them with the corresponding spawn, instead of relying on agentId or childSessionKey fields that are not emitted. #95191 Related #95186 . Thanks @ken-jo, @mahaohao-ch.

> Scheduled jobs and built-in tools now finish, retry, report failures, and preserve their intended inputs more consistently. Improvements to the plugin SDK runtime also make tool-backed extensions more reliable when loading, returning results, or running scheduled work.

> SDK runs created with timeoutMs: 0 now keep the requested zero timeout without an unwanted client-side watchdog. 2bdcc83 Thanks @vincentkoc.

> SDK applications now receive tool.call.failed when terminal tools fail or are blocked, instead of a misleading completion event, so existing failure handling can react correctly. #95383 Thanks @ly-wang19.

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
## Nearby in Apps and Integrations

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-allow-tool-calls-to-continue-when-hooks-time-out|Allow tool calls to continue when hooks time out]]
- Later: 2026-06-30 · OpenCode · [[Changes/OpenCode/2026-06-30-8-apps-and-integrations-changes-in-v1-17-12|8 Apps and Integrations changes in v1.17.12]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-6cf271&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-34-apps-and-integrations-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-6cf271%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->