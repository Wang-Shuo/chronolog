---
card_id: claude-code-2026-09-22-3ecbfe
date: '2026-09-22'
description: 'Claude Code · 2026-09-22 · Model Support: 5 changes in v2.1.280 — Added
  Claude Opus 5.5 (`claude-opus-5-5`), now the default Opus model — 1M context, $4/$20…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1352
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 40807bcd14c1bdf714b34a5d98ac2fcedab160b861398a3056c450839bb0bf35
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-22-3ecbfe
  comparison: ''
  date: '2026-09-22'
  description: 'Claude Code — v2.1.280: 5 Model Support changes'
  evidence:
  - quote: Added Claude Opus 5.5 (`claude-opus-5-5`), now the default Opus model —
      1M context, $4/$20 per Mtok with $0.20/Mtok cache reads
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: Changed the default model on Pro and Team Standard plans from Sonnet to
      Opus, matching Max, Team Premium, and Enterprise
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: Changed an effort level saved before `/effort` became per-model to no longer
      apply to newly released models such as Opus 5.5; they start at their default
      until you pick a level
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: Changed Opus 4.7, Opus 4.8 and Fable 5 to stop holding their launch-default
      effort over `/effort` in `-p` or the Agent SDK, a project, managed or `--settings`
      `effortLevel`, or a per-model level
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  - quote: '[VSCode] Added a Status dialog, with a typed `/status`, showing the session''s
      version, account, model and server details'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 5-model-support-changes-in-v2-1-280
  source_release: claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v2.1.280
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support
  changes in v2.1.274]]'
- '[[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added
  a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]]'
- '[[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed
  Fable to always appear in /model on the Anthropic API]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b|claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v2.1.280
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v2.1.280

**Claude Code** · 2026-09-22 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.280) · from [[Releases/Claude Code/claude-code-2026-09-22-v2-1-280-github-393879189-1cf5db2b|v2.1.280]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added Claude Opus 5.5 (`claude-opus-5-5`), now the default Opus model — 1M context, $4/$20 per Mtok with $0.20/Mtok cache reads

> Changed the default model on Pro and Team Standard plans from Sonnet to Opus, matching Max, Team Premium, and Enterprise

> Changed an effort level saved before `/effort` became per-model to no longer apply to newly released models such as Opus 5.5; they start at their default until you pick a level

> Changed Opus 4.7, Opus 4.8 and Fable 5 to stop holding their launch-default effort over `/effort` in `-p` or the Agent SDK, a project, managed or `--settings` `effortLevel`, or a per-model level

> [VSCode] Added a Status dialog, with a typed `/status`, showing the session's version, account, model and server details

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.280
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-22-8-apps-and-integrations-changes-in-v2-1-280|8 Apps and Integrations changes in v2.1.280]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-22-improved-cost-cache-miss-causes-to-name-thinking-mode-and-thinking-display-chang|Improved /cost cache-miss causes to name thinking mode and thinking display changes]] · Pricing Model
- [[Changes/Claude Code/2026-09-22-2-agent-mode-changes-in-v2-1-280|2 Agent Mode changes in v2.1.280]] · Agent Mode
- [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-22-5-interface-experience-changes-in-v2-1-280|5 Interface Experience changes in v2.1.280]] · Interface Experience
- [[Changes/Claude Code/2026-09-22-claude-tag-improved-the-github-banner-in-claude-tag-admin-settings-to-say-why-gi|Claude Tag Improved the GitHub banner in Claude Tag admin settings to say why…]] · Account and Access
- [[Changes/Claude Code/2026-09-22-vscode-changed-open-in-new-tab-to-open-claude-beside-the-editor-group-you-are-wo|VSCode Changed "Open in New Tab" to open Claude beside the editor group you…]] · Editor Experience
- [[Changes/Claude Code/2026-09-22-3-developer-workflow-changes-in-v2-1-280|3 Developer Workflow changes in v2.1.280]] · Developer Workflow
- [[Changes/Claude Code/2026-09-22-17-other-changes-in-v2-1-280|17 other changes in v2.1.280]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-18 · Claude Code · [[Changes/Claude Code/2026-09-18-changed-fable-to-always-appear-in-model-on-the-anthropic-api-it-is-greyed-out-on|Changed Fable to always appear in /model on the Anthropic API]]
- Later: 2026-09-23 · Claude Code · [[Changes/Claude Code/2026-09-23-improved-interactive-startup-time-git-reads-startup-telemetry-and-the-bedrock-ve|Improved interactive startup time]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-22-3ecbfe&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-22-5-model-support-changes-in-v2-1-280.md%0ACard%20ID%3A%20claude-code-2026-09-22-3ecbfe%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.280%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->