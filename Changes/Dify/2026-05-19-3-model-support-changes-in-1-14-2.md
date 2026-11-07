---
card_id: dify-2026-05-19-021b75
date: '2026-05-19'
description: 'Dify · 2026-05-19 · Model Support: 3 changes in v1.14.2 - Security fixes,
  agent groundwork, workflow reliability, and deployment updates — **Workflow and
  model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1226
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 985eb8f2780a9a94bc155d09e34649ca87ce78021766f6e159517fbdb6e9db8b
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-19-021b75
  comparison: ''
  date: '2026-05-19'
  description: 'Dify — v1.14.2 - Security fixes, agent groundwork, workflow reliability,
    and deployment updates: 3 Model Support changes'
  evidence:
  - quote: '**Workflow and model selection polish** — fixed loading behavior when
      no model is selected, filtered model presets by supported parameters, and improved
      API extension dialog controls. Thanks @iamjoel and @lyzno1 in [#36342](https://github.com/langgenius/dify/pull/36342),
      [#36339](https://github.com/langgenius/dify/pull/36339), and [#36323](https://github.com/langgenius/dify/pull/36323).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  - quote: '**RAG and document processing** — allowed LLM nodes to access retrieved
      knowledge files, regenerated document summaries after API updates, fixed pipeline
      template rendering, and handled credential fetch failures in RAG pipelines more
      gracefully. Thanks @laipz8200, @EvanYao826, @FFXN, and @linw1995 in [#36175](https://github.com/langgenius/dify/pull/36175),
      [#36035](https://github.com/langgenius/dify/pull/36035), [#36168](https://github.com/langgenius/dify/pull/36168),
      and [#36165](https://github.com/langgenius/dify/pull/36165).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  - quote: 'chore: Filter model presets by supported parameters by @iamjoel in https://github.com/langgenius/dify/pull/36339'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-model-support-changes-in-1-14-2
  source_release: dify-2026-05-19-1-14-2-github-324730496-11d48ace
  source_type: github_releases
  theme: model-support
  title: 3 Model Support changes in 1.14.2
  type: change
related_changes:
- '[[Changes/Lovable/2026-05-18-lovable-ai-models-for-app-features|Lovable AI models
  for app features]]'
- '[[Changes/Claude Code/2026-05-19-resumed-sessions-now-keep-the-model-they-were-using-instead-of-picking-up-anothe|Resumed
  sessions now keep the model they were using instead of picking up another…]]'
- '[[Changes/Cline/2026-05-19-add-sap-ai-core-support-for-additional-hosted-models|Add
  SAP AI Core support for additional hosted models]]'
source_release: '[[Releases/Dify/dify-2026-05-19-1-14-2-github-324730496-11d48ace|dify-2026-05-19-1-14-2-github-324730496-11d48ace]]'
source_type: github_releases
theme: model-support
title: 3 Model Support changes in 1.14.2
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Model Support changes in 1.14.2

**Dify** · 2026-05-19 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.2) · from [[Releases/Dify/dify-2026-05-19-1-14-2-github-324730496-11d48ace|v1.14.2 - Security fixes, agent groundwork, workflow reliability, and deployment updates]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Workflow and model selection polish** — fixed loading behavior when no model is selected, filtered model presets by supported parameters, and improved API extension dialog controls. Thanks @iamjoel and @lyzno1 in [#36342](https://github.com/langgenius/dify/pull/36342), [#36339](https://github.com/langgenius/dify/pull/36339), and [#36323](https://github.com/langgenius/dify/pull/36323).

> **RAG and document processing** — allowed LLM nodes to access retrieved knowledge files, regenerated document summaries after API updates, fixed pipeline template rendering, and handled credential fetch failures in RAG pipelines more gracefully. Thanks @laipz8200, @EvanYao826, @FFXN, and @linw1995 in [#36175](https://github.com/langgenius/dify/pull/36175), [#36035](https://github.com/langgenius/dify/pull/36035), [#36168](https://github.com/langgenius/dify/pull/36168), and [#36165](https://github.com/langgenius/dify/pull/36165).

> chore: Filter model presets by supported parameters by @iamjoel in https://github.com/langgenius/dify/pull/36339

Source: https://github.com/langgenius/dify/releases/tag/1.14.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-05-19-feat-messagelogmodal-refactor-modal-structure-and-improve-tab-handling-by-coding|feat(MessageLogModal): refactor modal structure and improve tab handling]] · Editor Experience
- [[Changes/Dify/2026-05-19-knowledge-base-stability-fixed-knowledge-hit-testing-rendering-empty-knowledge-c|Knowledge-base stability — fixed knowledge hit-testing rendering, empty…]] · Reliability and Performance
- [[Changes/Dify/2026-05-19-2-safety-and-privacy-changes-in-1-14-2|2 Safety and Privacy changes in 1.14.2]] · Safety and Privacy
- [[Changes/Dify/2026-05-19-4-apps-and-integrations-changes-in-1-14-2|4 Apps and Integrations changes in 1.14.2]] · Apps and Integrations
- [[Changes/Dify/2026-05-19-chore-enchance-copywriting-in-none-education-plan-warning-modal-by-iamjoel-in-ht|chore: enchance copywriting in none education plan warning modal]] · Enterprise and Administration
- [[Changes/Dify/2026-05-19-app-creation-and-onboarding-tracked-app-creation-source-and-template-id-initiali|App creation and onboarding]] · Interface Experience
- [[Changes/Dify/2026-05-19-3-agent-mode-changes-in-1-14-2|3 Agent Mode changes in 1.14.2]] · Agent Mode
- [[Changes/Dify/2026-05-19-workflow-execution-reliability-restored-tracing-after-hitl-workflow-resume-impro|Workflow execution reliability]] · Memory and Personalization
- [[Changes/Dify/2026-05-19-59-other-changes-in-1-14-2|59 other changes in 1.14.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-05-19 · Cline · [[Changes/Cline/2026-05-19-add-sap-ai-core-support-for-additional-hosted-models|Add SAP AI Core support for additional hosted models]]
- Later: 2026-05-19 · Gemini · [[Changes/Gemini/2026-05-19-3-5-flash-delivers-frontier-level-intelligence-for-your-daily-life|3.5 Flash delivers frontier-level intelligence for your daily life]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-19-021b75&body=Card%3A%20Changes%2FDify%2F2026-05-19-3-model-support-changes-in-1-14-2.md%0ACard%20ID%3A%20dify-2026-05-19-021b75%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->