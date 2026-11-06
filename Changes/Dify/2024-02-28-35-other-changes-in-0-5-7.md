---
card_id: dify-2024-02-28-21a49a
date: '2024-02-28'
description: 'Dify · 2024-02-28 · Other changes: 35 changes in v0.5.7 — Added Vector
  Database migrate tool, see below. #2562'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2950cfb41826fe96500411b31284f0b71f567e51c732d8347958211027ea8c63
product: dify
product_name: Dify
record:
  card_id: dify-2024-02-28-21a49a
  comparison: ''
  date: '2024-02-28'
  description: 'Dify — v0.5.7: 35 other changes'
  evidence:
  - quote: 'Added Vector Database migrate tool, see below. #2562'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'Added `response format`(JSON/XML) for `google`, `anthropic`, `openai`,
      `wenxin`, `chatglm`, `tongyi` LLMs. #2563'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'Refactor RAG(knowledge) module, remove dependency on langchain to increase
      scalability and flexibility. #2528'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: When you want to switch to another vector database, you can deactivate
      or delete the original vector database after switching.
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: If you are starting from local source code, modify the environment variable
      in the `.env` file to the vector database you want to migrate to.
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'For example:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: If you are starting from `docker compose`, modify the environment variable
      in the `docker-compose.yaml` file to the vector database you want to migrate
      to, both api and worker are all needed.
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'Get the latest code from the main branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: '**Note**: To use TTS, `ffmpeg` installation is required on servers running
      Dify API from source. More details can be found in our [FAQ](https://docs.dify.ai/getting-started/install-self-hosted/install-faq#id-14.-what-to-do-if-this-error-occurs-in-text-to-speech).'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Windows local deployment switch "tool“ interface failed by @kukuze in https://github.com/langgenius/dify/pull/2483
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: del doc support by @JohnJyong in https://github.com/langgenius/dify/pull/2494
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Add default values for optional parameters in API tool and parser by @Yeuoly
      in https://github.com/langgenius/dify/pull/2491
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'doc: typo in chat by @crazywoola in https://github.com/langgenius/dify/pull/2492'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'feat: increase max tools by @Yeuoly in https://github.com/langgenius/dify/pull/2497'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Chore/delete chunk decode error alert by @guchenhe in https://github.com/langgenius/dify/pull/2500
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Feat/stream react by @Yeuoly in https://github.com/langgenius/dify/pull/2498
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: update issue template by @crazywoola in https://github.com/langgenius/dify/pull/2507
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Feat/dify rag by @JohnJyong in https://github.com/langgenius/dify/pull/2528
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'chore: add api key and value placeholder by @iamjoel in https://github.com/langgenius/dify/pull/2538'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Feat/i18n restructure by @crazywoola in https://github.com/langgenius/dify/pull/2529
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Update README_CN.md by @takatost in https://github.com/langgenius/dify/pull/2550
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'feat: change max_question_num to 5 by @wststone in https://github.com/langgenius/dify/pull/2520'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Feat/use searchparams as state by @wststone in https://github.com/langgenius/dify/pull/2554
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Feat/json mode by @Yeuoly in https://github.com/langgenius/dify/pull/2563
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'chore: remove redundant casting flask app config into dict by @bowenliang123
      in https://github.com/langgenius/dify/pull/2564'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Add Dify Meetup Event on Mar 9 by @crazywoola in https://github.com/langgenius/dify/pull/2566
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'enhancement: improve client-side code by @wststone in https://github.com/langgenius/dify/pull/2568'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'enhancement: skip fetching to improve user experience when switching …
      by @wststone in https://github.com/langgenius/dify/pull/2580'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: feat:add mistral ai by @joshua20231026 in https://github.com/langgenius/dify/pull/2594
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: Feat/provider mistralai by @joshua20231026 in https://github.com/langgenius/dify/pull/2598
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: 'doc: props.appDetail.api_base_url by @crazywoola in https://github.com/langgenius/dify/pull/2597'
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  - quote: version to 0.5.7 by @takatost in https://github.com/langgenius/dify/pull/2610
    source_release: https://github.com/langgenius/dify/releases/tag/0.5.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 35-other-changes-in-0-5-7
  source_release: dify-2024-02-28-0-5-7-github-143968174-dc5f7626
  source_type: github_releases
  theme: uncategorized
  title: 35 other changes in 0.5.7
  type: change
source_release: '[[Releases/Dify/dify-2024-02-28-0-5-7-github-143968174-dc5f7626|dify-2024-02-28-0-5-7-github-143968174-dc5f7626]]'
source_type: github_releases
theme: uncategorized
title: 35 other changes in 0.5.7
type: change
---

<!-- chronolog:begin region="header" -->
# 35 other changes in 0.5.7

**Dify** · 2024-02-28 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.5.7) · from [[Releases/Dify/dify-2024-02-28-0-5-7-github-143968174-dc5f7626|v0.5.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Vector Database migrate tool, see below. #2562

> Added `response format`(JSON/XML) for `google`, `anthropic`, `openai`, `wenxin`, `chatglm`, `tongyi` LLMs. #2563

> Refactor RAG(knowledge) module, remove dependency on langchain to increase scalability and flexibility. #2528

> When you want to switch to another vector database, you can deactivate or delete the original vector database after switching.

> If you are starting from local source code, modify the environment variable in the `.env` file to the vector database you want to migrate to.

> For example:

> If you are starting from `docker compose`, modify the environment variable in the `docker-compose.yaml` file to the vector database you want to migrate to, both api and worker are all needed.

> Get the latest code from the main branch:

> Stop API server, Worker and Web frontend Server.

> Then, let's run the migration script:

> **Note**: To use TTS, `ffmpeg` installation is required on servers running Dify API from source. More details can be found in our [FAQ](https://docs.dify.ai/getting-started/install-self-hosted/install-faq#id-14.-what-to-do-if-this-error-occurs-in-text-to-speech).

> Finally, run API server, Worker and Web frontend Server again.

> Windows local deployment switch "tool“ interface failed by @kukuze in https://github.com/langgenius/dify/pull/2483

> del doc support by @JohnJyong in https://github.com/langgenius/dify/pull/2494

> Add default values for optional parameters in API tool and parser by @Yeuoly in https://github.com/langgenius/dify/pull/2491

> doc: typo in chat by @crazywoola in https://github.com/langgenius/dify/pull/2492

> feat: increase max tools by @Yeuoly in https://github.com/langgenius/dify/pull/2497

> Chore/delete chunk decode error alert by @guchenhe in https://github.com/langgenius/dify/pull/2500

> Feat/stream react by @Yeuoly in https://github.com/langgenius/dify/pull/2498

> update issue template by @crazywoola in https://github.com/langgenius/dify/pull/2507

> Feat/dify rag by @JohnJyong in https://github.com/langgenius/dify/pull/2528

> chore: add api key and value placeholder by @iamjoel in https://github.com/langgenius/dify/pull/2538

> Feat/i18n restructure by @crazywoola in https://github.com/langgenius/dify/pull/2529

> Update README_CN.md by @takatost in https://github.com/langgenius/dify/pull/2550

> feat: change max_question_num to 5 by @wststone in https://github.com/langgenius/dify/pull/2520

> Feat/use searchparams as state by @wststone in https://github.com/langgenius/dify/pull/2554

> Feat/json mode by @Yeuoly in https://github.com/langgenius/dify/pull/2563

> chore: remove redundant casting flask app config into dict by @bowenliang123 in https://github.com/langgenius/dify/pull/2564

> Add Dify Meetup Event on Mar 9 by @crazywoola in https://github.com/langgenius/dify/pull/2566

> enhancement: improve client-side code by @wststone in https://github.com/langgenius/dify/pull/2568

> enhancement: skip fetching to improve user experience when switching … by @wststone in https://github.com/langgenius/dify/pull/2580

> feat:add mistral ai by @joshua20231026 in https://github.com/langgenius/dify/pull/2594

> Feat/provider mistralai by @joshua20231026 in https://github.com/langgenius/dify/pull/2598

> doc: props.appDetail.api_base_url by @crazywoola in https://github.com/langgenius/dify/pull/2597

> version to 0.5.7 by @takatost in https://github.com/langgenius/dify/pull/2610

Source: https://github.com/langgenius/dify/releases/tag/0.5.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-02-28-2-agent-mode-changes-in-0-5-7|2 Agent Mode changes in 0.5.7]] · Agent Mode
- [[Changes/Dify/2024-02-28-2-safety-and-privacy-changes-in-0-5-7|2 Safety and Privacy changes in 0.5.7]] · Safety and Privacy
- [[Changes/Dify/2024-02-28-2-developer-workflow-changes-in-0-5-7|2 Developer Workflow changes in 0.5.7]] · Developer Workflow
- [[Changes/Dify/2024-02-28-voice-audition-by-charli117-in-https-github-com-langgenius-dify-pull-2504|Voice audition]] · Voice and Audio
- [[Changes/Dify/2024-02-28-3-model-support-changes-in-0-5-7|3 Model Support changes in 0.5.7]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-02-28-21a49a&body=Card%3A%20Changes%2FDify%2F2024-02-28-35-other-changes-in-0-5-7.md%0ACard%20ID%3A%20dify-2024-02-28-21a49a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.5.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->