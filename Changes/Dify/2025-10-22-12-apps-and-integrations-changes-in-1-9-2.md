---
card_id: dify-2025-10-22-d7883b
date: '2025-10-22'
description: 'Dify · 2025-10-22 · Apps and Integrations: 12 changes in v1.9.2 - Sharper,
  Faster, and More Reliable — > A recent change has modernized the Dify integration…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 944
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2d1dccf89c95999a054eb860f175b82f29ec3cd3dfa953e64e0cc0a5f0ffbe59
product: dify
product_name: Dify
record:
  card_id: dify-2025-10-22-d7883b
  comparison: ''
  date: '2025-10-22'
  description: 'Dify — v1.9.2 - Sharper, Faster, and More Reliable: 12 Apps and Integrations
    changes'
  evidence:
  - quote: '> A recent change has modernized the Dify integration for Weaviate (see
      PR #25447 and related update in PR #26964). The upgrade switches the Weaviate
      Python client from v3 to v4 and raises the minimum required Weaviate server
      version to 1.24.0 or newer. With this update:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: '**Integrations & SDK**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: Improved DataSources with marketplace plugin integration and filtering
      *(by [@WTW0313](https://github.com/WTW0313) in [#26810](https://github.com/langgenius/dify/pull/26810))*
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: 'minor fix: improve check_upgradable_plugin_task.py by @NeatGuyCoding in
      https://github.com/langgenius/dify/pull/26468'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: Removes the 'extensions' directory from pyrightconfig.json and fixes …
      by @asukaminato0721 in https://github.com/langgenius/dify/pull/26512
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: removing horus eye and adding mcp icon by @jubinsoni in https://github.com/langgenius/dify/pull/25323
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: 'feat: migrate Python SDK to httpx with async/await support by @lyzno1
      in https://github.com/langgenius/dify/pull/26726'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: 'feat: enhance DataSources component with marketplace plugin integration
      and search filtering by @WTW0313 in https://github.com/langgenius/dify/pull/26810'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: Add timeout so any plugin daemon call (including the SSE path) that legitimately
      takes longer than 5s would right. by @Eric-Guo in https://github.com/langgenius/dify/pull/26852
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: 'feat: add Tencent Cloud APM tracing integration by @minimAluminiumalism
      in https://github.com/langgenius/dify/pull/25657'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: Remove unused after_request hooks from console API keys by @laipz8200 in
      https://github.com/langgenius/dify/pull/26896
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  - quote: 'feat(web): Add parameter rendering to MCP tool item component by @croatialu
      in https://github.com/langgenius/dify/pull/27099'
    source_release: https://github.com/langgenius/dify/releases/tag/1.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 12-apps-and-integrations-changes-in-1-9-2
  source_release: dify-2025-10-22-1-9-2-github-255984243-4bd350a7
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in 1.9.2
  type: change
related_changes:
- '[[Changes/Windsurf/2025-10-17-improved-diagnostics-for-third-party-extensions|Improved
  diagnostics for third party extensions]]'
- '[[Changes/GitHub Copilot CLI/2025-10-18-enabled-github-mcp-server-in-prompt-mode|Enabled
  GitHub MCP server in prompt mode]]'
- '[[Changes/ElevenLabs/2025-10-20-sdk-releases|SDK Releases]]'
source_release: '[[Releases/Dify/dify-2025-10-22-1-9-2-github-255984243-4bd350a7|dify-2025-10-22-1-9-2-github-255984243-4bd350a7]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in 1.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in 1.9.2

