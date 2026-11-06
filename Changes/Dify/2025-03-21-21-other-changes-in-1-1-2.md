---
card_id: dify-2025-03-21-fb9dae
date: '2025-03-21'
description: 'Dify · 2025-03-21 · Other changes: 21 changes in v1.1.2 — > [!Important]'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9e8301d970d55354bcd39682972e05a0061ff672054c50fca89f4e54bdcd82f2
product: dify
product_name: Dify
record:
  card_id: dify-2025-03-21-fb9dae
  comparison: ''
  date: '2025-03-21'
  description: 'Dify — v1.1.2: 21 other changes'
  evidence:
  - quote: '> [!Important]'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: '> 1. Your service is exposed to the internet.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: '> 2. You provide external WebApps.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: '> 3. You have not configured `SERVICE_API_URL` and `FILES_URL` on different
      domains.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: '**Knowledge Base Cleanup**: Fixed an issue where the OpenAPI interface
      couldn''t delete metadata, thanks to @StrayDragon in #16365. Now clearing out
      old or unnecessary metadata is straightforward.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: '**Metadata Migration Check**: Added a check for built-in fields during
      old metadata migration to ensure completeness and accuracy, contributed by @JohnJyong
      in #16371. Your metadata migrations have stepped up in robustness.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: '**Literal Syntax Error Handling**: Fixed errors related to `literal_eval`
      function usage, courtesy of @svcvit in #16297. These changes help keep your
      code from breaking due to syntax evaluation.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: "This update is all about refining the edges and enhancing the user experience—an
      essential pit-stop on our road to new features and capabilities. Keep those
      contributions and feedback coming, and let's make Dify even better, together!
      \U0001F680"
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: Stop the API server, Worker, and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: 'Get the latest code from the release branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: Finally, run the API server, Worker, and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: add built-in field check when doing old metadata migrate by @JohnJyong
      in https://github.com/langgenius/dify/pull/16371
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: 'Chore: frontend infrastructure upgrade by @iamjoel in https://github.com/langgenius/dify/pull/16420'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: 'feat: replace file content type to avoid load script in svg. by @laipz8200
      in https://github.com/langgenius/dify/pull/16454'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  - quote: 'chore(api): enhance ruff rules to disallow dangerous functions and modules
      by @QuantumGhost in https://github.com/langgenius/dify/pull/16461'
    source_release: https://github.com/langgenius/dify/releases/tag/1.1.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 21-other-changes-in-1-1-2
  source_release: dify-2025-03-21-1-1-2-github-207382802-6a01a92e
  source_type: github_releases
  theme: uncategorized
  title: 21 other changes in 1.1.2
  type: change
source_release: '[[Releases/Dify/dify-2025-03-21-1-1-2-github-207382802-6a01a92e|dify-2025-03-21-1-1-2-github-207382802-6a01a92e]]'
source_type: github_releases
theme: uncategorized
title: 21 other changes in 1.1.2
type: change
---

<!-- chronolog:begin region="header" -->
# 21 other changes in 1.1.2

**Dify** · 2025-03-21 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.1.2) · from [[Releases/Dify/dify-2025-03-21-1-1-2-github-207382802-6a01a92e|v1.1.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > [!Important]

> > 1. Your service is exposed to the internet.

> > 2. You provide external WebApps.

> > 3. You have not configured `SERVICE_API_URL` and `FILES_URL` on different domains.

> **Knowledge Base Cleanup**: Fixed an issue where the OpenAPI interface couldn't delete metadata, thanks to @StrayDragon in #16365. Now clearing out old or unnecessary metadata is straightforward.

> **Metadata Migration Check**: Added a check for built-in fields during old metadata migration to ensure completeness and accuracy, contributed by @JohnJyong in #16371. Your metadata migrations have stepped up in robustness.

> **Literal Syntax Error Handling**: Fixed errors related to `literal_eval` function usage, courtesy of @svcvit in #16297. These changes help keep your code from breaking due to syntax evaluation.

> This update is all about refining the edges and enhancing the user experience—an essential pit-stop on our road to new features and capabilities. Keep those contributions and feedback coming, and let's make Dify even better, together! 🚀

> Back up your customized docker-compose YAML file (optional)

> Get the latest code from the main branch

> Back up data

> Upgrade services

> Stop the API server, Worker, and Web frontend Server.

> Get the latest code from the release branch:

> Update Python dependencies:

> Then, let's run the migration script:

> Finally, run the API server, Worker, and Web frontend Server again.

> add built-in field check when doing old metadata migrate by @JohnJyong in https://github.com/langgenius/dify/pull/16371

> Chore: frontend infrastructure upgrade by @iamjoel in https://github.com/langgenius/dify/pull/16420

> feat: replace file content type to avoid load script in svg. by @laipz8200 in https://github.com/langgenius/dify/pull/16454

> chore(api): enhance ruff rules to disallow dangerous functions and modules by @QuantumGhost in https://github.com/langgenius/dify/pull/16461

Source: https://github.com/langgenius/dify/releases/tag/1.1.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-03-21-3-safety-and-privacy-changes-in-1-1-2|3 Safety and Privacy changes in 1.1.2]] · Safety and Privacy
- [[Changes/Dify/2025-03-21-stop-the-service-command-please-execute-in-the-docker-directory|Stop the service, Command, please execute in the docker directory]] · Developer Workflow
- [[Changes/Dify/2025-03-21-this-version-disables-the-svg-rendering-in-the-message-if-you-are-using-our-comm| This version disables the SVG rendering in the message]] · Interface Experience
- [[Changes/Dify/2025-03-21-github-plugin-installation-resolved-an-import-dsl-issue-that-blocked-the-install|GitHub Plugin Installation]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-03-21-fb9dae&body=Card%3A%20Changes%2FDify%2F2025-03-21-21-other-changes-in-1-1-2.md%0ACard%20ID%3A%20dify-2025-03-21-fb9dae%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.1.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->