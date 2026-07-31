---
card_id: claude-code-2026-05-15-4c3e5a
date: '2026-05-15'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1149
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-14-web-setup-warns-before-replacing-an-existing-github-app-connection|claude-code-2026-05-14-b7cb42]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: bdd04c7fc5589a663bcd736580043671dae83f95a333401aa94f0022ab8f35fd
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-14-plugins-with-a-root-level-skill-md-and-no-skills-subdirectory-are-now-surfaced-a|claude-code-2026-05-14-236f0b]]'
- '[[Changes/Claude Code/2026-05-14-the-plugin-details-pane-and-claude-plugin-details-now-show-lsp-servers-a-plugin|claude-code-2026-05-14-4abb1d]]'
- '[[Changes/Claude Code/2026-05-14-web-setup-warns-before-replacing-an-existing-github-app-connection|claude-code-2026-05-14-b7cb42]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c]]'
theme: apps-integrations
type: change
---

# Added plugin dependency enforcement: `claude plugin disable` now refuses when an

<!-- chronolog:begin region="description" -->
Added plugin dependency enforcement: `claude plugin disable` now refuses when another enabled plugin depends on the target (with a copy-pasteable disable-chain hint), and `claude plugin enable` force-enables transitive dependencies
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added plugin dependency enforcement: `claude plugin disable` now refuses when another enabled plugin depends on the target (with a copy-pasteable disable-chain hint), and `claude plugin enable` force-enables transitive dependencies
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-14-web-setup-warns-before-replacing-an-existing-github-app-connection|claude-code-2026-05-14-b7cb42]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1149
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes