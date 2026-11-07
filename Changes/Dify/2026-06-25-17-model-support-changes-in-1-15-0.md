---
card_id: dify-2026-06-25-be260c
date: '2026-06-25'
description: 'Dify · 2026-06-25 · Model Support: 17 changes in 1.15.0 — Chat Flow
  / Workflow can now stream the model''s reasoning into a dedicated live "thinking"
  panel…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5e6e171c47d94636f5dd641e110ecca8b0ee0f126879b3898f8c6d42fac31cbc
product: dify
product_name: Dify
record:
  card_id: dify-2026-06-25-be260c
  comparison: ''
  date: '2026-06-25'
  description: 'Dify — 1.15.0: 17 Model Support changes'
  evidence:
  - quote: 'Chat Flow / Workflow can now stream the model''s reasoning into a dedicated
      live "thinking" panel while keeping the final answer clean and readable. The
      reasoning is preserved so it''s still there after a page refresh, and the same
      reasoning is visible in CLI and workflow run previews (#37460, #37828)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '**Support for slow, long-running models**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'Workflows can now use generation models that take a long time to respond
      (such as image or video generation) via a polling mechanism: the node patiently
      waits for the final result instead of timing out (#37462)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '> **One-time legacy model type migration for self-hosted upgrades**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '> This migration is **not included in `flask db upgrade`**. Without it,
      legacy model records can cause model-related API requests to fail with errors,
      preventing affected models from being loaded or used.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: After applying the migration, run the dry-run command again. If it reports
      no additional row updates or deletions, restart the relevant services and verify
      that existing models can be loaded and invoked successfully.
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: hide model provider setting in default model setting by @iamjoel
      in https://github.com/langgenius/dify/pull/36383'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor: add missing @override decorators to TypeDecorator subclasses
      in models/types.py by @zhang-liz in https://github.com/langgenius/dify/pull/36565'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(api): introduce model-type migration script by @QuantumGhost in https://github.com/langgenius/dify/pull/36520'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore(api): polishhelp output for legacy-model-types migration script
      by @QuantumGhost in https://github.com/langgenius/dify/pull/36707'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: dep inject for model by @asukaminato0721 in https://github.com/langgenius/dify/pull/36750'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: split trial models to a single API by @hjlarry in https://github.com/langgenius/dify/pull/36796'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(web): migrate code generator model storage by @popsiclelmlm in
      https://github.com/langgenius/dify/pull/37195'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(api): LLM polling support by @QuantumGhost in https://github.com/langgenius/dify/pull/37462'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(chatflow): stream LLM reasoning to a live thinking panel by @lin-snow
      in https://github.com/langgenius/dify/pull/37460'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat: surface separated-mode LLM reasoning in CLI and workflow run preview
      by @lin-snow in https://github.com/langgenius/dify/pull/37828'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(test): replace SimpleNamespace with real UploadFile model in
      test_dataset_models.py by @manan-tech in https://github.com/langgenius/dify/pull/37935'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 17-model-support-changes-in-1-15-0
  source_release: dify-2026-06-25-1-15-0-github-344699591-4dd01045
  source_type: github_releases
  theme: model-support
  title: 17 Model Support changes in 1.15.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-06-24-core-hid-gpt-5-5-pro-when-using-codex-oauth|Core
  Hid gpt-5.5-pro when using Codex OAuth]]'
- '[[Changes/Claude Code/2026-06-25-added-claude-code-assistant-response-opentelemetry-log-event-containing-the-mode|Added
  claude_code.assistant_response OpenTelemetry log event containing…]]'
- '[[Changes/Codex CLI/2026-06-25-4-model-support-changes-in-rust-v0-142-2|4 Model
  Support changes in rust-v0.142.2]]'
source_release: '[[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|dify-2026-06-25-1-15-0-github-344699591-4dd01045]]'
source_type: github_releases
theme: model-support
title: 17 Model Support changes in 1.15.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Model Support changes in 1.15.0

**Dify** · 2026-06-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.15.0) · from [[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Chat Flow / Workflow can now stream the model's reasoning into a dedicated live "thinking" panel while keeping the final answer clean and readable. The reasoning is preserved so it's still there after a page refresh, and the same reasoning is visible in CLI and workflow run previews (#37460, #37828)

> **Support for slow, long-running models**

> Workflows can now use generation models that take a long time to respond (such as image or video generation) via a polling mechanism: the node patiently waits for the final result instead of timing out (#37462)

> > **One-time legacy model type migration for self-hosted upgrades**

> > This migration is **not included in `flask db upgrade`**. Without it, legacy model records can cause model-related API requests to fail with errors, preventing affected models from being loaded or used.

> After applying the migration, run the dry-run command again. If it reports no additional row updates or deletions, restart the relevant services and verify that existing models can be loaded and invoked successfully.

> chore: hide model provider setting in default model setting by @iamjoel in https://github.com/langgenius/dify/pull/36383

> refactor: add missing @override decorators to TypeDecorator subclasses in models/types.py by @zhang-liz in https://github.com/langgenius/dify/pull/36565

> feat(api): introduce model-type migration script by @QuantumGhost in https://github.com/langgenius/dify/pull/36520

> chore(api): polishhelp output for legacy-model-types migration script by @QuantumGhost in https://github.com/langgenius/dify/pull/36707

> chore: dep inject for model by @asukaminato0721 in https://github.com/langgenius/dify/pull/36750

> chore: split trial models to a single API by @hjlarry in https://github.com/langgenius/dify/pull/36796

> refactor(web): migrate code generator model storage by @popsiclelmlm in https://github.com/langgenius/dify/pull/37195

> feat(api): LLM polling support by @QuantumGhost in https://github.com/langgenius/dify/pull/37462

> feat(chatflow): stream LLM reasoning to a live thinking panel by @lin-snow in https://github.com/langgenius/dify/pull/37460

> feat: surface separated-mode LLM reasoning in CLI and workflow run preview by @lin-snow in https://github.com/langgenius/dify/pull/37828

> refactor(test): replace SimpleNamespace with real UploadFile model in test_dataset_models.py by @manan-tech in https://github.com/langgenius/dify/pull/37935

Source: https://github.com/langgenius/dify/releases/tag/1.15.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-06-25-6-interface-experience-changes-in-1-15-0|6 Interface Experience changes in 1.15.0]] · Interface Experience
- [[Changes/Dify/2026-06-25-38-agent-mode-changes-in-1-15-0|38 Agent Mode changes in 1.15.0]] · Agent Mode
- [[Changes/Dify/2026-06-25-14-safety-and-privacy-changes-in-1-15-0|14 Safety and Privacy changes in 1.15.0]] · Safety and Privacy
- [[Changes/Dify/2026-06-25-refactor-inject-session-into-audio-tts-by-myshkin451-in-https-github-com-langgen|refactor: inject session into audio TTS]] · Voice and Audio
- [[Changes/Dify/2026-06-25-2-reliability-and-performance-changes-in-1-15-0|2 Reliability and Performance changes in 1.15.0]] · Reliability and Performance
- [[Changes/Dify/2026-06-25-3-context-window-changes-in-1-15-0|3 Context Window changes in 1.15.0]] · Context Window
- [[Changes/Dify/2026-06-25-install-it-on-any-platform-macos-linux-windows-with-a-single-command-and-no-acce|Install it on any platform (macOS, Linux, Windows) with a single command and no…]] · Mobile and Desktop
- [[Changes/Dify/2026-06-25-numerous-web-ui-and-accessibility-focus-ring-polish-fixes|Numerous web UI and accessibility/focus-ring polish fixes]] · Accessibility and Localization
- [[Changes/Dify/2026-06-25-6-pricing-model-changes-in-1-15-0|6 Pricing Model changes in 1.15.0]] · Pricing Model
- [[Changes/Dify/2026-06-25-9-developer-workflow-changes-in-1-15-0|9 Developer Workflow changes in 1.15.0]] · Developer Workflow
- [[Changes/Dify/2026-06-25-6-files-and-data-changes-in-1-15-0|6 Files and Data changes in 1.15.0]] · Files and Data
- [[Changes/Dify/2026-06-25-5-account-and-access-changes-in-1-15-0|5 Account and Access changes in 1.15.0]] · Account and Access
- [[Changes/Dify/2026-06-25-6-collaboration-changes-in-1-15-0|6 Collaboration changes in 1.15.0]] · Collaboration
- [[Changes/Dify/2026-06-25-27-apps-and-integrations-changes-in-1-15-0|27 Apps and Integrations changes in 1.15.0]] · Apps and Integrations
- [[Changes/Dify/2026-06-25-2-automation-and-scheduling-changes-in-1-15-0|2 Automation and Scheduling changes in 1.15.0]] · Automation and Scheduling
- [[Changes/Dify/2026-06-25-3-editor-experience-changes-in-1-15-0|3 Editor Experience changes in 1.15.0]] · Editor Experience
- [[Changes/Dify/2026-06-25-365-other-changes-in-1-15-0|365 other changes in 1.15.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-4-model-support-changes-in-rust-v0-142-2|4 Model Support changes in rust-v0.142.2]]
- Later: 2026-06-25 · Google Antigravity · [[Changes/Google Antigravity/2026-06-25-improved-the-model-selector-dropdown-to-dynamically-resize-and-prevent-truncatio|Improved the model selector dropdown to dynamically resize and prevent truncation…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-06-25-be260c&body=Card%3A%20Changes%2FDify%2F2026-06-25-17-model-support-changes-in-1-15-0.md%0ACard%20ID%3A%20dify-2026-06-25-be260c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.15.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->