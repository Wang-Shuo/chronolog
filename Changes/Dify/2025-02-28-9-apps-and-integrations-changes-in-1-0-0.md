---
card_id: dify-2025-02-28-b5cbb9
date: '2025-02-28'
description: 'Dify · 2025-02-28 · Apps and Integrations: 9 changes in v1.0.0 — Plugins
  are modular components that extend AI applications with plug-and-play simplicity.
  Now…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2268
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2d7b975f1fb35582e0ddf4f100e91b3e454848e0929606f7fb4c9dbd1da9fce8
product: dify
product_name: Dify
record:
  card_id: dify-2025-02-28-b5cbb9
  comparison: ''
  date: '2025-02-28'
  description: 'Dify — v1.0.0: 9 Apps and Integrations changes'
  evidence:
  - quote: Plugins are modular components that extend AI applications with plug-and-play
      simplicity. Now you can assemble external services and custom functionalities
      with your Dify apps effortlessly.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: We've developed a plugin system, a standard for Dify that lets users create
      plugins with the suffix .difypkg. By installing different plugin packages, you
      can add various capabilities to Dify.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: We've also introduced a new type of plugin called Extension, which is a
      custom service hosted within Dify. You can customize this service's code through
      plugins to handle external Webhook events.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: We've launched the Dify Marketplace, a centralized platform where plugins
      can be freely shared, allowing users to publish and download different plugins.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: 'The first step in upgrading to v1.0.0 is to install the tools and models
      used in your current environment into the new plugin environment, ensuring plugin
      installation is completed before database migration, run the following command:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: The final result will be saved in the plugins.jsonl file, which contains
      the plugin information for all workspaces in the current Dify instance.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: This command will download and install all necessary plugins into the latest
      environment.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: After completing the basic plugin installation process, follow the standard
      Dify upgrade procedure to update the database schema to the latest version.
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  - quote: '**Logical Optimization**: Integration of short-circuit evaluation to optimize
      logical conditions by @llinvokerl.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.0.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 9-apps-and-integrations-changes-in-1-0-0
  source_release: dify-2025-02-28-1-0-0-github-202962689-d5695ce1
  source_type: github_releases
  theme: apps-integrations
  title: 9 Apps and Integrations changes in 1.0.0
  type: change
related_changes:
- '[[Changes/Raycast/2025-02-26-raycast-focus-added-an-option-to-define-apps-websites-you-want-to-allow-instead|Raycast
  Focus: Added an option to define apps & websites you want to allow instead…]]'
- '[[Changes/Raycast/2025-02-26-introducing-ai-extensions|Introducing: AI Extensions]]'
- '[[Changes/Open WebUI/2025-02-27-2-apps-and-integrations-changes-in-v0-5-17|2 Apps
  and Integrations changes in v0.5.17]]'
source_release: '[[Releases/Dify/dify-2025-02-28-1-0-0-github-202962689-d5695ce1|dify-2025-02-28-1-0-0-github-202962689-d5695ce1]]'
source_type: github_releases
theme: apps-integrations
title: 9 Apps and Integrations changes in 1.0.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in 1.0.0

**Dify** · 2025-02-28 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.0.0) · from [[Releases/Dify/dify-2025-02-28-1-0-0-github-202962689-d5695ce1|v1.0.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugins are modular components that extend AI applications with plug-and-play simplicity. Now you can assemble external services and custom functionalities with your Dify apps effortlessly.

> We've developed a plugin system, a standard for Dify that lets users create plugins with the suffix .difypkg. By installing different plugin packages, you can add various capabilities to Dify.

> We've also introduced a new type of plugin called Extension, which is a custom service hosted within Dify. You can customize this service's code through plugins to handle external Webhook events.

> We've launched the Dify Marketplace, a centralized platform where plugins can be freely shared, allowing users to publish and download different plugins.

> The first step in upgrading to v1.0.0 is to install the tools and models used in your current environment into the new plugin environment, ensuring plugin installation is completed before database migration, run the following command:

> The final result will be saved in the plugins.jsonl file, which contains the plugin information for all workspaces in the current Dify instance.

> This command will download and install all necessary plugins into the latest environment.

> After completing the basic plugin installation process, follow the standard Dify upgrade procedure to update the database schema to the latest version.

> **Logical Optimization**: Integration of short-circuit evaluation to optimize logical conditions by @llinvokerl.

Source: https://github.com/langgenius/dify/releases/tag/1.0.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-02-28-4-model-support-changes-in-1-0-0|4 Model Support changes in 1.0.0]] · Model Support
- [[Changes/Dify/2025-02-28-we-ve-introduced-a-new-agent-node-in-workflow-where-the-agent-s-behavior-can-now|We've introduced a new Agent node in Workflow, where the agent's behavior can now…]] · Agent Mode
- [[Changes/Dify/2025-02-28-we-are-glad-to-share-that-we-re-launching-dify-v1-0-0|We are glad to share that we're launching Dify v1.0.0]] · Collaboration
- [[Changes/Dify/2025-02-28-2-developer-workflow-changes-in-1-0-0|2 Developer Workflow changes in 1.0.0]] · Developer Workflow
- [[Changes/Dify/2025-02-28-hnsw-vector-index-now-available-for-tidb-vector-store-with-tiflash-optimizing-ho|HNSW Vector Index]] · Other changes
- [[Changes/Dify/2025-02-28-13-other-changes-in-1-0-0|13 other changes in 1.0.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-02-27 · Open WebUI · [[Changes/Open WebUI/2025-02-27-2-apps-and-integrations-changes-in-v0-5-17|2 Apps and Integrations changes in v0.5.17]]
- Later: 2025-03-01 · Cline · [[Changes/Cline/2025-03-01-2-apps-and-integrations-changes-in-v3-5-0|2 Apps and Integrations changes in v3.5.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-02-28-b5cbb9&body=Card%3A%20Changes%2FDify%2F2025-02-28-9-apps-and-integrations-changes-in-1-0-0.md%0ACard%20ID%3A%20dify-2025-02-28-b5cbb9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.0.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->