---
card_id: claude-code-2026-06-08-c60825
date: '2026-06-08'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]'
  lag_days: 1131
  role: follower
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|claude-code-2026-05-28-e3cabb]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 8bef69a5d6532a9d64af49de9663ab5c1ddcb014011efc09203858e487a8d4c4
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|claude-code-2026-05-28-e3cabb]]'
- '[[Changes/Cursor/2026-06-04-context-usage-report-in-canvas|cursor-2026-06-04-215f02]]'
- '[[Changes/Cursor/2026-06-04-this-release-introduces-design-mode-for-faster-canvas-editing-new-ways-to-unders|cursor-2026-06-04-434310]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d|claude-code-2026-06-08-v2-1-169-github-336158564-d513d69d]]'
theme: context-window
type: change
---

# Added `/cd` command to move a session to a new working directory without breakin

<!-- chronolog:begin region="description" -->
Added `/cd` command to move a session to a new working directory without breaking the prompt cache mid-session
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `/cd` command to move a session to a new working directory without breaking the prompt cache mid-session
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.169
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|claude-code-2026-05-28-e3cabb]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: context-window
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|cursor-2023-05-04-00d3b7]]
- Lag Days: 1131
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes