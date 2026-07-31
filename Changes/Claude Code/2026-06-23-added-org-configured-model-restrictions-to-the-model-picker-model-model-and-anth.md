---
card_id: claude-code-2026-06-23-761df2
date: '2026-06-23'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]'
  lag_days: 1261
  role: follower
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-19-changed-config-toggle-behavior-enter-and-space-both-change-the-selected-setting|claude-code-2026-06-19-fd6838]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 3ea18d979360a1aa7b2516793d5d6ca6f764ffc4a108eccda583c023fced6acc
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-17-improved-streaming-of-long-paragraphs-text-now-appears-line-by-line-instead-of-w|claude-code-2026-06-17-64f521]]'
- '[[Changes/Claude Code/2026-06-19-added-config-help-to-list-all-available-shorthand-keys-for-config-key-value|claude-code-2026-06-19-24d717]]'
- '[[Changes/Claude Code/2026-06-19-changed-config-toggle-behavior-enter-and-space-both-change-the-selected-setting|claude-code-2026-06-19-fd6838]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-23-v2-1-187-github-343665388-744f9775|claude-code-2026-06-23-v2-1-187-github-343665388-744f9775]]'
theme: interface-experience
type: change
---

# Added org-configured model restrictions to the model picker, `--model`, `/model`

<!-- chronolog:begin region="description" -->
Added org-configured model restrictions to the model picker, `--model`, `/model`, and `ANTHROPIC_MODEL`, with a "restricted by your organization's settings" message when a restricted model is selected
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added org-configured model restrictions to the model picker, `--model`, `/model`, and `ANTHROPIC_MODEL`, with a "restricted by your organization's settings" message when a restricted model is selected
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.187
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-19-changed-config-toggle-behavior-enter-and-space-both-change-the-selected-setting|claude-code-2026-06-19-fd6838]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: interface-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|chatgpt-2023-01-09-254e7f]]
- Lag Days: 1261
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes