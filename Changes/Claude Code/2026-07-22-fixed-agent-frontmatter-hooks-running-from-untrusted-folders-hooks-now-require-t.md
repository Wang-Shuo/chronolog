---
card_id: claude-code-2026-07-22-9528ae
date: '2026-07-22'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1193
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-22-improved-auto-mode-the-dangerous-rm-background-and-suspicious-windows-path-check|claude-code-2026-07-22-56473f]]'
extractor_version: fallback-v2
impact: paradigm-shift
machine_hash: a2f9d122a44c760ac52dbd50d1949847b8001e1d6c7ce9cccfda8ced5aac12af
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-20-fixed-powershell-tool-permission-validation-of-commands-containing-invisible-uni|claude-code-2026-07-20-e38a9f]]'
- '[[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|claude-code-2026-07-21-608ceb]]'
- '[[Changes/Claude Code/2026-07-22-improved-auto-mode-the-dangerous-rm-background-and-suspicious-windows-path-check|claude-code-2026-07-22-56473f]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4|claude-code-2026-07-22-v2-1-218-github-358276841-57d73db4]]'
theme: safety-privacy
type: change
---

# Fixed agent frontmatter hooks running from untrusted folders: hooks now require

<!-- chronolog:begin region="description" -->
Fixed agent frontmatter hooks running from untrusted folders: hooks now require the agent file's own folder to have accepted workspace trust
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed agent frontmatter hooks running from untrusted folders: hooks now require the agent file's own folder to have accepted workspace trust
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.218
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-22-improved-auto-mode-the-dangerous-rm-background-and-suspicious-windows-path-check|claude-code-2026-07-22-56473f]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1193
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes