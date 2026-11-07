---
card_id: openclaw-2026-09-05-8e79c2
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Agent Mode: 34 changes in v2026.9.2 — Clean,
  environment-only agent runs using an OpenAI API key can now start through the built-in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1157
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b514ba4619019fa9595e02ca066c477b0cf3bc359eae53598c77668272844ef8
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-8e79c2
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 34 Agent Mode changes'
  evidence:
  - quote: Clean, environment-only agent runs using an OpenAI API key can now start
      through the built-in OpenClaw runtime when the optional Codex runtime is absent.
      This removes a setup failure before the agent could answer or begin its task,
      while explicitly chosen runtimes and existing session pins continue to require
      their selected runtime.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When the bundled Control UI skill is available to your agent, type /dashboard
      with what you want to see to request a board for the current session. Choosing
      Dashboard in the side panel opens the board directly without adding anything
      to your message. The dashboard guide includes a one-prompt demonstration, and
      the command uses the bundled Control UI instructions even when a workspace has
      another skill with that name. A custom skill named dashboard remains available
      through $dashboard or /skill dashboard , with its slash alias moved to /dashboard_2
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Widgets pinned from an agent's global session stay with that agent's board
      and notify its authorized viewers. Automatically sized HTML widgets keep their
      content height instead of progressively shrinking, while manual sizes remain
      yours to set. If creating a visible dashboard session fails, cleanup preserves
      a newer replacement session and tells you when the original child needs inspection
      before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Searching Sessions can now find matching active or archived conversations
      beyond the rows already loaded, with Load more sessions bringing in further
      matches. It searches conversation details such as names, models, status, and
      agent identity, while transcript search remains a separate way to search the
      messages themselves. Counts, grouping, and sorting still describe the loaded
      rows.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Owner choices move into a compact submenu, sharing and owner details sit
      together in the chat header, and copied session links use the configured public
      address even through a local SSH tunnel. Unrelated agent activity no longer
      repeatedly reloads the selected agent's list, and pinning or renaming another
      session can continue while a model catalog loads. Opening a chat clears its
      unread dot immediately, although new activity arriving during the acknowledgement
      refresh can still briefly be masked.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Tool activity keeps related calls together after reload and shows a short
      purpose supplied by the acting agent when one is available, with full commands
      and results underneath. There are no extra model calls just to name those rows,
      and the description tells you the intended work while the result tells you whether
      it succeeded. If your configuration contains the retired gateway.controlUi.toolTitles
      key, remove it even when its value is false. openclaw doctor --fix handles supported
      configurations, while managed or included configuration files may need changes
      at their source.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Automatic updates now keep enabled skill preferences when a prerequisite
      happens to be missing from the update environment, and fully repairable older
      multi-agent configurations retain current choices such as the update channel,
      port, and original default agent. A failed agent-settings save also keeps the
      previous complete file readable. Enabled skills still need their prerequisites
      before they can run, and an explicit standalone Doctor repair can still disable
      unavailable skills.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: If an intended owner has lost access to restart or update commands because
      their saved identity uses an older channel:user:id form, run the same explicit
      Doctor repair to migrate recognized, unambiguous entries. Upgrading alone does
      not rewrite those owner entries, and ambiguous identities or default-agent choices
      still need manual correction.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: In supported Slack agent sessions, the native Stop button now reaches the
      work running in the selected conversation, including overlapping replies in
      group DMs, while session status shows when the agent is working or waiting for
      an approval. Rename a supported session in Slack and OpenClaw keeps that name
      through later messages, with delayed controls checked against the conversation
      they belong to.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: In Slack compact progress mode , the final answer arrives as a new message
      after any conversation or media that appeared while the agent worked. Temporary
      progress is removed after Slack confirms delivery, and a failed send leaves
      the preview available.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When Claude Code needs an answer before continuing, its native question
      can now reach the channel conversation instead of appearing only in the web
      dashboard. Replying in plain text to that same conversation can answer the waiting
      question and resume the run, including in installations with several agents.
      This repairs the existing question workflow, with Telegram directly demonstrated;
      messages containing media do not use this early plain-text answer path.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A final answer already delivered to the same external conversation can
      now suppress the extra automatic reply or same-conversation agent announcement,
      even when another layer rewrites the tool’s visible output. This depends on
      confirmed final delivery to that destination; a progress update, a dry run,
      or a message to another conversation does not count as the answer.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When an agent has already generated images or other files, a later tool
      error or reasoning-only response no longer decides which of those attachments
      survive. The media guide explains how generated files remain available alongside
      the warning, even when the warning mentions only one of them.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Skills get practical repairs from creation through installation and remote
      use. Workshop explains more failed reviews and protects current edits during
      uncertain restores, while paired and remote workers use the instructions and
      supporting files prepared for their own turn. Bundled guidance also gives agents
      a clearer path through dashboard building and delegated work without changing
      the permissions those tasks require.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Skill Workshop now identifies conflicting support-file locations before
      saving a proposal, and refuses proposals or evaluations that would silently
      omit unreadable or excessively nested content. When agents sharing a workspace
      cannot start a collection review because a provider credential is missing, the
      error names the affected provider and agent so the operator can fix authentication
      without guessing at model settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: You can change the thinking level before the next turn while retaining
      a compatible cached prompt prefix. Automatic compaction, automatic truncation,
      pro mode, and API multi-agent mode do not support that optimization, and a restart
      or rewritten history starts a fresh request. Finish pending tool results or
      approvals in a compatible Astra mode before switching. Where runtime capabilities
      permit it, /think ultra also enables proactive delegation to sub-agents, using
      max effort in OpenClaw and xhigh in native Codex.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The local-server guide now uses llmman , the maintained replacement for
      Inferrs, with corrected startup commands, readiness checks, and troubleshooting
      for requests that work directly but fail during a larger agent task. Existing
      Inferrs documentation links redirect to the new guide. Keep its unauthenticated
      service on loopback or behind trusted access controls.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Codex conversations keep the model and account selected for their native
      thread when you continue them, including imported conversations whose model
      differs from the agent's default. Fork from here retains the draft and source
      thread's current model on Codex 0.153 or newer, and an empty native tool catalog
      no longer makes a supervised conversation look corrupt. Separate Ask OpenClaw
      conversations also keep separate Codex threads.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Failed requests with unfinished tool calls now retain the provider's reported
      usage, served model, and available failure reason when terminal information
      arrives. Incomplete tools remain blocked, along with later parallel tool completions
      after the incomplete call. Tiny managed output budgets are raised to the API's
      16-token minimum, and explicitly selected agents can use their allowed API model
      overrides on multi-agent Gateways without requiring a system agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A scheduled agent or script that is allowed to remove its own job can now
      delete the schedule and still finish its final result. Removing the job yourself
      continues to cancel it, and removing or disabling a job while it checks a condition
      prevents that pending check from starting the action. Effects already completed
      are not undone, and work already handed to the main conversation's heartbeat
      keeps its own lifecycle.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Turning off recurring heartbeats no longer drops the spacing and flood
      limits for event-triggered work, and reloading settings preserves those limits
      while a turn is running. When OpenClaw refuses a check, its notice explains
      the reason without requiring verbose mode. Duplicate heartbeat and skill-review
      monitors can also be reconciled during startup, while large agent fleets avoid
      repeated heartbeat-summary work in health and status checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A2A tasks that need an execution approval now keep their original task
      and reply path through the operator's decision, including peers without an outbound
      URL. Ordinary text such as “Explain /help please” reaches the agent unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Direct calls to File Transfer directory tools now give the agent usable
      filenames and distinguish files from directories. A listing can continue after
      its last displayed entry, and fetched directories show the saved root and relative
      paths needed to open the files locally. Large fetched trees remain saved even
      when only part of their manifest fits in the text result; the result explains
      how to inspect omitted files, and reports when an unrepresentable path prevents
      text pagination from advancing.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Successful individual file fetches also expose both their saved path and
      a reusable media ID, so an authorized write tool can copy those bytes without
      guessing at a hidden identifier. Restricted tool sets receive self-contained
      Bitable and search guidance without being sent to unavailable companion tools.
      If Bitable creates an application but cannot retrieve its table metadata, the
      guidance now tells the agent to keep the successfully created application.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: If you run several agents on one Gateway, review their conversation access
      before upgrading. Where the settings were previously omitted, agents with session
      tools now gain access to other agents’ conversations, including other users’
      transcripts. Choose narrower session visibility, restrict the participating
      agents, or disable ordinary cross-agent access if that sharing is not what you
      intend. Alongside this change, approvals follow current permissions through
      more of a task, switching Gateways retires the previous Gateway’s automatic
      skill trust, and conversation cleanup preserves data belonging to other agents.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Agents can now cooperate across one Gateway without first enabling two
      settings. Omitted tools.sessions.visibility changes from agent to all , and
      omitted tools.agentToAgent.enabled changes from false to true , allowing agents
      with the relevant tools to list, read, search, message, and inspect other agents’
      sessions. Existing explicit restrictions still apply, but leaving these settings
      unset on an older installation now permits broader access on upgrade.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The session visibility settings let you set tools.sessions.visibility to
      agent for the current agent’s conversations or self for only the current conversation.
      agent can still include other users’ conversations under that agent. To keep
      selected agents working together, set an explicit tools.agentToAgent.allow list
      that includes both the requesting and receiving agents, or set tools.agentToAgent.enabled
      to false to block ordinary cross-agent access. An omitted or empty allowlist
      permits all agent pairs when access is enabled, and deleting an agent can empty
      that list, so check it again after removal.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Run openclaw security audit to identify agents that retain unrestricted
      cross-agent session-tool access and see narrowing guidance. These are controls
      within one trusted Gateway , not isolation from its administrators. Mutually
      untrusted users need separate Gateways and credentials, ideally under separate
      OS users or on separate hosts.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Deleting a conversation now retains current and historical data if the
      original caller loses authority before the deletion commits. Deleting one agent’s
      global session also preserves other agents’ saved plugin state and timestamps.
      Selected-agent global-session reads, delivery, boards, run lookup, search checks,
      and GitHub publication keep the explicitly selected agent, although retained-global
      links and unscoped session-list ownership still have separate unresolved cases.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Swarm lets an agent coordinate several helpers and collect their results,
      and eligible agents now have it available by default. It remains experimental
      and follows your existing tool permissions and limits, with an explicit opt-out
      in Settings → Agents & Tools → Labs → Swarm . OpenClaw Code Mode remains a separate
      opt-in.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A failed tool call no longer puts Code Mode into a separate read-only recovery
      mode. Your agent can read the error, inspect the current files or settings,
      and make the remaining changes without restarting the conversation or being
      limited to one further edit. Failed programs are not automatically replayed,
      and because an earlier call may have partly succeeded, the agent needs to check
      what already happened before repeating an action. Normal permissions and approvals
      still apply to every later call.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: You can ask your agent to organize the conversations it is allowed to manage
      through session tools , including applying the same group, pin, model, or supported
      setting to as many as 100 sessions at once. A batch reports which changes succeeded
      and which failed, so one inaccessible conversation does not discard the successful
      changes. Interrupted group renames and deletions keep the groups needed by the
      remaining conversations and can be reloaded and retried; group_set manages the
      group catalog and does not move conversations between groups.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The Tasks view does less repeated history reading and checks current permissions
      before returning a page. A conversation with only a few related background tasks
      can also show those tasks while unrelated work is busy elsewhere, and profile
      merges now ask clients to restart pagination so newly accessible tasks are included.
      If accepting a task suggestion fails because its source agent was removed, the
      suggestion stays pending so you can restore that agent and retry it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When a file already contains the change you asked for, the agent now treats
      that as a successful step and continues to the rest of the task, including its
      final answer. Local CLI agents also keep access to their embedded Gateway tools
      after starting a run.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 34-agent-mode-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: agent-mode
  title: 34 Agent Mode changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Replit/2026-09-04-understand-app-usage-with-project-analytics|Understand
  app usage with Project Analytics]]'
- '[[Changes/Runway/2026-09-04-team-is-a-new-self-serve-plan-for-small-teams-that-create-together-in-runway-eve|Introducing
  Team Plan]]'
- '[[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm
  is now available to eligible agents without a separate enablement step…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: agent-mode
title: 34 Agent Mode changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 34 Agent Mode changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Clean, environment-only agent runs using an OpenAI API key can now start through the built-in OpenClaw runtime when the optional Codex runtime is absent. This removes a setup failure before the agent could answer or begin its task, while explicitly chosen runtimes and existing session pins continue to require their selected runtime.

> When the bundled Control UI skill is available to your agent, type /dashboard with what you want to see to request a board for the current session. Choosing Dashboard in the side panel opens the board directly without adding anything to your message. The dashboard guide includes a one-prompt demonstration, and the command uses the bundled Control UI instructions even when a workspace has another skill with that name. A custom skill named dashboard remains available through $dashboard or /skill dashboard , with its slash alias moved to /dashboard_2 .

> Widgets pinned from an agent's global session stay with that agent's board and notify its authorized viewers. Automatically sized HTML widgets keep their content height instead of progressively shrinking, while manual sizes remain yours to set. If creating a visible dashboard session fails, cleanup preserves a newer replacement session and tells you when the original child needs inspection before retrying.

> Searching Sessions can now find matching active or archived conversations beyond the rows already loaded, with Load more sessions bringing in further matches. It searches conversation details such as names, models, status, and agent identity, while transcript search remains a separate way to search the messages themselves. Counts, grouping, and sorting still describe the loaded rows.

> Owner choices move into a compact submenu, sharing and owner details sit together in the chat header, and copied session links use the configured public address even through a local SSH tunnel. Unrelated agent activity no longer repeatedly reloads the selected agent's list, and pinning or renaming another session can continue while a model catalog loads. Opening a chat clears its unread dot immediately, although new activity arriving during the acknowledgement refresh can still briefly be masked.

> Tool activity keeps related calls together after reload and shows a short purpose supplied by the acting agent when one is available, with full commands and results underneath. There are no extra model calls just to name those rows, and the description tells you the intended work while the result tells you whether it succeeded. If your configuration contains the retired gateway.controlUi.toolTitles key, remove it even when its value is false. openclaw doctor --fix handles supported configurations, while managed or included configuration files may need changes at their source.

> Automatic updates now keep enabled skill preferences when a prerequisite happens to be missing from the update environment, and fully repairable older multi-agent configurations retain current choices such as the update channel, port, and original default agent. A failed agent-settings save also keeps the previous complete file readable. Enabled skills still need their prerequisites before they can run, and an explicit standalone Doctor repair can still disable unavailable skills.

> If an intended owner has lost access to restart or update commands because their saved identity uses an older channel:user:id form, run the same explicit Doctor repair to migrate recognized, unambiguous entries. Upgrading alone does not rewrite those owner entries, and ambiguous identities or default-agent choices still need manual correction.

> In supported Slack agent sessions, the native Stop button now reaches the work running in the selected conversation, including overlapping replies in group DMs, while session status shows when the agent is working or waiting for an approval. Rename a supported session in Slack and OpenClaw keeps that name through later messages, with delayed controls checked against the conversation they belong to.

> In Slack compact progress mode , the final answer arrives as a new message after any conversation or media that appeared while the agent worked. Temporary progress is removed after Slack confirms delivery, and a failed send leaves the preview available.

> When Claude Code needs an answer before continuing, its native question can now reach the channel conversation instead of appearing only in the web dashboard. Replying in plain text to that same conversation can answer the waiting question and resume the run, including in installations with several agents. This repairs the existing question workflow, with Telegram directly demonstrated; messages containing media do not use this early plain-text answer path.

> A final answer already delivered to the same external conversation can now suppress the extra automatic reply or same-conversation agent announcement, even when another layer rewrites the tool’s visible output. This depends on confirmed final delivery to that destination; a progress update, a dry run, or a message to another conversation does not count as the answer.

