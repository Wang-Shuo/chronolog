---
card_id: dify-2024-09-13-ed7207
date: '2024-09-13'
description: 'Dify · 2024-09-13 · Other changes: 18 changes in v0.8.2 — Hey everyone,
  we''ve got some fresh updates in version 0.8.2 that are all about making your experience…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e36d9e4eed496e9237ee3a8c18b90de191f8e1868e499ed8f7246677e8f63394
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-13-ed7207
  comparison: ''
  date: '2024-09-13'
  description: 'Dify — v0.8.2: 18 other changes'
  evidence:
  - quote: 'Hey everyone, we''ve got some fresh updates in version 0.8.2 that are
      all about making your experience smoother and more efficient. Here''s the lowdown:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: '**Service API Workflow Logs**: Thanks to @fanlia in #8323, you can now
      access detailed workflow logs via the service API. This is a big win for those
      of you who need to keep a close eye on what''s happening under the hood.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: '**Workflow Var-Selector Update**: Fixed a bug where the var-selector wasn''t
      updating when edges changed in workflows. Kudos to @HiChen404 for this fix in
      #8259.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: '**Copy and Paste Shortcut**: Resolved an issue with the copy and paste
      shortcut in the textarea of the workflow run panel, making text manipulation
      a breeze again. Thanks to @YIXIAO0 for the fix in #8345.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: That's it for this release! Keep those feedback and contributions coming,
      and let's keep making this platform even better together.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: Feature/service api workflow logs by @fanlia in https://github.com/langgenius/dify/pull/8323
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: 'feat: add langfuse sentry ignore error by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/8353'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  - quote: 'chore: update version to 0.8.2 in packaging and docker-compose files by
      @laipz8200 in https://github.com/langgenius/dify/pull/8352'
    source_release: https://github.com/langgenius/dify/releases/tag/0.8.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 18-other-changes-in-0-8-2
  source_release: dify-2024-09-13-0-8-2-github-174888917-656dae82
  source_type: github_releases
  theme: uncategorized
  title: 18 other changes in 0.8.2
  type: change
source_release: '[[Releases/Dify/dify-2024-09-13-0-8-2-github-174888917-656dae82|dify-2024-09-13-0-8-2-github-174888917-656dae82]]'
source_type: github_releases
theme: uncategorized
title: 18 other changes in 0.8.2
type: change
---

<!-- chronolog:begin region="header" -->
# 18 other changes in 0.8.2

**Dify** · 2024-09-13 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.8.2) · from [[Releases/Dify/dify-2024-09-13-0-8-2-github-174888917-656dae82|v0.8.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hey everyone, we've got some fresh updates in version 0.8.2 that are all about making your experience smoother and more efficient. Here's the lowdown:

> **Service API Workflow Logs**: Thanks to @fanlia in #8323, you can now access detailed workflow logs via the service API. This is a big win for those of you who need to keep a close eye on what's happening under the hood.

> **Workflow Var-Selector Update**: Fixed a bug where the var-selector wasn't updating when edges changed in workflows. Kudos to @HiChen404 for this fix in #8259.

> **Copy and Paste Shortcut**: Resolved an issue with the copy and paste shortcut in the textarea of the workflow run panel, making text manipulation a breeze again. Thanks to @YIXIAO0 for the fix in #8345.

> That's it for this release! Keep those feedback and contributions coming, and let's keep making this platform even better together.

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

> Feature/service api workflow logs by @fanlia in https://github.com/langgenius/dify/pull/8323

> feat: add langfuse sentry ignore error by @ZhouhaoJiang in https://github.com/langgenius/dify/pull/8353

> chore: update version to 0.8.2 in packaging and docker-compose files by @laipz8200 in https://github.com/langgenius/dify/pull/8352

Source: https://github.com/langgenius/dify/releases/tag/0.8.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-13-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2024-09-13-2-model-support-changes-in-0-8-2|2 Model Support changes in 0.8.2]] · Model Support
- [[Changes/Dify/2024-09-13-score-threshold-fix-addressed-an-issue-where-the-score-threshold-was-set-to-none|Score Threshold Fix]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-13-ed7207&body=Card%3A%20Changes%2FDify%2F2024-09-13-18-other-changes-in-0-8-2.md%0ACard%20ID%3A%20dify-2024-09-13-ed7207%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.8.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->