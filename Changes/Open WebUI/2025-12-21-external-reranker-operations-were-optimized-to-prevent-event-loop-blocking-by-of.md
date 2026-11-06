---
card_id: open-webui-2025-12-21-b9ccc2
date: '2025-12-21'
description: 'Open WebUI · 2025-12-21 · Automation and Scheduling: ⚡ External reranker
  operations were optimized to prevent event loop blocking by offloading synchronous…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 719
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 15f910444860014c41d3b0a5077ecaf4b58c977b991a9081f3601c7993373b74
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-12-21-b9ccc2
  comparison: ''
  date: '2025-12-21'
  description: 'Open WebUI — v0.6.42: ⚡ External reranker operations were optimized
    to prevent event loop blocking by offloading synchronous HTTP requests to a thread
    pool using asyncio.to_thread(), eliminating application freezes during RAG reranking
    queries. [#20049](https://github.com/open-webui/open-webui/pull/20049), [#19900](https://github.com/open-webui/open-webui/issues/19900)'
  evidence:
  - quote: ⚡ External reranker operations were optimized to prevent event loop blocking
      by offloading synchronous HTTP requests to a thread pool using asyncio.to_thread(),
      eliminating application freezes during RAG reranking queries. [#20049](https://github.com/open-webui/open-webui/pull/20049),
      [#19900](https://github.com/open-webui/open-webui/issues/19900)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of
  source_release: open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9
  source_type: github_releases
  theme: automation-scheduling
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: ⚡ External reranker operations were optimized to prevent event loop blocking…
  type: change
related_changes:
- '[[Changes/Dify/2025-12-11-admin-api-keys-skip-csrf-automation-now-flows-smoother-than-espresso|Admin
  API Keys skip CSRF — automation now flows smoother than espresso]]'
- '[[Changes/ChatGPT/2025-12-17-tasks-let-you-set-up-automated-prompts-that-chatgpt-can-run-for-you-you-can-now-b3f799|Tasks
  let you set up automated prompts that ChatGPT can run for you]]'
- '[[Changes/Codex CLI/2025-12-18-7961-refactor-tui-event-loop-to-enable-dropping-recreating-crossterm-event-strea|♯7961
  refactor TUI event loop to enable dropping + recreating crossterm event stream]]'
source_release: '[[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9]]'
source_type: github_releases
theme: automation-scheduling
title: ⚡ External reranker operations were optimized to prevent event loop blocking…
type: change
---

<!-- chronolog:begin region="header" -->
# ⚡ External reranker operations were optimized to prevent event loop blocking…

**Open WebUI** · 2025-12-21 · [[Themes/automation-scheduling|Automation and Scheduling]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.42) · from [[Releases/Open WebUI/open-webui-2025-12-21-v0-6-42-github-272053915-b8e46ad9|v0.6.42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> ⚡ External reranker operations were optimized to prevent event loop blocking by offloading synchronous HTTP requests to a thread pool using asyncio.to_thread(), eliminating application freezes during RAG reranking queries. [#20049](https://github.com/open-webui/open-webui/pull/20049), [#19900](https://github.com/open-webui/open-webui/issues/19900)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.42
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-12-21-user-uploaded-images-are-now-automatically-converted-from-base64-to-actual-file|🖼️ User-uploaded images are now automatically converted from base64 to actual file…]] · Collaboration
- [[Changes/Open WebUI/2025-12-21-3-editor-experience-changes-in-v0-6-42|3 Editor Experience changes in v0.6.42]] · Editor Experience
- [[Changes/Open WebUI/2025-12-21-looking-for-an-enterprise-plan-https-docs-openwebui-com-enterprise-speak-with-ou| Looking for an Enterprise Plan((source link)]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-12-21-2-apps-and-integrations-changes-in-v0-6-42|2 Apps and Integrations changes in v0.6.42]] · Apps and Integrations
- [[Changes/Open WebUI/2025-12-21-6-files-and-data-changes-in-v0-6-42|6 Files and Data changes in v0.6.42]] · Files and Data
- [[Changes/Open WebUI/2025-12-21-7-reliability-and-performance-changes-in-v0-6-42|7 Reliability and Performance changes in v0.6.42]] · Reliability and Performance
- [[Changes/Open WebUI/2025-12-21-11-model-support-changes-in-v0-6-42|11 Model Support changes in v0.6.42]] · Model Support
- [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Safety and Privacy
- [[Changes/Open WebUI/2025-12-21-8-interface-experience-changes-in-v0-6-42|8 Interface Experience changes in v0.6.42]] · Interface Experience
- [[Changes/Open WebUI/2025-12-21-4-account-and-access-changes-in-v0-6-42|4 Account and Access changes in v0.6.42]] · Account and Access
- [[Changes/Open WebUI/2025-12-21-3-search-and-browsing-changes-in-v0-6-42|3 Search and Browsing changes in v0.6.42]] · Search and Browsing
- [[Changes/Open WebUI/2025-12-21-11-developer-workflow-changes-in-v0-6-42|11 Developer Workflow changes in v0.6.42]] · Developer Workflow
- [[Changes/Open WebUI/2025-12-21-2-multimodal-input-changes-in-v0-6-42|2 Multimodal Input changes in v0.6.42]] · Multimodal Input
- [[Changes/Open WebUI/2025-12-21-4-image-generation-changes-in-v0-6-42|4 Image Generation changes in v0.6.42]] · Image Generation
- [[Changes/Open WebUI/2025-12-21-2-voice-and-audio-changes-in-v0-6-42|2 Voice and Audio changes in v0.6.42]] · Voice and Audio
- [[Changes/Open WebUI/2025-12-21-channel-image-upload-handling-was-optimized-to-process-and-store-compressed-imag|🖼️ Channel image upload handling was optimized to process and store compressed…]] · Memory and Personalization
- [[Changes/Open WebUI/2025-12-21-28-other-changes-in-v0-6-42|28 other changes in v0.6.42]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2025-12-18 · Codex CLI · [[Changes/Codex CLI/2025-12-18-7961-refactor-tui-event-loop-to-enable-dropping-recreating-crossterm-event-strea|♯7961 refactor TUI event loop to enable dropping + recreating crossterm event stream]]
- Later: 2026-01-07 · Gemini CLI · [[Changes/Gemini CLI/2026-01-07-chore-core-remove-legacy-fallback-flags-and-migrate-loop-detection-by-adamfweidm|chore(core): remove legacy fallback flags and migrate loop detection]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-12-21-b9ccc2&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-12-21-external-reranker-operations-were-optimized-to-prevent-event-loop-blocking-by-of.md%0ACard%20ID%3A%20open-webui-2025-12-21-b9ccc2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.42%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->