**Dify** · 2025-10-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.9.2) · from [[Releases/Dify/dify-2025-10-22-1-9-2-github-255984243-4bd350a7|v1.9.2 - Sharper, Faster, and More Reliable]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > A recent change has modernized the Dify integration for Weaviate (see PR #25447 and related update in PR #26964). The upgrade switches the Weaviate Python client from v3 to v4 and raises the minimum required Weaviate server version to 1.24.0 or newer. With this update:

> **Integrations & SDK**

> Improved DataSources with marketplace plugin integration and filtering *(by [@WTW0313](https://github.com/WTW0313) in [#26810](https://github.com/langgenius/dify/pull/26810))*

> minor fix: improve check_upgradable_plugin_task.py by @NeatGuyCoding in https://github.com/langgenius/dify/pull/26468

> Removes the 'extensions' directory from pyrightconfig.json and fixes … by @asukaminato0721 in https://github.com/langgenius/dify/pull/26512

> removing horus eye and adding mcp icon by @jubinsoni in https://github.com/langgenius/dify/pull/25323

> feat: migrate Python SDK to httpx with async/await support by @lyzno1 in https://github.com/langgenius/dify/pull/26726

> feat: enhance DataSources component with marketplace plugin integration and search filtering by @WTW0313 in https://github.com/langgenius/dify/pull/26810

> Add timeout so any plugin daemon call (including the SSE path) that legitimately takes longer than 5s would right. by @Eric-Guo in https://github.com/langgenius/dify/pull/26852

> feat: add Tencent Cloud APM tracing integration by @minimAluminiumalism in https://github.com/langgenius/dify/pull/25657

> Remove unused after_request hooks from console API keys by @laipz8200 in https://github.com/langgenius/dify/pull/26896

> feat(web): Add parameter rendering to MCP tool item component by @croatialu in https://github.com/langgenius/dify/pull/27099

Source: https://github.com/langgenius/dify/releases/tag/1.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2025-10-22-4-agent-mode-changes-in-1-9-2|4 Agent Mode changes in 1.9.2]] · Agent Mode
- [[Changes/Dify/2025-10-22-fix-web-app-permission-check-by-douxc-in-https-github-com-langgenius-dify-pull-2|Fix/web app permission check]] · Safety and Privacy
- [[Changes/Dify/2025-10-22-knowledge-pipeline-for-enterprise-by-garfielddai-in-https-github-com-langgenius|knowledge-pipeline-for-enterprise]] · Enterprise and Administration
- [[Changes/Dify/2025-10-22-improve-explicitly-delete-task-redis-key-on-completion-in-appqueuemanager-by-bla|improve: Explicitly delete task Redis key on completion in AppQueueManager]] · Editor Experience
- [[Changes/Dify/2025-10-22-chore-remove-pnpm-build-from-dev-setup-command-by-laipz8200-in-https-github-com|chore: remove pnpm build from dev-setup command]] · Developer Workflow
- [[Changes/Dify/2025-10-22-3-context-window-changes-in-1-9-2|3 Context Window changes in 1.9.2]] · Context Window
- [[Changes/Dify/2025-10-22-3-interface-experience-changes-in-1-9-2|3 Interface Experience changes in 1.9.2]] · Interface Experience
- [[Changes/Dify/2025-10-22-4-account-and-access-changes-in-1-9-2|4 Account and Access changes in 1.9.2]] · Account and Access
- [[Changes/Dify/2025-10-22-3-pricing-model-changes-in-1-9-2|3 Pricing Model changes in 1.9.2]] · Pricing Model
- [[Changes/Dify/2025-10-22-5-reliability-and-performance-changes-in-1-9-2|5 Reliability and Performance changes in 1.9.2]] · Reliability and Performance
- [[Changes/Dify/2025-10-22-8-model-support-changes-in-1-9-2|8 Model Support changes in 1.9.2]] · Model Support
- [[Changes/Dify/2025-10-22-139-other-changes-in-1-9-2|139 other changes in 1.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-10-20 · ElevenLabs · [[Changes/ElevenLabs/2025-10-20-sdk-releases|SDK Releases]]
- Later: 2025-10-22 · Gemini CLI · [[Changes/Gemini CLI/2025-10-22-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2025-10-22-d7883b&body=Card%3A%20Changes%2FDify%2F2025-10-22-12-apps-and-integrations-changes-in-1-9-2.md%0ACard%20ID%3A%20dify-2025-10-22-d7883b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->