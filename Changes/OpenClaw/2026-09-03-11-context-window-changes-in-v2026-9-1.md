---
card_id: openclaw-2026-09-03-d2c686
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Context Window: 11 changes in v2026.9.1 — The
  chat transcript now holds together more consistently as live events become saved
  history…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2542
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5b953457e13c9198b4d2aa14d900d9fc5dbacf79f2410a6f8a87e1b2a337e611
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-d2c686
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 11 Context Window changes'
  evidence:
  - quote: The chat transcript now holds together more consistently as live events
      become saved history. Reconnects and refreshes keep one copy of a completed
      answer, queued prompts stay above the replies they produced, commentary remains
      distinct from the final answer, and manually taking over the scroll position
      is less likely to be undone by delayed layout work. Compaction now appears as
      one calm inline marker that settles into a durable completed state instead of
      splitting itself across temporary and saved notices.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Updates now make a clearer distinction between work OpenClaw can finish
      safely and work that needs your attention first. The updater protects more of
      the setup already on the machine, hands service-owned restarts to a process
      that can survive them, and leaves recoverable failures with enough context for
      Doctor or a configured coding agent to take over the investigation.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: A bounded, sanitized failure record carries useful context into the triage
      conversation. Conceptual illustration, not a screenshot. Conceptual flow. JSON,
      --yes, background, and managed-service runs remain diagnostic-only.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: When delivery cannot finish, the result is now less ambiguous. Rejected
      webhook uploads across bundled channels receive their complete response before
      the connection closes, malformed Signal response text fails visibly, and an
      affected iMessage send explains that its bridge stopped responding and gives
      the operator the two recovery commands. Context-only prompts no longer hang
      at completion, while Discord thread replies split after mention expansion and
      avoid replaying an uncertain or partially accepted webhook delivery as a duplicate
      bot message.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The recovery details matter just as much as the retry count. Affected llama.cpp
      context-limit failures can compact and retry, OpenAI Responses conversations
      keep compact continuation when tool lists or safely admitted large-integer arguments
      change, and pre-output transport failures can resume after completed tools without
      running them again. Provider and context diagnostics now survive more of these
      paths, while the official failover guide matches the controller that actually
      owns them.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: New Browser Talk conversations also keep the internal consultation question,
      context, and speaking instructions out of later model turns while preserving
      genuine speech, assistant results, and lossless exports. Existing unflagged
      records are not rewritten, and the separate decision about how a consultation
      answer should be presented remains open.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Authorized operators can also rotate or revoke approved scoped node tokens
      through openclaw devices . The operation cannot add a role or widen the approved
      scope baseline, under-scoped callers remain blocked, and operator-token operations
      with broader stored scopes may still require a broader authenticated connection.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Underneath that workflow, nested session writes remain ordered, malformed
      cyclic ancestry returns bounded context instead of hanging, and a stale local
      CLI recovery attempt can no longer replace a newer session. Older canonical
      messages without recorded native provenance remain outside the new fork path.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Interrupted work now keeps its shape through restart and cleanup. A user
      message interrupted by a Gateway restart remains in later model context, cloud-session
      cleanup failures stay visible and retryable without discarding accepted workspace
      changes, and retried agent or CLI commands remain attached to the process tree
      that actually owns their cancellation, output, and diagnostics.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Status and logs now make a problem visible without overstating what is
      healthy. Detailed status reports show inbound queue pressure and dead letters
      even when channel connectivity looks fine, usage requests reject unsupported
      fixed offsets instead of returning totals for the wrong day, and Telegram and
      TUI status retain known context usage after tool-only turns.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Two narrower channel fixes remove behavior that depended on the wrong condition.
      Native /compact now gives an explicit authorization refusal without starting
      compaction work when the sender is not allowed to use it, while Buzz applies
      stable event ordering when profile or room updates share a timestamp instead
      of letting arrival order decide which state wins.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 11-context-window-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: context-window
  title: 11 Context Window changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Ollama/2026-09-02-report-cached-prompt-tokens|Report cached prompt tokens]]'
- '[[Changes/Claude Code/2026-09-03-3-context-window-changes-in-v2-1-260|3 Context
  Window changes in v2.1.260]]'
- '[[Changes/Codex CLI/2026-09-03-6-context-window-changes-in-rust-v0-153-0|6 Context
  Window changes in rust-v0.153.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: context-window
title: 11 Context Window changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Context Window changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The chat transcript now holds together more consistently as live events become saved history. Reconnects and refreshes keep one copy of a completed answer, queued prompts stay above the replies they produced, commentary remains distinct from the final answer, and manually taking over the scroll position is less likely to be undone by delayed layout work. Compaction now appears as one calm inline marker that settles into a durable completed state instead of splitting itself across temporary and saved notices.

> Updates now make a clearer distinction between work OpenClaw can finish safely and work that needs your attention first. The updater protects more of the setup already on the machine, hands service-owned restarts to a process that can survive them, and leaves recoverable failures with enough context for Doctor or a configured coding agent to take over the investigation.

> A bounded, sanitized failure record carries useful context into the triage conversation. Conceptual illustration, not a screenshot. Conceptual flow. JSON, --yes, background, and managed-service runs remain diagnostic-only.

> When delivery cannot finish, the result is now less ambiguous. Rejected webhook uploads across bundled channels receive their complete response before the connection closes, malformed Signal response text fails visibly, and an affected iMessage send explains that its bridge stopped responding and gives the operator the two recovery commands. Context-only prompts no longer hang at completion, while Discord thread replies split after mention expansion and avoid replaying an uncertain or partially accepted webhook delivery as a duplicate bot message.

> The recovery details matter just as much as the retry count. Affected llama.cpp context-limit failures can compact and retry, OpenAI Responses conversations keep compact continuation when tool lists or safely admitted large-integer arguments change, and pre-output transport failures can resume after completed tools without running them again. Provider and context diagnostics now survive more of these paths, while the official failover guide matches the controller that actually owns them.

> New Browser Talk conversations also keep the internal consultation question, context, and speaking instructions out of later model turns while preserving genuine speech, assistant results, and lossless exports. Existing unflagged records are not rewritten, and the separate decision about how a consultation answer should be presented remains open.

> Authorized operators can also rotate or revoke approved scoped node tokens through openclaw devices . The operation cannot add a role or widen the approved scope baseline, under-scoped callers remain blocked, and operator-token operations with broader stored scopes may still require a broader authenticated connection.

> Underneath that workflow, nested session writes remain ordered, malformed cyclic ancestry returns bounded context instead of hanging, and a stale local CLI recovery attempt can no longer replace a newer session. Older canonical messages without recorded native provenance remain outside the new fork path.

> Interrupted work now keeps its shape through restart and cleanup. A user message interrupted by a Gateway restart remains in later model context, cloud-session cleanup failures stay visible and retryable without discarding accepted workspace changes, and retried agent or CLI commands remain attached to the process tree that actually owns their cancellation, output, and diagnostics.

> Status and logs now make a problem visible without overstating what is healthy. Detailed status reports show inbound queue pressure and dead letters even when channel connectivity looks fine, usage requests reject unsupported fixed offsets instead of returning totals for the wrong day, and Telegram and TUI status retain known context usage after tool-only turns.

> Two narrower channel fixes remove behavior that depended on the wrong condition. Native /compact now gives an explicit authorization refusal without starting compaction work when the sender is not allowed to use it, while Buzz applies stable event ordering when profile or room updates share a timestamp instead of letting arrival order decide which state wins.

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
- [[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13 Automation and Scheduling changes in v2026.9.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-6-context-window-changes-in-rust-v0-153-0|6 Context Window changes in rust-v0.153.0]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-changed-context-token-counting-to-use-a-local-estimate-when-the-token-counting-a|Changed /context token counting to use a local estimate when the token-counting…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-d2c686&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-11-context-window-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-d2c686%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->