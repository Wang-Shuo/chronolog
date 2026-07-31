---
card_id: claude-code-2026-07-24-89a3e1
date: '2026-07-24'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  lag_days: 1195
  role: follower
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-07-22-fixed-agent-frontmatter-hooks-running-from-untrusted-folders-hooks-now-require-t|claude-code-2026-07-22-9528ae]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 5eb356369207e012f8a35f354428f303f07d6e6c2a53a9f886fb75a8f7e46fce
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-07-22-improved-auto-mode-the-dangerous-rm-background-and-suspicious-windows-path-check|claude-code-2026-07-22-56473f]]'
- '[[Changes/Claude Code/2026-07-22-fixed-agent-frontmatter-hooks-running-from-untrusted-folders-hooks-now-require-t|claude-code-2026-07-22-9528ae]]'
- '[[Changes/ChatGPT/2026-07-23-health-is-built-with-layered-privacy-and-security-safeguards-connected-medical-r|chatgpt-2026-07-23-4a5fd5]]'
source_release: '[[Releases/Claude Code/claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233|claude-code-2026-07-24-v2-1-219-github-359412713-6c14d233]]'
theme: safety-privacy
type: change
---

# Added `sandbox.network.strictAllowlist` setting to deny non-allowlisted hosts fo

<!-- chronolog:begin region="description" -->
Added `sandbox.network.strictAllowlist` setting to deny non-allowlisted hosts for sandboxed commands without prompting
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `sandbox.network.strictAllowlist` setting to deny non-allowlisted hosts for sandboxed commands without prompting
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.219
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-07-22-fixed-agent-frontmatter-hooks-running-from-untrusted-folders-hooks-now-require-t|claude-code-2026-07-22-9528ae]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1195
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes