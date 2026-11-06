---
card_id: github-copilot-cli-2026-06-23-681cd3
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Reliability and Performance: Show
  per-model token totals in /usage and speed up large history scans'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1286
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 9cd8f2a1d11c19d090ecffc54ba2c70912609259bb9843090f578af37fce5b05
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  ai_generated: true
  card_id: github-copilot-cli-2026-06-23-681cd3
  comparison: ''
  confidence: low
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: Show per-model token totals in /usage
    and speed up large history scans'
  evidence:
  - quote: Show per-model token totals in /usage and speed up large history scans
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: show-per-model-token-totals-in-usage-and-speed-up-large-history-scans
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - model
    score: 50
    theme: model-support
  - matched_terms:
    - speed
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v1
  title: Show per-model token totals in /usage and speed up large history scans
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-06-18-easier-conversation-sharing-sharing-a-conversation-is-now-faster-with-a-one-clic|Easier
  conversation sharing]]'
- '[[Changes/Claude Code/2026-06-20-the-stream-stall-hint-now-reads-waiting-for-api-response-will-retry-in-instead-o|The
  stream-stall hint now reads "Waiting for API response · will retry in …" instead…]]'
- '[[Changes/Codex CLI/2026-06-22-2-reliability-and-performance-changes-in-rust-v0-142-0|2
  Reliability and Performance changes in rust-v0.142.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: reliability-performance
title: Show per-model token totals in /usage and speed up large history scans
type: change
---

<!-- chronolog:begin region="header" -->
# Show per-model token totals in /usage and speed up large history scans

**GitHub Copilot CLI** · 2026-06-23 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Show per-model token totals in /usage and speed up large history scans
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.64
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-23-clear-queued-tool-images-when-vision-is-disabled|Clear queued tool images when vision is disabled]] · Multimodal Input
- [[Changes/GitHub Copilot CLI/2026-06-23-9-editor-experience-changes-in-v1-0-64|9 Editor Experience changes in v1.0.64]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-2-account-and-access-changes-in-v1-0-64|2 Account and Access changes in v1.0.64]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-open-canvas-instances-across-reconnects-and-restarts|Preserve open canvas instances across reconnects and restarts]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-markdown-blockquotes-in-share-exports|Preserve Markdown blockquotes in /share exports]] · Collaboration
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
## Nearby in Reliability and Performance

- Earlier: 2026-06-22 · Codex CLI · [[Changes/Codex CLI/2026-06-22-2-reliability-and-performance-changes-in-rust-v0-142-0|2 Reliability and Performance changes in rust-v0.142.0]]
- Later: 2026-06-24 · Claude Code · [[Changes/Claude Code/2026-06-24-reduced-long-session-memory-growth-from-terminal-output-cache|Reduced long-session memory growth from terminal output cache]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-681cd3&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-show-per-model-token-totals-in-usage-and-speed-up-large-history-scans.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-681cd3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->