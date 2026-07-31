---
card_id: claude-code-2026-06-04-d9a4ce
date: '2026-06-04'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1169
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|claude-code-2026-06-03-ede705]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a7952983210498232d5f061b2125a127b30aff736c6918e5dba7f9615337abd4
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-29-added-autocomplete-for-plugin-arguments-subcommands-installed-plugin-names-and-p|claude-code-2026-05-29-adc504]]'
- '[[Changes/Claude Code/2026-06-02-mcp-now-collapses-claude-ai-connectors-you-ve-never-signed-in-to-behind-a-show-u|claude-code-2026-06-02-187c5a]]'
- '[[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|claude-code-2026-06-03-ede705]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988|claude-code-2026-06-04-v2-1-163-github-334509318-c6b9f988]]'
theme: apps-integrations
type: change
---

# Hooks: Stop and SubagentStop hooks can now return `hookSpecificOutput.additional

<!-- chronolog:begin region="description" -->
Hooks: Stop and SubagentStop hooks can now return `hookSpecificOutput.additionalContext` to give Claude feedback and keep the turn going without being labeled a hook error
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Hooks: Stop and SubagentStop hooks can now return `hookSpecificOutput.additionalContext` to give Claude feedback and keep the turn going without being labeled a hook error
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.163
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-03-remote-control-now-shows-as-a-persistent-footer-pill-with-a-link-to-the-session|claude-code-2026-06-03-ede705]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1169
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes