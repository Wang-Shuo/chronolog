---
card_id: github-copilot-cli-2026-05-05-16045a
date: '2026-05-05'
description: 'GitHub Copilot CLI · 2026-05-05 · Agent Mode: Add experimental MCP Tasks
  support: MCP tools with `taskSupport: "required"` run as non-blocking background…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1034
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 024dcc6516c4f511b3895ae8b873c72c2a9c2b49f7e928814d56dd636970710e
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  ai_generated: true
  card_id: github-copilot-cli-2026-05-05-16045a
  comparison: ''
  confidence: low
  date: '2026-05-05'
  description: 'GitHub Copilot CLI — 1.0.41: Add experimental MCP Tasks support: MCP
    tools with `taskSupport: "required"` run as non-blocking background agents trackable
    via `list_agents` and `read_agent` (available when experimental mode is enabled,
    e.g. via `/experimental on` or the `--experimental` flag)'
  evidence:
  - quote: 'Add experimental MCP Tasks support: MCP tools with `taskSupport: "required"`
      run as non-blocking background agents trackable via `list_agents` and `read_agent`
      (available when experimental mode is enabled, e.g. via `/experimental on` or
      the `--experimental` flag)'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.41
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: add-experimental-mcp-tasks-support-mcp-tools-with-tasksupport-required-run-as-no
  source_release: github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863
  source_type: github_releases
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  title: Add experimental MCP Tasks support
  type: change
related_changes:
- '[[Changes/Replit/2026-05-01-agent|Agent]]'
- '[[Changes/Claude Code/2026-05-04-auto-mode-when-the-classifier-can-t-evaluate-an-action-the-error-now-includes-a|Auto
  mode: when the classifier can''t evaluate an action, the error now includes…]]'
- '[[Changes/Gemini CLI/2026-05-05-feat-core-enhance-shell-command-validation-and-add-core-tools-allowlist-by-galz1|feat(core):
  enhance shell command validation and add core tools allowlist]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863|github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863]]'
source_type: github_releases
theme: agent-mode
title: Add experimental MCP Tasks support
type: change
---

<!-- chronolog:begin region="header" -->
# Add experimental MCP Tasks support

**GitHub Copilot CLI** · 2026-05-05 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.41) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-05-v1-0-41-github-318057614-7319e863|1.0.41]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Add experimental MCP Tasks support: MCP tools with `taskSupport: "required"` run as non-blocking background agents trackable via `list_agents` and `read_agent` (available when experimental mode is enabled, e.g. via `/experimental on` or the `--experimental` flag)
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.41
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-05-4-editor-experience-changes-in-v1-0-41|4 Editor Experience changes in v1.0.41]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-05-package-extraction-no-longer-crashes-on-windows-when-antivirus-or-filesystem-loc|Package extraction no longer crashes on Windows when antivirus or filesystem locks…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-05-cli-starts-faster-by-rendering-the-ui-immediately-while-authentication-resolves|CLI starts faster by rendering the UI immediately while authentication resolves…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-05-improve-stability-on-windows-by-working-around-a-v8-crash-in-node-24-x|Improve stability on Windows by working around a V8 crash in Node 24.x]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-05-05-2-interface-experience-changes-in-v1-0-41|2 Interface Experience changes in v1.0.41]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-05-2-apps-and-integrations-changes-in-v1-0-41|2 Apps and Integrations changes in v1.0.41]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-05-add-attachment-flag-in-non-interactive-p-prompt-mode-to-attach-files-images-or-n|Add --attachment flag in non-interactive (-p/--prompt) mode to attach files…]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-05-05-memory-tool-confirmation-prompt-now-shows-the-scope-repository-or-user-when-requ|Memory tool confirmation prompt now shows the scope (repository or user)…]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-05-7-other-changes-in-v1-0-41|7 other changes in v1.0.41]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-05 · Gemini CLI · [[Changes/Gemini CLI/2026-05-05-feat-core-enhance-shell-command-validation-and-add-core-tools-allowlist-by-galz1|feat(core): enhance shell command validation and add core tools allowlist]]
- Later: 2026-05-06 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-06-add-rubber-duck-agent-for-gpt-sessions-powered-by-claude-available-in-experiment|Add rubber-duck agent for GPT sessions, powered by Claude (available in /experimental)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-05-16045a&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-05-add-experimental-mcp-tasks-support-mcp-tools-with-tasksupport-required-run-as-no.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-05-16045a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.41%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->