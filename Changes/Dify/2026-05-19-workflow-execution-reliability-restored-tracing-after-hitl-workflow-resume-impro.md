---
card_id: dify-2026-05-19-f3ec56
date: '2026-05-19'
description: 'Dify · 2026-05-19 · Memory and Personalization: **Workflow execution
  reliability** — restored tracing after HITL workflow resume, improved workflow run…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1034
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: da4e5bdf3c23833d05fa18fb4d4ee6cebb10d7669a1068f9adba421fa2f0d70d
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-19-f3ec56
  comparison: ''
  date: '2026-05-19'
  description: 'Dify — v1.14.2 - Security fixes, agent groundwork, workflow reliability,
    and deployment updates: **Workflow execution reliability** — restored tracing
    after HITL workflow resume, improved workflow run callback tracking, reduced message-update
    database roundtrips, fixed memory fetches outside Flask context, and closed base64
    file lookup sessions correctly. Thanks @Blackoutta, @CodingOnStar, @wylswz, @hjlarry,
    and @escape0707 in [#36064](https://github.com/langgenius/dify/pull/36064), [#36149](https://github.com/langgenius/dify/pull/36149),
    [#36213](https://github.com/langgenius/dify/pull/36213), [#36253](https://github.com/langgenius/dify/pull/36253),
    and [#36308](https://github.com/langgenius/dify/pull/36308).'
  evidence:
  - quote: '**Workflow execution reliability** — restored tracing after HITL workflow
      resume, improved workflow run callback tracking, reduced message-update database
      roundtrips, fixed memory fetches outside Flask context, and closed base64 file
      lookup sessions correctly. Thanks @Blackoutta, @CodingOnStar, @wylswz, @hjlarry,
      and @escape0707 in [#36064](https://github.com/langgenius/dify/pull/36064),
      [#36149](https://github.com/langgenius/dify/pull/36149), [#36213](https://github.com/langgenius/dify/pull/36213),
      [#36253](https://github.com/langgenius/dify/pull/36253), and [#36308](https://github.com/langgenius/dify/pull/36308).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: dify
  product_name: Dify
  slug: workflow-execution-reliability-restored-tracing-after-hitl-workflow-resume-impro
  source_release: dify-2026-05-19-1-14-2-github-324730496-11d48ace
  source_type: github_releases
  theme: memory
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - context
    score: 50
    theme: context-window
  title: '**Workflow execution reliability**'
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-05-12-feat-memory-add-auto-memory-inbox-flow-with-canonical-patch-contract-by-sandytao|feat(memory):
  add Auto Memory inbox flow with canonical-patch contract]]'
- '[[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4
  Memory and Personalization changes in rust-v0.131.0]]'
- '[[Changes/Lovable/2026-05-18-security-memory|Security memory]]'
source_release: '[[Releases/Dify/dify-2026-05-19-1-14-2-github-324730496-11d48ace|dify-2026-05-19-1-14-2-github-324730496-11d48ace]]'
source_type: github_releases
theme: memory
title: Workflow execution reliability
type: change
---

<!-- chronolog:begin region="header" -->
# **Workflow execution reliability**

**Dify** · 2026-05-19 · [[Themes/memory|Memory and Personalization]] · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.2) · from [[Releases/Dify/dify-2026-05-19-1-14-2-github-324730496-11d48ace|v1.14.2 - Security fixes, agent groundwork, workflow reliability, and deployment updates]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Workflow execution reliability** — restored tracing after HITL workflow resume, improved workflow run callback tracking, reduced message-update database roundtrips, fixed memory fetches outside Flask context, and closed base64 file lookup sessions correctly. Thanks @Blackoutta, @CodingOnStar, @wylswz, @hjlarry, and @escape0707 in [#36064](https://github.com/langgenius/dify/pull/36064), [#36149](https://github.com/langgenius/dify/pull/36149), [#36213](https://github.com/langgenius/dify/pull/36213), [#36253](https://github.com/langgenius/dify/pull/36253), and [#36308](https://github.com/langgenius/dify/pull/36308).
>
> Source: https://github.com/langgenius/dify/releases/tag/1.14.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-05-19-3-model-support-changes-in-1-14-2|3 Model Support changes in 1.14.2]] · Model Support
- [[Changes/Dify/2026-05-19-feat-messagelogmodal-refactor-modal-structure-and-improve-tab-handling-by-coding|feat(MessageLogModal): refactor modal structure and improve tab handling]] · Editor Experience
- [[Changes/Dify/2026-05-19-knowledge-base-stability-fixed-knowledge-hit-testing-rendering-empty-knowledge-c|Knowledge-base stability — fixed knowledge hit-testing rendering, empty…]] · Reliability and Performance
- [[Changes/Dify/2026-05-19-2-safety-and-privacy-changes-in-1-14-2|2 Safety and Privacy changes in 1.14.2]] · Safety and Privacy
- [[Changes/Dify/2026-05-19-4-apps-and-integrations-changes-in-1-14-2|4 Apps and Integrations changes in 1.14.2]] · Apps and Integrations
- [[Changes/Dify/2026-05-19-chore-enchance-copywriting-in-none-education-plan-warning-modal-by-iamjoel-in-ht|chore: enchance copywriting in none education plan warning modal]] · Enterprise and Administration
- [[Changes/Dify/2026-05-19-app-creation-and-onboarding-tracked-app-creation-source-and-template-id-initiali|App creation and onboarding]] · Interface Experience
- [[Changes/Dify/2026-05-19-3-agent-mode-changes-in-1-14-2|3 Agent Mode changes in 1.14.2]] · Agent Mode
- [[Changes/Dify/2026-05-19-59-other-changes-in-1-14-2|59 other changes in 1.14.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-05-18 · Lovable · [[Changes/Lovable/2026-05-18-security-memory|Security memory]]
- Later: 2026-05-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-19-2-memory-and-personalization-changes-in-v1-0-49|2 Memory and Personalization changes in v1.0.49]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-19-f3ec56&body=Card%3A%20Changes%2FDify%2F2026-05-19-workflow-execution-reliability-restored-tracing-after-hitl-workflow-resume-impro.md%0ACard%20ID%3A%20dify-2026-05-19-f3ec56%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->