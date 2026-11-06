---
card_id: gemini-cli-2025-08-14-4336ff
date: '2025-08-14'
description: 'Gemini CLI · 2025-08-14 · Reliability and Performance: 6 changes in
  Release v0.1.21 — Run model availability check in the background to speed up startup
  by…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 973
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c1f8a515fedd221b43cf97d0da93f12b01f1936a6a0ead178d2b4101b3fba128
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-08-14-4336ff
  comparison: ''
  date: '2025-08-14'
  description: 'Gemini CLI — Release v0.1.21: 6 Reliability and Performance changes'
  evidence:
  - quote: Run model availability check in the background to speed up startup by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/4256
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'perf(core): parallelize bfsFileSearch for 40% faster CLI startup by @scato3
      in https://github.com/google-gemini/gemini-cli/pull/5185'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'perf(core): implement parallel file processing for 74% performance improvement
      by @Han5991 in https://github.com/google-gemini/gemini-cli/pull/4763'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(core, cli): Introduce high-performance FileSearch engine by @brychanrobot
      in https://github.com/google-gemini/gemini-cli/pull/5136'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(telemetry): Prevent memory leak in ClearcutLogger by @galz10 in https://github.com/google-gemini/gemini-cli/pull/5734'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Add --experimental-cli to speed up prettier formatting. by @cornmander
      in https://github.com/google-gemini/gemini-cli/pull/5999
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 6-reliability-and-performance-changes-in-v0-1-21
  source_release: gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa
  source_type: github_releases
  theme: reliability-performance
  title: 6 Reliability and Performance changes in v0.1.21
  type: change
related_changes:
- '[[Changes/Cursor/2025-08-06-1-4-5-improved-performance|1.4.5: Improved performance]]'
- '[[Changes/Gemini CLI/2025-08-06-4-reliability-and-performance-changes-in-v0-1-18|4
  Reliability and Performance changes in v0.1.18]]'
- '[[Changes/Gemini CLI/2025-08-12-2-reliability-and-performance-changes-in-v0-1-19|2
  Reliability and Performance changes in v0.1.19]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa|gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa]]'
source_type: github_releases
theme: reliability-performance
title: 6 Reliability and Performance changes in v0.1.21
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Reliability and Performance changes in v0.1.21

**Gemini CLI** · 2025-08-14 · [[Themes/reliability-performance|Reliability and Performance]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21) · from [[Releases/Gemini CLI/gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa|Release v0.1.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Run model availability check in the background to speed up startup by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4256

> perf(core): parallelize bfsFileSearch for 40% faster CLI startup by @scato3 in https://github.com/google-gemini/gemini-cli/pull/5185

> perf(core): implement parallel file processing for 74% performance improvement by @Han5991 in https://github.com/google-gemini/gemini-cli/pull/4763

> feat(core, cli): Introduce high-performance FileSearch engine by @brychanrobot in https://github.com/google-gemini/gemini-cli/pull/5136

> feat(telemetry): Prevent memory leak in ClearcutLogger by @galz10 in https://github.com/google-gemini/gemini-cli/pull/5734

> Add --experimental-cli to speed up prettier formatting. by @cornmander in https://github.com/google-gemini/gemini-cli/pull/5999

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-08-14-39-developer-workflow-changes-in-v0-1-21|39 Developer Workflow changes in v0.1.21]] · Developer Workflow
- [[Changes/Gemini CLI/2025-08-14-7-agent-mode-changes-in-v0-1-21|7 Agent Mode changes in v0.1.21]] · Agent Mode
- [[Changes/Gemini CLI/2025-08-14-3-interface-experience-changes-in-v0-1-21|3 Interface Experience changes in v0.1.21]] · Interface Experience
- [[Changes/Gemini CLI/2025-08-14-feat-core-parse-multimodal-mcp-tool-responses-by-luccasparoni-in-https-github-co|feat(core): Parse Multimodal MCP Tool responses]] · Multimodal Input
- [[Changes/Gemini CLI/2025-08-14-6-context-window-changes-in-v0-1-21|6 Context Window changes in v0.1.21]] · Context Window
- [[Changes/Gemini CLI/2025-08-14-41-apps-and-integrations-changes-in-v0-1-21|41 Apps and Integrations changes in v0.1.21]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-08-14-2-mobile-and-desktop-changes-in-v0-1-21|2 Mobile and Desktop changes in v0.1.21]] · Mobile and Desktop
- [[Changes/Gemini CLI/2025-08-14-3-memory-and-personalization-changes-in-v0-1-21|3 Memory and Personalization changes in v0.1.21]] · Memory and Personalization
- [[Changes/Gemini CLI/2025-08-14-8-automation-and-scheduling-changes-in-v0-1-21|8 Automation and Scheduling changes in v0.1.21]] · Automation and Scheduling
- [[Changes/Gemini CLI/2025-08-14-document-certificate-issue-workaround-by-scidomino-in-https-github-com-google-ge|Document certificate issue workaround]] · Files and Data
- [[Changes/Gemini CLI/2025-08-14-7-account-and-access-changes-in-v0-1-21|7 Account and Access changes in v0.1.21]] · Account and Access
- [[Changes/Gemini CLI/2025-08-14-7-safety-and-privacy-changes-in-v0-1-21|7 Safety and Privacy changes in v0.1.21]] · Safety and Privacy
- [[Changes/Gemini CLI/2025-08-14-35-editor-experience-changes-in-v0-1-21|35 Editor Experience changes in v0.1.21]] · Editor Experience
- [[Changes/Gemini CLI/2025-08-14-28-model-support-changes-in-v0-1-21|28 Model Support changes in v0.1.21]] · Model Support
- [[Changes/Gemini CLI/2025-08-14-181-other-changes-in-v0-1-21|181 other changes in v0.1.21]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2025-08-12 · Gemini CLI · [[Changes/Gemini CLI/2025-08-12-2-reliability-and-performance-changes-in-v0-1-19|2 Reliability and Performance changes in v0.1.19]]
- Later: 2025-08-21 · Cursor · [[Changes/Cursor/2025-08-21-1-5-5-general-stability-improvements-and-bug-fixes-to-enhance-overall-applicatio|1.5.5: General stability improvements and bug fixes to enhance overall application…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-08-14-4336ff&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-08-14-6-reliability-and-performance-changes-in-v0-1-21.md%0ACard%20ID%3A%20gemini-cli-2025-08-14-4336ff%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.1.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->