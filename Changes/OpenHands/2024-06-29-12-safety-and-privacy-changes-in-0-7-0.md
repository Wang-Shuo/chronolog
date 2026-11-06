---
card_id: openhands-2024-06-29-76d733
date: '2024-06-29'
description: 'OpenHands · 2024-06-29 · Safety and Privacy: 12 changes in 0.7.0 — Makefile
  setup-config to store the persist_sandbox boolean value by @mohammadkazem-sadoughi…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 440
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9d5240114252a2da20bbc08a5ac304a6a2672752d293f56a48eb85ddb72eb593
product: openhands
product_name: OpenHands
record:
  card_id: openhands-2024-06-29-76d733
  comparison: ''
  date: '2024-06-29'
  description: 'OpenHands — 0.7.0: 12 Safety and Privacy changes'
  evidence:
  - quote: Makefile setup-config to store the persist_sandbox boolean value by @mohammadkazem-sadoughi
      in https://github.com/OpenDevin/OpenDevin/pull/2304
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Dockerfile for make plugins sandbox-agnostic by @yufansong in https://github.com/OpenDevin/OpenDevin/pull/2409
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Make plugins sandbox-agnostic by @Shimada666 in https://github.com/OpenDevin/OpenDevin/pull/2101
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Always pull sandbox image by @SmartManoj in https://github.com/OpenDevin/OpenDevin/pull/2538
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: 'Evaluation time travel: build sandbox on the fly by @li-boxuan in https://github.com/OpenDevin/OpenDevin/pull/2491'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Enable test_agnostic_sandbox_jupyter_agentskills_fileop_pwd in CI by @li-boxuan
      in https://github.com/OpenDevin/OpenDevin/pull/2534
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Revert "Always pull sandbox image" by @Shimada666 in https://github.com/OpenDevin/OpenDevin/pull/2560
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Remove PERSIST_SANDBOX=true option by @mamoodi in https://github.com/OpenDevin/OpenDevin/pull/2591
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Default makefile for persist_sandbox to be false by @mamoodi in https://github.com/OpenDevin/OpenDevin/pull/2605
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: 'feat: allow SANDBOX_CONTAINER_IMAGEs built from opendevin/sandbox:main
      by @xverges in https://github.com/OpenDevin/OpenDevin/pull/2622'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: Added Documentation for How To Run Custom Sandbox Image by @sheunaluko
      in https://github.com/OpenDevin/OpenDevin/pull/2637
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  - quote: 'docs: Update custom_sandbox_guide.md by @xingyaoww in https://github.com/OpenDevin/OpenDevin/pull/2650'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openhands
  product_name: OpenHands
  slug: 12-safety-and-privacy-changes-in-0-7-0
  source_release: openhands-2024-06-29-0-7-0-github-163149742-cace6f1a
  source_type: github_releases
  theme: safety-privacy
  title: 12 Safety and Privacy changes in 0.7.0
  type: change
related_changes:
- '[[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf|Introducing
  ChatGPT Enterprise]]'
- '[[Changes/Cursor/2023-08-30-api-key-input-box-is-now-a-password-type|API Key input
  box is now a password type]]'
- '[[Changes/OpenHands/2024-06-04-2-safety-and-privacy-changes-in-0-6-1|2 Safety and
  Privacy changes in 0.6.1]]'
source_release: '[[Releases/OpenHands/openhands-2024-06-29-0-7-0-github-163149742-cace6f1a|openhands-2024-06-29-0-7-0-github-163149742-cace6f1a]]'
source_type: github_releases
theme: safety-privacy
title: 12 Safety and Privacy changes in 0.7.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Safety and Privacy changes in 0.7.0

**OpenHands** · 2024-06-29 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/OpenHands/OpenHands/releases/tag/0.7.0) · from [[Releases/OpenHands/openhands-2024-06-29-0-7-0-github-163149742-cace6f1a|0.7.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Makefile setup-config to store the persist_sandbox boolean value by @mohammadkazem-sadoughi in https://github.com/OpenDevin/OpenDevin/pull/2304

> Dockerfile for make plugins sandbox-agnostic by @yufansong in https://github.com/OpenDevin/OpenDevin/pull/2409

> Make plugins sandbox-agnostic by @Shimada666 in https://github.com/OpenDevin/OpenDevin/pull/2101

> Always pull sandbox image by @SmartManoj in https://github.com/OpenDevin/OpenDevin/pull/2538

> Evaluation time travel: build sandbox on the fly by @li-boxuan in https://github.com/OpenDevin/OpenDevin/pull/2491

> Enable test_agnostic_sandbox_jupyter_agentskills_fileop_pwd in CI by @li-boxuan in https://github.com/OpenDevin/OpenDevin/pull/2534

> Revert "Always pull sandbox image" by @Shimada666 in https://github.com/OpenDevin/OpenDevin/pull/2560

> Remove PERSIST_SANDBOX=true option by @mamoodi in https://github.com/OpenDevin/OpenDevin/pull/2591

> Default makefile for persist_sandbox to be false by @mamoodi in https://github.com/OpenDevin/OpenDevin/pull/2605

> feat: allow SANDBOX_CONTAINER_IMAGEs built from opendevin/sandbox:main by @xverges in https://github.com/OpenDevin/OpenDevin/pull/2622

> Added Documentation for How To Run Custom Sandbox Image by @sheunaluko in https://github.com/OpenDevin/OpenDevin/pull/2637

> docs: Update custom_sandbox_guide.md by @xingyaoww in https://github.com/OpenDevin/OpenDevin/pull/2650

Source: https://github.com/OpenHands/OpenHands/releases/tag/0.7.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenHands/2024-06-29-10-apps-and-integrations-changes-in-0-7-0|10 Apps and Integrations changes in 0.7.0]] · Apps and Integrations
- [[Changes/OpenHands/2024-06-29-5-search-and-browsing-changes-in-0-7-0|5 Search and Browsing changes in 0.7.0]] · Search and Browsing
- [[Changes/OpenHands/2024-06-29-3-agent-mode-changes-in-0-7-0|3 Agent Mode changes in 0.7.0]] · Agent Mode
- [[Changes/OpenHands/2024-06-29-2-model-support-changes-in-0-7-0|2 Model Support changes in 0.7.0]] · Model Support
- [[Changes/OpenHands/2024-06-29-add-links-to-a-feedback-sharing-site-by-neubig-in-https-github-com-opendevin-ope|Add links to a feedback sharing site]] · Collaboration
- [[Changes/OpenHands/2024-06-29-3-editor-experience-changes-in-0-7-0|3 Editor Experience changes in 0.7.0]] · Editor Experience
- [[Changes/OpenHands/2024-06-29-2-files-and-data-changes-in-0-7-0|2 Files and Data changes in 0.7.0]] · Files and Data
- [[Changes/OpenHands/2024-06-29-4-developer-workflow-changes-in-0-7-0|4 Developer Workflow changes in 0.7.0]] · Developer Workflow
- [[Changes/OpenHands/2024-06-29-2-mobile-and-desktop-changes-in-0-7-0|2 Mobile and Desktop changes in 0.7.0]] · Mobile and Desktop
- [[Changes/OpenHands/2024-06-29-159-other-changes-in-0-7-0|159 other changes in 0.7.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2024-06-04 · OpenHands · [[Changes/OpenHands/2024-06-04-2-safety-and-privacy-changes-in-0-6-1|2 Safety and Privacy changes in 0.6.1]]
- Later: 2024-07-05 · OpenHands · [[Changes/OpenHands/2024-07-05-2-safety-and-privacy-changes-in-0-7-1|2 Safety and Privacy changes in 0.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openhands-2024-06-29-76d733&body=Card%3A%20Changes%2FOpenHands%2F2024-06-29-12-safety-and-privacy-changes-in-0-7-0.md%0ACard%20ID%3A%20openhands-2024-06-29-76d733%0ASource%3A%20https%3A%2F%2Fgithub.com%2FOpenHands%2FOpenHands%2Freleases%2Ftag%2F0.7.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->