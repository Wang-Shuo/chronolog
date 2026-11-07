---
card_id: openclaw-2026-09-08-223e05
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Memory and Personalization: 10 changes in v2026.9.3
  — Large Git backups and restores use bounded batches, reducing the need to hold…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1146
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9b946f6087c7319e3d80ae24055d0eb77bfe4620a1e275a31fe184a35d4234c3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-223e05
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 10 Memory and Personalization changes'
  evidence:
  - quote: Large Git backups and restores use bounded batches, reducing the need to
      hold complete database tables in memory while keeping verification checks. State-only
      backups leave shared-workspace scratch out of the archive, and oversized required
      Git output produces an error instead of a partially parsed history.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Memory search keeps useful notes available through more backend failures
      and long-running conversations, while exact filenames, older notes and readable
      excerpts are easier to recover. Native vector searches also spend less work
      starting up, with the improvement scoped to that search path.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Published memory remains searchable while changed-file writes and cleanup
      contend for database access. Deadline recovery can return memory-file keyword
      hits with a warning, while session hits remain outside that fallback. Large
      state replacements and clears also yield between batches so other queued work
      can proceed.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: When results may be stale, Memories shows the existing rebuild command
      with its warning. Exhausted file-watcher capacity falls back to the existing
      synchronization path, although an initial search may still use the previous
      index while that refresh finishes.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Adding messages to a long conversation now resumes memory import from the
      previously verified position, avoiding repeated imports of earlier messages.
      Existing memory history stays intact, while edits and truncations still trigger
      a conservative rescan.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: OpenClaw-managed compaction accounts for the full incoming request once
      that context is prepared, and background memory work stays separate from human
      prompts. Cold sessions use their prepared model’s context limits while honoring
      smaller explicit caps, and transcript growth after the last provider report
      contributes to fresh accounting.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: In the built-in agent loop, cancelled or failed tool turns no longer commit
      unfinished exchanges to context-engine memory. Native runtimes retain their
      own compaction behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Cited excerpts keep the leading spaces and tabs that make code and structured
      notes readable. Profile workspaces and Termux home paths are honored by memory-host
      lookups, while command JSON distinguishes a disabled backend, a backend that
      failed to open, and a successful search with no results.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Small excerpts from large notes can be selected in one forward pass while
      preserving continuation offsets and the existing output budget. Memory Wiki
      pages without link brackets skip unnecessary link parsing, and indexing reuses
      prepared database statements within each nonempty file.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Maintainer references describe review commands, release operations, and
      validation ownership more clearly. Translation-memory and glossary updates support
      the documentation and localization process without implying that every tooling
      update changes visible app text.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-memory-and-personalization-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: memory
  title: 10 Memory and Personalization changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-04-long-running-sessions-on-linux-return-freed-memory-to-the-system-instead-of-hold|Long-running
  sessions on Linux return freed memory to the system instead of holding…]]'
- '[[Changes/Superwhisper/2026-09-04-lower-memory-use-during-long-recordings|Lower
  memory use during long recordings]]'
- '[[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21
  Memory and Personalization changes in v2026.9.2]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: memory
title: 10 Memory and Personalization changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Memory and Personalization changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Large Git backups and restores use bounded batches, reducing the need to hold complete database tables in memory while keeping verification checks. State-only backups leave shared-workspace scratch out of the archive, and oversized required Git output produces an error instead of a partially parsed history.

> Memory search keeps useful notes available through more backend failures and long-running conversations, while exact filenames, older notes and readable excerpts are easier to recover. Native vector searches also spend less work starting up, with the improvement scoped to that search path.

> Published memory remains searchable while changed-file writes and cleanup contend for database access. Deadline recovery can return memory-file keyword hits with a warning, while session hits remain outside that fallback. Large state replacements and clears also yield between batches so other queued work can proceed.

> When results may be stale, Memories shows the existing rebuild command with its warning. Exhausted file-watcher capacity falls back to the existing synchronization path, although an initial search may still use the previous index while that refresh finishes.

> Adding messages to a long conversation now resumes memory import from the previously verified position, avoiding repeated imports of earlier messages. Existing memory history stays intact, while edits and truncations still trigger a conservative rescan.

> OpenClaw-managed compaction accounts for the full incoming request once that context is prepared, and background memory work stays separate from human prompts. Cold sessions use their prepared model’s context limits while honoring smaller explicit caps, and transcript growth after the last provider report contributes to fresh accounting.

> In the built-in agent loop, cancelled or failed tool turns no longer commit unfinished exchanges to context-engine memory. Native runtimes retain their own compaction behavior.

> Cited excerpts keep the leading spaces and tabs that make code and structured notes readable. Profile workspaces and Termux home paths are honored by memory-host lookups, while command JSON distinguishes a disabled backend, a backend that failed to open, and a successful search with no results.

> Small excerpts from large notes can be selected in one forward pass while preserving continuation offsets and the existing output budget. Memory Wiki pages without link brackets skip unnecessary link parsing, and indexing reuses prepared database statements within each nonempty file.

> Maintainer references describe review commands, release operations, and validation ownership more clearly. Translation-memory and glossary updates support the documentation and localization process without implying that every tooling update changes visible app text.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
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
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
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
## Nearby in Memory and Personalization

- Earlier: 2026-09-05 · OpenClaw · [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]]
- Later: 2026-09-09 · Codex CLI · [[Changes/Codex CLI/2026-09-09-2-memory-and-personalization-changes-in-rust-v0-154-0|2 Memory and Personalization changes in rust-v0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-223e05&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-223e05%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->