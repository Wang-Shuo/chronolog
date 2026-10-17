---
card_id: claude-code-2026-09-10-c2c77b
date: '2026-09-10'
description: 'Claude Code · 2026-09-10 · Apps and Integrations: 7 changes in v2.1.268
  — Added `--json` to `claude plugin install`, `uninstall`, `update`, `enable` and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1267
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1dd4905fee54917d117986c376b063bca83ac4564745725170e25f10c8e408d8
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-10-c2c77b
  comparison: ''
  date: '2026-09-10'
  description: 'Claude Code — v2.1.268: 7 Apps and Integrations changes'
  evidence:
  - quote: Added `--json` to `claude plugin install`, `uninstall`, `update`, `enable`
      and `disable`, and `errorDetails`/`noteDetails` to each row of `claude plugin
      list --json`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: 'Improved `--continue` / `--resume`: the conversation appears immediately
      instead of waiting for SessionStart hooks, and the first message no longer re-reads
      the whole transcript'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: 'Improved `/plugin`: installing, enabling or disabling a plugin now takes
      effect when you close the menu; `/reload-plugins` is no longer needed afterwards'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[VSCode] Changed the Manage plugins dialog to apply installs, enables,
      disables and uninstalls to open sessions without a restart'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[Claude Code on the web] Improved routine creation from a conversation:
      when the new routine has no connectors, Claude now says so and how to add them
      instead of only confirming it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[Claude Tag] Added a link from a Slack channel''s configure page back
      to the organization''s Claude in Slack admin settings'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  - quote: '[Claude Tag] Improved the message shown when your Claude account is in
      a different organization than the Slack workspace: it now explains how to connect
      the workspace to your org'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-apps-and-integrations-changes-in-v2-1-268
  source_release: claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v2.1.268
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-08-4-apps-and-integrations-changes-in-v2-1-265|4
  Apps and Integrations changes in v2.1.265]]'
- '[[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude
  Tag Added a "Use a custom connector" link to the preset connection forms…]]'
- '[[Changes/ChatGPT/2026-09-10-the-data-plugin-helps-you-analyze-connected-business-data-in-chatgpt-work-and-co|Data
  plugin in ChatGPT Work and Codex]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848|claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v2.1.268
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v2.1.268

**Claude Code** · 2026-09-10 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.268) · from [[Releases/Claude Code/claude-code-2026-09-10-v2-1-268-github-386532237-baa1a848|v2.1.268]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--json` to `claude plugin install`, `uninstall`, `update`, `enable` and `disable`, and `errorDetails`/`noteDetails` to each row of `claude plugin list --json`

> Improved `--continue` / `--resume`: the conversation appears immediately instead of waiting for SessionStart hooks, and the first message no longer re-reads the whole transcript

> Improved `/plugin`: installing, enabling or disabling a plugin now takes effect when you close the menu; `/reload-plugins` is no longer needed afterwards

> [VSCode] Changed the Manage plugins dialog to apply installs, enables, disables and uninstalls to open sessions without a restart

> [Claude Code on the web] Improved routine creation from a conversation: when the new routine has no connectors, Claude now says so and how to add them instead of only confirming it

> [Claude Tag] Added a link from a Slack channel's configure page back to the organization's Claude in Slack admin settings

> [Claude Tag] Improved the message shown when your Claude account is in a different organization than the Slack workspace: it now explains how to connect the workspace to your org

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.268
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-10-2-account-and-access-changes-in-v2-1-268|2 Account and Access changes in v2.1.268]] · Account and Access
- [[Changes/Claude Code/2026-09-10-2-interface-experience-changes-in-v2-1-268|2 Interface Experience changes in v2.1.268]] · Interface Experience
- [[Changes/Claude Code/2026-09-10-2-pricing-model-changes-in-v2-1-268|2 Pricing Model changes in v2.1.268]] · Pricing Model
- [[Changes/Claude Code/2026-09-10-added-browser-tab-icons-for-published-artifacts-chosen-by-claude-to-match-each-p|Added browser-tab icons for published artifacts, chosen by Claude to match each page]] · Editor Experience
- [[Changes/Claude Code/2026-09-10-2-memory-and-personalization-changes-in-v2-1-268|2 Memory and Personalization changes in v2.1.268]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-10-2-reliability-and-performance-changes-in-v2-1-268|2 Reliability and Performance changes in v2.1.268]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-10-code-review-added-a-note-under-the-still-open-findings-list-in-follow-up-reviews|Code Review Added a note under the still-open findings list in follow-up reviews]] · Developer Workflow
- [[Changes/Claude Code/2026-09-10-improved-auto-mode-denials-the-message-claude-receives-now-names-the-rule-that-b|Improved auto mode denials]] · Agent Mode
- [[Changes/Claude Code/2026-09-10-vscode-added-a-claude-code-focus-last-message-command-that-moves-keyboard-focus|VSCode Added a "Claude Code]] · Accessibility and Localization
- [[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety and Privacy changes in v2.1.268]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-10-2-model-support-changes-in-v2-1-268|2 Model Support changes in v2.1.268]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-10 · ChatGPT · [[Changes/ChatGPT/2026-09-10-the-data-plugin-helps-you-analyze-connected-business-data-in-chatgpt-work-and-co|Data plugin in ChatGPT Work and Codex]]
- Later: 2026-09-11 · ChatGPT · [[Changes/ChatGPT/2026-09-11-we-re-planning-to-retire-custom-gpts-across-chatgpt-plans-and-provide-a-migratio|Planned custom GPT retirement and migration to plugins]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-10-c2c77b&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-10-7-apps-and-integrations-changes-in-v2-1-268.md%0ACard%20ID%3A%20claude-code-2026-09-10-c2c77b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.268%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->