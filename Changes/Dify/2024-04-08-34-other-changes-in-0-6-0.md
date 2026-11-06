---
card_id: dify-2024-04-08-d5eafa
date: '2024-04-08'
description: 'Dify · 2024-04-08 · Other changes: 34 changes in v0.6.0 — **There are
  two Workflow application types with this update:**'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 93eaa51db464c8073cd86cbd2d9a2b4bc4ff33b9160e9eb3513abbeefa747643
product: dify
product_name: Dify
record:
  card_id: dify-2024-04-08-d5eafa
  comparison: ''
  date: '2024-04-08'
  description: 'Dify — v0.6.0: 34 other changes'
  evidence:
  - quote: '**There are two Workflow application types with this update:**'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: '**Workflow App**'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: '![image](https://github.com/langgenius/dify/assets/5485478/67c214e1-bc7e-44ad-8d81-297a30ebcc99)'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: '**Chatflow App (A Sub-Type of Chatbot)**'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: '![image](https://github.com/langgenius/dify/assets/5485478/3fe94294-7e44-497a-9f19-e89808b2675f)'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'For more information, please visit: https://docs.dify.ai/features/workflow/introduce'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'Other Enhancements:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Optimized UI flow for app creation.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Conversion support from various basic application types to Workflow-based
      applications.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: '> - Text Generator → Workflow'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: '> ![image](https://github.com/langgenius/dify/assets/5485478/9227958e-4a9d-482b-91b8-7c5b72a16a14)'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Support for adding descriptions to applications.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Support for porting applications in and out of Dify with DSL.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Under the hood, we also refactored the underlying execution logic of all
      app types for cleaner architecture and a tidier repo.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: '**If you need to upgrade from** `0.6.0-preview-workflow.1`**, you will
      need to connect to** **PostgreSQL** **and execute the following SQL (migration
      inserted in the main branch) to ensure data integrity.**'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'Get the latest code from the main branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Update README.md by @guchenhe in https://github.com/langgenius/dify/pull/3081
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Chore/move chrome ext by @crazywoola in https://github.com/langgenius/dify/pull/3085
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: add embedding cache and clean embedding cache job by @JohnJyong in https://github.com/langgenius/dify/pull/3087
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: new readme slogan by @guchenhe in https://github.com/langgenius/dify/pull/3094
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Improve ModelTypeEnum type by @lng2020 in https://github.com/langgenius/dify/pull/3051
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'feat: claude3 tool call by @Yeuoly in https://github.com/langgenius/dify/pull/3111'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'feat: update link by @crazywoola in https://github.com/langgenius/dify/pull/3121'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'chore: update link of feedback by @JzoNgKVO in https://github.com/langgenius/dify/pull/3130'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Duplicate embedding cache check by @JohnJyong in https://github.com/langgenius/dify/pull/3134
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: improve qa generate prompt by @JohnJyong in https://github.com/langgenius/dify/pull/3132
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Feat/update issue template by @crazywoola in https://github.com/langgenius/dify/pull/3147
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Update descriptions in StackExchange Tool by @richards199999 in https://github.com/langgenius/dify/pull/3043
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: Optimize csv and excel extract by @JohnJyong in https://github.com/langgenius/dify/pull/3155
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  - quote: 'FEAT: NEW WORKFLOW ENGINE by @takatost in https://github.com/langgenius/dify/pull/3160'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 34-other-changes-in-0-6-0
  source_release: dify-2024-04-08-0-6-0-github-150191925-0ce534e4
  source_type: github_releases
  theme: uncategorized
  title: 34 other changes in 0.6.0
  type: change
source_release: '[[Releases/Dify/dify-2024-04-08-0-6-0-github-150191925-0ce534e4|dify-2024-04-08-0-6-0-github-150191925-0ce534e4]]'
source_type: github_releases
theme: uncategorized
title: 34 other changes in 0.6.0
type: change
---

<!-- chronolog:begin region="header" -->
# 34 other changes in 0.6.0

**Dify** · 2024-04-08 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.6.0) · from [[Releases/Dify/dify-2024-04-08-0-6-0-github-150191925-0ce534e4|v0.6.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **There are two Workflow application types with this update:**

> **Workflow App**

> ![image](https://github.com/langgenius/dify/assets/5485478/67c214e1-bc7e-44ad-8d81-297a30ebcc99)

> **Chatflow App (A Sub-Type of Chatbot)**

> ![image](https://github.com/langgenius/dify/assets/5485478/3fe94294-7e44-497a-9f19-e89808b2675f)

> For more information, please visit: https://docs.dify.ai/features/workflow/introduce

> Other Enhancements:

> Optimized UI flow for app creation.

> Conversion support from various basic application types to Workflow-based applications.

> > - Text Generator → Workflow

> > ![image](https://github.com/langgenius/dify/assets/5485478/9227958e-4a9d-482b-91b8-7c5b72a16a14)

> Support for adding descriptions to applications.

> Support for porting applications in and out of Dify with DSL.

> Under the hood, we also refactored the underlying execution logic of all app types for cleaner architecture and a tidier repo.

> **If you need to upgrade from** `0.6.0-preview-workflow.1`**, you will need to connect to** **PostgreSQL** **and execute the following SQL (migration inserted in the main branch) to ensure data integrity.**

> Get the latest code from the main branch:

> Stop API server, Worker and Web frontend Server.

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run API server, Worker and Web frontend Server again.

> Update README.md by @guchenhe in https://github.com/langgenius/dify/pull/3081

> Chore/move chrome ext by @crazywoola in https://github.com/langgenius/dify/pull/3085

> add embedding cache and clean embedding cache job by @JohnJyong in https://github.com/langgenius/dify/pull/3087

> new readme slogan by @guchenhe in https://github.com/langgenius/dify/pull/3094

> Improve ModelTypeEnum type by @lng2020 in https://github.com/langgenius/dify/pull/3051

> feat: claude3 tool call by @Yeuoly in https://github.com/langgenius/dify/pull/3111

> feat: update link by @crazywoola in https://github.com/langgenius/dify/pull/3121

> chore: update link of feedback by @JzoNgKVO in https://github.com/langgenius/dify/pull/3130

> Duplicate embedding cache check by @JohnJyong in https://github.com/langgenius/dify/pull/3134

> improve qa generate prompt by @JohnJyong in https://github.com/langgenius/dify/pull/3132

> Feat/update issue template by @crazywoola in https://github.com/langgenius/dify/pull/3147

> Update descriptions in StackExchange Tool by @richards199999 in https://github.com/langgenius/dify/pull/3043

> Optimize csv and excel extract by @JohnJyong in https://github.com/langgenius/dify/pull/3155

> FEAT: NEW WORKFLOW ENGINE by @takatost in https://github.com/langgenius/dify/pull/3160

Source: https://github.com/langgenius/dify/releases/tag/0.6.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-04-08-the-much-anticipated-workflow-feature-is-here-in-a-nutshell-workflow-provides-a|The much-anticipated workflow feature is here]] · Files and Data
- [[Changes/Dify/2024-04-08-2-apps-and-integrations-changes-in-0-6-0|2 Apps and Integrations changes in 0.6.0]] · Apps and Integrations
- [[Changes/Dify/2024-04-08-targeting-automation-and-batch-processing-this-is-ideal-for-translation-data-ana|Targeting Automation and Batch Processing]] · Automation and Scheduling
- [[Changes/Dify/2024-04-08-we-also-moved-the-agent-data-within-the-database-execute-the-below-script-to-com|We also moved the agent data within the database, Execute the below…]] · Agent Mode
- [[Changes/Dify/2024-04-08-chore-replace-outdated-config-in-vscode-debug-settings-by-lng2020-in-https-githu|chore: replace outdated config in vscode debug settings]] · Developer Workflow
- [[Changes/Dify/2024-04-08-add-segment-function-billing-check-for-saas-env-by-johnjyong-in-https-github-com|add segment function billing check for SAAS env]] · Pricing Model
- [[Changes/Dify/2024-04-08-compared-to-the-regular-workflow-app-type-chatflow-adds-chat-specific-features-s|Compared to the regular Workflow app type, Chatflow adds chat-specific features such…]] · Memory and Personalization
- [[Changes/Dify/2024-04-08-feat-new-llm-add-support-for-openrouter-by-korayem-in-https-github-com-langgeniu|feat (new llm): add support for openrouter]] · Model Support
- [[Changes/Dify/2024-04-08-dify-s-official-app-templates-are-now-available-in-self-hosted-mode|Dify's official app templates are now available in self-hosted mode]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-04-08-d5eafa&body=Card%3A%20Changes%2FDify%2F2024-04-08-34-other-changes-in-0-6-0.md%0ACard%20ID%3A%20dify-2024-04-08-d5eafa%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.6.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->