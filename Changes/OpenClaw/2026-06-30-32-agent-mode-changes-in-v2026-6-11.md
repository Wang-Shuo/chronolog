---
card_id: openclaw-2026-06-30-2bcbe1
date: '2026-06-30'
description: 'OpenClaw · 2026-06-30 · Agent Mode: 32 changes in v2026.6.11 — Bound
  multi-agent channel conversations now load the workspace files for the configured
  agent…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1090
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9d56fb3f1b750b89e4a5cc5eb6aa9791bf3e691a621b5c37730dbeededa3759d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-06-30-2bcbe1
  comparison: ''
  date: '2026-06-30'
  description: 'OpenClaw — v2026.6.11: 32 Agent Mode changes'
  evidence:
  - quote: 'Bound multi-agent channel conversations now load the workspace files for
      the configured agent instead of the default agent, though previously misfiled
      conversations may start fresh in the corrected agent store. #95118 Related #92903
      . Thanks @849261680, @axjing.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Telegram chats recover after one stuck message times out, allowing later
      messages in the same chat or topic to reach the agent without restarting the
      gateway. #95299 Related #95248 . Thanks @kriegerbangerz-ship-it, @mikasa0818,
      @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Synology Chat users can now receive agent replies that take more than
      120 seconds when the configured core timeout allows it, instead of having the
      channel reject them early. #95707 Thanks @sahibzada-allahyar, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Replies and message-tool delivery in Mattermost channels now use channel
      and thread guidance because the agent identifies those conversations as channels
      rather than group chats, while existing group-chat behavior remains unchanged.
      #96244 Related #95645 . Thanks @arkyu2077, @iloveleon19, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Discord progress previews are less likely to stop before the final edits
      when an agent response has already started arriving. 86ea382
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Provider-qualified model IDs now honor their configured agent runtime
      policies and CLI aliases instead of unexpectedly falling back to OpenClaw''s
      default runtime. #91724 Thanks @vincentkoc, @yu-xin-c.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Fallback agent runs now honor each model's configured automatic fast-mode
      cutoff even when fast mode is overridden for the run, keeping fallback behavior
      aligned with the selected model policy. efd3172
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Embedded agent runs now keep automatic fast mode working consistently through
      retries and progress updates without confusing it with a manually selected fast-mode
      setting. cf1b6fe Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Affected agent conversations using OpenAI Responses can now recover and
      keep replying after a visible channel response leaves their saved history incomplete,
      instead of every later turn failing before a reply appears. #84708 Thanks @anyech.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When a Codex-backed agent produces unusually large tool output, saved
      and replayed conversations now keep its text within the usual size limit while
      leaving non-text content unchanged. #87912 Thanks @adrianip0204.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When cross-agent session access is blocked, OpenClaw now lists all required
      visibility, agent-to-agent, and allow-list settings, helping operators correct
      policy configuration instead of chasing a nonexistent agent failure. #90489
      Related #90443 . Thanks @ramitrkar-hash, @sahibzada-allahyar, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'The /stop and abort commands now keep stopping active runs, clearing queued
      followups, and ending related subagents promptly even when session keys need
      canonicalizing or abort metadata cannot be saved. #96201 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Embedded agent runs with a missing or blank session key now stay attached
      to the intended session instead of being sent through inconsistent session routing.
      911f853 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Agent sessions with many tool calls repair out-of-order results with less
      repeated work while keeping each result paired with the right tool call. #96014
      Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Raft External Agent operators can now wake an OpenClaw agent when a workspace
      has pending work through the supported local CLI bridge, with named profiles
      and checks for missing CLI prerequisites. #95497 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Gateway health and troubleshooting signals now line up more consistently
      with whether OpenClaw is actually ready, restarting, or unable to continue.
      Agent runs started through the CLI recover more cleanly from disconnects, shutdowns,
      routing changes, and failed startup conditions.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Long or parallel internal subagent runs now avoid unnecessary live-preview
      processing, while visible subagent sessions still show live updates and final
      responses. #91906 Thanks @lanzhi-lee, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Long, tool-heavy agent sessions now retain prompt-cache savings as results
      accumulate, reducing avoidable delays and cost from resending rewritten history
      between turns. #95624 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Copilot-backed agents can now ask users a question and accept the answer
      through OpenClaw''s normal chat reply flow, while compact tool-search and code-mode
      controls avoid loading the full tool catalog into the session. #96005 Thanks
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Embedded agent sessions now wait reliably for another session to release
      its file lock, even with an extremely large timeout, instead of risking timer
      overflow. 4c736df Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Agent sessions using OpenAI Responses now resume tool-based work without
      failing or losing progress when replayed history contains mismatched tool requests
      and results. b4bc1f2 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Remote image results and completed subagent work now return through the
      active gateway conversation more reliably instead of appearing to fail or disappear.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: When a subagent finishes, its result now reaches the active parent run
      more reliably instead of appearing silent. 7fc4bbc Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'When a WebChat message fails before the agent starts, WebChat and Control
      UI now show the session as failed instead of leaving it looking like it is still
      running. #84352 Thanks @jesse-merhi.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Android users now get a cleaner Overview where connection status, the
      configured agent, node health, approvals, recent sessions, and Chat and Talk
      actions are visible at a glance. #95557 Thanks @joshavant, @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Long, multiline, or code-heavy prompts can now be sent to openclaw agent
      with --message-file , avoiding fragile shell quoting and reporting invalid files
      before dispatch. #93351 Thanks @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Multi-agent operators can now use openclaw gateway usage-cost to view
      costs for one configured agent or all agents while the existing default-agent
      command remains unchanged. #94483 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Agent channel bindings now reject malformed account specs such as matrix:work:extra
      with a clear error instead of silently routing the agent to a different account.
      #95572 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'People setting a local agent avatar can avoid missing images by keeping
      workspace-relative files under 2 MB, while HTTP(S) and data URI avatars are
      not subject to that limit. #78884 Related #65312 . Thanks @wangjieweb3-design,
      @nyx-nocturna.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'OpenClaw''s default agent instructions now ask agents to check for suitable
      free or open-source solutions before proposing a custom build, while still allowing
      custom work when it is the better fit. #86608 Thanks @cablackmon.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: Windows users are less likely to see agent-managed tool installs fail while
      unpacking ZIP downloads such as ripgrep, because OpenClaw now uses the built-in
      Windows extraction programs instead of relying on PATH lookup. a5fde91
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  - quote: 'Codex subagent monitoring handles large sets of child agents and transcript
      files with less unnecessary scanning, while older transcript filename formats
      continue to resolve as before. #96085 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.6.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 32-agent-mode-changes-in-v2026-6-11
  source_release: openclaw-2026-06-30-v2026-6-11-23cb95a9
  source_type: openclaw_changelog
  theme: agent-mode
  title: 32 Agent Mode changes in v2026.6.11
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|\U0001FAAA
  Client User-Agent forwarded to model backends. The browser's User-Agent is now…]]"
