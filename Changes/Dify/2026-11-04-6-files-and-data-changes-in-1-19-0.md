---
card_id: dify-2026-11-04-a8b785
date: '2026-11-04'
description: 'Dify · 2026-11-04 · Files and Data: 6 changes in v1.19.0 - Trace Your
  Workflows, Layer by Layer — Read PDFs inline, inspect source files with syntax…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2
    Files and Data changes in 0.2.2]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1259
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: file-data
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6979e4da3a3dae41eef1f1b73c75fe2f8a883391623652faa7d1fc55fe640bcf
product: dify
product_name: Dify
record:
  card_id: dify-2026-11-04-a8b785
  comparison: ''
  date: '2026-11-04'
  description: 'Dify — v1.19.0 - Trace Your Workflows, Layer by Layer: 6 Files and
    Data changes'
  evidence:
  - quote: 'Read PDFs inline, inspect source files with syntax highlighting, and see
      when text has been truncated. Previews cover configured files, Skill members,
      and working-directory files, with a download action when a PDF cannot be loaded.
      (#45032, #45045)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Extraction changes affect newly processed content.** Re-import or re-index
      documents whose stored content was affected by the EPUB, EML, DOCX, CSV, Markdown,
      or Notion fixes. The repeated-PDF-preview fix prevents new duplicate assets
      for source uploads; it does not remove duplicates already stored. (#44836, #44953,
      #44905, #43505, #43434, #45053, #44684)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Request clear-canvas confirmation only when clearing a previously nonempty
      saved draft, and wrap long workflow error messages. (#45028, #45106)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: '**Knowledge and document processing**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Remove index entries written by a document that was deleted during indexing.
      Partial QA-segment updates preserve an omitted answer and its contribution to
      counts. (#44364, #44997)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  - quote: 'Include documents missing a metadata key in negative metadata filters,
      honor explicit `top_k=0`, normalize blank legacy retrieval settings on read,
      and use keyword retrieval for Economy datasets in retrieval previews. (#44753,
      #42980, #45020, #44895)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.19.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-files-and-data-changes-in-1-19-0
  source_release: dify-2026-11-04-1-19-0-github-433629888-738006ec
  source_type: github_releases
  theme: file-data
  title: 6 Files and Data changes in 1.19.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-11-02-2-files-and-data-changes-in-elevenlabs-updates-2026-11-02|2
  Files and Data changes in ElevenLabs updates — 2026-11-02]]'
- '[[Changes/OpenClaw/2026-11-03-2-files-and-data-changes-in-v2026-10-10|2 Files and
  Data changes in v2026.10.10]]'
- '[[Changes/OpenHands/2026-11-03-feat-canvas-attribute-local-cloud-signup-entries-all-5962-by-malhotra5-in-https|feat(canvas):
  attribute local Cloud signup entries (ALL-5962)]]'
source_release: '[[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|dify-2026-11-04-1-19-0-github-433629888-738006ec]]'
source_type: github_releases
theme: file-data
title: 6 Files and Data changes in 1.19.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Files and Data changes in 1.19.0

**Dify** · 2026-11-04 · [[Themes/file-data|Files and Data]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.19.0) · from [[Releases/Dify/dify-2026-11-04-1-19-0-github-433629888-738006ec|v1.19.0 - Trace Your Workflows, Layer by Layer]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Read PDFs inline, inspect source files with syntax highlighting, and see when text has been truncated. Previews cover configured files, Skill members, and working-directory files, with a download action when a PDF cannot be loaded. (#45032, #45045)

> **Extraction changes affect newly processed content.** Re-import or re-index documents whose stored content was affected by the EPUB, EML, DOCX, CSV, Markdown, or Notion fixes. The repeated-PDF-preview fix prevents new duplicate assets for source uploads; it does not remove duplicates already stored. (#44836, #44953, #44905, #43505, #43434, #45053, #44684)

> Request clear-canvas confirmation only when clearing a previously nonempty saved draft, and wrap long workflow error messages. (#45028, #45106)

> **Knowledge and document processing**

> Remove index entries written by a document that was deleted during indexing. Partial QA-segment updates preserve an omitted answer and its contribution to counts. (#44364, #44997)

> Include documents missing a metadata key in negative metadata filters, honor explicit `top_k=0`, normalize blank legacy retrieval settings on read, and use keyword retrieval for Economy datasets in retrieval previews. (#44753, #42980, #45020, #44895)

Source: https://github.com/langgenius/dify/releases/tag/1.19.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-11-04-4-model-support-changes-in-1-19-0|4 Model Support changes in 1.19.0]] · Model Support
- [[Changes/Dify/2026-11-04-stop-serializing-the-entire-prompt-history-into-every-agent-llm-gateway-response|Stop serializing the entire prompt history into every Agent LLM gateway response chunk]] · Multimodal Input
- [[Changes/Dify/2026-11-04-4-collaboration-changes-in-1-19-0|4 Collaboration changes in 1.19.0]] · Collaboration
- [[Changes/Dify/2026-11-04-15-apps-and-integrations-changes-in-1-19-0|15 Apps and Integrations changes in 1.19.0]] · Apps and Integrations
- [[Changes/Dify/2026-11-04-3-automation-and-scheduling-changes-in-1-19-0|3 Automation and Scheduling changes in 1.19.0]] · Automation and Scheduling
- [[Changes/Dify/2026-11-04-2-developer-workflow-changes-in-1-19-0|2 Developer Workflow changes in 1.19.0]] · Developer Workflow
- [[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes in 1.19.0]] · Pricing Model
- [[Changes/Dify/2026-11-04-3-editor-experience-changes-in-1-19-0|3 Editor Experience changes in 1.19.0]] · Editor Experience
- [[Changes/Dify/2026-11-04-2-voice-and-audio-changes-in-1-19-0|2 Voice and Audio changes in 1.19.0]] · Voice and Audio
- [[Changes/Dify/2026-11-04-4-safety-and-privacy-changes-in-1-19-0|4 Safety and Privacy changes in 1.19.0]] · Safety and Privacy
- [[Changes/Dify/2026-11-04-workspace-controls-enabling-or-disabling-provider-models-requires-an-owner-or-ad|Workspace controls: enabling or disabling provider models requires an owner…]] · Enterprise and Administration
- [[Changes/Dify/2026-11-04-summary-strong-improvements-editing-accessibility-performance-and-operations-str|summarystrongImprovements · editing, accessibility, performance…]] · Accessibility and Localization
- [[Changes/Dify/2026-11-04-2-interface-experience-changes-in-1-19-0|2 Interface Experience changes in 1.19.0]] · Interface Experience
- [[Changes/Dify/2026-11-04-6-context-window-changes-in-1-19-0|6 Context Window changes in 1.19.0]] · Context Window
- [[Changes/Dify/2026-11-04-14-agent-mode-changes-in-1-19-0|14 Agent Mode changes in 1.19.0]] · Agent Mode
- [[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and Access changes in 1.19.0]] · Account and Access
- [[Changes/Dify/2026-11-04-66-other-changes-in-1-19-0|66 other changes in 1.19.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Files and Data

- Earlier: 2026-11-03 · OpenHands · [[Changes/OpenHands/2026-11-03-feat-canvas-attribute-local-cloud-signup-entries-all-5962-by-malhotra5-in-https|feat(canvas): attribute local Cloud signup entries (ALL-5962)]]
- Later: 2026-11-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-25 · Dify · [[Changes/Dify/2023-05-25-2-files-and-data-changes-in-0-2-2|2 Files and Data changes in 0.2.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-11-04-a8b785&body=Card%3A%20Changes%2FDify%2F2026-11-04-6-files-and-data-changes-in-1-19-0.md%0ACard%20ID%3A%20dify-2026-11-04-a8b785%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.19.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->