---
card_id: openclaw-2026-09-03-3a68a0
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Memory and Personalization: 19 changes in v2026.9.1
  — Mermaid diagrams now render directly inside conversations in the Control UI…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1141
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: da1c989133ef557d667db3f346d8e6e0df2fb4c455a7e6654d7b9462dbb8cd6f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-3a68a0
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 19 Memory and Personalization changes'
  evidence:
  - quote: Mermaid diagrams now render directly inside conversations in the Control
      UI, Android, iPhone, iPad, and Mac, and Android gains a fuller chat and session
      experience. Updates preserve more of a working setup and stop before a known
      problem becomes a broken restart. When an update does fail, OpenClaw gives you
      a clearer path back to a working installation. Testing also found lower memory
      use and less repeated work while OpenClaw handled long conversations and large
      installations.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Large retained Memory Core event logs now import in bounded resumable batches
      during Doctor instead of migrating one row at a time, reducing upgrade delays
      without changing the automatic migration or database schema.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Memory now keeps rebuildable index work separate from the conversations
      people need to protect. There is a safe reset path that leaves sessions and
      transcripts in place, search avoids needless full rebuilds for healthy or ordinarily
      dirty indexes, legacy retrieval settings survive Doctor upgrades, and long conversations
      retain capture progress through compaction while closed transcript views release
      message text they no longer need.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Built-in Memory now has an explicit openclaw memory reset path that discards
      only rebuildable index data for one agent or every configured agent while preserving
      sessions, transcripts, memory source files, and other durable agent state. It
      asks before acting, requires --yes in non-interactive use, treats an absent
      or empty index as a successful no-op, and refuses to race indexing already in
      progress.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Full reindexes are safer around that path. Replacement caches are bounded
      before publication, failed full rebuilds leave the previously published cache
      intact, a memory change during automatic maintenance gets one retry against
      current content, and abandoned workspace locks can recover after process-ID
      reuse. Recovery messages identify whether an incompatible index belongs to OpenClaw
      or configuration, warn when an explicit rebuild may contact a paid embedding
      provider, and retain the unreadable source path; ordinary replies remain available
      while a legacy index is repaired in the background, and combined memory and
      wiki searches continue to show the affected agent's repair instructions.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The explicit memory reset path removes rebuildable search data while keeping
      durable sources. Conceptual illustration, not a screenshot. Conceptual boundary.
      Confirmation is required; non-interactive use requires --yes. A later rebuild
      may use a paid embedding provider.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: One-shot openclaw memory search commands can reuse a healthy persisted
      index and exit instead of starting indexing work after they already found the
      answer. The command still checks its sources, so a real change starts maintenance
      and becomes searchable rather than leaving the clean state frozen forever.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: When an index is dirty, ordinary memory-file and session changes can be
      applied incrementally while searches remain available instead of repeatedly
      selecting a full rebuild. Workspace discovery also skips symlinked and other
      non-regular memory entries rather than allowing one linked USER.md to abort
      indexing for every regular file.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Running openclaw doctor --fix on an older configuration no longer silently
      drops an agent's knowledge paths or session-memory choices and falls back to
      global defaults. Custom OpenAI-compatible embedding providers can also resolve
      a saved API-key or bearer-token profile before indexing or search, while invalid
      or unavailable bindings stop before a network request rather than selecting
      a different credential.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: On eligible private-chat turns, Active Memory now tells the main model
      when deep recall was intentionally skipped or unavailable, so an absent lookup
      is not mistaken for a successful search that found nothing relevant. The note
      stays bounded and leaves provider errors and sensitive search details out of
      model context.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Memory Core Dreaming also carries an explicitly selected agent through
      deep consolidation in multi-agent setups, letting recalled facts consolidate
      under the right owner instead of silently falling back to append-only storage.
      When no owner is available, that safer append-only fallback remains.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The surrounding runtime reports and installs are more truthful too. Source-run
      Gateways can load compiled OpenAI and Memory Core plugins again, context-free
      harness checks distinguish allowlist, denylist, and disabled-plugin policy from
      a missing installation, and copied hook packs attempt the optional runtime packages
      their handlers need.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Computer input is more faithful to what the agent and user can see. Successful
      typing and key actions on paired macOS Peekaboo nodes report success after the
      action occurs, screenshot-grounded clicks share one bounded frame across unusual
      capture shapes, smaller-Mac Settings can resize and scroll, and multiline WebVNC
      text keeps its line breaks. Windows remote-desktop handoff retains the authenticated
      TightVNC viewer until its replacement is ready, while large macOS CUA Computer
      responses use less temporary memory without changing the existing response limit
      or setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Strict single-message and atomic-batch transcript appends can once again
      omit the documented optional storePath and resolve the selected agent's configured
      or default store. Explicit-environment integrations can create and reopen non-main
      incognito sessions without replacing the process environment, with incognito
      data remaining memory-only. Corrected migration guidance separates public SDK
      exports, retained compatibility imports, injected alternatives, and compatibility
      deadlines without claiming new runtime exports.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: OpenClaw spends less time repeating work you never asked it to do. Long
      conversations and concurrent replies use less CPU and memory in the measured
      workloads, large installations give health checks and session views more room
      to respond, and routine starts, commands, files, worktrees, logs, and remote
      checks shed a long tail of avoidable overhead.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The streaming path also does less work as replies grow. Concurrent long
      replies reuse their prepared text instead of repeatedly rebuilding it, producing
      substantially lower CPU and memory use in the tested workloads while preserving
      tool ordering, corrections, reply targeting, and final media. These measurements
      cover the built-in runtime on defined local workloads rather than model-provider
      latency.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Repeated Code Mode work can reuse bounded warm workers and look up only
      the requested session, cutting preparation and CPU work once those workers are
      warm. Snapshot buffers also move between tool calls without another storage-format
      copy. The warm pools can retain materially more process memory, so this improves
      the measured Code Mode workloads without establishing a general Gateway capacity
      or throughput gain.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Installations with large saved-session histories also keep less conversation
      data in memory and do far less work to count or list sessions, while read-only
      diagnostics stay out of SQLite's writer lifecycle. Retained Control UI assets
      use less memory on constrained ARM64 hosts as well, improving headroom in the
      tested 768 MiB and 1 GiB setups, though 512 MiB without swap can still fail
      when status work overlaps startup.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Local agents can work directly in an existing project directory while their
      instructions and memory remain in OpenClaw's managed workspace. Existing setups
      keep their old behavior unless a separate directory is configured, session-created
      and paired-agent directories still take precedence, and the split-directory
      option is limited to unsandboxed runs.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 19-memory-and-personalization-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: memory
  title: 19 Memory and Personalization changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Midjourney/2026-08-27-using-personalization-moodboards-and-srefs-moodboards-srefs-may-work-best-with-s|Using
  personalization, moodboards and srefs…]]'
- '[[Changes/OpenClaw/2026-08-31-memory-an-eligible-personal-claw-can-recall-relevant-context-from-that-agent-s-o|Memory
  - An eligible personal Claw can recall relevant context from that agent''s…]]'
- '[[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4
  Memory and Personalization changes in v2026.8.2]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: memory
title: 19 Memory and Personalization changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 19 Memory and Personalization changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Mermaid diagrams now render directly inside conversations in the Control UI, Android, iPhone, iPad, and Mac, and Android gains a fuller chat and session experience. Updates preserve more of a working setup and stop before a known problem becomes a broken restart. When an update does fail, OpenClaw gives you a clearer path back to a working installation. Testing also found lower memory use and less repeated work while OpenClaw handled long conversations and large installations.

> Large retained Memory Core event logs now import in bounded resumable batches during Doctor instead of migrating one row at a time, reducing upgrade delays without changing the automatic migration or database schema.

> Memory now keeps rebuildable index work separate from the conversations people need to protect. There is a safe reset path that leaves sessions and transcripts in place, search avoids needless full rebuilds for healthy or ordinarily dirty indexes, legacy retrieval settings survive Doctor upgrades, and long conversations retain capture progress through compaction while closed transcript views release message text they no longer need.

> Built-in Memory now has an explicit openclaw memory reset path that discards only rebuildable index data for one agent or every configured agent while preserving sessions, transcripts, memory source files, and other durable agent state. It asks before acting, requires --yes in non-interactive use, treats an absent or empty index as a successful no-op, and refuses to race indexing already in progress.

> Full reindexes are safer around that path. Replacement caches are bounded before publication, failed full rebuilds leave the previously published cache intact, a memory change during automatic maintenance gets one retry against current content, and abandoned workspace locks can recover after process-ID reuse. Recovery messages identify whether an incompatible index belongs to OpenClaw or configuration, warn when an explicit rebuild may contact a paid embedding provider, and retain the unreadable source path; ordinary replies remain available while a legacy index is repaired in the background, and combined memory and wiki searches continue to show the affected agent's repair instructions.

> The explicit memory reset path removes rebuildable search data while keeping durable sources. Conceptual illustration, not a screenshot. Conceptual boundary. Confirmation is required; non-interactive use requires --yes. A later rebuild may use a paid embedding provider.

> One-shot openclaw memory search commands can reuse a healthy persisted index and exit instead of starting indexing work after they already found the answer. The command still checks its sources, so a real change starts maintenance and becomes searchable rather than leaving the clean state frozen forever.

> When an index is dirty, ordinary memory-file and session changes can be applied incrementally while searches remain available instead of repeatedly selecting a full rebuild. Workspace discovery also skips symlinked and other non-regular memory entries rather than allowing one linked USER.md to abort indexing for every regular file.

> Running openclaw doctor --fix on an older configuration no longer silently drops an agent's knowledge paths or session-memory choices and falls back to global defaults. Custom OpenAI-compatible embedding providers can also resolve a saved API-key or bearer-token profile before indexing or search, while invalid or unavailable bindings stop before a network request rather than selecting a different credential.

> On eligible private-chat turns, Active Memory now tells the main model when deep recall was intentionally skipped or unavailable, so an absent lookup is not mistaken for a successful search that found nothing relevant. The note stays bounded and leaves provider errors and sensitive search details out of model context.

> Memory Core Dreaming also carries an explicitly selected agent through deep consolidation in multi-agent setups, letting recalled facts consolidate under the right owner instead of silently falling back to append-only storage. When no owner is available, that safer append-only fallback remains.

> The surrounding runtime reports and installs are more truthful too. Source-run Gateways can load compiled OpenAI and Memory Core plugins again, context-free harness checks distinguish allowlist, denylist, and disabled-plugin policy from a missing installation, and copied hook packs attempt the optional runtime packages their handlers need.

> Computer input is more faithful to what the agent and user can see. Successful typing and key actions on paired macOS Peekaboo nodes report success after the action occurs, screenshot-grounded clicks share one bounded frame across unusual capture shapes, smaller-Mac Settings can resize and scroll, and multiline WebVNC text keeps its line breaks. Windows remote-desktop handoff retains the authenticated TightVNC viewer until its replacement is ready, while large macOS CUA Computer responses use less temporary memory without changing the existing response limit or setup.

> Strict single-message and atomic-batch transcript appends can once again omit the documented optional storePath and resolve the selected agent's configured or default store. Explicit-environment integrations can create and reopen non-main incognito sessions without replacing the process environment, with incognito data remaining memory-only. Corrected migration guidance separates public SDK exports, retained compatibility imports, injected alternatives, and compatibility deadlines without claiming new runtime exports.

> OpenClaw spends less time repeating work you never asked it to do. Long conversations and concurrent replies use less CPU and memory in the measured workloads, large installations give health checks and session views more room to respond, and routine starts, commands, files, worktrees, logs, and remote checks shed a long tail of avoidable overhead.

> The streaming path also does less work as replies grow. Concurrent long replies reuse their prepared text instead of repeatedly rebuilding it, producing substantially lower CPU and memory use in the tested workloads while preserving tool ordering, corrections, reply targeting, and final media. These measurements cover the built-in runtime on defined local workloads rather than model-provider latency.

> Repeated Code Mode work can reuse bounded warm workers and look up only the requested session, cutting preparation and CPU work once those workers are warm. Snapshot buffers also move between tool calls without another storage-format copy. The warm pools can retain materially more process memory, so this improves the measured Code Mode workloads without establishing a general Gateway capacity or throughput gain.

> Installations with large saved-session histories also keep less conversation data in memory and do far less work to count or list sessions, while read-only diagnostics stay out of SQLite's writer lifecycle. Retained Control UI assets use less memory on constrained ARM64 hosts as well, improving headroom in the tested 768 MiB and 1 GiB setups, though 512 MiB without swap can still fail when status work overlaps startup.

> Local agents can work directly in an existing project directory while their instructions and memory remain in OpenClaw's managed workspace. Existing setups keep their old behavior unless a separate directory is configured, session-created and paired-agent directories still take precedence, and the split-directory option is limited to unsandboxed runs.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration changes in v2026.9.1]] · Collaboration
- [[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile and Desktop changes in v2026.9.1]] · Mobile and Desktop
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
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-09-01 · OpenClaw · [[Changes/OpenClaw/2026-09-01-4-memory-and-personalization-changes-in-v2026-8-2|4 Memory and Personalization changes in v2026.8.2]]
- Later: 2026-09-04 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running sessions on Linux return freed memory to the system instead of holding…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-3a68a0&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-3a68a0%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->