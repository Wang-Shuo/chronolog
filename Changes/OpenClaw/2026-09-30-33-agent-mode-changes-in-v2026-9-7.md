---
card_id: openclaw-2026-09-30-3c428a
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Agent Mode: 33 changes in v2026.9.7 — You can
  ask setup chat to remove a setting override and return to the inherited default
  without…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1182
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 706c4ad1d11ccc86df166457b39b20872608145f6fd87062944212757e00e72e
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-3c428a
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 33 Agent Mode changes'
  evidence:
  - quote: You can ask setup chat to remove a setting override and return to the inherited
      default without changing neighboring settings. Existing approvals still apply.
      Remote rescue messages cannot make this change, so use your regular agent or
      the local CLI. Automated channel setup also points to options your selected
      channel supports when something goes wrong.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: New chats can start with the selected agent’s configured model and reasoning
      defaults , while still letting you choose different settings for a draft. This
      is optional; remembering your last choice remains the default. Update the Gateway
      and UI together, then refresh or reconnect before enabling it.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Progress cards remember whether you left them open during the current visit.
      With write access, you can dismiss any card, including unfinished or note-only
      progress, without stopping the agent; later progress may create another one.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Verified backups cover more agent databases, and automatic database rollback
      is available for eligible updates that fail before the new version is allowed
      to start. Check the migration notes below if you use an older installation or
      a retired feature.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: New verified backups check that every database recorded during capture
      is present, including discovered custom and moved agent databases. Older archives
      may have unknown completeness. Make and verify a full backup before updating;
      a config-only export is not a recovery backup. Automatic rollback has limits.
      Database restoration requires a capture made while OpenClaw was stopped, with
      the new version never started and no unaccounted later writes. Changed or incompletely
      captured configuration files may also need manual recovery.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Candidate compatibility checks also preserve the original profile and agent
      database files, including when an incompatible update is refused.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Restart recovery shows interrupted child runs separately from failures
      and helps the parent agent find unfinished work. Children are not automatically
      relaunched. Before repeating an action, the parent must check that the earlier
      run stopped and whether it already changed anything outside OpenClaw.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Feishu reports successful cleanup accurately and lets the agent continue
      editing a newly created document table. Reconnecting also stops matching rich-text
      posts without attachments from starting duplicate replies.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: iMessage sends conversations to their assigned agent even when other routing
      settings conflict. If OpenClaw cannot check that assignment, it stops routing
      instead of choosing another agent. A known harmless Contacts message also stops
      appearing as an error.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Supported channels show typing again when the main assistant resumes work
      after a subagent finishes. Waiting no longer produces a false failure message.
      With tool progress enabled , you can still follow recent work and plans after
      a tool fails.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The agent can resend available attachments from chat history with their
      captions and reply targets. Telegram also stops rejecting reply attachments
      at an accidental 5 MiB cutoff, using its existing 100 MiB default unless you
      set a smaller limit. Telegram's own upload limits still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Native Codex can answer side questions in Discord and Slack while continuing
      the original task. Native child agents can also return follow-up answers after
      waiting for delegated work, within the same running OpenClaw process. See session
      messaging .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Persistent workers created by an agent now need a separate thread, as supported
      by Discord and Matrix. On Telegram and other affected channels, use one-shot
      mode="run" instead. Telegram rejects thread=true and ignores defaultSpawnContext
      for these spawns. Deliberate ACP binding commands remain available; see thread-bound
      sessions .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Recovery of archived child-agent answers now runs its initial database
      checks in the background.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Agents pick up edited skills more consistently after folders are replaced
      or file watching fails. Keep skill watching enabled to use the fallback refresh.
      Sessions in managed worktrees also use the intended skills from your configured
      workspace and project.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Self-hosted Agents API sessions can use skills installed on the executor
      . Install the skills and their dependencies there, then choose their folders
      in settings. All skills in those folders become available for discovery, without
      per-agent filtering. This is opt-in, excludes hosted sessions, and requires
      a session reset when you change a nonempty folder list.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Large Skills menus open with less delay, and choosing an action no longer
      unexpectedly moves focus to the message box. Agents using Code Mode can find
      and read personal skills again, with the same access permissions and content
      limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: User-home Codex connections now follow the provider configured in that
      Codex home, including when an existing chat resumes or forks. Check that it
      supports your model. To keep built-in OpenAI routing, set model_provider = "openai"
      there and restart the app-server, or use an agent-home setup with suitable credentials.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: ACP agents now keep their external agent's model choice separate from OpenClaw's
      own model calls. After updating, check agents.defaults.model and its credentials.
      This can change the provider and account used for those calls, who bills you,
      and where your data goes. Signing in to the external agent does not sign you
      in to that provider. The model guide explains the settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Ollama agents no longer lose free-form tool arguments because of how OpenClaw
      describes them. This fixes affected Tool Search calls that repeatedly failed
      with missing-input errors.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The chat Browser panel shows tabs related to your conversation, and attached
      or cloud-session desktops let you hand control back to the agent after a manual
      step.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Experimental Lightpanda profiles let your agent read pages and fill forms.
      Lightpanda needs separate setup with a protected connection and supports one
      temporary page at a time. After a disconnect, reopen the page and take a new
      snapshot. Chromium remains the default for screenshots, PDFs, file transfers,
      saved sign-ins, multiple tabs, and unsupported sites.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Connected ACP coding agents accept prompts again after a settings-triggered
      restart, and Stop waits for work and cleanup to finish. Some cancellation and
      reset paths can still affect a replacement session. Codex and Claude can recover
      from missing adapter files; restart OpenClaw after updating to refresh their
      launchers. Recovery may need internet access to download an uncached adapter.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Operators can turn off client file and image uploads with gateway.uploads.enabled=false
      while text chat keeps working, without a restart. Uploads are enabled by default.
      Turning them off preserves draft attachments and lets already accepted uploads
      finish; downloads, channel media, and agent-created files follow their own settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Failed remote agent deletion or session cleanup now leaves the computer
      running the command untouched. Restore the remote connection or run the command
      on the Gateway host before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can ask your agent to change OpenClaw settings and update skills you
      own. Existing approvals still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can ask your agent who is connected and which device was recently used
      , within your existing access. Connected tabs may be idle, and any reported
      location is approximate.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Swarms now default to 32 collectors per group, up from eight, and no longer
      compete with ordinary subagents for the same running slots. Ordinary subagent
      limits also apply separately to each spawning conversation. This can increase
      resource use; set tools.swarm.maxConcurrent=8 to keep the previous Swarm cap.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Before ending a reply, the built-in agent gets one chance to revisit an
      unfinished checklist it saved during that run . It can continue the work or
      explain a blocker, which may use another model response. This does not restart
      old tasks or override cancellation and approval waits.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Back up your databases before updating and verify the backup. This update
      automatically moves agent databases to schema 24 , which older builds cannot
      open. To downgrade, restore a verified pre-upgrade backup with its matching
      build; do not lower database version markers.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Conversation lists keep refreshing while other chats save changes. The
      release also fixes temporary-file buildup that could block updates despite free
      disk space, and lets an agent accept new requests after a temporary database
      cleanup failure clears. Failed requests are not automatically repeated.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: A finished subagent batch can now return its results while an unrelated
      earlier batch keeps working. It still waits for its own helpers and their nested
      tasks. The release also fixes cases where helper results restarted work you
      had stopped, or an interrupted task could not find its original request after
      a restart. An agent resuming after its helpers finish can also keep using its
      authorized tools.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Canceling a queued message before it starts now leaves the current reply
      and goal running. Follow-ups sent after a reply finishes go to the next turn,
      and recovery from stuck loops can let waiting messages proceed. Steering sent
      to a busy built-in agent stays queued, but its acceptance does not mean it has
      been read or saved. Queued steering is lost on restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 33-agent-mode-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: agent-mode
  title: 33 Agent Mode changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-30-auto-approval-now-takes-into-account-messages-you-type-while-the-agent-is-workin|Auto-approval
  now takes into account messages you type while the agent is working…]]'
- '[[Changes/Google Antigravity/2026-09-30-message-subagents-directly-export-markdown-as-pdf-and-conversation-only-undo|Message
  subagents directly, export Markdown as PDF, and conversation-only undo]]'
- '[[Changes/Google Antigravity/2026-09-30-you-can-now-send-a-message-directly-to-a-subagent-from-the-message-box-without-g|Send
  a message directly to a subagent from the message box, without going through…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: agent-mode
title: 33 Agent Mode changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 33 Agent Mode changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> You can ask setup chat to remove a setting override and return to the inherited default without changing neighboring settings. Existing approvals still apply. Remote rescue messages cannot make this change, so use your regular agent or the local CLI. Automated channel setup also points to options your selected channel supports when something goes wrong.

> New chats can start with the selected agent’s configured model and reasoning defaults , while still letting you choose different settings for a draft. This is optional; remembering your last choice remains the default. Update the Gateway and UI together, then refresh or reconnect before enabling it.

> Progress cards remember whether you left them open during the current visit. With write access, you can dismiss any card, including unfinished or note-only progress, without stopping the agent; later progress may create another one.

> Verified backups cover more agent databases, and automatic database rollback is available for eligible updates that fail before the new version is allowed to start. Check the migration notes below if you use an older installation or a retired feature.

