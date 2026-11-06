---
card_id: dify-2025-07-28-51666b
date: '2025-07-28'
description: 'Dify · 2025-07-28 · Other changes: 43 changes in v1.7.1 — Hello, Dify
  enthusiasts! We''re thrilled to announce version 1.7.1 of our platform, bringing
  a fresh…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ffd9d231cb4e4e29ce2f75bf5c729cad76c71ee957c58463ebae56f9fc80c254
product: dify
product_name: Dify
record:
  card_id: dify-2025-07-28-51666b
  comparison: ''
  date: '2025-07-28'
  description: 'Dify — v1.7.1: 43 other changes'
  evidence:
  - quote: 'Hello, Dify enthusiasts! We''re thrilled to announce version 1.7.1 of
      our platform, bringing a fresh batch of refinements and enhancements to your
      workflow. Here''s a breakdown of what''s changed:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: '**Default Value for Select Inputs**: Now you can set a default value for
      select input fields, providing a smoother user experience when working with
      forms. Thanks to @antonko. (#21192)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: '**OpenAPI Schema Enhancement**: Support for `allOf` in OpenAPI properties
      inside schema has been added, courtesy of @mike1936. It''s a big win for API
      design consistency. (#22975)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: '**K8s Pure Migration Option**: We''ve introduced a pure migration option
      for the `api` component within Kubernetes deployments, making migrations simpler
      for large-scale systems. Thanks, @BorisPolonsky ! (#22750)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: '**Revamped Tool List Page**: @nite-knite made the tool list page slicker
      and more user-friendly—check it out! (#22879)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: '**Duplicate TYPE_CHECKING Import**: Removed those unnecessary imports
      for sleeker code. Thanks, @hyongtao-db. (#23013)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: "Pulling all these improvements together, this release takes a big step
      forward in polishing everyday experiences and paving the way for future development.
      Enjoy the upgrade, and as always, reach out with feedback and ideas for what
      you'd love to see next. Keep coding! \U0001F680"
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Back up your customized docker-compose YAML file (optional)
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Get the latest code from the main branch
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Stop the service. Please execute in the docker directory
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Back up data
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Upgrade services
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Stop the API server, Worker, and Web frontend Server.
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'Get the latest code from the release branch:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'Update Python dependencies:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'Then, let''s run the migration script:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Finally, run the API server, Worker, and Web frontend Server again.
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'feat(k8s): Add pure migration option for `api` component by @BorisPolonsky
      in https://github.com/langgenius/dify/pull/22750'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'refactor: Change "filter" to "where" to match SQLAlchemy 2.x style. by
      @asukaminato0721 in https://github.com/langgenius/dify/pull/22801'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: add autofix by @asukaminato0721 in https://github.com/langgenius/dify/pull/22785
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'refactor(dayjs): Refactor internationalized time formatting feature (#22870)
      by @HyaCiovo in https://github.com/langgenius/dify/pull/22872'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'feat: revamp tool list page by @nite-knite in https://github.com/langgenius/dify/pull/22879'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'Feat: add notification for change email completed by @JzoNgKVO in https://github.com/langgenius/dify/pull/22812'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'refactor(i18next): streamline fallback translation handling and initi…
      by @WTW0313 in https://github.com/langgenius/dify/pull/22894'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Feat/change user email freezes limit by @zyssyz123 in https://github.com/langgenius/dify/pull/22900
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'chore: enhance error message when handling PluginInvokeError by @Yeuoly
      in https://github.com/langgenius/dify/pull/22908'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'Feat: change user email freezes limit by @JzoNgKVO in https://github.com/langgenius/dify/pull/22912'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'chore: translate i18n files by @github-actions[bot] in https://github.com/langgenius/dify/pull/22934'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'test: add comprehensive tests for file_factory build_from_mapping by @farion1231
      in https://github.com/langgenius/dify/pull/22926'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: make logging not use f-str, change others to f-str by @asukaminato0721
      in https://github.com/langgenius/dify/pull/22882
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'feat: clear all annotation by @leslie2046 in https://github.com/langgenius/dify/pull/22878'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Remove redundant condition check by @hyongtao-db in https://github.com/langgenius/dify/pull/22983
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: node title number on copied iteration node by @jubinsoni in https://github.com/langgenius/dify/pull/23004
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: adding LANG LC_ALL PYTHONIOENCODING UTF-8 by @jubinsoni in https://github.com/langgenius/dify/pull/22928
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: ability to select same type sub item by preserving children of both f…
      by @jubinsoni in https://github.com/langgenius/dify/pull/23002
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'Chore: remove duplicate TYPE_CHECKING import by @hyongtao-db in https://github.com/langgenius/dify/pull/23013'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: Rollback Aliyun Trace Icon File by @hieheihei in https://github.com/langgenius/dify/pull/23027
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'feat: Support allOf in OpenAPI properties inside schema #22946 by @mike1936
      in https://github.com/langgenius/dify/pull/22975'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'chore: Updata eslint config dependencies by @WTW0313 in https://github.com/langgenius/dify/pull/23040'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'feat: Support selecting variables in conditional filtering in list operations.
      by @leslie2046 in https://github.com/langgenius/dify/pull/23029'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'feat: default value option for select input fields by @antonko in https://github.com/langgenius/dify/pull/21192'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'refactor(web): Optimize workflow operation tip popup (#23051) by @HyaCiovo
      in https://github.com/langgenius/dify/pull/23052'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  - quote: 'chore(version): bump version to 1.7.1 by @QuantumGhost in https://github.com/langgenius/dify/pull/23048'
    source_release: https://github.com/langgenius/dify/releases/tag/1.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 43-other-changes-in-1-7-1
  source_release: dify-2025-07-28-1-7-1-github-235626993-47ad2206
  source_type: github_releases
  theme: uncategorized
  title: 43 other changes in 1.7.1
  type: change
source_release: '[[Releases/Dify/dify-2025-07-28-1-7-1-github-235626993-47ad2206|dify-2025-07-28-1-7-1-github-235626993-47ad2206]]'
source_type: github_releases
theme: uncategorized
title: 43 other changes in 1.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 43 other changes in 1.7.1

**Dify** · 2025-07-28 · Other changes · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.7.1) · from [[Releases/Dify/dify-2025-07-28-1-7-1-github-235626993-47ad2206|v1.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hello, Dify enthusiasts! We're thrilled to announce version 1.7.1 of our platform, bringing a fresh batch of refinements and enhancements to your workflow. Here's a breakdown of what's changed:

> **Default Value for Select Inputs**: Now you can set a default value for select input fields, providing a smoother user experience when working with forms. Thanks to @antonko. (#21192)

> **OpenAPI Schema Enhancement**: Support for `allOf` in OpenAPI properties inside schema has been added, courtesy of @mike1936. It's a big win for API design consistency. (#22975)

> **K8s Pure Migration Option**: We've introduced a pure migration option for the `api` component within Kubernetes deployments, making migrations simpler for large-scale systems. Thanks, @BorisPolonsky ! (#22750)

> **Revamped Tool List Page**: @nite-knite made the tool list page slicker and more user-friendly—check it out! (#22879)

> **Duplicate TYPE_CHECKING Import**: Removed those unnecessary imports for sleeker code. Thanks, @hyongtao-db. (#23013)

> Pulling all these improvements together, this release takes a big step forward in polishing everyday experiences and paving the way for future development. Enjoy the upgrade, and as always, reach out with feedback and ideas for what you'd love to see next. Keep coding! 🚀

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

> feat(k8s): Add pure migration option for `api` component by @BorisPolonsky in https://github.com/langgenius/dify/pull/22750

> refactor: Change "filter" to "where" to match SQLAlchemy 2.x style. by @asukaminato0721 in https://github.com/langgenius/dify/pull/22801

> add autofix by @asukaminato0721 in https://github.com/langgenius/dify/pull/22785

> refactor(dayjs): Refactor internationalized time formatting feature (#22870) by @HyaCiovo in https://github.com/langgenius/dify/pull/22872

> feat: revamp tool list page by @nite-knite in https://github.com/langgenius/dify/pull/22879

> Feat: add notification for change email completed by @JzoNgKVO in https://github.com/langgenius/dify/pull/22812

> refactor(i18next): streamline fallback translation handling and initi… by @WTW0313 in https://github.com/langgenius/dify/pull/22894

> Feat/change user email freezes limit by @zyssyz123 in https://github.com/langgenius/dify/pull/22900

> chore: enhance error message when handling PluginInvokeError by @Yeuoly in https://github.com/langgenius/dify/pull/22908

> Feat: change user email freezes limit by @JzoNgKVO in https://github.com/langgenius/dify/pull/22912

> chore: translate i18n files by @github-actions[bot] in https://github.com/langgenius/dify/pull/22934

> test: add comprehensive tests for file_factory build_from_mapping by @farion1231 in https://github.com/langgenius/dify/pull/22926

> make logging not use f-str, change others to f-str by @asukaminato0721 in https://github.com/langgenius/dify/pull/22882

> feat: clear all annotation by @leslie2046 in https://github.com/langgenius/dify/pull/22878

> Remove redundant condition check by @hyongtao-db in https://github.com/langgenius/dify/pull/22983

> node title number on copied iteration node by @jubinsoni in https://github.com/langgenius/dify/pull/23004

> adding LANG LC_ALL PYTHONIOENCODING UTF-8 by @jubinsoni in https://github.com/langgenius/dify/pull/22928

> ability to select same type sub item by preserving children of both f… by @jubinsoni in https://github.com/langgenius/dify/pull/23002

> Chore: remove duplicate TYPE_CHECKING import by @hyongtao-db in https://github.com/langgenius/dify/pull/23013

> Rollback Aliyun Trace Icon File by @hieheihei in https://github.com/langgenius/dify/pull/23027

> feat: Support allOf in OpenAPI properties inside schema #22946 by @mike1936 in https://github.com/langgenius/dify/pull/22975

> chore: Updata eslint config dependencies by @WTW0313 in https://github.com/langgenius/dify/pull/23040

> feat: Support selecting variables in conditional filtering in list operations. by @leslie2046 in https://github.com/langgenius/dify/pull/23029

> feat: default value option for select input fields by @antonko in https://github.com/langgenius/dify/pull/21192

> refactor(web): Optimize workflow operation tip popup (#23051) by @HyaCiovo in https://github.com/langgenius/dify/pull/23052

> chore(version): bump version to 1.7.1 by @QuantumGhost in https://github.com/langgenius/dify/pull/23048

Source: https://github.com/langgenius/dify/releases/tag/1.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-07-28-3-interface-experience-changes-in-1-7-1|3 Interface Experience changes in 1.7.1]] · Interface Experience
- [[Changes/Dify/2025-07-28-time-formatting-internationalization-the-time-formatting-feature-has-been-refact|Time Formatting Internationalization]] · Accessibility and Localization
- [[Changes/Dify/2025-07-28-postgresql-healthcheck-enhanced-the-healthcheck-command-to-avoid-fatal-log-error|PostgreSQL Healthcheck: Enhanced the healthcheck command to avoid fatal log…]] · Developer Workflow
- [[Changes/Dify/2025-07-28-2-files-and-data-changes-in-1-7-1|2 Files and Data changes in 1.7.1]] · Files and Data
- [[Changes/Dify/2025-07-28-2-model-support-changes-in-1-7-1|2 Model Support changes in 1.7.1]] · Model Support
- [[Changes/Dify/2025-07-28-2-apps-and-integrations-changes-in-1-7-1|2 Apps and Integrations changes in 1.7.1]] · Apps and Integrations
- [[Changes/Dify/2025-07-28-windows-pem-keypath-fix-corrected-path-errors-for-private-pem-key-files-on-windo|Windows PEM KeyPath Fix]] · Mobile and Desktop
- [[Changes/Dify/2025-07-28-test-add-comprehensive-integration-tests-for-api-key-authentication-system-by-fa|test: add comprehensive integration tests for API key authentication system]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-07-28-51666b&body=Card%3A%20Changes%2FDify%2F2025-07-28-43-other-changes-in-1-7-1.md%0ACard%20ID%3A%20dify-2025-07-28-51666b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->