---
card_id: cline-2026-09-02-e54006
date: '2026-09-02'
description: 'Cline · 2026-09-02 · Other changes: 7 changes in v4.1.17 — ClinePass
  is now surfaced across the app: a card on the account page describing what the plan…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 26c62cf113cda7ad1bdb30bd7db940c5737494116a066338e4b52813b3711179
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-02-e54006
  comparison: ''
  date: '2026-09-02'
  description: 'Cline — v4.1.17: 7 other changes'
  evidence:
  - quote: 'ClinePass is now surfaced across the app: a card on the account page describing
      what the plan covers, a hint in provider settings, and a banner on the home
      screen. Dismissed banners stay dismissed.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: Hook scripts that fail to spawn no longer crash the extension's core process
      and take the running task down with them.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: Pasted provider API keys are now stripped of the invisible characters clipboards
      smuggle in (newlines, zero-width spaces, BOM). A key corrupted that way was
      hidden by the masked field and rejected by the provider with a 401 indistinguishable
      from a genuinely wrong key. Credential rejections now say that the API key is
      the problem and point at its configuration, keeping the provider's raw response
      as a diagnostic tail.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: Restoring a checkpoint now refuses to run when commits were made after
      it, instead of silently knocking them off the branch where only the reflog could
      recover them. Chat-only restore is unaffected.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: '`apply_patch` now preserves a file''s existing CRLF line endings.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: Langfuse tracing now works in released builds. Detection identified the
      OpenTelemetry provider by class name, which minification renames, so tracing
      silently initialized as not ready in every published build while working in
      development.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: Hook execution telemetry now fires; the task id was not threaded into hook
      runner creation, so those events were dropped.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 7-other-changes-in-v4-1-17
  source_release: cline-2026-09-02-v4-1-17-github-381000681-694bbda2
  source_type: github_releases
  theme: uncategorized
  title: 7 other changes in v4.1.17
  type: change
source_release: '[[Releases/Cline/cline-2026-09-02-v4-1-17-github-381000681-694bbda2|cline-2026-09-02-v4-1-17-github-381000681-694bbda2]]'
source_type: github_releases
theme: uncategorized
title: 7 other changes in v4.1.17
type: change
---

<!-- chronolog:begin region="header" -->
# 7 other changes in v4.1.17

**Cline** · 2026-09-02 · Other changes · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.17) · from [[Releases/Cline/cline-2026-09-02-v4-1-17-github-381000681-694bbda2|v4.1.17]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> ClinePass is now surfaced across the app: a card on the account page describing what the plan covers, a hint in provider settings, and a banner on the home screen. Dismissed banners stay dismissed.

> Hook scripts that fail to spawn no longer crash the extension's core process and take the running task down with them.

> Pasted provider API keys are now stripped of the invisible characters clipboards smuggle in (newlines, zero-width spaces, BOM). A key corrupted that way was hidden by the masked field and rejected by the provider with a 401 indistinguishable from a genuinely wrong key. Credential rejections now say that the API key is the problem and point at its configuration, keeping the provider's raw response as a diagnostic tail.

> Restoring a checkpoint now refuses to run when commits were made after it, instead of silently knocking them off the branch where only the reflog could recover them. Chat-only restore is unaffected.

> `apply_patch` now preserves a file's existing CRLF line endings.

> Langfuse tracing now works in released builds. Detection identified the OpenTelemetry provider by class name, which minification renames, so tracing silently initialized as not ready in every published build while working in development.

> Hook execution telemetry now fires; the task id was not threaded into hook runner creation, so those events were dropped.

Source: https://github.com/cline/cline/releases/tag/v4.1.17
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-02-3-model-support-changes-in-v4-1-17|3 Model Support changes in v4.1.17]] · Model Support
- [[Changes/Cline/2026-09-02-2-apps-and-integrations-changes-in-v4-1-17|2 Apps and Integrations changes in v4.1.17]] · Apps and Integrations
- [[Changes/Cline/2026-09-02-aborting-a-task-now-also-cancels-the-delegated-subagents-and-teammates-it-spawne|Aborting a task now also cancels the delegated subagents and teammates it spawned…]] · Agent Mode
- [[Changes/Cline/2026-09-02-cost-estimates-no-longer-appear-in-task-history-for-subscription-billed-tasks-cl|Cost estimates no longer appear in task history for subscription-billed tasks…]] · Pricing Model
- [[Changes/Cline/2026-09-02-global-rules-are-now-also-read-from-cline-rules-which-is-where-the-rules-tab-wri|Global rules are now also read from ~/Cline/Rules, which is where the Rules tab…]] · Developer Workflow
- [[Changes/Cline/2026-09-02-2-account-and-access-changes-in-v4-1-17|2 Account and Access changes in v4.1.17]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-02-e54006&body=Card%3A%20Changes%2FCline%2F2026-09-02-7-other-changes-in-v4-1-17.md%0ACard%20ID%3A%20cline-2026-09-02-e54006%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.17%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->