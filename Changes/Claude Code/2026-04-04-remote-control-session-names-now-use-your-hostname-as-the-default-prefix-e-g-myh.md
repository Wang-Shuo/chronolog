---
card_id: claude-code-2026-04-04-121336
date: '2026-04-04'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]'
  lag_days: 1108
  role: follower
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-04-02-plugins-can-now-ship-executables-under-bin-and-invoke-them-as-bare-commands-from|claude-code-2026-04-02-ff5971]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 21588a4da06d838ceb401aca968d18695283678b06d49e8762bfe7d45dda9fd3
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-04-02-added-mcp-tool-result-persistence-override-via-meta-anthropic-maxresultsizechars|claude-code-2026-04-02-ba957b]]'
- '[[Changes/Claude Code/2026-04-02-added-disableskillshellexecution-setting-to-disable-inline-shell-execution-in-sk|claude-code-2026-04-02-cbe9e3]]'
- '[[Changes/Claude Code/2026-04-02-plugins-can-now-ship-executables-under-bin-and-invoke-them-as-bare-commands-from|claude-code-2026-04-02-ff5971]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5|claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5]]'
theme: apps-integrations
type: change
---

# Remote Control session names now use your hostname as the default prefix (e.g. `

<!-- chronolog:begin region="description" -->
Remote Control session names now use your hostname as the default prefix (e.g. `myhost-graceful-unicorn`), overridable with `--remote-control-session-name-prefix`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Remote Control session names now use your hostname as the default prefix (e.g. `myhost-graceful-unicorn`), overridable with `--remote-control-session-name-prefix`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.92
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-04-02-plugins-can-now-ship-executables-under-bin-and-invoke-them-as-bare-commands-from|claude-code-2026-04-02-ff5971]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: apps-integrations
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed|chatgpt-2023-03-23-86e5a9]]
- Lag Days: 1108
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes