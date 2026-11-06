---
card_id: dify-2024-09-03-349b2e
date: '2024-09-03'
description: 'Dify · 2024-09-03 · Other changes: 60 changes in v0.7.3 — Hey everyone,
  we''ve just dropped version 0.7.3, and it''s packed with new features, enhancements,
  and…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0896d888a28e91020776229b214db0543244d256c45ec53d318630148a068f03
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-03-349b2e
  comparison: ''
  date: '2024-09-03'
  description: 'Dify — v0.7.3: 60 other changes'
  evidence:
  - quote: 'Hey everyone, we''ve just dropped version 0.7.3, and it''s packed with
      new features, enhancements, and fixes. Let''s dive into what''s new:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Message Count**: You can now monitor the message usage directly from
      the monitoring page by @leslie2046 in #7603.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: <img width="842" alt="image" src="https://github.com/user-attachments/assets/a14dae68-a4fe-41ad-b61a-74b011add469">
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Azure AI Studio Provider**: Added Azure AI Studio as a provider by @helioLJ
      in #7549.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Perplexity Search Tool**: Introduced a new search tool that utilizes
      perplexity-based techniques to enhance search capabilities by @leilei-jiang
      in #7861.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**App Icon as Answer Icon**: Now you can use your app icon as the answer
      icon by @kurokobo in #7888.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Array Types in Variable List**: Support for array types in the available
      variable list by @YidaHu in #7715.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Question Classifier Prompt Optimization**: Enhanced prompt accuracy
      by @JohnJyong in #4262.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Code Execution Configs**: Added support for configurations in code execution
      requests by @bowenliang123 in #7704.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**CODE_MAX_STRING_LENGTH Config**: Fixed configuration issue by @bowenliang123
      in #7683.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**MyScale VectorDB Score Threshold**: Set `score_threshold` to zero if
      it is `None` by @lqhl in #7640.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Empty Knowledge Add File**: Fixed issue with adding empty knowledge
      files by @zxhlyh in #7690.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Chunk Overlap Fix**: Addressed `None` value in chunk overlap by @JohnJyong
      in #7703.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Tongyi Error Fix**: Resolved ''NoneType'' object error by @crazywoola
      in #7705.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Annotation Reply Settings**: Fixed settings issue by @JzoNgKVO in #7696.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Crawl Options Max Length**: Fixed issue where max length could not be
      set to 0 by @iamjoel in #7758.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Variable Aggregator Groups**: Fixed issue with passing arrays of string/number/object
      by @Leheng620 in #7757.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**WebApp SSO Setting**: Ensured latest value is shown on refresh by @douxc
      in #7795.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Keyword Search in Application Log**: Fixed issue in application log
      list by @realethanhsu in #7816.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**HTTP Timeout Configs**: Corrected default values and ignorance by HttpRequestNode
      by @bowenliang123 in #7762.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**ECharts Crash**: Fixed crash when accessing undefined objects by @zhujinle
      in #7853.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**RetrievalConfig Score Threshold**: Fixed assignment for zero value by
      @MH4GF in #7865.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Layout Shift on App Card Hover**: Fixed layout shift issue by @yikayiyo
      in #7872.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Linked Images**: Ignored linked images when image ID is `None` by @JohnJyong
      in #7890.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '**Russian Language Support**: Added support for the Russian language by
      @d8rt8v in #7860.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: "That's all for this release! As always, thanks for your contributions
      and feedback. Keep them coming! \U0001F680"
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Add Azure AI Studio as provider by @helioLJ in https://github.com/langgenius/dify/pull/7549
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'bug: (#7586 followup) fix config of CODE_MAX_STRING_LENGTH by @bowenliang123
      in https://github.com/langgenius/dify/pull/7683'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Langfuse view button by @charli117 in https://github.com/langgenius/dify/pull/7684
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'feat: rewrite Elasticsearch index and search code to achieve Elasticsearch
      vector and full-text search by @KennFalcon in https://github.com/langgenius/dify/pull/7641'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'feat: chart for message count by @leslie2046 in https://github.com/langgenius/dify/pull/7603'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'feat: remove unused code by @crazywoola in https://github.com/langgenius/dify/pull/7702'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'feat: support configs for code execution request by @bowenliang123 in
      https://github.com/langgenius/dify/pull/7704'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'chore: update default endpoint for ark provider by @sinomoe in https://github.com/langgenius/dify/pull/7741'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Update package "libldap-2.5-0" for docker build. by @snickerjp in https://github.com/langgenius/dify/pull/7726
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'feat: add support for array types in available variable list by @YidaHu
      in https://github.com/langgenius/dify/pull/7715'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'chore: improve http executor configs by @bowenliang123 in https://github.com/langgenius/dify/pull/7730'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'chore: ignore openai error record in sentry by @takatost in https://github.com/langgenius/dify/pull/7770'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Update ssrf_proxy related doc link in docker-compose file by @htynkn in
      https://github.com/langgenius/dify/pull/7778
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Sync Input component from feat/attachments branch by @douxc in https://github.com/langgenius/dify/pull/7782
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'chore: add app generator overload by @Yeuoly in https://github.com/langgenius/dify/pull/7792'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'feat: support auth by api key for ark provider by @sinomoe in https://github.com/langgenius/dify/pull/7845'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'refactor: Remove typecasting by any by @MH4GF in https://github.com/langgenius/dify/pull/7862'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Add ALIYUN_OSS_PATH configuration for Aliyun OSS by @Seayon in https://github.com/langgenius/dify/pull/7864
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Add perplexity search as a new tool by @leilei-jiang in https://github.com/langgenius/dify/pull/7861
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: Add Russian language by @d8rt8v in https://github.com/langgenius/dify/pull/7860
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: ignore linked images when image id is none by @JohnJyong in https://github.com/langgenius/dify/pull/7890
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'feat: allow users to use the app icon as the answer icon by @kurokobo
      in https://github.com/langgenius/dify/pull/7888'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'chore(Dockerfile): Bump expat to 2.6.2-2 by @laipz8200 in https://github.com/langgenius/dify/pull/7904'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  - quote: 'chore: Update versions to 0.7.3 by @laipz8200 in https://github.com/langgenius/dify/pull/7895'
    source_release: https://github.com/langgenius/dify/releases/tag/0.7.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 60-other-changes-in-0-7-3
  source_release: dify-2024-09-03-0-7-3-github-173123686-c526228f
  source_type: github_releases
  theme: uncategorized
  title: 60 other changes in 0.7.3
  type: change
source_release: '[[Releases/Dify/dify-2024-09-03-0-7-3-github-173123686-c526228f|dify-2024-09-03-0-7-3-github-173123686-c526228f]]'
source_type: github_releases
theme: uncategorized
title: 60 other changes in 0.7.3
type: change
---

<!-- chronolog:begin region="header" -->
# 60 other changes in 0.7.3

**Dify** · 2024-09-03 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.7.3) · from [[Releases/Dify/dify-2024-09-03-0-7-3-github-173123686-c526228f|v0.7.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hey everyone, we've just dropped version 0.7.3, and it's packed with new features, enhancements, and fixes. Let's dive into what's new:

> **Message Count**: You can now monitor the message usage directly from the monitoring page by @leslie2046 in #7603.

> \<img width="842" alt="image" src="https://github.com/user-attachments/assets/a14dae68-a4fe-41ad-b61a-74b011add469">

> **Azure AI Studio Provider**: Added Azure AI Studio as a provider by @helioLJ in #7549.

> **Perplexity Search Tool**: Introduced a new search tool that utilizes perplexity-based techniques to enhance search capabilities by @leilei-jiang in #7861.

> **App Icon as Answer Icon**: Now you can use your app icon as the answer icon by @kurokobo in #7888.

> **Array Types in Variable List**: Support for array types in the available variable list by @YidaHu in #7715.

> **Question Classifier Prompt Optimization**: Enhanced prompt accuracy by @JohnJyong in #4262.

> **Code Execution Configs**: Added support for configurations in code execution requests by @bowenliang123 in #7704.

> **CODE_MAX_STRING_LENGTH Config**: Fixed configuration issue by @bowenliang123 in #7683.

> **MyScale VectorDB Score Threshold**: Set `score_threshold` to zero if it is `None` by @lqhl in #7640.

> **Empty Knowledge Add File**: Fixed issue with adding empty knowledge files by @zxhlyh in #7690.

> **Chunk Overlap Fix**: Addressed `None` value in chunk overlap by @JohnJyong in #7703.

> **Tongyi Error Fix**: Resolved 'NoneType' object error by @crazywoola in #7705.

> **Annotation Reply Settings**: Fixed settings issue by @JzoNgKVO in #7696.

> **Crawl Options Max Length**: Fixed issue where max length could not be set to 0 by @iamjoel in #7758.

> **Variable Aggregator Groups**: Fixed issue with passing arrays of string/number/object by @Leheng620 in #7757.

> **WebApp SSO Setting**: Ensured latest value is shown on refresh by @douxc in #7795.

> **Keyword Search in Application Log**: Fixed issue in application log list by @realethanhsu in #7816.

> **HTTP Timeout Configs**: Corrected default values and ignorance by HttpRequestNode by @bowenliang123 in #7762.

> **ECharts Crash**: Fixed crash when accessing undefined objects by @zhujinle in #7853.

> **RetrievalConfig Score Threshold**: Fixed assignment for zero value by @MH4GF in #7865.

> **Layout Shift on App Card Hover**: Fixed layout shift issue by @yikayiyo in #7872.

> **Linked Images**: Ignored linked images when image ID is `None` by @JohnJyong in #7890.

> **Russian Language Support**: Added support for the Russian language by @d8rt8v in #7860.

> That's all for this release! As always, thanks for your contributions and feedback. Keep them coming! 🚀

> > [!WARNING]

> > The `docker-compose.yaml` has been refactored. If you've made any changes to the file, make sure to check out the "Upgrade to new docker compose deployment" section above for usage and migration tips.

> Back up your customized docker-compose YAML file (optional)

> Get the latest code from the main branch

> Back up data

> Upgrade services

> Stop API server, Worker and Web frontend Server.

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run API server, Worker and Web frontend Server again.

> Add Azure AI Studio as provider by @helioLJ in https://github.com/langgenius/dify/pull/7549

> bug: (#7586 followup) fix config of CODE_MAX_STRING_LENGTH by @bowenliang123 in https://github.com/langgenius/dify/pull/7683

> Langfuse view button by @charli117 in https://github.com/langgenius/dify/pull/7684

> feat: rewrite Elasticsearch index and search code to achieve Elasticsearch vector and full-text search by @KennFalcon in https://github.com/langgenius/dify/pull/7641

> feat: chart for message count by @leslie2046 in https://github.com/langgenius/dify/pull/7603

> feat: remove unused code by @crazywoola in https://github.com/langgenius/dify/pull/7702

> feat: support configs for code execution request by @bowenliang123 in https://github.com/langgenius/dify/pull/7704

> chore: update default endpoint for ark provider by @sinomoe in https://github.com/langgenius/dify/pull/7741

> Update package "libldap-2.5-0" for docker build. by @snickerjp in https://github.com/langgenius/dify/pull/7726

> feat: add support for array types in available variable list by @YidaHu in https://github.com/langgenius/dify/pull/7715

> chore: improve http executor configs by @bowenliang123 in https://github.com/langgenius/dify/pull/7730

> chore: ignore openai error record in sentry by @takatost in https://github.com/langgenius/dify/pull/7770

> Update ssrf_proxy related doc link in docker-compose file by @htynkn in https://github.com/langgenius/dify/pull/7778

> Sync Input component from feat/attachments branch by @douxc in https://github.com/langgenius/dify/pull/7782

> chore: add app generator overload by @Yeuoly in https://github.com/langgenius/dify/pull/7792

> feat: support auth by api key for ark provider by @sinomoe in https://github.com/langgenius/dify/pull/7845

> refactor: Remove typecasting by any by @MH4GF in https://github.com/langgenius/dify/pull/7862

> Add ALIYUN_OSS_PATH configuration for Aliyun OSS by @Seayon in https://github.com/langgenius/dify/pull/7864

> Add perplexity search as a new tool by @leilei-jiang in https://github.com/langgenius/dify/pull/7861

> Add Russian language by @d8rt8v in https://github.com/langgenius/dify/pull/7860

> ignore linked images when image id is none by @JohnJyong in https://github.com/langgenius/dify/pull/7890

> feat: allow users to use the app icon as the answer icon by @kurokobo in https://github.com/langgenius/dify/pull/7888

> chore(Dockerfile): Bump expat to 2.6.2-2 by @laipz8200 in https://github.com/langgenius/dify/pull/7904

> chore: Update versions to 0.7.3 by @laipz8200 in https://github.com/langgenius/dify/pull/7895

Source: https://github.com/langgenius/dify/releases/tag/0.7.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-03-4-apps-and-integrations-changes-in-0-7-3|4 Apps and Integrations changes in 0.7.3]] · Apps and Integrations
- [[Changes/Dify/2024-09-03-2-interface-experience-changes-in-0-7-3|2 Interface Experience changes in 0.7.3]] · Interface Experience
- [[Changes/Dify/2024-09-03-3-developer-workflow-changes-in-0-7-3|3 Developer Workflow changes in 0.7.3]] · Developer Workflow
- [[Changes/Dify/2024-09-03-4-pricing-model-changes-in-0-7-3|4 Pricing Model changes in 0.7.3]] · Pricing Model
- [[Changes/Dify/2024-09-03-4-safety-and-privacy-changes-in-0-7-3|4 Safety and Privacy changes in 0.7.3]] · Safety and Privacy
- [[Changes/Dify/2024-09-03-3-files-and-data-changes-in-0-7-3|3 Files and Data changes in 0.7.3]] · Files and Data
- [[Changes/Dify/2024-09-03-3-model-support-changes-in-0-7-3|3 Model Support changes in 0.7.3]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-03-349b2e&body=Card%3A%20Changes%2FDify%2F2024-09-03-60-other-changes-in-0-7-3.md%0ACard%20ID%3A%20dify-2024-09-03-349b2e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.7.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->