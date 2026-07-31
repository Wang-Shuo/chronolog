---
card_id: claude-code-2026-06-02-8214a8
date: '2026-06-02'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1160
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-05-06-improved-visual-consistency-in-slash-command-dialogs-and-login-upgrade-extra-usa|claude-code-2026-05-06-67e323]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 70c0465615a2a4ffbc4662606752dc155b365d081f1f6cf35a367dd24145652f
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-05-06-improved-visual-consistency-in-slash-command-dialogs-and-login-upgrade-extra-usa|claude-code-2026-05-06-67e323]]'
- '[[Changes/ChatGPT/2026-06-02-active-sessions-shows-sessions-known-through-session-management-including-chatgp|chatgpt-2026-06-02-4822a8]]'
- '[[Changes/ChatGPT/2026-06-02-log-out-of-individual-sessions-or-all-sessions-from-active-sessions|chatgpt-2026-06-02-a6ea70]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a|claude-code-2026-06-02-v2-1-160-github-332740156-03dd8b5a]]'
theme: account-access
type: change
---

# Added a prompt before writing to shell startup files (`.zshenv`, `.zlogin`, `.ba

<!-- chronolog:begin region="description" -->
Added a prompt before writing to shell startup files (`.zshenv`, `.zlogin`, `.bash_login`) and `~/.config/git/`, which could otherwise lead to unintended command execution
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a prompt before writing to shell startup files (`.zshenv`, `.zlogin`, `.bash_login`) and `~/.config/git/`, which could otherwise lead to unintended command execution
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.160
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-05-06-improved-visual-consistency-in-slash-command-dialogs-and-login-upgrade-extra-usa|claude-code-2026-05-06-67e323]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1160
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes