---
card_id: dify-2024-09-30-400e73
date: '2024-09-30'
description: 'Dify · 2024-09-30 · Other changes: 17 changes in v0.9.1 — We''ve shipped
  version 0.9.1 and it’s all about tightening up those loose ends. Let’s dive into
  what’s…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8c160fc4038085de4d42576ebfcbb369a6e98d3e1d79fbf2ca92a39064b4112
product: dify
product_name: Dify
record:
  card_id: dify-2024-09-30-400e73
  comparison: ''
  date: '2024-09-30'
  description: 'Dify — v0.9.1: 17 other changes'
  evidence:
  - quote: 'We''ve shipped version 0.9.1 and it’s all about tightening up those loose
      ends. Let’s dive into what’s been improved:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: '**Dataset Updates Refined**: We''ve streamlined the process for updating
      original datasets by removing unnecessary parameters. Kudos to @JohnJyong for
      ironing this out in #8935 and #8939. Less clutter, smoother update experience.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: '**Web Page Import via Jina**: If you''ve hit a snag with importing web
      pages using Jina, the fix is now in place. Thanks to @douxc, those pesky errors
      should be a thing of the past in #8937.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: '**Internal Dataset Request Params**: Adjustments have been made to correct
      request parameters for internal datasets, ensuring your data requests play nice.
      Thanks, @YIXIAO0, for handling this in #8940.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: '> [!WARNING]'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: '> The `docker-compose.yaml` has been refactored. If you''ve made any changes
      to the file, make sure to check out the "Upgrade to new docker compose deployment"
      section above for usage and migration tips.'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: Stop API server, Worker and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: Finally, run API server, Worker and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: original dataset update issue by @JohnJyong in https://github.com/langgenius/dify/pull/8935
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: original dataset update remove unuseful parameters by @JohnJyong in https://github.com/langgenius/dify/pull/8939
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  - quote: 'chore(version): bump to 0.9.1 by @laipz8200 in https://github.com/langgenius/dify/pull/8938'
    source_release: https://github.com/langgenius/dify/releases/tag/0.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 17-other-changes-in-0-9-1
  source_release: dify-2024-09-30-0-9-1-github-177627506-02de3b97
  source_type: github_releases
  theme: uncategorized
  title: 17 other changes in 0.9.1
  type: change
source_release: '[[Releases/Dify/dify-2024-09-30-0-9-1-github-177627506-02de3b97|dify-2024-09-30-0-9-1-github-177627506-02de3b97]]'
source_type: github_releases
theme: uncategorized
title: 17 other changes in 0.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 17 other changes in 0.9.1

**Dify** · 2024-09-30 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.9.1) · from [[Releases/Dify/dify-2024-09-30-0-9-1-github-177627506-02de3b97|v0.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> We've shipped version 0.9.1 and it’s all about tightening up those loose ends. Let’s dive into what’s been improved:

> **Dataset Updates Refined**: We've streamlined the process for updating original datasets by removing unnecessary parameters. Kudos to @JohnJyong for ironing this out in #8935 and #8939. Less clutter, smoother update experience.

> **Web Page Import via Jina**: If you've hit a snag with importing web pages using Jina, the fix is now in place. Thanks to @douxc, those pesky errors should be a thing of the past in #8937.

> **Internal Dataset Request Params**: Adjustments have been made to correct request parameters for internal datasets, ensuring your data requests play nice. Thanks, @YIXIAO0, for handling this in #8940.

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

> original dataset update issue by @JohnJyong in https://github.com/langgenius/dify/pull/8935

> original dataset update remove unuseful parameters by @JohnJyong in https://github.com/langgenius/dify/pull/8939

> chore(version): bump to 0.9.1 by @laipz8200 in https://github.com/langgenius/dify/pull/8938

Source: https://github.com/langgenius/dify/releases/tag/0.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2024-09-30-2-reliability-and-performance-changes-in-0-9-1|2 Reliability and Performance changes in 0.9.1]] · Reliability and Performance
- [[Changes/Dify/2024-09-30-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service，Command, please execute in the docker directory]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2024-09-30-400e73&body=Card%3A%20Changes%2FDify%2F2024-09-30-17-other-changes-in-0-9-1.md%0ACard%20ID%3A%20dify-2024-09-30-400e73%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->