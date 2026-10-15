---
card_id: claude-code-2026-06-02-fb9f22
date: '2026-06-02'
description: 'Claude Code · 2026-06-02 · Interface Experience: Fullscreen mode: clipboard
  now uses `wl-copy`/`xclip`/`xsel` on Linux when available, copies to both the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1240
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 0b35806fefb4c4196929a02376f29c086c733d663dcd6b62181d4e61d4917054
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-06-02-fb9f22
  comparison: ''
  date: '2026-06-02'
  description: 'Claude Code — v2.1.161: Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel`
    on Linux when available, copies to both the clipboard and PRIMARY selection for
    middle-click paste, and the "hold {key} for native selection" hint now shows the
    correct key per terminal'
  evidence:
  - quote: 'Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux
      when available, copies to both the clipboard and PRIMARY selection for middle-click
      paste, and the "hold {key} for native selection" hint now shows the correct
      key per terminal'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.161
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fullscreen-mode-clipboard-now-uses-wl-copy-xclip-xsel-on-linux-when-available-co
  source_release: claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa
  source_type: github_releases
  theme: interface-experience
  theme_matches:
  - matched_terms:
    - terminal
    score: 50
    theme: developer-workflow
  - matched_terms:
    - fullscreen
    score: 50
    theme: interface-experience
  theme_resolution: manual-semantic-rule-v1
  title: 'Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux…'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-21-prompt-history-no-longer-records-consecutive-duplicate-entries-recalling-a-promp|Prompt
  history no longer records consecutive duplicate entries]]'
- '[[Changes/Claude Code/2026-05-22-markdown-output-now-renders-gfm-task-list-checkboxes-todo-x-done-instead-of-plai|Markdown
  output now renders GFM task list checkboxes (-   todo / - x done)…]]'
- '[[Changes/Claude Code/2026-05-28-claude-agents-autocomplete-in-the-dispatch-input-now-suggests-native-slash-comma|claude
  agents: autocomplete in the dispatch input now suggests native slash…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa|claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa]]'
source_type: github_releases
theme: interface-experience
title: 'Fullscreen mode: clipboard now uses wl-copy/xclip/xsel on Linux…'
type: change
---

<!-- chronolog:begin region="header" -->
# Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux…

**Claude Code** · 2026-06-02 · [[Themes/interface-experience|Interface Experience]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.161) · from [[Releases/Claude Code/claude-code-2026-06-02-v2-1-161-github-333271302-7337e6fa|v2.1.161]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux when available, copies to both the clipboard and PRIMARY selection for middle-click paste, and the "hold {key} for native selection" hint now shows the correct key per terminal
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.161
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|/mcp now collapses claude.ai connectors you've never signed in to behind…]] · Apps and Integrations
- [[Changes/Claude Code/2026-06-02-parallel-tool-calls-a-failed-bash-command-no-longer-cancels-other-calls-in-the-s|Parallel tool calls]] · Developer Workflow
- [[Changes/Claude Code/2026-06-02-otel-resource-attributes-values-are-now-included-as-labels-on-metric-datapoints|OTEL_RESOURCE_ATTRIBUTES values are now included as labels on metric datapoints…]] · Collaboration
- [[Changes/Claude Code/2026-06-02-claude-agents-rows-now-show-done-total-before-the-detail-when-work-is-fanned-out|claude agents rows now show done/total before the detail when work is fanned out]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-claude-agents-autocomplete-in-the-dispatch-input-now-suggests-native-slash-comma|claude agents: autocomplete in the dispatch input now suggests native slash…]]
- Later: 2026-06-03 · Claude Code · [[Changes/Claude Code/2026-06-03-clicking-a-slash-command-in-the-autocomplete-menu-now-fills-it-into-your-prompt|Clicking a slash command in the autocomplete menu now fills it into your prompt…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-06-02-fb9f22&body=Card%3A%20Changes%2FClaude%20Code%2F2026-06-02-fullscreen-mode-clipboard-now-uses-wl-copy-xclip-xsel-on-linux-when-available-co.md%0ACard%20ID%3A%20claude-code-2026-06-02-fb9f22%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.161%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->