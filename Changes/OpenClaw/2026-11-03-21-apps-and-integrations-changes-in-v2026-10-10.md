---
card_id: openclaw-2026-11-03-e4084f
date: '2026-11-03'
description: 'OpenClaw · 2026-11-03 · Apps and Integrations: 21 changes in v2026.10.10
  — The optional MCP Relay lets you connect ChatGPT or Claude to your OpenClaw…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2881
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 49ca6ecd0678f452d06f6dd947b40414d9d1159965cbc433c933b6271f2c9334
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-11-03-e4084f
  comparison: ''
  date: '2026-11-03'
  description: 'OpenClaw — v2026.10.10: 21 Apps and Integrations changes'
  evidence:
  - quote: The optional MCP Relay lets you connect ChatGPT or Claude to your OpenClaw
      conversations without opening an internet-facing Gateway port or handing the
      app your Gateway password. Choose each app's access in Connected apps and revoke
      it there when needed. The relay can read content passing through it, so grant
      access only to apps and a relay you trust.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: An automation can now start when a connected MCP server reports a supported
      event , rather than waiting for a timer to check for changes. Give the event
      instructions for your agent and the connected app need not stay open. This opt-in
      integration supports an experimental MCP Events profile and needs a public HTTPS
      callback; expose only its callback route, not the rest of OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Plugin authors can move affected storage, session and other SDK calls to
      asynchronous replacements . Migrate deprecated synchronous calls by December
      31, 2026; some unsupported calls already reject synchronous use.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Plugin download counts now use the correct million or billion label.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: The community banner no longer shows Pinterest’s Save overlay when the
      integration respects its opt-out.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: When a plugin tool opts in to sending the final reply, that reply now waits
      for the other tools in the same group to finish, so their errors or unfinished
      work are not hidden.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Slack and Discord channel rules now stay with the channel they were set
      for, rather than applying to another channel or thread with the same name. Supported
      credentials and owner approvals also follow the intended account, while changed
      permissions apply to messages still waiting to start.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: MCP tools can reconnect for future calls after a legacy server restarts,
      and duplicate structured results appear only once. A call whose outcome is unknown
      during the disconnect is not automatically repeated; inspect its effect before
      trying again.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Plugin installation and inspection show clearer failure reasons, and a
      broken plugin no longer prevents you from inspecting healthy ones. Configured
      tool guards also apply when an agent runs a standalone command.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Plugin changes now report pending migrations and cleanup failures more
      clearly, while completed migrations stop showing as pending. If an older plugin
      keeps using a file that has been retired and cleaned up, it may need a restart.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Building bundled plugin browser views no longer rewrites tracked source
      manifests.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: In supported Gateway-hosted conversations, an agent can end its current
      turn to reload a plugin, then continue in the same conversation with the result.
      Existing permissions still apply. If the Gateway exits before the result arrives,
      inspect the plugin's state before trying again.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Installed plugins can appear in the list while remote catalog details are
      still loading; refresh later to see those details. Plugin cleanup now reports
      more failures without hiding healthy plugins.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Plugin settings and uninstall previews are less likely to lose your intended
      change when results arrive late, a secret is masked or a plugin ID uses mixed
      capitalization. Changing a masked secret's backend still requires its explicit
      ID.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Claude CLI now follows the MCP server choices you saved for this session
      on its next turn, even when the Claude process is already running.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Plugin turns and side questions now start with the on-request approval
      settings you selected instead of losing them.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Codex and Claude CLI setup now show more of the models and tools your installation
      and account can actually use, with clearer guidance when access or a plugin
      is missing.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: An MCP agent now releases computer control when its run ends, so the session
      no longer keeps that control open. Recording and file transfer remain restricted
      on this path.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Changing settings, plugins or credentials is less likely to interrupt work
      already underway or discard unrelated changes. Some plugin reloads wait until
      active work finishes; if it never finishes, the saved change can remain pending.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: After an update, the result now says whether the core installation finished
      but channel, plugin or restart checks still need attention. A recorded success
      describes that update, not the Gateway's current health.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  - quote: Git backup and pruning now preserve unrelated files and staged edits. Opt-in
      secret exclusions omit identified bundled-plugin credentials, not every possible
      secret or anything already in Git history; restoring a redacted backup may require
      signing in again.
    source_release: https://docs.openclaw.ai/releases/2026.10.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 21-apps-and-integrations-changes-in-v2026-10-10
  source_release: openclaw-2026-11-03-v2026-10-10-c26ff355
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 21 Apps and Integrations changes in v2026.10.10
  type: change
related_changes:
- '[[Changes/Lovable/2026-11-02-connect-your-app-to-bamboohr|Connect your app to BambooHR]]'
- '[[Changes/Google Antigravity/2026-11-03-2-apps-and-integrations-changes-in-hub-v2-29-0-voice-mode-remote|2
  Apps and Integrations changes in HUB v2.29.0 — Voice mode, remote…]]'
- "[[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|\U0001F9E9
  MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]]"
source_release: '[[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|openclaw-2026-11-03-v2026-10-10-c26ff355]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 21 Apps and Integrations changes in v2026.10.10
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Apps and Integrations changes in v2026.10.10

**OpenClaw** · 2026-11-03 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.10) · from [[Releases/OpenClaw/openclaw-2026-11-03-v2026-10-10-c26ff355|v2026.10.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The optional MCP Relay lets you connect ChatGPT or Claude to your OpenClaw conversations without opening an internet-facing Gateway port or handing the app your Gateway password. Choose each app's access in Connected apps and revoke it there when needed. The relay can read content passing through it, so grant access only to apps and a relay you trust.

> An automation can now start when a connected MCP server reports a supported event , rather than waiting for a timer to check for changes. Give the event instructions for your agent and the connected app need not stay open. This opt-in integration supports an experimental MCP Events profile and needs a public HTTPS callback; expose only its callback route, not the rest of OpenClaw.

> Plugin authors can move affected storage, session and other SDK calls to asynchronous replacements . Migrate deprecated synchronous calls by December 31, 2026; some unsupported calls already reject synchronous use.

> Plugin download counts now use the correct million or billion label.

> The community banner no longer shows Pinterest’s Save overlay when the integration respects its opt-out.

> When a plugin tool opts in to sending the final reply, that reply now waits for the other tools in the same group to finish, so their errors or unfinished work are not hidden.

> Slack and Discord channel rules now stay with the channel they were set for, rather than applying to another channel or thread with the same name. Supported credentials and owner approvals also follow the intended account, while changed permissions apply to messages still waiting to start.

> MCP tools can reconnect for future calls after a legacy server restarts, and duplicate structured results appear only once. A call whose outcome is unknown during the disconnect is not automatically repeated; inspect its effect before trying again.

> Plugin installation and inspection show clearer failure reasons, and a broken plugin no longer prevents you from inspecting healthy ones. Configured tool guards also apply when an agent runs a standalone command.

> Plugin changes now report pending migrations and cleanup failures more clearly, while completed migrations stop showing as pending. If an older plugin keeps using a file that has been retired and cleaned up, it may need a restart.

> Building bundled plugin browser views no longer rewrites tracked source manifests.

> In supported Gateway-hosted conversations, an agent can end its current turn to reload a plugin, then continue in the same conversation with the result. Existing permissions still apply. If the Gateway exits before the result arrives, inspect the plugin's state before trying again.

> Installed plugins can appear in the list while remote catalog details are still loading; refresh later to see those details. Plugin cleanup now reports more failures without hiding healthy plugins.

> Plugin settings and uninstall previews are less likely to lose your intended change when results arrive late, a secret is masked or a plugin ID uses mixed capitalization. Changing a masked secret's backend still requires its explicit ID.

> Claude CLI now follows the MCP server choices you saved for this session on its next turn, even when the Claude process is already running.

> Plugin turns and side questions now start with the on-request approval settings you selected instead of losing them.

> Codex and Claude CLI setup now show more of the models and tools your installation and account can actually use, with clearer guidance when access or a plugin is missing.

> An MCP agent now releases computer control when its run ends, so the session no longer keeps that control open. Recording and file transfer remain restricted on this path.

> Changing settings, plugins or credentials is less likely to interrupt work already underway or discard unrelated changes. Some plugin reloads wait until active work finishes; if it never finishes, the saved change can remain pending.

> After an update, the result now says whether the core installation finished but channel, plugin or restart checks still need attention. A recorded success describes that update, not the Gateway's current health.

> Git backup and pruning now preserve unrelated files and staged edits. Opt-in secret exclusions omit identified bundled-plugin credentials, not every possible secret or anything already in Git history; restoring a redacted backup may require signing in again.

Source: https://docs.openclaw.ai/releases/2026.10.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-11-03-generated-images-music-and-video-can-wait-behind-a-busy-chat-without-reporting-f|Generated images, music and video can wait behind a busy chat without reporting…]] · Multimodal Input
- [[Changes/OpenClaw/2026-11-03-you-can-now-guide-the-same-running-conversation-from-the-control-ui-or-an-admini|Guide the same running conversation from the Control UI or an administrator-linked…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-11-03-2-files-and-data-changes-in-v2026-10-10|2 Files and Data changes in v2026.10.10]] · Files and Data
- [[Changes/OpenClaw/2026-11-03-6-account-and-access-changes-in-v2026-10-10|6 Account and Access changes in v2026.10.10]] · Account and Access
- [[Changes/OpenClaw/2026-11-03-image-generation-and-editing-now-reject-invalid-size-and-shape-options-before-co|Image generation and editing now reject invalid size and shape options before…]] · Image Generation
- [[Changes/OpenClaw/2026-11-03-9-agent-mode-changes-in-v2026-10-10|9 Agent Mode changes in v2026.10.10]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-13-interface-experience-changes-in-v2026-10-10|13 Interface Experience changes in v2026.10.10]] · Interface Experience
- [[Changes/OpenClaw/2026-11-03-you-can-now-work-directly-in-a-folder-on-another-computer-connected-to-openclaw|Work directly in a folder on another computer connected to OpenClaw]] · Agent Mode
- [[Changes/OpenClaw/2026-11-03-5-context-window-changes-in-v2026-10-10|5 Context Window changes in v2026.10.10]] · Context Window
- [[Changes/OpenClaw/2026-11-03-15-memory-and-personalization-changes-in-v2026-10-10|15 Memory and Personalization changes in v2026.10.10]] · Memory and Personalization
- [[Changes/OpenClaw/2026-11-03-4-automation-and-scheduling-changes-in-v2026-10-10|4 Automation and Scheduling changes in v2026.10.10]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-11-03-3-editor-experience-changes-in-v2026-10-10|3 Editor Experience changes in v2026.10.10]] · Editor Experience
- [[Changes/OpenClaw/2026-11-03-web-search-now-honors-more-of-your-chosen-provider-settings-result-counts-and-ti|Web search now honors more of your chosen provider settings, result counts…]] · Search and Browsing
- [[Changes/OpenClaw/2026-11-03-6-collaboration-changes-in-v2026-10-10|6 Collaboration changes in v2026.10.10]] · Collaboration
- [[Changes/OpenClaw/2026-11-03-6-voice-and-audio-changes-in-v2026-10-10|6 Voice and Audio changes in v2026.10.10]] · Voice and Audio
- [[Changes/OpenClaw/2026-11-03-7-safety-and-privacy-changes-in-v2026-10-10|7 Safety and Privacy changes in v2026.10.10]] · Safety and Privacy
- [[Changes/OpenClaw/2026-11-03-4-mobile-and-desktop-changes-in-v2026-10-10|4 Mobile and Desktop changes in v2026.10.10]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-11-03-retrying-a-meeting-transcript-from-summary-or-transcript-now-restores-all-availa|Retrying a meeting transcript from Summary or Transcript now restores all available pages]] · Meeting Notes
- [[Changes/OpenClaw/2026-11-03-18-developer-workflow-changes-in-v2026-10-10|18 Developer Workflow changes in v2026.10.10]] · Developer Workflow
- [[Changes/OpenClaw/2026-11-03-17-model-support-changes-in-v2026-10-10|17 Model Support changes in v2026.10.10]] · Model Support
- [[Changes/OpenClaw/2026-11-03-incognito-conversations-now-keep-openclaw-conversation-contents-in-memory-instea|Incognito conversations now keep OpenClaw conversation contents in memory instead…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-11-03-83-other-changes-in-v2026-10-10|83 other changes in v2026.10.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-11-03 · Open WebUI · [[Changes/Open WebUI/2026-11-03-mcp-apps-in-chat-tools-from-mcp-servers-that-come-with-an-interactive-app-now-sh|🧩 MCP Apps in chat. Tools from MCP servers that come with an interactive app now…]]
- Later: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-3-apps-and-integrations-changes-in-v1-35-0|3 Apps and Integrations changes in v1.35.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-11-03-e4084f&body=Card%3A%20Changes%2FOpenClaw%2F2026-11-03-21-apps-and-integrations-changes-in-v2026-10-10.md%0ACard%20ID%3A%20openclaw-2026-11-03-e4084f%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->