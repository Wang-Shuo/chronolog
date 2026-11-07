---
card_id: openclaw-2026-09-08-cecf2d
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Agent Mode: 16 changes in v2026.9.3 — Alongside
  those highlights, Skill Workshop now keeps each agent''s learned skills together
  across…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1160
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7fcdadc0831d4aaf0de943246633467e56bde8a4beaf44f90afb50399f80d678
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-cecf2d
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 16 Agent Mode changes'
  evidence:
  - quote: Alongside those highlights, Skill Workshop now keeps each agent's learned
      skills together across workspaces. The Mac app gains native browser tabs that
      stay open when you switch conversations, and Models settings adds individual
      account controls and supported account ordering.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Source-install tooling moves to pnpm 12.3.4, and workspace template instructions
      clarify bootstrap, backup coverage and identity fields. New workspaces receive
      more direct default agent guidance without rewriting existing personalized files.
      Setup scripts also receive valid JSON when combining QR setup-code options.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Switching agents finishes loading the sidebar even while another conversation
      receives activity, and expanded children remain visible during roster refreshes.
      Running and unread indicators sit beside session icons without obscuring row
      actions or repeating screen-reader announcements. Long action and owner labels
      also remain within their menus. Aggregate session views preserve the conversation’s
      actual agent and database.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Subagent transcripts stay view-only, with a route back to the parent conversation
      and Stop for runs that can be cancelled. Live progress remains in the parent
      conversation, while visible persistent sessions created by an agent stay editable
      in their parent tree.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Agents can publish bounded native reports containing text, metrics, tables,
      charts and links without an HTML frame. Report properties are limited to 8 KiB
      and contain data rather than executable content, and rejected dashboard actions
      show their error immediately.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Eligible updates driven by 2026.9.2 can cross a shared-state schema change
      while the older updater finishes reading its update history. Agent-schema migrations,
      missing state metadata and failed state migrations still require the documented
      external-install and fresh-Doctor recovery path. See schema-bump recovery if
      your update is refused.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Discord persona and bot replies share Markdown formatting, preserving leading
      indentation and expanding mentions after multiline code while leaving names
      inside code literal. Nested Components v2 starter text and forwarded snapshots
      remain readable when the agent joins a thread.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Persistent progress cards keep checklists visible through tool calls and
      clear without erasing unrelated activity. Native subagent progress reaches the
      supported Slack and Discord displays, while inactive cards pause. Progress visibility
      follows its configured setting and retains transport behavior such as iMessage
      typing.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Skill Workshop now gives each agent one persistent collection across its
      workspaces, with full instruction comparisons for suggestions and clearer recovery
      when an old suggestion can no longer be applied.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: A skill your agent learns now belongs to that agent’s Workshop , so moving
      between workspaces no longer means moving the collection along with it. Installed
      skills and suggestions have separate views, keeping what the agent can already
      use distinct from changes awaiting review.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Automatic learning can maintain complete Workshop packages with normal
      file tools while foreground work continues. In auto mode those are direct edits
      without an automatic rollback copy, and completed writes remain if the background
      run later fails or is cancelled. Choose propose mode when you want to review
      each capture before it changes a skill.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: In auto mode, weekly Workshop reviews now run as ordinary isolated automations,
      with file discovery and run history available through that workflow. They review
      the agent’s collection using ordinary file edits, so completed changes remain
      if a later step fails or is cancelled; there is no new whole-collection backup
      or automatic rollback.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Administrators can see each provider account’s credential source and health
      in Models settings, change supported account priority for the selected agent,
      and sign out of one account without disconnecting the others. Clearing a custom
      order removes the saved priority while leaving accounts connected; inherited
      and provider-managed orders explain their restrictions. When an explicitly selected
      account disappears, OpenClaw keeps that choice and offers recovery guidance
      instead of silently choosing another account. Missing environment-backed credentials
      are reported locally, so restore the environment value and reload secrets on
      a running Gateway before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Accepted private monitor notes now survive reply transformations and reach
      the next check without appearing in public replies or notifications. Monitor
      reconciliation yields so other Gateway requests can make progress during startup
      or reload. Doctor can repair known legacy multi-agent job owners, and an unresolved
      owner no longer stops valid jobs from running alongside it. Ambiguous jobs remain
      inspectable and are skipped until their ownership is resolved.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: The Browser panel now lets you follow supported agent pages as they change,
      and the Mac app brings links you open yourself into native tabs beside them.
      The two kinds of tabs share a panel while keeping their own controls and lifetime.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Core handoffs acknowledge settled children, yielded orchestrators can resume
      their original task, and reset or cancellation targets the current child execution.
      If unfinished native child work cannot be cancelled, the conversation remains
      uncleared with an actionable error. Ordinary sub-agents are recommended for
      one or a few tasks, with Swarm reserved in guidance for larger batches.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 16-agent-mode-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: agent-mode
  title: 16 Agent Mode changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-09-07-elevenagents|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-09-07-python-sdk|Python SDK]]'
- '[[Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the|Improved
  /workflows agent detail]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: agent-mode
title: 16 Agent Mode changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Agent Mode changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Alongside those highlights, Skill Workshop now keeps each agent's learned skills together across workspaces. The Mac app gains native browser tabs that stay open when you switch conversations, and Models settings adds individual account controls and supported account ordering.

> Source-install tooling moves to pnpm 12.3.4, and workspace template instructions clarify bootstrap, backup coverage and identity fields. New workspaces receive more direct default agent guidance without rewriting existing personalized files. Setup scripts also receive valid JSON when combining QR setup-code options.

> Switching agents finishes loading the sidebar even while another conversation receives activity, and expanded children remain visible during roster refreshes. Running and unread indicators sit beside session icons without obscuring row actions or repeating screen-reader announcements. Long action and owner labels also remain within their menus. Aggregate session views preserve the conversation’s actual agent and database.

> Subagent transcripts stay view-only, with a route back to the parent conversation and Stop for runs that can be cancelled. Live progress remains in the parent conversation, while visible persistent sessions created by an agent stay editable in their parent tree.

> Agents can publish bounded native reports containing text, metrics, tables, charts and links without an HTML frame. Report properties are limited to 8 KiB and contain data rather than executable content, and rejected dashboard actions show their error immediately.

> Eligible updates driven by 2026.9.2 can cross a shared-state schema change while the older updater finishes reading its update history. Agent-schema migrations, missing state metadata and failed state migrations still require the documented external-install and fresh-Doctor recovery path. See schema-bump recovery if your update is refused.

> Discord persona and bot replies share Markdown formatting, preserving leading indentation and expanding mentions after multiline code while leaving names inside code literal. Nested Components v2 starter text and forwarded snapshots remain readable when the agent joins a thread.

> Persistent progress cards keep checklists visible through tool calls and clear without erasing unrelated activity. Native subagent progress reaches the supported Slack and Discord displays, while inactive cards pause. Progress visibility follows its configured setting and retains transport behavior such as iMessage typing.

> Skill Workshop now gives each agent one persistent collection across its workspaces, with full instruction comparisons for suggestions and clearer recovery when an old suggestion can no longer be applied.

> A skill your agent learns now belongs to that agent’s Workshop , so moving between workspaces no longer means moving the collection along with it. Installed skills and suggestions have separate views, keeping what the agent can already use distinct from changes awaiting review.

> Automatic learning can maintain complete Workshop packages with normal file tools while foreground work continues. In auto mode those are direct edits without an automatic rollback copy, and completed writes remain if the background run later fails or is cancelled. Choose propose mode when you want to review each capture before it changes a skill.

> In auto mode, weekly Workshop reviews now run as ordinary isolated automations, with file discovery and run history available through that workflow. They review the agent’s collection using ordinary file edits, so completed changes remain if a later step fails or is cancelled; there is no new whole-collection backup or automatic rollback.

> Administrators can see each provider account’s credential source and health in Models settings, change supported account priority for the selected agent, and sign out of one account without disconnecting the others. Clearing a custom order removes the saved priority while leaving accounts connected; inherited and provider-managed orders explain their restrictions. When an explicitly selected account disappears, OpenClaw keeps that choice and offers recovery guidance instead of silently choosing another account. Missing environment-backed credentials are reported locally, so restore the environment value and reload secrets on a running Gateway before retrying.

> Accepted private monitor notes now survive reply transformations and reach the next check without appearing in public replies or notifications. Monitor reconciliation yields so other Gateway requests can make progress during startup or reload. Doctor can repair known legacy multi-agent job owners, and an unresolved owner no longer stops valid jobs from running alongside it. Ambiguous jobs remain inspectable and are skipped until their ownership is resolved.

> The Browser panel now lets you follow supported agent pages as they change, and the Mac app brings links you open yourself into native tabs beside them. The two kinds of tabs share a panel while keeping their own controls and lifetime.

> Core handoffs acknowledge settled children, yielded orchestrators can resume their original task, and reset or cancellation targets the current child execution. If unfinished native child work cannot be cancelled, the conversation remains uncleared with an actionable error. Ordinary sub-agents are recommended for one or a few tasks, with Swarm reserved in guidance for larger batches.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
- [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3|10 Mobile and Desktop changes in v2026.9.3]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-08 · Claude Code · [[Changes/Claude Code/2026-09-08-improved-workflows-agent-detail-tool-calls-are-marked-running-failed-or-done-the|Improved /workflows agent detail]]
- Later: 2026-09-09 · Codex CLI · [[Changes/Codex CLI/2026-09-09-6-agent-mode-changes-in-rust-v0-154-0|6 Agent Mode changes in rust-v0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-cecf2d&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-16-agent-mode-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-cecf2d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->