> When an agent has already generated images or other files, a later tool error or reasoning-only response no longer decides which of those attachments survive. The media guide explains how generated files remain available alongside the warning, even when the warning mentions only one of them.

> Skills get practical repairs from creation through installation and remote use. Workshop explains more failed reviews and protects current edits during uncertain restores, while paired and remote workers use the instructions and supporting files prepared for their own turn. Bundled guidance also gives agents a clearer path through dashboard building and delegated work without changing the permissions those tasks require.

> Skill Workshop now identifies conflicting support-file locations before saving a proposal, and refuses proposals or evaluations that would silently omit unreadable or excessively nested content. When agents sharing a workspace cannot start a collection review because a provider credential is missing, the error names the affected provider and agent so the operator can fix authentication without guessing at model settings.

> You can change the thinking level before the next turn while retaining a compatible cached prompt prefix. Automatic compaction, automatic truncation, pro mode, and API multi-agent mode do not support that optimization, and a restart or rewritten history starts a fresh request. Finish pending tool results or approvals in a compatible Astra mode before switching. Where runtime capabilities permit it, /think ultra also enables proactive delegation to sub-agents, using max effort in OpenClaw and xhigh in native Codex.

> The local-server guide now uses llmman , the maintained replacement for Inferrs, with corrected startup commands, readiness checks, and troubleshooting for requests that work directly but fail during a larger agent task. Existing Inferrs documentation links redirect to the new guide. Keep its unauthenticated service on loopback or behind trusted access controls.

> Codex conversations keep the model and account selected for their native thread when you continue them, including imported conversations whose model differs from the agent's default. Fork from here retains the draft and source thread's current model on Codex 0.153 or newer, and an empty native tool catalog no longer makes a supervised conversation look corrupt. Separate Ask OpenClaw conversations also keep separate Codex threads.

> Failed requests with unfinished tool calls now retain the provider's reported usage, served model, and available failure reason when terminal information arrives. Incomplete tools remain blocked, along with later parallel tool completions after the incomplete call. Tiny managed output budgets are raised to the API's 16-token minimum, and explicitly selected agents can use their allowed API model overrides on multi-agent Gateways without requiring a system agent.

> A scheduled agent or script that is allowed to remove its own job can now delete the schedule and still finish its final result. Removing the job yourself continues to cancel it, and removing or disabling a job while it checks a condition prevents that pending check from starting the action. Effects already completed are not undone, and work already handed to the main conversation's heartbeat keeps its own lifecycle.

> Turning off recurring heartbeats no longer drops the spacing and flood limits for event-triggered work, and reloading settings preserves those limits while a turn is running. When OpenClaw refuses a check, its notice explains the reason without requiring verbose mode. Duplicate heartbeat and skill-review monitors can also be reconciled during startup, while large agent fleets avoid repeated heartbeat-summary work in health and status checks.

> A2A tasks that need an execution approval now keep their original task and reply path through the operator's decision, including peers without an outbound URL. Ordinary text such as “Explain /help please” reaches the agent unchanged.

> Direct calls to File Transfer directory tools now give the agent usable filenames and distinguish files from directories. A listing can continue after its last displayed entry, and fetched directories show the saved root and relative paths needed to open the files locally. Large fetched trees remain saved even when only part of their manifest fits in the text result; the result explains how to inspect omitted files, and reports when an unrepresentable path prevents text pagination from advancing.

> Successful individual file fetches also expose both their saved path and a reusable media ID, so an authorized write tool can copy those bytes without guessing at a hidden identifier. Restricted tool sets receive self-contained Bitable and search guidance without being sent to unavailable companion tools. If Bitable creates an application but cannot retrieve its table metadata, the guidance now tells the agent to keep the successfully created application.

