---
card_id: github-copilot-cli-2026-11-06-cad093
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Pricing Model: 5 changes in 1.0.106
  — `copilot help billing` now says the footer shows the AI credits used in this session…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1422
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 108aafb1801622c2b069b2be7be5f3a243d216cd7977d16752a4d7ae175e0fc5
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-cad093
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 5 Pricing Model changes'
  evidence:
  - quote: '`copilot help billing` now says the footer shows the AI credits used in
      this session (nothing by default on the legacy billing platform), and that the
      `/statusline` `quota` item is off by default and `ai-used` is on.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The /model picker shows token prices in terminals narrower than 64 columns,
      and the dot leaders start right after each price label.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`--max-ai-credits` with `NaN`, `inf` or a number too large to represent
      now fails with an error that names the value you typed, instead of reporting
      it as "null".'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Increase default subagent concurrency for non-usage-based billing sessions.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Model picker no longer shows a Category column, leaving more space for
      model and pricing details.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-pricing-model-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: pricing-model
  title: 5 Pricing Model changes in v1.0.106
  type: change
related_changes:
- "[[Changes/Open WebUI/2026-11-03-context-compaction-and-prompt-caching-when-the-same-model-handles-the-conversati|\U0001F9E0
  Context compaction and prompt caching. When the same model handles…]]"
- '[[Changes/Dify/2026-11-04-3-pricing-model-changes-in-1-19-0|3 Pricing Model changes
  in 1.19.0]]'
- '[[Changes/OpenClaw/2026-11-05-avoids-restoring-cold-archived-conversations-just-to-refresh-usage-and-cost-repo|Avoids
  restoring cold archived conversations just to refresh usage and cost reports…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: pricing-model
title: 5 Pricing Model changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Pricing Model changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `copilot help billing` now says the footer shows the AI credits used in this session (nothing by default on the legacy billing platform), and that the `/statusline` `quota` item is off by default and `ai-used` is on.

> The /model picker shows token prices in terminals narrower than 64 columns, and the dot leaders start right after each price label.

> `--max-ai-credits` with `NaN`, `inf` or a number too large to represent now fails with an error that names the value you typed, instead of reporting it as "null".

> Increase default subagent concurrency for non-usage-based billing sessions.

> Model picker no longer shows a Category column, leaving more space for model and pricing details.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-11-05 · OpenClaw · [[Changes/OpenClaw/2026-11-05-avoids-restoring-cold-archived-conversations-just-to-refresh-usage-and-cost-repo|Avoids restoring cold archived conversations just to refresh usage and cost reports…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-cad093&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-5-pricing-model-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-cad093%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->