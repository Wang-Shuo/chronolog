---
card_id: claude-code-2026-05-28-8e54c2
date: '2026-05-28'
description: 'Claude Code · 2026-05-28 · Apps and Integrations: 4 changes in v2.1.154
  — Plugins can now declare `defaultEnabled: false` in `plugin.json` or a marketplace…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1162
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 075d7ed05dae0e224afaa64e3f8c609f4862d98b94600deb6def6b7984ff8cbc
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-28-8e54c2
  comparison: ''
  date: '2026-05-28'
  description: 'Claude Code — v2.1.154: 4 Apps and Integrations changes'
  evidence:
  - quote: 'Plugins can now declare `defaultEnabled: false` in `plugin.json` or a
      marketplace entry; enable them with `/plugin` or `claude plugin enable`. Dependencies
      of enabled plugins are still enabled automatically'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: The `/plugin` Discover tab now pins plugins whose relevance signals match
      the current directory with a "suggested for this directory" annotation
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: Stdio MCP server subprocesses now receive `CLAUDE_CODE_SESSION_ID` and
      `CLAUDECODE=1` in their environment
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  - quote: '`claude mcp list`/`get` now show unapproved `.mcp.json` servers as `⏸
      Pending approval` instead of auto-approving and connecting when output is piped'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-154
  source_release: claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.154
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-22-2-apps-and-integrations-changes-in-v2-1-149|2
  Apps and Integrations changes in v2.1.149]]'
- '[[Changes/Claude Code/2026-05-27-4-apps-and-integrations-changes-in-v2-1-152|4
  Apps and Integrations changes in v2.1.152]]'
- '[[Changes/Claude Code/2026-05-28-2-apps-and-integrations-changes-in-v2-1-153|2
  Apps and Integrations changes in v2.1.153]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9|claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.154
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.154

**Claude Code** · 2026-05-28 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.154) · from [[Releases/Claude Code/claude-code-2026-05-28-v2-1-154-github-330944050-782cdfc9|v2.1.154]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Plugins can now declare `defaultEnabled: false` in `plugin.json` or a marketplace entry; enable them with `/plugin` or `claude plugin enable`. Dependencies of enabled plugins are still enabled automatically

> The `/plugin` Discover tab now pins plugins whose relevance signals match the current directory with a "suggested for this directory" annotation

> Stdio MCP server subprocesses now receive `CLAUDE_CODE_SESSION_ID` and `CLAUDECODE=1` in their environment

> `claude mcp list`/`get` now show unapproved `.mcp.json` servers as `⏸ Pending approval` instead of auto-approving and connecting when output is piped

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.154
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-28-remote-control-autocomplete-now-shows-disconnect-remote-control-when-remote-cont|/remote-control autocomplete now shows "Disconnect Remote Control" when Remote…]] · Editor Experience
- [[Changes/Claude Code/2026-05-28-vscode-auto-mode-no-longer-requires-the-bypass-permissions-setting-to-appear-in|VSCode Auto mode no longer requires the bypass-permissions setting to appear…]] · Interface Experience
- [[Changes/Claude Code/2026-05-28-4-agent-mode-changes-in-v2-1-154|4 Agent Mode changes in v2.1.154]] · Agent Mode
- [[Changes/Claude Code/2026-05-28-5-model-support-changes-in-v2-1-154|5 Model Support changes in v2.1.154]] · Model Support
- [[Changes/Claude Code/2026-05-28-simplify-now-runs-a-cleanup-only-review-reuse-simplification-efficiency-altitude|/simplify now runs a cleanup-only review…]] · Developer Workflow
- [[Changes/Claude Code/2026-05-28-introducing-dynamic-workflows-ask-claude-to-create-a-workflow-and-it-orchestrate|Introducing dynamic workflows]] · Agent Mode
- [[Changes/Claude Code/2026-05-28-claude-now-reserves-the-multiple-choice-question-prompt-for-decisions-it-genuine|Claude now reserves the multiple-choice question prompt for decisions it genuinely…]] · Context Window
- [[Changes/Claude Code/2026-05-28-renamed-the-effort-slider-labels-from-speed-intelligence-to-faster-smarter-for-c|Renamed the /effort slider labels…]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-2-apps-and-integrations-changes-in-v2-1-153|2 Apps and Integrations changes in v2.1.153]]
- Later: 2026-05-29 · Claude Code · [[Changes/Claude Code/2026-05-29-4-apps-and-integrations-changes-in-v2-1-157|4 Apps and Integrations changes in v2.1.157]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-28-8e54c2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-28-4-apps-and-integrations-changes-in-v2-1-154.md%0ACard%20ID%3A%20claude-code-2026-05-28-8e54c2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.154%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->