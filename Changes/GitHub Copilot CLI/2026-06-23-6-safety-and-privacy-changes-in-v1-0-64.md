---
card_id: github-copilot-cli-2026-06-23-4aedc7
date: '2026-06-23'
description: 'GitHub Copilot CLI · 2026-06-23 · Safety and Privacy: 6 changes in 1.0.64
  — Add an option to bypass the sandbox for shell commands'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2156
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6cb2a136026ae3058f418741d5371894ff774ade0526d733be84ab2213ab5639
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-23-4aedc7
  comparison: ''
  date: '2026-06-23'
  description: 'GitHub Copilot CLI — 1.0.64: 6 Safety and Privacy changes'
  evidence:
  - quote: Add an option to bypass the sandbox for shell commands
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Treat 2>/dev/null redirects as read-only in shell safety prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Skip computer-use consent prompts in full allow-all sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Wait for the remote sandbox to start before opening the cloud session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Autopilot mode now auto-handles elicitation, ask_user, sampling, and permission
      prompts (including on launch with --autopilot and during continuation turns)
      instead of surfacing dialogs to the user
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  - quote: Make `/security-review` available to all users without --experimental
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.64
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-safety-and-privacy-changes-in-v1-0-64
  source_release: github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v1.0.64
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-06-22-fixed-agent-permission-issue-fixed-the-bug-where-changes-to-the-agent-security-m|Fixed
  Agent Permission Issue]]'
- '[[Changes/Google Antigravity/2026-06-22-model-quota-screen-and-agent-security-fixes|Model
  quota screen and agent security fixes]]'
- '[[Changes/Claude Code/2026-06-23-2-safety-and-privacy-changes-in-v2-1-187|2 Safety
  and Privacy changes in v2.1.187]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v1.0.64
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v1.0.64

**GitHub Copilot CLI** · 2026-06-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.64) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-23-v1-0-64-github-343650012-6d4aa4bd|1.0.64]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add an option to bypass the sandbox for shell commands

> Treat 2>/dev/null redirects as read-only in shell safety prompts

> Skip computer-use consent prompts in full allow-all sessions

> Wait for the remote sandbox to start before opening the cloud session

> Autopilot mode now auto-handles elicitation, ask_user, sampling, and permission prompts (including on launch with --autopilot and during continuation turns) instead of surfacing dialogs to the user

> Make `/security-review` available to all users without --experimental

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.64
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-23-clear-queued-tool-images-when-vision-is-disabled|Clear queued tool images when vision is disabled]] · Multimodal Input
- [[Changes/GitHub Copilot CLI/2026-06-23-9-editor-experience-changes-in-v1-0-64|9 Editor Experience changes in v1.0.64]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-23-2-account-and-access-changes-in-v1-0-64|2 Account and Access changes in v1.0.64]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-23-preserve-open-canvas-instances-across-reconnects-and-restarts|Preserve open canvas instances across reconnects and restarts]] · Files and Data
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
## Nearby in Safety and Privacy

- Earlier: 2026-06-23 · Claude Code · [[Changes/Claude Code/2026-06-23-2-safety-and-privacy-changes-in-v2-1-187|2 Safety and Privacy changes in v2.1.187]]
- Later: 2026-06-23 · Lovable · [[Changes/Lovable/2026-06-23-restrict-external-collaborators-without-enforcing-sso|Restrict external collaborators without enforcing SSO]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-23-4aedc7&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-23-6-safety-and-privacy-changes-in-v1-0-64.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-23-4aedc7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.64%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->