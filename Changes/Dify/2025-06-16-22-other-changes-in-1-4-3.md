---
card_id: dify-2025-06-16-1689b5
date: '2025-06-16'
description: 'Dify · 2025-06-16 · Other changes: 22 changes in v1.4.3 — It’s all about
  smoothing out the wrinkles and enhancing flexibility in this update. Here’s the…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 81222627fb2f21d0c770c78cd4f02d3f72d768cce577da16fec3ae5664174b16
product: dify
product_name: Dify
record:
  card_id: dify-2025-06-16-1689b5
  comparison: ''
  date: '2025-06-16'
  description: 'Dify — v1.4.3: 22 other changes'
  evidence:
  - quote: 'It’s all about smoothing out the wrinkles and enhancing flexibility in
      this update. Here’s the rundown:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: '**Markdown Button Fix**: Sending messages through the Markdown button
      should now work flawlessly, thanks to @hjlarry in [#20933](https://github.com/langgenius/dify/pull/20933).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: '**App Info Update**: For better transparency, the author_name is now part
      of the app info, thanks to @quicksandznzn in [#20973](https://github.com/langgenius/dify/pull/20973).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: '**Documentation Link Fixes**: We’ve generalized the method for retrieving
      documentation links to respect localizations and squashed those error link paths,
      thanks to insights from @bowenliang123 in [#20801](https://github.com/langgenius/dify/pull/20801).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Stop the service. Please execute in the docker directory
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Stop the API server, Worker, and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'Get the latest code from the release branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Finally, run the API server, Worker, and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'refactor(sqlalchemy_workflow_execution_repository): Use the max funtion
      for getting next_sequence_number. by @laipz8200 in https://github.com/langgenius/dify/pull/20966'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'chore: app info add author_name by @quicksandznzn in https://github.com/langgenius/dify/pull/20973'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'refactor: generalize method for getting doc link respecting locale and
      fix error link paths by @bowenliang123 in https://github.com/langgenius/dify/pull/20801'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'docs: conv and user_id by @alterxyz in https://github.com/langgenius/dify/pull/21004'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'test: run vdb test of oceanbase with docker compose in CI tests by @bowenliang123
      in https://github.com/langgenius/dify/pull/20945'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: Feat/add rag dev deploy by @JohnJyong in https://github.com/langgenius/dify/pull/21049
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'chore: rename workflow blocks by @zxhlyh in https://github.com/langgenius/dify/pull/21052'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  - quote: 'chore: bump version to 1.4.3 by @laipz8200 in https://github.com/langgenius/dify/pull/21045'
    source_release: https://github.com/langgenius/dify/releases/tag/1.4.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 22-other-changes-in-1-4-3
  source_release: dify-2025-06-16-1-4-3-github-225472835-d7a5d7fa
  source_type: github_releases
  theme: uncategorized
  title: 22 other changes in 1.4.3
  type: change
source_release: '[[Releases/Dify/dify-2025-06-16-1-4-3-github-225472835-d7a5d7fa|dify-2025-06-16-1-4-3-github-225472835-d7a5d7fa]]'
source_type: github_releases
theme: uncategorized
title: 22 other changes in 1.4.3
type: change
---

<!-- chronolog:begin region="header" -->
# 22 other changes in 1.4.3

**Dify** · 2025-06-16 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.4.3) · from [[Releases/Dify/dify-2025-06-16-1-4-3-github-225472835-d7a5d7fa|v1.4.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> It’s all about smoothing out the wrinkles and enhancing flexibility in this update. Here’s the rundown:

> **Markdown Button Fix**: Sending messages through the Markdown button should now work flawlessly, thanks to @hjlarry in [#20933](https://github.com/langgenius/dify/pull/20933).

> **App Info Update**: For better transparency, the author_name is now part of the app info, thanks to @quicksandznzn in [#20973](https://github.com/langgenius/dify/pull/20973).

> **Documentation Link Fixes**: We’ve generalized the method for retrieving documentation links to respect localizations and squashed those error link paths, thanks to insights from @bowenliang123 in [#20801](https://github.com/langgenius/dify/pull/20801).

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

> refactor(sqlalchemy_workflow_execution_repository): Use the max funtion for getting next_sequence_number. by @laipz8200 in https://github.com/langgenius/dify/pull/20966

> chore: app info add author_name by @quicksandznzn in https://github.com/langgenius/dify/pull/20973

> refactor: generalize method for getting doc link respecting locale and fix error link paths by @bowenliang123 in https://github.com/langgenius/dify/pull/20801

> docs: conv and user_id by @alterxyz in https://github.com/langgenius/dify/pull/21004

> test: run vdb test of oceanbase with docker compose in CI tests by @bowenliang123 in https://github.com/langgenius/dify/pull/20945

> Feat/add rag dev deploy by @JohnJyong in https://github.com/langgenius/dify/pull/21049

> chore: rename workflow blocks by @zxhlyh in https://github.com/langgenius/dify/pull/21052

> chore: bump version to 1.4.3 by @laipz8200 in https://github.com/langgenius/dify/pull/21045

Source: https://github.com/langgenius/dify/releases/tag/1.4.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-06-16-conversation-panel-optimization-we-ve-fine-tuned-the-width-adjustment-logic-for|Conversation Panel Optimization]] · Interface Experience
- [[Changes/Dify/2025-06-16-2-files-and-data-changes-in-1-4-3|2 Files and Data changes in 1.4.3]] · Files and Data
- [[Changes/Dify/2025-06-16-login-rate-limit-clearing-after-a-password-reset-we-ve-made-sure-the-login-rate|Login Rate Limit Clearing]] · Account and Access
- [[Changes/Dify/2025-06-16-3-model-support-changes-in-1-4-3|3 Model Support changes in 1.4.3]] · Model Support
- [[Changes/Dify/2025-06-16-keep-those-pull-requests-coming-as-we-aim-to-make-your-user-experience-as-seamle|Keep those pull requests coming as we aim to make your user experience as seamless…]] · Developer Workflow
- [[Changes/Dify/2025-06-16-localized-documentation-updates-documentation-link-updates-now-support-localizat|Localized Documentation Updates]] · Accessibility and Localization
- [[Changes/Dify/2025-06-16-2-apps-and-integrations-changes-in-1-4-3|2 Apps and Integrations changes in 1.4.3]] · Apps and Integrations
- [[Changes/Dify/2025-06-16-dead-code-cleanup-we-ve-removed-some-obsolete-code-utilizing-vulture-keeping-our|Dead Code Cleanup]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-06-16-1689b5&body=Card%3A%20Changes%2FDify%2F2025-06-16-22-other-changes-in-1-4-3.md%0ACard%20ID%3A%20dify-2025-06-16-1689b5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.4.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->