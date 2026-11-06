---
card_id: gemini-cli-2025-08-14-c8151a
date: '2025-08-14'
description: 'Gemini CLI · 2025-08-14 · Automation and Scheduling: 8 changes in Release
  v0.1.21 — Introduce loop detection service that breaks simple loop by @SandyTao520
  in…'
diffusion:
  first_in_tracked: '[[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add
    data clean schedule]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 590
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 035001542868d29a940800b86d9f26b8fc2cf2cf3e06b80fd97164898e6e93eb
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-08-14-c8151a
  comparison: ''
  date: '2025-08-14'
  description: 'Gemini CLI — Release v0.1.21: 8 Automation and Scheduling changes'
  evidence:
  - quote: Introduce loop detection service that breaks simple loop by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/3919
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Log the 2 types of loop detection by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4193
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Log prompt id when a loop is detected by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4765
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Implement hashing based loop detection by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4831
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Skip and reset loop checking around code blocks by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/5144
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: 'feat(docs): create new documentation for automation and triage by @mattKorwel
      in https://github.com/google-gemini/gemini-cli/pull/5363'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: Add a request queue to the tool scheduler by @jakemac53 in https://github.com/google-gemini/gemini-cli/pull/5845
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  - quote: skip loop check if it is currently inside a loop by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/6022
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 8-automation-and-scheduling-changes-in-v0-1-21
  source_release: gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa
  source_type: github_releases
  theme: automation-scheduling
  title: 8 Automation and Scheduling changes in v0.1.21
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-06-6-automation-and-scheduling-changes-in-v0-1-18|6
  Automation and Scheduling changes in v0.1.18]]'
- '[[Changes/Open WebUI/2025-08-09-customizable-floating-quick-actions-with-tool-support-take-full-control-of-your|✍️
  Customizable Floating Quick Actions with Tool Support]]'
- '[[Changes/Gemini CLI/2025-08-12-2-automation-and-scheduling-changes-in-v0-1-19|2
  Automation and Scheduling changes in v0.1.19]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa|gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa]]'
source_type: github_releases
theme: automation-scheduling
title: 8 Automation and Scheduling changes in v0.1.21
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Automation and Scheduling changes in v0.1.21

**Gemini CLI** · 2025-08-14 · [[Themes/automation-scheduling|Automation and Scheduling]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21) · from [[Releases/Gemini CLI/gemini-cli-2025-08-14-v0-1-21-github-239867721-f576cbaa|Release v0.1.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Introduce loop detection service that breaks simple loop by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/3919

> Log the 2 types of loop detection by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4193

> Log prompt id when a loop is detected by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4765

> Implement hashing based loop detection by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/4831

> Skip and reset loop checking around code blocks by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/5144

> feat(docs): create new documentation for automation and triage by @mattKorwel in https://github.com/google-gemini/gemini-cli/pull/5363

> Add a request queue to the tool scheduler by @jakemac53 in https://github.com/google-gemini/gemini-cli/pull/5845

> skip loop check if it is currently inside a loop by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/6022

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-08-14-39-developer-workflow-changes-in-v0-1-21|39 Developer Workflow changes in v0.1.21]] · Developer Workflow
- [[Changes/Gemini CLI/2025-08-14-7-agent-mode-changes-in-v0-1-21|7 Agent Mode changes in v0.1.21]] · Agent Mode
- [[Changes/Gemini CLI/2025-08-14-3-interface-experience-changes-in-v0-1-21|3 Interface Experience changes in v0.1.21]] · Interface Experience
- [[Changes/Gemini CLI/2025-08-14-6-reliability-and-performance-changes-in-v0-1-21|6 Reliability and Performance changes in v0.1.21]] · Reliability and Performance
- [[Changes/Gemini CLI/2025-08-14-feat-core-parse-multimodal-mcp-tool-responses-by-luccasparoni-in-https-github-co|feat(core): Parse Multimodal MCP Tool responses]] · Multimodal Input
- [[Changes/Gemini CLI/2025-08-14-6-context-window-changes-in-v0-1-21|6 Context Window changes in v0.1.21]] · Context Window
- [[Changes/Gemini CLI/2025-08-14-41-apps-and-integrations-changes-in-v0-1-21|41 Apps and Integrations changes in v0.1.21]] · Apps and Integrations
- [[Changes/Gemini CLI/2025-08-14-2-mobile-and-desktop-changes-in-v0-1-21|2 Mobile and Desktop changes in v0.1.21]] · Mobile and Desktop
- [[Changes/Gemini CLI/2025-08-14-3-memory-and-personalization-changes-in-v0-1-21|3 Memory and Personalization changes in v0.1.21]] · Memory and Personalization
- [[Changes/Gemini CLI/2025-08-14-document-certificate-issue-workaround-by-scidomino-in-https-github-com-google-ge|Document certificate issue workaround]] · Files and Data
- [[Changes/Gemini CLI/2025-08-14-7-account-and-access-changes-in-v0-1-21|7 Account and Access changes in v0.1.21]] · Account and Access
- [[Changes/Gemini CLI/2025-08-14-7-safety-and-privacy-changes-in-v0-1-21|7 Safety and Privacy changes in v0.1.21]] · Safety and Privacy
- [[Changes/Gemini CLI/2025-08-14-35-editor-experience-changes-in-v0-1-21|35 Editor Experience changes in v0.1.21]] · Editor Experience
- [[Changes/Gemini CLI/2025-08-14-28-model-support-changes-in-v0-1-21|28 Model Support changes in v0.1.21]] · Model Support
- [[Changes/Gemini CLI/2025-08-14-181-other-changes-in-v0-1-21|181 other changes in v0.1.21]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2025-08-12 · Gemini CLI · [[Changes/Gemini CLI/2025-08-12-2-automation-and-scheduling-changes-in-v0-1-19|2 Automation and Scheduling changes in v0.1.19]]
- Later: 2025-08-26 · Codex CLI · [[Changes/Codex CLI/2025-08-26-2692-do-not-schedule-frames-for-tui-draw-events-in-backtrack|♯2692 do not schedule frames for Tui::Draw events in backtrack]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-01-02 · Dify · [[Changes/Dify/2024-01-02-add-data-clean-schedule-by-johnjyong-in-https-github-com-langgenius-dify-pull-18|Add data clean schedule]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-08-14-c8151a&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-08-14-8-automation-and-scheduling-changes-in-v0-1-21.md%0ACard%20ID%3A%20gemini-cli-2025-08-14-c8151a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.1.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->