---
card_id: dify-2025-07-10-9decca
date: '2025-07-10'
description: "Dify · 2025-07-10 · Other changes: 54 changes in v1.6.0 — Welcome to
  version 1.6.0! \U0001F389\U0001F389\U0001F389 This release is packed with new features,
  crucial fixes, and various…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2e413ad74b63bc08b3d728a27763e0378d936d6a5f0733f528315a47c1f975e8
product: dify
product_name: Dify
record:
  card_id: dify-2025-07-10-9decca
  comparison: ''
  date: '2025-07-10'
  description: 'Dify — v1.6.0: 54 other changes'
  evidence:
  - quote: "Welcome to version 1.6.0! \U0001F389\U0001F389\U0001F389 This release
      is packed with new features, crucial fixes, and various optimisations aimed
      at enhancing your experience. We've listened to your feedback and made significant
      improvements across the board."
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '![image](https://github.com/user-attachments/assets/16fadc71-b085-4c2f-a948-f5cc36345c2d)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '**Drag-and-Drop for Topics**: Now, you can easily reorder your topics
      list with a drag-and-drop sorting feature. (See #22066, by *Minamiyama*)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '**SSL Verify Toggle**: You now have the ability to change SSL verification
      settings in the HTTP Node. (See #22052, by *Davide Delbianco*)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '**Batch Embedding Optimisation**: Optimised batch embeddings and Qdrant
      write consistency. (See #21776, by *luckylhb90*)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '**Redis Fallback Mechanism**: Added a robust fallback mechanism for Redis
      to ensure data resilience. (See #21044, by *NeatGuyCoding*)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '**Json Output Issue**: Resolved an issue with JSON output that was affecting
      data consistency. (See #22053, by *baonudesifeizhai*)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '**Variable Name Uniqueness**: Ensured unique variable names in the list
      to avoid conflicts. (See #22038, by *Minamiyama*)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: '**Overflow Hidden Fix in Drawer**: Ensured that the copy button remains
      clickable by adding overflow hidden. (See #22103, by *Heyang Wang*)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Stop the service. Please execute in the docker directory
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Stop the API server, Worker, and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'Get the latest code from the release branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Finally, run the API server, Worker, and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: remove unused config CURRENT_VERSION by @bowenliang123 in https://github.com/langgenius/dify/pull/21832
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Chore/workflow last run by @zxhlyh in https://github.com/langgenius/dify/pull/21823
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'chore: add message status enum by @jiangbo721 in https://github.com/langgenius/dify/pull/21825'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat(variables): auto replace spaces with underscores in variable name
      inputs by @Minamiyama in https://github.com/langgenius/dify/pull/21843'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: use repair_json fix json parse error of HTTPRequestNode by @ZombieBlue
      in https://github.com/langgenius/dify/pull/21909
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Feat list query by @ZeroZ-lab in https://github.com/langgenius/dify/pull/21907
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: test:add unit test for api version config by @bowenliang123 in https://github.com/langgenius/dify/pull/21919
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'minor fix: removes the duplicated handling logic for TracingProviderEnum.ARIZE
      and TracingProviderEnum.PHOENIX from the OpsTraceProviderConfigMap by @NeatGuyCoding
      in https://github.com/langgenius/dify/pull/21927'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'refactor(web): Restructure the operation buttons layout in the app information
      component (#21742) by @HyaCiovo in https://github.com/langgenius/dify/pull/21818'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'minor fix: translation for pause by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21949'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'chore(i18n): fix typos and improve Korean translation by @heojawon in
      https://github.com/langgenius/dify/pull/21955'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'refactor: extract common url validator for config_entity.py by @NeatGuyCoding
      in https://github.com/langgenius/dify/pull/21934'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat: Add support for type="hidden" input elements in Markdown forms by
      @mizoo-snow21 in https://github.com/langgenius/dify/pull/21922'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'refactor(graph_engine): Take GraphRuntimeState out of GraphEngine by @laipz8200
      in https://github.com/langgenius/dify/pull/21882'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'ENH(ui): enhance check list by @Minamiyama in https://github.com/langgenius/dify/pull/21932'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'chore(docker): increase NGINX_CLIENT_MAX_BODY_SIZE from 15M to 100M i…
      by @lrhan321 in https://github.com/langgenius/dify/pull/21995'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'Chore: remove unreachable code by @hyongtao-db in https://github.com/langgenius/dify/pull/21986'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat: add unit tests and validation for aliyun tracing by @NeatGuyCoding
      in https://github.com/langgenius/dify/pull/22012'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'test: add unit tests for password validation and hashing by @farion1231
      in https://github.com/langgenius/dify/pull/22003'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: don't add search params when opening detail links from marketplace. by
      @douxc in https://github.com/langgenius/dify/pull/22034
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'test: add comprehensive unit tests for UrlSigner by @farion1231 in https://github.com/langgenius/dify/pull/22030'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: Remove tow unused files by @hyongtao-db in https://github.com/langgenius/dify/pull/22022
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'Feat: description field for env variables by @Minamiyama in https://github.com/langgenius/dify/pull/21556'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat: Allow to change SSL verify in HTTP Node by @DavideDelbianco in https://github.com/langgenius/dify/pull/22052'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat(libs): Introduce `extract_tenant_id` by @laipz8200 in https://github.com/langgenius/dify/pull/22086'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'test: add comprehensive unit tests for encrypter module by @farion1231
      in https://github.com/langgenius/dify/pull/22102'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat(question-classifier): add drag-and-drop sorting for topics list by
      @Minamiyama in https://github.com/langgenius/dify/pull/22066'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'chore: Update theme vars by @WTW0313 in https://github.com/langgenius/dify/pull/22113'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'optimize: batch embedding and qdrant write_consistency_factor parameter
      by @luckylhb90 in https://github.com/langgenius/dify/pull/21776'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat: add redis fallback mechanism #21043 by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21044'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'Chore: rm useless import and vars by @hyongtao-db in https://github.com/langgenius/dify/pull/22108'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/22132'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: update worklow events logs. by @zhanluxianshen in https://github.com/langgenius/dify/pull/19871
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'feat: add support for dark icons in provider and tool entities by @Yeuoly
      in https://github.com/langgenius/dify/pull/22081'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  - quote: 'chore(version): bump to 1.6.0 by @Mairuis in https://github.com/langgenius/dify/pull/22136'
    source_release: https://github.com/langgenius/dify/releases/tag/1.6.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 54-other-changes-in-1-6-0
  source_release: dify-2025-07-10-1-6-0-github-231400193-9181f945
  source_type: github_releases
  theme: uncategorized
  title: 54 other changes in 1.6.0
  type: change
source_release: '[[Releases/Dify/dify-2025-07-10-1-6-0-github-231400193-9181f945|dify-2025-07-10-1-6-0-github-231400193-9181f945]]'
source_type: github_releases
theme: uncategorized
title: 54 other changes in 1.6.0
type: change
---

<!-- chronolog:begin region="header" -->
# 54 other changes in 1.6.0

**Dify** · 2025-07-10 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.6.0) · from [[Releases/Dify/dify-2025-07-10-1-6-0-github-231400193-9181f945|v1.6.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Welcome to version 1.6.0! 🎉🎉🎉 This release is packed with new features, crucial fixes, and various optimisations aimed at enhancing your experience. We've listened to your feedback and made significant improvements across the board.

> ![image](https://github.com/user-attachments/assets/16fadc71-b085-4c2f-a948-f5cc36345c2d)

> **Drag-and-Drop for Topics**: Now, you can easily reorder your topics list with a drag-and-drop sorting feature. (See #22066, by *Minamiyama*)

> **SSL Verify Toggle**: You now have the ability to change SSL verification settings in the HTTP Node. (See #22052, by *Davide Delbianco*)

> **Batch Embedding Optimisation**: Optimised batch embeddings and Qdrant write consistency. (See #21776, by *luckylhb90*)

> **Redis Fallback Mechanism**: Added a robust fallback mechanism for Redis to ensure data resilience. (See #21044, by *NeatGuyCoding*)

> **Json Output Issue**: Resolved an issue with JSON output that was affecting data consistency. (See #22053, by *baonudesifeizhai*)

> **Variable Name Uniqueness**: Ensured unique variable names in the list to avoid conflicts. (See #22038, by *Minamiyama*)

> **Overflow Hidden Fix in Drawer**: Ensured that the copy button remains clickable by adding overflow hidden. (See #22103, by *Heyang Wang*)

> Back up your customized docker-compose YAML file (optional)

> Get the latest code from the main branch

> Stop the service. Please execute in the docker directory

> Back up data

> Upgrade services

> Stop the API server, Worker, and Web frontend Server.

> Get the latest code from the release branch:

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run the API server, Worker, and Web frontend Server again.

> remove unused config CURRENT_VERSION by @bowenliang123 in https://github.com/langgenius/dify/pull/21832

> Chore/workflow last run by @zxhlyh in https://github.com/langgenius/dify/pull/21823

> chore: add message status enum by @jiangbo721 in https://github.com/langgenius/dify/pull/21825

> feat(variables): auto replace spaces with underscores in variable name inputs by @Minamiyama in https://github.com/langgenius/dify/pull/21843

> use repair_json fix json parse error of HTTPRequestNode by @ZombieBlue in https://github.com/langgenius/dify/pull/21909

> Feat list query by @ZeroZ-lab in https://github.com/langgenius/dify/pull/21907

> test:add unit test for api version config by @bowenliang123 in https://github.com/langgenius/dify/pull/21919

> minor fix: removes the duplicated handling logic for TracingProviderEnum.ARIZE and TracingProviderEnum.PHOENIX from the OpsTraceProviderConfigMap by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21927

> refactor(web): Restructure the operation buttons layout in the app information component (#21742) by @HyaCiovo in https://github.com/langgenius/dify/pull/21818

> minor fix: translation for pause by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21949

> chore(i18n): fix typos and improve Korean translation by @heojawon in https://github.com/langgenius/dify/pull/21955

> refactor: extract common url validator for config_entity.py by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21934

> feat: Add support for type="hidden" input elements in Markdown forms by @mizoo-snow21 in https://github.com/langgenius/dify/pull/21922

> refactor(graph_engine): Take GraphRuntimeState out of GraphEngine by @laipz8200 in https://github.com/langgenius/dify/pull/21882

> ENH(ui): enhance check list by @Minamiyama in https://github.com/langgenius/dify/pull/21932

> chore(docker): increase NGINX_CLIENT_MAX_BODY_SIZE from 15M to 100M i… by @lrhan321 in https://github.com/langgenius/dify/pull/21995

> Chore: remove unreachable code by @hyongtao-db in https://github.com/langgenius/dify/pull/21986

> feat: add unit tests and validation for aliyun tracing by @NeatGuyCoding in https://github.com/langgenius/dify/pull/22012

> test: add unit tests for password validation and hashing by @farion1231 in https://github.com/langgenius/dify/pull/22003

> don't add search params when opening detail links from marketplace. by @douxc in https://github.com/langgenius/dify/pull/22034

> test: add comprehensive unit tests for UrlSigner by @farion1231 in https://github.com/langgenius/dify/pull/22030

> Remove tow unused files by @hyongtao-db in https://github.com/langgenius/dify/pull/22022

> Feat: description field for env variables by @Minamiyama in https://github.com/langgenius/dify/pull/21556

> feat: Allow to change SSL verify in HTTP Node by @DavideDelbianco in https://github.com/langgenius/dify/pull/22052

> feat(libs): Introduce `extract_tenant_id` by @laipz8200 in https://github.com/langgenius/dify/pull/22086

> test: add comprehensive unit tests for encrypter module by @farion1231 in https://github.com/langgenius/dify/pull/22102

> feat(question-classifier): add drag-and-drop sorting for topics list by @Minamiyama in https://github.com/langgenius/dify/pull/22066

> chore: Update theme vars by @WTW0313 in https://github.com/langgenius/dify/pull/22113

> optimize: batch embedding and qdrant write_consistency_factor parameter by @luckylhb90 in https://github.com/langgenius/dify/pull/21776

> feat: add redis fallback mechanism #21043 by @NeatGuyCoding in https://github.com/langgenius/dify/pull/21044

> Chore: rm useless import and vars by @hyongtao-db in https://github.com/langgenius/dify/pull/22108

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/22132

> update worklow events logs. by @zhanluxianshen in https://github.com/langgenius/dify/pull/19871

> feat: add support for dark icons in provider and tool entities by @Yeuoly in https://github.com/langgenius/dify/pull/22081

> chore(version): bump to 1.6.0 by @Mairuis in https://github.com/langgenius/dify/pull/22136

Source: https://github.com/langgenius/dify/releases/tag/1.6.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-07-10-2-editor-experience-changes-in-1-6-0|2 Editor Experience changes in 1.6.0]] · Editor Experience
- [[Changes/Dify/2025-07-10-optimize-the-memory-usage-of-tencent-vector-database-by-wlleiiwang-in-https-gith|Optimize the memory usage of Tencent Vector Database]] · Reliability and Performance
- [[Changes/Dify/2025-07-10-feat-retain-llm-setting-for-agent-node-by-fdb02983rhy-in-https-github-com-langge|feat: Retain llm setting for agent node]] · Agent Mode
- [[Changes/Dify/2025-07-10-10-apps-and-integrations-changes-in-1-6-0|10 Apps and Integrations changes in 1.6.0]] · Apps and Integrations
- [[Changes/Dify/2025-07-10-2-interface-experience-changes-in-1-6-0|2 Interface Experience changes in 1.6.0]] · Interface Experience
- [[Changes/Dify/2025-07-10-style-config-var-update-styling-classes-to-use-design-system-tokens-by-minamiyam|style(config-var): update styling classes to use design system tokens]] · Context Window
- [[Changes/Dify/2025-07-10-3-files-and-data-changes-in-1-6-0|3 Files and Data changes in 1.6.0]] · Files and Data
- [[Changes/Dify/2025-07-10-4-model-support-changes-in-1-6-0|4 Model Support changes in 1.6.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-07-10-9decca&body=Card%3A%20Changes%2FDify%2F2025-07-10-54-other-changes-in-1-6-0.md%0ACard%20ID%3A%20dify-2025-07-10-9decca%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.6.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->