---
card_id: cline-2026-08-21-e269fc
date: '2026-08-21'
description: 'Cline · 2026-08-21 · Other changes: 8 changes in v4.1.11 — Continue
  the surviving session when resuming a task, instead of rebuilding it from the original
  task…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 65c8ca1757420b5c3a0a9f397762c6fd7b67486518684cecb1bc69abb218234e
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-21-e269fc
  comparison: ''
  date: '2026-08-21'
  description: 'Cline — v4.1.11: 8 other changes'
  evidence:
  - quote: Continue the surviving session when resuming a task, instead of rebuilding
      it from the original task text.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Clear the task-scoped settings overlay when the task view is cleared or
      switched, so one task's overrides no longer leak into the next.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Honor the classic truncation range when migrating legacy tasks.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Preserve LiteLLM input token limits instead of overwriting them with catalog
      values.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Point provider signup links at each provider's API key page instead of
      a generic landing page.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Load skill slash commands through the skills tool instead of pasting their
      instructions into your message, which previously delivered them twice.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Show tool activity a provider runs itself — every tool the Claude Code
      provider executes inside its own session — instead of dropping it from the conversation.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  - quote: Run PowerShell commands fail-fast, so a pipeline erroring per item stops
      at the first error instead of flooding output and still reporting success.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.11
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 8-other-changes-in-v4-1-11
  source_release: cline-2026-08-21-v4-1-11-github-374187578-938b5fa5
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in v4.1.11
  type: change
source_release: '[[Releases/Cline/cline-2026-08-21-v4-1-11-github-374187578-938b5fa5|cline-2026-08-21-v4-1-11-github-374187578-938b5fa5]]'
source_type: github_releases
theme: uncategorized
title: 8 other changes in v4.1.11
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v4.1.11

**Cline** · 2026-08-21 · Other changes · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.11) · from [[Releases/Cline/cline-2026-08-21-v4-1-11-github-374187578-938b5fa5|v4.1.11]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Continue the surviving session when resuming a task, instead of rebuilding it from the original task text.

> Clear the task-scoped settings overlay when the task view is cleared or switched, so one task's overrides no longer leak into the next.

> Honor the classic truncation range when migrating legacy tasks.

> Preserve LiteLLM input token limits instead of overwriting them with catalog values.

> Point provider signup links at each provider's API key page instead of a generic landing page.

> Load skill slash commands through the skills tool instead of pasting their instructions into your message, which previously delivered them twice.

> Show tool activity a provider runs itself — every tool the Claude Code provider executes inside its own session — instead of dropping it from the conversation.

> Run PowerShell commands fail-fast, so a pipeline erroring per item stops at the first error instead of flooding output and still reporting success.

Source: https://github.com/cline/cline/releases/tag/v4.1.11
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-21-stop-offering-image-voice-and-other-non-chat-models-in-chat-model-pickers|Stop offering image, voice, and other non-chat models in chat model pickers]] · Voice and Audio
- [[Changes/Cline/2026-08-21-only-treat-an-anthropic-invalid-request-error-as-a-context-overflow-when-its-mes|Only treat an Anthropic invalid_request_error as a context-overflow…]] · Context Window
- [[Changes/Cline/2026-08-21-let-models-that-support-it-generate-images-during-a-task-generated-images-render|Let models that support it generate images during a task]] · Image Generation
- [[Changes/Cline/2026-08-21-show-the-billed-cost-for-cline-gateway-usage|Show the billed cost for Cline gateway usage]] · Pricing Model
- [[Changes/Cline/2026-08-21-show-the-diff-edit-view-for-multi-line-edits-in-files-with-crlf-line-endings|Show the diff edit view for multi-line edits in files with CRLF line endings]] · Editor Experience
- [[Changes/Cline/2026-08-21-3-model-support-changes-in-v4-1-11|3 Model Support changes in v4.1.11]] · Model Support
- [[Changes/Cline/2026-08-21-2-apps-and-integrations-changes-in-v4-1-11|2 Apps and Integrations changes in v4.1.11]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-21-e269fc&body=Card%3A%20Changes%2FCline%2F2026-08-21-8-other-changes-in-v4-1-11.md%0ACard%20ID%3A%20cline-2026-08-21-e269fc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.11%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->