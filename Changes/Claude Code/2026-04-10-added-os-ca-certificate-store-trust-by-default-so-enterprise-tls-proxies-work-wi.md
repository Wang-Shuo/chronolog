---
card_id: claude-code-2026-04-10-efc05f
date: '2026-04-10'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]'
  lag_days: 988
  role: follower
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-07-changed-default-effort-level-from-medium-to-high-for-api-key-bedrock-vertex-foun|claude-code-2026-04-07-ff50d2]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: a7820decd7c6b46d7817bd86df6bcbf75ea2e92c70be215757d190680fd346ee
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/ChatGPT/2026-03-18-we-re-rolling-out-gpt-5-4-mini-in-chatgpt-gpt-5-4-mini-is-available-to-free-and|chatgpt-2026-03-18-64ffa1]]'
- '[[Changes/Claude Code/2026-04-04-added-forceremotesettingsrefresh-policy-setting-when-set-the-cli-blocks-startup|claude-code-2026-04-04-a0bc10]]'
- '[[Changes/Claude Code/2026-04-07-changed-default-effort-level-from-medium-to-high-for-api-key-bedrock-vertex-foun|claude-code-2026-04-07-ff50d2]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642|claude-code-2026-04-10-v2-1-101-github-307692858-ffcdf642]]'
theme: enterprise-admin
type: change
---

# Added OS CA certificate store trust by default, so enterprise TLS proxies work w

<!-- chronolog:begin region="description" -->
Added OS CA certificate store trust by default, so enterprise TLS proxies work without extra setup (set `CLAUDE_CODE_CERT_STORE=bundled` to use only bundled CAs)
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added OS CA certificate store trust by default, so enterprise TLS proxies work without extra setup (set `CLAUDE_CODE_CERT_STORE=bundled` to use only bundled CAs)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.101
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-07-changed-default-effort-level-from-medium-to-high-for-api-key-bedrock-vertex-foun|claude-code-2026-04-07-ff50d2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: enterprise-admin
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-07-27-enterprise-support|cursor-2023-07-27-4d0704]]
- Lag Days: 988
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes