---
card_id: dify-2024-05-13-6dfbe7
date: '2024-05-13'
description: 'Dify · 2024-05-13 · Other changes: 33 changes in v0.6.8 GPT-4o is available
  now in Dify — Hey folks, we''ve rolled out version 0.6.8 of our platform and it''s…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 50e3c0bd043bb3025e9c571aa76c43722a25100e07c3a8c047dc714c0fc36253
product: dify
product_name: Dify
record:
  card_id: dify-2024-05-13-6dfbe7
  comparison: ''
  date: '2024-05-13'
  description: 'Dify — v0.6.8 GPT-4o is available now in Dify: 33 other changes'
  evidence:
  - quote: 'Hey folks, we''ve rolled out version 0.6.8 of our platform and it''s packed
      with some new features, enhancements, and fixes. Here’s a quick rundown of what’s
      new:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Code node with upgraded network support and additional Python dependencies
      by @Yeuoly in #4231.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Added support for Google Storage by @KiyotakaMatsushita in #4266.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Korean language support (ko-KR) by @qkdxorjs1002 in #4333.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Optimized workflow graph sync by @takatost in #4251 and @zxhlyh in #4250.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: Now, you won't lose any workflow graph data when switching between multiple
      tabs in the browser. It's instantly synced to the latest draft version!
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: Before, the tracing of the workflow might expose the log details of the
      nodes to the end-users, now we have disabled it.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Increased max steps to 50 in workflows by @takatost in #4252.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Question classifier prompt optimization for better accuracy by @JohnJyong
      in #4262.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: After optimization, the classification results will be more accurate.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Optimized install form for better user experience by @TinsFox in #4154.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: For additional enhancements and updates, refer to the What's Changed section
      below.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Get the latest code from the main branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'refactor: install form by @TinsFox in https://github.com/langgenius/dify/pull/4154'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'feat: workflow interaction by @zxhlyh in https://github.com/langgenius/dify/pull/4214'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'chore: workflow sync with hash by @zxhlyh in https://github.com/langgenius/dify/pull/4250'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'feat: Add draft hash check in workflow by @takatost in https://github.com/langgenius/dify/pull/4251'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'feat: increase max steps to 50 in workflow by @takatost in https://github.com/langgenius/dify/pull/4252'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: correct comparison chart by @guchenhe in https://github.com/langgenius/dify/pull/4254
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: Feat/vector db pgvector by @vaayne in https://github.com/langgenius/dify/pull/3879
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: question classifier prompt optimize by @JohnJyong in https://github.com/langgenius/dify/pull/4262
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'feat: Add storage type and Google Storage settings to worker by @KiyotakaMatsushita
      in https://github.com/langgenius/dify/pull/4266'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'feat: hide node detail outputs in webapp & installed app in explore by
      @takatost in https://github.com/langgenius/dify/pull/3954'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: Update docker-compose.yaml by @rechardwang in https://github.com/langgenius/dify/pull/4288
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: Update README.md to remove outdated badge by @guchenhe in https://github.com/langgenius/dify/pull/4302
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'chore: update gmpy2_pkcs10aep_cipher.py by @eltociear in https://github.com/langgenius/dify/pull/4314'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'improve: code upgrade by @Yeuoly in https://github.com/langgenius/dify/pull/4231'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: 'feat: i18n: add korean language (ko-KR) by @qkdxorjs1002 in https://github.com/langgenius/dify/pull/4333'
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  - quote: version to 0.6.8 by @takatost in https://github.com/langgenius/dify/pull/4347
    source_release: https://github.com/langgenius/dify/releases/tag/0.6.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 33-other-changes-in-0-6-8
  source_release: dify-2024-05-13-0-6-8-github-155567404-54e0e464
  source_type: github_releases
  theme: uncategorized
  title: 33 other changes in 0.6.8
  type: change
source_release: '[[Releases/Dify/dify-2024-05-13-0-6-8-github-155567404-54e0e464|dify-2024-05-13-0-6-8-github-155567404-54e0e464]]'
source_type: github_releases
theme: uncategorized
title: 33 other changes in 0.6.8
type: change
---

<!-- chronolog:begin region="header" -->
# 33 other changes in 0.6.8

**Dify** · 2024-05-13 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.6.8) · from [[Releases/Dify/dify-2024-05-13-0-6-8-github-155567404-54e0e464|v0.6.8 GPT-4o is available now in Dify]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hey folks, we've rolled out version 0.6.8 of our platform and it's packed with some new features, enhancements, and fixes. Here’s a quick rundown of what’s new:

> Code node with upgraded network support and additional Python dependencies by @Yeuoly in #4231.

> Added support for Google Storage by @KiyotakaMatsushita in #4266.

> Korean language support (ko-KR) by @qkdxorjs1002 in #4333.

> Optimized workflow graph sync by @takatost in #4251 and @zxhlyh in #4250.

> Now, you won't lose any workflow graph data when switching between multiple tabs in the browser. It's instantly synced to the latest draft version!

> Before, the tracing of the workflow might expose the log details of the nodes to the end-users, now we have disabled it.

> Increased max steps to 50 in workflows by @takatost in #4252.

> Question classifier prompt optimization for better accuracy by @JohnJyong in #4262.

> After optimization, the classification results will be more accurate.

> Optimized install form for better user experience by @TinsFox in #4154.

> For additional enhancements and updates, refer to the What's Changed section below.

> Get the latest code from the main branch:

> Stop API server, Worker and Web frontend Server.

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run API server, Worker and Web frontend Server again.

> refactor: install form by @TinsFox in https://github.com/langgenius/dify/pull/4154

> feat: workflow interaction by @zxhlyh in https://github.com/langgenius/dify/pull/4214

> chore: workflow sync with hash by @zxhlyh in https://github.com/langgenius/dify/pull/4250

> feat: Add draft hash check in workflow by @takatost in https://github.com/langgenius/dify/pull/4251

> feat: increase max steps to 50 in workflow by @takatost in https://github.com/langgenius/dify/pull/4252

> correct comparison chart by @guchenhe in https://github.com/langgenius/dify/pull/4254

> Feat/vector db pgvector by @vaayne in https://github.com/langgenius/dify/pull/3879

> question classifier prompt optimize by @JohnJyong in https://github.com/langgenius/dify/pull/4262

> feat: Add storage type and Google Storage settings to worker by @KiyotakaMatsushita in https://github.com/langgenius/dify/pull/4266

> feat: hide node detail outputs in webapp & installed app in explore by @takatost in https://github.com/langgenius/dify/pull/3954

> Update docker-compose.yaml by @rechardwang in https://github.com/langgenius/dify/pull/4288

> Update README.md to remove outdated badge by @guchenhe in https://github.com/langgenius/dify/pull/4302

> chore: update gmpy2_pkcs10aep_cipher.py by @eltociear in https://github.com/langgenius/dify/pull/4314

> improve: code upgrade by @Yeuoly in https://github.com/langgenius/dify/pull/4231

> feat: i18n: add korean language (ko-KR) by @qkdxorjs1002 in https://github.com/langgenius/dify/pull/4333

> version to 0.6.8 by @takatost in https://github.com/langgenius/dify/pull/4347

Source: https://github.com/langgenius/dify/releases/tag/0.6.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-05-13-12-model-support-changes-in-0-6-8|12 Model Support changes in 0.6.8]] · Model Support
- [[Changes/Dify/2024-05-13-4-apps-and-integrations-changes-in-0-6-8|4 Apps and Integrations changes in 0.6.8]] · Apps and Integrations
- [[Changes/Dify/2024-05-13-feat-support-copy-run-text-result-in-debug-panel-in-workflow-by-iamjoel-in-https|feat: support copy run text result in debug panel in workflow]] · Developer Workflow
- [[Changes/Dify/2024-05-13-and-we-also-removed-the-need-for-sys-admin-permission-for-the-sandbox-service|And we also removed the need for SYS_ADMIN permission for the sandbox service]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-05-13-6dfbe7&body=Card%3A%20Changes%2FDify%2F2024-05-13-33-other-changes-in-0-6-8.md%0ACard%20ID%3A%20dify-2024-05-13-6dfbe7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.6.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->