> If you run several agents on one Gateway, review their conversation access before upgrading. Where the settings were previously omitted, agents with session tools now gain access to other agents’ conversations, including other users’ transcripts. Choose narrower session visibility, restrict the participating agents, or disable ordinary cross-agent access if that sharing is not what you intend. Alongside this change, approvals follow current permissions through more of a task, switching Gateways retires the previous Gateway’s automatic skill trust, and conversation cleanup preserves data belonging to other agents.

> Agents can now cooperate across one Gateway without first enabling two settings. Omitted tools.sessions.visibility changes from agent to all , and omitted tools.agentToAgent.enabled changes from false to true , allowing agents with the relevant tools to list, read, search, message, and inspect other agents’ sessions. Existing explicit restrictions still apply, but leaving these settings unset on an older installation now permits broader access on upgrade.

> The session visibility settings let you set tools.sessions.visibility to agent for the current agent’s conversations or self for only the current conversation. agent can still include other users’ conversations under that agent. To keep selected agents working together, set an explicit tools.agentToAgent.allow list that includes both the requesting and receiving agents, or set tools.agentToAgent.enabled to false to block ordinary cross-agent access. An omitted or empty allowlist permits all agent pairs when access is enabled, and deleting an agent can empty that list, so check it again after removal.

> Run openclaw security audit to identify agents that retain unrestricted cross-agent session-tool access and see narrowing guidance. These are controls within one trusted Gateway , not isolation from its administrators. Mutually untrusted users need separate Gateways and credentials, ideally under separate OS users or on separate hosts.

> Deleting a conversation now retains current and historical data if the original caller loses authority before the deletion commits. Deleting one agent’s global session also preserves other agents’ saved plugin state and timestamps. Selected-agent global-session reads, delivery, boards, run lookup, search checks, and GitHub publication keep the explicitly selected agent, although retained-global links and unscoped session-list ownership still have separate unresolved cases.

> Swarm lets an agent coordinate several helpers and collect their results, and eligible agents now have it available by default. It remains experimental and follows your existing tool permissions and limits, with an explicit opt-out in Settings → Agents & Tools → Labs → Swarm . OpenClaw Code Mode remains a separate opt-in.

> A failed tool call no longer puts Code Mode into a separate read-only recovery mode. Your agent can read the error, inspect the current files or settings, and make the remaining changes without restarting the conversation or being limited to one further edit. Failed programs are not automatically replayed, and because an earlier call may have partly succeeded, the agent needs to check what already happened before repeating an action. Normal permissions and approvals still apply to every later call.

> You can ask your agent to organize the conversations it is allowed to manage through session tools , including applying the same group, pin, model, or supported setting to as many as 100 sessions at once. A batch reports which changes succeeded and which failed, so one inaccessible conversation does not discard the successful changes. Interrupted group renames and deletions keep the groups needed by the remaining conversations and can be reloaded and retried; group_set manages the group catalog and does not move conversations between groups.

> The Tasks view does less repeated history reading and checks current permissions before returning a page. A conversation with only a few related background tasks can also show those tasks while unrelated work is busy elsewhere, and profile merges now ask clients to restart pagination so newly accessible tasks are included. If accepting a task suggestion fails because its source agent was removed, the suggestion stays pending so you can restore that agent and retry it.

> When a file already contains the change you asked for, the agent now treats that as a successful step and continues to the rest of the task, including its final answer. Local CLI agents also keep access to their embedded Gateway tools after starting a run.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-04 · Runway · [[Changes/Runway/2026-09-04-team-is-a-new-self-serve-plan-for-small-teams-that-create-together-in-runway-eve|Introducing Team Plan]]
- Later: 2026-09-07 · ElevenLabs · [[Changes/ElevenLabs/2026-09-07-javascript-sdk|JavaScript SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-8e79c2&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-34-agent-mode-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-8e79c2%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->