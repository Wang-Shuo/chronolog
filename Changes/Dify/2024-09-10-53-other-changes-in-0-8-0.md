---
card_id: dify-2024-09-10-f7470d
date: '2024-09-10'
description: 'Dify · 2024-09-10 · Other changes: 53 changes in v0.8.0 — Hey everyone,
  we’re excited to announce the release of version 0.8.0! This update brings a mix
  of new…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 902b5377d5ffadb8e0623983f6188ecd02d571073627614b44ccb3baeea7cff5
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-10-f7470d
  comparison: ''
  date: '2024-09-10'
  description: 'Dify — v0.8.0: 53 other changes'
  evidence:
  - quote: 'Hey everyone, we’re excited to announce the release of version 0.8.0!
      This update brings a mix of new features, enhancements, and crucial bug fixes.
      Here’s a quick rundown:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '**Parallel Execution of Nodes in Workflows** by @takatost, @zxhlyh, and
      @YIXIAO0 in #8192.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '![image](https://github.com/user-attachments/assets/98b209a1-d72e-4e8b-8bfe-7ca0babf27c4)'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Dive deeper into the details and unleash the full potential of these new
      features by exploring our [latest blog post](https://dify.ai/blog/accelerating-workflow-processing-with-parallel-branch)
      and [documentation](https://docs.dify.ai/guides/workflow/orchestrate-node)!
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '**Deprecate N to 1 Retrieval** by @zxhlyh in #8134'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: The N-to-1 retrieval strategy is officially deprecated in this version,
      of which the entrance will be closed but applications that have selected this
      feature will still be retained. We recommend switching to the more flexible
      multi-path retrieval strategy to boost your application's retrieval efficiency.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '**Update App Published Time After Clicking Publish Button**: The published
      time of an app now updates correctly when you click the publish button by @vicoooo26
      in #7801'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '**Fix Notion Table Extract**: Fixed issues with extracting data from Notion
      tables by @JohnJyong in #7925'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '**Fix Nvidia Rerank Top N Missed**: Addressed issues with Nvidia rerank
      top N functionality by @JohnJyong in #8185'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '**Fix Claude Credential Validation**: Resolved credential validation issues
      for Claude by @crazywoola in #8109'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: "That’s it for this release! As always, we appreciate your feedback and
      contributions. Do it for you! \U0001F680"
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat: support auto generate i18n translate by @iamjoel in https://github.com/langgenius/dify/pull/6964'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: improve the notion table extract by @JohnJyong in https://github.com/langgenius/dify/pull/7925
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: #7603 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7931'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Chore/add default step 1x url by @crazywoola in https://github.com/langgenius/dify/pull/7933
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Chore/add roadmap by @crazywoola in https://github.com/langgenius/dify/pull/7943
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: #7943 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7948'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'Revert "fix: an issue of keyword search feature in application log list"
      by @takatost in https://github.com/langgenius/dify/pull/7949'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'Feat: update app published time after clicking publish button by @vicoooo26
      in https://github.com/langgenius/dify/pull/7801'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat: add health check for pg and redis in docker-compose.middleware.yaml
      (#7961) by @hwzhuhao in https://github.com/langgenius/dify/pull/7962'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/7965'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Update milvus-standalone version and expose required ports for the container.
      by @winsonwhe in https://github.com/langgenius/dify/pull/7709
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: support huawei cloud obs storage (#7980) by @hwzhuhao in https://github.com/langgenius/dify/pull/7981
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: #7348, support query conversations by updated_at by @ZuzooVn in
      https://github.com/langgenius/dify/pull/8047'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: ifEsle node add regex match by @charli117 in https://github.com/langgenius/dify/pull/8007
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: If else add regexmatch by @crazywoola in https://github.com/langgenius/dify/pull/8059
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'Revert "fix: parameter rule" by @AAEE86 in https://github.com/langgenius/dify/pull/8070'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat: support redis sentinel mode by @erigo in https://github.com/langgenius/dify/pull/7756'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: feat:add fishaudio in xinference by @leslie2046 in https://github.com/langgenius/dify/pull/8100
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: keep dify compose file consistent format by @soulteary in https://github.com/langgenius/dify/pull/8102'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: offline n to 1 retrieval by @zxhlyh in https://github.com/langgenius/dify/pull/8134'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8135'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: Update LICENSE - remove 'SaaS' from restriction term definition by @guchenhe
      in https://github.com/langgenius/dify/pull/8143
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: update qwen-long max token by @crazywoola in https://github.com/langgenius/dify/pull/8157
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: add volcengine tos storage by @yaoice in https://github.com/langgenius/dify/pull/8164
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: code merge error by @JohnJyong in https://github.com/langgenius/dify/pull/8183
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: upgrade expat from 2.6.2-2 to 2.6.3-1 by @ZuzooVn in https://github.com/langgenius/dify/pull/8182'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: nvidia rerank top n missed by @JohnJyong in https://github.com/langgenius/dify/pull/8185
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'docs: replace docker-compose with docker compose by @crazywoola in https://github.com/langgenius/dify/pull/8195'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'feat: Parallel Execution of Nodes in Workflows by @takatost in https://github.com/langgenius/dify/pull/8192'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8202'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: 'chore(api/core): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7624'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  - quote: revert page column by @JohnJyong in https://github.com/langgenius/dify/pull/8217
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 53-other-changes-in-0-8-0
  source_release: dify-2024-09-10-0-8-0-github-174308904-2a45a31c
  source_type: github_releases
  theme: uncategorized
  title: 53 other changes in 0.8.0
  type: change
source_release: '[[Releases/Dify/dify-2024-09-10-0-8-0-github-174308904-2a45a31c|dify-2024-09-10-0-8-0-github-174308904-2a45a31c]]'
source_type: github_releases
theme: uncategorized
title: 53 other changes in 0.8.0
type: change
---

<!-- chronolog:begin region="header" -->
# 53 other changes in 0.8.0

**Dify** · 2024-09-10 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.8.0) · from [[Releases/Dify/dify-2024-09-10-0-8-0-github-174308904-2a45a31c|v0.8.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hey everyone, we’re excited to announce the release of version 0.8.0! This update brings a mix of new features, enhancements, and crucial bug fixes. Here’s a quick rundown:

> **Parallel Execution of Nodes in Workflows** by @takatost, @zxhlyh, and @YIXIAO0 in #8192.

> ![image](https://github.com/user-attachments/assets/98b209a1-d72e-4e8b-8bfe-7ca0babf27c4)

> Dive deeper into the details and unleash the full potential of these new features by exploring our [latest blog post](https://dify.ai/blog/accelerating-workflow-processing-with-parallel-branch) and [documentation](https://docs.dify.ai/guides/workflow/orchestrate-node)!

> **Deprecate N to 1 Retrieval** by @zxhlyh in #8134

> The N-to-1 retrieval strategy is officially deprecated in this version, of which the entrance will be closed but applications that have selected this feature will still be retained. We recommend switching to the more flexible multi-path retrieval strategy to boost your application's retrieval efficiency.

> **Update App Published Time After Clicking Publish Button**: The published time of an app now updates correctly when you click the publish button by @vicoooo26 in #7801

> **Fix Notion Table Extract**: Fixed issues with extracting data from Notion tables by @JohnJyong in #7925

> **Fix Nvidia Rerank Top N Missed**: Addressed issues with Nvidia rerank top N functionality by @JohnJyong in #8185

> **Fix Claude Credential Validation**: Resolved credential validation issues for Claude by @crazywoola in #8109

> That’s it for this release! As always, we appreciate your feedback and contributions. Do it for you! 🚀

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

> feat: support auto generate i18n translate by @iamjoel in https://github.com/langgenius/dify/pull/6964

> improve the notion table extract by @JohnJyong in https://github.com/langgenius/dify/pull/7925

> chore: #7603 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7931

> Chore/add default step 1x url by @crazywoola in https://github.com/langgenius/dify/pull/7933

> Chore/add roadmap by @crazywoola in https://github.com/langgenius/dify/pull/7943

> chore: #7943 i18n by @ZuzooVn in https://github.com/langgenius/dify/pull/7948

> Revert "fix: an issue of keyword search feature in application log list" by @takatost in https://github.com/langgenius/dify/pull/7949

> Feat: update app published time after clicking publish button by @vicoooo26 in https://github.com/langgenius/dify/pull/7801

> feat: add health check for pg and redis in docker-compose.middleware.yaml (#7961) by @hwzhuhao in https://github.com/langgenius/dify/pull/7962

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/7965

> Update milvus-standalone version and expose required ports for the container. by @winsonwhe in https://github.com/langgenius/dify/pull/7709

> support huawei cloud obs storage (#7980) by @hwzhuhao in https://github.com/langgenius/dify/pull/7981

> chore: #7348, support query conversations by updated_at by @ZuzooVn in https://github.com/langgenius/dify/pull/8047

> ifEsle node add regex match by @charli117 in https://github.com/langgenius/dify/pull/8007

> If else add regexmatch by @crazywoola in https://github.com/langgenius/dify/pull/8059

> Revert "fix: parameter rule" by @AAEE86 in https://github.com/langgenius/dify/pull/8070

> feat: support redis sentinel mode by @erigo in https://github.com/langgenius/dify/pull/7756

> feat:add fishaudio in xinference by @leslie2046 in https://github.com/langgenius/dify/pull/8100

> chore: keep dify compose file consistent format by @soulteary in https://github.com/langgenius/dify/pull/8102

> chore: offline n to 1 retrieval by @zxhlyh in https://github.com/langgenius/dify/pull/8134

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8135

> Update LICENSE - remove 'SaaS' from restriction term definition by @guchenhe in https://github.com/langgenius/dify/pull/8143

> update qwen-long max token by @crazywoola in https://github.com/langgenius/dify/pull/8157

> add volcengine tos storage by @yaoice in https://github.com/langgenius/dify/pull/8164

> code merge error by @JohnJyong in https://github.com/langgenius/dify/pull/8183

> chore: upgrade expat from 2.6.2-2 to 2.6.3-1 by @ZuzooVn in https://github.com/langgenius/dify/pull/8182

> nvidia rerank top n missed by @JohnJyong in https://github.com/langgenius/dify/pull/8185

> docs: replace docker-compose with docker compose by @crazywoola in https://github.com/langgenius/dify/pull/8195

> feat: Parallel Execution of Nodes in Workflows by @takatost in https://github.com/langgenius/dify/pull/8192

> chore: translate i18n files by @github-actions in https://github.com/langgenius/dify/pull/8202

> chore(api/core): apply ruff reformatting by @bowenliang123 in https://github.com/langgenius/dify/pull/7624

> revert page column by @JohnJyong in https://github.com/langgenius/dify/pull/8217

Source: https://github.com/langgenius/dify/releases/tag/0.8.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-10-refactor-api-core-improve-type-hints-and-apply-ruff-formatter-in-agent-runner-an|refactor(api/core): Improve type hints and apply ruff formatter in agent runner…]] · Agent Mode
- [[Changes/Dify/2024-09-10-2-pricing-model-changes-in-0-8-0|2 Pricing Model changes in 0.8.0]] · Pricing Model
- [[Changes/Dify/2024-09-10-11-model-support-changes-in-0-8-0|11 Model Support changes in 0.8.0]] · Model Support
- [[Changes/Dify/2024-09-10-3-voice-and-audio-changes-in-0-8-0|3 Voice and Audio changes in 0.8.0]] · Voice and Audio
- [[Changes/Dify/2024-09-10-nodes-can-now-be-executed-in-parallel-within-a-workflow-greatly-increasing-the-e|Nodes can now be executed in parallel within a workflow, greatly increasing…]] · Reliability and Performance
- [[Changes/Dify/2024-09-10-add-dify-sandbox-health-check-in-docker-compose-yaml-8121-by-hwzhuhao-in-https-g|add dify-sandbox health check in docker-compose.yaml (♯8121)]] · Safety and Privacy
- [[Changes/Dify/2024-09-10-2-developer-workflow-changes-in-0-8-0|2 Developer Workflow changes in 0.8.0]] · Developer Workflow
- [[Changes/Dify/2024-09-10-feat-return-page-number-of-pdf-documents-upon-retrieval-by-jasonkang14-in-https|feat: return page number of pdf documents upon retrieval]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-10-f7470d&body=Card%3A%20Changes%2FDify%2F2024-09-10-53-other-changes-in-0-8-0.md%0ACard%20ID%3A%20dify-2024-09-10-f7470d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.8.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->