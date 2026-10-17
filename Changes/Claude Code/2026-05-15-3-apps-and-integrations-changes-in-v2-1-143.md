---
card_id: claude-code-2026-05-15-9570a4
date: '2026-05-15'
description: 'Claude Code · 2026-05-15 · Apps and Integrations: 3 changes in v2.1.143
  — Added plugin dependency enforcement: `claude plugin disable` now refuses when
  another…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1149
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 401d1679d81250ec6b303e453f96744b713d996893f597aa00ac501ab5fe1f35
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-15-9570a4
  comparison: ''
  date: '2026-05-15'
  description: 'Claude Code — v2.1.143: 3 Apps and Integrations changes'
  evidence:
  - quote: 'Added plugin dependency enforcement: `claude plugin disable` now refuses
      when another enabled plugin depends on the target (with a copy-pasteable disable-chain
      hint), and `claude plugin enable` force-enables transitive dependencies'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  - quote: '`claude agents` now accepts `--add-dir`, `--settings`, `--mcp-config`,
      and `--plugin-dir` and applies them to the dashboard and to background sessions
      dispatched from it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  - quote: '`/bg` now preserves `--mcp-config`, `--settings`, `--add-dir`, `--plugin-dir`,
      and `--strict-mcp-config`, so backgrounded sessions keep their MCP servers and
      settings across respawn.'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-143
  source_release: claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.143
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-13-2-apps-and-integrations-changes-in-v2-1-141|2
  Apps and Integrations changes in v2.1.141]]'
- '[[Changes/Cursor/2026-05-13-improved-mcp-auth-token-lifecycle-handling|Improved
  MCP auth token lifecycle handling]]'
- '[[Changes/Claude Code/2026-05-14-3-apps-and-integrations-changes-in-v2-1-142|3
  Apps and Integrations changes in v2.1.142]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.143
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.143

**Claude Code** · 2026-05-15 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.143) · from [[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|v2.1.143]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added plugin dependency enforcement: `claude plugin disable` now refuses when another enabled plugin depends on the target (with a copy-pasteable disable-chain hint), and `claude plugin enable` force-enables transitive dependencies

> `claude agents` now accepts `--add-dir`, `--settings`, `--mcp-config`, and `--plugin-dir` and applies them to the dashboard and to background sessions dispatched from it

> `/bg` now preserves `--mcp-config`, `--settings`, `--add-dir`, `--plugin-dir`, and `--strict-mcp-config`, so backgrounded sessions keep their MCP servers and settings across respawn.

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-15-bg-and-detach-now-preserve-allow-dangerously-skip-permissions-so-the-forked-work|/bg and ←-detach now preserve --allow-dangerously-skip-permissions…]] · Editor Experience
- [[Changes/Claude Code/2026-05-15-3-safety-and-privacy-changes-in-v2-1-143|3 Safety and Privacy changes in v2.1.143]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-15-the-powershell-tool-is-now-enabled-by-default-on-windows-for-bedrock-vertex-and|The PowerShell tool is now enabled by default on Windows for Bedrock, Vertex…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-05-15-2-model-support-changes-in-v2-1-143|2 Model Support changes in v2.1.143]] · Model Support
- [[Changes/Claude Code/2026-05-15-2-developer-workflow-changes-in-v2-1-143|2 Developer Workflow changes in v2.1.143]] · Developer Workflow
- [[Changes/Claude Code/2026-05-15-2-agent-mode-changes-in-v2-1-143|2 Agent Mode changes in v2.1.143]] · Agent Mode
- [[Changes/Claude Code/2026-05-15-added-projected-context-cost-per-turn-and-per-invocation-token-estimates-to-the|Added projected context cost (per-turn and per-invocation token estimates)…]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-14 · Claude Code · [[Changes/Claude Code/2026-05-14-3-apps-and-integrations-changes-in-v2-1-142|3 Apps and Integrations changes in v2.1.142]]
- Later: 2026-05-19 · Claude Code · [[Changes/Claude Code/2026-05-19-plugin-discover-and-browse-screens-now-show-a-plugin-s-commands-agents-skills-ho|/plugin Discover and Browse screens now show a plugin's commands, agents, skills…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-15-9570a4&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-15-3-apps-and-integrations-changes-in-v2-1-143.md%0ACard%20ID%3A%20claude-code-2026-05-15-9570a4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.143%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->