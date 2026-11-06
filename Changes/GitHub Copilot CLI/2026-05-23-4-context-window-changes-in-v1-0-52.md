---
card_id: github-copilot-cli-2026-05-23-dda264
date: '2026-05-23'
description: 'GitHub Copilot CLI · 2026-05-23 · Context Window: 4 changes in 1.0.52
  — copilot --continue from a session''s saved directory now refreshes the saved branch
  and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1115
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6e161d5ab24a9b105d9e4ba2b135439e18f1003060d35a6c74c2df61ed0edacb
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-23-dda264
  comparison: ''
  date: '2026-05-23'
  description: 'GitHub Copilot CLI — 1.0.52: 4 Context Window changes'
  evidence:
  - quote: copilot --continue from a session's saved directory now refreshes the saved
      branch and git context instead of leaving them stale
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: Context window tier selection (default ~200K vs 1M tokens) is now enforced
      end-to-end, so picking a tier actually constrains compaction, truncation, and
      token display
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: Reasoning tokens display as a parenthetical on output token count in the
      token usage summary
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: /compact accepts optional focus instructions to shape the compaction summary
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-context-window-changes-in-v1-0-52
  source_release: github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4
  source_type: github_releases
  theme: context-window
  title: 4 Context Window changes in v1.0.52
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-21-5-context-window-changes-in-rust-v0-133-0|5 Context
  Window changes in rust-v0.133.0]]'
- '[[Changes/Claude Code/2026-05-22-improved-feedback-reports-to-include-the-conversation-that-happened-before-conte|Improved
  /feedback reports to include the conversation that happened before…]]'
- '[[Changes/Gemini CLI/2026-05-22-3-context-window-changes-in-v0-43-0|3 Context Window
  changes in v0.43.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4]]'
source_type: github_releases
theme: context-window
title: 4 Context Window changes in v1.0.52
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Context Window changes in v1.0.52

**GitHub Copilot CLI** · 2026-05-23 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.52) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|1.0.52]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> copilot --continue from a session's saved directory now refreshes the saved branch and git context instead of leaving them stale

> Context window tier selection (default ~200K vs 1M tokens) is now enforced end-to-end, so picking a tier actually constrains compaction, truncation, and token display

> Reasoning tokens display as a parenthetical on output token count in the token usage summary

> /compact accepts optional focus instructions to shape the compaction summary

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.52
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-23-automatically-prune-old-process-log-files-from-copilot-logs-at-startup-to-preven|Automatically prune old process log files from ~/.copilot/logs/ at startup…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-2-mobile-and-desktop-changes-in-v1-0-52|2 Mobile and Desktop changes in v1.0.52]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-23-2-account-and-access-changes-in-v1-0-52|2 Account and Access changes in v1.0.52]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-23-6-interface-experience-changes-in-v1-0-52|6 Interface Experience changes in v1.0.52]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-general-purpose-subagents-use-gpt-5-4-or-gpt-5-5-when-available|General-purpose subagents use GPT-5.4 or GPT-5.5 when available]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom agents support opt-in deferred tool loading via deferred-tool-loading…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-23-2-apps-and-integrations-changes-in-v1-0-52|2 Apps and Integrations changes in v1.0.52]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-23-3-pricing-model-changes-in-v1-0-52|3 Pricing Model changes in v1.0.52]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-05-23-2-safety-and-privacy-changes-in-v1-0-52|2 Safety and Privacy changes in v1.0.52]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-23-6-other-changes-in-v1-0-52|6 other changes in v1.0.52]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-05-22 · Gemini CLI · [[Changes/Gemini CLI/2026-05-22-3-context-window-changes-in-v0-43-0|3 Context Window changes in v0.43.0]]
- Later: 2026-05-26 · Codex CLI · [[Changes/Codex CLI/2026-05-26-5-context-window-changes-in-rust-v0-134-0|5 Context Window changes in rust-v0.134.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-23-dda264&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-23-4-context-window-changes-in-v1-0-52.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-23-dda264%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.52%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->