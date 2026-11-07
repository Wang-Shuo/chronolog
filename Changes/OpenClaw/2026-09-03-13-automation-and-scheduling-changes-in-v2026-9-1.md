---
card_id: openclaw-2026-09-03-7d1818
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Automation and Scheduling: 13 changes in v2026.9.1
  — Doctor can now resolve more of the old state that used to leave an installation…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 975
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c1998662fc5ce3e8d111ef3a2a280d86d83dc679312a51324fb12b3de58bbc52
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-7d1818
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 13 Automation and Scheduling changes'
  evidence:
  - quote: Doctor can now resolve more of the old state that used to leave an installation
      stuck between versions, including empty legacy roots and approval stubs, stale
      workspace setup files, malformed scheduled jobs, incomplete Skill Workshop proposals,
      and narrowly safe database, roster, and workspace migrations. Repair stays deliberately
      conservative. Conflicting or populated state remains available for recovery,
      invalid cron jobs go to quarantine with their identity and reason, and successful
      repairs are designed to stay clean on the next pass.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Scheduled work now keeps more of its identity from creation through delivery.
      An automation can begin with the access somebody already configured, make it
      through a restart without quietly becoming a different job, and leave a result
      that is easier to find and understand afterward. Recurring work also gets a
      deliberate choice about missed jobs, while one-time jobs keep their separate
      recovery behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Configured Codex app-server users can create app-backed automations through
      the authenticated connection they already use, without preparing a second OpenClaw
      profile or supplying a separate tool allowlist. Reauthenticating the same endpoint
      keeps the automation usable, while a removed endpoint, changed connection identity,
      unavailable plugin, or newly disallowed app or tool stops before app work and
      leaves an actionable recorded failure.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: 'Operators who do not want stale reminders, digests, or model calls after
      downtime can enable cron.skipMissedJobs: true . On startup, OpenClaw advances
      overdue recurring schedules to their next future occurrence and saves that decision
      before normal scheduling resumes. The setting is opt-in, so leaving it unset
      or false preserves the existing catch-up behavior, and one-time jobs are not
      skipped.'
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: 'With cron.skipMissedJobs enabled, downtime does not trigger a backlog
      of recurring garden reminders. Conceptual illustration, not a screenshot. Conceptual
      timeline. This is opt-in: unset or false retains the existing catch-up behavior.'
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: An Automations link now opens the intended job and highlighted run even
      when that job sits beyond the loaded page or outside the current agent filter,
      with a visible lookup error when it is no longer available. Session-restricted
      operators receive complete pages and accurate totals for the run history they
      are allowed to see, while large name-sorted job lists avoid repeating the same
      locale setup for every comparison.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Schedule and history durations also keep all meaningful units across locales,
      and a settled failure alert appears as delivered, not delivered, or genuinely
      unknown in the live job view. Confirmed non-delivery retains a bounded redacted
      error and the existing in-app fallback, while immutable run-history entries
      remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: openclaw backup disable can find the managed backup after its schedule
      has been renamed or moved beyond the first 200 jobs in a larger automation inventory.
      It follows the schedule's stable declaration identity, so an unrelated automation
      with the same name is left alone.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Pending clicks, typing, and uploads now remain scoped to the selected tab,
      so cancellation does not disrupt unrelated pages or allow the cancelled action
      to run later. Attached-browser automation also survives malformed sessionless
      worker events without taking down the Gateway or its active browser sessions.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Operators can now deny selected destinations across browser access, guarded
      web fetches, and automation webhooks without maintaining a complete allowlist.
      Exact hostnames and wildcard subdomains are rejected before DNS resolution and
      before allow or private-network exceptions, while an absent or empty blocklist
      leaves existing behavior unchanged. This is a destination policy rather than
      a complete browser egress firewall, a wildcard does not cover its apex host,
      and supported Chrome MCP endpoints supplied only through mcpArgs remain outside
      the shipped hostname check.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Automation can now guard one direct config set operation with an expectation
      that the current value is absent or exactly matches supplied JSON. A mismatch
      writes nothing, reveals neither value, and leaves the existing final snapshot
      guard in place for later races. The expectation does not apply to batch or dry-run
      mode, redirected SecretRef writes, or roster updates.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Long-running work gives the agent more useful signals before it goes off
      course. A background command tells Code Mode how to poll for its eventual output,
      early tool-loop warnings reach the model before the blocking threshold, completed
      fallback reports stop delegated work from launching again on the covered CLI
      path, and cleanup can finish even when plugin setup fails.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Command-line automation now fails without guessing. MCP read commands return
      the normal JSON failure document on early errors, agent exec preserves the original
      run failure and exit code when cleanup also fails, and Windows command lookup
      ignores empty PATHEXT entries instead of treating an extensionless file as runnable.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 13-automation-and-scheduling-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: automation-scheduling
  title: 13 Automation and Scheduling changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-08-31-automations-and-scheduling-scheduled-work-comes-together-under-one-name-across-t|Automations
  and Scheduling - Scheduled work comes together under one name across…]]'
- '[[Changes/Codex CLI/2026-09-01-41457-source-proactive-multi-agent-instructions-from-the-model-catalog-copyberry|♯41457
  Source proactive multi-agent instructions from the model catalog @copyberry]]'
- '[[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2
  Automation and Scheduling changes in v2026.8.2]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: automation-scheduling
title: 13 Automation and Scheduling changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Automation and Scheduling changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Doctor can now resolve more of the old state that used to leave an installation stuck between versions, including empty legacy roots and approval stubs, stale workspace setup files, malformed scheduled jobs, incomplete Skill Workshop proposals, and narrowly safe database, roster, and workspace migrations. Repair stays deliberately conservative. Conflicting or populated state remains available for recovery, invalid cron jobs go to quarantine with their identity and reason, and successful repairs are designed to stay clean on the next pass.

> Scheduled work now keeps more of its identity from creation through delivery. An automation can begin with the access somebody already configured, make it through a restart without quietly becoming a different job, and leave a result that is easier to find and understand afterward. Recurring work also gets a deliberate choice about missed jobs, while one-time jobs keep their separate recovery behavior.

> Configured Codex app-server users can create app-backed automations through the authenticated connection they already use, without preparing a second OpenClaw profile or supplying a separate tool allowlist. Reauthenticating the same endpoint keeps the automation usable, while a removed endpoint, changed connection identity, unavailable plugin, or newly disallowed app or tool stops before app work and leaves an actionable recorded failure.

> Operators who do not want stale reminders, digests, or model calls after downtime can enable cron.skipMissedJobs: true . On startup, OpenClaw advances overdue recurring schedules to their next future occurrence and saves that decision before normal scheduling resumes. The setting is opt-in, so leaving it unset or false preserves the existing catch-up behavior, and one-time jobs are not skipped.

> With cron.skipMissedJobs enabled, downtime does not trigger a backlog of recurring garden reminders. Conceptual illustration, not a screenshot. Conceptual timeline. This is opt-in: unset or false retains the existing catch-up behavior.

> An Automations link now opens the intended job and highlighted run even when that job sits beyond the loaded page or outside the current agent filter, with a visible lookup error when it is no longer available. Session-restricted operators receive complete pages and accurate totals for the run history they are allowed to see, while large name-sorted job lists avoid repeating the same locale setup for every comparison.

> Schedule and history durations also keep all meaningful units across locales, and a settled failure alert appears as delivered, not delivered, or genuinely unknown in the live job view. Confirmed non-delivery retains a bounded redacted error and the existing in-app fallback, while immutable run-history entries remain unchanged.

> openclaw backup disable can find the managed backup after its schedule has been renamed or moved beyond the first 200 jobs in a larger automation inventory. It follows the schedule's stable declaration identity, so an unrelated automation with the same name is left alone.

> Pending clicks, typing, and uploads now remain scoped to the selected tab, so cancellation does not disrupt unrelated pages or allow the cancelled action to run later. Attached-browser automation also survives malformed sessionless worker events without taking down the Gateway or its active browser sessions.

> Operators can now deny selected destinations across browser access, guarded web fetches, and automation webhooks without maintaining a complete allowlist. Exact hostnames and wildcard subdomains are rejected before DNS resolution and before allow or private-network exceptions, while an absent or empty blocklist leaves existing behavior unchanged. This is a destination policy rather than a complete browser egress firewall, a wildcard does not cover its apex host, and supported Chrome MCP endpoints supplied only through mcpArgs remain outside the shipped hostname check.

> Automation can now guard one direct config set operation with an expectation that the current value is absent or exactly matches supplied JSON. A mismatch writes nothing, reveals neither value, and leaves the existing final snapshot guard in place for later races. The expectation does not apply to batch or dry-run mode, redirected SecretRef writes, or roster updates.

> Long-running work gives the agent more useful signals before it goes off course. A background command tells Code Mode how to poll for its eventual output, early tool-loop warnings reach the model before the blocking threshold, completed fallback reports stop delegated work from launching again on the covered CLI path, and cleanup can finish even when plugin setup fails.

> Command-line automation now fails without guessing. MCP read commands return the normal JSON failure document on early errors, agent exec preserves the original run failure and exit code when cleanup also fails, and Windows command lookup ignores empty PATHEXT entries instead of treating an extensionless file as runnable.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration changes in v2026.9.1]] · Collaboration
- [[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile and Desktop changes in v2026.9.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-03-3-editor-experience-changes-in-v2026-9-1|3 Editor Experience changes in v2026.9.1]] · Editor Experience
- [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-03-12-account-and-access-changes-in-v2026-9-1|12 Account and Access changes in v2026.9.1]] · Account and Access
- [[Changes/OpenClaw/2026-09-03-several-less-visible-repairs-keep-the-apps-from-failing-around-dependencies-and|Several less visible repairs keep the apps from failing around dependencies…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-09-01 · OpenClaw · [[Changes/OpenClaw/2026-09-01-2-automation-and-scheduling-changes-in-v2026-8-2|2 Automation and Scheduling changes in v2026.8.2]]
- Later: 2026-09-05 · OpenClaw · [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-7d1818&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-7d1818%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->