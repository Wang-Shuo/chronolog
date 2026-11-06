---
card_id: dify-2025-03-18-c944b8
date: '2025-03-18'
description: 'Dify · 2025-03-18 · Other changes: 51 changes in v1.1.0 — Welcome to
  v1.1.0! This release packs a punch with significant improvements, enhancements,
  and the…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8f5893f30feaaf8081b9e1e34694aaa08022d4b79ba98b721bca84f7534f7db
product: dify
product_name: Dify
record:
  card_id: dify-2025-03-18-c944b8
  comparison: ''
  date: '2025-03-18'
  description: 'Dify — v1.1.0: 51 other changes'
  evidence:
  - quote: 'Welcome to v1.1.0! This release packs a punch with significant improvements,
      enhancements, and the introduction of some much-awaited features. Here''s what
      we''ve got:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Metadata Filtering for Knowledge Retrieval** by @JohnJyong in #15982
      and #16063. Metadata filtering enhances the retrieval and accuracy of relevant
      data in knowledge bases by leveraging custom metadata attributes. This makes
      finding the right data quicker and more precise. To get more information, please
      read [our blog](https://dify.ai/blog/dify-v1-1-0-filtering-knowledge-retrieval-with-customized-metadata).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '![image](https://github.com/user-attachments/assets/2321e288-4311-4aa6-bd91-8481a43d823c)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**IF-ELSE Node Improvements**: Handles missing optional file variables
      seamlessly by @lrhan321 in #15693.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Increased Maximum Number of Parallelism Branches** by @XiaoBa-Yu in
      #15964.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**HTTP request node now supports skipping SSL verification** by @sho-takano-dev
      in #15664.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Fixed SQL Injection Vulnerabilities in Vector DB** by @JohnJyong in
      #16096. *We recommend users upgrade to this version immediately to mitigate
      risks.*'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Resolved Conditional Branches That Disrupted Streaming Output** by @Nov1c444
      in #14065.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Fixed Trace Return Null Issues Causing Page Crashes** by @iamjoel in
      #15588.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Corrected Missing Translations** by @crazywoola in #4212.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Improved Handling of Unicode in Keyword Search Queries** by @kenwoodjw
      in #15522.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Fixed Dataset Re-Ranking Mode to Handle Optional Fields Gracefully**
      by @JohnJyong in #15643.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Fixed Nginx Template Environment Variable Replacement Issues** by @LiuBodong
      in #15651.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Improved InputNumber Component Behavior** by @ACAne0320 in #16044.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Opensandal Version Update** by @yihong0618 in #14343.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Updated default Milvus URI value** by @codingjaguar in #13140.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: '**Ruff Linting Fixes** bump to 0.11.0 by @bowenliang123 in #15953.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Stop the API server, Worker, and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'Get the latest code from the release branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Finally, run the API server, Worker, and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore: update opendal version by @yihong0618 in https://github.com/langgenius/dify/pull/14343'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'feat: add debounced enter key submission to install form (#15445) by @jw0903
      in https://github.com/langgenius/dify/pull/15542'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore: remove unused parameter by @crazywoola in https://github.com/langgenius/dify/pull/15558'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore: use TenantAccountRole instead of TenantAccountJoinRole by @jiangbo721
      in https://github.com/langgenius/dify/pull/15514'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'feat: env MAX_TOOLS_NUM by @rafaelncarvalho in https://github.com/langgenius/dify/pull/15431'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Update .env.example to fix MILVUS_URI default value by @codingjaguar in
      https://github.com/langgenius/dify/pull/13140
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: improve text split by @JohnJyong in https://github.com/langgenius/dify/pull/15719
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'Feat: Add pg_bigm for keyword search in pgvector by @utsumi-fj in https://github.com/langgenius/dify/pull/13876'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'feat: add keyboard shortcuts support for dialog confirmation by @ACAne0320
      in https://github.com/langgenius/dify/pull/15752'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'feat: add Http Request Node to skip ssl verify function #15177 by @sho-takano-dev
      in https://github.com/langgenius/dify/pull/15664'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore: remove useless doc and font by @hjlarry in https://github.com/langgenius/dify/pull/15838'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore(api): improve type hints for BaseNode and its subclasses by @QuantumGhost
      in https://github.com/langgenius/dify/pull/15826'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'Chore: remove unused fields by @hyongtao-db in https://github.com/langgenius/dify/pull/15764'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: When decrypt_trace_config is empty, it should be skipped directly by @shaxiaozz
      in https://github.com/langgenius/dify/pull/15870
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore: bump ruff to 0.11.0 and fix linting violations by @bowenliang123
      in https://github.com/langgenius/dify/pull/15953'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'feat: support openGauss vector database by @LittleFish-15 in https://github.com/langgenius/dify/pull/15865'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore: enhance ListWrapper and PluginPage components with stable scro…
      by @fdb02983rhy in https://github.com/langgenius/dify/pull/16048'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'feat: add Maximum number of Parallelism branches to env by @XiaoBa-Yu
      in https://github.com/langgenius/dify/pull/15964'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'Chore: PromptMessage is not an abstract base class by @hyongtao-db in
      https://github.com/langgenius/dify/pull/15965'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Feat/upgrade knowledge metabase by @zxhlyh in https://github.com/langgenius/dify/pull/16063
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: support config filename in meta for create_blob_message by @StoneFancyX
      in https://github.com/langgenius/dify/pull/15605
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'doc: auto correct the doc using autocorrect close #16091 by @yihong0618
      in https://github.com/langgenius/dify/pull/16092'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Feat：app list dark mode by @JzoNgKVO in https://github.com/langgenius/dify/pull/16110
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: Support knowledge metadata filter by @JohnJyong in https://github.com/langgenius/dify/pull/15982
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  - quote: 'chore: bump version to 1.1.0 by @laipz8200 in https://github.com/langgenius/dify/pull/16128'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 51-other-changes-in-1-1-0
  source_release: dify-2025-03-18-1-1-0-github-206514946-497d593d
  source_type: github_releases
  theme: uncategorized
  title: 51 other changes in 1.1.0
  type: change
source_release: '[[Releases/Dify/dify-2025-03-18-1-1-0-github-206514946-497d593d|dify-2025-03-18-1-1-0-github-206514946-497d593d]]'
source_type: github_releases
theme: uncategorized
title: 51 other changes in 1.1.0
type: change
---

<!-- chronolog:begin region="header" -->
# 51 other changes in 1.1.0

**Dify** · 2025-03-18 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.1.0) · from [[Releases/Dify/dify-2025-03-18-1-1-0-github-206514946-497d593d|v1.1.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Welcome to v1.1.0! This release packs a punch with significant improvements, enhancements, and the introduction of some much-awaited features. Here's what we've got:

> **Metadata Filtering for Knowledge Retrieval** by @JohnJyong in #15982 and #16063. Metadata filtering enhances the retrieval and accuracy of relevant data in knowledge bases by leveraging custom metadata attributes. This makes finding the right data quicker and more precise. To get more information, please read [our blog](https://dify.ai/blog/dify-v1-1-0-filtering-knowledge-retrieval-with-customized-metadata).

> ![image](https://github.com/user-attachments/assets/2321e288-4311-4aa6-bd91-8481a43d823c)

> **IF-ELSE Node Improvements**: Handles missing optional file variables seamlessly by @lrhan321 in #15693.

> **Increased Maximum Number of Parallelism Branches** by @XiaoBa-Yu in #15964.

> **HTTP request node now supports skipping SSL verification** by @sho-takano-dev in #15664.

> **Fixed SQL Injection Vulnerabilities in Vector DB** by @JohnJyong in #16096. *We recommend users upgrade to this version immediately to mitigate risks.*

> **Resolved Conditional Branches That Disrupted Streaming Output** by @Nov1c444 in #14065.

> **Fixed Trace Return Null Issues Causing Page Crashes** by @iamjoel in #15588.

> **Corrected Missing Translations** by @crazywoola in #4212.

> **Improved Handling of Unicode in Keyword Search Queries** by @kenwoodjw in #15522.

> **Fixed Dataset Re-Ranking Mode to Handle Optional Fields Gracefully** by @JohnJyong in #15643.

> **Fixed Nginx Template Environment Variable Replacement Issues** by @LiuBodong in #15651.

> **Improved InputNumber Component Behavior** by @ACAne0320 in #16044.

> **Opensandal Version Update** by @yihong0618 in #14343.

> **Updated default Milvus URI value** by @codingjaguar in #13140.

> **Ruff Linting Fixes** bump to 0.11.0 by @bowenliang123 in #15953.

> Back up your customized docker-compose YAML file (optional)

> Get the latest code from the main branch

> Back up data

> Upgrade services

> Stop the API server, Worker, and Web frontend Server.

> Get the latest code from the release branch:

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run the API server, Worker, and Web frontend Server again.

> chore: update opendal version by @yihong0618 in https://github.com/langgenius/dify/pull/14343

> feat: add debounced enter key submission to install form (#15445) by @jw0903 in https://github.com/langgenius/dify/pull/15542

> chore: remove unused parameter by @crazywoola in https://github.com/langgenius/dify/pull/15558

> chore: use TenantAccountRole instead of TenantAccountJoinRole by @jiangbo721 in https://github.com/langgenius/dify/pull/15514

> feat: env MAX_TOOLS_NUM by @rafaelncarvalho in https://github.com/langgenius/dify/pull/15431

> Update .env.example to fix MILVUS_URI default value by @codingjaguar in https://github.com/langgenius/dify/pull/13140

> improve text split by @JohnJyong in https://github.com/langgenius/dify/pull/15719

> Feat: Add pg_bigm for keyword search in pgvector by @utsumi-fj in https://github.com/langgenius/dify/pull/13876

> feat: add keyboard shortcuts support for dialog confirmation by @ACAne0320 in https://github.com/langgenius/dify/pull/15752

> feat: add Http Request Node to skip ssl verify function #15177 by @sho-takano-dev in https://github.com/langgenius/dify/pull/15664

> chore: remove useless doc and font by @hjlarry in https://github.com/langgenius/dify/pull/15838

> chore(api): improve type hints for BaseNode and its subclasses by @QuantumGhost in https://github.com/langgenius/dify/pull/15826

> Chore: remove unused fields by @hyongtao-db in https://github.com/langgenius/dify/pull/15764

> When decrypt_trace_config is empty, it should be skipped directly by @shaxiaozz in https://github.com/langgenius/dify/pull/15870

> chore: bump ruff to 0.11.0 and fix linting violations by @bowenliang123 in https://github.com/langgenius/dify/pull/15953

> feat: support openGauss vector database by @LittleFish-15 in https://github.com/langgenius/dify/pull/15865

> chore: enhance ListWrapper and PluginPage components with stable scro… by @fdb02983rhy in https://github.com/langgenius/dify/pull/16048

> feat: add Maximum number of Parallelism branches to env by @XiaoBa-Yu in https://github.com/langgenius/dify/pull/15964

> Chore: PromptMessage is not an abstract base class by @hyongtao-db in https://github.com/langgenius/dify/pull/15965

> Feat/upgrade knowledge metabase by @zxhlyh in https://github.com/langgenius/dify/pull/16063

> support config filename in meta for create_blob_message by @StoneFancyX in https://github.com/langgenius/dify/pull/15605

> doc: auto correct the doc using autocorrect close #16091 by @yihong0618 in https://github.com/langgenius/dify/pull/16092

> Feat：app list dark mode by @JzoNgKVO in https://github.com/langgenius/dify/pull/16110

> Support knowledge metadata filter by @JohnJyong in https://github.com/langgenius/dify/pull/15982

> chore: bump version to 1.1.0 by @laipz8200 in https://github.com/langgenius/dify/pull/16128

Source: https://github.com/langgenius/dify/releases/tag/1.1.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-03-18-feat-add-click-away-and-mounting-logic-to-agent-setting-component-by-fdb02983rhy|feat: add click-away and mounting logic to agent setting component]] · Agent Mode
- [[Changes/Dify/2025-03-18-ci-deploy-enterprise-by-garearc-in-https-github-com-langgenius-dify-pull-15699|Ci/deploy enterprise]] · Enterprise and Administration
- [[Changes/Dify/2025-03-18-2-files-and-data-changes-in-1-1-0|2 Files and Data changes in 1.1.0]] · Files and Data
- [[Changes/Dify/2025-03-18-enhanced-integration-of-pg-bigm-for-keyword-search-in-pgvector-by-utsumi-fj-in-1|Enhanced Integration of pg_bigm for Keyword Search in pgvector by @utsumi-fj in ♯13876]] · Apps and Integrations
- [[Changes/Dify/2025-03-18-2-model-support-changes-in-1-1-0|2 Model Support changes in 1.1.0]] · Model Support
- [[Changes/Dify/2025-03-18-3-developer-workflow-changes-in-1-1-0|3 Developer Workflow changes in 1.1.0]] · Developer Workflow
- [[Changes/Dify/2025-03-18-this-release-aims-to-strengthen-our-platform-s-reliability-security-and-usabilit|This release aims to strengthen our platform's reliability, security, and usability…]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-03-18-c944b8&body=Card%3A%20Changes%2FDify%2F2025-03-18-51-other-changes-in-1-1-0.md%0ACard%20ID%3A%20dify-2025-03-18-c944b8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.1.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->