- '[[Changes/GitHub Copilot CLI/2026-06-30-2-agent-mode-changes-in-v1-0-67|2 Agent
  Mode changes in v1.0.67]]'
- '[[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent
  Mode changes in v1.0.66]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|openclaw-2026-06-30-v2026-6-11-23cb95a9]]'
source_type: openclaw_changelog
theme: agent-mode
title: 32 Agent Mode changes in v2026.6.11
type: change
---

<!-- chronolog:begin region="header" -->
# 32 Agent Mode changes in v2026.6.11

**OpenClaw** · 2026-06-30 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.6.11) · from [[Releases/OpenClaw/openclaw-2026-06-30-v2026-6-11-23cb95a9|v2026.6.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Bound multi-agent channel conversations now load the workspace files for the configured agent instead of the default agent, though previously misfiled conversations may start fresh in the corrected agent store. #95118 Related #92903 . Thanks @849261680, @axjing.

> Telegram chats recover after one stuck message times out, allowing later messages in the same chat or topic to reach the agent without restarting the gateway. #95299 Related #95248 . Thanks @kriegerbangerz-ship-it, @mikasa0818, @obviyus.

> Synology Chat users can now receive agent replies that take more than 120 seconds when the configured core timeout allows it, instead of having the channel reject them early. #95707 Thanks @sahibzada-allahyar, @vincentkoc.

> Replies and message-tool delivery in Mattermost channels now use channel and thread guidance because the agent identifies those conversations as channels rather than group chats, while existing group-chat behavior remains unchanged. #96244 Related #95645 . Thanks @arkyu2077, @iloveleon19, @vincentkoc.

> Discord progress previews are less likely to stop before the final edits when an agent response has already started arriving. 86ea382

> Provider-qualified model IDs now honor their configured agent runtime policies and CLI aliases instead of unexpectedly falling back to OpenClaw's default runtime. #91724 Thanks @vincentkoc, @yu-xin-c.

> Fallback agent runs now honor each model's configured automatic fast-mode cutoff even when fast mode is overridden for the run, keeping fallback behavior aligned with the selected model policy. efd3172

> Embedded agent runs now keep automatic fast mode working consistently through retries and progress updates without confusing it with a manually selected fast-mode setting. cf1b6fe Thanks @vincentkoc.

> Affected agent conversations using OpenAI Responses can now recover and keep replying after a visible channel response leaves their saved history incomplete, instead of every later turn failing before a reply appears. #84708 Thanks @anyech.

> When a Codex-backed agent produces unusually large tool output, saved and replayed conversations now keep its text within the usual size limit while leaving non-text content unchanged. #87912 Thanks @adrianip0204.

> When cross-agent session access is blocked, OpenClaw now lists all required visibility, agent-to-agent, and allow-list settings, helping operators correct policy configuration instead of chasing a nonexistent agent failure. #90489 Related #90443 . Thanks @ramitrkar-hash, @sahibzada-allahyar, @vincentkoc.

> The /stop and abort commands now keep stopping active runs, clearing queued followups, and ending related subagents promptly even when session keys need canonicalizing or abort metadata cannot be saved. #96201 Thanks @jalehman.

> Embedded agent runs with a missing or blank session key now stay attached to the intended session instead of being sent through inconsistent session routing. 911f853 Thanks @vincentkoc.

> Agent sessions with many tool calls repair out-of-order results with less repeated work while keeping each result paired with the right tool call. #96014 Thanks @vincentkoc.

> Raft External Agent operators can now wake an OpenClaw agent when a workspace has pending work through the supported local CLI bridge, with named profiles and checks for missing CLI prerequisites. #95497 Thanks @vincentkoc.

> Gateway health and troubleshooting signals now line up more consistently with whether OpenClaw is actually ready, restarting, or unable to continue. Agent runs started through the CLI recover more cleanly from disconnects, shutdowns, routing changes, and failed startup conditions.

> Long or parallel internal subagent runs now avoid unnecessary live-preview processing, while visible subagent sessions still show live updates and final responses. #91906 Thanks @lanzhi-lee, @vincentkoc.

> Long, tool-heavy agent sessions now retain prompt-cache savings as results accumulate, reducing avoidable delays and cost from resending rewritten history between turns. #95624 Thanks @vincentkoc.

> Copilot-backed agents can now ask users a question and accept the answer through OpenClaw's normal chat reply flow, while compact tool-search and code-mode controls avoid loading the full tool catalog into the session. #96005 Thanks @vincentkoc.

> Embedded agent sessions now wait reliably for another session to release its file lock, even with an extremely large timeout, instead of risking timer overflow. 4c736df Thanks @vincentkoc.

> Agent sessions using OpenAI Responses now resume tool-based work without failing or losing progress when replayed history contains mismatched tool requests and results. b4bc1f2 Thanks @vincentkoc.

> Remote image results and completed subagent work now return through the active gateway conversation more reliably instead of appearing to fail or disappear.

> When a subagent finishes, its result now reaches the active parent run more reliably instead of appearing silent. 7fc4bbc Thanks @vincentkoc.

> When a WebChat message fails before the agent starts, WebChat and Control UI now show the session as failed instead of leaving it looking like it is still running. #84352 Thanks @jesse-merhi.

> Android users now get a cleaner Overview where connection status, the configured agent, node health, approvals, recent sessions, and Chat and Talk actions are visible at a glance. #95557 Thanks @joshavant, @solvely-colin.

> Long, multiline, or code-heavy prompts can now be sent to openclaw agent with --message-file , avoiding fragile shell quoting and reporting invalid files before dispatch. #93351 Thanks @ooiuuii.

> Multi-agent operators can now use openclaw gateway usage-cost to view costs for one configured agent or all agents while the existing default-agent command remains unchanged. #94483 Thanks @ly-wang19.

> Agent channel bindings now reject malformed account specs such as matrix:work:extra with a clear error instead of silently routing the agent to a different account. #95572 Thanks @ly-wang19.

> People setting a local agent avatar can avoid missing images by keeping workspace-relative files under 2 MB, while HTTP(S) and data URI avatars are not subject to that limit. #78884 Related #65312 . Thanks @wangjieweb3-design, @nyx-nocturna.

> OpenClaw's default agent instructions now ask agents to check for suitable free or open-source solutions before proposing a custom build, while still allowing custom work when it is the better fit. #86608 Thanks @cablackmon.

> Windows users are less likely to see agent-managed tool installs fail while unpacking ZIP downloads such as ripgrep, because OpenClaw now uses the built-in Windows extraction programs instead of relying on PATH lookup. a5fde91

> Codex subagent monitoring handles large sets of child agents and transcript files with less unnecessary scanning, while older transcript filename formats continue to resolve as before. #96085 Thanks @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.6.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-06-30-7-editor-experience-changes-in-v2026-6-11|7 Editor Experience changes in v2026.6.11]] · Editor Experience
- [[Changes/OpenClaw/2026-06-30-canvas-a2ui-now-serves-only-the-current-app-assets-after-each-build-so-outdated|Canvas A2UI now serves only the current app assets after each build, so outdated…]] · Files and Data
- [[Changes/OpenClaw/2026-06-30-word-powerpoint-and-excel-document-reads-and-writes-now-use-the-intended-docx-pp|Word, PowerPoint, and Excel document reads and writes now use the intended .docx…]] · Presentation Creation
- [[Changes/OpenClaw/2026-06-30-20-context-window-changes-in-v2026-6-11|20 Context Window changes in v2026.6.11]] · Context Window
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
- [[Changes/OpenClaw/2026-06-30-9-developer-workflow-changes-in-v2026-6-11|9 Developer Workflow changes in v2026.6.11]] · Developer Workflow
- [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Safety and Privacy
- [[Changes/OpenClaw/2026-06-30-more-official-channel-provider-and-web-search-plugins-can-now-be-installed-or-re|More official channel, provider, and web-search plugins can now be installed…]] · Search and Browsing
- [[Changes/OpenClaw/2026-06-30-generated-images-from-a-remote-codex-app-server-now-arrive-as-attachments-instea|Generated images from a remote Codex app-server now arrive as attachments instead…]] · Image Generation
- [[Changes/OpenClaw/2026-06-30-background-image-video-and-music-results-now-return-to-the-chat-that-requested-t|Background image, video, and music results now return to the chat that requested…]] · Music Generation
- [[Changes/OpenClaw/2026-06-30-2-account-and-access-changes-in-v2026-6-11|2 Account and Access changes in v2026.6.11]] · Account and Access
- [[Changes/OpenClaw/2026-06-30-96-other-changes-in-v2026-6-11|96 other changes in v2026.6.11]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent Mode changes in v1.0.66]]
- Later: 2026-07-01 · Claude Code · [[Changes/Claude Code/2026-07-01-5-agent-mode-changes-in-v2-1-198|5 Agent Mode changes in v2.1.198]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-06-30-2bcbe1&body=Card%3A%20Changes%2FOpenClaw%2F2026-06-30-32-agent-mode-changes-in-v2026-6-11.md%0ACard%20ID%3A%20openclaw-2026-06-30-2bcbe1%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.6.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->