---
card_id: claude-code-2026-07-14-e7f86d
date: '2026-07-14'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-09-11-chatgpt-now-supports-a-limited-selection-of-languages-in-the-interface|chatgpt-2023-09-11-bac960]]'
  lag_days: 1037
  role: follower
  scope: tracked-products-only
  theme: accessibility-localization
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-03-improved-screen-reader-output-decorative-glyphs-are-now-hidden-transcript-symbol|claude-code-2026-07-03-347d88]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5b0f3f596a6178304a26a3dfa78e24338fdd2567f73612b96e240e64d9863cc3
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-04-added-support-for-full-width-zenkaku-space-input-from-japanese-ime-in-checkbox-s|claude-code-2026-02-04-0a49b9]]'
- '[[Changes/Claude Code/2026-06-12-session-titles-are-now-generated-in-the-language-of-your-conversation-set-the-la|claude-code-2026-06-12-f7d6f6]]'
- '[[Changes/Claude Code/2026-07-03-improved-screen-reader-output-decorative-glyphs-are-now-hidden-transcript-symbol|claude-code-2026-07-03-347d88]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-14-v2-1-208-github-353442054-2756b984|claude-code-2026-07-14-v2-1-208-github-353442054-2756b984]]'
theme: accessibility-localization
type: change
---

# Added screen reader mode: opt-in plain-text rendering for screen reader users. R

<!-- chronolog:begin region="description" -->
Added screen reader mode: opt-in plain-text rendering for screen reader users. Run `claude --ax-screen-reader`, set CLAUDE_AX_SCREEN_READER=1, or add "axScreenReader": true to settings.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added screen reader mode: opt-in plain-text rendering for screen reader users. Run `claude --ax-screen-reader`, set CLAUDE_AX_SCREEN_READER=1, or add "axScreenReader": true to settings.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.208
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-03-improved-screen-reader-output-decorative-glyphs-are-now-hidden-transcript-symbol|claude-code-2026-07-03-347d88]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: accessibility-localization
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-09-11-chatgpt-now-supports-a-limited-selection-of-languages-in-the-interface|chatgpt-2023-09-11-bac960]]
- Lag Days: 1037
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes