---
card_id: claude-code-2026-05-15-23edf3
date: '2026-05-15'
description: 'Claude Code · 2026-05-15 · Safety and Privacy: 3 changes in v2.1.143
  — PowerShell tool now passes `-ExecutionPolicy Bypass`. Opt out with…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2117
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1b5346603a8a520ff0f295d54d548d48b7a7cc7f87b91eec359d0c92a5395c9c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-15-23edf3
  comparison: ''
  date: '2026-05-15'
  description: 'Claude Code — v2.1.143: 3 Safety and Privacy changes'
  evidence:
  - quote: PowerShell tool now passes `-ExecutionPolicy Bypass`. Opt out with `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  - quote: '`claude agents` accepts `--permission-mode`, `--model`, `--effort`, and
      `--dangerously-skip-permissions` to set defaults for sessions dispatched from
      the view'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  - quote: Fixed `claude agents --allow-dangerously-skip-permissions` defaulting dispatched
      sessions to bypass mode instead of making it available in the permission cycle
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-safety-and-privacy-changes-in-v2-1-143
  source_release: claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v2.1.143
  type: change
related_changes:
- '[[Changes/Notion/2026-05-13-meet-your-notion-workers|Meet your Notion Workers]]'
- '[[Changes/OpenCode/2026-05-13-core-preserve-layered-permission-rule-order-in-config-merges|Core
  Preserve layered permission rule order in config merges]]'
- '[[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|Added
  new claude agents flags]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v2.1.143
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v2.1.143

**Claude Code** · 2026-05-15 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.143) · from [[Releases/Claude Code/claude-code-2026-05-15-v2-1-143-github-323423445-53eb447c|v2.1.143]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> PowerShell tool now passes `-ExecutionPolicy Bypass`. Opt out with `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`

> `claude agents` accepts `--permission-mode`, `--model`, `--effort`, and `--dangerously-skip-permissions` to set defaults for sessions dispatched from the view

> Fixed `claude agents --allow-dangerously-skip-permissions` defaulting dispatched sessions to bypass mode instead of making it available in the permission cycle

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.143
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-15-bg-and-detach-now-preserve-allow-dangerously-skip-permissions-so-the-forked-work|/bg and ←-detach now preserve --allow-dangerously-skip-permissions…]] · Editor Experience
- [[Changes/Claude Code/2026-05-15-the-powershell-tool-is-now-enabled-by-default-on-windows-for-bedrock-vertex-and|The PowerShell tool is now enabled by default on Windows for Bedrock, Vertex…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-05-15-3-apps-and-integrations-changes-in-v2-1-143|3 Apps and Integrations changes in v2.1.143]] · Apps and Integrations
- [[Changes/Claude Code/2026-05-15-2-model-support-changes-in-v2-1-143|2 Model Support changes in v2.1.143]] · Model Support
- [[Changes/Claude Code/2026-05-15-2-developer-workflow-changes-in-v2-1-143|2 Developer Workflow changes in v2.1.143]] · Developer Workflow
- [[Changes/Claude Code/2026-05-15-2-agent-mode-changes-in-v2-1-143|2 Agent Mode changes in v2.1.143]] · Agent Mode
- [[Changes/Claude Code/2026-05-15-added-projected-context-cost-per-turn-and-per-invocation-token-estimates-to-the|Added projected context cost (per-turn and per-invocation token estimates)…]] · Pricing Model
- [[Changes/Claude Code/2026-05-15-claude-bg-dangerously-skip-permissions-now-persists-across-retire-wake|claude --bg --dangerously-skip-permissions now persists across retire→wake]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-14 · Claude Code · [[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|Added new claude agents flags]]
- Later: 2026-05-15 · v0 · [[Changes/v0/2026-05-15-added-docs-for-the-project-sandbox-terminal-commands-and-permission-modes|Added docs for the project sandbox , terminal commands , and permission modes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-15-23edf3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-15-3-safety-and-privacy-changes-in-v2-1-143.md%0ACard%20ID%3A%20claude-code-2026-05-15-23edf3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.143%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->