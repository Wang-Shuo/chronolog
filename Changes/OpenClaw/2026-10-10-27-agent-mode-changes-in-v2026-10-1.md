---
card_id: openclaw-2026-10-10-bde95e
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Agent Mode: 27 changes in v2026.10.1 — Your
  agent can use installed-skill search to find a relevant skill when a task needs
  it, without…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1192
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 67f7371ae5ff9ce8eeb6d00e969ef133db0792749f96ac5faafe0ebd088affad
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-bde95e
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 27 Agent Mode changes'
  evidence:
  - quote: Your agent can use installed-skill search to find a relevant skill when
      a task needs it, without loading the whole skill library into the conversation.
      This works in supported embedded agents, Code Mode and Codex sessions .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: In interactive Code Mode, your agent can save small JSON results and reuse
      them in later cells, follow-up replies and after a restart. Only completed cells
      save their data, and ordinary cell variables still start fresh.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Rules and pins now determine placement, replacing model classification
      and its instructions and Refresh control. Use rules for any placement you previously
      described in column text. Large boards can open while optional PR details arrive
      in the background; a board-only view needs a session or PR-watcher event to
      refresh. Deleting a Sessions board keeps its conversations and Board agent conversation.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: This store is shared across sessions. On a multi-user Gateway, an agent
      with the exact path can also read another session's media there. Other directory
      restrictions remain, and sandboxed tools gain no host-filesystem access.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Authorized, identified participants can react to eligible saved prompts
      and replies without starting another agent turn. Other readers see counts and
      names, and the agent learns about reactions on its next turn. Some imported
      messages cannot receive reactions.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Chat shows Waiting on subagents when an agent has handed off work and its
      delegated agents are still active. Handoff and resumption remain visible with
      tool details hidden, and a link appears when one active direct child can be
      identified in the loaded sidebar. Delegated rows show the assignment and readable
      task titles.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The Control UI and healthy agents can open while eligible large agent databases
      finish checking. Agents still being checked remain unavailable, with retry hints
      for clients that support them; the CLI does not retry automatically. Startup
      probes keep waiting for those checks. Restarts also finish accepted subagent
      cleanup and let deferred databases prepare without waiting for unrelated subagents.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Cancelled replacements or revoked access can restore the previous skill,
      although forcibly stopping a stuck installer may prevent recovery. Disconnected
      devices return an error, and an agent may need to reread an updated skill.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The recurring-job authoring guide helps agents use scripts for repeatable
      checks and bookkeeping. Scripts must throw to record failure; returning an error
      object counts as success.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Accepted follow-up instructions no longer prevent an Agents API task from
      retrying a temporary failure; the next turn reads fresh history. #161444 . Thanks
      @sjf-oa , @sjf .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: With experimental Claws enabled, you can bring an existing configured local
      agent under Claw management while keeping its ID and workspace. Preview the
      migration plan before applying it using the Claws guide . It adopts supported
      settings and selected prompt files, leaving credentials and conversation data
      outside Claw ownership. Removing an adopted Claw retains the original resources,
      but older Claw readers reject the new ownership format.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Experimental Claw migration previews enrollment of an existing configured
      agent and retains its original resources on removal. #162329 . Thanks @Patrick-Erichsen
      , @sasan1200 , @jalehman . Thanks @giodl73-repo for earlier adoption proposals.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Parent agents can wait for queued follow-ups and continue active visible
      or hidden children, with separate answers retained when completions overlap
      or another task starts quickly. A child waiting for a message still needs an
      authorized sender to continue it.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can keep a readable copy of a native-tool conversation in OpenClaw
      using Import to OpenClaw or the sessions import CLI. Repeat imports append unseen
      items when you use the same agent and full source locator. New copies are creator/admin-visible
      drafts when drafts are enabled, otherwise configured defaults apply.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can use guided agents add to recreate a fully deleted agent after cleanup
      finishes, with copied or new sign-in credentials. Starting a Gateway directly
      or in a container also checks whether another Gateway already owns its saved
      data, even on another port; startup may wait up to five minutes before reporting
      the conflict.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: The configuration examples no longer suggest an accidental ten-minute limit
      for an entire agent run. If you copied it into your settings, remove or change
      that override yourself . Multi-agent examples now explain which agent owns the
      data and receives each conversation. After a manual binary upgrade with a legacy
      agent roster, run openclaw doctor --fix before startup; the roster migration
      guide covers configurations split across files.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Doctor can repair supported session ownership and quarantined data, do
      less repeated archive work, and repair writable state with read-only configuration
      . Required configuration edits still belong in the deployment source. Accepted
      settings and repair permissions remain protected, and explicit recovery references
      must verify before repair. If Doctor finishes while the managed Gateway is still
      starting, check openclaw gateway status afterward. Empty-transcript recovery
      can still break another agent's reference to a shared file; keep the originals
      and backups together at their reported paths. See running Doctor .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Telegram replies can use the related photos, forwarded notes and attachments
      together when they are already queued on a busy host or an eligible attachment
      download is slow. Albums keep their arrival order within each chat or topic,
      and successive messages from one sender can queue separately behind a busy agent.
      Collection remains bounded, so late arrivals can still form another turn.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Telegram agents can see supported images sent as files when they have image
      capability . Hyphenated commands remain copyable, deeply nested replies become
      readable text with media links, and rich messages keep explicit numeric user
      mentions. Long single-agent tasks can deliver completed progress messages through
      reply plugins, respecting streaming opt-outs. Progress links remain clickable
      without website preview cards.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Astra preserves completed answers after silent tool results without sending
      them twice. Custom OpenAI-compatible routes can opt into stale-output pruning
      . Image guidance explains replay costs and replacing images with descriptions,
      which removes access to their pixels for that turn. Kimi K3's Code Mode fix
      renames the result-waiting argument to awaitResults on exec , shellexec and
      agents_wait ; callers must replace required , which is now ignored.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can follow an isolated scheduled run from messages through agent activity
      and available billed usage in one trace with diagnostics-otel .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Typed configuration uses models[ref].agentRuntime and agents.defaults.compaction
      instead of the retired per-agent fields. #164586 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Feishu broadcasts and agent selection accept canonical keyed rosters,
      while source types reject retired roster/default fields earlier. #164103 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Guests can again launch private sandboxed helpers, notify their child agents
      and ask agents to rename conversations they created without broad write access.
      Shared work follows the chosen verified participant's permissions and the original
      run's limits, within a shared trust boundary. On multi-user installations, only
      creators or administrators can archive or restore threads; assigned noncreators
      lose those actions after upgrading, including on existing threads.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Workspace saves and recovery wait for durable records before changing files
      or reporting success. Stock persona files stay in the configured agent workspace
      when work runs in a separate project.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Completed native subagent results can return after a user follow-up under
      the original caller's permissions. An ended child's delayed delivery also need
      not hold its parent's completed batch indefinitely; active work still waits.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Configuration errors show which file failed validation and why. If an external
      edit invalidates or removes the file while a change is being applied, the request
      reports an error and keeps the last working runtime settings. Repair the file,
      call config.get , then reapply the change. Pairing lists skip malformed entries,
      reject invalid schema type lists, and keep existing system-agent approval details.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 27-agent-mode-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: agent-mode
  title: 27 Agent Mode changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes
  in v2026.9.9]]'
- '[[Changes/Claude Code/2026-10-09-3-agent-mode-changes-in-v2-1-296|3 Agent Mode
  changes in v2.1.296]]'
- '[[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes
  in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: agent-mode
title: 27 Agent Mode changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 27 Agent Mode changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Your agent can use installed-skill search to find a relevant skill when a task needs it, without loading the whole skill library into the conversation. This works in supported embedded agents, Code Mode and Codex sessions .

> In interactive Code Mode, your agent can save small JSON results and reuse them in later cells, follow-up replies and after a restart. Only completed cells save their data, and ordinary cell variables still start fresh.

> Rules and pins now determine placement, replacing model classification and its instructions and Refresh control. Use rules for any placement you previously described in column text. Large boards can open while optional PR details arrive in the background; a board-only view needs a session or PR-watcher event to refresh. Deleting a Sessions board keeps its conversations and Board agent conversation.

> This store is shared across sessions. On a multi-user Gateway, an agent with the exact path can also read another session's media there. Other directory restrictions remain, and sandboxed tools gain no host-filesystem access.

> Authorized, identified participants can react to eligible saved prompts and replies without starting another agent turn. Other readers see counts and names, and the agent learns about reactions on its next turn. Some imported messages cannot receive reactions.

> Chat shows Waiting on subagents when an agent has handed off work and its delegated agents are still active. Handoff and resumption remain visible with tool details hidden, and a link appears when one active direct child can be identified in the loaded sidebar. Delegated rows show the assignment and readable task titles.

> The Control UI and healthy agents can open while eligible large agent databases finish checking. Agents still being checked remain unavailable, with retry hints for clients that support them; the CLI does not retry automatically. Startup probes keep waiting for those checks. Restarts also finish accepted subagent cleanup and let deferred databases prepare without waiting for unrelated subagents.

> Cancelled replacements or revoked access can restore the previous skill, although forcibly stopping a stuck installer may prevent recovery. Disconnected devices return an error, and an agent may need to reread an updated skill.

> The recurring-job authoring guide helps agents use scripts for repeatable checks and bookkeeping. Scripts must throw to record failure; returning an error object counts as success.

> Accepted follow-up instructions no longer prevent an Agents API task from retrying a temporary failure; the next turn reads fresh history. #161444 . Thanks @sjf-oa , @sjf .

> With experimental Claws enabled, you can bring an existing configured local agent under Claw management while keeping its ID and workspace. Preview the migration plan before applying it using the Claws guide . It adopts supported settings and selected prompt files, leaving credentials and conversation data outside Claw ownership. Removing an adopted Claw retains the original resources, but older Claw readers reject the new ownership format.

> Experimental Claw migration previews enrollment of an existing configured agent and retains its original resources on removal. #162329 . Thanks @Patrick-Erichsen , @sasan1200 , @jalehman . Thanks @giodl73-repo for earlier adoption proposals.

> Parent agents can wait for queued follow-ups and continue active visible or hidden children, with separate answers retained when completions overlap or another task starts quickly. A child waiting for a message still needs an authorized sender to continue it.

> You can keep a readable copy of a native-tool conversation in OpenClaw using Import to OpenClaw or the sessions import CLI. Repeat imports append unseen items when you use the same agent and full source locator. New copies are creator/admin-visible drafts when drafts are enabled, otherwise configured defaults apply.

> You can use guided agents add to recreate a fully deleted agent after cleanup finishes, with copied or new sign-in credentials. Starting a Gateway directly or in a container also checks whether another Gateway already owns its saved data, even on another port; startup may wait up to five minutes before reporting the conflict.

> The configuration examples no longer suggest an accidental ten-minute limit for an entire agent run. If you copied it into your settings, remove or change that override yourself . Multi-agent examples now explain which agent owns the data and receives each conversation. After a manual binary upgrade with a legacy agent roster, run openclaw doctor --fix before startup; the roster migration guide covers configurations split across files.

> Doctor can repair supported session ownership and quarantined data, do less repeated archive work, and repair writable state with read-only configuration . Required configuration edits still belong in the deployment source. Accepted settings and repair permissions remain protected, and explicit recovery references must verify before repair. If Doctor finishes while the managed Gateway is still starting, check openclaw gateway status afterward. Empty-transcript recovery can still break another agent's reference to a shared file; keep the originals and backups together at their reported paths. See running Doctor .

> Telegram replies can use the related photos, forwarded notes and attachments together when they are already queued on a busy host or an eligible attachment download is slow. Albums keep their arrival order within each chat or topic, and successive messages from one sender can queue separately behind a busy agent. Collection remains bounded, so late arrivals can still form another turn.

> Telegram agents can see supported images sent as files when they have image capability . Hyphenated commands remain copyable, deeply nested replies become readable text with media links, and rich messages keep explicit numeric user mentions. Long single-agent tasks can deliver completed progress messages through reply plugins, respecting streaming opt-outs. Progress links remain clickable without website preview cards.

> Astra preserves completed answers after silent tool results without sending them twice. Custom OpenAI-compatible routes can opt into stale-output pruning . Image guidance explains replay costs and replacing images with descriptions, which removes access to their pixels for that turn. Kimi K3's Code Mode fix renames the result-waiting argument to awaitResults on exec , shellexec and agents_wait ; callers must replace required , which is now ignored.

> You can follow an isolated scheduled run from messages through agent activity and available billed usage in one trace with diagnostics-otel .

> Typed configuration uses models[ref].agentRuntime and agents.defaults.compaction instead of the retired per-agent fields. #164586 . Thanks @steipete .

> Feishu broadcasts and agent selection accept canonical keyed rosters, while source types reject retired roster/default fields earlier. #164103 . Thanks @steipete .

> Guests can again launch private sandboxed helpers, notify their child agents and ask agents to rename conversations they created without broad write access. Shared work follows the chosen verified participant's permissions and the original run's limits, within a shared trust boundary. On multi-user installations, only creators or administrators can archive or restore threads; assigned noncreators lose those actions after upgrading, including on existing threads.

> Workspace saves and recovery wait for durable records before changing files or reporting success. Stock persona files stay in the configured agent workspace when work runs in a separate project.

> Completed native subagent results can return after a user follow-up under the original caller's permissions. An ended child's delayed delivery also need not hold its parent's completed batch indefinitely; active work still waits.

> Configuration errors show which file failed validation and why. If an external edit invalidates or removes the file while a change is being applied, the request reports an error and keeps the last working runtime settings. Repair the file, call config.get , then reapply the change. Pairing lists skip malformed entries, reject invalid schema type lists, and keep existing system-agent approval details.

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]]
- Later: 2026-10-12 · ElevenLabs · [[Changes/ElevenLabs/2026-10-12-elevenagents|ElevenAgents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-bde95e&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-27-agent-mode-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-bde95e%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->