> New verified backups check that every database recorded during capture is present, including discovered custom and moved agent databases. Older archives may have unknown completeness. Make and verify a full backup before updating; a config-only export is not a recovery backup. Automatic rollback has limits. Database restoration requires a capture made while OpenClaw was stopped, with the new version never started and no unaccounted later writes. Changed or incompletely captured configuration files may also need manual recovery.

> Candidate compatibility checks also preserve the original profile and agent database files, including when an incompatible update is refused.

> Restart recovery shows interrupted child runs separately from failures and helps the parent agent find unfinished work. Children are not automatically relaunched. Before repeating an action, the parent must check that the earlier run stopped and whether it already changed anything outside OpenClaw.

> Feishu reports successful cleanup accurately and lets the agent continue editing a newly created document table. Reconnecting also stops matching rich-text posts without attachments from starting duplicate replies.

> iMessage sends conversations to their assigned agent even when other routing settings conflict. If OpenClaw cannot check that assignment, it stops routing instead of choosing another agent. A known harmless Contacts message also stops appearing as an error.

> Supported channels show typing again when the main assistant resumes work after a subagent finishes. Waiting no longer produces a false failure message. With tool progress enabled , you can still follow recent work and plans after a tool fails.

> The agent can resend available attachments from chat history with their captions and reply targets. Telegram also stops rejecting reply attachments at an accidental 5 MiB cutoff, using its existing 100 MiB default unless you set a smaller limit. Telegram's own upload limits still apply.

> Native Codex can answer side questions in Discord and Slack while continuing the original task. Native child agents can also return follow-up answers after waiting for delegated work, within the same running OpenClaw process. See session messaging .

> Persistent workers created by an agent now need a separate thread, as supported by Discord and Matrix. On Telegram and other affected channels, use one-shot mode="run" instead. Telegram rejects thread=true and ignores defaultSpawnContext for these spawns. Deliberate ACP binding commands remain available; see thread-bound sessions .

> Recovery of archived child-agent answers now runs its initial database checks in the background.

> Agents pick up edited skills more consistently after folders are replaced or file watching fails. Keep skill watching enabled to use the fallback refresh. Sessions in managed worktrees also use the intended skills from your configured workspace and project.

> Self-hosted Agents API sessions can use skills installed on the executor . Install the skills and their dependencies there, then choose their folders in settings. All skills in those folders become available for discovery, without per-agent filtering. This is opt-in, excludes hosted sessions, and requires a session reset when you change a nonempty folder list.

> Large Skills menus open with less delay, and choosing an action no longer unexpectedly moves focus to the message box. Agents using Code Mode can find and read personal skills again, with the same access permissions and content limits.

> User-home Codex connections now follow the provider configured in that Codex home, including when an existing chat resumes or forks. Check that it supports your model. To keep built-in OpenAI routing, set model_provider = "openai" there and restart the app-server, or use an agent-home setup with suitable credentials.

> ACP agents now keep their external agent's model choice separate from OpenClaw's own model calls. After updating, check agents.defaults.model and its credentials. This can change the provider and account used for those calls, who bills you, and where your data goes. Signing in to the external agent does not sign you in to that provider. The model guide explains the settings.

> Ollama agents no longer lose free-form tool arguments because of how OpenClaw describes them. This fixes affected Tool Search calls that repeatedly failed with missing-input errors.

> The chat Browser panel shows tabs related to your conversation, and attached or cloud-session desktops let you hand control back to the agent after a manual step.

> Experimental Lightpanda profiles let your agent read pages and fill forms. Lightpanda needs separate setup with a protected connection and supports one temporary page at a time. After a disconnect, reopen the page and take a new snapshot. Chromium remains the default for screenshots, PDFs, file transfers, saved sign-ins, multiple tabs, and unsupported sites.

> Connected ACP coding agents accept prompts again after a settings-triggered restart, and Stop waits for work and cleanup to finish. Some cancellation and reset paths can still affect a replacement session. Codex and Claude can recover from missing adapter files; restart OpenClaw after updating to refresh their launchers. Recovery may need internet access to download an uncached adapter.

> Operators can turn off client file and image uploads with gateway.uploads.enabled=false while text chat keeps working, without a restart. Uploads are enabled by default. Turning them off preserves draft attachments and lets already accepted uploads finish; downloads, channel media, and agent-created files follow their own settings.

> Failed remote agent deletion or session cleanup now leaves the computer running the command untouched. Restore the remote connection or run the command on the Gateway host before retrying.

> You can ask your agent to change OpenClaw settings and update skills you own. Existing approvals still apply.

> You can ask your agent who is connected and which device was recently used , within your existing access. Connected tabs may be idle, and any reported location is approximate.

> Swarms now default to 32 collectors per group, up from eight, and no longer compete with ordinary subagents for the same running slots. Ordinary subagent limits also apply separately to each spawning conversation. This can increase resource use; set tools.swarm.maxConcurrent=8 to keep the previous Swarm cap.

> Before ending a reply, the built-in agent gets one chance to revisit an unfinished checklist it saved during that run . It can continue the work or explain a blocker, which may use another model response. This does not restart old tasks or override cancellation and approval waits.

> Back up your databases before updating and verify the backup. This update automatically moves agent databases to schema 24 , which older builds cannot open. To downgrade, restore a verified pre-upgrade backup with its matching build; do not lower database version markers.

> Conversation lists keep refreshing while other chats save changes. The release also fixes temporary-file buildup that could block updates despite free disk space, and lets an agent accept new requests after a temporary database cleanup failure clears. Failed requests are not automatically repeated.

> A finished subagent batch can now return its results while an unrelated earlier batch keeps working. It still waits for its own helpers and their nested tasks. The release also fixes cases where helper results restarted work you had stopped, or an interrupted task could not find its original request after a restart. An agent resuming after its helpers finish can also keep using its authorized tools.

> Canceling a queued message before it starts now leaves the current reply and goal running. Follow-ups sent after a reply finishes go to the next turn, and recovery from stuck loops can let waiting messages proceed. Steering sent to a busy built-in agent stays queued, but its acceptance does not mean it has been read or saved. Queued steering is lost on restart.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-30 · Google Antigravity · [[Changes/Google Antigravity/2026-09-30-you-can-now-send-a-message-directly-to-a-subagent-from-the-message-box-without-g|Send a message directly to a subagent from the message box, without going through…]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-4-agent-mode-changes-in-v2-1-287|4 Agent Mode changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-3c428a&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-33-agent-mode-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-3c428a%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->