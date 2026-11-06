---
card_id: github-copilot-cli-2026-06-23-100cd4
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Editor Experience: 9 changes in 1.0.64
  — Content exclusion no longer blocks every file when the rules service is unreachable…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1197
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e4a76e017c02ab96249b290ac69b1d53d5c356bb3466e21faa16b2338eb37269
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-23-100cd4
  comparison: ''
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: 9 Editor Experience changes'
  evidence:
  - quote: Content exclusion no longer blocks every file when the rules service is
      unreachable (offline or a transient network error). Access is allowed until
      rules can be fetched and retried in the background, matching the editor's behavior.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: /diff shows a session diff of Copilot's changes in non-git folders
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Normalize edited text to LF when opening prompts in an external editor
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Add tab completion for /agent names
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Sessions tab row label updates immediately when a session is renamed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Expand Windows home-directory paths in slash-command completion
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Allow /update to restart sessions started with copilot -r
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Click filenames in /diff tree to jump to that file's first change
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Wrap long lines in /diff view so content no longer truncates
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 9-editor-experience-changes-in-v1-0-64
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: editor-experience
  title: 9 Editor Experience changes in v1.0.64
  type: change
related_changes:
- '[[Changes/Windsurf/2026-06-16-removed-the-explain-sparkle-button-from-the-editor-breadcrumbs|Removed
  the Explain sparkle button from the editor breadcrumbs]]'
- '[[Changes/Windsurf/2026-06-16-agent-and-editor-modes|Agent and Editor modes]]'
- '[[Changes/Codex CLI/2026-06-22-29289-code-mode-preserve-initial-yield-at-completion-cconger|♯29289
  code-mode: preserve initial yield at completion @cconger]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: editor-experience
title: 9 Editor Experience changes in v1.0.64
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Editor Experience changes in v1.0.64

**GitHub Copilot CLI** · 2026-06-23 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Content exclusion no longer blocks every file when the rules service is unreachable (offline or a transient network error). Access is allowed until rules can be fetched and retried in the background, matching the editor's behavior.

> /diff shows a session diff of Copilot's changes in non-git folders

> Normalize edited text to LF when opening prompts in an external editor

> Add tab completion for /agent names

> Sessions tab row label updates immediately when a session is renamed

> Expand Windows home-directory paths in slash-command completion

> Allow /update to restart sessions started with copilot -r

> Click filenames in /diff tree to jump to that file's first change

> Wrap long lines in /diff view so content no longer truncates

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.64
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-23-clear-queued-tool-images-when-vision-is-disabled|Clear queued tool images when vision is disabled]] · Multimodal Input
- [[Changes/GitHub Copilot CLI/2026-06-23-2-account-and-access-changes-in-v1-0-64|2 Account and Access changes in v1.0.64]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-open-canvas-instances-across-reconnects-and-restarts|Preserve open canvas instances across reconnects and restarts]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-markdown-blockquotes-in-share-exports|Preserve Markdown blockquotes in /share exports]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans|Show per-model token totals in /usage and speed up large history scans]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-23-add-loop-alias-for-the-every-command|Add /loop alias for the /every command]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-23-add-mcp-registry-installation-for-browsing-and-installing-mcp-servers|Add /mcp registry installation for browsing and installing MCP servers]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-06-23-8-apps-and-integrations-changes-in-v1-0-64|8 Apps and Integrations changes in v1.0.64]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-23-7-model-support-changes-in-v1-0-64|7 Model Support changes in v1.0.64]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-23-6-agent-mode-changes-in-v1-0-64|6 Agent Mode changes in v1.0.64]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-23-11-interface-experience-changes-in-v1-0-64|11 Interface Experience changes in v1.0.64]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-15-developer-workflow-changes-in-v1-0-64|15 Developer Workflow changes in v1.0.64]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-23-4-projects-and-workspaces-changes-in-v1-0-64|4 Projects and Workspaces changes in v1.0.64]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-23-display-cache-write-pricing-for-models-that-omit-it|Display cache-write pricing for models that omit it]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-23-3-context-window-changes-in-v1-0-64|3 Context Window changes in v1.0.64]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-23-42-other-changes-in-v1-0-64|42 other changes in v1.0.64]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-06-22 · Codex CLI · [[Changes/Codex CLI/2026-06-22-29289-code-mode-preserve-initial-yield-at-completion-cconger|♯29289 code-mode: preserve initial yield at completion @cconger]]
- Later: 2026-06-24 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-24-add-a-copilot-skill-subcommand-and-a-skill-alias-for-skills-to-list-add-and-remo|Add a copilot skill subcommand (and a /skill alias for /skills) to list, add…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-100cd4&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-9-editor-experience-changes-in-v1-0-64.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-100cd4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->