---
card_id: openclaw-2026-09-23-909dfe
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Files and Data: 6 changes in v2026.9.6 — Authored
  section links now scroll within the displayed document, including strict previews…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode
    offset]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2562
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 83c9951caf491484781122858ba017eea4fc1946c3c11abd798a460373a112fc
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-909dfe
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 6 Files and Data changes'
  evidence:
  - quote: Authored section links now scroll within the displayed document, including
      strict previews, without losing form values. Links created later by scripts
      are outside this change.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Keep the remote Skills connection in place until its tasks finish. Replacing
      it with a document-only connection while a task retains its remote skill list
      can make that task read supporting files from the Gateway computer instead.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When using an existing Chrome session , captured references now survive
      condition waits within the same document, and the packaged helper supports controls
      across cross-origin frames. Navigation still retires references from the replaced
      document, so take a fresh snapshot before acting again. The default helper ships
      with OpenClaw and no longer needs an npm download at browser startup. Native
      coordinate input supports left and double clicks; right or middle clicks and
      nonzero click delays require a managed profile. A missing target is never silently
      replaced with another tab.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: PDF extraction keeps images of low-text or visual-only pages alongside
      selectable text, so a text-rich page no longer hides a neighboring diagram or
      scanned page. This affects extraction fallback; native Anthropic and Google
      PDF input is unchanged. More rendered pages can increase image-token charges,
      while the existing 20-page default selection, 200,000-character text cap, and
      shared four-million-pixel budget remain.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The 2026.9.1 release guide gains interface illustrations and labeled conceptual
      examples to explain that older release. The figures document existing capabilities,
      with fictional and conceptual examples identified as such.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Stopping a chat turn now interrupts optional idle waits and affected cleanup
      reads that were waiting on a stalled history rebuild. Required saves and cleanup
      still run, saved answers and attachment references remain intact, and an interrupted
      delivery check stays pending until its outcome is known. Completions canceled
      during connection setup now stop before contacting the provider, and PDF or
      image-analysis fallbacks also stop if their prepared resources are no longer
      valid. Requests already sent retain their existing cancellation limits.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 6-files-and-data-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: file-data
  title: 6 Files and Data changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-22-fewer-link-cards-you-did-not-ask-for-the-agent-surfaces-a-link-card-in-the-conve|Fewer
  link cards you did not ask for]]'
- '[[Changes/OpenHands/2026-09-22-docs-codereview-clarify-agent-canvas-checkpoints-by-neubig-in-https-github-com-o|docs(codereview):
  clarify Agent Canvas checkpoints]]'
- '[[Changes/OpenHands/2026-09-22-docs-review-add-repository-and-product-scope-to-the-canvas-review-guide-by-all-h|docs(review):
  add repository and product scope to the Canvas review guide]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: file-data
title: 6 Files and Data changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Files and Data changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Authored section links now scroll within the displayed document, including strict previews, without losing form values. Links created later by scripts are outside this change.

> Keep the remote Skills connection in place until its tasks finish. Replacing it with a document-only connection while a task retains its remote skill list can make that task read supporting files from the Gateway computer instead.

> When using an existing Chrome session , captured references now survive condition waits within the same document, and the packaged helper supports controls across cross-origin frames. Navigation still retires references from the replaced document, so take a fresh snapshot before acting again. The default helper ships with OpenClaw and no longer needs an npm download at browser startup. Native coordinate input supports left and double clicks; right or middle clicks and nonzero click delays require a managed profile. A missing target is never silently replaced with another tab.

> PDF extraction keeps images of low-text or visual-only pages alongside selectable text, so a text-rich page no longer hides a neighboring diagram or scanned page. This affects extraction fallback; native Anthropic and Google PDF input is unchanged. More rendered pages can increase image-token charges, while the existing 20-page default selection, 200,000-character text cap, and shared four-million-pixel budget remain.

> The 2026.9.1 release guide gains interface illustrations and labeled conceptual examples to explain that older release. The figures document existing capabilities, with fictional and conceptual examples identified as such.

> Stopping a chat turn now interrupts optional idle waits and affected cleanup reads that were waiting on a stalled history rebuild. Required saves and cleanup still run, saved answers and attachment references remain intact, and an interrupted delivery check stays pending until its outcome is known. Completions canceled during connection setup now stop before contacting the provider, and PDF or image-analysis fallbacks also stop if their prepared resources are no longer valid. Requests already sent retain their existing cancellation limits.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-09-22 · OpenHands · [[Changes/OpenHands/2026-09-22-docs-review-add-repository-and-product-scope-to-the-canvas-review-guide-by-all-h|docs(review): add repository and product scope to the Canvas review guide]]
- Later: 2026-09-23 · OpenHands · [[Changes/OpenHands/2026-09-23-feat-tag-agent-canvas-telemetry-by-deployment-kind-oss-13530-by-malhotra5-in-htt|feat: tag Agent Canvas telemetry by deployment kind (OSS-13530)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-in-document-export-there-s-a-field-where-the-user-can-add-the-number-of-seconds|Timecode offset]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-909dfe&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-6-files-and-data-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-909dfe%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->