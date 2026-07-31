---
card_id: claude-code-2026-02-05-175f9f
date: '2026-02-05'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1050
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-01-30-vscode-enabled-claude-in-chrome-integration|claude-code-2026-01-30-fcf3b6]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a928038ad2d24fb593ed2e76a48a23ecdf3803dceaecbed454302c44abc00b33
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-01-23-changed-skills-without-additional-permissions-or-hooks-to-be-allowed-without-req|claude-code-2026-01-23-869c23]]'
- '[[Changes/Claude Code/2026-01-23-sdk-added-replay-of-queued-command-attachment-messages-as-sdkusermessagereplay-e|claude-code-2026-01-23-d838c0]]'
- '[[Changes/Claude Code/2026-01-30-vscode-enabled-claude-in-chrome-integration|claude-code-2026-01-30-fcf3b6]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-05-v2-1-32-github-283457817-0910feb0|claude-code-2026-02-05-v2-1-32-github-283457817-0910feb0]]'
theme: apps-integrations
type: change
---

# Skills defined in `.claude/skills/` within additional directories (`--add-dir`)

<!-- chronolog:begin region="description" -->
Skills defined in `.claude/skills/` within additional directories (`--add-dir`) are now loaded automatically.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Skills defined in `.claude/skills/` within additional directories (`--add-dir`) are now loaded automatically.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.32
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-01-30-vscode-enabled-claude-in-chrome-integration|claude-code-2026-01-30-fcf3b6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1050
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes