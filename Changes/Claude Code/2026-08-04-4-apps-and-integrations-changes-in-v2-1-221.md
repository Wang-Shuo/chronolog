---
card_id: claude-code-2026-08-04-3c53b8
date: '2026-08-04'
description: 'Claude Code · 2026-08-04 · Apps and Integrations: 4 changes in v2.1.221
  — Added warnings to `claude plugin validate` when a marketplace or plugin name would
  be…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1230
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3d8ad66ffebcb389e071e20ac7160e04db6c2b5248dddacd36943439ac52d283
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-04-3c53b8
  comparison: ''
  date: '2026-08-04'
  description: 'Claude Code — v2.1.221: 4 Apps and Integrations changes'
  evidence:
  - quote: Added warnings to `claude plugin validate` when a marketplace or plugin
      name would be rejected by Claude Desktop's managed marketplace sync
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Changed `/plugin install` to refresh a stale marketplace catalog and retry
      before reporting a plugin not found
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Changed plugins installed from `/plugin` to activate immediately when safe,
      instead of always requiring `/reload-plugins`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  - quote: Changed plugins to accept `"."` as a `skills` path, and the root-level
      `SKILL.md` validation error now suggests using the plugin root
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-221
  source_release: claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.221
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-07-29-we-re-beginning-to-roll-out-sign-in-with-chatgpt-across-select-plugins-and-partn|Sign
  in with ChatGPT]]'
- '[[Changes/Cursor/2026-08-03-cursor-can-now-read-write-and-act-across-your-google-workspace|Google
  Workspace Plugins]]'
- '[[Changes/ChatGPT/2026-08-04-three-new-plugins-for-chatgpt-work-and-codex-help-students-and-educators-work-wi-e7aee9|Three
  new plugins for ChatGPT Work and Codex help students and educators work…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.221
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.221

**Claude Code** · 2026-08-04 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.221) · from [[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|v2.1.221]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added warnings to `claude plugin validate` when a marketplace or plugin name would be rejected by Claude Desktop's managed marketplace sync

> Changed `/plugin install` to refresh a stale marketplace catalog and retry before reporting a plugin not found

> Changed plugins installed from `/plugin` to activate immediately when safe, instead of always requiring `/reload-plugins`

> Changed plugins to accept `"."` as a `skills` path, and the root-level `SKILL.md` validation error now suggests using the plugin root

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-04-improved-stats-panel-to-count-cache-tokens-in-its-token-totals-with-a-breakdown|Improved Stats panel to count cache tokens in its token totals, with a breakdown…]] · Context Window
- [[Changes/Claude Code/2026-08-04-changed-emoji-autocomplete-to-accept-common-alternate-shortcodes-like-thumbsup-t|Changed emoji autocomplete to accept common alternate shortcodes like :thumbsup:…]] · Editor Experience
- [[Changes/Claude Code/2026-08-04-3-model-support-changes-in-v2-1-221|3 Model Support changes in v2.1.221]] · Model Support
- [[Changes/Claude Code/2026-08-04-vscode-added-focus-view-a-chat-menu-toggle-that-hides-tool-activity-behind-an-ex|VSCode Added Focus view]] · Interface Experience
- [[Changes/Claude Code/2026-08-04-3-developer-workflow-changes-in-v2-1-221|3 Developer Workflow changes in v2.1.221]] · Developer Workflow
- [[Changes/Claude Code/2026-08-04-changed-fast-mode-to-report-on-the-stream-when-usage-credits-run-out-mid-session|Changed fast mode to report on the stream when usage credits run out mid-session…]] · Pricing Model
- [[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety and Privacy changes in v2.1.221]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-04-3-other-changes-in-v2-1-221|3 other changes in v2.1.221]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-04 · ChatGPT · [[Changes/ChatGPT/2026-08-04-three-new-plugins-for-chatgpt-work-and-codex-help-students-and-educators-work-wi-e7aee9|Three new plugins for ChatGPT Work and Codex help students and educators work…]]
- Later: 2026-08-04 · Claude Code · [[Changes/Claude Code/2026-08-04-2-apps-and-integrations-changes-in-v2-1-222|2 Apps and Integrations changes in v2.1.222]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-04-3c53b8&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-04-4-apps-and-integrations-changes-in-v2-1-221.md%0ACard%20ID%3A%20claude-code-2026-08-04-3c53b8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.221%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->