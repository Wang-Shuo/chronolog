---
card_id: claude-code-2026-06-22-27079a
date: '2026-06-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1180
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|claude-code-2026-06-02-8214a8]]'
extractor_version: fallback-v2
impact: significant
machine_hash: c45e3118017d19407a4383b642a778e32b6dd84ea5e9f66e31cc6e5f4ad5f774
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-06-02-active-sessions-shows-sessions-known-through-session-management-including-chatgp|chatgpt-2026-06-02-4822a8]]'
- '[[Changes/ChatGPT/2026-06-02-log-out-of-individual-sessions-or-all-sessions-from-active-sessions|chatgpt-2026-06-02-a6ea70]]'
- '[[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|claude-code-2026-06-02-8214a8]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b|claude-code-2026-06-22-v2-1-186-github-343079393-93ecc37b]]'
theme: account-access
type: change
---

# Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate M

<!-- chronolog:begin region="description" -->
Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser` stdin redirect support for completing over SSH
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `claude mcp login <name>` and `claude mcp logout <name>` to authenticate MCP servers from the CLI without opening the interactive `/mcp` menu, with `--no-browser` stdin redirect support for completing over SSH
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.186
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-02-added-a-prompt-before-writing-to-shell-startup-files-zshenv-zlogin-bash-login-an|claude-code-2026-06-02-8214a8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1180
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes